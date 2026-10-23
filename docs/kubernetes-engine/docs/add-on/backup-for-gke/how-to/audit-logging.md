---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/audit-logging/
title: Backup for GKE audit logging information \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:00.646219+00:00
---

# Backup for GKE audit logging information  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Backup for GKE audit logging information Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Backup for GKE. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Backup for GKE audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="gkebackup.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Backup for GKE generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.gkebackup.v1.BackupForGKE.GetBackup`  
`google.cloud.gkebackup.v1.BackupForGKE.GetBackupChannel`  
`google.cloud.gkebackup.v1.BackupForGKE.GetBackupIndexDownloadUrl`  
`google.cloud.gkebackup.v1.BackupForGKE.GetBackupPlan`  
`google.cloud.gkebackup.v1.BackupForGKE.GetBackupPlanBinding`  
`google.cloud.gkebackup.v1.BackupForGKE.GetRestore`  
`google.cloud.gkebackup.v1.BackupForGKE.GetRestoreChannel`  
`google.cloud.gkebackup.v1.BackupForGKE.GetRestorePlan`  
`google.cloud.gkebackup.v1.BackupForGKE.GetRestorePlanBinding`  
`google.cloud.gkebackup.v1.BackupForGKE.GetVolumeBackup`  
`google.cloud.gkebackup.v1.BackupForGKE.GetVolumeRestore`  
`google.cloud.gkebackup.v1.BackupForGKE.ListBackupChannels`  
`google.cloud.gkebackup.v1.BackupForGKE.ListBackupPlanBindings`  
`google.cloud.gkebackup.v1.BackupForGKE.ListBackupPlans`  
`google.cloud.gkebackup.v1.BackupForGKE.ListBackups`  
`google.cloud.gkebackup.v1.BackupForGKE.ListRestoreChannels`  
`google.cloud.gkebackup.v1.BackupForGKE.ListRestorePlanBindings`  
`google.cloud.gkebackup.v1.BackupForGKE.ListRestorePlans`  
`google.cloud.gkebackup.v1.BackupForGKE.ListRestores`  
`google.cloud.gkebackup.v1.BackupForGKE.ListVolumeBackups`  
`google.cloud.gkebackup.v1.BackupForGKE.ListVolumeRestores`  
`GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.gkebackup.v1.BackupForGKE.CreateBackup` (LRO)  
`google.cloud.gkebackup.v1.BackupForGKE.CreateBackupChannel` (LRO)  
`google.cloud.gkebackup.v1.BackupForGKE.CreateBackupPlan` (LRO)  
`google.cloud.gkebackup.v1.BackupForGKE.CreateRestore` (LRO)  
`google.cloud.gkebackup.v1.BackupForGKE.CreateRestoreChannel` (LRO)  
`google.cloud.gkebackup.v1.BackupForGKE.CreateRestorePlan` (LRO)  
`google.cloud.gkebackup.v1.BackupForGKE.DeleteBackup` (LRO)  
`google.cloud.gkebackup.v1.BackupForGKE.DeleteBackupChannel` (LRO)  
`google.cloud.gkebackup.v1.BackupForGKE.DeleteBackupPlan` (LRO)  
`google.cloud.gkebackup.v1.BackupForGKE.DeleteRestore` (LRO)  
`google.cloud.gkebackup.v1.BackupForGKE.DeleteRestoreChannel` (LRO)  
`google.cloud.gkebackup.v1.BackupForGKE.DeleteRestorePlan` (LRO)  
`google.cloud.gkebackup.v1.BackupForGKE.UpdateBackup` (LRO)  
`google.cloud.gkebackup.v1.BackupForGKE.UpdateBackupChannel` (LRO)  
`google.cloud.gkebackup.v1.BackupForGKE.UpdateBackupPlan` (LRO)  
`google.cloud.gkebackup.v1.BackupForGKE.UpdateRestore` (LRO)  
`google.cloud.gkebackup.v1.BackupForGKE.UpdateRestoreChannel` (LRO)  
`google.cloud.gkebackup.v1.BackupForGKE.UpdateRestorePlan` (LRO)  
`SetIamPolicy`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Backup for GKE.

### `google.cloud.gkebackup.v1.BackupForGKE`

The following audit logs are associated with methods belonging to `google.cloud.gkebackup.v1.BackupForGKE`.

#### `CreateBackup`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.CreateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkebackup.backups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.CreateBackup" `  




#### `CreateBackupChannel`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.CreateBackupChannel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkebackup.backupChannels.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.CreateBackupChannel" `  




#### `CreateBackupPlan`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.CreateBackupPlan`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkebackup.backupPlans.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.CreateBackupPlan" `  




#### `CreateRestore`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.CreateRestore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkebackup.backups.get - ADMIN_READ`
    * `gkebackup.restores.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.CreateRestore" `  




#### `CreateRestoreChannel`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.CreateRestoreChannel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkebackup.restoreChannels.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.CreateRestoreChannel" `  




#### `CreateRestorePlan`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.CreateRestorePlan`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkebackup.restorePlans.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.CreateRestorePlan" `  




#### `DeleteBackup`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.DeleteBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkebackup.backups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.DeleteBackup" `  




#### `DeleteBackupChannel`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.DeleteBackupChannel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkebackup.backupChannels.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.DeleteBackupChannel" `  




#### `DeleteBackupPlan`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.DeleteBackupPlan`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkebackup.backupPlans.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.DeleteBackupPlan" `  




#### `DeleteRestore`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.DeleteRestore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkebackup.restores.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.DeleteRestore" `  




#### `DeleteRestoreChannel`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.DeleteRestoreChannel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkebackup.restoreChannels.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.DeleteRestoreChannel" `  




#### `DeleteRestorePlan`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.DeleteRestorePlan`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkebackup.restorePlans.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.DeleteRestorePlan" `  




#### `GetBackup`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.GetBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.backups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.GetBackup" `  




#### `GetBackupChannel`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.GetBackupChannel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.backupChannels.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.GetBackupChannel" `  




#### `GetBackupIndexDownloadUrl`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.GetBackupIndexDownloadUrl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.backups.getBackupIndex - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.GetBackupIndexDownloadUrl" `  




#### `GetBackupPlan`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.GetBackupPlan`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.backupPlans.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.GetBackupPlan" `  




#### `GetBackupPlanBinding`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.GetBackupPlanBinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.backupPlanBindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.GetBackupPlanBinding" `  




#### `GetRestore`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.GetRestore`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.restores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.GetRestore" `  




#### `GetRestoreChannel`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.GetRestoreChannel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.restoreChannels.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.GetRestoreChannel" `  




#### `GetRestorePlan`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.GetRestorePlan`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.restorePlans.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.GetRestorePlan" `  




#### `GetRestorePlanBinding`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.GetRestorePlanBinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.restorePlanBindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.GetRestorePlanBinding" `  




#### `GetVolumeBackup`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.GetVolumeBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.volumeBackups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.GetVolumeBackup" `  




#### `GetVolumeRestore`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.GetVolumeRestore`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.volumeRestores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.GetVolumeRestore" `  




#### `ListBackupChannels`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.ListBackupChannels`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.backupChannels.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.ListBackupChannels" `  




#### `ListBackupPlanBindings`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.ListBackupPlanBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.backupPlanBindings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.ListBackupPlanBindings" `  




#### `ListBackupPlans`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.ListBackupPlans`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.backupPlans.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.ListBackupPlans" `  




#### `ListBackups`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.ListBackups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.backups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.ListBackups" `  




#### `ListRestoreChannels`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.ListRestoreChannels`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.restoreChannels.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.ListRestoreChannels" `  




#### `ListRestorePlanBindings`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.ListRestorePlanBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.restorePlanBindings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.ListRestorePlanBindings" `  




#### `ListRestorePlans`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.ListRestorePlans`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.restorePlans.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.ListRestorePlans" `  




#### `ListRestores`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.ListRestores`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.restores.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.ListRestores" `  




#### `ListVolumeBackups`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.ListVolumeBackups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.volumeBackups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.ListVolumeBackups" `  




#### `ListVolumeRestores`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.ListVolumeRestores`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.volumeRestores.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.ListVolumeRestores" `  




#### `UpdateBackup`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.UpdateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkebackup.backups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.UpdateBackup" `  




#### `UpdateBackupChannel`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.UpdateBackupChannel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkebackup.backupChannels.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.UpdateBackupChannel" `  




#### `UpdateBackupPlan`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.UpdateBackupPlan`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkebackup.backupPlans.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.UpdateBackupPlan" `  




#### `UpdateRestore`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.UpdateRestore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkebackup.restores.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.UpdateRestore" `  




#### `UpdateRestoreChannel`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.UpdateRestoreChannel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkebackup.restoreChannels.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.UpdateRestoreChannel" `  




#### `UpdateRestorePlan`

  * **Method** : `google.cloud.gkebackup.v1.BackupForGKE.UpdateRestorePlan`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkebackup.restorePlans.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkebackup.v1.BackupForGKE.UpdateRestorePlan" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.backupPlans.getIamPolicy - ADMIN_READ`
    * `gkebackup.restorePlans.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : See IAM documentation for permissions.
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkebackup.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkebackup.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkebackup.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.cloud.resourcemanager.tags.consumerapi.v1.TagBindings.GetTags`
  * `google.cloud.resourcemanager.tags.consumerapi.v1.TagBindings.SetTags`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
