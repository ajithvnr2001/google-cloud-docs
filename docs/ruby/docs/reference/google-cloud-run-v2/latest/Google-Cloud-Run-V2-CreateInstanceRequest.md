---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-CreateInstanceRequest/
title: Cloud Run V2 API - Class Google::Cloud::Run::V2::CreateInstanceRequest (v0.29.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:32:10.438693+00:00
---

# Cloud Run V2 API - Class Google::Cloud::Run::V2::CreateInstanceRequest (v0.29.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-CreateInstanceRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Run V2 API - Class Google::Cloud::Run::V2::CreateInstanceRequest (v0.29.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.1 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.1  0.23.0  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.2  0.12.0  0.11.0  0.10.1  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Run V2 API class Google::Cloud::Run::V2::CreateInstanceRequest.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #instance
    
    
    def instance() -> ::Google::Cloud::Run::V2::Instance

**Returns**

  * ([::Google::Cloud::Run::V2::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Instance)) 



### #instance=
    
    
    def instance=(value) -> ::Google::Cloud::Run::V2::Instance

**Parameter**

  * **value** ([::Google::Cloud::Run::V2::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Instance)) 



**Returns**

  * ([::Google::Cloud::Run::V2::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Instance)) 



### #instance_id
    
    
    def instance_id() -> ::String

**Returns**

  * (::String) — Required. The unique identifier for the Instance. It must begin with letter, and cannot end with hyphen; must contain fewer than 50 characters. The name of the instance becomes {parent}/instances/{instance_id}. 



### #instance_id=
    
    
    def instance_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The unique identifier for the Instance. It must begin with letter, and cannot end with hyphen; must contain fewer than 50 characters. The name of the instance becomes {parent}/instances/{instance_id}. 



**Returns**

  * (::String) — Required. The unique identifier for the Instance. It must begin with letter, and cannot end with hyphen; must contain fewer than 50 characters. The name of the instance becomes {parent}/instances/{instance_id}. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) 



**Returns**

  * (::String) 



### #validate_only
    
    
    def validate_only() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Indicates that the request should be validated and default values populated, without persisting the request or creating any resources. 



### #validate_only=
    
    
    def validate_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Indicates that the request should be validated and default values populated, without persisting the request or creating any resources. 



**Returns**

  * (::Boolean) — Optional. Indicates that the request should be validated and default values populated, without persisting the request or creating any resources. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
