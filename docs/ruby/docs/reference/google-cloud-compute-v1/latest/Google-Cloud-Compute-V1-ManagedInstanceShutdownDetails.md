---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ManagedInstanceShutdownDetails/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ManagedInstanceShutdownDetails (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:06.558016+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ManagedInstanceShutdownDetails (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ManagedInstanceShutdownDetails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ManagedInstanceShutdownDetails (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::ManagedInstanceShutdownDetails.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #max_duration
    
    
    def max_duration() -> ::Google::Cloud::Compute::V1::Duration

**Returns**

  * ([::Google::Cloud::Compute::V1::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Duration)) — Output only. The duration for graceful shutdown. Only applicable when the instance is in `PENDING_STOP` state. 



### #max_duration=
    
    
    def max_duration=(value) -> ::Google::Cloud::Compute::V1::Duration

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Duration)) — Output only. The duration for graceful shutdown. Only applicable when the instance is in `PENDING_STOP` state. 



**Returns**

  * ([::Google::Cloud::Compute::V1::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Duration)) — Output only. The duration for graceful shutdown. Only applicable when the instance is in `PENDING_STOP` state. 



### #request_timestamp
    
    
    def request_timestamp() -> ::String

**Returns**

  * (::String) — Output only. Past timestamp indicating the beginning of `PENDING_STOP` state of instance in RFC3339 text format. 



### #request_timestamp=
    
    
    def request_timestamp=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. Past timestamp indicating the beginning of `PENDING_STOP` state of instance in RFC3339 text format. 



**Returns**

  * (::String) — Output only. Past timestamp indicating the beginning of `PENDING_STOP` state of instance in RFC3339 text format. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
