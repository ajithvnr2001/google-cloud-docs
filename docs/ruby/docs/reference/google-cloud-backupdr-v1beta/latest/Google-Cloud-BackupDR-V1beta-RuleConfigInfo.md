---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-RuleConfigInfo/
title: Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::RuleConfigInfo (v0.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:46.451357+00:00
---

# Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::RuleConfigInfo (v0.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-RuleConfigInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::RuleConfigInfo (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the Backup and DR Service V1BETA API class Google::Cloud::BackupDR::V1beta::RuleConfigInfo.

Message for rules config info.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #last_backup_error
    
    
    def last_backup_error() -> ::Google::Rpc::Status

**Returns**

  * ([::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Rpc-Status)) — Output only. google.rpc.Status object to store the last backup error. 



### #last_backup_state
    
    
    def last_backup_state() -> ::Google::Cloud::BackupDR::V1beta::RuleConfigInfo::LastBackupState

**Returns**

  * ([::Google::Cloud::BackupDR::V1beta::RuleConfigInfo::LastBackupState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-RuleConfigInfo-LastBackupState)) — Output only. The last backup state for rule. 



### #last_successful_backup_consistency_time
    
    
    def last_successful_backup_consistency_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Protobuf-Timestamp)) — Output only. The point in time when the last successful backup was captured from the source. 



### #rule_id
    
    
    def rule_id() -> ::String

**Returns**

  * (::String) — Output only. Backup Rule id fetched from backup plan. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
