---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-StreamsService-Paths/
title: Vision AI V1 API - Module Google::Cloud::VisionAI::V1::StreamsService::Paths (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:02.917444+00:00
---

# Vision AI V1 API - Module Google::Cloud::VisionAI::V1::StreamsService::Paths (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-StreamsService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vision AI V1 API - Module Google::Cloud::VisionAI::V1::StreamsService::Paths (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.1  1.2.0  1.1.1  1.0.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vision AI V1 API module Google::Cloud::VisionAI::V1::StreamsService::Paths.

Path helper methods for the StreamsService API.

## Extended By

  * [Google::Cloud::VisionAI::V1::StreamsService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-StreamsService-Paths)



## Included In

  * [Google::Cloud::VisionAI::V1::StreamsService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-StreamsService-Client)
  * [Google::Cloud::VisionAI::V1::StreamsService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-StreamsService-Paths)
  * [Google::Cloud::VisionAI::V1::StreamsService::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-StreamsService-Rest-Client)



## Methods 

### #channel_path
    
    
    def channel_path(project:, location:, cluster:, channel:) -> ::String

Create a fully-qualified Channel resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/clusters/{cluster}/channels/{channel}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **cluster** (String) 
  * **channel** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #cluster_path
    
    
    def cluster_path(project:, location:, cluster:) -> ::String

Create a fully-qualified Cluster resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/clusters/{cluster}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **cluster** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #event_path
    
    
    def event_path(project:, location:, cluster:, event:) -> ::String

Create a fully-qualified Event resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/clusters/{cluster}/events/{event}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **cluster** (String) 
  * **event** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #location_path
    
    
    def location_path(project:, location:) -> ::String

Create a fully-qualified Location resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}`

**Parameters**

  * **project** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #series_path
    
    
    def series_path(project:, location:, cluster:, series:) -> ::String

Create a fully-qualified Series resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/clusters/{cluster}/series/{series}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **cluster** (String) 
  * **series** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #stream_path
    
    
    def stream_path(project:, location:, cluster:, stream:) -> ::String

Create a fully-qualified Stream resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/clusters/{cluster}/streams/{stream}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **cluster** (String) 
  * **stream** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
