---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-GetBackupRequest/
title: Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::GetBackupRequest (v0.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:35.234021+00:00
---

# Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::GetBackupRequest (v0.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-GetBackupRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::GetBackupRequest (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the Backup and DR Service V1BETA API class Google::Cloud::BackupDR::V1beta::GetBackupRequest.

Request message for getting a Backup.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. Name of the data source resource name, in the format 'projects/{project_id}/locations/{location}/backupVaults/{backupVault}/dataSources/{datasource}/backups/{backup}' 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Name of the data source resource name, in the format 'projects/{project_id}/locations/{location}/backupVaults/{backupVault}/dataSources/{datasource}/backups/{backup}' 



**Returns**

  * (::String) — Required. Name of the data source resource name, in the format 'projects/{project_id}/locations/{location}/backupVaults/{backupVault}/dataSources/{datasource}/backups/{backup}' 



### #view
    
    
    def view() -> ::Google::Cloud::BackupDR::V1beta::BackupView

**Returns**

  * ([::Google::Cloud::BackupDR::V1beta::BackupView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-BackupView)) — Optional. Reserved for future use to provide a BASIC & FULL view of Backup resource. 



### #view=
    
    
    def view=(value) -> ::Google::Cloud::BackupDR::V1beta::BackupView

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1beta::BackupView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-BackupView)) — Optional. Reserved for future use to provide a BASIC & FULL view of Backup resource. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1beta::BackupView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-BackupView)) — Optional. Reserved for future use to provide a BASIC & FULL view of Backup resource. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
