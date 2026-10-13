---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-Inventory/
title: Cloud OS Config V1alpha API - Class Google::Cloud::OsConfig::V1alpha::Inventory (v0.17.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:51:04.389047+00:00
---

# Cloud OS Config V1alpha API - Class Google::Cloud::OsConfig::V1alpha::Inventory (v0.17.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-Inventory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud OS Config V1alpha API - Class Google::Cloud::OsConfig::V1alpha::Inventory (v0.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.16.1  0.15.0  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.1  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.2 

Reference documentation and code samples for the Cloud OS Config V1alpha API class Google::Cloud::OsConfig::V1alpha::Inventory.

This API resource represents the available inventory data for a Compute Engine virtual machine (VM) instance at a given point in time.

You can use this API resource to determine the inventory data of your VM.

For more information, see [Information provided by OS inventory management](https://cloud.google.com/compute/docs/instances/os-inventory-management#data-collected).

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #items
    
    
    def items() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::OsConfig::V1alpha::Inventory::Item}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::OsConfig::V1alpha::Inventory::Item}) — Output only. Inventory items related to the VM keyed by an opaque unique identifier for each inventory item. The identifier is unique to each distinct and addressable inventory item and will change, when there is a new package version. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The `Inventory` API resource name.

Format: `projects/{project_number}/locations/{location}/instances/{instance_id}/inventory`




### #os_info
    
    
    def os_info() -> ::Google::Cloud::OsConfig::V1alpha::Inventory::OsInfo

**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::Inventory::OsInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-Inventory-OsInfo)) — Output only. Base level operating system information for the VM. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp of the last reported inventory for the VM. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
