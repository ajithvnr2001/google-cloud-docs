---
url: https://docs.cloud.google.com/bigtable/docs/audit-logging-bigtableadmin/
title: Cloud Bigtable Admin API audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:13.133325+00:00
---

# Cloud Bigtable Admin API audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/audit-logging-bigtableadmin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Bigtable Admin API audit logging

This document lists the audited methods for Cloud Bigtable Admin API. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Cloud Bigtable Admin API audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="bigtableadmin.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Bigtable Admin API generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.bigtable.admin.v2.BigtableInstanceAdmin.GetAppProfile`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.GetCluster`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.GetIamPolicy`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.GetInstance`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.GetLogicalView`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.GetMaterializedView`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.GetMemoryLayer`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.ListAppProfiles`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.ListClusters`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.ListHotTablets`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.ListInstances`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.ListLogicalViews`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.ListMaterializedViews`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.ListMemoryLayers`  
`google.bigtable.admin.v2.BigtableTableAdmin.CheckConsistency`  
`google.bigtable.admin.v2.BigtableTableAdmin.GenerateConsistencyToken`  
`google.bigtable.admin.v2.BigtableTableAdmin.GetAuthorizedView`  
`google.bigtable.admin.v2.BigtableTableAdmin.GetBackup`  
`google.bigtable.admin.v2.BigtableTableAdmin.GetIamPolicy`  
`google.bigtable.admin.v2.BigtableTableAdmin.GetSchemaBundle`  
`google.bigtable.admin.v2.BigtableTableAdmin.GetTable`  
`google.bigtable.admin.v2.BigtableTableAdmin.ListAuthorizedViews`  
`google.bigtable.admin.v2.BigtableTableAdmin.ListBackups`  
`google.bigtable.admin.v2.BigtableTableAdmin.ListSchemaBundles`  
`google.bigtable.admin.v2.BigtableTableAdmin.ListTables`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.bigtable.admin.v2.BigtableInstanceAdmin.CreateAppProfile`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.CreateCluster` (LRO)  
`google.bigtable.admin.v2.BigtableInstanceAdmin.CreateInstance` (LRO)  
`google.bigtable.admin.v2.BigtableInstanceAdmin.CreateLogicalView` (LRO)  
`google.bigtable.admin.v2.BigtableInstanceAdmin.CreateMaterializedView` (LRO)  
`google.bigtable.admin.v2.BigtableInstanceAdmin.DeleteAppProfile`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.DeleteCluster`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.DeleteInstance`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.DeleteLogicalView`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.DeleteMaterializedView`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.PartialUpdateCluster` (LRO)  
`google.bigtable.admin.v2.BigtableInstanceAdmin.PartialUpdateInstance` (LRO)  
`google.bigtable.admin.v2.BigtableInstanceAdmin.SetIamPolicy`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.UpdateAppProfile` (LRO)  
`google.bigtable.admin.v2.BigtableInstanceAdmin.UpdateCluster` (LRO)  
`google.bigtable.admin.v2.BigtableInstanceAdmin.UpdateInstance`  
`google.bigtable.admin.v2.BigtableInstanceAdmin.UpdateLogicalView` (LRO)  
`google.bigtable.admin.v2.BigtableInstanceAdmin.UpdateMaterializedView` (LRO)  
`google.bigtable.admin.v2.BigtableTableAdmin.CopyBackup` (LRO)  
`google.bigtable.admin.v2.BigtableTableAdmin.CreateAuthorizedView` (LRO)  
`google.bigtable.admin.v2.BigtableTableAdmin.CreateBackup` (LRO)  
`google.bigtable.admin.v2.BigtableTableAdmin.CreateSchemaBundle` (LRO)  
`google.bigtable.admin.v2.BigtableTableAdmin.CreateTable`  
`google.bigtable.admin.v2.BigtableTableAdmin.DeleteAuthorizedView`  
`google.bigtable.admin.v2.BigtableTableAdmin.DeleteBackup`  
`google.bigtable.admin.v2.BigtableTableAdmin.DeleteSchemaBundle`  
`google.bigtable.admin.v2.BigtableTableAdmin.DeleteTable`  
`google.bigtable.admin.v2.BigtableTableAdmin.ModifyColumnFamilies`  
`google.bigtable.admin.v2.BigtableTableAdmin.RestoreTable` (LRO)  
`google.bigtable.admin.v2.BigtableTableAdmin.SetIamPolicy`  
`google.bigtable.admin.v2.BigtableTableAdmin.UndeleteTable` (LRO)  
`google.bigtable.admin.v2.BigtableTableAdmin.UpdateAuthorizedView` (LRO)  
`google.bigtable.admin.v2.BigtableTableAdmin.UpdateBackup`  
`google.bigtable.admin.v2.BigtableTableAdmin.UpdateSchemaBundle` (LRO)  
`google.bigtable.admin.v2.BigtableTableAdmin.UpdateTable` (LRO)  
`DATA_WRITE` | `google.bigtable.admin.v2.BigtableTableAdmin.DropRowRange`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Bigtable Admin API.

### `google.bigtable.admin.v2.BigtableInstanceAdmin`

The following audit logs are associated with methods belonging to `google.bigtable.admin.v2.BigtableInstanceAdmin`.

#### `CreateAppProfile`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.CreateAppProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.appProfiles.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.CreateAppProfile" `  




#### `CreateCluster`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.CreateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.CreateCluster" `  




#### `CreateInstance`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.CreateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.clusters.create - ADMIN_WRITE`
    * `bigtable.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.CreateInstance" `  




#### `CreateLogicalView`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.CreateLogicalView`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.logicalViews.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.CreateLogicalView" `  




#### `CreateMaterializedView`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.CreateMaterializedView`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.materializedViews.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.CreateMaterializedView" `  




#### `DeleteAppProfile`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.DeleteAppProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.appProfiles.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.DeleteAppProfile" `  




#### `DeleteCluster`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.DeleteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.clusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.DeleteCluster" `  




#### `DeleteInstance`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.DeleteInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.instances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.DeleteInstance" `  




#### `DeleteLogicalView`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.DeleteLogicalView`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.logicalViews.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.DeleteLogicalView" `  




#### `DeleteMaterializedView`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.DeleteMaterializedView`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.materializedViews.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.DeleteMaterializedView" `  




#### `GetAppProfile`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.GetAppProfile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.appProfiles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.GetAppProfile" `  




#### `GetCluster`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.GetCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.GetCluster" `  




#### `GetIamPolicy`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.instances.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.GetIamPolicy" `  




#### `GetInstance`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.GetInstance" `  




#### `GetLogicalView`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.GetLogicalView`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.logicalViews.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.GetLogicalView" `  




#### `GetMaterializedView`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.GetMaterializedView`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.materializedViews.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.GetMaterializedView" `  




#### `GetMemoryLayer`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.GetMemoryLayer`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.memoryLayers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.GetMemoryLayer" `  




#### `ListAppProfiles`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.ListAppProfiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.appProfiles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.ListAppProfiles" `  




#### `ListClusters`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.ListClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.clusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.ListClusters" `  




#### `ListHotTablets`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.ListHotTablets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.hotTablets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.ListHotTablets" `  




#### `ListInstances`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.ListInstances" `  




#### `ListLogicalViews`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.ListLogicalViews`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.logicalViews.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.ListLogicalViews" `  




#### `ListMaterializedViews`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.ListMaterializedViews`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.materializedViews.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.ListMaterializedViews" `  




#### `ListMemoryLayers`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.ListMemoryLayers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.memoryLayers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.ListMemoryLayers" `  




#### `PartialUpdateCluster`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.PartialUpdateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.PartialUpdateCluster" `  




#### `PartialUpdateInstance`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.PartialUpdateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.PartialUpdateInstance" `  




#### `SetIamPolicy`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.instances.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.SetIamPolicy" `  




#### `UpdateAppProfile`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.UpdateAppProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.appProfiles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.UpdateAppProfile" `  




#### `UpdateCluster`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.UpdateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.UpdateCluster" `  




#### `UpdateInstance`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.UpdateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.UpdateInstance" `  




#### `UpdateLogicalView`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.UpdateLogicalView`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.logicalViews.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.UpdateLogicalView" `  




#### `UpdateMaterializedView`

  * **Method** : `google.bigtable.admin.v2.BigtableInstanceAdmin.UpdateMaterializedView`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.materializedViews.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableInstanceAdmin.UpdateMaterializedView" `  




### `google.bigtable.admin.v2.BigtableTableAdmin`

The following audit logs are associated with methods belonging to `google.bigtable.admin.v2.BigtableTableAdmin`.

#### `CheckConsistency`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.CheckConsistency`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.tables.checkConsistency - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.CheckConsistency" `  




#### `CopyBackup`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.CopyBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.backups.create - ADMIN_WRITE`
    * `bigtable.backups.read - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.CopyBackup" `  




#### `CreateAuthorizedView`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.CreateAuthorizedView`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.authorizedViews.create - ADMIN_WRITE`
    * `bigtable.tables.mutateRows - DATA_WRITE`
    * `bigtable.tables.readRows - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.CreateAuthorizedView" `  




#### `CreateBackup`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.CreateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.backups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.CreateBackup" `  




#### `CreateSchemaBundle`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.CreateSchemaBundle`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.schemaBundles.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.CreateSchemaBundle" `  




#### `CreateTable`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.CreateTable`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.tables.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.CreateTable" `  




#### `DeleteAuthorizedView`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.DeleteAuthorizedView`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.authorizedViews.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.DeleteAuthorizedView" `  




#### `DeleteBackup`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.DeleteBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.backups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.DeleteBackup" `  




#### `DeleteSchemaBundle`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.DeleteSchemaBundle`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.schemaBundles.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.DeleteSchemaBundle" `  




#### `DeleteTable`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.DeleteTable`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.tables.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.DeleteTable" `  




#### `DropRowRange`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.DropRowRange`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.tables.mutateRows - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.DropRowRange" `  




#### `GenerateConsistencyToken`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.GenerateConsistencyToken`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.tables.generateConsistencyToken - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.GenerateConsistencyToken" `  




#### `GetAuthorizedView`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.GetAuthorizedView`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.authorizedViews.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.GetAuthorizedView" `  




#### `GetBackup`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.GetBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.backups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.GetBackup" `  




#### `GetIamPolicy`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.backups.getIamPolicy - ADMIN_READ`
    * `bigtable.tables.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.GetIamPolicy" `  




#### `GetSchemaBundle`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.GetSchemaBundle`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.schemaBundles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.GetSchemaBundle" `  




#### `GetTable`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.GetTable`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.tables.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.GetTable" `  




#### `ListAuthorizedViews`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.ListAuthorizedViews`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.authorizedViews.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.ListAuthorizedViews" `  




#### `ListBackups`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.ListBackups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.backups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.ListBackups" `  




#### `ListSchemaBundles`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.ListSchemaBundles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.schemaBundles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.ListSchemaBundles" `  




#### `ListTables`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.ListTables`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.tables.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.ListTables" `  




#### `ModifyColumnFamilies`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.ModifyColumnFamilies`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.instances.list - ADMIN_READ`
    * `bigtable.tables.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.ModifyColumnFamilies" `  




#### `RestoreTable`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.RestoreTable`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.tables.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.RestoreTable" `  




#### `SetIamPolicy`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.tables.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.SetIamPolicy" `  




#### `UndeleteTable`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.UndeleteTable`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.tables.undelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.UndeleteTable" `  




#### `UpdateAuthorizedView`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.UpdateAuthorizedView`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.authorizedViews.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.UpdateAuthorizedView" `  




#### `UpdateBackup`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.UpdateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.backups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.UpdateBackup" `  




#### `UpdateSchemaBundle`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.UpdateSchemaBundle`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.schemaBundles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.UpdateSchemaBundle" `  




#### `UpdateTable`

  * **Method** : `google.bigtable.admin.v2.BigtableTableAdmin.UpdateTable`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `bigtable.tables.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.bigtable.admin.v2.BigtableTableAdmin.UpdateTable" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `bigtable.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## System events

System Event audit logs are generated by GCP systems, not direct user action. For more information, see [System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event).

Method Name | Filter For This Event | Notes  
---|---|---  
AutoscaleCluster |  ` protoPayload.methodName="AutoscaleCluster" ` |   
CreateAutomatedBackup |  ` protoPayload.methodName="CreateAutomatedBackup" ` |   
DelayedAutomatedBackup |  ` protoPayload.methodName="DelayedAutomatedBackup" ` |   
  
## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.bigtable.admin.v2.BigtableInstanceAdmin.TestIamPermissions`
  * `google.bigtable.admin.v2.BigtableTableAdmin.TestIamPermissions`
  * `google.cloud.location.Locations.ListLocations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
