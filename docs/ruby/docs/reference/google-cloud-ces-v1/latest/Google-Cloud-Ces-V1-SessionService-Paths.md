---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-SessionService-Paths/
title: Gemini Enterprise for Customer Experience V1 API - Module Google::Cloud::Ces::V1::SessionService::Paths (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:06.685615+00:00
---

# Gemini Enterprise for Customer Experience V1 API - Module Google::Cloud::Ces::V1::SessionService::Paths (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-SessionService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience V1 API - Module Google::Cloud::Ces::V1::SessionService::Paths (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Gemini Enterprise for Customer Experience V1 API module Google::Cloud::Ces::V1::SessionService::Paths.

Path helper methods for the SessionService API.

## Extended By

  * [Google::Cloud::Ces::V1::SessionService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-SessionService-Paths)



## Included In

  * [Google::Cloud::Ces::V1::SessionService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-SessionService-Client)
  * [Google::Cloud::Ces::V1::SessionService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-SessionService-Paths)
  * [Google::Cloud::Ces::V1::SessionService::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-SessionService-Rest-Client)



## Methods 

### #agent_path
    
    
    def agent_path(project:, location:, app:, agent:) -> ::String

Create a fully-qualified Agent resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/apps/{app}/agents/{agent}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **app** (String) 
  * **agent** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #session_path
    
    
    def session_path(project:, location:, app:, session:) -> ::String

Create a fully-qualified Session resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/apps/{app}/sessions/{session}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **app** (String) 
  * **session** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #tool_path
    
    
    def tool_path(project:, location:, app:, tool:) -> ::String

Create a fully-qualified Tool resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/apps/{app}/tools/{tool}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **app** (String) 
  * **tool** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #toolset_path
    
    
    def toolset_path(project:, location:, app:, toolset:) -> ::String

Create a fully-qualified Toolset resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **app** (String) 
  * **toolset** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
