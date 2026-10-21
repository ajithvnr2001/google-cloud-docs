---
url: https://docs.cloud.google.com/dataproc-metastore/docs/audit-logging/
title: Dataproc Metastore audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:00.392972+00:00
---

# Dataproc Metastore audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Dataproc Metastore audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Dataproc Metastore. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Dataproc Metastore audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="metastore.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Dataproc Metastore generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.metastore.v1.DataprocMetastore.GetBackup`  
`google.cloud.metastore.v1.DataprocMetastore.GetMetadataImport`  
`google.cloud.metastore.v1.DataprocMetastore.GetService`  
`google.cloud.metastore.v1.DataprocMetastore.ListBackups`  
`google.cloud.metastore.v1.DataprocMetastore.ListMetadataImports`  
`google.cloud.metastore.v1.DataprocMetastore.ListServices`  
`google.cloud.metastore.v1.DataprocMetastoreFederation.GetFederation`  
`google.cloud.metastore.v1.DataprocMetastoreFederation.ListFederations`  
`google.cloud.metastore.v1alpha.DataprocMetastore.GetBackup`  
`google.cloud.metastore.v1alpha.DataprocMetastore.GetMetadataImport`  
`google.cloud.metastore.v1alpha.DataprocMetastore.GetService`  
`google.cloud.metastore.v1alpha.DataprocMetastore.ListBackups`  
`google.cloud.metastore.v1alpha.DataprocMetastore.ListMetadataImports`  
`google.cloud.metastore.v1alpha.DataprocMetastore.ListServices`  
`google.cloud.metastore.v1alpha.DataprocMetastoreFederation.GetFederation`  
`google.cloud.metastore.v1alpha.DataprocMetastoreFederation.ListFederations`  
`google.cloud.metastore.v1beta.DataprocMetastore.GetBackup`  
`google.cloud.metastore.v1beta.DataprocMetastore.GetMetadataImport`  
`google.cloud.metastore.v1beta.DataprocMetastore.GetService`  
`google.cloud.metastore.v1beta.DataprocMetastore.ListBackups`  
`google.cloud.metastore.v1beta.DataprocMetastore.ListMetadataImports`  
`google.cloud.metastore.v1beta.DataprocMetastore.ListServices`  
`google.cloud.metastore.v1beta.DataprocMetastoreFederation.GetFederation`  
`google.cloud.metastore.v1beta.DataprocMetastoreFederation.ListFederations`  
`GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.metastore.v1.DataprocMetastore.CreateBackup` (LRO)  
`google.cloud.metastore.v1.DataprocMetastore.CreateService` (LRO)  
`google.cloud.metastore.v1.DataprocMetastore.DeleteBackup` (LRO)  
`google.cloud.metastore.v1.DataprocMetastore.DeleteService` (LRO)  
`google.cloud.metastore.v1.DataprocMetastore.UpdateMetadataImport` (LRO)  
`google.cloud.metastore.v1.DataprocMetastore.UpdateService` (LRO)  
`google.cloud.metastore.v1.DataprocMetastoreFederation.CreateFederation` (LRO)  
`google.cloud.metastore.v1.DataprocMetastoreFederation.DeleteFederation` (LRO)  
`google.cloud.metastore.v1.DataprocMetastoreFederation.UpdateFederation` (LRO)  
`google.cloud.metastore.v1alpha.DataprocMetastore.CreateBackup` (LRO)  
`google.cloud.metastore.v1alpha.DataprocMetastore.CreateService` (LRO)  
`google.cloud.metastore.v1alpha.DataprocMetastore.DeleteBackup` (LRO)  
`google.cloud.metastore.v1alpha.DataprocMetastore.DeleteService` (LRO)  
`google.cloud.metastore.v1alpha.DataprocMetastore.RemoveIamPolicy`  
`google.cloud.metastore.v1alpha.DataprocMetastore.UpdateMetadataImport` (LRO)  
`google.cloud.metastore.v1alpha.DataprocMetastore.UpdateService` (LRO)  
`google.cloud.metastore.v1alpha.DataprocMetastoreFederation.CreateFederation` (LRO)  
`google.cloud.metastore.v1alpha.DataprocMetastoreFederation.DeleteFederation` (LRO)  
`google.cloud.metastore.v1alpha.DataprocMetastoreFederation.UpdateFederation` (LRO)  
`google.cloud.metastore.v1beta.DataprocMetastore.CreateBackup` (LRO)  
`google.cloud.metastore.v1beta.DataprocMetastore.CreateService` (LRO)  
`google.cloud.metastore.v1beta.DataprocMetastore.DeleteBackup` (LRO)  
`google.cloud.metastore.v1beta.DataprocMetastore.DeleteService` (LRO)  
`google.cloud.metastore.v1beta.DataprocMetastore.RemoveIamPolicy`  
`google.cloud.metastore.v1beta.DataprocMetastore.UpdateMetadataImport` (LRO)  
`google.cloud.metastore.v1beta.DataprocMetastore.UpdateService` (LRO)  
`google.cloud.metastore.v1beta.DataprocMetastoreFederation.CreateFederation` (LRO)  
`google.cloud.metastore.v1beta.DataprocMetastoreFederation.DeleteFederation` (LRO)  
`google.cloud.metastore.v1beta.DataprocMetastoreFederation.UpdateFederation` (LRO)  
`SetIamPolicy`  
`google.longrunning.Operations.DeleteOperation`  
`DATA_READ` | `google.cloud.metastore.v1.DataprocMetastore.ExportMetadata` (LRO)  
`google.cloud.metastore.v1.DataprocMetastore.QueryMetadata` (LRO)  
`google.cloud.metastore.v1alpha.DataprocMetastore.ExportMetadata` (LRO)  
`google.cloud.metastore.v1alpha.DataprocMetastore.QueryMetadata` (LRO)  
`google.cloud.metastore.v1alpha.DataprocMetastore.RestoreService` (LRO)  
`google.cloud.metastore.v1beta.DataprocMetastore.ExportMetadata` (LRO)  
`google.cloud.metastore.v1beta.DataprocMetastore.QueryMetadata` (LRO)  
`google.cloud.metastore.v1beta.DataprocMetastore.RestoreService` (LRO)  
`DATA_WRITE` | `google.cloud.metastore.v1.DataprocMetastore.AlterMetadataResourceLocation` (LRO)  
`google.cloud.metastore.v1.DataprocMetastore.AlterTableProperties` (LRO)  
`google.cloud.metastore.v1.DataprocMetastore.CreateMetadataImport` (LRO)  
`google.cloud.metastore.v1.DataprocMetastore.MoveTableToDatabase` (LRO)  
`google.cloud.metastore.v1.DataprocMetastore.RestoreService` (LRO)  
`google.cloud.metastore.v1alpha.DataprocMetastore.AlterMetadataResourceLocation` (LRO)  
`google.cloud.metastore.v1alpha.DataprocMetastore.AlterTableProperties` (LRO)  
`google.cloud.metastore.v1alpha.DataprocMetastore.CreateMetadataImport` (LRO)  
`google.cloud.metastore.v1alpha.DataprocMetastore.MoveTableToDatabase` (LRO)  
`google.cloud.metastore.v1alpha.DataprocMetastore.RestoreService` (LRO)  
`google.cloud.metastore.v1beta.DataprocMetastore.AlterMetadataResourceLocation` (LRO)  
`google.cloud.metastore.v1beta.DataprocMetastore.AlterTableProperties` (LRO)  
`google.cloud.metastore.v1beta.DataprocMetastore.CreateMetadataImport` (LRO)  
`google.cloud.metastore.v1beta.DataprocMetastore.MoveTableToDatabase` (LRO)  
`google.cloud.metastore.v1beta.DataprocMetastore.RestoreService` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Dataproc Metastore.

### `google.cloud.metastore.v1.DataprocMetastore`

The following audit logs are associated with methods belonging to `google.cloud.metastore.v1.DataprocMetastore`.

#### `AlterMetadataResourceLocation`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastore.AlterMetadataResourceLocation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.mutateMetadata - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastore.AlterMetadataResourceLocation" `  




#### `AlterTableProperties`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastore.AlterTableProperties`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.mutateMetadata - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastore.AlterTableProperties" `  




#### `CreateBackup`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastore.CreateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.backups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastore.CreateBackup" `  




#### `CreateMetadataImport`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastore.CreateMetadataImport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.imports.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastore.CreateMetadataImport" `  




#### `CreateService`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastore.CreateService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.services.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastore.CreateService" `  




#### `DeleteBackup`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastore.DeleteBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.backups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastore.DeleteBackup" `  




#### `DeleteService`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastore.DeleteService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.services.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastore.DeleteService" `  




#### `ExportMetadata`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastore.ExportMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.export - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastore.ExportMetadata" `  




#### `GetBackup`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastore.GetBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.backups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastore.GetBackup" `  




#### `GetMetadataImport`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastore.GetMetadataImport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.imports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastore.GetMetadataImport" `  




#### `GetService`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastore.GetService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastore.GetService" `  




#### `ListBackups`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastore.ListBackups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.backups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastore.ListBackups" `  




#### `ListMetadataImports`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastore.ListMetadataImports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.imports.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastore.ListMetadataImports" `  




#### `ListServices`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastore.ListServices`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastore.ListServices" `  




#### `MoveTableToDatabase`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastore.MoveTableToDatabase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.mutateMetadata - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastore.MoveTableToDatabase" `  




#### `QueryMetadata`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastore.QueryMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.queryMetadata - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastore.QueryMetadata" `  




#### `RestoreService`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastore.RestoreService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.backups.use - DATA_READ`
    * `metastore.services.restore - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastore.RestoreService" `  




#### `UpdateMetadataImport`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastore.UpdateMetadataImport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.imports.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastore.UpdateMetadataImport" `  




#### `UpdateService`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastore.UpdateService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.services.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastore.UpdateService" `  




### `google.cloud.metastore.v1.DataprocMetastoreFederation`

The following audit logs are associated with methods belonging to `google.cloud.metastore.v1.DataprocMetastoreFederation`.

#### `CreateFederation`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastoreFederation.CreateFederation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.federations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastoreFederation.CreateFederation" `  




#### `DeleteFederation`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastoreFederation.DeleteFederation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.federations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastoreFederation.DeleteFederation" `  




#### `GetFederation`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastoreFederation.GetFederation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.federations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastoreFederation.GetFederation" `  




#### `ListFederations`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastoreFederation.ListFederations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.federations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastoreFederation.ListFederations" `  




#### `UpdateFederation`

  * **Method** : `google.cloud.metastore.v1.DataprocMetastoreFederation.UpdateFederation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.federations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1.DataprocMetastoreFederation.UpdateFederation" `  




### `google.cloud.metastore.v1alpha.DataprocMetastore`

The following audit logs are associated with methods belonging to `google.cloud.metastore.v1alpha.DataprocMetastore`.

#### `AlterMetadataResourceLocation`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastore.AlterMetadataResourceLocation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.mutateMetadata - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastore.AlterMetadataResourceLocation" `  




#### `AlterTableProperties`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastore.AlterTableProperties`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.mutateMetadata - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastore.AlterTableProperties" `  




#### `CreateBackup`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastore.CreateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.backups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastore.CreateBackup" `  




#### `CreateMetadataImport`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastore.CreateMetadataImport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.imports.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastore.CreateMetadataImport" `  




#### `CreateService`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastore.CreateService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.services.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastore.CreateService" `  




#### `DeleteBackup`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastore.DeleteBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.backups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastore.DeleteBackup" `  




#### `DeleteService`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastore.DeleteService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.services.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastore.DeleteService" `  




#### `ExportMetadata`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastore.ExportMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.export - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastore.ExportMetadata" `  




#### `GetBackup`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastore.GetBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.backups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastore.GetBackup" `  




#### `GetMetadataImport`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastore.GetMetadataImport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.imports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastore.GetMetadataImport" `  




#### `GetService`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastore.GetService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastore.GetService" `  




#### `ListBackups`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastore.ListBackups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.backups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastore.ListBackups" `  




#### `ListMetadataImports`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastore.ListMetadataImports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.imports.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastore.ListMetadataImports" `  




#### `ListServices`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastore.ListServices`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastore.ListServices" `  




#### `MoveTableToDatabase`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastore.MoveTableToDatabase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.mutateMetadata - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastore.MoveTableToDatabase" `  




#### `QueryMetadata`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastore.QueryMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.queryMetadata - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastore.QueryMetadata" `  




#### `RemoveIamPolicy`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastore.RemoveIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.databases.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastore.RemoveIamPolicy" `  




#### `RestoreService`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastore.RestoreService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.backups.use - DATA_READ`
    * `metastore.services.restore - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastore.RestoreService" `  




#### `UpdateMetadataImport`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastore.UpdateMetadataImport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.imports.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastore.UpdateMetadataImport" `  




#### `UpdateService`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastore.UpdateService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.services.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastore.UpdateService" `  




### `google.cloud.metastore.v1alpha.DataprocMetastoreFederation`

The following audit logs are associated with methods belonging to `google.cloud.metastore.v1alpha.DataprocMetastoreFederation`.

#### `CreateFederation`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastoreFederation.CreateFederation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.federations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastoreFederation.CreateFederation" `  




#### `DeleteFederation`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastoreFederation.DeleteFederation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.federations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastoreFederation.DeleteFederation" `  




#### `GetFederation`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastoreFederation.GetFederation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.federations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastoreFederation.GetFederation" `  




#### `ListFederations`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastoreFederation.ListFederations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.federations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastoreFederation.ListFederations" `  




#### `UpdateFederation`

  * **Method** : `google.cloud.metastore.v1alpha.DataprocMetastoreFederation.UpdateFederation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.federations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1alpha.DataprocMetastoreFederation.UpdateFederation" `  




### `google.cloud.metastore.v1beta.DataprocMetastore`

The following audit logs are associated with methods belonging to `google.cloud.metastore.v1beta.DataprocMetastore`.

#### `AlterMetadataResourceLocation`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastore.AlterMetadataResourceLocation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.mutateMetadata - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastore.AlterMetadataResourceLocation" `  




#### `AlterTableProperties`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastore.AlterTableProperties`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.mutateMetadata - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastore.AlterTableProperties" `  




#### `CreateBackup`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastore.CreateBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.backups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastore.CreateBackup" `  




#### `CreateMetadataImport`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastore.CreateMetadataImport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.imports.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastore.CreateMetadataImport" `  




#### `CreateService`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastore.CreateService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.services.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastore.CreateService" `  




#### `DeleteBackup`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastore.DeleteBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.backups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastore.DeleteBackup" `  




#### `DeleteService`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastore.DeleteService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.services.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastore.DeleteService" `  




#### `ExportMetadata`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastore.ExportMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.export - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastore.ExportMetadata" `  




#### `GetBackup`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastore.GetBackup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.backups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastore.GetBackup" `  




#### `GetMetadataImport`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastore.GetMetadataImport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.imports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastore.GetMetadataImport" `  




#### `GetService`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastore.GetService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastore.GetService" `  




#### `ListBackups`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastore.ListBackups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.backups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastore.ListBackups" `  




#### `ListMetadataImports`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastore.ListMetadataImports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.imports.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastore.ListMetadataImports" `  




#### `ListServices`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastore.ListServices`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastore.ListServices" `  




#### `MoveTableToDatabase`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastore.MoveTableToDatabase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.mutateMetadata - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastore.MoveTableToDatabase" `  




#### `QueryMetadata`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastore.QueryMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.services.queryMetadata - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastore.QueryMetadata" `  




#### `RemoveIamPolicy`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastore.RemoveIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.databases.setIamPolicy - ADMIN_WRITE`
    * `metastore.tables.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastore.RemoveIamPolicy" `  




#### `RestoreService`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastore.RestoreService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.backups.use - DATA_READ`
    * `metastore.services.restore - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastore.RestoreService" `  




#### `UpdateMetadataImport`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastore.UpdateMetadataImport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.imports.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastore.UpdateMetadataImport" `  




#### `UpdateService`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastore.UpdateService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.services.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastore.UpdateService" `  




### `google.cloud.metastore.v1beta.DataprocMetastoreFederation`

The following audit logs are associated with methods belonging to `google.cloud.metastore.v1beta.DataprocMetastoreFederation`.

#### `CreateFederation`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastoreFederation.CreateFederation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.federations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastoreFederation.CreateFederation" `  




#### `DeleteFederation`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastoreFederation.DeleteFederation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.federations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastoreFederation.DeleteFederation" `  




#### `GetFederation`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastoreFederation.GetFederation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.federations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastoreFederation.GetFederation" `  




#### `ListFederations`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastoreFederation.ListFederations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.federations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastoreFederation.ListFederations" `  




#### `UpdateFederation`

  * **Method** : `google.cloud.metastore.v1beta.DataprocMetastoreFederation.UpdateFederation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.federations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.metastore.v1beta.DataprocMetastoreFederation.UpdateFederation" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.federations.getIamPolicy - ADMIN_READ`
    * `metastore.services.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.backups.setIamPolicy - ADMIN_WRITE`
    * `metastore.databases.setIamPolicy - ADMIN_WRITE`
    * `metastore.federations.setIamPolicy - ADMIN_WRITE`
    * `metastore.services.setIamPolicy - ADMIN_WRITE`
    * `metastore.tables.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `metastore.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `metastore.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
