---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/latest/Google.Cloud.ResourceManager.V3.Purpose
title: Cloud Resource Manager v3 API - Enum Purpose (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:17:34.828304+00:00
---

# Cloud Resource Manager v3 API - Enum Purpose (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/latest/Google.Cloud.ResourceManager.V3.Purpose

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Resource Manager v3 API - Enum Purpose (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/latest/Google.Cloud.ResourceManager.V3.Purpose)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/2.5.0/Google.Cloud.ResourceManager.V3.Purpose)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/2.4.0/Google.Cloud.ResourceManager.V3.Purpose)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/2.3.0/Google.Cloud.ResourceManager.V3.Purpose)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/2.2.0/Google.Cloud.ResourceManager.V3.Purpose)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/2.1.0/Google.Cloud.ResourceManager.V3.Purpose)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/2.0.0/Google.Cloud.ResourceManager.V3.Purpose)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/1.2.0/Google.Cloud.ResourceManager.V3.Purpose)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/1.1.0/Google.Cloud.ResourceManager.V3.Purpose)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/1.0.0/Google.Cloud.ResourceManager.V3.Purpose)


    
    
    public enum Purpose

Reference documentation and code samples for the Cloud Resource Manager v3 API enum Purpose.

A purpose for each policy engine requiring such an integration. A single policy engine may have multiple purposes defined, however a TagKey may only specify a single purpose.

## Namespace

[Google.Cloud.ResourceManager.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/latest/Google.Cloud.ResourceManager.V3)

## Assembly

Google.Cloud.ResourceManager.V3.dll

## Fields   
  
---  
**Name** | **Description**  
`GceFirewall` | Purpose for Compute Engine firewalls. A corresponding `purpose_data` should be set for the network the tag is intended for. The key should be `network` and the value should be in either of these two formats: \- `https://www.googleapis.com/compute/{compute_version}/projects/{project_id}/global/networks/{network_id}`

  * `{project_id}/{network_name}`

Examples: \- `https://www.googleapis.com/compute/staging_v1/projects/fail-closed-load-testing/global/networks/6992953698831725600`

  * `fail-closed-load-testing/load-testing-network`

  
`Unspecified` | Unspecified purpose.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
