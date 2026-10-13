---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-DiskMigrationJobTargetDetails/
title: Migrate for Compute Engine V1 API - Class Google::Cloud::VMMigration::V1::DiskMigrationJobTargetDetails (v2.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:03.520346+00:00
---

# Migrate for Compute Engine V1 API - Class Google::Cloud::VMMigration::V1::DiskMigrationJobTargetDetails (v2.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-DiskMigrationJobTargetDetails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Migrate for Compute Engine V1 API - Class Google::Cloud::VMMigration::V1::DiskMigrationJobTargetDetails (v2.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.1 (latest)  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.0  2.1.1  2.0.0  1.3.0  1.2.0  1.1.0  1.0.2  0.9.0  0.8.2  0.7.0  0.6.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Migrate for Compute Engine V1 API class Google::Cloud::VMMigration::V1::DiskMigrationJobTargetDetails.

Details of the target disk in Compute Engine.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #encryption
    
    
    def encryption() -> ::Google::Cloud::VMMigration::V1::Encryption

**Returns**

  * ([::Google::Cloud::VMMigration::V1::Encryption](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-Encryption)) — Optional. The encryption to apply to the disk. If the DiskMigrationJob parent Source resource has an encryption, this field must be set to the same encryption key. 



### #encryption=
    
    
    def encryption=(value) -> ::Google::Cloud::VMMigration::V1::Encryption

**Parameter**

  * **value** ([::Google::Cloud::VMMigration::V1::Encryption](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-Encryption)) — Optional. The encryption to apply to the disk. If the DiskMigrationJob parent Source resource has an encryption, this field must be set to the same encryption key. 



**Returns**

  * ([::Google::Cloud::VMMigration::V1::Encryption](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-Encryption)) — Optional. The encryption to apply to the disk. If the DiskMigrationJob parent Source resource has an encryption, this field must be set to the same encryption key. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. A map of labels to associate with the disk. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. A map of labels to associate with the disk. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. A map of labels to associate with the disk. 



### #target_disk
    
    
    def target_disk() -> ::Google::Cloud::VMMigration::V1::ComputeEngineDisk

**Returns**

  * ([::Google::Cloud::VMMigration::V1::ComputeEngineDisk](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-ComputeEngineDisk)) — Required. The target disk. 



### #target_disk=
    
    
    def target_disk=(value) -> ::Google::Cloud::VMMigration::V1::ComputeEngineDisk

**Parameter**

  * **value** ([::Google::Cloud::VMMigration::V1::ComputeEngineDisk](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-ComputeEngineDisk)) — Required. The target disk. 



**Returns**

  * ([::Google::Cloud::VMMigration::V1::ComputeEngineDisk](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-ComputeEngineDisk)) — Required. The target disk. 



### #target_project
    
    
    def target_project() -> ::String

**Returns**

  * (::String) — Required. The name of the resource of type TargetProject which represents the Compute Engine project in which to create the disk. Should be of the form: projects/{project}/locations/global/targetProjects/{target-project} 



### #target_project=
    
    
    def target_project=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the resource of type TargetProject which represents the Compute Engine project in which to create the disk. Should be of the form: projects/{project}/locations/global/targetProjects/{target-project} 



**Returns**

  * (::String) — Required. The name of the resource of type TargetProject which represents the Compute Engine project in which to create the disk. Should be of the form: projects/{project}/locations/global/targetProjects/{target-project} 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
