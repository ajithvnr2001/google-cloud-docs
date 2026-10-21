---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/
title: gcloud alpha artifacts print-settings \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:56:35.136772+00:00
---

# gcloud alpha artifacts print-settings  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha artifacts print-settings Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha artifacts print-settings - print snippets to add to native tools settings files 
SYNOPSIS
    

`gcloud alpha artifacts print-settings` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The snippets provide a credentials placeholder and configurations to allow native tools to interact with Artifact Registry repositories. 
EXAMPLES
     To print a snippet to add a repository to the Gradle build.gradle file for repository my-repo in the current project, run: 
    
    
    [gcloud alpha artifacts print-settings gradle](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/gradle) --repository=my-repo

To print a snippet to add to the Maven pom.xml file for repository my-repo in the current project, run: 
    
    
    [gcloud alpha artifacts print-settings mvn](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/mvn) --repository=my-repo

To print a snippet to add to the npm .npmrc file for repository my-repo in the current project, run: 
    
    
    [gcloud alpha artifacts print-settings npm](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/npm) --repository=my-repo

To print a snippet to add to the Python .pypirc and pip.comf files for repository my-repo in the current project, run: 
    
    
    [gcloud alpha artifacts print-settings python](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/python) --repository=my-repo

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[apt](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/apt)`
     `(ALPHA)` Print settings to add to the sources.list.d directory. 
`[gradle](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/gradle)`
     `(ALPHA)` Print a snippet to add a repository to the Gradle build.gradle file. 
`[mvn](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/mvn)`
     `(ALPHA)` Print a snippet to add a Maven repository to the pom.xml file. 
`[npm](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/npm)`
     `(ALPHA)` Print credential settings to add to the .npmrc file. 
`[python](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/python)`
     `(ALPHA)` Print credential settings to add to the .pypirc and pip.conf files. 
`[yum](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/print-settings/yum)`
     `(ALPHA)` Print settings to add to the yum.repos.d directory. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud artifacts print-settings](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/print-settings)
    
    
    [gcloud beta artifacts print-settings](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/print-settings)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
