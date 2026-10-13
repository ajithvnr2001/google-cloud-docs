---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-ListMigrationSubtasksRequest/
title: BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::ListMigrationSubtasksRequest (v0.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:04.050264+00:00
---

# BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::ListMigrationSubtasksRequest (v0.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-ListMigrationSubtasksRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::ListMigrationSubtasksRequest (v0.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.23.0 (latest)  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the BigQuery Migration V2 API class Google::Cloud::Bigquery::Migration::V2::ListMigrationSubtasksRequest.

A request to list previously created migration subtasks.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — Optional. The filter to apply. This can be used to get the subtasks of a specific tasks in a workflow, e.g. `migration_task = "ab012"` where `"ab012"` is the task ID (not the name in the named map). 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The filter to apply. This can be used to get the subtasks of a specific tasks in a workflow, e.g. `migration_task = "ab012"` where `"ab012"` is the task ID (not the name in the named map). 



**Returns**

  * (::String) — Optional. The filter to apply. This can be used to get the subtasks of a specific tasks in a workflow, e.g. `migration_task = "ab012"` where `"ab012"` is the task ID (not the name in the named map). 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The maximum number of migration tasks to return. The service may return fewer than this number. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of migration tasks to return. The service may return fewer than this number. 



**Returns**

  * (::Integer) — Optional. The maximum number of migration tasks to return. The service may return fewer than this number. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. A page token, received from previous `ListMigrationSubtasks` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListMigrationSubtasks` must match the call that provided the page token. 




### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A page token, received from previous `ListMigrationSubtasks` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListMigrationSubtasks` must match the call that provided the page token. 




**Returns**

  * (::String) — Optional. A page token, received from previous `ListMigrationSubtasks` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListMigrationSubtasks` must match the call that provided the page token. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The migration task of the subtasks to list. Example: `projects/123/locations/us/workflows/1234`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The migration task of the subtasks to list. Example: `projects/123/locations/us/workflows/1234`



**Returns**

  * (::String) — Required. The migration task of the subtasks to list. Example: `projects/123/locations/us/workflows/1234`



### #read_mask
    
    
    def read_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-FieldMask)) — Optional. The list of fields to be retrieved. 



### #read_mask=
    
    
    def read_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-FieldMask)) — Optional. The list of fields to be retrieved. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-FieldMask)) — Optional. The list of fields to be retrieved. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
