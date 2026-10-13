---
url: https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/
title: gcloud edge-cache \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:37.406237+00:00
---

# gcloud edge-cache  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud edge-cache Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud edge-cache - manage Media CDN resources 
SYNOPSIS
    

`gcloud edge-cache` `GROUP` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Manage Media CDN resources. 
EXAMPLES
     To list EdgeCacheService resources in the active Cloud Platform project, run: 
    
    
    [gcloud edge-cache services list](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/list)

To create an EdgeCacheOrigin resource named 'my-origin' that points to a Cloud Storage bucket, run: 
    
    
    [gcloud edge-cache origins create](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/origins/create) my-origin --origin-address="gs://bucket"

To import an EdgeCacheService resource configuration from a YAML definition, run: 
    
    
    [gcloud edge-cache services import](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/import) my-service --source=config.yaml

To describe an EdgeCacheKeyset resource named 'my-keyset', run: 
    
    
    [gcloud edge-cache keysets describe](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/describe) my-keyset

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[keysets](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/keysets)`
     Interact with and manage EdgeCacheKeyset resources. 
`[operations](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/operations)`
     Manage EdgeCache operations. 
`[origins](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/origins)`
     Interact with and manage EdgeCacheOrigin resources. 
`[services](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services)`
     Interact with and manage EdgeCacheService resources. 
NOTES
     This variant is also available: 
    
    
    [gcloud alpha edge-cache](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cache)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
