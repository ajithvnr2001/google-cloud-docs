---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Operation/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::Operation (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:48.450374+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::Operation (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Operation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::Operation (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::Operation.

Represents an Operation resource.

Google Compute Engine has three Operation resources:

  * [Global](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalOperations)
  * [Regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionOperations)
  * [Zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations)



You can use an operation resource to manage asynchronous API requests. For more information, readHandling API responses.

Operations can be global, regional or zonal.

  * For global operations, use the `globalOperations` resource.
  * For regional operations, use the `regionOperations` resource.
  * For zonal operations, use the `zoneOperations` resource.



For more information, read Global, Regional, and Zonal Resources.

Note that completed Operation resources have a limited retention period.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #client_operation_id
    
    
    def client_operation_id() -> ::String

**Returns**

  * (::String) — [Output Only] The value of `requestId` if you provided it in the request. Not present otherwise. 



### #client_operation_id=
    
    
    def client_operation_id=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] The value of `requestId` if you provided it in the request. Not present otherwise. 



**Returns**

  * (::String) — [Output Only] The value of `requestId` if you provided it in the request. Not present otherwise. 



### #creation_timestamp
    
    
    def creation_timestamp() -> ::String

**Returns**

  * (::String) — [Deprecated] This field is deprecated. 



### #creation_timestamp=
    
    
    def creation_timestamp=(value) -> ::String

**Parameter**

  * **value** (::String) — [Deprecated] This field is deprecated. 



**Returns**

  * (::String) — [Deprecated] This field is deprecated. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — [Output Only] A textual description of the operation, which is set when the operation is created. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] A textual description of the operation, which is set when the operation is created. 



**Returns**

  * (::String) — [Output Only] A textual description of the operation, which is set when the operation is created. 



### #end_time
    
    
    def end_time() -> ::String

**Returns**

  * (::String) — [Output Only] The time that this operation was completed. This value is inRFC3339 text format. 



### #end_time=
    
    
    def end_time=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] The time that this operation was completed. This value is inRFC3339 text format. 



**Returns**

  * (::String) — [Output Only] The time that this operation was completed. This value is inRFC3339 text format. 



### #error
    
    
    def error() -> ::Google::Cloud::Compute::V1::Error

**Returns**

  * ([::Google::Cloud::Compute::V1::Error](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Error)) — [Output Only] If errors are generated during processing of the operation, this field will be populated. 



### #error=
    
    
    def error=(value) -> ::Google::Cloud::Compute::V1::Error

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::Error](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Error)) — [Output Only] If errors are generated during processing of the operation, this field will be populated. 



**Returns**

  * ([::Google::Cloud::Compute::V1::Error](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Error)) — [Output Only] If errors are generated during processing of the operation, this field will be populated. 



### #get_health_operation_metadata
    
    
    def get_health_operation_metadata() -> ::Google::Cloud::Compute::V1::GetHealthOperationMetadata

**Returns**

  * ([::Google::Cloud::Compute::V1::GetHealthOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetHealthOperationMetadata)) — Output only. Metadata for GetHealth operations. 



### #get_health_operation_metadata=
    
    
    def get_health_operation_metadata=(value) -> ::Google::Cloud::Compute::V1::GetHealthOperationMetadata

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::GetHealthOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetHealthOperationMetadata)) — Output only. Metadata for GetHealth operations. 



**Returns**

  * ([::Google::Cloud::Compute::V1::GetHealthOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetHealthOperationMetadata)) — Output only. Metadata for GetHealth operations. 



### #get_version_operation_metadata
    
    
    def get_version_operation_metadata() -> ::Google::Cloud::Compute::V1::GetVersionOperationMetadata

**Returns**

  * ([::Google::Cloud::Compute::V1::GetVersionOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetVersionOperationMetadata)) 



### #get_version_operation_metadata=
    
    
    def get_version_operation_metadata=(value) -> ::Google::Cloud::Compute::V1::GetVersionOperationMetadata

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::GetVersionOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetVersionOperationMetadata)) 



**Returns**

  * ([::Google::Cloud::Compute::V1::GetVersionOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetVersionOperationMetadata)) 



### #http_error_message
    
    
    def http_error_message() -> ::String

**Returns**

  * (::String) — [Output Only] If the operation fails, this field contains the HTTP error message that was returned, such as `NOT FOUND`. 



### #http_error_message=
    
    
    def http_error_message=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] If the operation fails, this field contains the HTTP error message that was returned, such as `NOT FOUND`. 



**Returns**

  * (::String) — [Output Only] If the operation fails, this field contains the HTTP error message that was returned, such as `NOT FOUND`. 



### #http_error_status_code
    
    
    def http_error_status_code() -> ::Integer

**Returns**

  * (::Integer) — [Output Only] If the operation fails, this field contains the HTTP error status code that was returned. For example, a `404` means the resource was not found. 



### #http_error_status_code=
    
    
    def http_error_status_code=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — [Output Only] If the operation fails, this field contains the HTTP error status code that was returned. For example, a `404` means the resource was not found. 



**Returns**

  * (::Integer) — [Output Only] If the operation fails, this field contains the HTTP error status code that was returned. For example, a `404` means the resource was not found. 



### #id
    
    
    def id() -> ::Integer

**Returns**

  * (::Integer) — [Output Only] The unique identifier for the operation. This identifier is defined by the server. 



### #id=
    
    
    def id=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — [Output Only] The unique identifier for the operation. This identifier is defined by the server. 



**Returns**

  * (::Integer) — [Output Only] The unique identifier for the operation. This identifier is defined by the server. 



### #insert_time
    
    
    def insert_time() -> ::String

**Returns**

  * (::String) — [Output Only] The time that this operation was requested. This value is inRFC3339 text format. 



### #insert_time=
    
    
    def insert_time=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] The time that this operation was requested. This value is inRFC3339 text format. 



**Returns**

  * (::String) — [Output Only] The time that this operation was requested. This value is inRFC3339 text format. 



### #instances_bulk_insert_operation_metadata
    
    
    def instances_bulk_insert_operation_metadata() -> ::Google::Cloud::Compute::V1::InstancesBulkInsertOperationMetadata

**Returns**

  * ([::Google::Cloud::Compute::V1::InstancesBulkInsertOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstancesBulkInsertOperationMetadata)) 



### #instances_bulk_insert_operation_metadata=
    
    
    def instances_bulk_insert_operation_metadata=(value) -> ::Google::Cloud::Compute::V1::InstancesBulkInsertOperationMetadata

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::InstancesBulkInsertOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstancesBulkInsertOperationMetadata)) 



**Returns**

  * ([::Google::Cloud::Compute::V1::InstancesBulkInsertOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstancesBulkInsertOperationMetadata)) 



### #kind
    
    
    def kind() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Type of the resource. Always `compute#operation` for Operation resources. 



### #kind=
    
    
    def kind=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Type of the resource. Always `compute#operation` for Operation resources. 



**Returns**

  * (::String) — Output only. [Output Only] Type of the resource. Always `compute#operation` for Operation resources. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — [Output Only] Name of the operation. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] Name of the operation. 



**Returns**

  * (::String) — [Output Only] Name of the operation. 



### #operation_group_id
    
    
    def operation_group_id() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] An ID that represents a group of operations, such as when a group of operations results from a `bulkInsert` API request. 



### #operation_group_id=
    
    
    def operation_group_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] An ID that represents a group of operations, such as when a group of operations results from a `bulkInsert` API request. 



**Returns**

  * (::String) — Output only. [Output Only] An ID that represents a group of operations, such as when a group of operations results from a `bulkInsert` API request. 



### #operation_type
    
    
    def operation_type() -> ::String

**Returns**

  * (::String) — [Output Only] The type of operation, such as `insert`, `update`, or `delete`, and so on. 



### #operation_type=
    
    
    def operation_type=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] The type of operation, such as `insert`, `update`, or `delete`, and so on. 



**Returns**

  * (::String) — [Output Only] The type of operation, such as `insert`, `update`, or `delete`, and so on. 



### #progress
    
    
    def progress() -> ::Integer

**Returns**

  * (::Integer) — [Output Only] An optional progress indicator that ranges from 0 to 100. There is no requirement that this be linear or support any granularity of operations. This should not be used to guess when the operation will be complete. This number should monotonically increase as the operation progresses. 



### #progress=
    
    
    def progress=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — [Output Only] An optional progress indicator that ranges from 0 to 100. There is no requirement that this be linear or support any granularity of operations. This should not be used to guess when the operation will be complete. This number should monotonically increase as the operation progresses. 



**Returns**

  * (::Integer) — [Output Only] An optional progress indicator that ranges from 0 to 100. There is no requirement that this be linear or support any granularity of operations. This should not be used to guess when the operation will be complete. This number should monotonically increase as the operation progresses. 



### #region
    
    
    def region() -> ::String

**Returns**

  * (::String) — [Output Only] The URL of the region where the operation resides. Only applicable when performing regional operations. 



### #region=
    
    
    def region=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] The URL of the region where the operation resides. Only applicable when performing regional operations. 



**Returns**

  * (::String) — [Output Only] The URL of the region where the operation resides. Only applicable when performing regional operations. 



### #self_link
    
    
    def self_link() -> ::String

**Returns**

  * (::String) — [Output Only] Server-defined URL for the resource. 



### #self_link=
    
    
    def self_link=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] Server-defined URL for the resource. 



**Returns**

  * (::String) — [Output Only] Server-defined URL for the resource. 



### #set_common_instance_metadata_operation_metadata
    
    
    def set_common_instance_metadata_operation_metadata() -> ::Google::Cloud::Compute::V1::SetCommonInstanceMetadataOperationMetadata

**Returns**

  * ([::Google::Cloud::Compute::V1::SetCommonInstanceMetadataOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-SetCommonInstanceMetadataOperationMetadata)) — Output only. [Output Only] If the operation is for projects.setCommonInstanceMetadata, this field will contain information on all underlying zonal actions and their state. 



### #set_common_instance_metadata_operation_metadata=
    
    
    def set_common_instance_metadata_operation_metadata=(value) -> ::Google::Cloud::Compute::V1::SetCommonInstanceMetadataOperationMetadata

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::SetCommonInstanceMetadataOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-SetCommonInstanceMetadataOperationMetadata)) — Output only. [Output Only] If the operation is for projects.setCommonInstanceMetadata, this field will contain information on all underlying zonal actions and their state. 



**Returns**

  * ([::Google::Cloud::Compute::V1::SetCommonInstanceMetadataOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-SetCommonInstanceMetadataOperationMetadata)) — Output only. [Output Only] If the operation is for projects.setCommonInstanceMetadata, this field will contain information on all underlying zonal actions and their state. 



### #start_time
    
    
    def start_time() -> ::String

**Returns**

  * (::String) — [Output Only] The time that this operation was started by the server. This value is inRFC3339 text format. 



### #start_time=
    
    
    def start_time=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] The time that this operation was started by the server. This value is inRFC3339 text format. 



**Returns**

  * (::String) — [Output Only] The time that this operation was started by the server. This value is inRFC3339 text format. 



### #status
    
    
    def status() -> ::Google::Cloud::Compute::V1::Operation::Status

**Returns**

  * ([::Google::Cloud::Compute::V1::Operation::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Operation-Status)) — [Output Only] The status of the operation, which can be one of the following: `PENDING`, `RUNNING`, or `DONE`. 



### #status=
    
    
    def status=(value) -> ::Google::Cloud::Compute::V1::Operation::Status

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::Operation::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Operation-Status)) — [Output Only] The status of the operation, which can be one of the following: `PENDING`, `RUNNING`, or `DONE`. 



**Returns**

  * ([::Google::Cloud::Compute::V1::Operation::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Operation-Status)) — [Output Only] The status of the operation, which can be one of the following: `PENDING`, `RUNNING`, or `DONE`. 



### #status_message
    
    
    def status_message() -> ::String

**Returns**

  * (::String) — [Output Only] An optional textual description of the current status of the operation. 



### #status_message=
    
    
    def status_message=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] An optional textual description of the current status of the operation. 



**Returns**

  * (::String) — [Output Only] An optional textual description of the current status of the operation. 



### #target_id
    
    
    def target_id() -> ::Integer

**Returns**

  * (::Integer) — [Output Only] The unique target ID, which identifies a specific incarnation of the target resource. 



### #target_id=
    
    
    def target_id=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — [Output Only] The unique target ID, which identifies a specific incarnation of the target resource. 



**Returns**

  * (::Integer) — [Output Only] The unique target ID, which identifies a specific incarnation of the target resource. 



### #target_link
    
    
    def target_link() -> ::String

**Returns**

  * (::String) — [Output Only] The URL of the resource that the operation modifies. For operations related to creating a snapshot, this points to the disk that the snapshot was created from. 



### #target_link=
    
    
    def target_link=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] The URL of the resource that the operation modifies. For operations related to creating a snapshot, this points to the disk that the snapshot was created from. 



**Returns**

  * (::String) — [Output Only] The URL of the resource that the operation modifies. For operations related to creating a snapshot, this points to the disk that the snapshot was created from. 



### #user
    
    
    def user() -> ::String

**Returns**

  * (::String) — [Output Only] User who requested the operation, for example: `user@example.com` or `alice_smith_identifier (global/workforcePools/example-com-us-employees)`. 



### #user=
    
    
    def user=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] User who requested the operation, for example: `user@example.com` or `alice_smith_identifier (global/workforcePools/example-com-us-employees)`. 



**Returns**

  * (::String) — [Output Only] User who requested the operation, for example: `user@example.com` or `alice_smith_identifier (global/workforcePools/example-com-us-employees)`. 



### #warnings
    
    
    def warnings() -> ::Array<::Google::Cloud::Compute::V1::Warnings>

**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::Warnings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Warnings)>) — [Output Only] If warning messages are generated during processing of the operation, this field will be populated. 



### #warnings=
    
    
    def warnings=(value) -> ::Array<::Google::Cloud::Compute::V1::Warnings>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Compute::V1::Warnings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Warnings)>) — [Output Only] If warning messages are generated during processing of the operation, this field will be populated. 



**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::Warnings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Warnings)>) — [Output Only] If warning messages are generated during processing of the operation, this field will be populated. 



### #zone
    
    
    def zone() -> ::String

**Returns**

  * (::String) — [Output Only] The URL of the zone where the operation resides. Only applicable when performing per-zone operations. 



### #zone=
    
    
    def zone=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] The URL of the zone where the operation resides. Only applicable when performing per-zone operations. 



**Returns**

  * (::String) — [Output Only] The URL of the zone where the operation resides. Only applicable when performing per-zone operations. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
