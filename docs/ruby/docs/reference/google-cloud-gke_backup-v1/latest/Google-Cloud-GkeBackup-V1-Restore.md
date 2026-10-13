---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Restore/
title: Backup for GKE V1 API - Class Google::Cloud::GkeBackup::V1::Restore (v1.8.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:42.424768+00:00
---

# Backup for GKE V1 API - Class Google::Cloud::GkeBackup::V1::Restore (v1.8.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup for GKE V1 API - Class Google::Cloud::GkeBackup::V1::Restore (v1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.2  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Backup for GKE V1 API class Google::Cloud::GkeBackup::V1::Restore.

Represents both a request to Restore some portion of a Backup into a target GKE cluster and a record of the restore operation itself.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #backup
    
    
    def backup() -> ::String

**Returns**

  * (::String) — Required. Immutable. A reference to the [Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Backup "Google::Cloud::GkeBackup::V1::Backup \(class\)") used as the source from which this Restore will restore. Note that this Backup must be a sub-resource of the RestorePlan's [backup_plan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestorePlan#Google__Cloud__GkeBackup__V1__RestorePlan_backup_plan_instance_ "Google::Cloud::GkeBackup::V1::RestorePlan#backup_plan \(method\)"). Format: `projects/*/locations/*/backupPlans/*/backups/*`. 



### #backup=
    
    
    def backup=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Immutable. A reference to the [Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Backup "Google::Cloud::GkeBackup::V1::Backup \(class\)") used as the source from which this Restore will restore. Note that this Backup must be a sub-resource of the RestorePlan's [backup_plan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestorePlan#Google__Cloud__GkeBackup__V1__RestorePlan_backup_plan_instance_ "Google::Cloud::GkeBackup::V1::RestorePlan#backup_plan \(method\)"). Format: `projects/*/locations/*/backupPlans/*/backups/*`. 



**Returns**

  * (::String) — Required. Immutable. A reference to the [Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Backup "Google::Cloud::GkeBackup::V1::Backup \(class\)") used as the source from which this Restore will restore. Note that this Backup must be a sub-resource of the RestorePlan's [backup_plan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestorePlan#Google__Cloud__GkeBackup__V1__RestorePlan_backup_plan_instance_ "Google::Cloud::GkeBackup::V1::RestorePlan#backup_plan \(method\)"). Format: `projects/*/locations/*/backupPlans/*/backups/*`. 



### #cluster
    
    
    def cluster() -> ::String

**Returns**

  * (::String) — Output only. The target cluster into which this Restore will restore data. Valid formats:

    * `projects/*/locations/*/clusters/*`
    * `projects/*/zones/*/clusters/*`

Inherited from parent RestorePlan's [cluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestorePlan#Google__Cloud__GkeBackup__V1__RestorePlan_cluster_instance_ "Google::Cloud::GkeBackup::V1::RestorePlan#cluster \(method\)") value. 




### #complete_time
    
    
    def complete_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp of when the restore operation completed. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Protobuf-Timestamp)) — Output only. The timestamp when this Restore resource was created. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. User specified descriptive string for this Restore. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. User specified descriptive string for this Restore. 



**Returns**

  * (::String) — Optional. User specified descriptive string for this Restore. 



### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a restore from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform restore updates in order to avoid race conditions: An `etag` is returned in the response to `GetRestore`, and systems are expected to put that etag in the request to `UpdateRestore` or `DeleteRestore` to ensure that their change will be applied to the same version of the resource. 



### #filter
    
    
    def filter() -> ::Google::Cloud::GkeBackup::V1::Restore::Filter

**Returns**

  * ([::Google::Cloud::GkeBackup::V1::Restore::Filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Restore-Filter)) — Optional. Immutable. Filters resources for `Restore`. If not specified, the scope of the restore will remain the same as defined in the `RestorePlan`. If this is specified and no resources are matched by the `inclusion_filters` or everything is excluded by the `exclusion_filters`, nothing will be restored. This filter can only be specified if the value of [namespaced_resource_restore_mode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestoreConfig#Google__Cloud__GkeBackup__V1__RestoreConfig_namespaced_resource_restore_mode_instance_ "Google::Cloud::GkeBackup::V1::RestoreConfig#namespaced_resource_restore_mode \(method\)") is set to `MERGE_SKIP_ON_CONFLICT`, `MERGE_REPLACE_VOLUME_ON_CONFLICT` or `MERGE_REPLACE_ON_CONFLICT`. 



### #filter=
    
    
    def filter=(value) -> ::Google::Cloud::GkeBackup::V1::Restore::Filter

**Parameter**

  * **value** ([::Google::Cloud::GkeBackup::V1::Restore::Filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Restore-Filter)) — Optional. Immutable. Filters resources for `Restore`. If not specified, the scope of the restore will remain the same as defined in the `RestorePlan`. If this is specified and no resources are matched by the `inclusion_filters` or everything is excluded by the `exclusion_filters`, nothing will be restored. This filter can only be specified if the value of [namespaced_resource_restore_mode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestoreConfig#Google__Cloud__GkeBackup__V1__RestoreConfig_namespaced_resource_restore_mode_instance_ "Google::Cloud::GkeBackup::V1::RestoreConfig#namespaced_resource_restore_mode \(method\)") is set to `MERGE_SKIP_ON_CONFLICT`, `MERGE_REPLACE_VOLUME_ON_CONFLICT` or `MERGE_REPLACE_ON_CONFLICT`. 



**Returns**

  * ([::Google::Cloud::GkeBackup::V1::Restore::Filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Restore-Filter)) — Optional. Immutable. Filters resources for `Restore`. If not specified, the scope of the restore will remain the same as defined in the `RestorePlan`. If this is specified and no resources are matched by the `inclusion_filters` or everything is excluded by the `exclusion_filters`, nothing will be restored. This filter can only be specified if the value of [namespaced_resource_restore_mode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestoreConfig#Google__Cloud__GkeBackup__V1__RestoreConfig_namespaced_resource_restore_mode_instance_ "Google::Cloud::GkeBackup::V1::RestoreConfig#namespaced_resource_restore_mode \(method\)") is set to `MERGE_SKIP_ON_CONFLICT`, `MERGE_REPLACE_VOLUME_ON_CONFLICT` or `MERGE_REPLACE_ON_CONFLICT`. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — A set of custom labels supplied by user. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — A set of custom labels supplied by user. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — A set of custom labels supplied by user. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The full name of the Restore resource. Format: `projects/*/locations/*/restorePlans/*/restores/*`



### #resources_excluded_count
    
    
    def resources_excluded_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. Number of resources excluded during the restore execution. 



### #resources_failed_count
    
    
    def resources_failed_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. Number of resources that failed to be restored during the restore execution. 



### #resources_restored_count
    
    
    def resources_restored_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. Number of resources restored during the restore execution. 



### #restore_config
    
    
    def restore_config() -> ::Google::Cloud::GkeBackup::V1::RestoreConfig

**Returns**

  * ([::Google::Cloud::GkeBackup::V1::RestoreConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestoreConfig)) — Output only. Configuration of the Restore. Inherited from parent RestorePlan's [restore_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestorePlan#Google__Cloud__GkeBackup__V1__RestorePlan_restore_config_instance_ "Google::Cloud::GkeBackup::V1::RestorePlan#restore_config \(method\)"). 



### #state
    
    
    def state() -> ::Google::Cloud::GkeBackup::V1::Restore::State

**Returns**

  * ([::Google::Cloud::GkeBackup::V1::Restore::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Restore-State)) — Output only. The current state of the Restore. 



### #state_reason
    
    
    def state_reason() -> ::String

**Returns**

  * (::String) — Output only. Human-readable description of why the Restore is in its current state. This field is only meant for human readability and should not be used programmatically as this field is not guaranteed to be consistent. 



### #uid
    
    
    def uid() -> ::String

**Returns**

  * (::String) — Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Protobuf-Timestamp)) — Output only. The timestamp when this Restore resource was last updated. 



### #volume_data_restore_policy_overrides
    
    
    def volume_data_restore_policy_overrides() -> ::Array<::Google::Cloud::GkeBackup::V1::VolumeDataRestorePolicyOverride>

**Returns**

  * (::Array<[::Google::Cloud::GkeBackup::V1::VolumeDataRestorePolicyOverride](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-VolumeDataRestorePolicyOverride)>) — Optional. Immutable. Overrides the volume data restore policies selected in the Restore Config for override-scoped resources. 



### #volume_data_restore_policy_overrides=
    
    
    def volume_data_restore_policy_overrides=(value) -> ::Array<::Google::Cloud::GkeBackup::V1::VolumeDataRestorePolicyOverride>

**Parameter**

  * **value** (::Array<[::Google::Cloud::GkeBackup::V1::VolumeDataRestorePolicyOverride](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-VolumeDataRestorePolicyOverride)>) — Optional. Immutable. Overrides the volume data restore policies selected in the Restore Config for override-scoped resources. 



**Returns**

  * (::Array<[::Google::Cloud::GkeBackup::V1::VolumeDataRestorePolicyOverride](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-VolumeDataRestorePolicyOverride)>) — Optional. Immutable. Overrides the volume data restore policies selected in the Restore Config for override-scoped resources. 



### #volumes_restored_count
    
    
    def volumes_restored_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. Number of volumes restored during the restore execution. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-12 UTC."],[],[]] 
