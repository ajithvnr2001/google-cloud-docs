---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging-v2/latest/Google-Cloud-Logging-V2-ListMonitoredResourceDescriptorsRequest/
title: Cloud Logging V2 API - Class Google::Cloud::Logging::V2::ListMonitoredResourceDescriptorsRequest (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:17:38.308019+00:00
---

# Cloud Logging V2 API - Class Google::Cloud::Logging::V2::ListMonitoredResourceDescriptorsRequest (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging-v2/latest/Google-Cloud-Logging-V2-ListMonitoredResourceDescriptorsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Logging V2 API - Class Google::Cloud::Logging::V2::ListMonitoredResourceDescriptorsRequest (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.13.0  0.12.2  0.11.0  0.10.1  0.9.0  0.8.1  0.7.0  0.6.0  0.5.6 

Reference documentation and code samples for the Cloud Logging V2 API class Google::Cloud::Logging::V2::ListMonitoredResourceDescriptorsRequest.

The parameters to ListMonitoredResourceDescriptors

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The maximum number of results to return from this request. Non-positive values are ignored. The presence of `nextPageToken` in the response indicates that more results might be available. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of results to return from this request. Non-positive values are ignored. The presence of `nextPageToken` in the response indicates that more results might be available. 



**Returns**

  * (::Integer) — Optional. The maximum number of results to return from this request. Non-positive values are ignored. The presence of `nextPageToken` in the response indicates that more results might be available. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. If present, then retrieve the next batch of results from the preceding call to this method. `pageToken` must be the value of `nextPageToken` from the previous response. The values of other method parameters should be identical to those in the previous call. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. If present, then retrieve the next batch of results from the preceding call to this method. `pageToken` must be the value of `nextPageToken` from the previous response. The values of other method parameters should be identical to those in the previous call. 



**Returns**

  * (::String) — Optional. If present, then retrieve the next batch of results from the preceding call to this method. `pageToken` must be the value of `nextPageToken` from the previous response. The values of other method parameters should be identical to those in the previous call. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
