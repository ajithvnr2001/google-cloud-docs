---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Api-BatchingDescriptorProto/
title: Cloud Spanner Instance Admin V1 API - Class Google::Api::BatchingDescriptorProto (v2.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:50.600380+00:00
---

# Cloud Spanner Instance Admin V1 API - Class Google::Api::BatchingDescriptorProto (v2.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Api-BatchingDescriptorProto/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Spanner Instance Admin V1 API - Class Google::Api::BatchingDescriptorProto (v2.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.1 (latest)  2.8.0  2.7.1  2.6.0  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.16.0  0.15.0  0.14.0  0.13.2  0.12.0  0.11.0  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.5 

Reference documentation and code samples for the Cloud Spanner Instance Admin V1 API class Google::Api::BatchingDescriptorProto.

`BatchingDescriptorProto` specifies the fields of the request message to be used for batching, and, optionally, the fields of the response message to be used for demultiplexing.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #batched_field
    
    
    def batched_field() -> ::String

**Returns**

  * (::String) — The repeated field in the request message to be aggregated by batching. 



### #batched_field=
    
    
    def batched_field=(value) -> ::String

**Parameter**

  * **value** (::String) — The repeated field in the request message to be aggregated by batching. 



**Returns**

  * (::String) — The repeated field in the request message to be aggregated by batching. 



### #discriminator_fields
    
    
    def discriminator_fields() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — A list of the fields in the request message. Two requests will be batched together only if the values of every field specified in `request_discriminator_fields` is equal between the two requests. 



### #discriminator_fields=
    
    
    def discriminator_fields=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — A list of the fields in the request message. Two requests will be batched together only if the values of every field specified in `request_discriminator_fields` is equal between the two requests. 



**Returns**

  * (::Array<::String>) — A list of the fields in the request message. Two requests will be batched together only if the values of every field specified in `request_discriminator_fields` is equal between the two requests. 



### #subresponse_field
    
    
    def subresponse_field() -> ::String

**Returns**

  * (::String) — Optional. When present, indicates the field in the response message to be used to demultiplex the response into multiple response messages, in correspondence with the multiple request messages originally batched together. 



### #subresponse_field=
    
    
    def subresponse_field=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. When present, indicates the field in the response message to be used to demultiplex the response into multiple response messages, in correspondence with the multiple request messages originally batched together. 



**Returns**

  * (::String) — Optional. When present, indicates the field in the response message to be used to demultiplex the response into multiple response messages, in correspondence with the multiple request messages originally batched together. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
