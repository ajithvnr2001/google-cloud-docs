---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-MaintenancePolicy/
title: Google Cloud Memorystore for Redis V1beta1 API - Class Google::Cloud::Redis::V1beta1::MaintenancePolicy (v0.22.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:02.934477+00:00
---

# Google Cloud Memorystore for Redis V1beta1 API - Class Google::Cloud::Redis::V1beta1::MaintenancePolicy (v0.22.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-MaintenancePolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis V1beta1 API - Class Google::Cloud::Redis::V1beta1::MaintenancePolicy (v0.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.0 (latest)  0.21.1  0.20.0  0.19.1  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.2  0.12.2  0.11.0  0.10.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.1 

Reference documentation and code samples for the Google Cloud Memorystore for Redis V1beta1 API class Google::Cloud::Redis::V1beta1::MaintenancePolicy.

Maintenance policy for an instance.

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

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the policy was created. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. Description of what this policy is for. Create/Update methods return INVALID_ARGUMENT if the length is greater than 512. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Description of what this policy is for. Create/Update methods return INVALID_ARGUMENT if the length is greater than 512. 



**Returns**

  * (::String) — Optional. Description of what this policy is for. Create/Update methods return INVALID_ARGUMENT if the length is greater than 512. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the policy was last updated. 



### #weekly_maintenance_window
    
    
    def weekly_maintenance_window() -> ::Array<::Google::Cloud::Redis::V1beta1::WeeklyMaintenanceWindow>

**Returns**

  * (::Array<[::Google::Cloud::Redis::V1beta1::WeeklyMaintenanceWindow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-WeeklyMaintenanceWindow)>) — Optional. Maintenance window that is applied to resources covered by this policy. Minimum 1. For the current version, the maximum number of weekly_window is expected to be one. 



### #weekly_maintenance_window=
    
    
    def weekly_maintenance_window=(value) -> ::Array<::Google::Cloud::Redis::V1beta1::WeeklyMaintenanceWindow>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Redis::V1beta1::WeeklyMaintenanceWindow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-WeeklyMaintenanceWindow)>) — Optional. Maintenance window that is applied to resources covered by this policy. Minimum 1. For the current version, the maximum number of weekly_window is expected to be one. 



**Returns**

  * (::Array<[::Google::Cloud::Redis::V1beta1::WeeklyMaintenanceWindow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-WeeklyMaintenanceWindow)>) — Optional. Maintenance window that is applied to resources covered by this policy. Minimum 1. For the current version, the maximum number of weekly_window is expected to be one. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
