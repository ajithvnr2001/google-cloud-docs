---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-UpgradeEvent/
title: Kubernetes Engine V1beta1 API - Class Google::Cloud::Container::V1beta1::UpgradeEvent (v0.57.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:36.638608+00:00
---

# Kubernetes Engine V1beta1 API - Class Google::Cloud::Container::V1beta1::UpgradeEvent (v0.57.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-UpgradeEvent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Kubernetes Engine V1beta1 API - Class Google::Cloud::Container::V1beta1::UpgradeEvent (v0.57.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.57.1 (latest)  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.1  0.50.0  0.49.1  0.48.0  0.47.0  0.46.0  0.45.1  0.44.0  0.43.0  0.42.1  0.41.0  0.40.1  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.3  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.0  0.17.0  0.16.3  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.3 

Reference documentation and code samples for the Kubernetes Engine V1beta1 API class Google::Cloud::Container::V1beta1::UpgradeEvent.

UpgradeEvent is a notification sent to customers by the cluster server when a resource is upgrading.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #current_emulated_version
    
    
    def current_emulated_version() -> ::String

**Returns**

  * (::String) — The current emulated version before the upgrade. 



### #current_emulated_version=
    
    
    def current_emulated_version=(value) -> ::String

**Parameter**

  * **value** (::String) — The current emulated version before the upgrade. 



**Returns**

  * (::String) — The current emulated version before the upgrade. 



### #current_version
    
    
    def current_version() -> ::String

**Returns**

  * (::String) — The current version before the upgrade. 



### #current_version=
    
    
    def current_version=(value) -> ::String

**Parameter**

  * **value** (::String) — The current version before the upgrade. 



**Returns**

  * (::String) — The current version before the upgrade. 



### #operation
    
    
    def operation() -> ::String

**Returns**

  * (::String) — The operation associated with this upgrade. 



### #operation=
    
    
    def operation=(value) -> ::String

**Parameter**

  * **value** (::String) — The operation associated with this upgrade. 



**Returns**

  * (::String) — The operation associated with this upgrade. 



### #operation_start_time
    
    
    def operation_start_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Protobuf-Timestamp)) — The time when the operation was started. 



### #operation_start_time=
    
    
    def operation_start_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Protobuf-Timestamp)) — The time when the operation was started. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Protobuf-Timestamp)) — The time when the operation was started. 



### #resource
    
    
    def resource() -> ::String

**Returns**

  * (::String) — Optional relative path to the resource. For example in node pool upgrades, the relative path of the node pool. 



### #resource=
    
    
    def resource=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional relative path to the resource. For example in node pool upgrades, the relative path of the node pool. 



**Returns**

  * (::String) — Optional relative path to the resource. For example in node pool upgrades, the relative path of the node pool. 



### #resource_type
    
    
    def resource_type() -> ::Google::Cloud::Container::V1beta1::UpgradeResourceType

**Returns**

  * ([::Google::Cloud::Container::V1beta1::UpgradeResourceType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-UpgradeResourceType)) — The resource type that is upgrading. 



### #resource_type=
    
    
    def resource_type=(value) -> ::Google::Cloud::Container::V1beta1::UpgradeResourceType

**Parameter**

  * **value** ([::Google::Cloud::Container::V1beta1::UpgradeResourceType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-UpgradeResourceType)) — The resource type that is upgrading. 



**Returns**

  * ([::Google::Cloud::Container::V1beta1::UpgradeResourceType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-UpgradeResourceType)) — The resource type that is upgrading. 



### #target_emulated_version
    
    
    def target_emulated_version() -> ::String

**Returns**

  * (::String) — The target emulated version for the upgrade. 



### #target_emulated_version=
    
    
    def target_emulated_version=(value) -> ::String

**Parameter**

  * **value** (::String) — The target emulated version for the upgrade. 



**Returns**

  * (::String) — The target emulated version for the upgrade. 



### #target_version
    
    
    def target_version() -> ::String

**Returns**

  * (::String) — The target version for the upgrade. 



### #target_version=
    
    
    def target_version=(value) -> ::String

**Parameter**

  * **value** (::String) — The target version for the upgrade. 



**Returns**

  * (::String) — The target version for the upgrade. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
