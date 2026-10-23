---
url: https://docs.cloud.google.com/database-migration/docs/audit-logging/
title: Database Migration Service audit logging information \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:38.936880+00:00
---

# Database Migration Service audit logging information  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Resources ](https://docs.cloud.google.com/database-migration/docs/release-notes)



Send feedback 

#  Database Migration Service audit logging information Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Database Migration Service. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Database Migration Service audit logs use the service name `datamigration.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="datamigration.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Database Migration Service generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.clouddms.v1.DataMigrationService.DescribeConversionWorkspaceRevisions`  
`google.cloud.clouddms.v1.DataMigrationService.DescribeDatabaseEntities`  
`google.cloud.clouddms.v1.DataMigrationService.FetchSourceObjects` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.FetchStaticIps`  
`google.cloud.clouddms.v1.DataMigrationService.GenerateTcpProxyScript`  
`google.cloud.clouddms.v1.DataMigrationService.GetConnectionProfile`  
`google.cloud.clouddms.v1.DataMigrationService.GetConversionWorkspace`  
`google.cloud.clouddms.v1.DataMigrationService.GetMappingRule`  
`google.cloud.clouddms.v1.DataMigrationService.GetMigrationJob`  
`google.cloud.clouddms.v1.DataMigrationService.GetMigrationJobObject`  
`google.cloud.clouddms.v1.DataMigrationService.GetPrivateConnection`  
`google.cloud.clouddms.v1.DataMigrationService.ListConnectionProfiles`  
`google.cloud.clouddms.v1.DataMigrationService.ListConversionWorkspaces`  
`google.cloud.clouddms.v1.DataMigrationService.ListMappingRules`  
`google.cloud.clouddms.v1.DataMigrationService.ListMigrationJobObjects`  
`google.cloud.clouddms.v1.DataMigrationService.ListMigrationJobs`  
`google.cloud.clouddms.v1.DataMigrationService.ListPrivateConnections`  
`google.cloud.clouddms.v1.DataMigrationService.LookupMigrationJobObject`  
`google.cloud.clouddms.v1.DataMigrationService.SearchBackgroundJobs`  
`google.cloud.clouddms.v1.DataMigrationService.VerifyMigrationJob` (LRO)  
`google.cloud.clouddms.v1alpha2.DataMigrationService.GetConnectionProfile`  
`google.cloud.clouddms.v1alpha2.DataMigrationService.GetMigrationJob`  
`google.cloud.clouddms.v1alpha2.DataMigrationService.ListConnectionProfiles`  
`google.cloud.clouddms.v1alpha2.DataMigrationService.ListMigrationJobs`  
`google.cloud.clouddms.v1alpha2.DataMigrationService.VerifyMigrationJob`  
`google.cloud.clouddms.v1beta1.DataMigrationService.GetConnectionProfile`  
`google.cloud.clouddms.v1beta1.DataMigrationService.GetMigrationJob`  
`google.cloud.clouddms.v1beta1.DataMigrationService.ListConnectionProfiles`  
`google.cloud.clouddms.v1beta1.DataMigrationService.ListMigrationJobs`  
`google.cloud.clouddms.v1beta1.DataMigrationService.VerifyMigrationJob`  
`GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.clouddms.v1.DataMigrationService.ApplyConversionWorkspace` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.CommitConversionWorkspace` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.ConvertConversionWorkspace` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.CreateConnectionProfile` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.CreateConversionWorkspace` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.CreateMappingRule`  
`google.cloud.clouddms.v1.DataMigrationService.CreateMigrationJob` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.CreatePrivateConnection` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.DeleteConnectionProfile` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.DeleteConversionWorkspace` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.DeleteMappingRule`  
`google.cloud.clouddms.v1.DataMigrationService.DeleteMigrationJob` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.DeletePrivateConnection` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.DemoteDestination` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.GenerateSshScript`  
`google.cloud.clouddms.v1.DataMigrationService.ImportMappingRules`  
`google.cloud.clouddms.v1.DataMigrationService.PromoteMigrationJob` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.RestartMigrationJob` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.ResumeMigrationJob` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.RollbackConversionWorkspace` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.SeedConversionWorkspace` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.StartMigrationJob` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.StopMigrationJob` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.UpdateConnectionProfile` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.UpdateConversionWorkspace` (LRO)  
`google.cloud.clouddms.v1.DataMigrationService.UpdateMigrationJob` (LRO)  
`google.cloud.clouddms.v1alpha2.DataMigrationService.CreateConnectionProfile` (LRO)  
`google.cloud.clouddms.v1alpha2.DataMigrationService.CreateMigrationJob` (LRO)  
`google.cloud.clouddms.v1alpha2.DataMigrationService.DeleteConnectionProfile` (LRO)  
`google.cloud.clouddms.v1alpha2.DataMigrationService.DeleteMigrationJob` (LRO)  
`google.cloud.clouddms.v1alpha2.DataMigrationService.GenerateSshScript`  
`google.cloud.clouddms.v1alpha2.DataMigrationService.PromoteMigrationJob`  
`google.cloud.clouddms.v1alpha2.DataMigrationService.RestartMigrationJob`  
`google.cloud.clouddms.v1alpha2.DataMigrationService.ResumeMigrationJob`  
`google.cloud.clouddms.v1alpha2.DataMigrationService.StartMigrationJob`  
`google.cloud.clouddms.v1alpha2.DataMigrationService.StopMigrationJob`  
`google.cloud.clouddms.v1alpha2.DataMigrationService.UpdateConnectionProfile` (LRO)  
`google.cloud.clouddms.v1alpha2.DataMigrationService.UpdateMigrationJob` (LRO)  
`google.cloud.clouddms.v1beta1.DataMigrationService.CreateConnectionProfile` (LRO)  
`google.cloud.clouddms.v1beta1.DataMigrationService.CreateMigrationJob` (LRO)  
`google.cloud.clouddms.v1beta1.DataMigrationService.DeleteConnectionProfile` (LRO)  
`google.cloud.clouddms.v1beta1.DataMigrationService.DeleteMigrationJob` (LRO)  
`google.cloud.clouddms.v1beta1.DataMigrationService.GenerateSshScript`  
`google.cloud.clouddms.v1beta1.DataMigrationService.PromoteMigrationJob`  
`google.cloud.clouddms.v1beta1.DataMigrationService.RestartMigrationJob`  
`google.cloud.clouddms.v1beta1.DataMigrationService.ResumeMigrationJob`  
`google.cloud.clouddms.v1beta1.DataMigrationService.StartMigrationJob`  
`google.cloud.clouddms.v1beta1.DataMigrationService.StopMigrationJob`  
`google.cloud.clouddms.v1beta1.DataMigrationService.UpdateConnectionProfile` (LRO)  
`google.cloud.clouddms.v1beta1.DataMigrationService.UpdateMigrationJob` (LRO)  
`SetIamPolicy`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Database Migration Service.

### `google.cloud.clouddms.v1.DataMigrationService`

The following audit logs are associated with methods belonging to `google.cloud.clouddms.v1.DataMigrationService`.

#### `ApplyConversionWorkspace`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.ApplyConversionWorkspace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.conversionworkspaces.apply - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.ApplyConversionWorkspace" `  




#### `CommitConversionWorkspace`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.CommitConversionWorkspace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.conversionworkspaces.commit - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.CommitConversionWorkspace" `  




#### `ConvertConversionWorkspace`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.ConvertConversionWorkspace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.conversionworkspaces.convert - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.ConvertConversionWorkspace" `  




#### `CreateConnectionProfile`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.CreateConnectionProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.connectionprofiles.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.CreateConnectionProfile" `  




#### `CreateConversionWorkspace`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.CreateConversionWorkspace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.conversionworkspaces.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.CreateConversionWorkspace" `  




#### `CreateMappingRule`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.CreateMappingRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.conversionworkspaces.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.CreateMappingRule" `  




#### `CreateMigrationJob`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.CreateMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.CreateMigrationJob" `  




#### `CreatePrivateConnection`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.CreatePrivateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.privateconnections.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.CreatePrivateConnection" `  




#### `DeleteConnectionProfile`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.DeleteConnectionProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.connectionprofiles.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.DeleteConnectionProfile" `  




#### `DeleteConversionWorkspace`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.DeleteConversionWorkspace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.conversionworkspaces.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.DeleteConversionWorkspace" `  




#### `DeleteMappingRule`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.DeleteMappingRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.conversionworkspaces.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.DeleteMappingRule" `  




#### `DeleteMigrationJob`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.DeleteMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.DeleteMigrationJob" `  




#### `DeletePrivateConnection`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.DeletePrivateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.privateconnections.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.DeletePrivateConnection" `  




#### `DemoteDestination`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.DemoteDestination`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.demoteDestination - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.DemoteDestination" `  




#### `DescribeConversionWorkspaceRevisions`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.DescribeConversionWorkspaceRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.conversionworkspaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.DescribeConversionWorkspaceRevisions" `  




#### `DescribeDatabaseEntities`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.DescribeDatabaseEntities`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.conversionworkspaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.DescribeDatabaseEntities" `  




#### `FetchSourceObjects`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.FetchSourceObjects`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.migrationjobs.fetchSourceObjects - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.FetchSourceObjects" `  




#### `FetchStaticIps`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.FetchStaticIps`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.locations.fetchStaticIps - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.FetchStaticIps" `  




#### `GenerateSshScript`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.GenerateSshScript`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.generateSshScript - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.GenerateSshScript" `  




#### `GenerateTcpProxyScript`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.GenerateTcpProxyScript`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.migrationjobs.generateTcpProxyScript - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.GenerateTcpProxyScript" `  




#### `GetConnectionProfile`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.GetConnectionProfile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.connectionprofiles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.GetConnectionProfile" `  




#### `GetConversionWorkspace`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.GetConversionWorkspace`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.conversionworkspaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.GetConversionWorkspace" `  




#### `GetMappingRule`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.GetMappingRule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.conversionworkspaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.GetMappingRule" `  




#### `GetMigrationJob`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.GetMigrationJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.migrationjobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.GetMigrationJob" `  




#### `GetMigrationJobObject`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.GetMigrationJobObject`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.objects.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.GetMigrationJobObject" `  




#### `GetPrivateConnection`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.GetPrivateConnection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.privateconnections.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.GetPrivateConnection" `  




#### `ImportMappingRules`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.ImportMappingRules`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.conversionworkspaces.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.ImportMappingRules" `  




#### `ListConnectionProfiles`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.ListConnectionProfiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.connectionprofiles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.ListConnectionProfiles" `  




#### `ListConversionWorkspaces`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.ListConversionWorkspaces`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.conversionworkspaces.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.ListConversionWorkspaces" `  




#### `ListMappingRules`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.ListMappingRules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.conversionworkspaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.ListMappingRules" `  




#### `ListMigrationJobObjects`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.ListMigrationJobObjects`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.objects.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.ListMigrationJobObjects" `  




#### `ListMigrationJobs`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.ListMigrationJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.migrationjobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.ListMigrationJobs" `  




#### `ListPrivateConnections`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.ListPrivateConnections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.privateconnections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.ListPrivateConnections" `  




#### `LookupMigrationJobObject`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.LookupMigrationJobObject`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.objects.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.LookupMigrationJobObject" `  




#### `PromoteMigrationJob`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.PromoteMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.promote - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.PromoteMigrationJob" `  




#### `RestartMigrationJob`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.RestartMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.restart - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.RestartMigrationJob" `  




#### `ResumeMigrationJob`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.ResumeMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.resume - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.ResumeMigrationJob" `  




#### `RollbackConversionWorkspace`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.RollbackConversionWorkspace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.conversionworkspaces.rollback - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.RollbackConversionWorkspace" `  




#### `SearchBackgroundJobs`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.SearchBackgroundJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.conversionworkspaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.SearchBackgroundJobs" `  




#### `SeedConversionWorkspace`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.SeedConversionWorkspace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.conversionworkspaces.seed - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.SeedConversionWorkspace" `  




#### `StartMigrationJob`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.StartMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.start - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.StartMigrationJob" `  




#### `StopMigrationJob`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.StopMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.StopMigrationJob" `  




#### `UpdateConnectionProfile`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.UpdateConnectionProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.connectionprofiles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.UpdateConnectionProfile" `  




#### `UpdateConversionWorkspace`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.UpdateConversionWorkspace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.conversionworkspaces.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.UpdateConversionWorkspace" `  




#### `UpdateMigrationJob`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.UpdateMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.UpdateMigrationJob" `  




#### `VerifyMigrationJob`

  * **Method** : `google.cloud.clouddms.v1.DataMigrationService.VerifyMigrationJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.migrationjobs.verify - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1.DataMigrationService.VerifyMigrationJob" `  




### `google.cloud.clouddms.v1alpha2.DataMigrationService`

The following audit logs are associated with methods belonging to `google.cloud.clouddms.v1alpha2.DataMigrationService`.

#### `CreateConnectionProfile`

  * **Method** : `google.cloud.clouddms.v1alpha2.DataMigrationService.CreateConnectionProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.connectionprofiles.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1alpha2.DataMigrationService.CreateConnectionProfile" `  




#### `CreateMigrationJob`

  * **Method** : `google.cloud.clouddms.v1alpha2.DataMigrationService.CreateMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1alpha2.DataMigrationService.CreateMigrationJob" `  




#### `DeleteConnectionProfile`

  * **Method** : `google.cloud.clouddms.v1alpha2.DataMigrationService.DeleteConnectionProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.connectionprofiles.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1alpha2.DataMigrationService.DeleteConnectionProfile" `  




#### `DeleteMigrationJob`

  * **Method** : `google.cloud.clouddms.v1alpha2.DataMigrationService.DeleteMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1alpha2.DataMigrationService.DeleteMigrationJob" `  




#### `GenerateSshScript`

  * **Method** : `google.cloud.clouddms.v1alpha2.DataMigrationService.GenerateSshScript`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.generateSshScript - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1alpha2.DataMigrationService.GenerateSshScript" `  




#### `GetConnectionProfile`

  * **Method** : `google.cloud.clouddms.v1alpha2.DataMigrationService.GetConnectionProfile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.connectionprofiles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1alpha2.DataMigrationService.GetConnectionProfile" `  




#### `GetMigrationJob`

  * **Method** : `google.cloud.clouddms.v1alpha2.DataMigrationService.GetMigrationJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.migrationjobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1alpha2.DataMigrationService.GetMigrationJob" `  




#### `ListConnectionProfiles`

  * **Method** : `google.cloud.clouddms.v1alpha2.DataMigrationService.ListConnectionProfiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.connectionprofiles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1alpha2.DataMigrationService.ListConnectionProfiles" `  




#### `ListMigrationJobs`

  * **Method** : `google.cloud.clouddms.v1alpha2.DataMigrationService.ListMigrationJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.migrationjobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1alpha2.DataMigrationService.ListMigrationJobs" `  




#### `PromoteMigrationJob`

  * **Method** : `google.cloud.clouddms.v1alpha2.DataMigrationService.PromoteMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.promote - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1alpha2.DataMigrationService.PromoteMigrationJob" `  




#### `RestartMigrationJob`

  * **Method** : `google.cloud.clouddms.v1alpha2.DataMigrationService.RestartMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.restart - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1alpha2.DataMigrationService.RestartMigrationJob" `  




#### `ResumeMigrationJob`

  * **Method** : `google.cloud.clouddms.v1alpha2.DataMigrationService.ResumeMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.resume - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1alpha2.DataMigrationService.ResumeMigrationJob" `  




#### `StartMigrationJob`

  * **Method** : `google.cloud.clouddms.v1alpha2.DataMigrationService.StartMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.start - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1alpha2.DataMigrationService.StartMigrationJob" `  




#### `StopMigrationJob`

  * **Method** : `google.cloud.clouddms.v1alpha2.DataMigrationService.StopMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1alpha2.DataMigrationService.StopMigrationJob" `  




#### `UpdateConnectionProfile`

  * **Method** : `google.cloud.clouddms.v1alpha2.DataMigrationService.UpdateConnectionProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.connectionprofiles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1alpha2.DataMigrationService.UpdateConnectionProfile" `  




#### `UpdateMigrationJob`

  * **Method** : `google.cloud.clouddms.v1alpha2.DataMigrationService.UpdateMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1alpha2.DataMigrationService.UpdateMigrationJob" `  




#### `VerifyMigrationJob`

  * **Method** : `google.cloud.clouddms.v1alpha2.DataMigrationService.VerifyMigrationJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.migrationjobs.verify - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1alpha2.DataMigrationService.VerifyMigrationJob" `  




### `google.cloud.clouddms.v1beta1.DataMigrationService`

The following audit logs are associated with methods belonging to `google.cloud.clouddms.v1beta1.DataMigrationService`.

#### `CreateConnectionProfile`

  * **Method** : `google.cloud.clouddms.v1beta1.DataMigrationService.CreateConnectionProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.connectionprofiles.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1beta1.DataMigrationService.CreateConnectionProfile" `  




#### `CreateMigrationJob`

  * **Method** : `google.cloud.clouddms.v1beta1.DataMigrationService.CreateMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1beta1.DataMigrationService.CreateMigrationJob" `  




#### `DeleteConnectionProfile`

  * **Method** : `google.cloud.clouddms.v1beta1.DataMigrationService.DeleteConnectionProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.connectionprofiles.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1beta1.DataMigrationService.DeleteConnectionProfile" `  




#### `DeleteMigrationJob`

  * **Method** : `google.cloud.clouddms.v1beta1.DataMigrationService.DeleteMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1beta1.DataMigrationService.DeleteMigrationJob" `  




#### `GenerateSshScript`

  * **Method** : `google.cloud.clouddms.v1beta1.DataMigrationService.GenerateSshScript`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.generateSshScript - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1beta1.DataMigrationService.GenerateSshScript" `  




#### `GetConnectionProfile`

  * **Method** : `google.cloud.clouddms.v1beta1.DataMigrationService.GetConnectionProfile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.connectionprofiles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1beta1.DataMigrationService.GetConnectionProfile" `  




#### `GetMigrationJob`

  * **Method** : `google.cloud.clouddms.v1beta1.DataMigrationService.GetMigrationJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.migrationjobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1beta1.DataMigrationService.GetMigrationJob" `  




#### `ListConnectionProfiles`

  * **Method** : `google.cloud.clouddms.v1beta1.DataMigrationService.ListConnectionProfiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.connectionprofiles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1beta1.DataMigrationService.ListConnectionProfiles" `  




#### `ListMigrationJobs`

  * **Method** : `google.cloud.clouddms.v1beta1.DataMigrationService.ListMigrationJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.migrationjobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1beta1.DataMigrationService.ListMigrationJobs" `  




#### `PromoteMigrationJob`

  * **Method** : `google.cloud.clouddms.v1beta1.DataMigrationService.PromoteMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.promote - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1beta1.DataMigrationService.PromoteMigrationJob" `  




#### `RestartMigrationJob`

  * **Method** : `google.cloud.clouddms.v1beta1.DataMigrationService.RestartMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.restart - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1beta1.DataMigrationService.RestartMigrationJob" `  




#### `ResumeMigrationJob`

  * **Method** : `google.cloud.clouddms.v1beta1.DataMigrationService.ResumeMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.resume - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1beta1.DataMigrationService.ResumeMigrationJob" `  




#### `StartMigrationJob`

  * **Method** : `google.cloud.clouddms.v1beta1.DataMigrationService.StartMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.start - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1beta1.DataMigrationService.StartMigrationJob" `  




#### `StopMigrationJob`

  * **Method** : `google.cloud.clouddms.v1beta1.DataMigrationService.StopMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1beta1.DataMigrationService.StopMigrationJob" `  




#### `UpdateConnectionProfile`

  * **Method** : `google.cloud.clouddms.v1beta1.DataMigrationService.UpdateConnectionProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.connectionprofiles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1beta1.DataMigrationService.UpdateConnectionProfile" `  




#### `UpdateMigrationJob`

  * **Method** : `google.cloud.clouddms.v1beta1.DataMigrationService.UpdateMigrationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.migrationjobs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1beta1.DataMigrationService.UpdateMigrationJob" `  




#### `VerifyMigrationJob`

  * **Method** : `google.cloud.clouddms.v1beta1.DataMigrationService.VerifyMigrationJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.migrationjobs.verify - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.clouddms.v1beta1.DataMigrationService.VerifyMigrationJob" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.connectionprofiles.getIamPolicy - ADMIN_READ`
    * `datamigration.migrationjobs.getIamPolicy - ADMIN_READ`
    * `datamigration.privateconnections.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.connectionprofiles.setIamPolicy - ADMIN_WRITE`
    * `datamigration.conversionworkspaces.setIamPolicy - ADMIN_WRITE`
    * `datamigration.migrationjobs.setIamPolicy - ADMIN_WRITE`
    * `datamigration.privateconnections.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datamigration.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datamigration.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.clouddms.v1.DataMigrationService.FetchSourceObjects`
  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
