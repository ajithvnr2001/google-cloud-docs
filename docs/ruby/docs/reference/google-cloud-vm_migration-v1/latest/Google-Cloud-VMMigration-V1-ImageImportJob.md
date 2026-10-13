---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-ImageImportJob/
title: Migrate for Compute Engine V1 API - Class Google::Cloud::VMMigration::V1::ImageImportJob (v2.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:05.227284+00:00
---

# Migrate for Compute Engine V1 API - Class Google::Cloud::VMMigration::V1::ImageImportJob (v2.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-ImageImportJob/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Migrate for Compute Engine V1 API - Class Google::Cloud::VMMigration::V1::ImageImportJob (v2.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.1 (latest)  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.0  2.1.1  2.0.0  1.3.0  1.2.0  1.1.0  1.0.2  0.9.0  0.8.2  0.7.0  0.6.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Migrate for Compute Engine V1 API class Google::Cloud::VMMigration::V1::ImageImportJob.

ImageImportJob describes the progress and result of an image import.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #cloud_storage_uri
    
    
    def cloud_storage_uri() -> ::String

**Returns**

  * (::String) — Output only. The path to the Cloud Storage file from which the image should be imported. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time the image import was created (as an API call, not when it was actually created in the target). 



### #created_resources
    
    
    def created_resources() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. The resource paths of the resources created by the image import job. 



### #disk_image_target_details
    
    
    def disk_image_target_details() -> ::Google::Cloud::VMMigration::V1::DiskImageTargetDetails

**Returns**

  * ([::Google::Cloud::VMMigration::V1::DiskImageTargetDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-DiskImageTargetDetails)) — Output only. Target details used to import a disk image.

Note: The following fields are mutually exclusive: `disk_image_target_details`, `machine_image_target_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #end_time
    
    
    def end_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time the image import was ended. 



### #errors
    
    
    def errors() -> ::Array<::Google::Rpc::Status>

**Returns**

  * (::Array<[::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Rpc-Status)>) — Output only. Provides details on the error that led to the image import state in case of an error. 



### #machine_image_target_details
    
    
    def machine_image_target_details() -> ::Google::Cloud::VMMigration::V1::MachineImageTargetDetails

**Returns**

  * ([::Google::Cloud::VMMigration::V1::MachineImageTargetDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-MachineImageTargetDetails)) — Output only. Target details used to import a machine image.

Note: The following fields are mutually exclusive: `machine_image_target_details`, `disk_image_target_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The resource path of the ImageImportJob. 



### #state
    
    
    def state() -> ::Google::Cloud::VMMigration::V1::ImageImportJob::State

**Returns**

  * ([::Google::Cloud::VMMigration::V1::ImageImportJob::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-ImageImportJob-State)) — Output only. The state of the image import. 



### #steps
    
    
    def steps() -> ::Array<::Google::Cloud::VMMigration::V1::ImageImportStep>

**Returns**

  * (::Array<[::Google::Cloud::VMMigration::V1::ImageImportStep](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-ImageImportStep)>) — Output only. The image import steps list representing its progress. 



### #warnings
    
    
    def warnings() -> ::Array<::Google::Cloud::VMMigration::V1::MigrationWarning>

**Returns**

  * (::Array<[::Google::Cloud::VMMigration::V1::MigrationWarning](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-MigrationWarning)>) — Output only. Warnings that occurred during the image import. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
