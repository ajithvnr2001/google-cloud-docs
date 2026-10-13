---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-BackupDisasterRecovery/
title: Cloud Security Command Center V1 API - Class Google::Cloud::SecurityCenter::V1::BackupDisasterRecovery (v1.11.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:36.627266+00:00
---

# Cloud Security Command Center V1 API - Class Google::Cloud::SecurityCenter::V1::BackupDisasterRecovery (v1.11.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-BackupDisasterRecovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Security Command Center V1 API - Class Google::Cloud::SecurityCenter::V1::BackupDisasterRecovery (v1.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.1 (latest)  1.11.0  1.10.0  1.9.1  1.8.0  1.7.1  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.2  0.33.0  0.32.0  0.31.1  0.30.0  0.29.1  0.28.0  0.27.0  0.26.0  0.25.1  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.1  0.11.1 

Reference documentation and code samples for the Cloud Security Command Center V1 API class Google::Cloud::SecurityCenter::V1::BackupDisasterRecovery.

Information related to Google Cloud Backup and DR Service findings.

## Inherits

  * [Object](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-Kubernetes-Object)



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #appliance
    
    
    def appliance() -> ::String

**Returns**

  * (::String) — The name of the Backup and DR appliance that captures, moves, and manages the lifecycle of backup data. For example, `backup-server-57137`. 



### #appliance=
    
    
    def appliance=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the Backup and DR appliance that captures, moves, and manages the lifecycle of backup data. For example, `backup-server-57137`. 



**Returns**

  * (::String) — The name of the Backup and DR appliance that captures, moves, and manages the lifecycle of backup data. For example, `backup-server-57137`. 



### #applications
    
    
    def applications() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The names of Backup and DR applications. An application is a VM, database, or file system on a managed host monitored by a backup and recovery appliance. For example, `centos7-01-vol00`, `centos7-01-vol01`, `centos7-01-vol02`. 



### #applications=
    
    
    def applications=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The names of Backup and DR applications. An application is a VM, database, or file system on a managed host monitored by a backup and recovery appliance. For example, `centos7-01-vol00`, `centos7-01-vol01`, `centos7-01-vol02`. 



**Returns**

  * (::Array<::String>) — The names of Backup and DR applications. An application is a VM, database, or file system on a managed host monitored by a backup and recovery appliance. For example, `centos7-01-vol00`, `centos7-01-vol01`, `centos7-01-vol02`. 



### #backup_create_time
    
    
    def backup_create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Protobuf-Timestamp)) — The timestamp at which the Backup and DR backup was created. 



### #backup_create_time=
    
    
    def backup_create_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Protobuf-Timestamp)) — The timestamp at which the Backup and DR backup was created. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Protobuf-Timestamp)) — The timestamp at which the Backup and DR backup was created. 



### #backup_template
    
    
    def backup_template() -> ::String

**Returns**

  * (::String) — The name of a Backup and DR template which comprises one or more backup policies. See the [Backup and DR documentation](https://cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan#temp) for more information. For example, `snap-ov`. 



### #backup_template=
    
    
    def backup_template=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of a Backup and DR template which comprises one or more backup policies. See the [Backup and DR documentation](https://cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan#temp) for more information. For example, `snap-ov`. 



**Returns**

  * (::String) — The name of a Backup and DR template which comprises one or more backup policies. See the [Backup and DR documentation](https://cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan#temp) for more information. For example, `snap-ov`. 



### #backup_type
    
    
    def backup_type() -> ::String

**Returns**

  * (::String) — The backup type of the Backup and DR image. For example, `Snapshot`, `Remote Snapshot`, `OnVault`. 



### #backup_type=
    
    
    def backup_type=(value) -> ::String

**Parameter**

  * **value** (::String) — The backup type of the Backup and DR image. For example, `Snapshot`, `Remote Snapshot`, `OnVault`. 



**Returns**

  * (::String) — The backup type of the Backup and DR image. For example, `Snapshot`, `Remote Snapshot`, `OnVault`. 



### #host
    
    
    def host() -> ::String

**Returns**

  * (::String) — The name of a Backup and DR host, which is managed by the backup and recovery appliance and known to the management console. The host can be of type Generic (for example, Compute Engine, SQL Server, Oracle DB, SMB file system, etc.), vCenter, or an ESX server. See the [Backup and DR documentation on hosts](https://cloud.google.com/backup-disaster-recovery/docs/configuration/manage-hosts-and-their-applications) for more information. For example, `centos7-01`. 



### #host=
    
    
    def host=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of a Backup and DR host, which is managed by the backup and recovery appliance and known to the management console. The host can be of type Generic (for example, Compute Engine, SQL Server, Oracle DB, SMB file system, etc.), vCenter, or an ESX server. See the [Backup and DR documentation on hosts](https://cloud.google.com/backup-disaster-recovery/docs/configuration/manage-hosts-and-their-applications) for more information. For example, `centos7-01`. 



**Returns**

  * (::String) — The name of a Backup and DR host, which is managed by the backup and recovery appliance and known to the management console. The host can be of type Generic (for example, Compute Engine, SQL Server, Oracle DB, SMB file system, etc.), vCenter, or an ESX server. See the [Backup and DR documentation on hosts](https://cloud.google.com/backup-disaster-recovery/docs/configuration/manage-hosts-and-their-applications) for more information. For example, `centos7-01`. 



### #policies
    
    
    def policies() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The names of Backup and DR policies that are associated with a template and that define when to run a backup, how frequently to run a backup, and how long to retain the backup image. For example, `onvaults`. 



### #policies=
    
    
    def policies=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The names of Backup and DR policies that are associated with a template and that define when to run a backup, how frequently to run a backup, and how long to retain the backup image. For example, `onvaults`. 



**Returns**

  * (::Array<::String>) — The names of Backup and DR policies that are associated with a template and that define when to run a backup, how frequently to run a backup, and how long to retain the backup image. For example, `onvaults`. 



### #policy_options
    
    
    def policy_options() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The names of Backup and DR advanced policy options of a policy applying to an application. See the [Backup and DR documentation on policy options](https://cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings). For example, `skipofflineappsincongrp, nounmap`. 



### #policy_options=
    
    
    def policy_options=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The names of Backup and DR advanced policy options of a policy applying to an application. See the [Backup and DR documentation on policy options](https://cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings). For example, `skipofflineappsincongrp, nounmap`. 



**Returns**

  * (::Array<::String>) — The names of Backup and DR advanced policy options of a policy applying to an application. See the [Backup and DR documentation on policy options](https://cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings). For example, `skipofflineappsincongrp, nounmap`. 



### #profile
    
    
    def profile() -> ::String

**Returns**

  * (::String) — The name of the Backup and DR resource profile that specifies the storage media for backups of application and VM data. See the [Backup and DR documentation on profiles](https://cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan#profile). For example, `GCP`. 



### #profile=
    
    
    def profile=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the Backup and DR resource profile that specifies the storage media for backups of application and VM data. See the [Backup and DR documentation on profiles](https://cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan#profile). For example, `GCP`. 



**Returns**

  * (::String) — The name of the Backup and DR resource profile that specifies the storage media for backups of application and VM data. See the [Backup and DR documentation on profiles](https://cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan#profile). For example, `GCP`. 



### #storage_pool
    
    
    def storage_pool() -> ::String

**Returns**

  * (::String) — The name of the Backup and DR storage pool that the backup and recovery appliance is storing data in. The storage pool could be of type Cloud, Primary, Snapshot, or OnVault. See the [Backup and DR documentation on storage pools](https://cloud.google.com/backup-disaster-recovery/docs/concepts/storage-pools). For example, `DiskPoolOne`. 



### #storage_pool=
    
    
    def storage_pool=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the Backup and DR storage pool that the backup and recovery appliance is storing data in. The storage pool could be of type Cloud, Primary, Snapshot, or OnVault. See the [Backup and DR documentation on storage pools](https://cloud.google.com/backup-disaster-recovery/docs/concepts/storage-pools). For example, `DiskPoolOne`. 



**Returns**

  * (::String) — The name of the Backup and DR storage pool that the backup and recovery appliance is storing data in. The storage pool could be of type Cloud, Primary, Snapshot, or OnVault. See the [Backup and DR documentation on storage pools](https://cloud.google.com/backup-disaster-recovery/docs/concepts/storage-pools). For example, `DiskPoolOne`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
