---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-CreateTagHoldRequest/
title: Resource Manager V3 API - Class Google::Cloud::ResourceManager::V3::CreateTagHoldRequest (v1.8.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:04.108654+00:00
---

# Resource Manager V3 API - Class Google::Cloud::ResourceManager::V3::CreateTagHoldRequest (v1.8.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-CreateTagHoldRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Resource Manager V3 API - Class Google::Cloud::ResourceManager::V3::CreateTagHoldRequest (v1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.9.0  0.8.2  0.7.0  0.6.2  0.5.1  0.4.0  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Resource Manager V3 API class Google::Cloud::ResourceManager::V3::CreateTagHoldRequest.

The request message to create a TagHold.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the TagHold's parent TagValue. Must be of the form: `tagValues/{tag-value-id}`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the TagHold's parent TagValue. Must be of the form: `tagValues/{tag-value-id}`. 



**Returns**

  * (::String) — Required. The resource name of the TagHold's parent TagValue. Must be of the form: `tagValues/{tag-value-id}`. 



### #tag_hold
    
    
    def tag_hold() -> ::Google::Cloud::ResourceManager::V3::TagHold

**Returns**

  * ([::Google::Cloud::ResourceManager::V3::TagHold](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagHold)) — Required. The TagHold to be created. 



### #tag_hold=
    
    
    def tag_hold=(value) -> ::Google::Cloud::ResourceManager::V3::TagHold

**Parameter**

  * **value** ([::Google::Cloud::ResourceManager::V3::TagHold](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagHold)) — Required. The TagHold to be created. 



**Returns**

  * ([::Google::Cloud::ResourceManager::V3::TagHold](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagHold)) — Required. The TagHold to be created. 



### #validate_only
    
    
    def validate_only() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Set to true to perform the validations necessary for creating the resource, but not actually perform the action. 



### #validate_only=
    
    
    def validate_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Set to true to perform the validations necessary for creating the resource, but not actually perform the action. 



**Returns**

  * (::Boolean) — Optional. Set to true to perform the validations necessary for creating the resource, but not actually perform the action. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
