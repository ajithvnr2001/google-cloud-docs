---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-UpdateDiskMigrationJobRequest/
title: Migrate for Compute Engine V1 API - Class Google::Cloud::VMMigration::V1::UpdateDiskMigrationJobRequest (v2.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:10.549058+00:00
---

# Migrate for Compute Engine V1 API - Class Google::Cloud::VMMigration::V1::UpdateDiskMigrationJobRequest (v2.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-UpdateDiskMigrationJobRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Migrate for Compute Engine V1 API - Class Google::Cloud::VMMigration::V1::UpdateDiskMigrationJobRequest (v2.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.1 (latest)  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.0  2.1.1  2.0.0  1.3.0  1.2.0  1.1.0  1.0.2  0.9.0  0.8.2  0.7.0  0.6.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Migrate for Compute Engine V1 API class Google::Cloud::VMMigration::V1::UpdateDiskMigrationJobRequest.

Request message for 'UpdateDiskMigrationJob' request.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #disk_migration_job
    
    
    def disk_migration_job() -> ::Google::Cloud::VMMigration::V1::DiskMigrationJob

**Returns**

  * ([::Google::Cloud::VMMigration::V1::DiskMigrationJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-DiskMigrationJob)) — Required. The update request body. 



### #disk_migration_job=
    
    
    def disk_migration_job=(value) -> ::Google::Cloud::VMMigration::V1::DiskMigrationJob

**Parameter**

  * **value** ([::Google::Cloud::VMMigration::V1::DiskMigrationJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-DiskMigrationJob)) — Required. The update request body. 



**Returns**

  * ([::Google::Cloud::VMMigration::V1::DiskMigrationJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-DiskMigrationJob)) — Required. The update request body. 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request timed out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request timed out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Returns**

  * (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request timed out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Protobuf-FieldMask)) — Optional. Field mask is used to specify the fields to be overwritten in the DiskMigrationJob resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask, then a mask equivalent to all fields that are populated (have a non-empty value), will be implied. 



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Protobuf-FieldMask)) — Optional. Field mask is used to specify the fields to be overwritten in the DiskMigrationJob resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask, then a mask equivalent to all fields that are populated (have a non-empty value), will be implied. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Protobuf-FieldMask)) — Optional. Field mask is used to specify the fields to be overwritten in the DiskMigrationJob resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask, then a mask equivalent to all fields that are populated (have a non-empty value), will be implied. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
