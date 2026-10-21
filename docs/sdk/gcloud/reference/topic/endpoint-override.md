---
url: https://docs.cloud.google.com/sdk/gcloud/reference/topic/endpoint-override/
title: gcloud topic endpoint-override \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:28.296594+00:00
---

# gcloud topic endpoint-override  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/topic/endpoint-override/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud topic endpoint-override Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud topic endpoint-override - gcloud endpoint override supplementary help 
DESCRIPTION
     Use API endpoint overrides to override the API endpoints used by the `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` CLI. Applications such as Private Google Access and Private Service Connect use API endpoint overrides. 
Setting API endpoint overrides
     `gcloud` API endpoints are defined as `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` CLI properties and can be overridden through `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` CLI properties or environment variables. For example, to override the API endpoint for the `[gcloud storage](https://docs.cloud.google.com/sdk/gcloud/reference/storage)` command to use the private `storage-vialink1.p.googleapis.com` endpoint with either `http://` or `https://` prefix, you can use one of the following commands: 
    
    
    # Override using a property:
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) api_endpoint_overrides/storage <https://storage-vialink1.p.googleapis.com/>
    
    
    # Override using an environment variable
    CLOUDSDK_API_ENDPOINT_OVERRIDES_STORAGE=[https://\](https://\\)
    storage-vialink1.p.googleapis.com/
    gcloud storage objects list gs://my-bucket

Default API endpoints
     To get the default value for an API endpoint override, use `[gcloud config get](https://docs.cloud.google.com/sdk/gcloud/reference/config/get)` to determine the correct format for your API endpoint override: 
    
    
    [gcloud config get](https://docs.cloud.google.com/sdk/gcloud/reference/config/get) api_endpoint_overrides/storage

Unsetting API endpoint overrides
     To unset an API endpoint override, use `[gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset)`: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) api_endpoint_overrides/storage

Configured API endpoint overrides
     To see the APIs which have an endpoint override set, use `[gcloud config list](https://docs.cloud.google.com/sdk/gcloud/reference/config/list)`: 
    
    
    [gcloud config list](https://docs.cloud.google.com/sdk/gcloud/reference/config/list) api_endpoint_overrides/

To see all the set and unset API endpoint override properties, use the `--all` flag: 
    
    
    [gcloud config list](https://docs.cloud.google.com/sdk/gcloud/reference/config/list) api_endpoint_overrides/ --all

NOTES
     These variants are also available: 
    
    
    [gcloud alpha topic endpoint-override](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/topic/endpoint-override)
    
    
    [gcloud beta topic endpoint-override](https://docs.cloud.google.com/sdk/gcloud/reference/beta/topic/endpoint-override)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
