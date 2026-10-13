---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Backup-GCPBackupPlanInfo/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::Backup::GCPBackupPlanInfo (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:27.561901+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::Backup::GCPBackupPlanInfo (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Backup-GCPBackupPlanInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::Backup::GCPBackupPlanInfo (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::Backup::GCPBackupPlanInfo.

GCPBackupPlanInfo captures the plan configuration details of Google Cloud resources at the time of backup.

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

  * (::String) — Resource name of backup plan by which workload is protected at the time of the backup. Format: projects/{project}/locations/{location}/backupPlans/{backupPlanId} 



### #backup_plan=
    
    
    def backup_plan=(value) -> ::String

**Parameter**

  * **value** (::String) — Resource name of backup plan by which workload is protected at the time of the backup. Format: projects/{project}/locations/{location}/backupPlans/{backupPlanId} 



**Returns**

  * (::String) — Resource name of backup plan by which workload is protected at the time of the backup. Format: projects/{project}/locations/{location}/backupPlans/{backupPlanId} 



### #backup_plan_revision_id
    
    
    def backup_plan_revision_id() -> ::String

**Returns**

  * (::String) — The user friendly id of the backup plan revision which triggered this backup in case of scheduled backup or used for on demand backup. 



### #backup_plan_revision_id=
    
    
    def backup_plan_revision_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The user friendly id of the backup plan revision which triggered this backup in case of scheduled backup or used for on demand backup. 



**Returns**

  * (::String) — The user friendly id of the backup plan revision which triggered this backup in case of scheduled backup or used for on demand backup. 



### #backup_plan_revision_name
    
    
    def backup_plan_revision_name() -> ::String

**Returns**

  * (::String) — Resource name of the backup plan revision which triggered this backup in case of scheduled backup or used for on demand backup. Format: projects/{project}/locations/{location}/backupPlans/{backupPlanId}/revisions/{revisionId} 



### #backup_plan_revision_name=
    
    
    def backup_plan_revision_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Resource name of the backup plan revision which triggered this backup in case of scheduled backup or used for on demand backup. Format: projects/{project}/locations/{location}/backupPlans/{backupPlanId}/revisions/{revisionId} 



**Returns**

  * (::String) — Resource name of the backup plan revision which triggered this backup in case of scheduled backup or used for on demand backup. Format: projects/{project}/locations/{location}/backupPlans/{backupPlanId}/revisions/{revisionId} 



### #backup_plan_rule_id
    
    
    def backup_plan_rule_id() -> ::String

**Returns**

  * (::String) — The rule id of the backup plan which triggered this backup in case of scheduled backup or used for 



### #backup_plan_rule_id=
    
    
    def backup_plan_rule_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The rule id of the backup plan which triggered this backup in case of scheduled backup or used for 



**Returns**

  * (::String) — The rule id of the backup plan which triggered this backup in case of scheduled backup or used for 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
