---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Instance/
title: Financial Services V1 API - Class Google::Cloud::FinancialServices::V1::Instance (v1.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:40:12.735896+00:00
---

# Financial Services V1 API - Class Google::Cloud::FinancialServices::V1::Instance (v1.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Financial Services V1 API - Class Google::Cloud::FinancialServices::V1::Instance (v1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  0.7.0  0.6.1  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Financial Services V1 API class Google::Cloud::FinancialServices::V1::Instance.

Instance is a container for the rest of API resources. Only resources in the same instance can interact with each other. Child resources inherit the location (data residency) and encryption (CMEK). The location of the provided input and output in requests must match the location of the instance.

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

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp when the Instance was created. Assigned by the server. 



### #kms_key
    
    
    def kms_key() -> ::String

**Returns**

  * (::String) — Required. The KMS key name used for CMEK (encryption-at-rest). format: `projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey}` VPC-SC restrictions apply. 



### #kms_key=
    
    
    def kms_key=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The KMS key name used for CMEK (encryption-at-rest). format: `projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey}` VPC-SC restrictions apply. 



**Returns**

  * (::String) — Required. The KMS key name used for CMEK (encryption-at-rest). format: `projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey}` VPC-SC restrictions apply. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Labels 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The full path to the Instance resource in this API. format: `projects/{project}/locations/{location}/instances/{instance}`



### #state
    
    
    def state() -> ::Google::Cloud::FinancialServices::V1::Instance::State

**Returns**

  * ([::Google::Cloud::FinancialServices::V1::Instance::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-Instance-State)) — Output only. State of the instance. Assigned by the server. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp when the Instance was last updated. Assigned by the server. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
