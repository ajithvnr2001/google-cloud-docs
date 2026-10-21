---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cache/
title: gcloud alpha edge-cache \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:43:54.522518+00:00
---

# gcloud alpha edge-cache  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha edge-cache Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha edge-cache - manage Media CDN resources 
SYNOPSIS
    

`gcloud alpha edge-cache` `GROUP` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Manage Media CDN resources. 
EXAMPLES
     To list EdgeCacheService resources in the active Cloud Platform project, run: 
    
    
    [gcloud alpha edge-cache services list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cache/services/list)

To create an EdgeCacheOrigin resource named 'my-origin' that points to a Cloud Storage bucket, run: 
    
    
    [gcloud alpha edge-cache origins create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cache/origins/create) my-origin --origin-address="gs://bucket"

To import an EdgeCacheService resource configuration from a YAML definition, run: 
    
    
    [gcloud alpha edge-cache services import](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cache/services/import) my-service --source=config.yaml

To describe an EdgeCacheKeyset resource named 'my-keyset', run: 
    
    
    [gcloud alpha edge-cache keysets describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cache/keysets/describe) my-keyset

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[keysets](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cache/keysets)`
     `(ALPHA)` Interact with and manage EdgeCacheKeyset resources. 
`[operations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cache/operations)`
     `(ALPHA)` Manage EdgeCache operations. 
`[origins](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cache/origins)`
     `(ALPHA)` Interact with and manage EdgeCacheOrigin resources. 
`[services](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cache/services)`
     `(ALPHA)` Interact with and manage EdgeCacheService resources. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud edge-cache](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
