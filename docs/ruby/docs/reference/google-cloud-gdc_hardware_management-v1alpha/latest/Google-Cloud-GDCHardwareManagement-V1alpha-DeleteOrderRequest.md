---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gdc_hardware_management-v1alpha/latest/Google-Cloud-GDCHardwareManagement-V1alpha-DeleteOrderRequest/
title: GDC Hardware Management V1ALPHA API - Class Google::Cloud::GDCHardwareManagement::V1alpha::DeleteOrderRequest (v0.15.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:43.778412+00:00
---

# GDC Hardware Management V1ALPHA API - Class Google::Cloud::GDCHardwareManagement::V1alpha::DeleteOrderRequest (v0.15.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gdc_hardware_management-v1alpha/latest/Google-Cloud-GDCHardwareManagement-V1alpha-DeleteOrderRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  GDC Hardware Management V1ALPHA API - Class Google::Cloud::GDCHardwareManagement::V1alpha::DeleteOrderRequest (v0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.14.1  0.13.0  0.12.1  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the GDC Hardware Management V1ALPHA API class Google::Cloud::GDCHardwareManagement::V1alpha::DeleteOrderRequest.

A request to delete an order.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #force
    
    
    def force() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. An option to delete any nested resources in the Order, such as a HardwareGroup. If true, any nested resources for this Order will also be deleted. Otherwise, the request will only succeed if the Order has no nested resources. 



### #force=
    
    
    def force=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. An option to delete any nested resources in the Order, such as a HardwareGroup. If true, any nested resources for this Order will also be deleted. Otherwise, the request will only succeed if the Order has no nested resources. 



**Returns**

  * (::Boolean) — Optional. An option to delete any nested resources in the Order, such as a HardwareGroup. If true, any nested resources for this Order will also be deleted. Otherwise, the request will only succeed if the Order has no nested resources. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The name of the order. Format: `projects/{project}/locations/{location}/orders/{order}`



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the order. Format: `projects/{project}/locations/{location}/orders/{order}`



**Returns**

  * (::String) — Required. The name of the order. Format: `projects/{project}/locations/{location}/orders/{order}`



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. An optional unique identifier for this request. See [AIP-155](https://google.aip.dev/155). 



### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. An optional unique identifier for this request. See [AIP-155](https://google.aip.dev/155). 



**Returns**

  * (::String) — Optional. An optional unique identifier for this request. See [AIP-155](https://google.aip.dev/155). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
