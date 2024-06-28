# Coley Research Group Website

This is the repo for the website of the Coley Research group at MIT. It is modified on top of a Jekyll template developed by the Allan Lab.

## Contributor Guide

Any Coley Group members are free to make changes and additions to the website (such as adding/removing themselves to/from the "People" page) through this repo, pending approval. The existing templating combined with the following guide should hopefully make this process as painless as possible. Stylistic or template changes are also welcome but may require navigating Kevin's nightmarish templates and CSS.

### Local deployment

If you are making non-trivial changes (i.e. beyond just adding yourself to the "People" page), it is highly encouraged to locally deploy the website on your machine to preview the website before making a pull request. First, install Jekyll if you have not done so, following [the official guide](https://jekyllrb.com/docs/installation/#requirements) corresponding to your OS. 

Next, fork this repo and clone the forked repo to your local machine:
```bash
$ git clone https://github.com/{your_username}/coley.mit.edu.git
```

In your newly created folder, simply run the following to serve the website at `http://localhost:4000`.
```bash
$ jekyll serve
```

### Making changes and pull requests

Please create and checkout a new branch with the command
```bash
$ git checkout -b BRANCH_NAME
```
After you make and push your changes to the branch, perform a pull request so that your changes can be reviewed and merged into the main repo.

### Adding you or someone else to the "People" page

Adding yourself to the People page is very simple!
1. If you are a grad student / post-doc / research scientist, upload an image of yourself to `images/teampic/` with the format `{firstname}_{lastname}.[png|jpg|jpeg]`. **Please crop your image to a square**.
2. Navigate to the `_data/` folder and locate the `.yml` file that matches your position in the group (for instance, if you are a grad student, open `grad_students.yml`). 
3. Add all relevant information in the `.yml` file. 
    - For grad students / post-docs, this is `name` and `email` at minimum, with optional URLs provided in `twitter`, `linkedin`, and/or `website` fields.
    - For software developers this is `name` and optionally a `link` to a LinkedIn profile or personal website. 
    - For undergraduates, this is `name`, `school`, and an optional `link` to a LinkedIn profile or personal website. 

That's it! Go ahead and make a pull request when you are satisfied.