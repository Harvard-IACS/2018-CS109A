Title: Lab 11 README
Category: labs
Slug: lab11/readme
Author: Rahul Dave
Date: 2018-12-02

# gpages

## Script for the Lab: Preamble

1. Set up a github account
2. Create a Public repository called `testgpages` with a `README.md` and a **Jekyll** `.gitignore`.
3. Download the github app and clone this repository down.
4. Also fork-clone/clone the repository https://github.com/rahuldave/gpages . 
5. Open both repositories side by side in the Finder (File Manager)
6. Make an edit to the `README.md` in `testgpages` and commit and push to understand the git flow.

## Web Pages, Version 1

1. Open a terminal from the github app for `testgpages`.
2. Copy the `notebooks` folder from `gpages` into `testgpages`
3. Using that terminal, convert the notebooks to html: 
   1. `jupyter nbconvert --output-dir . --to html notebooks/olives-eda.ipynb`
   2. `jupyter nbconvert --output-dir . --to html notebooks/olives-model.ipynb`
4. Copy `oldondex.html` from `gpages` to `index.html` in `testgpages`
5. Commit and push
6. Go to the hithub user interface for settings and enable a website on the `master` branch of `testgpages`.
7. Go to `https://username.github.io/testgpages/index.html` to see your website

## Web Site Version 2

1. Delete the html files in the main `testgpages` folder. We will generate markdown instead
2. From `gpages` copy the `_layouts` folder, `index.md`, and `_config.yml`.
3. Using the `testgpages` terminal, convert the notebooks into markdown using our custom template.
   1. `jupyter nbconvert --output-dir . --to markdown --template ../gpages/_support/markdown.tpl notebooks/olives-eda.ipynb`
   2. `jupyter nbconvert --output-dir . --to markdown --template ../gpages/_support/markdown.tpl notebooks/olives-model.ipynb`
4. Add **YAML** preambles and some TOC frontmatter to our markdown files
   1. `python ../gpages/_support/nbmd.py olives-eda.md` 
   2. `python ../gpages/_support/nbmd.py olives-model.md`
5. Edit the markdown files to add a YAML tag `nav_include: 1` and `nav_include: 2` respectively to the above markdown files.The 1 and 2 reflect the position on the navigation menu in the `default.html` template in `_layouts`.  
6. Commit and push everything
7. Go to the website in a bit to check the improvements

## Things for you to do

1. Hide some cells: see our `nbconvert` template to see how to do this.
2. Use another theme from the github defaults
3. ADVANCED:  use your own jekyll theme.

## More Info



- http://jmcglone.com/guides/github-pages/
