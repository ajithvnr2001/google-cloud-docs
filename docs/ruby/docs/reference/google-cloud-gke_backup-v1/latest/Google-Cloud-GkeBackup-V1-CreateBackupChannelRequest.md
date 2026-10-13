---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-CreateBackupChannelRequest/
title: Backup for GKE V1 API - Class Google::Cloud::GkeBackup::V1::CreateBackupChannelRequest (v1.8.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:51:06.746212+00:00
---

# Backup for GKE V1 API - Class Google::Cloud::GkeBackup::V1::CreateBackupChannelRequest (v1.8.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-CreateBackupChannelRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup for GKE V1 API - Class Google::Cloud::GkeBackup::V1::CreateBackupChannelRequest (v1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.2  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Backup for GKE V1 API class Google::Cloud::GkeBackup::V1::CreateBackupChannelRequest.

Request message for CreateBackupChannel.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #backup_channel
    
    
    def backup_channel() -> ::Google::Cloud::GkeBackup::V1::BackupChannel

**Returns**

  * ([::Google::Cloud::GkeBackup::V1::BackupChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupChannel)) — Required. The BackupChannel resource object to create. 



### #backup_channel=
    
    
    def backup_channel=(value) -> ::Google::Cloud::GkeBackup::V1::BackupChannel

**Parameter**

  * **value** ([::Google::Cloud::GkeBackup::V1::BackupChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupChannel)) — Required. The BackupChannel resource object to create. 



**Returns**

  * ([::Google::Cloud::GkeBackup::V1::BackupChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupChannel)) — Required. The BackupChannel resource object to create. 



### #backup_channel_id
    
    
    def backup_channel_id() -> ::String

**Returns**

  * (::String) — 

Optional. The client-provided short name for the BackupChannel resource. This name must:

    * be between 1 and 63 characters long (inclusive)
    * consist of only lower-case ASCII letters, numbers, and dashes
    * start with a lower-case letter
    * end with a lower-case letter or number
    * be unique within the set of BackupChannels in this location If the user does not provide a name, a uuid will be used as the name.



### #backup_channel_id=
    
    
    def backup_channel_id=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. The client-provided short name for the BackupChannel resource. This name must:

    * be between 1 and 63 characters long (inclusive)
    * consist of only lower-case ASCII letters, numbers, and dashes
    * start with a lower-case letter
    * end with a lower-case letter or number
    * be unique within the set of BackupChannels in this location If the user does not provide a name, a uuid will be used as the name.



**Returns**

  * (::String) — 

Optional. The client-provided short name for the BackupChannel resource. This name must:

    * be between 1 and 63 characters long (inclusive)
    * consist of only lower-case ASCII letters, numbers, and dashes
    * start with a lower-case letter
    * end with a lower-case letter or number
    * be unique within the set of BackupChannels in this location If the user does not provide a name, a uuid will be used as the name.



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The location within which to create the BackupChannel. Format: `projects/*/locations/*`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The location within which to create the BackupChannel. Format: `projects/*/locations/*`



**Returns**

  * (::String) — Required. The location within which to create the BackupChannel. Format: `projects/*/locations/*`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-12 UTC."],[],[]] 
