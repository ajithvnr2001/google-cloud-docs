---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupConfigDetails/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupConfigDetails (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:29.278786+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupConfigDetails (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupConfigDetails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupConfigDetails (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::BackupConfigDetails.

BackupConfigDetails has information about how the resource is configured for backups and about the most recent backup taken for this configuration.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #applicable_resource
    
    
    def applicable_resource() -> ::String

**Returns**

  * (::String) — Output only. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the resource that is applicable for the backup configuration. Example: "//compute.googleapis.com/projects/{project}/zones/{zone}/instances/{instance}" 



### #backup_config_source
    
    
    def backup_config_source() -> ::String

**Returns**

  * (::String) — Output only. The full resource name of the backup config source resource. For example, "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupPlans/{backupplanId}" or "//compute.googleapis.com/projects/{project}/locations/{region}/resourcePolicies/{resourcePolicyId}". 



### #backup_config_source_display_name
    
    
    def backup_config_source_display_name() -> ::String

**Returns**

  * (::String) — Output only. The display name of the backup config source resource. 



### #backup_dr_plan_config
    
    
    def backup_dr_plan_config() -> ::Google::Cloud::BackupDR::V1::BackupDrPlanConfig

**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupDrPlanConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDrPlanConfig)) — Google Cloud Backup and DR's Backup Plan specific data.

Note: The following fields are mutually exclusive: `backup_dr_plan_config`, `backup_dr_template_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #backup_dr_plan_config=
    
    
    def backup_dr_plan_config=(value) -> ::Google::Cloud::BackupDR::V1::BackupDrPlanConfig

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::BackupDrPlanConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDrPlanConfig)) — Google Cloud Backup and DR's Backup Plan specific data.

Note: The following fields are mutually exclusive: `backup_dr_plan_config`, `backup_dr_template_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupDrPlanConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDrPlanConfig)) — Google Cloud Backup and DR's Backup Plan specific data.

Note: The following fields are mutually exclusive: `backup_dr_plan_config`, `backup_dr_template_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #backup_dr_template_config
    
    
    def backup_dr_template_config() -> ::Google::Cloud::BackupDR::V1::BackupDrTemplateConfig

**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupDrTemplateConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDrTemplateConfig)) — Google Cloud Backup and DR's Template specific data.

Note: The following fields are mutually exclusive: `backup_dr_template_config`, `backup_dr_plan_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #backup_dr_template_config=
    
    
    def backup_dr_template_config=(value) -> ::Google::Cloud::BackupDR::V1::BackupDrTemplateConfig

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::BackupDrTemplateConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDrTemplateConfig)) — Google Cloud Backup and DR's Template specific data.

Note: The following fields are mutually exclusive: `backup_dr_template_config`, `backup_dr_plan_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupDrTemplateConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDrTemplateConfig)) — Google Cloud Backup and DR's Template specific data.

Note: The following fields are mutually exclusive: `backup_dr_template_config`, `backup_dr_plan_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #backup_locations
    
    
    def backup_locations() -> ::Array<::Google::Cloud::BackupDR::V1::BackupLocation>

**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::BackupLocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupLocation)>) — The locations where the backups are to be stored. 



### #backup_locations=
    
    
    def backup_locations=(value) -> ::Array<::Google::Cloud::BackupDR::V1::BackupLocation>

**Parameter**

  * **value** (::Array<[::Google::Cloud::BackupDR::V1::BackupLocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupLocation)>) — The locations where the backups are to be stored. 



**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::BackupLocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupLocation)>) — The locations where the backups are to be stored. 



### #backup_vault
    
    
    def backup_vault() -> ::String

**Returns**

  * (::String) — Output only. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the backup vault that will store the backups generated through this backup configuration. Example: "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupVaults/{backupvaultId}" 



### #latest_successful_backup_time
    
    
    def latest_successful_backup_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp of the latest successful backup created via this backup configuration. 



### #pitr_settings
    
    
    def pitr_settings() -> ::Google::Cloud::BackupDR::V1::PitrSettings

**Returns**

  * ([::Google::Cloud::BackupDR::V1::PitrSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-PitrSettings)) — Output only. Point in time recovery settings of the backup configuration resource. 



### #state
    
    
    def state() -> ::Google::Cloud::BackupDR::V1::BackupConfigDetails::State

**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupConfigDetails::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupConfigDetails-State)) — Output only. The state of the backup config resource. 



### #type
    
    
    def type() -> ::Google::Cloud::BackupDR::V1::BackupConfigDetails::Type

**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupConfigDetails::Type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupConfigDetails-Type)) — Output only. The type of the backup config resource. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
