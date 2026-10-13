---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Instance/
title: Apigee Registry V1 API - Class Google::Cloud::ApigeeRegistry::V1::Instance (v0.16.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:54.171236+00:00
---

# Apigee Registry V1 API - Class Google::Cloud::ApigeeRegistry::V1::Instance (v0.16.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Apigee Registry V1 API - Class Google::Cloud::ApigeeRegistry::V1::Instance (v0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.16.0  0.15.0  0.14.0  0.13.1  0.12.0  0.11.0  0.10.1  0.9.0  0.8.1  0.7.2  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Apigee Registry V1 API class Google::Cloud::ApigeeRegistry::V1::Instance.

An Instance represents the instance resources of the Registry. Currently, only one instance is allowed for each project.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #config
    
    
    def config() -> ::Google::Cloud::ApigeeRegistry::V1::Instance::Config

**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::Instance::Config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Instance-Config)) — Required. Config of the Instance. 



### #config=
    
    
    def config=(value) -> ::Google::Cloud::ApigeeRegistry::V1::Instance::Config

**Parameter**

  * **value** ([::Google::Cloud::ApigeeRegistry::V1::Instance::Config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Instance-Config)) — Required. Config of the Instance. 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::Instance::Config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Instance-Config)) — Required. Config of the Instance. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Protobuf-Timestamp)) — Output only. Creation timestamp. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Format: `projects/*/locations/*/instance`. Currently only `locations/global` is supported. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Format: `projects/*/locations/*/instance`. Currently only `locations/global` is supported. 



**Returns**

  * (::String) — Format: `projects/*/locations/*/instance`. Currently only `locations/global` is supported. 



### #state
    
    
    def state() -> ::Google::Cloud::ApigeeRegistry::V1::Instance::State

**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::Instance::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Instance-State)) — Output only. The current state of the Instance. 



### #state_message
    
    
    def state_message() -> ::String

**Returns**

  * (::String) — Output only. Extra information of Instance.State if the state is `FAILED`. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Protobuf-Timestamp)) — Output only. Last update timestamp. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
