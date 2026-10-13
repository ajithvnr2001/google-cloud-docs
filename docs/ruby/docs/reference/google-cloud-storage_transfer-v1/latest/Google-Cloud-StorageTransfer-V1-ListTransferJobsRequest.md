---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-ListTransferJobsRequest/
title: Storage Transfer Service V1 API - Class Google::Cloud::StorageTransfer::V1::ListTransferJobsRequest (v1.11.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:21.607100+00:00
---

# Storage Transfer Service V1 API - Class Google::Cloud::StorageTransfer::V1::ListTransferJobsRequest (v1.11.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-ListTransferJobsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Storage Transfer Service V1 API - Class Google::Cloud::StorageTransfer::V1::ListTransferJobsRequest (v1.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.1 (latest)  1.11.0  1.10.0  1.9.0  1.8.1  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Storage Transfer Service V1 API class Google::Cloud::StorageTransfer::V1::ListTransferJobsRequest.

`projectId`, `jobNames`, and `jobStatuses` are query parameters that can be specified when listing transfer jobs.

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

  * (::String) — 

Required. A list of query parameters specified as JSON text in the form of:

` { "projectId":"my_project_id", "jobNames":["jobid1","jobid2",...], "jobStatuses":["status1","status2",...], "dataBackend":"QUERY_REPLICATION_CONFIGS", "sourceBucket":"source-bucket-name", "sinkBucket":"sink-bucket-name", } `

The JSON formatting in the example is for display only; provide the query parameters without spaces or line breaks.

    * `projectId` is required.
    * Since `jobNames` and `jobStatuses` support multiple values, their values must be specified with array notation. `jobNames` and `jobStatuses` are optional. Valid values are case-insensitive: 
      * [ENABLED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob-Status#Google__Cloud__StorageTransfer__V1__TransferJob__Status__ENABLED "Google::Cloud::StorageTransfer::V1::TransferJob::Status::ENABLED \(constant\)")
      * [DISABLED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob-Status#Google__Cloud__StorageTransfer__V1__TransferJob__Status__DISABLED "Google::Cloud::StorageTransfer::V1::TransferJob::Status::DISABLED \(constant\)")
      * [DELETED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob-Status#Google__Cloud__StorageTransfer__V1__TransferJob__Status__DELETED "Google::Cloud::StorageTransfer::V1::TransferJob::Status::DELETED \(constant\)")
    * Specify `"dataBackend":"QUERY_REPLICATION_CONFIGS"` to return a list of cross-bucket replication jobs.
    * Limit the results to jobs from a particular bucket with `sourceBucket` and/or to a particular bucket with `sinkBucket`.



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Required. A list of query parameters specified as JSON text in the form of:

` { "projectId":"my_project_id", "jobNames":["jobid1","jobid2",...], "jobStatuses":["status1","status2",...], "dataBackend":"QUERY_REPLICATION_CONFIGS", "sourceBucket":"source-bucket-name", "sinkBucket":"sink-bucket-name", } `

The JSON formatting in the example is for display only; provide the query parameters without spaces or line breaks.

    * `projectId` is required.
    * Since `jobNames` and `jobStatuses` support multiple values, their values must be specified with array notation. `jobNames` and `jobStatuses` are optional. Valid values are case-insensitive: 
      * [ENABLED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob-Status#Google__Cloud__StorageTransfer__V1__TransferJob__Status__ENABLED "Google::Cloud::StorageTransfer::V1::TransferJob::Status::ENABLED \(constant\)")
      * [DISABLED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob-Status#Google__Cloud__StorageTransfer__V1__TransferJob__Status__DISABLED "Google::Cloud::StorageTransfer::V1::TransferJob::Status::DISABLED \(constant\)")
      * [DELETED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob-Status#Google__Cloud__StorageTransfer__V1__TransferJob__Status__DELETED "Google::Cloud::StorageTransfer::V1::TransferJob::Status::DELETED \(constant\)")
    * Specify `"dataBackend":"QUERY_REPLICATION_CONFIGS"` to return a list of cross-bucket replication jobs.
    * Limit the results to jobs from a particular bucket with `sourceBucket` and/or to a particular bucket with `sinkBucket`.



**Returns**

  * (::String) — 

Required. A list of query parameters specified as JSON text in the form of:

` { "projectId":"my_project_id", "jobNames":["jobid1","jobid2",...], "jobStatuses":["status1","status2",...], "dataBackend":"QUERY_REPLICATION_CONFIGS", "sourceBucket":"source-bucket-name", "sinkBucket":"sink-bucket-name", } `

The JSON formatting in the example is for display only; provide the query parameters without spaces or line breaks.

    * `projectId` is required.
    * Since `jobNames` and `jobStatuses` support multiple values, their values must be specified with array notation. `jobNames` and `jobStatuses` are optional. Valid values are case-insensitive: 
      * [ENABLED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob-Status#Google__Cloud__StorageTransfer__V1__TransferJob__Status__ENABLED "Google::Cloud::StorageTransfer::V1::TransferJob::Status::ENABLED \(constant\)")
      * [DISABLED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob-Status#Google__Cloud__StorageTransfer__V1__TransferJob__Status__DISABLED "Google::Cloud::StorageTransfer::V1::TransferJob::Status::DISABLED \(constant\)")
      * [DELETED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob-Status#Google__Cloud__StorageTransfer__V1__TransferJob__Status__DELETED "Google::Cloud::StorageTransfer::V1::TransferJob::Status::DELETED \(constant\)")
    * Specify `"dataBackend":"QUERY_REPLICATION_CONFIGS"` to return a list of cross-bucket replication jobs.
    * Limit the results to jobs from a particular bucket with `sourceBucket` and/or to a particular bucket with `sinkBucket`.



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — The list page size. The max allowed value is 256. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The list page size. The max allowed value is 256. 



**Returns**

  * (::Integer) — The list page size. The max allowed value is 256. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — The list page token. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — The list page token. 



**Returns**

  * (::String) — The list page token. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
