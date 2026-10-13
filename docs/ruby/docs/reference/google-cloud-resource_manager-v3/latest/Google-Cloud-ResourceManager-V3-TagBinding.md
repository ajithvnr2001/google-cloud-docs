---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagBinding/
title: Resource Manager V3 API - Class Google::Cloud::ResourceManager::V3::TagBinding (v1.8.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:53:13.468371+00:00
---

# Resource Manager V3 API - Class Google::Cloud::ResourceManager::V3::TagBinding (v1.8.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagBinding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Resource Manager V3 API - Class Google::Cloud::ResourceManager::V3::TagBinding (v1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.9.0  0.8.2  0.7.0  0.6.2  0.5.1  0.4.0  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Resource Manager V3 API class Google::Cloud::ResourceManager::V3::TagBinding.

A TagBinding represents a connection between a TagValue and a cloud resource Once a TagBinding is created, the TagValue is applied to all the descendants of the Google Cloud resource.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The name of the TagBinding. This is a String of the form: `tagBindings/{full-resource-name}/{tag-value-name}` (e.g. `tagBindings/%2F%2Fcloudresourcemanager.googleapis.com%2Fprojects%2F123/tagValues/456`). 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — The full resource name of the resource the TagValue is bound to. E.g. `//cloudresourcemanager.googleapis.com/projects/123`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — The full resource name of the resource the TagValue is bound to. E.g. `//cloudresourcemanager.googleapis.com/projects/123`



**Returns**

  * (::String) — The full resource name of the resource the TagValue is bound to. E.g. `//cloudresourcemanager.googleapis.com/projects/123`



### #tag_value
    
    
    def tag_value() -> ::String

**Returns**

  * (::String) — The TagValue of the TagBinding. Must be of the form `tagValues/456`. 



### #tag_value=
    
    
    def tag_value=(value) -> ::String

**Parameter**

  * **value** (::String) — The TagValue of the TagBinding. Must be of the form `tagValues/456`. 



**Returns**

  * (::String) — The TagValue of the TagBinding. Must be of the form `tagValues/456`. 



### #tag_value_namespaced_name
    
    
    def tag_value_namespaced_name() -> ::String

**Returns**

  * (::String) — The namespaced name for the TagValue of the TagBinding. Must be in the format `{parent_id}/{tag_key_short_name}/{short_name}`.

For methods that support TagValue namespaced name, only one of tag_value_namespaced_name or tag_value may be filled. Requests with both fields will be rejected. 




### #tag_value_namespaced_name=
    
    
    def tag_value_namespaced_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The namespaced name for the TagValue of the TagBinding. Must be in the format `{parent_id}/{tag_key_short_name}/{short_name}`.

For methods that support TagValue namespaced name, only one of tag_value_namespaced_name or tag_value may be filled. Requests with both fields will be rejected. 




**Returns**

  * (::String) — The namespaced name for the TagValue of the TagBinding. Must be in the format `{parent_id}/{tag_key_short_name}/{short_name}`.

For methods that support TagValue namespaced name, only one of tag_value_namespaced_name or tag_value may be filled. Requests with both fields will be rejected. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
