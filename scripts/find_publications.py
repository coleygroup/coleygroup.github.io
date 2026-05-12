#!/usr/bin/env python3

import os
import sys
import yaml
import requests
import json
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import Dict, List, Optional, Set
from urllib.parse import quote

class PublicationFinder:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.publications_file = os.path.join(self.base_dir, '_data', 'publications.yml')
        self.blacklist_file = os.path.join(self.base_dir, '_data', 'publications_blacklist.yml')
        
        self.orcid_id = "0000-0002-8271-8723"
        
        self.existing_publications = self.load_existing_publications()
        self.blacklist = self.load_blacklist()
        
        self.github_token = os.environ.get('GITHUB_TOKEN')
        self.github_repo = os.environ.get('GITHUB_REPOSITORY')
        
        if not self.github_token or not self.github_repo:
            print(" Missing GitHub token or repository environment variables")
            sys.exit(1)
    
    def load_existing_publications(self) -> List[Dict]:
        try:
            with open(self.publications_file, 'r') as f:
                content = f.read()
            
            # skip header template
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('- title:'):
                    publications_content = '\n'.join(lines[i:])
                    return yaml.safe_load(publications_content) or []
            return []
        except FileNotFoundError:
            print("  No existing publications file found")
            return []
    
    def load_blacklist(self) -> Dict:
        try:
            with open(self.blacklist_file, 'r') as f:
                blacklist_data = yaml.safe_load(f) or {}
                
                dois = blacklist_data.get('blacklisted_dois') or []
                arxiv_ids = blacklist_data.get('blacklisted_arxiv_ids') or []
                titles = blacklist_data.get('blacklisted_titles') or []
                
                return {
                    'dois': set(dois),
                    'arxiv_ids': set(arxiv_ids),
                    'titles': set(self.normalize_title(title) for title in titles)
                }
        except FileNotFoundError:
            print("  No blacklist file found")
            return {'dois': set(), 'arxiv_ids': set(), 'titles': set()}
    
    def normalize_title(self, title: str) -> str:
        normalized = title.lower()
        
        normalized = re.sub(r'[^\w]', '', normalized)
        
        return normalized
    
    def is_connor_coley_author(self, authors_str: str) -> bool:
        authors_lower = authors_str.lower()
        connor_variants = [
            'connor coley',
            'connor w coley',
            'connor w. coley',
            'c coley',
            'c. coley',
            'c w coley',
            'c. w. coley',
            'coley, connor',
            'coley, c',
            'coley, c.',
            'coley, c. w.',
            'coley, c w'
        ]
        return any(variant in authors_lower for variant in connor_variants)
    
    def is_blacklisted(self, pub: Dict) -> bool:
        if pub.get('doi') and pub['doi'] in self.blacklist['dois']:
            return True
        
        preprint = pub.get('preprint', '')
        if preprint:
            arxiv_id = preprint.replace('arXiv:', '').strip()
            if arxiv_id in self.blacklist['arxiv_ids']:
                return True
        
        normalized_title = self.normalize_title(pub.get('title', ''))
        if normalized_title in self.blacklist['titles']:
            return True
        
        return False
    
    def get_existing_identifiers(self) -> Dict[str, Set[str]]:
        identifiers = {'dois': set(), 'titles': set()}
        
        for pub in self.existing_publications:
            if 'doi' in pub:
                identifiers['dois'].add(pub['doi'])
            if 'url' in pub and 'doi.org' in pub['url']:
                doi_match = re.search(r'10\.\d+/[^\s&]+', pub['url'])
                if doi_match:
                    identifiers['dois'].add(doi_match.group())
            
            if 'title' in pub:
                normalized_title = self.normalize_title(pub['title'])
                identifiers['titles'].add(normalized_title)
        
        return identifiers
    
    def fetch_orcid_publications(self) -> List[Dict]:
        try:
            print(" Searching ORCID...")
            url = f"https://pub.orcid.org/v3.0/{self.orcid_id}/works"
            headers = {'Accept': 'application/json'}
            
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            works = response.json()
            publications = []
            
            for work in works.get('group', []):
                work_summary = work.get('work-summary', [{}])[0]
                put_code = work_summary.get('put-code')
                
                if put_code:
                    detail_url = f"https://pub.orcid.org/v3.0/{self.orcid_id}/work/{put_code}"
                    detail_response = requests.get(detail_url, headers=headers, timeout=15)
                    
                    if detail_response.status_code == 200:
                        detail_data = detail_response.json()
                        pub = self.parse_orcid_publication(detail_data)
                        if pub:
                            publications.append(pub)
            
            print(f" Found {len(publications)} ORCID publications")
            return publications
            
        except Exception as e:
            print(f" Error fetching ORCID publications: {e}")
            return []
    
    def parse_orcid_publication(self, work_data: Dict) -> Optional[Dict]:
        try:
            title = work_data.get('title', {}).get('title', {}).get('value', '')
            if not title:
                return None
            
            journal_title = ''
            if 'journal-title' in work_data:
                journal_title = work_data['journal-title'].get('value', '')
            
            pub_date = work_data.get('publication-date')
            year = None
            if pub_date:
                year = pub_date.get('year', {}).get('value')
            
            doi = None
            external_ids = work_data.get('external-ids', {}).get('external-id', [])
            for ext_id in external_ids:
                if ext_id.get('external-id-type') == 'doi':
                    doi = ext_id.get('external-id-value')
                    break
            
            if not doi:
                return None
            
            authors_str = self.get_crossref_authors(doi)
            
            if not self.is_connor_coley_author(authors_str):
                return None
            
            return {
                'title': title,
                'authors': authors_str,
                'journal': journal_title,
                'year': int(year) if year else datetime.now().year,
                'doi': doi,
                'url': f"https://doi.org/{doi}",
                'source': 'ORCID'
            }
            
        except Exception as e:
            return None
    
    def get_crossref_authors(self, doi: str) -> str:
        try:
            url = f"https://api.crossref.org/works/{doi}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            message = data.get('message', {})
            
            authors = []
            for author in message.get('author', []):
                given = author.get('given', '')
                family = author.get('family', '')
                if given and family:
                    authors.append(f"{given} {family}")
                elif family:
                    authors.append(family)
            
            return ', '.join(authors) if authors else 'Authors not available'
            
        except Exception:
            return 'Authors not available'
    
    def fetch_arxiv_publications(self) -> List[Dict]:
        try:
            print(" Searching ArXiv...")
            base_url = "http://export.arxiv.org/api/query"
            search_query = 'au:"Connor W. Coley" OR au:"Connor Coley" OR au:"C. W. Coley"'
            
            params = {
                'search_query': search_query,
                'start': 0,
                'max_results': 50,
                'sortBy': 'submittedDate',
                'sortOrder': 'descending'
            }
            
            response = requests.get(base_url, params=params, timeout=30)
            response.raise_for_status()
            
            root = ET.fromstring(response.content)
            ns = {'atom': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}
            entries = root.findall('atom:entry', ns)
            
            publications = []
            for entry in entries:
                pub = self.parse_arxiv_entry(entry, ns)
                if pub:
                    publications.append(pub)
            
            print(f" Found {len(publications)} ArXiv publications")
            return publications
            
        except Exception as e:
            print(f" Error fetching ArXiv publications: {e}")
            return []
    
    def parse_arxiv_entry(self, entry, ns) -> Optional[Dict]:
        try:
            title_elem = entry.find('atom:title', ns)
            if title_elem is None:
                return None
            title = title_elem.text.strip().replace('\n', ' ').replace('  ', ' ')
            
            authors = []
            for author in entry.findall('atom:author', ns):
                name_elem = author.find('atom:name', ns)
                if name_elem is not None:
                    authors.append(name_elem.text.strip())
            
            if not authors:
                return None
            
            authors_str = ', '.join(authors)
            
            if not self.is_connor_coley_author(authors_str):
                print(f"Skipping ArXiv paper (Connor not author): {title[:50]}...")
                return None
            
            id_elem = entry.find('atom:id', ns)
            if id_elem is None:
                return None
            
            arxiv_url = id_elem.text.strip()
            arxiv_id_match = re.search(r'(\d{4}\.\d{4,5})', arxiv_url)
            if not arxiv_id_match:
                return None
            
            arxiv_id = arxiv_id_match.group(1)
            
            published_elem = entry.find('atom:published', ns)
            if published_elem is not None:
                date_str = published_elem.text.strip()
                year = int(date_str[:4])
                publication_date = date_str[:10]  # YYYY-MM-DD format
            else:
                year = datetime.now().year
                publication_date = f"{year}-01-01"
            
            summary_elem = entry.find('atom:summary', ns)
            summary = summary_elem.text.strip() if summary_elem is not None else ''
            
            arxiv_doi = f"10.48550/arXiv.{arxiv_id}"
            
            pub_entry = {
                'title': title,
                'authors': authors_str,
                'journal': 'arxiv',
                'year': year,
                'publication_date': publication_date,
                'doi': arxiv_doi,
                'url': f"https://doi.org/{arxiv_doi}",
                'preprint': f"arXiv:{arxiv_id}",
                'preprint_url': f"https://arxiv.org/abs/{arxiv_id}",
                'preprint_site': 'arxiv',
                'preprint_year': year,
                'abstract': summary[:200] + "..." if len(summary) > 200 else summary,
                'source': 'ArXiv'
            }
            
            print(f"  Added ArXiv: {title[:50]}...")
            return pub_entry
            
        except Exception as e:
            print(f"  Error parsing ArXiv entry: {e}")
            return None
    
    def find_new_publications(self) -> List[Dict]:
        existing_identifiers = self.get_existing_identifiers()
        
        orcid_publications = self.fetch_orcid_publications()
        arxiv_publications = self.fetch_arxiv_publications()
        
        all_publications = orcid_publications + arxiv_publications
        
        seen_dois = set()
        seen_titles = set()
        deduplicated_publications = []
        
        for pub in all_publications:
            if pub.get('doi') and pub['doi'] in seen_dois:
                continue
            
            normalized_title = self.normalize_title(pub['title'])
            if normalized_title in seen_titles:
                continue
            
            if pub.get('doi'):
                seen_dois.add(pub['doi'])
            seen_titles.add(normalized_title)
            deduplicated_publications.append(pub)
        
        new_publications = []
        for pub in deduplicated_publications:
            if self.is_blacklisted(pub):
                print(f"Skipping blacklisted publication: {pub['title']}")
                continue
            
            if pub.get('doi') in existing_identifiers['dois']:
                continue
            
            normalized_title = self.normalize_title(pub['title'])
            if normalized_title in existing_identifiers['titles']:
                continue
            
            new_publications.append(pub)
        
        return new_publications
    
    def create_combined_github_issue(self, publications: List[Dict]) -> bool:
        try:
            if not publications:
                return False
            
            count = len(publications)
            issue_title = f" Found {count} New Publication{'s' if count != 1 else ''}"
            
            issue_body = self.format_combined_issue_body(publications)
            
            labels = ['new-publications']
            
            url = f"https://api.github.com/repos/{self.github_repo}/issues"
            headers = {
                'Authorization': f"token {self.github_token}",
                'Accept': 'application/vnd.github.v3+json'
            }
            
            data = {
                'title': issue_title,
                'body': issue_body,
                'labels': labels
            }
            
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            
            issue_data = response.json()
            print(f" Created issue #{issue_data['number']} with {count} publications")
            return True
            
        except Exception as e:
            print(f" Error creating combined issue: {e}")
            return False
    
    def format_combined_issue_body(self, publications: List[Dict]) -> str:
        count = len(publications)
        sources = list(set(pub['source'] for pub in publications))
        years = sorted(set(pub['year'] for pub in publications))
        
        body = f"""This automated script found {count} new publication{'s' if count != 1 else ''} for Connor Coley that {'are' if count != 1 else 'is'} not yet listed on the website.

##  {count} New Publications Found

**Sources:** {', '.join(sources)}  
**Years:** {', '.join(map(str, years))}  
**Found on:** {datetime.now().strftime('%Y-%m-%d')}

---

"""
        
        for i, pub in enumerate(publications, 1):
            body += f"""### {i}. {pub['title']}

**Authors:** {pub['authors']}  
**Journal/Venue:** {pub['journal']}  
**Year:** {pub['year']}  
**Source:** {pub['source']}  
**DOI:** {pub['doi']}  
**URL:** {pub['url']}  """
            
            if 'preprint' in pub:
                body += f"**Preprint:** {pub['preprint']}  \n"
                body += f"**Preprint URL:** {pub.get('preprint_url', 'N/A')}  \n"
            
            if 'publication_date' in pub:
                body += f"**Publication Date:** {pub['publication_date']}  \n"
            
            if 'abstract' in pub:
                body += f"\n**Abstract:** {pub['abstract']}\n"
            
            body += "\n---\n\n"
        
        body += """## Suggested YAML Entries

Copy and paste the following entries into `_data/publications.yml`:

```yaml
"""
        
        for pub in publications:
            body += f"""- title: "{pub['title']}"
  authors: {pub['authors']}
  journal: {pub['journal']}
  year: {pub['year']}
  doi: {pub['doi']}
  url: {pub['url']}"""
            
            if 'preprint' in pub:
                body += f"""
  preprint: {pub['preprint']}
  preprint_url: {pub.get('preprint_url', pub['url'])}
  preprint_site: arxiv
  preprint_year: {pub['year']}"""
            
            body += """
  themes:
    - # Add appropriate themes here

"""
        
        body += """```

## Review Checklist

- [ ] Verify all publication details are accurate
- [ ] Confirm Connor W. Coley is actually an author on each paper
- [ ] Check if all publications are appropriate for the website
- [ ] Assign relevant research themes to each publication
- [ ] Add approved publications to `_data/publications.yml`
- [ ] Close this issue when all publications have been processed

---
*This issue was automatically generated by the publication finder bot.*
"""
        
        return body
    
    def run(self):
        print(" Finding new publications...")
        
        new_publications = self.find_new_publications()
        
        if not new_publications:
            print(" No new publications found")
            return
        
        print(f" Found {len(new_publications)} new publications")
        
        if self.create_combined_github_issue(new_publications):
            print(f" Created GitHub issue with {len(new_publications)} new publications")
        else:
            print(" Failed to create GitHub issue")

if __name__ == "__main__":
    finder = PublicationFinder()
    finder.run()