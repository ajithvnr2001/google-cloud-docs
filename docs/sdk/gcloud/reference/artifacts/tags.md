---
url: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/tags/
title: gcloud artifacts tags \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:16.011457+00:00
---

# gcloud artifacts tags  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud artifacts tags Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud artifacts tags - manage Artifact Registry tags 
SYNOPSIS
    

`gcloud artifacts tags` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create tag with the name `my-tag` for version `1.0.0` of package `my-pkg` in the current project with `artifacts/repository` and `artifacts/location` properties are set, run: 
    
    
    [gcloud artifacts tags create](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/tags/create) my-tag --package=my-pkg --version=1.0.0

To list all tags under package `my-pkg`, run: 
    
    
    [gcloud artifacts tags list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/tags/list) --package=my-pkg

To update tag `my-tag` from a different version to version `1.0.0` of package `my-pkg`, run: 
    
    
    [gcloud artifacts tags update](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/tags/update) my-tag --version=1.0.0 --package=my-pkg

To delete tag `my-tag` of package `my-pkg`, run: 
    
    
    [gcloud artifacts tags delete](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/tags/delete) my-tag --package=my-pkg

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/tags/create)`
     Create an Artifact Registry tag. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/tags/delete)`
     Delete an Artifact Registry tag. 
`[export](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/tags/export)`
     Export an Artifact Registry package version by tag. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/tags/list)`
     List Artifact Registry tags. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/tags/update)`
     Update an Artifact Registry tag. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha artifacts tags](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags)
    
    
    [gcloud beta artifacts tags](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/tags)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
