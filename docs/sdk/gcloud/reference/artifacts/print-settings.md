---
url: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/print-settings/
title: gcloud artifacts print-settings \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:11.472067+00:00
---

# gcloud artifacts print-settings  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/print-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud artifacts print-settings Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud artifacts print-settings - print snippets to add to native tools settings files 
SYNOPSIS
    

`gcloud artifacts print-settings` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     The snippets provide a credentials placeholder and configurations to allow native tools to interact with Artifact Registry repositories. 
EXAMPLES
     To print a snippet to add a repository to the Gradle build.gradle file for repository my-repo in the current project, run: 
    
    
    [gcloud artifacts print-settings gradle](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/print-settings/gradle) --repository=my-repo

To print a snippet to add to the Maven pom.xml file for repository my-repo in the current project, run: 
    
    
    [gcloud artifacts print-settings mvn](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/print-settings/mvn) --repository=my-repo

To print a snippet to add to the npm .npmrc file for repository my-repo in the current project, run: 
    
    
    [gcloud artifacts print-settings npm](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/print-settings/npm) --repository=my-repo

To print a snippet to add to the Python .pypirc and pip.comf files for repository my-repo in the current project, run: 
    
    
    [gcloud artifacts print-settings python](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/print-settings/python) --repository=my-repo

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[gradle](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/print-settings/gradle)`
     Print a snippet to add a repository to the Gradle build.gradle file. 
`[mvn](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/print-settings/mvn)`
     Print a snippet to add a Maven repository to the pom.xml file. 
`[npm](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/print-settings/npm)`
     Print credential settings to add to the .npmrc file. 
`[python](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/print-settings/python)`
     Print credential settings to add to the .pypirc and pip.conf files. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha artifacts print-settings](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings)
    
    
    [gcloud beta artifacts print-settings](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/print-settings)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
