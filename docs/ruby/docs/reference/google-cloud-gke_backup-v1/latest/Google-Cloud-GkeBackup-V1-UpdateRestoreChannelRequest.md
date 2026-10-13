---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-UpdateRestoreChannelRequest/
title: Backup for GKE V1 API - Class Google::Cloud::GkeBackup::V1::UpdateRestoreChannelRequest (v1.8.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:14.539529+00:00
---

# Backup for GKE V1 API - Class Google::Cloud::GkeBackup::V1::UpdateRestoreChannelRequest (v1.8.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-UpdateRestoreChannelRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup for GKE V1 API - Class Google::Cloud::GkeBackup::V1::UpdateRestoreChannelRequest (v1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.2  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Backup for GKE V1 API class Google::Cloud::GkeBackup::V1::UpdateRestoreChannelRequest.

Request message for UpdateRestoreChannel.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #restore_channel
    
    
    def restore_channel() -> ::Google::Cloud::GkeBackup::V1::RestoreChannel

**Returns**

  * ([::Google::Cloud::GkeBackup::V1::RestoreChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestoreChannel)) — Required. A new version of the RestoreChannel resource that contains updated fields. This may be sparsely populated if an `update_mask` is provided. 



### #restore_channel=
    
    
    def restore_channel=(value) -> ::Google::Cloud::GkeBackup::V1::RestoreChannel

**Parameter**

  * **value** ([::Google::Cloud::GkeBackup::V1::RestoreChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestoreChannel)) — Required. A new version of the RestoreChannel resource that contains updated fields. This may be sparsely populated if an `update_mask` is provided. 



**Returns**

  * ([::Google::Cloud::GkeBackup::V1::RestoreChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestoreChannel)) — Required. A new version of the RestoreChannel resource that contains updated fields. This may be sparsely populated if an `update_mask` is provided. 



### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Protobuf-FieldMask)) — Optional. This is used to specify the fields to be overwritten in the RestoreChannel targeted for update. The values for each of these updated fields will be taken from the `restore_channel` provided with this request. Field names are relative to the root of the resource (e.g., `description`, `destination_project_id`, etc.) If no `update_mask` is provided, all fields in `restore_channel` will be written to the target RestoreChannel resource. Note that OUTPUT_ONLY and IMMUTABLE fields in `restore_channel` are ignored and are not used to update the target RestoreChannel. 



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Protobuf-FieldMask)) — Optional. This is used to specify the fields to be overwritten in the RestoreChannel targeted for update. The values for each of these updated fields will be taken from the `restore_channel` provided with this request. Field names are relative to the root of the resource (e.g., `description`, `destination_project_id`, etc.) If no `update_mask` is provided, all fields in `restore_channel` will be written to the target RestoreChannel resource. Note that OUTPUT_ONLY and IMMUTABLE fields in `restore_channel` are ignored and are not used to update the target RestoreChannel. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Protobuf-FieldMask)) — Optional. This is used to specify the fields to be overwritten in the RestoreChannel targeted for update. The values for each of these updated fields will be taken from the `restore_channel` provided with this request. Field names are relative to the root of the resource (e.g., `description`, `destination_project_id`, etc.) If no `update_mask` is provided, all fields in `restore_channel` will be written to the target RestoreChannel resource. Note that OUTPUT_ONLY and IMMUTABLE fields in `restore_channel` are ignored and are not used to update the target RestoreChannel. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-12 UTC."],[],[]] 
