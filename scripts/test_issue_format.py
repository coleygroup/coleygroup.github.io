#!/usr/bin/env python3

import sys
import os

os.environ['GITHUB_TOKEN'] = 'fake-token-for-testing'
os.environ['GITHUB_REPOSITORY'] = 'test/repo'

from find_publications import PublicationFinder

class IssuePreviewFinder(PublicationFinder):
    def __init__(self):
        super().__init__()
    
    def create_combined_github_issue(self, publications):
        if not publications:
            return False
        
        count = len(publications)
        issue_title = f"Found {count} New Publication{'s' if count != 1 else ''}"
        
        labels = ['new-publications']
        
        issue_body = self.format_combined_issue_body(publications)
        
        print(f"=" * 80)
        print(f"COMBINED ISSUE PREVIEW")
        print(f"=" * 80)
        print(f"TITLE: {issue_title}")
        print(f"LABELS: {', '.join(labels)}")
        print(f"=" * 80)
        print("BODY:")
        print(issue_body)
        print(f"=" * 80)
        print()
        
        return True

def main():
    print("Testing GitHub Issue Preview...")
    print("This shows exactly what the combined issue would look like without actually creating it.\n")
    
    finder = IssuePreviewFinder()
    
    new_publications = finder.find_new_publications()
    
    if not new_publications:
        print("No new publications found - no issue would be created")
        return
    
    print(f"Found {len(new_publications)} new publications")
    print(f"A single GitHub issue would be created with all {len(new_publications)} publications:\n")
    
    finder.create_combined_github_issue(new_publications)
    
    print(f"SUMMARY:")
    print(f"  - Total new publications: {len(new_publications)}")
    print(f"  - GitHub issues that would be created: 1 (combined)")
    print(f"  - Sources: {', '.join(set(pub['source'] for pub in new_publications))}")
    print(f"  - Years: {', '.join(map(str, sorted(set(pub['year'] for pub in new_publications))))}")

if __name__ == "__main__":
    main()