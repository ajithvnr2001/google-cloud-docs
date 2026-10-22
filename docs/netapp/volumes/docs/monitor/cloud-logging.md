---
url: https://docs.cloud.google.com/netapp/volumes/docs/monitor/cloud-logging/
title: Google Cloud NetApp Volumes audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:13.283995+00:00
---

# Google Cloud NetApp Volumes audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/monitor/cloud-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Google Cloud NetApp Volumes audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Google Cloud NetApp Volumes. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Google Cloud NetApp Volumes audit logs use the service name `netapp.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="netapp.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Google Cloud NetApp Volumes generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.netapp.v1.NetApp.GetActiveDirectory`  
`google.cloud.netapp.v1.NetApp.GetBackupPolicy`  
`google.cloud.netapp.v1.NetApp.GetBackupVault`  
`google.cloud.netapp.v1.NetApp.GetKmsConfig`  
`google.cloud.netapp.v1.NetApp.GetReplication`  
`google.cloud.netapp.v1.NetApp.GetSnapshot`  
`google.cloud.netapp.v1.NetApp.GetStoragePool`  
`google.cloud.netapp.v1.NetApp.GetVolume`  
`google.cloud.netapp.v1.NetApp.ListActiveDirectories`  
`google.cloud.netapp.v1.NetApp.ListBackupPolicies`  
`google.cloud.netapp.v1.NetApp.ListBackupVaults`  
`google.cloud.netapp.v1.NetApp.ListBackups`  
`google.cloud.netapp.v1.NetApp.ListKmsConfigs`  
`google.cloud.netapp.v1.NetApp.ListReplications`  
`google.cloud.netapp.v1.NetApp.ListSnapshots`  
`google.cloud.netapp.v1.NetApp.ListStoragePools`  
`google.cloud.netapp.v1.NetApp.ListVolumes`  
`google.cloud.netapp.v1alpha1.NetApp.GetActiveDirectory`  
`google.cloud.netapp.v1alpha1.NetApp.GetBackupPolicy`  
`google.cloud.netapp.v1alpha1.NetApp.GetSnapshot`  
`google.cloud.netapp.v1alpha1.NetApp.GetStoragePool`  
`google.cloud.netapp.v1alpha1.NetApp.GetVolume`  
`google.cloud.netapp.v1alpha1.NetApp.ListActiveDirectories`  
`google.cloud.netapp.v1alpha1.NetApp.ListBackupPolicies`  
`google.cloud.netapp.v1alpha1.NetApp.ListKmsConfigs`  
`google.cloud.netapp.v1alpha1.NetApp.ListSnapshots`  
`google.cloud.netapp.v1alpha1.NetApp.ListStoragePools`  
`google.cloud.netapp.v1alpha1.NetApp.ListVolumes`  
`google.cloud.netapp.v1beta1.NetApp.GetActiveDirectory`  
`google.cloud.netapp.v1beta1.NetApp.GetBackup`  
`google.cloud.netapp.v1beta1.NetApp.GetBackupPolicy`  
`google.cloud.netapp.v1beta1.NetApp.GetBackupVault`  
`google.cloud.netapp.v1beta1.NetApp.GetKmsConfig`  
`google.cloud.netapp.v1beta1.NetApp.GetSnapshot`  
`google.cloud.netapp.v1beta1.NetApp.GetStoragePool`  
`google.cloud.netapp.v1beta1.NetApp.GetVolume`  
`google.cloud.netapp.v1beta1.NetApp.ListActiveDirectories`  
`google.cloud.netapp.v1beta1.NetApp.ListBackupPolicies`  
`google.cloud.netapp.v1beta1.NetApp.ListBackupVaults`  
`google.cloud.netapp.v1beta1.NetApp.ListBackups`  
`google.cloud.netapp.v1beta1.NetApp.ListKmsConfigs`  
`google.cloud.netapp.v1beta1.NetApp.ListReplications`  
`google.cloud.netapp.v1beta1.NetApp.ListSnapshots`  
`google.cloud.netapp.v1beta1.NetApp.ListStoragePools`  
`google.cloud.netapp.v1beta1.NetApp.ListVolumes`  
`ADMIN_WRITE` | `google.cloud.netapp.v1.NetApp.CreateActiveDirectory` (LRO)  
`google.cloud.netapp.v1.NetApp.CreateBackupPolicy` (LRO)  
`google.cloud.netapp.v1.NetApp.CreateBackupVault` (LRO)  
`google.cloud.netapp.v1.NetApp.CreateKmsConfig` (LRO)  
`google.cloud.netapp.v1.NetApp.CreateStoragePool` (LRO)  
`google.cloud.netapp.v1.NetApp.CreateVolume` (LRO)  
`google.cloud.netapp.v1.NetApp.DeleteActiveDirectory` (LRO)  
`google.cloud.netapp.v1.NetApp.DeleteBackupPolicy` (LRO)  
`google.cloud.netapp.v1.NetApp.DeleteBackupVault` (LRO)  
`google.cloud.netapp.v1.NetApp.DeleteKmsConfig` (LRO)  
`google.cloud.netapp.v1.NetApp.DeleteStoragePool` (LRO)  
`google.cloud.netapp.v1.NetApp.ResumeReplication` (LRO)  
`google.cloud.netapp.v1.NetApp.ReverseReplicationDirection` (LRO)  
`google.cloud.netapp.v1.NetApp.StopReplication` (LRO)  
`google.cloud.netapp.v1.NetApp.UpdateActiveDirectory` (LRO)  
`google.cloud.netapp.v1.NetApp.UpdateBackup` (LRO)  
`google.cloud.netapp.v1.NetApp.UpdateBackupPolicy` (LRO)  
`google.cloud.netapp.v1.NetApp.UpdateBackupVault` (LRO)  
`google.cloud.netapp.v1.NetApp.UpdateKmsConfig` (LRO)  
`google.cloud.netapp.v1.NetApp.UpdateReplication` (LRO)  
`google.cloud.netapp.v1.NetApp.UpdateSnapshot` (LRO)  
`google.cloud.netapp.v1.NetApp.UpdateStoragePool` (LRO)  
`google.cloud.netapp.v1.NetApp.UpdateVolume` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.CreateActiveDirectory` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.CreateBackupPolicy` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.CreateBackupVault` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.CreateKmsConfig` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.CreateStoragePool` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.CreateVolume` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.DeleteActiveDirectory` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.DeleteBackupPolicy` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.DeleteBackupVault` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.DeleteKmsConfig` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.DeleteStoragePool` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.ResumeReplication` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.StopReplication` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.SwitchActiveReplicaZone`  
`google.cloud.netapp.v1alpha1.NetApp.UpdateActiveDirectory` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.UpdateBackup` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.UpdateBackupPolicy` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.UpdateBackupVault` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.UpdateKmsConfig` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.UpdateReplication` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.UpdateSnapshot` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.UpdateStoragePool` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.UpdateVolume` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.CreateActiveDirectory` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.CreateBackupPolicy` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.CreateBackupVault` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.CreateKmsConfig` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.CreateStoragePool` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.CreateVolume` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.DeleteActiveDirectory` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.DeleteBackupPolicy` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.DeleteBackupVault` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.DeleteKmsConfig` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.DeleteStoragePool` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.ResumeReplication` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.ReverseReplicationDirection` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.StopReplication` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.SwitchActiveReplicaZone` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.UpdateActiveDirectory` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.UpdateBackup` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.UpdateBackupPolicy` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.UpdateBackupVault` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.UpdateKmsConfig` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.UpdateReplication` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.UpdateSnapshot` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.UpdateStoragePool` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.UpdateVolume` (LRO)  
`DATA_WRITE` | `google.cloud.netapp.v1.NetApp.CreateBackup` (LRO)  
`google.cloud.netapp.v1.NetApp.CreateReplication` (LRO)  
`google.cloud.netapp.v1.NetApp.CreateSnapshot` (LRO)  
`google.cloud.netapp.v1.NetApp.DeleteBackup` (LRO)  
`google.cloud.netapp.v1.NetApp.DeleteReplication` (LRO)  
`google.cloud.netapp.v1.NetApp.DeleteSnapshot` (LRO)  
`google.cloud.netapp.v1.NetApp.DeleteVolume` (LRO)  
`google.cloud.netapp.v1.NetApp.EncryptVolumes`  
`google.cloud.netapp.v1.NetApp.RevertVolume` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.CreateSnapshot` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.DeleteSnapshot` (LRO)  
`google.cloud.netapp.v1alpha1.NetApp.DeleteVolume` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.CreateBackup` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.CreateReplication` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.CreateSnapshot` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.DeleteBackup` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.DeleteReplication` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.DeleteSnapshot` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.DeleteVolume` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.EncryptVolumes` (LRO)  
`google.cloud.netapp.v1beta1.NetApp.RevertVolume` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Google Cloud NetApp Volumes.

### `google.cloud.netapp.v1.NetApp`

The following audit logs are associated with methods belonging to `google.cloud.netapp.v1.NetApp`.

#### `CreateActiveDirectory`

  * **Method** : `google.cloud.netapp.v1.NetApp.CreateActiveDirectory`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.activeDirectories.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.CreateActiveDirectory" `  




#### `CreateBackup`

  * **Method** : `google.cloud.netapp.v1.NetApp.CreateBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.backups.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.CreateBackup" `  




#### `CreateBackupPolicy`

  * **Method** : `google.cloud.netapp.v1.NetApp.CreateBackupPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backupPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.CreateBackupPolicy" `  




#### `CreateBackupVault`

  * **Method** : `google.cloud.netapp.v1.NetApp.CreateBackupVault`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backupVaults.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.CreateBackupVault" `  




#### `CreateKmsConfig`

  * **Method** : `google.cloud.netapp.v1.NetApp.CreateKmsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.kmsConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.CreateKmsConfig" `  




#### `CreateReplication`

  * **Method** : `google.cloud.netapp.v1.NetApp.CreateReplication`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.replications.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.CreateReplication" `  




#### `CreateSnapshot`

  * **Method** : `google.cloud.netapp.v1.NetApp.CreateSnapshot`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.snapshots.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.CreateSnapshot" `  




#### `CreateStoragePool`

  * **Method** : `google.cloud.netapp.v1.NetApp.CreateStoragePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.storagePools.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.CreateStoragePool" `  




#### `CreateVolume`

  * **Method** : `google.cloud.netapp.v1.NetApp.CreateVolume`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.volumes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.CreateVolume" `  




#### `DeleteActiveDirectory`

  * **Method** : `google.cloud.netapp.v1.NetApp.DeleteActiveDirectory`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.activeDirectories.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.DeleteActiveDirectory" `  




#### `DeleteBackup`

  * **Method** : `google.cloud.netapp.v1.NetApp.DeleteBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.backups.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.DeleteBackup" `  




#### `DeleteBackupPolicy`

  * **Method** : `google.cloud.netapp.v1.NetApp.DeleteBackupPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backupPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.DeleteBackupPolicy" `  




#### `DeleteBackupVault`

  * **Method** : `google.cloud.netapp.v1.NetApp.DeleteBackupVault`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backupVaults.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.DeleteBackupVault" `  




#### `DeleteKmsConfig`

  * **Method** : `google.cloud.netapp.v1.NetApp.DeleteKmsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.kmsConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.DeleteKmsConfig" `  




#### `DeleteReplication`

  * **Method** : `google.cloud.netapp.v1.NetApp.DeleteReplication`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.replications.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.DeleteReplication" `  




#### `DeleteSnapshot`

  * **Method** : `google.cloud.netapp.v1.NetApp.DeleteSnapshot`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.snapshots.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.DeleteSnapshot" `  




#### `DeleteStoragePool`

  * **Method** : `google.cloud.netapp.v1.NetApp.DeleteStoragePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.storagePools.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.DeleteStoragePool" `  




#### `DeleteVolume`

  * **Method** : `google.cloud.netapp.v1.NetApp.DeleteVolume`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.volumes.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.DeleteVolume" `  




#### `EncryptVolumes`

  * **Method** : `google.cloud.netapp.v1.NetApp.EncryptVolumes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.kmsConfigs.encrypt - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.EncryptVolumes" `  




#### `GetActiveDirectory`

  * **Method** : `google.cloud.netapp.v1.NetApp.GetActiveDirectory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.activeDirectories.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.GetActiveDirectory" `  




#### `GetBackupPolicy`

  * **Method** : `google.cloud.netapp.v1.NetApp.GetBackupPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.backupPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.GetBackupPolicy" `  




#### `GetBackupVault`

  * **Method** : `google.cloud.netapp.v1.NetApp.GetBackupVault`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.backupVaults.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.GetBackupVault" `  




#### `GetKmsConfig`

  * **Method** : `google.cloud.netapp.v1.NetApp.GetKmsConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.kmsConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.GetKmsConfig" `  




#### `GetReplication`

  * **Method** : `google.cloud.netapp.v1.NetApp.GetReplication`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.replications.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.GetReplication" `  




#### `GetSnapshot`

  * **Method** : `google.cloud.netapp.v1.NetApp.GetSnapshot`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.snapshots.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.GetSnapshot" `  




#### `GetStoragePool`

  * **Method** : `google.cloud.netapp.v1.NetApp.GetStoragePool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.storagePools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.GetStoragePool" `  




#### `GetVolume`

  * **Method** : `google.cloud.netapp.v1.NetApp.GetVolume`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.volumes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.GetVolume" `  




#### `ListActiveDirectories`

  * **Method** : `google.cloud.netapp.v1.NetApp.ListActiveDirectories`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.activeDirectories.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.ListActiveDirectories" `  




#### `ListBackupPolicies`

  * **Method** : `google.cloud.netapp.v1.NetApp.ListBackupPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.backupPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.ListBackupPolicies" `  




#### `ListBackupVaults`

  * **Method** : `google.cloud.netapp.v1.NetApp.ListBackupVaults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.backupVaults.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.ListBackupVaults" `  




#### `ListBackups`

  * **Method** : `google.cloud.netapp.v1.NetApp.ListBackups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.backups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.ListBackups" `  




#### `ListKmsConfigs`

  * **Method** : `google.cloud.netapp.v1.NetApp.ListKmsConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.kmsConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.ListKmsConfigs" `  




#### `ListReplications`

  * **Method** : `google.cloud.netapp.v1.NetApp.ListReplications`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.replications.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.ListReplications" `  




#### `ListSnapshots`

  * **Method** : `google.cloud.netapp.v1.NetApp.ListSnapshots`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.snapshots.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.ListSnapshots" `  




#### `ListStoragePools`

  * **Method** : `google.cloud.netapp.v1.NetApp.ListStoragePools`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.storagePools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.ListStoragePools" `  




#### `ListVolumes`

  * **Method** : `google.cloud.netapp.v1.NetApp.ListVolumes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.volumes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.ListVolumes" `  




#### `ResumeReplication`

  * **Method** : `google.cloud.netapp.v1.NetApp.ResumeReplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.replications.resume - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.ResumeReplication" `  




#### `ReverseReplicationDirection`

  * **Method** : `google.cloud.netapp.v1.NetApp.ReverseReplicationDirection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.replications.reverse - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.ReverseReplicationDirection" `  




#### `RevertVolume`

  * **Method** : `google.cloud.netapp.v1.NetApp.RevertVolume`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.volumes.revert - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.RevertVolume" `  




#### `StopReplication`

  * **Method** : `google.cloud.netapp.v1.NetApp.StopReplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.replications.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.StopReplication" `  




#### `UpdateActiveDirectory`

  * **Method** : `google.cloud.netapp.v1.NetApp.UpdateActiveDirectory`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.activeDirectories.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.UpdateActiveDirectory" `  




#### `UpdateBackup`

  * **Method** : `google.cloud.netapp.v1.NetApp.UpdateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.UpdateBackup" `  




#### `UpdateBackupPolicy`

  * **Method** : `google.cloud.netapp.v1.NetApp.UpdateBackupPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backupPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.UpdateBackupPolicy" `  




#### `UpdateBackupVault`

  * **Method** : `google.cloud.netapp.v1.NetApp.UpdateBackupVault`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backupVaults.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.UpdateBackupVault" `  




#### `UpdateKmsConfig`

  * **Method** : `google.cloud.netapp.v1.NetApp.UpdateKmsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.kmsConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.UpdateKmsConfig" `  




#### `UpdateReplication`

  * **Method** : `google.cloud.netapp.v1.NetApp.UpdateReplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.replications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.UpdateReplication" `  




#### `UpdateSnapshot`

  * **Method** : `google.cloud.netapp.v1.NetApp.UpdateSnapshot`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.snapshots.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.UpdateSnapshot" `  




#### `UpdateStoragePool`

  * **Method** : `google.cloud.netapp.v1.NetApp.UpdateStoragePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.storagePools.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.UpdateStoragePool" `  




#### `UpdateVolume`

  * **Method** : `google.cloud.netapp.v1.NetApp.UpdateVolume`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.volumes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1.NetApp.UpdateVolume" `  




### `google.cloud.netapp.v1alpha1.NetApp`

The following audit logs are associated with methods belonging to `google.cloud.netapp.v1alpha1.NetApp`.

#### `CreateActiveDirectory`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.CreateActiveDirectory`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.activeDirectories.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.CreateActiveDirectory" `  




#### `CreateBackupPolicy`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.CreateBackupPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backupPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.CreateBackupPolicy" `  




#### `CreateBackupVault`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.CreateBackupVault`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backupVaults.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.CreateBackupVault" `  




#### `CreateKmsConfig`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.CreateKmsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.kmsConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.CreateKmsConfig" `  




#### `CreateSnapshot`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.CreateSnapshot`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.snapshots.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.CreateSnapshot" `  




#### `CreateStoragePool`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.CreateStoragePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.storagePools.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.CreateStoragePool" `  




#### `CreateVolume`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.CreateVolume`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.volumes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.CreateVolume" `  




#### `DeleteActiveDirectory`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.DeleteActiveDirectory`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.activeDirectories.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.DeleteActiveDirectory" `  




#### `DeleteBackupPolicy`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.DeleteBackupPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backupPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.DeleteBackupPolicy" `  




#### `DeleteBackupVault`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.DeleteBackupVault`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backupVaults.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.DeleteBackupVault" `  




#### `DeleteKmsConfig`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.DeleteKmsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.kmsConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.DeleteKmsConfig" `  




#### `DeleteSnapshot`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.DeleteSnapshot`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.snapshots.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.DeleteSnapshot" `  




#### `DeleteStoragePool`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.DeleteStoragePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.storagePools.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.DeleteStoragePool" `  




#### `DeleteVolume`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.DeleteVolume`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.volumes.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.DeleteVolume" `  




#### `GetActiveDirectory`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.GetActiveDirectory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.activeDirectories.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.GetActiveDirectory" `  




#### `GetBackupPolicy`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.GetBackupPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.backupPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.GetBackupPolicy" `  




#### `GetSnapshot`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.GetSnapshot`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.snapshots.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.GetSnapshot" `  




#### `GetStoragePool`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.GetStoragePool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.storagePools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.GetStoragePool" `  




#### `GetVolume`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.GetVolume`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.volumes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.GetVolume" `  




#### `ListActiveDirectories`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.ListActiveDirectories`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.activeDirectories.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.ListActiveDirectories" `  




#### `ListBackupPolicies`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.ListBackupPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.backupPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.ListBackupPolicies" `  




#### `ListKmsConfigs`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.ListKmsConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.kmsConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.ListKmsConfigs" `  




#### `ListSnapshots`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.ListSnapshots`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.snapshots.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.ListSnapshots" `  




#### `ListStoragePools`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.ListStoragePools`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.storagePools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.ListStoragePools" `  




#### `ListVolumes`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.ListVolumes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.volumes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.ListVolumes" `  




#### `ResumeReplication`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.ResumeReplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.replications.resume - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.ResumeReplication" `  




#### `StopReplication`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.StopReplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.replications.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.StopReplication" `  




#### `SwitchActiveReplicaZone`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.SwitchActiveReplicaZone`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.storagePools.switch - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.SwitchActiveReplicaZone" `  




#### `UpdateActiveDirectory`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.UpdateActiveDirectory`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.activeDirectories.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.UpdateActiveDirectory" `  




#### `UpdateBackup`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.UpdateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.UpdateBackup" `  




#### `UpdateBackupPolicy`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.UpdateBackupPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backupPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.UpdateBackupPolicy" `  




#### `UpdateBackupVault`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.UpdateBackupVault`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backupVaults.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.UpdateBackupVault" `  




#### `UpdateKmsConfig`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.UpdateKmsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.kmsConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.UpdateKmsConfig" `  




#### `UpdateReplication`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.UpdateReplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.replications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.UpdateReplication" `  




#### `UpdateSnapshot`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.UpdateSnapshot`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.snapshots.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.UpdateSnapshot" `  




#### `UpdateStoragePool`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.UpdateStoragePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.storagePools.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.UpdateStoragePool" `  




#### `UpdateVolume`

  * **Method** : `google.cloud.netapp.v1alpha1.NetApp.UpdateVolume`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.volumes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1alpha1.NetApp.UpdateVolume" `  




### `google.cloud.netapp.v1beta1.NetApp`

The following audit logs are associated with methods belonging to `google.cloud.netapp.v1beta1.NetApp`.

#### `CreateActiveDirectory`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.CreateActiveDirectory`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.activeDirectories.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.CreateActiveDirectory" `  




#### `CreateBackup`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.CreateBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.backups.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.CreateBackup" `  




#### `CreateBackupPolicy`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.CreateBackupPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backupPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.CreateBackupPolicy" `  




#### `CreateBackupVault`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.CreateBackupVault`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backupVaults.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.CreateBackupVault" `  




#### `CreateKmsConfig`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.CreateKmsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.kmsConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.CreateKmsConfig" `  




#### `CreateReplication`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.CreateReplication`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.replications.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.CreateReplication" `  




#### `CreateSnapshot`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.CreateSnapshot`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.snapshots.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.CreateSnapshot" `  




#### `CreateStoragePool`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.CreateStoragePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.storagePools.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.CreateStoragePool" `  




#### `CreateVolume`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.CreateVolume`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.volumes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.CreateVolume" `  




#### `DeleteActiveDirectory`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.DeleteActiveDirectory`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.activeDirectories.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.DeleteActiveDirectory" `  




#### `DeleteBackup`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.DeleteBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.backups.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.DeleteBackup" `  




#### `DeleteBackupPolicy`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.DeleteBackupPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backupPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.DeleteBackupPolicy" `  




#### `DeleteBackupVault`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.DeleteBackupVault`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backupVaults.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.DeleteBackupVault" `  




#### `DeleteKmsConfig`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.DeleteKmsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.kmsConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.DeleteKmsConfig" `  




#### `DeleteReplication`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.DeleteReplication`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.replications.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.DeleteReplication" `  




#### `DeleteSnapshot`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.DeleteSnapshot`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.snapshots.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.DeleteSnapshot" `  




#### `DeleteStoragePool`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.DeleteStoragePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.storagePools.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.DeleteStoragePool" `  




#### `DeleteVolume`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.DeleteVolume`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.volumes.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.DeleteVolume" `  




#### `EncryptVolumes`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.EncryptVolumes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.kmsConfigs.encrypt - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.EncryptVolumes" `  




#### `GetActiveDirectory`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.GetActiveDirectory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.activeDirectories.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.GetActiveDirectory" `  




#### `GetBackup`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.GetBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.backups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.GetBackup" `  




#### `GetBackupPolicy`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.GetBackupPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.backupPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.GetBackupPolicy" `  




#### `GetBackupVault`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.GetBackupVault`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.backupVaults.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.GetBackupVault" `  




#### `GetKmsConfig`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.GetKmsConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.kmsConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.GetKmsConfig" `  




#### `GetSnapshot`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.GetSnapshot`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.snapshots.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.GetSnapshot" `  




#### `GetStoragePool`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.GetStoragePool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.storagePools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.GetStoragePool" `  




#### `GetVolume`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.GetVolume`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.volumes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.GetVolume" `  




#### `ListActiveDirectories`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.ListActiveDirectories`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.activeDirectories.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.ListActiveDirectories" `  




#### `ListBackupPolicies`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.ListBackupPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.backupPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.ListBackupPolicies" `  




#### `ListBackupVaults`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.ListBackupVaults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.backupVaults.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.ListBackupVaults" `  




#### `ListBackups`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.ListBackups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.backups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.ListBackups" `  




#### `ListKmsConfigs`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.ListKmsConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.kmsConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.ListKmsConfigs" `  




#### `ListReplications`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.ListReplications`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.replications.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.ListReplications" `  




#### `ListSnapshots`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.ListSnapshots`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.snapshots.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.ListSnapshots" `  




#### `ListStoragePools`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.ListStoragePools`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.storagePools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.ListStoragePools" `  




#### `ListVolumes`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.ListVolumes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.volumes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.ListVolumes" `  




#### `ResumeReplication`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.ResumeReplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.replications.resume - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.ResumeReplication" `  




#### `ReverseReplicationDirection`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.ReverseReplicationDirection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.replications.reverse - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.ReverseReplicationDirection" `  




#### `RevertVolume`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.RevertVolume`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `netapp.volumes.revert - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.RevertVolume" `  




#### `StopReplication`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.StopReplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.replications.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.StopReplication" `  




#### `SwitchActiveReplicaZone`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.SwitchActiveReplicaZone`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.storagePools.switch - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.SwitchActiveReplicaZone" `  




#### `UpdateActiveDirectory`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.UpdateActiveDirectory`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.activeDirectories.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.UpdateActiveDirectory" `  




#### `UpdateBackup`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.UpdateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.UpdateBackup" `  




#### `UpdateBackupPolicy`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.UpdateBackupPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backupPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.UpdateBackupPolicy" `  




#### `UpdateBackupVault`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.UpdateBackupVault`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.backupVaults.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.UpdateBackupVault" `  




#### `UpdateKmsConfig`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.UpdateKmsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.kmsConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.UpdateKmsConfig" `  




#### `UpdateReplication`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.UpdateReplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.replications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.UpdateReplication" `  




#### `UpdateSnapshot`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.UpdateSnapshot`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.snapshots.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.UpdateSnapshot" `  




#### `UpdateStoragePool`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.UpdateStoragePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.storagePools.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.UpdateStoragePool" `  




#### `UpdateVolume`

  * **Method** : `google.cloud.netapp.v1beta1.NetApp.UpdateVolume`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `netapp.volumes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.netapp.v1beta1.NetApp.UpdateVolume" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.cloud.netapp.v1.NetApp.VerifyKmsConfig`
  * `google.cloud.netapp.v1alpha1.NetApp.VerifyKmsConfig`
  * `google.cloud.netapp.v1beta1.NetApp.VerifyKmsConfig`
  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.DeleteOperation`
  * `google.longrunning.Operations.GetOperation`
  * `google.longrunning.Operations.ListOperations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
