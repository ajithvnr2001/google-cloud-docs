---
url: https://docs.cloud.google.com/alloydb/docs/audit-logging/
title: AlloyDB for PostgreSQL audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:20.091333+00:00
---

# AlloyDB for PostgreSQL audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  AlloyDB for PostgreSQL audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for AlloyDB for PostgreSQL. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the AlloyDB for PostgreSQL audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="alloydb.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, AlloyDB for PostgreSQL generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.alloydb.v1.AlloyDBAdmin.GetBackup`  
`google.cloud.alloydb.v1.AlloyDBAdmin.GetCluster`  
`google.cloud.alloydb.v1.AlloyDBAdmin.GetInstance`  
`google.cloud.alloydb.v1.AlloyDBAdmin.GetUser`  
`google.cloud.alloydb.v1.AlloyDBAdmin.ListBackups`  
`google.cloud.alloydb.v1.AlloyDBAdmin.ListClusters`  
`google.cloud.alloydb.v1.AlloyDBAdmin.ListDatabases`  
`google.cloud.alloydb.v1.AlloyDBAdmin.ListInstances`  
`google.cloud.alloydb.v1.AlloyDBAdmin.ListUsers`  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.GetBackup`  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.GetCluster`  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.GetInstance`  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.GetUser`  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.ListBackups`  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.ListClusters`  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.ListInstances`  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.ListUsers`  
`google.cloud.alloydb.v1alpha.AlloyDBEndpointAdmin.GetEndpoint`  
`google.cloud.alloydb.v1alpha.AlloyDBEndpointAdmin.ListEndpoints`  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.GetBackup`  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.GetCluster`  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.GetInstance`  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.GetUser`  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.ListBackups`  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.ListClusters`  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.ListDatabases`  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.ListInstances`  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.ListUsers`  
`google.cloud.alloydb.v1beta.AlloyDBEndpointAdmin.GetEndpoint`  
`google.cloud.alloydb.v1beta.AlloyDBEndpointAdmin.ListEndpoints`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.alloydb.v1.AlloyDBAdmin.CreateBackup` (LRO)  
`google.cloud.alloydb.v1.AlloyDBAdmin.CreateCluster` (LRO)  
`google.cloud.alloydb.v1.AlloyDBAdmin.CreateInstance` (LRO)  
`google.cloud.alloydb.v1.AlloyDBAdmin.CreateSecondaryCluster` (LRO)  
`google.cloud.alloydb.v1.AlloyDBAdmin.CreateSecondaryInstance` (LRO)  
`google.cloud.alloydb.v1.AlloyDBAdmin.CreateUser`  
`google.cloud.alloydb.v1.AlloyDBAdmin.DeleteBackup` (LRO)  
`google.cloud.alloydb.v1.AlloyDBAdmin.DeleteCluster` (LRO)  
`google.cloud.alloydb.v1.AlloyDBAdmin.DeleteInstance` (LRO)  
`google.cloud.alloydb.v1.AlloyDBAdmin.DeleteUser`  
`google.cloud.alloydb.v1.AlloyDBAdmin.FailoverInstance` (LRO)  
`google.cloud.alloydb.v1.AlloyDBAdmin.GenerateClientCertificate`  
`google.cloud.alloydb.v1.AlloyDBAdmin.InjectFault` (LRO)  
`google.cloud.alloydb.v1.AlloyDBAdmin.PromoteCluster` (LRO)  
`google.cloud.alloydb.v1.AlloyDBAdmin.RestartInstance` (LRO)  
`google.cloud.alloydb.v1.AlloyDBAdmin.RestoreCluster` (LRO)  
`google.cloud.alloydb.v1.AlloyDBAdmin.SwitchoverCluster` (LRO)  
`google.cloud.alloydb.v1.AlloyDBAdmin.UpdateBackup` (LRO)  
`google.cloud.alloydb.v1.AlloyDBAdmin.UpdateCluster` (LRO)  
`google.cloud.alloydb.v1.AlloyDBAdmin.UpdateInstance` (LRO)  
`google.cloud.alloydb.v1.AlloyDBAdmin.UpdateUser`  
`google.cloud.alloydb.v1.AlloyDBAdmin.UpgradeCluster` (LRO)  
`google.cloud.alloydb.v1.AlloyDBCSQLAdmin.RestoreFromCloudSQL` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.BatchCreateInstances` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateBackup` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateCluster` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateDatabase`  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateInstance` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateSecondaryCluster` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateSecondaryInstance` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateUser`  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.DeleteBackup` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.DeleteCluster` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.DeleteInstance` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.DeleteUser`  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.FailoverInstance` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.GenerateClientCertificate`  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.InjectFault` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.PromoteCluster` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.RestartInstance` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.RestoreCluster` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.SwitchoverCluster` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.UpdateBackup` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.UpdateCluster` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.UpdateInstance` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.UpdateUser`  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.UpgradeCluster` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBCSQLAdmin.RestoreFromCloudSQL` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBEndpointAdmin.CreateEndpoint` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBEndpointAdmin.DeleteEndpoint` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBEndpointAdmin.UpdateEndpoint` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateBackup` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateCluster` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateDatabase`  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateInstance` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateSecondaryCluster` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateSecondaryInstance` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateUser`  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.DeleteBackup` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.DeleteCluster` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.DeleteInstance` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.DeleteUser`  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.FailoverInstance` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.GenerateClientCertificate`  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.InjectFault` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.PromoteCluster` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.RestartInstance` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.RestoreCluster` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.SwitchoverCluster` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.UpdateBackup` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.UpdateCluster` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.UpdateInstance` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.UpdateUser`  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.UpgradeCluster` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBCSQLAdmin.RestoreFromCloudSQL` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBEndpointAdmin.CreateEndpoint` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBEndpointAdmin.DeleteEndpoint` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBEndpointAdmin.UpdateEndpoint` (LRO)  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
`DATA_READ` | `google.cloud.alloydb.v1.AlloyDBAdmin.ExecuteSqlReadOnly`  
`google.cloud.alloydb.v1.AlloyDBAdmin.ExportCluster` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.ExecuteSqlReadOnly`  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.ExportCluster` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.ExecuteSqlReadOnly`  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.ExportCluster` (LRO)  
`DATA_WRITE` | `google.cloud.alloydb.v1.AlloyDBAdmin.ExecuteSql`  
`google.cloud.alloydb.v1.AlloyDBAdmin.ExecuteSqlReadOnly`  
`google.cloud.alloydb.v1.AlloyDBAdmin.ImportCluster` (LRO)  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.ExecuteSql`  
`google.cloud.alloydb.v1alpha.AlloyDBAdmin.ImportCluster` (LRO)  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.ExecuteSql`  
`google.cloud.alloydb.v1beta.AlloyDBAdmin.ImportCluster` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for AlloyDB for PostgreSQL.

### `google.cloud.alloydb.v1.AlloyDBAdmin`

The following audit logs are associated with methods belonging to `google.cloud.alloydb.v1.AlloyDBAdmin`.

#### `CreateBackup`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.CreateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.backups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.CreateBackup" `  




#### `CreateCluster`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.CreateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.CreateCluster" `  




#### `CreateInstance`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.CreateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.CreateInstance" `  




#### `CreateSecondaryCluster`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.CreateSecondaryCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.CreateSecondaryCluster" `  




#### `CreateSecondaryInstance`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.CreateSecondaryInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.CreateSecondaryInstance" `  




#### `CreateUser`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.CreateUser`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.users.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.CreateUser" `  




#### `DeleteBackup`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.DeleteBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.backups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.DeleteBackup" `  




#### `DeleteCluster`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.DeleteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.DeleteCluster" `  




#### `DeleteInstance`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.DeleteInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.DeleteInstance" `  




#### `DeleteUser`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.DeleteUser`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.users.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.DeleteUser" `  




#### `ExecuteSql`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.ExecuteSql`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.instances.executeSql - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.ExecuteSql" `  




#### `ExecuteSqlReadOnly`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.ExecuteSqlReadOnly`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.instances.executeSqlReadOnly - DATA_READ`
    * `alloydb.users.login - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.ExecuteSqlReadOnly" `  




#### `ExportCluster`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.ExportCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.clusters.export - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.ExportCluster" `  




#### `FailoverInstance`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.FailoverInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.failover - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.FailoverInstance" `  




#### `GenerateClientCertificate`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.GenerateClientCertificate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.generateClientCertificate - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.GenerateClientCertificate" `  




#### `GetBackup`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.GetBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.backups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.GetBackup" `  




#### `GetCluster`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.GetCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.GetCluster" `  




#### `GetInstance`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.GetInstance" `  




#### `GetUser`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.GetUser`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.users.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.GetUser" `  




#### `ImportCluster`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.ImportCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.clusters.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.ImportCluster" `  




#### `InjectFault`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.InjectFault`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.injectFault - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.InjectFault" `  




#### `ListBackups`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.ListBackups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.backups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.ListBackups" `  




#### `ListClusters`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.ListClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.clusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.ListClusters" `  




#### `ListDatabases`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.ListDatabases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.databases.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.ListDatabases" `  




#### `ListInstances`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.ListInstances" `  




#### `ListUsers`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.ListUsers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.users.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.ListUsers" `  




#### `PromoteCluster`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.PromoteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.promote - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.PromoteCluster" `  




#### `RestartInstance`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.RestartInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.restart - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.RestartInstance" `  




#### `RestoreCluster`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.RestoreCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.RestoreCluster" `  




#### `SwitchoverCluster`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.SwitchoverCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.get - ADMIN_READ`
    * `alloydb.clusters.switchover - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.SwitchoverCluster" `  




#### `UpdateBackup`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.UpdateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.backups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.UpdateBackup" `  




#### `UpdateCluster`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.UpdateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.UpdateCluster" `  




#### `UpdateInstance`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.UpdateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.UpdateInstance" `  




#### `UpdateUser`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.UpdateUser`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.users.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.UpdateUser" `  




#### `UpgradeCluster`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBAdmin.UpgradeCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.upgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBAdmin.UpgradeCluster" `  




### `google.cloud.alloydb.v1.AlloyDBCSQLAdmin`

The following audit logs are associated with methods belonging to `google.cloud.alloydb.v1.AlloyDBCSQLAdmin`.

#### `RestoreFromCloudSQL`

  * **Method** : `google.cloud.alloydb.v1.AlloyDBCSQLAdmin.RestoreFromCloudSQL`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1.AlloyDBCSQLAdmin.RestoreFromCloudSQL" `  




### `google.cloud.alloydb.v1alpha.AlloyDBAdmin`

The following audit logs are associated with methods belonging to `google.cloud.alloydb.v1alpha.AlloyDBAdmin`.

#### `BatchCreateInstances`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.BatchCreateInstances`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.BatchCreateInstances" `  




#### `CreateBackup`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.backups.create - ADMIN_WRITE`
    * `alloydb.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateBackup" `  




#### `CreateCluster`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateCluster" `  




#### `CreateDatabase`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateDatabase`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.databases.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateDatabase" `  




#### `CreateInstance`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateInstance" `  




#### `CreateSecondaryCluster`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateSecondaryCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.create - ADMIN_WRITE`
    * `alloydb.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateSecondaryCluster" `  




#### `CreateSecondaryInstance`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateSecondaryInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateSecondaryInstance" `  




#### `CreateUser`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateUser`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.users.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.CreateUser" `  




#### `DeleteBackup`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.DeleteBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.backups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.DeleteBackup" `  




#### `DeleteCluster`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.DeleteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.DeleteCluster" `  




#### `DeleteInstance`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.DeleteInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.DeleteInstance" `  




#### `DeleteUser`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.DeleteUser`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.users.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.DeleteUser" `  




#### `ExecuteSql`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.ExecuteSql`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.instances.executeSql - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.ExecuteSql" `  




#### `ExecuteSqlReadOnly`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.ExecuteSqlReadOnly`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.instances.executeSqlReadOnly - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.ExecuteSqlReadOnly" `  




#### `ExportCluster`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.ExportCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.clusters.export - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.ExportCluster" `  




#### `FailoverInstance`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.FailoverInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.failover - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.FailoverInstance" `  




#### `GenerateClientCertificate`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.GenerateClientCertificate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.generateClientCertificate - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.GenerateClientCertificate" `  




#### `GetBackup`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.GetBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.backups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.GetBackup" `  




#### `GetCluster`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.GetCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.GetCluster" `  




#### `GetInstance`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.GetInstance" `  




#### `GetUser`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.GetUser`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.users.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.GetUser" `  




#### `ImportCluster`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.ImportCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.clusters.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.ImportCluster" `  




#### `InjectFault`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.InjectFault`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.injectFault - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.InjectFault" `  




#### `ListBackups`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.ListBackups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.backups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.ListBackups" `  




#### `ListClusters`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.ListClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.clusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.ListClusters" `  




#### `ListInstances`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.ListInstances" `  




#### `ListUsers`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.ListUsers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.users.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.ListUsers" `  




#### `PromoteCluster`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.PromoteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.promote - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.PromoteCluster" `  




#### `RestartInstance`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.RestartInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.restart - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.RestartInstance" `  




#### `RestoreCluster`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.RestoreCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.backups.get - ADMIN_READ`
    * `alloydb.backups.list - ADMIN_READ`
    * `alloydb.clusters.create - ADMIN_WRITE`
    * `alloydb.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.RestoreCluster" `  




#### `SwitchoverCluster`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.SwitchoverCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.get - ADMIN_READ`
    * `alloydb.clusters.switchover - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.SwitchoverCluster" `  




#### `UpdateBackup`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.UpdateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.backups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.UpdateBackup" `  




#### `UpdateCluster`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.UpdateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.UpdateCluster" `  




#### `UpdateInstance`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.UpdateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.UpdateInstance" `  




#### `UpdateUser`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.UpdateUser`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.users.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.UpdateUser" `  




#### `UpgradeCluster`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBAdmin.UpgradeCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.upgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBAdmin.UpgradeCluster" `  




### `google.cloud.alloydb.v1alpha.AlloyDBCSQLAdmin`

The following audit logs are associated with methods belonging to `google.cloud.alloydb.v1alpha.AlloyDBCSQLAdmin`.

#### `RestoreFromCloudSQL`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBCSQLAdmin.RestoreFromCloudSQL`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBCSQLAdmin.RestoreFromCloudSQL" `  




### `google.cloud.alloydb.v1alpha.AlloyDBEndpointAdmin`

The following audit logs are associated with methods belonging to `google.cloud.alloydb.v1alpha.AlloyDBEndpointAdmin`.

#### `CreateEndpoint`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBEndpointAdmin.CreateEndpoint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.endpoints.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBEndpointAdmin.CreateEndpoint" `  




#### `DeleteEndpoint`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBEndpointAdmin.DeleteEndpoint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.endpoints.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBEndpointAdmin.DeleteEndpoint" `  




#### `GetEndpoint`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBEndpointAdmin.GetEndpoint`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.endpoints.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBEndpointAdmin.GetEndpoint" `  




#### `ListEndpoints`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBEndpointAdmin.ListEndpoints`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.endpoints.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBEndpointAdmin.ListEndpoints" `  




#### `UpdateEndpoint`

  * **Method** : `google.cloud.alloydb.v1alpha.AlloyDBEndpointAdmin.UpdateEndpoint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.endpoints.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1alpha.AlloyDBEndpointAdmin.UpdateEndpoint" `  




### `google.cloud.alloydb.v1beta.AlloyDBAdmin`

The following audit logs are associated with methods belonging to `google.cloud.alloydb.v1beta.AlloyDBAdmin`.

#### `CreateBackup`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.backups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateBackup" `  




#### `CreateCluster`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateCluster" `  




#### `CreateDatabase`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateDatabase`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.databases.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateDatabase" `  




#### `CreateInstance`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateInstance" `  




#### `CreateSecondaryCluster`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateSecondaryCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.create - ADMIN_WRITE`
    * `alloydb.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateSecondaryCluster" `  




#### `CreateSecondaryInstance`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateSecondaryInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateSecondaryInstance" `  




#### `CreateUser`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateUser`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.users.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.CreateUser" `  




#### `DeleteBackup`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.DeleteBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.backups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.DeleteBackup" `  




#### `DeleteCluster`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.DeleteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.DeleteCluster" `  




#### `DeleteInstance`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.DeleteInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.DeleteInstance" `  




#### `DeleteUser`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.DeleteUser`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.users.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.DeleteUser" `  




#### `ExecuteSql`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.ExecuteSql`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.instances.executeSql - DATA_WRITE`
    * `alloydb.users.login - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.ExecuteSql" `  




#### `ExecuteSqlReadOnly`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.ExecuteSqlReadOnly`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.instances.executeSqlReadOnly - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.ExecuteSqlReadOnly" `  




#### `ExportCluster`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.ExportCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.clusters.export - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.ExportCluster" `  




#### `FailoverInstance`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.FailoverInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.failover - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.FailoverInstance" `  




#### `GenerateClientCertificate`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.GenerateClientCertificate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.generateClientCertificate - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.GenerateClientCertificate" `  




#### `GetBackup`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.GetBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.backups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.GetBackup" `  




#### `GetCluster`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.GetCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.GetCluster" `  




#### `GetInstance`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.GetInstance" `  




#### `GetUser`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.GetUser`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.users.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.GetUser" `  




#### `ImportCluster`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.ImportCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.clusters.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.ImportCluster" `  




#### `InjectFault`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.InjectFault`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.injectFault - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.InjectFault" `  




#### `ListBackups`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.ListBackups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.backups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.ListBackups" `  




#### `ListClusters`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.ListClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.clusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.ListClusters" `  




#### `ListDatabases`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.ListDatabases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.databases.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.ListDatabases" `  




#### `ListInstances`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.ListInstances" `  




#### `ListUsers`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.ListUsers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.users.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.ListUsers" `  




#### `PromoteCluster`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.PromoteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.promote - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.PromoteCluster" `  




#### `RestartInstance`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.RestartInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.restart - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.RestartInstance" `  




#### `RestoreCluster`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.RestoreCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.backups.get - ADMIN_READ`
    * `alloydb.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.RestoreCluster" `  




#### `SwitchoverCluster`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.SwitchoverCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.get - ADMIN_READ`
    * `alloydb.clusters.switchover - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.SwitchoverCluster" `  




#### `UpdateBackup`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.UpdateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.backups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.UpdateBackup" `  




#### `UpdateCluster`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.UpdateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.UpdateCluster" `  




#### `UpdateInstance`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.UpdateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.UpdateInstance" `  




#### `UpdateUser`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.UpdateUser`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.users.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.UpdateUser" `  




#### `UpgradeCluster`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBAdmin.UpgradeCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.upgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBAdmin.UpgradeCluster" `  




### `google.cloud.alloydb.v1beta.AlloyDBCSQLAdmin`

The following audit logs are associated with methods belonging to `google.cloud.alloydb.v1beta.AlloyDBCSQLAdmin`.

#### `RestoreFromCloudSQL`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBCSQLAdmin.RestoreFromCloudSQL`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBCSQLAdmin.RestoreFromCloudSQL" `  




### `google.cloud.alloydb.v1beta.AlloyDBEndpointAdmin`

The following audit logs are associated with methods belonging to `google.cloud.alloydb.v1beta.AlloyDBEndpointAdmin`.

#### `CreateEndpoint`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBEndpointAdmin.CreateEndpoint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.endpoints.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBEndpointAdmin.CreateEndpoint" `  




#### `DeleteEndpoint`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBEndpointAdmin.DeleteEndpoint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.endpoints.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBEndpointAdmin.DeleteEndpoint" `  




#### `GetEndpoint`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBEndpointAdmin.GetEndpoint`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.endpoints.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBEndpointAdmin.GetEndpoint" `  




#### `ListEndpoints`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBEndpointAdmin.ListEndpoints`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.endpoints.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBEndpointAdmin.ListEndpoints" `  




#### `UpdateEndpoint`

  * **Method** : `google.cloud.alloydb.v1beta.AlloyDBEndpointAdmin.UpdateEndpoint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.endpoints.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.alloydb.v1beta.AlloyDBEndpointAdmin.UpdateEndpoint" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `alloydb.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `alloydb.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.alloydb.v1.AlloyDBAdmin.ListSupportedDatabaseFlags`
  * `google.cloud.alloydb.v1alpha.AlloyDBAdmin.ListSupportedDatabaseFlags`
  * `google.cloud.alloydb.v1beta.AlloyDBAdmin.ListSupportedDatabaseFlags`
  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.iam.v1.IAMPolicy.GetIamPolicy`
  * `google.iam.v1.IAMPolicy.SetIamPolicy`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
