---
url: https://docs.cloud.google.com/filestore/docs/audit-logging/
title: Filestore API audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:15:21.019565+00:00
---

# Filestore API audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Filestore API audit logging Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Filestore supports only [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity), or control plane, audit logs. While `ADMIN_READ` methods are considered a type of [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs, they are the only Data Access audit logs available. Data plane audit logging is not supported.

This document lists the audited methods for Filestore. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Notes

For a full list of Filestore resources and their methods, see the [Filestore API](https://docs.cloud.google.com/filestore/docs/reference/rest) overview.

## Service name

To view the Filestore audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="file.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Filestore generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.filestore.v1.CloudFilestoreManager.GetBackup`  
`google.cloud.filestore.v1.CloudFilestoreManager.GetInstance`  
`google.cloud.filestore.v1.CloudFilestoreManager.GetSnapshot`  
`google.cloud.filestore.v1.CloudFilestoreManager.ListBackups`  
`google.cloud.filestore.v1.CloudFilestoreManager.ListInstances`  
`google.cloud.filestore.v1.CloudFilestoreManager.ListSnapshots`  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.GetBackup`  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.GetInstance`  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.GetShare`  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.GetSnapshot`  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.ListBackups`  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.ListInstances`  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.ListShares`  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.ListSnapshots`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.filestore.v1.CloudFilestoreManager.CreateBackup` (LRO)  
`google.cloud.filestore.v1.CloudFilestoreManager.CreateInstance` (LRO)  
`google.cloud.filestore.v1.CloudFilestoreManager.CreateSnapshot` (LRO)  
`google.cloud.filestore.v1.CloudFilestoreManager.DeleteBackup` (LRO)  
`google.cloud.filestore.v1.CloudFilestoreManager.DeleteInstance` (LRO)  
`google.cloud.filestore.v1.CloudFilestoreManager.DeleteSnapshot` (LRO)  
`google.cloud.filestore.v1.CloudFilestoreManager.PauseReplica` (LRO)  
`google.cloud.filestore.v1.CloudFilestoreManager.PromoteReplica` (LRO)  
`google.cloud.filestore.v1.CloudFilestoreManager.RestoreInstance` (LRO)  
`google.cloud.filestore.v1.CloudFilestoreManager.ResumeReplica` (LRO)  
`google.cloud.filestore.v1.CloudFilestoreManager.RevertInstance` (LRO)  
`google.cloud.filestore.v1.CloudFilestoreManager.UpdateBackup` (LRO)  
`google.cloud.filestore.v1.CloudFilestoreManager.UpdateInstance` (LRO)  
`google.cloud.filestore.v1.CloudFilestoreManager.UpdateSnapshot` (LRO)  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.AcquireShare`  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.CreateBackup` (LRO)  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.CreateInstance` (LRO)  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.CreateShare` (LRO)  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.CreateSnapshot` (LRO)  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.DeleteBackup` (LRO)  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.DeleteInstance` (LRO)  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.DeleteShare` (LRO)  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.DeleteSnapshot` (LRO)  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.PauseReplica` (LRO)  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.PromoteReplica` (LRO)  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.ReleaseShare`  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.RestoreInstance` (LRO)  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.ResumeReplica` (LRO)  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.RevertInstance` (LRO)  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.UpdateBackup` (LRO)  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.UpdateInstance` (LRO)  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.UpdateShare` (LRO)  
`google.cloud.filestore.v1beta1.CloudFilestoreManager.UpdateSnapshot` (LRO)  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Filestore.

### `google.cloud.filestore.v1.CloudFilestoreManager`

The following audit logs are associated with methods belonging to `google.cloud.filestore.v1.CloudFilestoreManager`.

#### `CreateBackup`

  * **Method** : `google.cloud.filestore.v1.CloudFilestoreManager.CreateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.backups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1.CloudFilestoreManager.CreateBackup" `  




#### `CreateInstance`

  * **Method** : `google.cloud.filestore.v1.CloudFilestoreManager.CreateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1.CloudFilestoreManager.CreateInstance" `  




#### `CreateSnapshot`

  * **Method** : `google.cloud.filestore.v1.CloudFilestoreManager.CreateSnapshot`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.snapshots.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1.CloudFilestoreManager.CreateSnapshot" `  




#### `DeleteBackup`

  * **Method** : `google.cloud.filestore.v1.CloudFilestoreManager.DeleteBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.backups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1.CloudFilestoreManager.DeleteBackup" `  




#### `DeleteInstance`

  * **Method** : `google.cloud.filestore.v1.CloudFilestoreManager.DeleteInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.instances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1.CloudFilestoreManager.DeleteInstance" `  




#### `DeleteSnapshot`

  * **Method** : `google.cloud.filestore.v1.CloudFilestoreManager.DeleteSnapshot`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.snapshots.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1.CloudFilestoreManager.DeleteSnapshot" `  




#### `GetBackup`

  * **Method** : `google.cloud.filestore.v1.CloudFilestoreManager.GetBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `file.backups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1.CloudFilestoreManager.GetBackup" `  




#### `GetInstance`

  * **Method** : `google.cloud.filestore.v1.CloudFilestoreManager.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `file.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1.CloudFilestoreManager.GetInstance" `  




#### `GetSnapshot`

  * **Method** : `google.cloud.filestore.v1.CloudFilestoreManager.GetSnapshot`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `file.snapshots.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1.CloudFilestoreManager.GetSnapshot" `  




#### `ListBackups`

  * **Method** : `google.cloud.filestore.v1.CloudFilestoreManager.ListBackups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `file.backups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1.CloudFilestoreManager.ListBackups" `  




#### `ListInstances`

  * **Method** : `google.cloud.filestore.v1.CloudFilestoreManager.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `file.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1.CloudFilestoreManager.ListInstances" `  




#### `ListSnapshots`

  * **Method** : `google.cloud.filestore.v1.CloudFilestoreManager.ListSnapshots`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `file.snapshots.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1.CloudFilestoreManager.ListSnapshots" `  




#### `PauseReplica`

  * **Method** : `google.cloud.filestore.v1.CloudFilestoreManager.PauseReplica`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1.CloudFilestoreManager.PauseReplica" `  




#### `PromoteReplica`

  * **Method** : `google.cloud.filestore.v1.CloudFilestoreManager.PromoteReplica`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1.CloudFilestoreManager.PromoteReplica" `  




#### `RestoreInstance`

  * **Method** : `google.cloud.filestore.v1.CloudFilestoreManager.RestoreInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.instances.restore - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1.CloudFilestoreManager.RestoreInstance" `  




#### `ResumeReplica`

  * **Method** : `google.cloud.filestore.v1.CloudFilestoreManager.ResumeReplica`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1.CloudFilestoreManager.ResumeReplica" `  




#### `RevertInstance`

  * **Method** : `google.cloud.filestore.v1.CloudFilestoreManager.RevertInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.instances.revert - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1.CloudFilestoreManager.RevertInstance" `  




#### `UpdateBackup`

  * **Method** : `google.cloud.filestore.v1.CloudFilestoreManager.UpdateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.backups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1.CloudFilestoreManager.UpdateBackup" `  




#### `UpdateInstance`

  * **Method** : `google.cloud.filestore.v1.CloudFilestoreManager.UpdateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1.CloudFilestoreManager.UpdateInstance" `  




#### `UpdateSnapshot`

  * **Method** : `google.cloud.filestore.v1.CloudFilestoreManager.UpdateSnapshot`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.snapshots.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1.CloudFilestoreManager.UpdateSnapshot" `  




### `google.cloud.filestore.v1beta1.CloudFilestoreManager`

The following audit logs are associated with methods belonging to `google.cloud.filestore.v1beta1.CloudFilestoreManager`.

#### `AcquireShare`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.AcquireShare`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.shares.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.AcquireShare" `  




#### `CreateBackup`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.CreateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.backups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.CreateBackup" `  




#### `CreateInstance`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.CreateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.CreateInstance" `  




#### `CreateShare`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.CreateShare`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.shares.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.CreateShare" `  




#### `CreateSnapshot`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.CreateSnapshot`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.snapshots.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.CreateSnapshot" `  




#### `DeleteBackup`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.DeleteBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.backups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.DeleteBackup" `  




#### `DeleteInstance`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.DeleteInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.instances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.DeleteInstance" `  




#### `DeleteShare`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.DeleteShare`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.shares.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.DeleteShare" `  




#### `DeleteSnapshot`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.DeleteSnapshot`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.snapshots.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.DeleteSnapshot" `  




#### `GetBackup`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.GetBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `file.backups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.GetBackup" `  




#### `GetInstance`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `file.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.GetInstance" `  




#### `GetShare`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.GetShare`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `file.shares.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.GetShare" `  




#### `GetSnapshot`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.GetSnapshot`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `file.snapshots.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.GetSnapshot" `  




#### `ListBackups`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.ListBackups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `file.backups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.ListBackups" `  




#### `ListInstances`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `file.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.ListInstances" `  




#### `ListShares`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.ListShares`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `file.shares.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.ListShares" `  




#### `ListSnapshots`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.ListSnapshots`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `file.snapshots.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.ListSnapshots" `  




#### `PauseReplica`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.PauseReplica`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.PauseReplica" `  




#### `PromoteReplica`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.PromoteReplica`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.PromoteReplica" `  




#### `ReleaseShare`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.ReleaseShare`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.shares.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.ReleaseShare" `  




#### `RestoreInstance`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.RestoreInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.instances.restore - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.RestoreInstance" `  




#### `ResumeReplica`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.ResumeReplica`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.ResumeReplica" `  




#### `RevertInstance`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.RevertInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.instances.revert - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.RevertInstance" `  




#### `UpdateBackup`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.UpdateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.backups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.UpdateBackup" `  




#### `UpdateInstance`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.UpdateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.UpdateInstance" `  




#### `UpdateShare`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.UpdateShare`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.shares.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.UpdateShare" `  




#### `UpdateSnapshot`

  * **Method** : `google.cloud.filestore.v1beta1.CloudFilestoreManager.UpdateSnapshot`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.snapshots.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.filestore.v1beta1.CloudFilestoreManager.UpdateSnapshot" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `file.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `file.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `file.operations.list - ADMIN_READ`
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
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
