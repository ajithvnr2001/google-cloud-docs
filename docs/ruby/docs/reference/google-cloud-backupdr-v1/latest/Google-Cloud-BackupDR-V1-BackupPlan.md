---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlan/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupPlan (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:36.656227+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupPlan (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupPlan (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::BackupPlan.

A `BackupPlan` specifies some common fields, such as `description` as well as one or more `BackupRule` messages. Each `BackupRule` has a retention policy and defines a schedule by which the system is to perform backup workloads.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #backup_rules
    
    
    def backup_rules() -> ::Array<::Google::Cloud::BackupDR::V1::BackupRule>

**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::BackupRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupRule)>) — Required. The backup rules for this `BackupPlan`. There must be at least one `BackupRule` message. 



### #backup_rules=
    
    
    def backup_rules=(value) -> ::Array<::Google::Cloud::BackupDR::V1::BackupRule>

**Parameter**

  * **value** (::Array<[::Google::Cloud::BackupDR::V1::BackupRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupRule)>) — Required. The backup rules for this `BackupPlan`. There must be at least one `BackupRule` message. 



**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::BackupRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupRule)>) — Required. The backup rules for this `BackupPlan`. There must be at least one `BackupRule` message. 



### #backup_vault
    
    
    def backup_vault() -> ::String

**Returns**

  * (::String) — Required. Resource name of backup vault which will be used as storage location for backups. Format: projects/{project}/locations/{location}/backupVaults/{backupvault} 



### #backup_vault=
    
    
    def backup_vault=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Resource name of backup vault which will be used as storage location for backups. Format: projects/{project}/locations/{location}/backupVaults/{backupvault} 



**Returns**

  * (::String) — Required. Resource name of backup vault which will be used as storage location for backups. Format: projects/{project}/locations/{location}/backupVaults/{backupvault} 



### #backup_vault_service_account
    
    
    def backup_vault_service_account() -> ::String

**Returns**

  * (::String) — Output only. The Google Cloud Platform Service Account to be used by the BackupVault for taking backups. Specify the email address of the Backup Vault Service Account. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Output only. When the `BackupPlan` was created. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. The description of the `BackupPlan` resource.

The description allows for additional details about `BackupPlan` and its use cases to be provided. An example description is the following: "This is a backup plan that performs a daily backup at 6pm and retains data for 3 months". The description must be at most 2048 characters. 




### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The description of the `BackupPlan` resource.

The description allows for additional details about `BackupPlan` and its use cases to be provided. An example description is the following: "This is a backup plan that performs a daily backup at 6pm and retains data for 3 months". The description must be at most 2048 characters. 




**Returns**

  * (::String) — Optional. The description of the `BackupPlan` resource.

The description allows for additional details about `BackupPlan` and its use cases to be provided. An example description is the following: "This is a backup plan that performs a daily backup at 6pm and retains data for 3 months". The description must be at most 2048 characters. 




### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — Optional. `etag` is returned from the service in the response. As a user of the service, you may provide an etag value in this field to prevent stale resources. 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. `etag` is returned from the service in the response. As a user of the service, you may provide an etag value in this field to prevent stale resources. 



**Returns**

  * (::String) — Optional. `etag` is returned from the service in the response. As a user of the service, you may provide an etag value in this field to prevent stale resources. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. This collection of key/value pairs allows for custom labels to be supplied by the user. Example, {"tag": "Weekly"}. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. This collection of key/value pairs allows for custom labels to be supplied by the user. Example, {"tag": "Weekly"}. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. This collection of key/value pairs allows for custom labels to be supplied by the user. Example, {"tag": "Weekly"}. 



### #log_retention_days
    
    
    def log_retention_days() -> ::Integer

**Returns**

  * (::Integer) — Optional. Applicable only for CloudSQL and AlloyDB resource_type.

Configures how long logs will be stored. It is defined in “days”. This value should be greater than or equal to minimum enforced log retention duration of the backup vault. 




### #log_retention_days=
    
    
    def log_retention_days=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Applicable only for CloudSQL and AlloyDB resource_type.

Configures how long logs will be stored. It is defined in “days”. This value should be greater than or equal to minimum enforced log retention duration of the backup vault. 




**Returns**

  * (::Integer) — Optional. Applicable only for CloudSQL and AlloyDB resource_type.

Configures how long logs will be stored. It is defined in “days”. This value should be greater than or equal to minimum enforced log retention duration of the backup vault. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Identifier. The resource name of the `BackupPlan`.

Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`




### #resource_type
    
    
    def resource_type() -> ::String

**Returns**

  * (::String) — Required. The resource type to which the `BackupPlan` will be applied. Examples include, "compute.googleapis.com/Instance", "sqladmin.googleapis.com/Instance", "alloydb.googleapis.com/Cluster", "compute.googleapis.com/Disk". 



### #resource_type=
    
    
    def resource_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource type to which the `BackupPlan` will be applied. Examples include, "compute.googleapis.com/Instance", "sqladmin.googleapis.com/Instance", "alloydb.googleapis.com/Cluster", "compute.googleapis.com/Disk". 



**Returns**

  * (::String) — Required. The resource type to which the `BackupPlan` will be applied. Examples include, "compute.googleapis.com/Instance", "sqladmin.googleapis.com/Instance", "alloydb.googleapis.com/Cluster", "compute.googleapis.com/Disk". 



### #revision_id
    
    
    def revision_id() -> ::String

**Returns**

  * (::String) — Output only. The user friendly revision ID of the `BackupPlanRevision`.

Example: v0, v1, v2, etc. 




### #revision_name
    
    
    def revision_name() -> ::String

**Returns**

  * (::String) — Output only. The resource id of the `BackupPlanRevision`.

Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision_id}`




### #state
    
    
    def state() -> ::Google::Cloud::BackupDR::V1::BackupPlan::State

**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupPlan::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlan-State)) — Output only. The `State` for the `BackupPlan`. 



### #supported_resource_types
    
    
    def supported_resource_types() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. All resource types to which backupPlan can be applied. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Output only. When the `BackupPlan` was last updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
