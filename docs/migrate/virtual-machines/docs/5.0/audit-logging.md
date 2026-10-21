---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/audit-logging/
title: Migrate to Virtual Machines audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:08:56.991334+00:00
---

# Migrate to Virtual Machines audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Migrate to Virtual Machines audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Migrate to Virtual Machines. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Migrate to Virtual Machines audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="vmmigration.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Migrate to Virtual Machines generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.vmmigration.v1.VmMigration.FetchInventory`  
`google.cloud.vmmigration.v1.VmMigration.FetchStorageInventory`  
`google.cloud.vmmigration.v1.VmMigration.GetCloneJob`  
`google.cloud.vmmigration.v1.VmMigration.GetCutoverJob`  
`google.cloud.vmmigration.v1.VmMigration.GetDatacenterConnector`  
`google.cloud.vmmigration.v1.VmMigration.GetDiskMigrationJob`  
`google.cloud.vmmigration.v1.VmMigration.GetGroup`  
`google.cloud.vmmigration.v1.VmMigration.GetImageImport`  
`google.cloud.vmmigration.v1.VmMigration.GetImageImportJob`  
`google.cloud.vmmigration.v1.VmMigration.GetMigratingVm`  
`google.cloud.vmmigration.v1.VmMigration.GetReplicationCycle`  
`google.cloud.vmmigration.v1.VmMigration.GetSource`  
`google.cloud.vmmigration.v1.VmMigration.GetTargetProject`  
`google.cloud.vmmigration.v1.VmMigration.GetUtilizationReport`  
`google.cloud.vmmigration.v1.VmMigration.ListCloneJobs`  
`google.cloud.vmmigration.v1.VmMigration.ListCutoverJobs`  
`google.cloud.vmmigration.v1.VmMigration.ListDatacenterConnectors`  
`google.cloud.vmmigration.v1.VmMigration.ListDiskMigrationJobs`  
`google.cloud.vmmigration.v1.VmMigration.ListGroups`  
`google.cloud.vmmigration.v1.VmMigration.ListImageImportJobs`  
`google.cloud.vmmigration.v1.VmMigration.ListImageImports`  
`google.cloud.vmmigration.v1.VmMigration.ListMigratingVms`  
`google.cloud.vmmigration.v1.VmMigration.ListReplicationCycles`  
`google.cloud.vmmigration.v1.VmMigration.ListSources`  
`google.cloud.vmmigration.v1.VmMigration.ListTargetProjects`  
`google.cloud.vmmigration.v1.VmMigration.ListUtilizationReports`  
`google.cloud.vmmigration.v1alpha1.VmMigration.FetchInventory`  
`google.cloud.vmmigration.v1alpha1.VmMigration.FetchStorageInventory`  
`google.cloud.vmmigration.v1alpha1.VmMigration.GetCloneJob`  
`google.cloud.vmmigration.v1alpha1.VmMigration.GetCutoverJob`  
`google.cloud.vmmigration.v1alpha1.VmMigration.GetDatacenterConnector`  
`google.cloud.vmmigration.v1alpha1.VmMigration.GetDiskMigrationJob`  
`google.cloud.vmmigration.v1alpha1.VmMigration.GetGroup`  
`google.cloud.vmmigration.v1alpha1.VmMigration.GetImageImport`  
`google.cloud.vmmigration.v1alpha1.VmMigration.GetImageImportJob`  
`google.cloud.vmmigration.v1alpha1.VmMigration.GetMigratingVm`  
`google.cloud.vmmigration.v1alpha1.VmMigration.GetReplicationCycle`  
`google.cloud.vmmigration.v1alpha1.VmMigration.GetSource`  
`google.cloud.vmmigration.v1alpha1.VmMigration.GetTargetProject`  
`google.cloud.vmmigration.v1alpha1.VmMigration.GetUtilizationReport`  
`google.cloud.vmmigration.v1alpha1.VmMigration.ListCloneJobs`  
`google.cloud.vmmigration.v1alpha1.VmMigration.ListCutoverJobs`  
`google.cloud.vmmigration.v1alpha1.VmMigration.ListDatacenterConnectors`  
`google.cloud.vmmigration.v1alpha1.VmMigration.ListDiskMigrationJobs`  
`google.cloud.vmmigration.v1alpha1.VmMigration.ListGroups`  
`google.cloud.vmmigration.v1alpha1.VmMigration.ListImageImportJobs`  
`google.cloud.vmmigration.v1alpha1.VmMigration.ListImageImports`  
`google.cloud.vmmigration.v1alpha1.VmMigration.ListMigratingVms`  
`google.cloud.vmmigration.v1alpha1.VmMigration.ListReplicationCycles`  
`google.cloud.vmmigration.v1alpha1.VmMigration.ListSources`  
`google.cloud.vmmigration.v1alpha1.VmMigration.ListTargetProjects`  
`google.cloud.vmmigration.v1alpha1.VmMigration.ListUtilizationReports`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.vmmigration.v1.VmMigration.AddGroupMigration` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.CancelCloneJob` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.CancelCutoverJob` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.CancelDiskMigrationJob`  
`google.cloud.vmmigration.v1.VmMigration.CancelImageImportJob` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.CreateCloneJob` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.CreateCutoverJob` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.CreateDatacenterConnector` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.CreateDiskMigrationJob` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.CreateGroup` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.CreateImageImport` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.CreateMigratingVm` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.CreateSource` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.CreateTargetProject` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.CreateUtilizationReport` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.DeleteDatacenterConnector` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.DeleteDiskMigrationJob` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.DeleteGroup` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.DeleteImageImport` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.DeleteMigratingVm` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.DeleteSource` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.DeleteTargetProject` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.DeleteUtilizationReport` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.ExtendMigration`  
`google.cloud.vmmigration.v1.VmMigration.FinalizeMigration` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.PauseMigration` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.RemoveGroupMigration` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.ResumeMigration` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.RunDiskMigrationJob` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.StartMigration` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.UpdateDiskMigrationJob`  
`google.cloud.vmmigration.v1.VmMigration.UpdateGroup` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.UpdateMigratingVm` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.UpdateSource` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.UpdateTargetProject` (LRO)  
`google.cloud.vmmigration.v1.VmMigration.UpgradeAppliance`  
`google.cloud.vmmigration.v1alpha1.VmMigration.AddGroupMigration` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.CancelCloneJob` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.CancelCutoverJob` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.CancelDiskMigrationJob` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.CancelImageImportJob`  
`google.cloud.vmmigration.v1alpha1.VmMigration.CreateCloneJob` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.CreateCutoverJob` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.CreateDatacenterConnector` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.CreateDiskMigrationJob` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.CreateGroup` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.CreateImageImport` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.CreateMigratingVm` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.CreateSource` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.CreateTargetProject` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.CreateUtilizationReport` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.DeleteDatacenterConnector` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.DeleteDiskMigrationJob` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.DeleteGroup` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.DeleteImageImport` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.DeleteMigratingVm` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.DeleteSource` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.DeleteTargetProject` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.DeleteUtilizationReport` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.ExtendMigration` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.FinalizeMigration` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.PauseMigration` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.RemoveGroupMigration` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.ResumeMigration` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.RunDiskMigrationJob` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.StartMigration` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.UpdateDiskMigrationJob` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.UpdateGroup` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.UpdateMigratingVm` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.UpdateSource` (LRO)  
`google.cloud.vmmigration.v1alpha1.VmMigration.UpdateTargetProject`  
`google.cloud.vmmigration.v1alpha1.VmMigration.UpgradeAppliance` (LRO)  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Migrate to Virtual Machines.

### `google.cloud.vmmigration.v1.VmMigration`

The following audit logs are associated with methods belonging to `google.cloud.vmmigration.v1.VmMigration`.

#### `AddGroupMigration`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.AddGroupMigration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.groups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.AddGroupMigration" `  




#### `CancelCloneJob`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.CancelCloneJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.cloneJobs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.CancelCloneJob" `  




#### `CancelCutoverJob`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.CancelCutoverJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.cutoverJobs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.CancelCutoverJob" `  




#### `CancelDiskMigrationJob`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.CancelDiskMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.CancelDiskMigrationJob" `  




#### `CancelImageImportJob`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.CancelImageImportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.imageImportJobs.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.CancelImageImportJob" `  




#### `CreateCloneJob`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.CreateCloneJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.cloneJobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.CreateCloneJob" `  




#### `CreateCutoverJob`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.CreateCutoverJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.cutoverJobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.CreateCutoverJob" `  




#### `CreateDatacenterConnector`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.CreateDatacenterConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.datacenterConnectors.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.CreateDatacenterConnector" `  




#### `CreateDiskMigrationJob`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.CreateDiskMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.CreateDiskMigrationJob" `  




#### `CreateGroup`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.CreateGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.groups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.CreateGroup" `  




#### `CreateImageImport`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.CreateImageImport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.imageImports.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.CreateImageImport" `  




#### `CreateMigratingVm`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.CreateMigratingVm`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.CreateMigratingVm" `  




#### `CreateSource`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.CreateSource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.sources.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.CreateSource" `  




#### `CreateTargetProject`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.CreateTargetProject`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.targets.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.CreateTargetProject" `  




#### `CreateUtilizationReport`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.CreateUtilizationReport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.utilizationReports.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.CreateUtilizationReport" `  




#### `DeleteDatacenterConnector`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.DeleteDatacenterConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.datacenterConnectors.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.DeleteDatacenterConnector" `  




#### `DeleteDiskMigrationJob`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.DeleteDiskMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.DeleteDiskMigrationJob" `  




#### `DeleteGroup`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.DeleteGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.groups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.DeleteGroup" `  




#### `DeleteImageImport`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.DeleteImageImport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.imageImports.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.DeleteImageImport" `  




#### `DeleteMigratingVm`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.DeleteMigratingVm`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.DeleteMigratingVm" `  




#### `DeleteSource`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.DeleteSource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.sources.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.DeleteSource" `  




#### `DeleteTargetProject`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.DeleteTargetProject`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.targets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.DeleteTargetProject" `  




#### `DeleteUtilizationReport`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.DeleteUtilizationReport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.utilizationReports.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.DeleteUtilizationReport" `  




#### `ExtendMigration`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.ExtendMigration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.ExtendMigration" `  




#### `FetchInventory`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.FetchInventory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.sources.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.FetchInventory" `  




#### `FetchStorageInventory`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.FetchStorageInventory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.sources.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.FetchStorageInventory" `  




#### `FinalizeMigration`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.FinalizeMigration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.FinalizeMigration" `  




#### `GetCloneJob`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.GetCloneJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.cloneJobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.GetCloneJob" `  




#### `GetCutoverJob`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.GetCutoverJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.cutoverJobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.GetCutoverJob" `  




#### `GetDatacenterConnector`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.GetDatacenterConnector`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.datacenterConnectors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.GetDatacenterConnector" `  




#### `GetDiskMigrationJob`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.GetDiskMigrationJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.migratingVms.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.GetDiskMigrationJob" `  




#### `GetGroup`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.GetGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.groups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.GetGroup" `  




#### `GetImageImport`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.GetImageImport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.imageImports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.GetImageImport" `  




#### `GetImageImportJob`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.GetImageImportJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.imageImportJobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.GetImageImportJob" `  




#### `GetMigratingVm`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.GetMigratingVm`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.migratingVms.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.GetMigratingVm" `  




#### `GetReplicationCycle`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.GetReplicationCycle`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.replicationCycles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.GetReplicationCycle" `  




#### `GetSource`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.GetSource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.sources.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.GetSource" `  




#### `GetTargetProject`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.GetTargetProject`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.targets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.GetTargetProject" `  




#### `GetUtilizationReport`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.GetUtilizationReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.utilizationReports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.GetUtilizationReport" `  




#### `ListCloneJobs`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.ListCloneJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.cloneJobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.ListCloneJobs" `  




#### `ListCutoverJobs`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.ListCutoverJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.cutoverJobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.ListCutoverJobs" `  




#### `ListDatacenterConnectors`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.ListDatacenterConnectors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.datacenterConnectors.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.ListDatacenterConnectors" `  




#### `ListDiskMigrationJobs`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.ListDiskMigrationJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.migratingVms.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.ListDiskMigrationJobs" `  




#### `ListGroups`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.ListGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.groups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.ListGroups" `  




#### `ListImageImportJobs`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.ListImageImportJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.imageImportJobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.ListImageImportJobs" `  




#### `ListImageImports`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.ListImageImports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.imageImports.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.ListImageImports" `  




#### `ListMigratingVms`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.ListMigratingVms`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.migratingVms.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.ListMigratingVms" `  




#### `ListReplicationCycles`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.ListReplicationCycles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.replicationCycles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.ListReplicationCycles" `  




#### `ListSources`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.ListSources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.sources.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.ListSources" `  




#### `ListTargetProjects`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.ListTargetProjects`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.targets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.ListTargetProjects" `  




#### `ListUtilizationReports`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.ListUtilizationReports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.utilizationReports.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.ListUtilizationReports" `  




#### `PauseMigration`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.PauseMigration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.PauseMigration" `  




#### `RemoveGroupMigration`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.RemoveGroupMigration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.groups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.RemoveGroupMigration" `  




#### `ResumeMigration`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.ResumeMigration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.ResumeMigration" `  




#### `RunDiskMigrationJob`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.RunDiskMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.RunDiskMigrationJob" `  




#### `StartMigration`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.StartMigration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.StartMigration" `  




#### `UpdateDiskMigrationJob`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.UpdateDiskMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.UpdateDiskMigrationJob" `  




#### `UpdateGroup`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.UpdateGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.groups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.UpdateGroup" `  




#### `UpdateMigratingVm`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.UpdateMigratingVm`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.UpdateMigratingVm" `  




#### `UpdateSource`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.UpdateSource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.sources.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.UpdateSource" `  




#### `UpdateTargetProject`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.UpdateTargetProject`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.targets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.UpdateTargetProject" `  




#### `UpgradeAppliance`

  * **Method** : `google.cloud.vmmigration.v1.VmMigration.UpgradeAppliance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.datacenterConnectors.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1.VmMigration.UpgradeAppliance" `  




### `google.cloud.vmmigration.v1alpha1.VmMigration`

The following audit logs are associated with methods belonging to `google.cloud.vmmigration.v1alpha1.VmMigration`.

#### `AddGroupMigration`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.AddGroupMigration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.groups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.AddGroupMigration" `  




#### `CancelCloneJob`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.CancelCloneJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.cloneJobs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.CancelCloneJob" `  




#### `CancelCutoverJob`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.CancelCutoverJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.cutoverJobs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.CancelCutoverJob" `  




#### `CancelDiskMigrationJob`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.CancelDiskMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.CancelDiskMigrationJob" `  




#### `CancelImageImportJob`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.CancelImageImportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.imageImportJobs.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.CancelImageImportJob" `  




#### `CreateCloneJob`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.CreateCloneJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.cloneJobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.CreateCloneJob" `  




#### `CreateCutoverJob`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.CreateCutoverJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.cutoverJobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.CreateCutoverJob" `  




#### `CreateDatacenterConnector`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.CreateDatacenterConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.datacenterConnectors.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.CreateDatacenterConnector" `  




#### `CreateDiskMigrationJob`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.CreateDiskMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.CreateDiskMigrationJob" `  




#### `CreateGroup`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.CreateGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.groups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.CreateGroup" `  




#### `CreateImageImport`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.CreateImageImport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.imageImports.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.CreateImageImport" `  




#### `CreateMigratingVm`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.CreateMigratingVm`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.CreateMigratingVm" `  




#### `CreateSource`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.CreateSource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.sources.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.CreateSource" `  




#### `CreateTargetProject`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.CreateTargetProject`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.targets.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.CreateTargetProject" `  




#### `CreateUtilizationReport`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.CreateUtilizationReport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.utilizationReports.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.CreateUtilizationReport" `  




#### `DeleteDatacenterConnector`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.DeleteDatacenterConnector`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.datacenterConnectors.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.DeleteDatacenterConnector" `  




#### `DeleteDiskMigrationJob`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.DeleteDiskMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.DeleteDiskMigrationJob" `  




#### `DeleteGroup`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.DeleteGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.groups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.DeleteGroup" `  




#### `DeleteImageImport`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.DeleteImageImport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.imageImports.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.DeleteImageImport" `  




#### `DeleteMigratingVm`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.DeleteMigratingVm`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.DeleteMigratingVm" `  




#### `DeleteSource`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.DeleteSource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.sources.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.DeleteSource" `  




#### `DeleteTargetProject`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.DeleteTargetProject`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.targets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.DeleteTargetProject" `  




#### `DeleteUtilizationReport`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.DeleteUtilizationReport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.utilizationReports.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.DeleteUtilizationReport" `  




#### `ExtendMigration`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.ExtendMigration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.ExtendMigration" `  




#### `FetchInventory`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.FetchInventory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.sources.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.FetchInventory" `  




#### `FetchStorageInventory`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.FetchStorageInventory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.sources.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.FetchStorageInventory" `  




#### `FinalizeMigration`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.FinalizeMigration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.FinalizeMigration" `  




#### `GetCloneJob`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.GetCloneJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.cloneJobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.GetCloneJob" `  




#### `GetCutoverJob`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.GetCutoverJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.cutoverJobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.GetCutoverJob" `  




#### `GetDatacenterConnector`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.GetDatacenterConnector`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.datacenterConnectors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.GetDatacenterConnector" `  




#### `GetDiskMigrationJob`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.GetDiskMigrationJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.migratingVms.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.GetDiskMigrationJob" `  




#### `GetGroup`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.GetGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.groups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.GetGroup" `  




#### `GetImageImport`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.GetImageImport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.imageImports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.GetImageImport" `  




#### `GetImageImportJob`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.GetImageImportJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.imageImportJobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.GetImageImportJob" `  




#### `GetMigratingVm`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.GetMigratingVm`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.migratingVms.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.GetMigratingVm" `  




#### `GetReplicationCycle`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.GetReplicationCycle`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.replicationCycles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.GetReplicationCycle" `  




#### `GetSource`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.GetSource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.sources.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.GetSource" `  




#### `GetTargetProject`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.GetTargetProject`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.targets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.GetTargetProject" `  




#### `GetUtilizationReport`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.GetUtilizationReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.utilizationReports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.GetUtilizationReport" `  




#### `ListCloneJobs`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.ListCloneJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.cloneJobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.ListCloneJobs" `  




#### `ListCutoverJobs`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.ListCutoverJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.cutoverJobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.ListCutoverJobs" `  




#### `ListDatacenterConnectors`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.ListDatacenterConnectors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.datacenterConnectors.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.ListDatacenterConnectors" `  




#### `ListDiskMigrationJobs`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.ListDiskMigrationJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.migratingVms.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.ListDiskMigrationJobs" `  




#### `ListGroups`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.ListGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.groups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.ListGroups" `  




#### `ListImageImportJobs`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.ListImageImportJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.imageImportJobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.ListImageImportJobs" `  




#### `ListImageImports`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.ListImageImports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.imageImports.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.ListImageImports" `  




#### `ListMigratingVms`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.ListMigratingVms`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.migratingVms.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.ListMigratingVms" `  




#### `ListReplicationCycles`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.ListReplicationCycles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.replicationCycles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.ListReplicationCycles" `  




#### `ListSources`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.ListSources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.sources.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.ListSources" `  




#### `ListTargetProjects`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.ListTargetProjects`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.targets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.ListTargetProjects" `  




#### `ListUtilizationReports`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.ListUtilizationReports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.utilizationReports.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.ListUtilizationReports" `  




#### `PauseMigration`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.PauseMigration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.PauseMigration" `  




#### `RemoveGroupMigration`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.RemoveGroupMigration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.groups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.RemoveGroupMigration" `  




#### `ResumeMigration`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.ResumeMigration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.ResumeMigration" `  




#### `RunDiskMigrationJob`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.RunDiskMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.RunDiskMigrationJob" `  




#### `StartMigration`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.StartMigration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.StartMigration" `  




#### `UpdateDiskMigrationJob`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.UpdateDiskMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.UpdateDiskMigrationJob" `  




#### `UpdateGroup`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.UpdateGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.groups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.UpdateGroup" `  




#### `UpdateMigratingVm`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.UpdateMigratingVm`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.migratingVms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.UpdateMigratingVm" `  




#### `UpdateSource`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.UpdateSource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.sources.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.UpdateSource" `  




#### `UpdateTargetProject`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.UpdateTargetProject`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.targets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.UpdateTargetProject" `  




#### `UpgradeAppliance`

  * **Method** : `google.cloud.vmmigration.v1alpha1.VmMigration.UpgradeAppliance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.datacenterConnectors.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmmigration.v1alpha1.VmMigration.UpgradeAppliance" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmmigration.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmmigration.operations.list - ADMIN_READ`
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
