---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner-Admin-Instance-V1-ListInstanceConfigOperationsResponse/
title: Cloud Spanner Instance Admin V1 API - Class Google::Cloud::Spanner::Admin::Instance::V1::ListInstanceConfigOperationsResponse (v2.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:44.771065+00:00
---

# Cloud Spanner Instance Admin V1 API - Class Google::Cloud::Spanner::Admin::Instance::V1::ListInstanceConfigOperationsResponse (v2.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner-Admin-Instance-V1-ListInstanceConfigOperationsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Spanner Instance Admin V1 API - Class Google::Cloud::Spanner::Admin::Instance::V1::ListInstanceConfigOperationsResponse (v2.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.1 (latest)  2.8.0  2.7.1  2.6.0  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.16.0  0.15.0  0.14.0  0.13.2  0.12.0  0.11.0  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.5 

Reference documentation and code samples for the Cloud Spanner Instance Admin V1 API class Google::Cloud::Spanner::Admin::Instance::V1::ListInstanceConfigOperationsResponse.

The response for [ListInstanceConfigOperations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner-Admin-Instance-V1-InstanceAdmin-Client#Google__Cloud__Spanner__Admin__Instance__V1__InstanceAdmin__Client_list_instance_config_operations_instance_ "Google::Cloud::Spanner::Admin::Instance::V1::InstanceAdmin::Client#list_instance_config_operations \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — `next_page_token` can be sent in a subsequent [ListInstanceConfigOperations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner-Admin-Instance-V1-InstanceAdmin-Client#Google__Cloud__Spanner__Admin__Instance__V1__InstanceAdmin__Client_list_instance_config_operations_instance_ "Google::Cloud::Spanner::Admin::Instance::V1::InstanceAdmin::Client#list_instance_config_operations \(method\)") call to fetch more of the matching metadata. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — `next_page_token` can be sent in a subsequent [ListInstanceConfigOperations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner-Admin-Instance-V1-InstanceAdmin-Client#Google__Cloud__Spanner__Admin__Instance__V1__InstanceAdmin__Client_list_instance_config_operations_instance_ "Google::Cloud::Spanner::Admin::Instance::V1::InstanceAdmin::Client#list_instance_config_operations \(method\)") call to fetch more of the matching metadata. 



**Returns**

  * (::String) — `next_page_token` can be sent in a subsequent [ListInstanceConfigOperations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner-Admin-Instance-V1-InstanceAdmin-Client#Google__Cloud__Spanner__Admin__Instance__V1__InstanceAdmin__Client_list_instance_config_operations_instance_ "Google::Cloud::Spanner::Admin::Instance::V1::InstanceAdmin::Client#list_instance_config_operations \(method\)") call to fetch more of the matching metadata. 



### #operations
    
    
    def operations() -> ::Array<::Google::Longrunning::Operation>

**Returns**

  * (::Array<[::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Longrunning-Operation)>) — The list of matching instance configuration long-running operations. Each operation's name will be prefixed by the name of the instance configuration. The operation's metadata field type `metadata.type_url` describes the type of the metadata. 



### #operations=
    
    
    def operations=(value) -> ::Array<::Google::Longrunning::Operation>

**Parameter**

  * **value** (::Array<[::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Longrunning-Operation)>) — The list of matching instance configuration long-running operations. Each operation's name will be prefixed by the name of the instance configuration. The operation's metadata field type `metadata.type_url` describes the type of the metadata. 



**Returns**

  * (::Array<[::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Longrunning-Operation)>) — The list of matching instance configuration long-running operations. Each operation's name will be prefixed by the name of the instance configuration. The operation's metadata field type `metadata.type_url` describes the type of the metadata. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
