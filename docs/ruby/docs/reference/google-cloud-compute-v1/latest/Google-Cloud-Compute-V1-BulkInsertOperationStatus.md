---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-BulkInsertOperationStatus/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::BulkInsertOperationStatus (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:44.862372+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::BulkInsertOperationStatus (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-BulkInsertOperationStatus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::BulkInsertOperationStatus (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::BulkInsertOperationStatus.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #created_vm_count
    
    
    def created_vm_count() -> ::Integer

**Returns**

  * (::Integer) — [Output Only] Count of VMs successfully created so far. 



### #created_vm_count=
    
    
    def created_vm_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — [Output Only] Count of VMs successfully created so far. 



**Returns**

  * (::Integer) — [Output Only] Count of VMs successfully created so far. 



### #deleted_vm_count
    
    
    def deleted_vm_count() -> ::Integer

**Returns**

  * (::Integer) — [Output Only] Count of VMs that got deleted during rollback. 



### #deleted_vm_count=
    
    
    def deleted_vm_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — [Output Only] Count of VMs that got deleted during rollback. 



**Returns**

  * (::Integer) — [Output Only] Count of VMs that got deleted during rollback. 



### #failed_to_create_vm_count
    
    
    def failed_to_create_vm_count() -> ::Integer

**Returns**

  * (::Integer) — [Output Only] Count of VMs that started creating but encountered an error. 



### #failed_to_create_vm_count=
    
    
    def failed_to_create_vm_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — [Output Only] Count of VMs that started creating but encountered an error. 



**Returns**

  * (::Integer) — [Output Only] Count of VMs that started creating but encountered an error. 



### #status
    
    
    def status() -> ::String

**Returns**

  * (::String) — [Output Only] Creation status of BulkInsert operation - information if the flow is rolling forward or rolling back. Check the Status enum for the list of possible values. 



### #status=
    
    
    def status=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] Creation status of BulkInsert operation - information if the flow is rolling forward or rolling back. Check the Status enum for the list of possible values. 



**Returns**

  * (::String) — [Output Only] Creation status of BulkInsert operation - information if the flow is rolling forward or rolling back. Check the Status enum for the list of possible values. 



### #target_vm_count
    
    
    def target_vm_count() -> ::Integer

**Returns**

  * (::Integer) — [Output Only] Count of VMs originally planned to be created. 



### #target_vm_count=
    
    
    def target_vm_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — [Output Only] Count of VMs originally planned to be created. 



**Returns**

  * (::Integer) — [Output Only] Count of VMs originally planned to be created. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
