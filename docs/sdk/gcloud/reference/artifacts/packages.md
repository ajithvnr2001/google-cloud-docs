---
url: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/packages/
title: gcloud artifacts packages \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:44.787751+00:00
---

# gcloud artifacts packages  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud artifacts packages Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud artifacts packages - manage Artifact Registry packages 
SYNOPSIS
    

`gcloud artifacts packages` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To list all packages in the current project and `artifacts/repository` and `artifacts/location` properties are set, run: 
    
    
    [gcloud artifacts packages list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/packages/list)

To list packages under repository my-repo in the current project and location, run: 
    
    
    [gcloud artifacts packages list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/packages/list) --repository=my-repo

To delete package `my-pkg` under repository my-repo in the current project and location, run: 
    
    
    [gcloud artifacts packages delete](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/packages/delete) my-pkg --repository=my-repo

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/packages/delete)`
     Delete an Artifact Registry package. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/packages/describe)`
     Describe an Artifact Registry package. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/packages/list)`
     List Artifact Registry packages. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/packages/update)`
     Update annotations on an Artifact Registry package. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha artifacts packages](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/packages)
    
    
    [gcloud beta artifacts packages](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/packages)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
