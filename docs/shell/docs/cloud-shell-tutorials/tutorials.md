---
url: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/tutorials/
title: Write tutorials in Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:25.053417+00:00
---

# Write tutorials in Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/tutorials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)



Send feedback 

#  Write tutorials in Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Shell supports building and launching tutorials to help users familiarize themselves with your project quickly and effectively.

A tutorial is a set of instructions written in Markdown. Cloud Shell creates in-context tutorials from these Markdown files by parsing the text into steps and substeps that are then displayed in a panel in Google Cloud console.

![A tutorial running in Cloud Shell](https://docs.cloud.google.com/static/shell/docs/images/cloudshelltutorial.png)

## Write tutorials

Tutorials are written in [CommonMark Markdown](http://commonmark.org/). Additional [Markdown extensions](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/markdown-extensions) are supported, as are directives, which include advanced functionality like [spotlighting features](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/directives-spotlights) and adding [inline icons](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/directives-layout#icons).

### Steps

When creating a tutorial, headings are important in determining its structure. To set the correct title, step headings, and underlying instructions, use the following hierarchy:

  * H1 (#) tags for the tutorial title. There should only be one H1 tag in a tutorial.
  * H2 (##) tags for a step title.
  * H3 (###) tags for a sub-step title.



Here is a sample Markdown file you can use to create a tutorial:
    
    
    # First tutorial
    
    ## First step
    
    Hello world
    
    ### Part 1
    
    Part one instructions.
    
    ### Part 2
    
    Part two instructions.
    
    ## Conclusion
    
    Done!
    

### Directives

Directives enable advanced functionality like spotlighting features and adding inline icons.

To add a directive, use the following format:
    
    
    <walkthrough-DIRECTIVE_NAME PARAMETER="PARAMETER_VALUE">
    </walkthrough-DIRECTIVE_NAME>
    

For example, if you'd like to use the directive `editor-open-file` and the parameter `filePath`, it would be written as follows:
    
    
    <walkthrough-editor-open-file filePath="test/hello.md">
    </walkthrough-editor-open-file>
    

For the available directives, refer to the [directives reference](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/directives-cloud-shell-editor).

## Launch tutorials in Cloud Shell

There are two ways to kickstart a tutorial in Cloud Shell:

  1. **Use the`cloudshell launch-tutorial` command**

Run the following `cloudshell` command in your [Cloud Shell session](https://ssh.cloud.google.com/cloudshell) to launch a tutorial from an existing Markdown file, `tutorial.md`:
         
         cloudshell launch-tutorial tutorial.md
         

Alternatively, you can use the `teachme` alias by running the following command in your [Cloud Shell session](https://ssh.cloud.google.com/cloudshell) to launch a tutorial from an existing file, `hello.md`:
         
         teachme hello.md
         

  2. **Use _Open in Cloud Shell_**

Alternatively, you can use the [_Open in Cloud Shell_](https://cloud.google.com/shell/docs/open-in-cloud-shell) feature to guide your users from a website, blog, or open source project to your tutorial hosted in a Git repository. The _Open in Cloud Shell_ feature allows for a `cloudshell_tutorial` parameter, which can be added to the end of the URL to specify the location of the source Markdown file in the repository. This means that the Markdown for a button linked to your tutorial would look like:
         
         [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://ssh.cloud.google.com/cloudshell/open**?cloudshell_git_repo= GIT_REPO_URL&cloudshell_tutorial=PATH_TO_MD_FILE**)
         




## Next steps

  * For a comprehensive list of tutorial-specific Markdown expressions, see the [Tutorial Markdown reference](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/markdown-extensions).
  * For guidelines on how to write effective tutorials, see the [Tutorial style guide](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/style-guide).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
