---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Symptom/
title: Cloud TPU V1 API - Class Google::Cloud::Tpu::V1::Symptom (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:44.558644+00:00
---

# Cloud TPU V1 API - Class Google::Cloud::Tpu::V1::Symptom (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Symptom/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud TPU V1 API - Class Google::Cloud::Tpu::V1::Symptom (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.7.0  0.6.2  0.5.0  0.4.1  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Cloud TPU V1 API class Google::Cloud::Tpu::V1::Symptom.

A Symptom instance.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Protobuf-Timestamp)) — Timestamp when the Symptom is created. 



### #create_time=
    
    
    def create_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Protobuf-Timestamp)) — Timestamp when the Symptom is created. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Protobuf-Timestamp)) — Timestamp when the Symptom is created. 



### #details
    
    
    def details() -> ::String

**Returns**

  * (::String) — Detailed information of the current Symptom. 



### #details=
    
    
    def details=(value) -> ::String

**Parameter**

  * **value** (::String) — Detailed information of the current Symptom. 



**Returns**

  * (::String) — Detailed information of the current Symptom. 



### #symptom_type
    
    
    def symptom_type() -> ::Google::Cloud::Tpu::V1::Symptom::SymptomType

**Returns**

  * ([::Google::Cloud::Tpu::V1::Symptom::SymptomType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Symptom-SymptomType)) — Type of the Symptom. 



### #symptom_type=
    
    
    def symptom_type=(value) -> ::Google::Cloud::Tpu::V1::Symptom::SymptomType

**Parameter**

  * **value** ([::Google::Cloud::Tpu::V1::Symptom::SymptomType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Symptom-SymptomType)) — Type of the Symptom. 



**Returns**

  * ([::Google::Cloud::Tpu::V1::Symptom::SymptomType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Symptom-SymptomType)) — Type of the Symptom. 



### #worker_id
    
    
    def worker_id() -> ::String

**Returns**

  * (::String) — A string used to uniquely distinguish a worker within a TPU node. 



### #worker_id=
    
    
    def worker_id=(value) -> ::String

**Parameter**

  * **value** (::String) — A string used to uniquely distinguish a worker within a TPU node. 



**Returns**

  * (::String) — A string used to uniquely distinguish a worker within a TPU node. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
