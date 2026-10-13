---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-ListBackupsRequest/
title: Memorystore V1 API - Class Google::Cloud::Memorystore::V1::ListBackupsRequest (v1.11.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:51.275924+00:00
---

# Memorystore V1 API - Class Google::Cloud::Memorystore::V1::ListBackupsRequest (v1.11.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-ListBackupsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Memorystore V1 API - Class Google::Cloud::Memorystore::V1::ListBackupsRequest (v1.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.1 (latest)  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Memorystore V1 API class Google::Cloud::Memorystore::V1::ListBackupsRequest.

Request for `ListBackups`.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The maximum number of items to return.

If not specified, a default value of 1000 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's `next_page_token` to determine if there are more clusters left to be queried. 




### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of items to return.

If not specified, a default value of 1000 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's `next_page_token` to determine if there are more clusters left to be queried. 




**Returns**

  * (::Integer) — Optional. The maximum number of items to return.

If not specified, a default value of 1000 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's `next_page_token` to determine if there are more clusters left to be queried. 




### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. The `next_page_token` value returned from a previous `ListBackupCollections` request, if any. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The `next_page_token` value returned from a previous `ListBackupCollections` request, if any. 



**Returns**

  * (::String) — Optional. The `next_page_token` value returned from a previous `ListBackupCollections` request, if any. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the backupCollection using the form: `projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the backupCollection using the form: `projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}`



**Returns**

  * (::String) — Required. The resource name of the backupCollection using the form: `projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
