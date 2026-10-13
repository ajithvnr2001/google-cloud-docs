---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GcpBackupConfig/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::GcpBackupConfig (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:49.285285+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::GcpBackupConfig (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GcpBackupConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::GcpBackupConfig (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::GcpBackupConfig.

GcpBackupConfig captures the Backup configuration details for Google Cloud resources. All Google Cloud resources regardless of type are protected with backup plan associations.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #backup_plan
    
    
    def backup_plan() -> ::String

**Returns**

  * (::String) — The name of the backup plan. 



### #backup_plan=
    
    
    def backup_plan=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the backup plan. 



**Returns**

  * (::String) — The name of the backup plan. 



### #backup_plan_association
    
    
    def backup_plan_association() -> ::String

**Returns**

  * (::String) — The name of the backup plan association. 



### #backup_plan_association=
    
    
    def backup_plan_association=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the backup plan association. 



**Returns**

  * (::String) — The name of the backup plan association. 



### #backup_plan_description
    
    
    def backup_plan_description() -> ::String

**Returns**

  * (::String) — The description of the backup plan. 



### #backup_plan_description=
    
    
    def backup_plan_description=(value) -> ::String

**Parameter**

  * **value** (::String) — The description of the backup plan. 



**Returns**

  * (::String) — The description of the backup plan. 



### #backup_plan_revision_id
    
    
    def backup_plan_revision_id() -> ::String

**Returns**

  * (::String) — The user friendly id of the backup plan revision. E.g. v0, v1 etc. 



### #backup_plan_revision_id=
    
    
    def backup_plan_revision_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The user friendly id of the backup plan revision. E.g. v0, v1 etc. 



**Returns**

  * (::String) — The user friendly id of the backup plan revision. E.g. v0, v1 etc. 



### #backup_plan_revision_name
    
    
    def backup_plan_revision_name() -> ::String

**Returns**

  * (::String) — The name of the backup plan revision. 



### #backup_plan_revision_name=
    
    
    def backup_plan_revision_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the backup plan revision. 



**Returns**

  * (::String) — The name of the backup plan revision. 



### #backup_plan_rules
    
    
    def backup_plan_rules() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The names of the backup plan rules which point to this backupvault 



### #backup_plan_rules=
    
    
    def backup_plan_rules=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The names of the backup plan rules which point to this backupvault 



**Returns**

  * (::Array<::String>) — The names of the backup plan rules which point to this backupvault 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
