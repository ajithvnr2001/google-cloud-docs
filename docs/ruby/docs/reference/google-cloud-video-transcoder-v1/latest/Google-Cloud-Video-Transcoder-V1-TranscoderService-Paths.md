---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-TranscoderService-Paths/
title: Transcoder V1 API - Module Google::Cloud::Video::Transcoder::V1::TranscoderService::Paths (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:50.106209+00:00
---

# Transcoder V1 API - Module Google::Cloud::Video::Transcoder::V1::TranscoderService::Paths (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-TranscoderService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Transcoder V1 API - Module Google::Cloud::Video::Transcoder::V1::TranscoderService::Paths (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.13.0  0.12.2  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.2 

Reference documentation and code samples for the Transcoder V1 API module Google::Cloud::Video::Transcoder::V1::TranscoderService::Paths.

Path helper methods for the TranscoderService API.

## Extended By

  * [Google::Cloud::Video::Transcoder::V1::TranscoderService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-TranscoderService-Paths)



## Included In

  * [Google::Cloud::Video::Transcoder::V1::TranscoderService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-TranscoderService-Client)
  * [Google::Cloud::Video::Transcoder::V1::TranscoderService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-TranscoderService-Paths)
  * [Google::Cloud::Video::Transcoder::V1::TranscoderService::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-TranscoderService-Rest-Client)



## Methods 

### #job_path
    
    
    def job_path(project:, location:, job:) -> ::String

Create a fully-qualified Job resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/jobs/{job}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **job** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #job_template_path
    
    
    def job_template_path(project:, location:, job_template:) -> ::String

Create a fully-qualified JobTemplate resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/jobTemplates/{job_template}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **job_template** (String) 



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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
