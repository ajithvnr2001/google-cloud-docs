---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterVersionPayload/
title: Parameter Manager V1 API - Class Google::Cloud::ParameterManager::V1::ParameterVersionPayload (v1.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:16:37.412350+00:00
---

# Parameter Manager V1 API - Class Google::Cloud::ParameterManager::V1::ParameterVersionPayload (v1.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterVersionPayload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Parameter Manager V1 API - Class Google::Cloud::ParameterManager::V1::ParameterVersionPayload (v1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Parameter Manager V1 API class Google::Cloud::ParameterManager::V1::ParameterVersionPayload.

Message for storing a ParameterVersion resource's payload data

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #data
    
    
    def data() -> ::String

**Returns**

  * (::String) — Required. bytes data for storing payload. 



### #data=
    
    
    def data=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. bytes data for storing payload. 



**Returns**

  * (::String) — Required. bytes data for storing payload. 



### #data_crc32c
    
    
    def data_crc32c() -> ::Integer

**Returns**

  * (::Integer) — Optional. [Optional] The integrity checksum of the payload. If provided, the server will verify that the checksum matches the payload. If not provided, the server will generate the checksum. 



### #data_crc32c=
    
    
    def data_crc32c=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. [Optional] The integrity checksum of the payload. If provided, the server will verify that the checksum matches the payload. If not provided, the server will generate the checksum. 



**Returns**

  * (::Integer) — Optional. [Optional] The integrity checksum of the payload. If provided, the server will verify that the checksum matches the payload. If not provided, the server will generate the checksum. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
