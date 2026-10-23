---
url: https://docs.cloud.google.com/oracle/database/docs/view-audit-logs/
title: Oracle Database@Google Cloud audit logging \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:56.120986+00:00
---

# Oracle Database@Google Cloud audit logging  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/view-audit-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Oracle Database@Google Cloud audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Oracle Database@Google Cloud. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Oracle Database@Google Cloud audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="oracledatabase.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Oracle Database@Google Cloud generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.oracledatabase.v1.OracleDatabase.GenerateAutonomousDatabaseWallet`  
`google.cloud.oracledatabase.v1.OracleDatabase.GetAutonomousDatabase`  
`google.cloud.oracledatabase.v1.OracleDatabase.GetAutonomousDatabaseRefreshableClones`  
`google.cloud.oracledatabase.v1.OracleDatabase.GetCloudExadataInfrastructure`  
`google.cloud.oracledatabase.v1.OracleDatabase.GetCloudVmCluster`  
`google.cloud.oracledatabase.v1.OracleDatabase.GetDatabase`  
`google.cloud.oracledatabase.v1.OracleDatabase.GetDbSystem`  
`google.cloud.oracledatabase.v1.OracleDatabase.GetExadbVmCluster`  
`google.cloud.oracledatabase.v1.OracleDatabase.GetExascaleDbStorageVault`  
`google.cloud.oracledatabase.v1.OracleDatabase.GetGoldengateConnection`  
`google.cloud.oracledatabase.v1.OracleDatabase.GetGoldengateConnectionAssignment`  
`google.cloud.oracledatabase.v1.OracleDatabase.GetGoldengateDeployment`  
`google.cloud.oracledatabase.v1.OracleDatabase.GetOdbNetwork`  
`google.cloud.oracledatabase.v1.OracleDatabase.GetOdbSubnet`  
`google.cloud.oracledatabase.v1.OracleDatabase.GetPluggableDatabase`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListAutonomousDatabaseBackups`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListAutonomousDatabaseCharacterSets`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListAutonomousDatabases`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListAutonomousDbVersions`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListCloudExadataInfrastructures`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListCloudVmClusters`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListDatabaseCharacterSets`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListDatabases`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListDbNodes`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListDbServers`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListDbSystemInitialStorageSizes`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListDbSystemShapes`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListDbSystems`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListDbVersions`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListEntitlements`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListExadbVmClusters`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListExascaleDbStorageVaults`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListGiVersions`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateConnectionAssignments`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateConnectionTypes`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateConnections`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateDeploymentEnvironments`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateDeploymentTypes`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateDeploymentVersions`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateDeployments`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListMinorVersions`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListOdbNetworks`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListOdbSubnets`  
`google.cloud.oracledatabase.v1.OracleDatabase.ListPluggableDatabases`  
`ADMIN_WRITE` | `google.cloud.oracledatabase.v1.OracleDatabase.ConfigureExascaleCloudExadataInfrastructure` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.CreateAutonomousDatabase` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.CreateCloudExadataInfrastructure` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.CreateCloudVmCluster` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.CreateDbSystem` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.CreateExadbVmCluster` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.CreateExascaleDbStorageVault` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.CreateGoldengateConnection` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.CreateGoldengateConnectionAssignment` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.CreateGoldengateDeployment` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.CreateOdbNetwork` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.CreateOdbSubnet` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.DeleteAutonomousDatabase` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.DeleteCloudExadataInfrastructure` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.DeleteCloudVmCluster` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.DeleteDbSystem` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.DeleteExadbVmCluster` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.DeleteExascaleDbStorageVault` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.DeleteGoldengateConnection` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.DeleteGoldengateConnectionAssignment` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.DeleteGoldengateDeployment` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.DeleteOdbNetwork` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.DeleteOdbSubnet` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.FailoverAutonomousDatabase` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.RefreshAutonomousDatabase` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.RemoveVirtualMachineExadbVmCluster`  
`google.cloud.oracledatabase.v1.OracleDatabase.RestartAutonomousDatabase` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.RestoreAutonomousDatabase` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.StartAutonomousDatabase` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.StartGoldengateDeployment` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.StopAutonomousDatabase` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.StopGoldengateDeployment` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.SwitchoverAutonomousDatabase` (LRO)  
`google.cloud.oracledatabase.v1.OracleDatabase.TestGoldengateConnectionAssignment`  
`google.cloud.oracledatabase.v1.OracleDatabase.UpdateExadbVmCluster` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the [Identity and Access Management documentation](https://docs.cloud.google.com/oracle/database/docs/iam-overview) for Oracle Database@Google Cloud.

### `google.cloud.oracledatabase.v1.OracleDatabase`

The following audit logs are associated with methods belonging to `google.cloud.oracledatabase.v1.OracleDatabase`.

#### `ConfigureExascaleCloudExadataInfrastructure`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ConfigureExascaleCloudExadataInfrastructure`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.cloudExadataInfrastructures.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ConfigureExascaleCloudExadataInfrastructure" `  




#### `CreateAutonomousDatabase`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.CreateAutonomousDatabase`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.autonomousDatabases.create - ADMIN_WRITE`
    * `oracledatabase.odbSubnets.use - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.CreateAutonomousDatabase" `  




#### `CreateCloudExadataInfrastructure`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.CreateCloudExadataInfrastructure`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.cloudExadataInfrastructures.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.CreateCloudExadataInfrastructure" `  




#### `CreateCloudVmCluster`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.CreateCloudVmCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.cloudExadataInfrastructures.use - ADMIN_READ`
    * `oracledatabase.cloudVmClusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.CreateCloudVmCluster" `  




#### `CreateDbSystem`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.CreateDbSystem`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.dbSystems.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.CreateDbSystem" `  




#### `CreateExadbVmCluster`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.CreateExadbVmCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.exadbVmClusters.create - ADMIN_WRITE`
    * `oracledatabase.odbSubnets.use - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.CreateExadbVmCluster" `  




#### `CreateExascaleDbStorageVault`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.CreateExascaleDbStorageVault`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.exascaleDbStorageVaults.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.CreateExascaleDbStorageVault" `  




#### `CreateGoldengateConnection`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.CreateGoldengateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.goldenGateConnections.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.CreateGoldengateConnection" `  




#### `CreateGoldengateConnectionAssignment`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.CreateGoldengateConnectionAssignment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.goldenGateConnectionAssignments.create - ADMIN_WRITE`
    * `oracledatabase.goldenGateConnections.use - ADMIN_READ`
    * `oracledatabase.goldenGateDeployments.use - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.CreateGoldengateConnectionAssignment" `  




#### `CreateGoldengateDeployment`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.CreateGoldengateDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.goldenGateDeployments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.CreateGoldengateDeployment" `  




#### `CreateOdbNetwork`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.CreateOdbNetwork`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.odbNetworks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.CreateOdbNetwork" `  




#### `CreateOdbSubnet`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.CreateOdbSubnet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.odbSubnets.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.CreateOdbSubnet" `  




#### `DeleteAutonomousDatabase`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.DeleteAutonomousDatabase`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.autonomousDatabases.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.DeleteAutonomousDatabase" `  




#### `DeleteCloudExadataInfrastructure`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.DeleteCloudExadataInfrastructure`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.cloudExadataInfrastructures.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.DeleteCloudExadataInfrastructure" `  




#### `DeleteCloudVmCluster`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.DeleteCloudVmCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.cloudVmClusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.DeleteCloudVmCluster" `  




#### `DeleteDbSystem`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.DeleteDbSystem`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.dbSystems.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.DeleteDbSystem" `  




#### `DeleteExadbVmCluster`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.DeleteExadbVmCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.exadbVmClusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.DeleteExadbVmCluster" `  




#### `DeleteExascaleDbStorageVault`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.DeleteExascaleDbStorageVault`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.exascaleDbStorageVaults.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.DeleteExascaleDbStorageVault" `  




#### `DeleteGoldengateConnection`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.DeleteGoldengateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.goldenGateConnections.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.DeleteGoldengateConnection" `  




#### `DeleteGoldengateConnectionAssignment`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.DeleteGoldengateConnectionAssignment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.goldenGateConnectionAssignments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.DeleteGoldengateConnectionAssignment" `  




#### `DeleteGoldengateDeployment`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.DeleteGoldengateDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.goldenGateDeployments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.DeleteGoldengateDeployment" `  




#### `DeleteOdbNetwork`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.DeleteOdbNetwork`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.odbNetworks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.DeleteOdbNetwork" `  




#### `DeleteOdbSubnet`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.DeleteOdbSubnet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.odbSubnets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.DeleteOdbSubnet" `  




#### `FailoverAutonomousDatabase`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.FailoverAutonomousDatabase`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.autonomousDatabases.failover - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.FailoverAutonomousDatabase" `  




#### `GenerateAutonomousDatabaseWallet`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.GenerateAutonomousDatabaseWallet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.autonomousDatabases.generateWallet - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.GenerateAutonomousDatabaseWallet" `  




#### `GetAutonomousDatabase`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.GetAutonomousDatabase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.autonomousDatabases.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.GetAutonomousDatabase" `  




#### `GetAutonomousDatabaseRefreshableClones`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.GetAutonomousDatabaseRefreshableClones`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.autonomousDatabases.listRefreshableClones - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.GetAutonomousDatabaseRefreshableClones" `  




#### `GetCloudExadataInfrastructure`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.GetCloudExadataInfrastructure`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.cloudExadataInfrastructures.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.GetCloudExadataInfrastructure" `  




#### `GetCloudVmCluster`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.GetCloudVmCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.cloudVmClusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.GetCloudVmCluster" `  




#### `GetDatabase`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.GetDatabase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.databases.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.GetDatabase" `  




#### `GetDbSystem`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.GetDbSystem`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.dbSystems.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.GetDbSystem" `  




#### `GetExadbVmCluster`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.GetExadbVmCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.exadbVmClusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.GetExadbVmCluster" `  




#### `GetExascaleDbStorageVault`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.GetExascaleDbStorageVault`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.exascaleDbStorageVaults.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.GetExascaleDbStorageVault" `  




#### `GetGoldengateConnection`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.GetGoldengateConnection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.goldenGateConnections.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.GetGoldengateConnection" `  




#### `GetGoldengateConnectionAssignment`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.GetGoldengateConnectionAssignment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.goldenGateConnectionAssignments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.GetGoldengateConnectionAssignment" `  




#### `GetGoldengateDeployment`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.GetGoldengateDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.goldenGateDeployments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.GetGoldengateDeployment" `  




#### `GetOdbNetwork`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.GetOdbNetwork`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.odbNetworks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.GetOdbNetwork" `  




#### `GetOdbSubnet`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.GetOdbSubnet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.odbSubnets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.GetOdbSubnet" `  




#### `GetPluggableDatabase`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.GetPluggableDatabase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.pluggableDatabases.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.GetPluggableDatabase" `  




#### `ListAutonomousDatabaseBackups`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListAutonomousDatabaseBackups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.autonomousDatabaseBackups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListAutonomousDatabaseBackups" `  




#### `ListAutonomousDatabaseCharacterSets`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListAutonomousDatabaseCharacterSets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.autonomousDatabaseCharacterSets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListAutonomousDatabaseCharacterSets" `  




#### `ListAutonomousDatabases`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListAutonomousDatabases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.autonomousDatabases.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListAutonomousDatabases" `  




#### `ListAutonomousDbVersions`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListAutonomousDbVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.autonomousDbVersions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListAutonomousDbVersions" `  




#### `ListCloudExadataInfrastructures`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListCloudExadataInfrastructures`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.cloudExadataInfrastructures.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListCloudExadataInfrastructures" `  




#### `ListCloudVmClusters`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListCloudVmClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.cloudVmClusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListCloudVmClusters" `  




#### `ListDatabaseCharacterSets`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListDatabaseCharacterSets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.databaseCharacterSets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListDatabaseCharacterSets" `  




#### `ListDatabases`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListDatabases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.databases.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListDatabases" `  




#### `ListDbNodes`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListDbNodes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.dbNodes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListDbNodes" `  




#### `ListDbServers`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListDbServers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.dbServers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListDbServers" `  




#### `ListDbSystemInitialStorageSizes`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListDbSystemInitialStorageSizes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.dbSystemInitialStorageSizes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListDbSystemInitialStorageSizes" `  




#### `ListDbSystemShapes`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListDbSystemShapes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.dbSystemShapes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListDbSystemShapes" `  




#### `ListDbSystems`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListDbSystems`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.dbSystems.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListDbSystems" `  




#### `ListDbVersions`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListDbVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.dbVersions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListDbVersions" `  




#### `ListEntitlements`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListEntitlements`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.entitlements.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListEntitlements" `  




#### `ListExadbVmClusters`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListExadbVmClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.exadbVmClusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListExadbVmClusters" `  




#### `ListExascaleDbStorageVaults`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListExascaleDbStorageVaults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.exascaleDbStorageVaults.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListExascaleDbStorageVaults" `  




#### `ListGiVersions`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListGiVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.giVersions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListGiVersions" `  




#### `ListGoldengateConnectionAssignments`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateConnectionAssignments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.goldenGateConnectionAssignments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateConnectionAssignments" `  




#### `ListGoldengateConnectionTypes`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateConnectionTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.goldenGateConnectionTypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateConnectionTypes" `  




#### `ListGoldengateConnections`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateConnections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.goldenGateConnections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateConnections" `  




#### `ListGoldengateDeploymentEnvironments`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateDeploymentEnvironments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.goldenGateDeploymentEnvironments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateDeploymentEnvironments" `  




#### `ListGoldengateDeploymentTypes`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateDeploymentTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.goldenGateDeploymentTypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateDeploymentTypes" `  




#### `ListGoldengateDeploymentVersions`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateDeploymentVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.goldenGateDeploymentVersions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateDeploymentVersions" `  




#### `ListGoldengateDeployments`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.goldenGateDeployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListGoldengateDeployments" `  




#### `ListMinorVersions`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListMinorVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.minorVersions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListMinorVersions" `  




#### `ListOdbNetworks`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListOdbNetworks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.odbNetworks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListOdbNetworks" `  




#### `ListOdbSubnets`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListOdbSubnets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.odbSubnets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListOdbSubnets" `  




#### `ListPluggableDatabases`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.ListPluggableDatabases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `oracledatabase.pluggableDatabases.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.ListPluggableDatabases" `  




#### `RefreshAutonomousDatabase`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.RefreshAutonomousDatabase`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.autonomousDatabases.refresh - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.RefreshAutonomousDatabase" `  




#### `RemoveVirtualMachineExadbVmCluster`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.RemoveVirtualMachineExadbVmCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.exadbVmClusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.RemoveVirtualMachineExadbVmCluster" `  




#### `RestartAutonomousDatabase`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.RestartAutonomousDatabase`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.autonomousDatabases.restart - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.RestartAutonomousDatabase" `  




#### `RestoreAutonomousDatabase`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.RestoreAutonomousDatabase`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.autonomousDatabases.restore - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.RestoreAutonomousDatabase" `  




#### `StartAutonomousDatabase`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.StartAutonomousDatabase`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.autonomousDatabases.start - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.StartAutonomousDatabase" `  




#### `StartGoldengateDeployment`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.StartGoldengateDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.goldenGateDeployments.start - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.StartGoldengateDeployment" `  




#### `StopAutonomousDatabase`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.StopAutonomousDatabase`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.autonomousDatabases.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.StopAutonomousDatabase" `  




#### `StopGoldengateDeployment`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.StopGoldengateDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.goldenGateDeployments.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.StopGoldengateDeployment" `  




#### `SwitchoverAutonomousDatabase`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.SwitchoverAutonomousDatabase`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.autonomousDatabases.switchover - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.SwitchoverAutonomousDatabase" `  




#### `TestGoldengateConnectionAssignment`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.TestGoldengateConnectionAssignment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.goldenGateConnectionAssignments.test - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.TestGoldengateConnectionAssignment" `  




#### `UpdateExadbVmCluster`

  * **Method** : `google.cloud.oracledatabase.v1.OracleDatabase.UpdateExadbVmCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `oracledatabase.exadbVmClusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.oracledatabase.v1.OracleDatabase.UpdateExadbVmCluster" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.cloud.oracledatabase.v1.OracleDatabase.UpdateAutonomousDatabase`
  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.DeleteOperation`
  * `google.longrunning.Operations.GetOperation`
  * `google.longrunning.Operations.ListOperations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
