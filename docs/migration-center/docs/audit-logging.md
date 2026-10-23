---
url: https://docs.cloud.google.com/migration-center/docs/audit-logging/
title: Google Cloud Migration Center audit logging information \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:03.866800+00:00
---

# Google Cloud Migration Center audit logging information  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Google Cloud Migration Center audit logging information Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Google Cloud Migration Center. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Google Cloud Migration Center audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="migrationcenter.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Google Cloud Migration Center generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.migrationcenter.v1.MigrationCenter.AggregateAssetsValues`  
`google.cloud.migrationcenter.v1.MigrationCenter.GetAsset`  
`google.cloud.migrationcenter.v1.MigrationCenter.GetAssetsExportJob`  
`google.cloud.migrationcenter.v1.MigrationCenter.GetDiscoveryClient`  
`google.cloud.migrationcenter.v1.MigrationCenter.GetGroup`  
`google.cloud.migrationcenter.v1.MigrationCenter.GetImportJob`  
`google.cloud.migrationcenter.v1.MigrationCenter.GetPreferenceSet`  
`google.cloud.migrationcenter.v1.MigrationCenter.GetRelation`  
`google.cloud.migrationcenter.v1.MigrationCenter.GetReport`  
`google.cloud.migrationcenter.v1.MigrationCenter.GetReportConfig`  
`google.cloud.migrationcenter.v1.MigrationCenter.GetSettings`  
`google.cloud.migrationcenter.v1.MigrationCenter.GetSource`  
`google.cloud.migrationcenter.v1.MigrationCenter.ListAssets`  
`google.cloud.migrationcenter.v1.MigrationCenter.ListAssetsExportJobs`  
`google.cloud.migrationcenter.v1.MigrationCenter.ListDiscoveryClients`  
`google.cloud.migrationcenter.v1.MigrationCenter.ListGroups`  
`google.cloud.migrationcenter.v1.MigrationCenter.ListImportJobs`  
`google.cloud.migrationcenter.v1.MigrationCenter.ListPreferenceSets`  
`google.cloud.migrationcenter.v1.MigrationCenter.ListRelations`  
`google.cloud.migrationcenter.v1.MigrationCenter.ListReportConfigs`  
`google.cloud.migrationcenter.v1.MigrationCenter.ListReports`  
`google.cloud.migrationcenter.v1.MigrationCenter.ListSources`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.AggregateAssetsValues`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetAsset`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetAssetsExportJob`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetDiscoveryClient`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetGroup`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetImportJob`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetPreferenceSet`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetRelation`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetReport`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetReportConfig`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetReportExportJob`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetSettings`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetSource`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListAssets`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListAssetsExportJobs`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListDiscoveryClients`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListGroups`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListImportJobs`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListPreferenceSets`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListRelations`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListReportConfigs`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListReportExportJobs`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListReports`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListSources`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.migrationcenter.v1.MigrationCenter.AddAssetsToGroup` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.BatchDeleteAssets`  
`google.cloud.migrationcenter.v1.MigrationCenter.BatchUpdateAssets`  
`google.cloud.migrationcenter.v1.MigrationCenter.CreateAssetsExportJob` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.CreateDiscoveryClient` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.CreateGroup` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.CreateImportJob` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.CreatePreferenceSet` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.CreateReport` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.CreateReportConfig` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.CreateSource` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.DeleteAsset`  
`google.cloud.migrationcenter.v1.MigrationCenter.DeleteAssetsExportJob` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.DeleteDiscoveryClient` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.DeleteGroup` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.DeleteImportJob` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.DeletePreferenceSet` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.DeleteReport` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.DeleteReportConfig` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.DeleteSource` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.RemoveAssetsFromGroup` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.ReportAssetFrames`  
`google.cloud.migrationcenter.v1.MigrationCenter.RunAssetsExportJob` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.RunImportJob` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.UpdateAsset`  
`google.cloud.migrationcenter.v1.MigrationCenter.UpdateDiscoveryClient` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.UpdateGroup` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.UpdateImportJob` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.UpdatePreferenceSet` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.UpdateSettings` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.UpdateSource` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.ValidateImportJob` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.AddAssetsToGroup` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.BatchDeleteAssets`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.BatchUpdateAssets`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateAssetsExportJob` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateDiscoveryClient` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateGroup` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateImportJob` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreatePreferenceSet` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateReport` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateReportConfig` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateReportExportJob` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateSource` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteAsset`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteAssetsExportJob` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteDiscoveryClient` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteGroup` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteImportJob` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeletePreferenceSet` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteReport` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteReportConfig` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteReportExportJob` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteSource` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.RemoveAssetsFromGroup` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.ReportAssetFrames`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.RunAssetsExportJob` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.RunImportJob` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.RunReportExportJob` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdateAsset`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdateDiscoveryClient` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdateGroup` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdateImportJob` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdatePreferenceSet` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdateSettings` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdateSource` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.ValidateImportJob` (LRO)  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
`DATA_READ` | `google.cloud.migrationcenter.v1.MigrationCenter.GetErrorFrame`  
`google.cloud.migrationcenter.v1.MigrationCenter.GetImportDataFile`  
`google.cloud.migrationcenter.v1.MigrationCenter.ListErrorFrames`  
`google.cloud.migrationcenter.v1.MigrationCenter.ListImportDataFiles`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetErrorFrame`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetImportDataFile`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListErrorFrames`  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListImportDataFiles`  
`DATA_WRITE` | `google.cloud.migrationcenter.v1.MigrationCenter.CreateImportDataFile` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.DeleteImportDataFile` (LRO)  
`google.cloud.migrationcenter.v1.MigrationCenter.SendDiscoveryClientHeartbeat` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateImportDataFile` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteImportDataFile` (LRO)  
`google.cloud.migrationcenter.v1alpha1.MigrationCenter.SendDiscoveryClientHeartbeat` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Google Cloud Migration Center.

### `google.cloud.migrationcenter.v1.MigrationCenter`

The following audit logs are associated with methods belonging to `google.cloud.migrationcenter.v1.MigrationCenter`.

#### `AddAssetsToGroup`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.AddAssetsToGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.groups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.AddAssetsToGroup" `  




#### `AggregateAssetsValues`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.AggregateAssetsValues`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.assets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.AggregateAssetsValues" `  




#### `BatchDeleteAssets`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.BatchDeleteAssets`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.assets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.BatchDeleteAssets" `  




#### `BatchUpdateAssets`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.BatchUpdateAssets`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.assets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.BatchUpdateAssets" `  




#### `CreateAssetsExportJob`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.CreateAssetsExportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.assetsExportJobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.CreateAssetsExportJob" `  




#### `CreateDiscoveryClient`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.CreateDiscoveryClient`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.discoveryClients.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.CreateDiscoveryClient" `  




#### `CreateGroup`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.CreateGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.groups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.CreateGroup" `  




#### `CreateImportDataFile`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.CreateImportDataFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.importDataFiles.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.CreateImportDataFile" `  




#### `CreateImportJob`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.CreateImportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.importJobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.CreateImportJob" `  




#### `CreatePreferenceSet`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.CreatePreferenceSet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.preferenceSets.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.CreatePreferenceSet" `  




#### `CreateReport`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.CreateReport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.reports.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.CreateReport" `  




#### `CreateReportConfig`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.CreateReportConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.reportConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.CreateReportConfig" `  




#### `CreateSource`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.CreateSource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.sources.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.CreateSource" `  




#### `DeleteAsset`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.DeleteAsset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.assets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.DeleteAsset" `  




#### `DeleteAssetsExportJob`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.DeleteAssetsExportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.assetsExportJobs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.DeleteAssetsExportJob" `  




#### `DeleteDiscoveryClient`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.DeleteDiscoveryClient`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.discoveryClients.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.DeleteDiscoveryClient" `  




#### `DeleteGroup`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.DeleteGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.groups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.DeleteGroup" `  




#### `DeleteImportDataFile`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.DeleteImportDataFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.importDataFiles.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.DeleteImportDataFile" `  




#### `DeleteImportJob`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.DeleteImportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.importJobs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.DeleteImportJob" `  




#### `DeletePreferenceSet`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.DeletePreferenceSet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.preferenceSets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.DeletePreferenceSet" `  




#### `DeleteReport`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.DeleteReport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.reports.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.DeleteReport" `  




#### `DeleteReportConfig`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.DeleteReportConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.reportConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.DeleteReportConfig" `  




#### `DeleteSource`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.DeleteSource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.sources.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.DeleteSource" `  




#### `GetAsset`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.GetAsset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.assets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.GetAsset" `  




#### `GetAssetsExportJob`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.GetAssetsExportJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.assetsExportJobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.GetAssetsExportJob" `  




#### `GetDiscoveryClient`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.GetDiscoveryClient`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.discoveryClients.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.GetDiscoveryClient" `  




#### `GetErrorFrame`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.GetErrorFrame`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.errorFrames.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.GetErrorFrame" `  




#### `GetGroup`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.GetGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.groups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.GetGroup" `  




#### `GetImportDataFile`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.GetImportDataFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.importDataFiles.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.GetImportDataFile" `  




#### `GetImportJob`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.GetImportJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.importJobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.GetImportJob" `  




#### `GetPreferenceSet`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.GetPreferenceSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.preferenceSets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.GetPreferenceSet" `  




#### `GetRelation`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.GetRelation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.relations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.GetRelation" `  




#### `GetReport`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.GetReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.reports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.GetReport" `  




#### `GetReportConfig`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.GetReportConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.reportConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.GetReportConfig" `  




#### `GetSettings`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.GetSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.settings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.GetSettings" `  




#### `GetSource`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.GetSource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.sources.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.GetSource" `  




#### `ListAssets`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.ListAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.assets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.ListAssets" `  




#### `ListAssetsExportJobs`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.ListAssetsExportJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.assetsExportJobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.ListAssetsExportJobs" `  




#### `ListDiscoveryClients`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.ListDiscoveryClients`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.discoveryClients.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.ListDiscoveryClients" `  




#### `ListErrorFrames`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.ListErrorFrames`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.errorFrames.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.ListErrorFrames" `  




#### `ListGroups`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.ListGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.groups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.ListGroups" `  




#### `ListImportDataFiles`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.ListImportDataFiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.importDataFiles.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.ListImportDataFiles" `  




#### `ListImportJobs`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.ListImportJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.importJobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.ListImportJobs" `  




#### `ListPreferenceSets`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.ListPreferenceSets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.preferenceSets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.ListPreferenceSets" `  




#### `ListRelations`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.ListRelations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.relations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.ListRelations" `  




#### `ListReportConfigs`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.ListReportConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.reportConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.ListReportConfigs" `  




#### `ListReports`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.ListReports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.reports.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.ListReports" `  




#### `ListSources`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.ListSources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.sources.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.ListSources" `  




#### `RemoveAssetsFromGroup`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.RemoveAssetsFromGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.groups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.RemoveAssetsFromGroup" `  




#### `ReportAssetFrames`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.ReportAssetFrames`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.assets.reportFrames - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.ReportAssetFrames" `  




#### `RunAssetsExportJob`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.RunAssetsExportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.assetsExportJobs.run - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.RunAssetsExportJob" `  




#### `RunImportJob`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.RunImportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.importJobs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.RunImportJob" `  




#### `SendDiscoveryClientHeartbeat`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.SendDiscoveryClientHeartbeat`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.discoveryClients.sendHeartbeat - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.SendDiscoveryClientHeartbeat" `  




#### `UpdateAsset`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.UpdateAsset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.assets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.UpdateAsset" `  




#### `UpdateDiscoveryClient`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.UpdateDiscoveryClient`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.discoveryClients.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.UpdateDiscoveryClient" `  




#### `UpdateGroup`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.UpdateGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.groups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.UpdateGroup" `  




#### `UpdateImportJob`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.UpdateImportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.importJobs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.UpdateImportJob" `  




#### `UpdatePreferenceSet`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.UpdatePreferenceSet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.preferenceSets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.UpdatePreferenceSet" `  




#### `UpdateSettings`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.UpdateSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.settings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.UpdateSettings" `  




#### `UpdateSource`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.UpdateSource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.sources.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.UpdateSource" `  




#### `ValidateImportJob`

  * **Method** : `google.cloud.migrationcenter.v1.MigrationCenter.ValidateImportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.importJobs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1.MigrationCenter.ValidateImportJob" `  




### `google.cloud.migrationcenter.v1alpha1.MigrationCenter`

The following audit logs are associated with methods belonging to `google.cloud.migrationcenter.v1alpha1.MigrationCenter`.

#### `AddAssetsToGroup`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.AddAssetsToGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.groups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.AddAssetsToGroup" `  




#### `AggregateAssetsValues`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.AggregateAssetsValues`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.assets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.AggregateAssetsValues" `  




#### `BatchDeleteAssets`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.BatchDeleteAssets`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.assets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.BatchDeleteAssets" `  




#### `BatchUpdateAssets`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.BatchUpdateAssets`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.assets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.BatchUpdateAssets" `  




#### `CreateAssetsExportJob`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateAssetsExportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.assetsExportJobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateAssetsExportJob" `  




#### `CreateDiscoveryClient`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateDiscoveryClient`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.discoveryClients.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateDiscoveryClient" `  




#### `CreateGroup`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.groups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateGroup" `  




#### `CreateImportDataFile`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateImportDataFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.importDataFiles.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateImportDataFile" `  




#### `CreateImportJob`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateImportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.importJobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateImportJob" `  




#### `CreatePreferenceSet`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreatePreferenceSet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.preferenceSets.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreatePreferenceSet" `  




#### `CreateReport`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateReport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.reports.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateReport" `  




#### `CreateReportConfig`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateReportConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.reportConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateReportConfig" `  




#### `CreateReportExportJob`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateReportExportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.reportExportJobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateReportExportJob" `  




#### `CreateSource`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateSource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.sources.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.CreateSource" `  




#### `DeleteAsset`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteAsset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.assets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteAsset" `  




#### `DeleteAssetsExportJob`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteAssetsExportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.assetsExportJobs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteAssetsExportJob" `  




#### `DeleteDiscoveryClient`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteDiscoveryClient`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.discoveryClients.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteDiscoveryClient" `  




#### `DeleteGroup`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.groups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteGroup" `  




#### `DeleteImportDataFile`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteImportDataFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.importDataFiles.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteImportDataFile" `  




#### `DeleteImportJob`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteImportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.importJobs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteImportJob" `  




#### `DeletePreferenceSet`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeletePreferenceSet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.preferenceSets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeletePreferenceSet" `  




#### `DeleteReport`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteReport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.reports.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteReport" `  




#### `DeleteReportConfig`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteReportConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.reportConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteReportConfig" `  




#### `DeleteReportExportJob`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteReportExportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.reportExportJobs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteReportExportJob" `  




#### `DeleteSource`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteSource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.sources.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.DeleteSource" `  




#### `GetAsset`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetAsset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.assets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetAsset" `  




#### `GetAssetsExportJob`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetAssetsExportJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.assetsExportJobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetAssetsExportJob" `  




#### `GetDiscoveryClient`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetDiscoveryClient`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.discoveryClients.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetDiscoveryClient" `  




#### `GetErrorFrame`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetErrorFrame`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.errorFrames.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetErrorFrame" `  




#### `GetGroup`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.groups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetGroup" `  




#### `GetImportDataFile`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetImportDataFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.importDataFiles.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetImportDataFile" `  




#### `GetImportJob`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetImportJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.importJobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetImportJob" `  




#### `GetPreferenceSet`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetPreferenceSet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.preferenceSets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetPreferenceSet" `  




#### `GetRelation`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetRelation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.relations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetRelation" `  




#### `GetReport`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.reports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetReport" `  




#### `GetReportConfig`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetReportConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.reportConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetReportConfig" `  




#### `GetReportExportJob`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetReportExportJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.reportExportJobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetReportExportJob" `  




#### `GetSettings`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.settings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetSettings" `  




#### `GetSource`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetSource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.sources.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.GetSource" `  




#### `ListAssets`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.assets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListAssets" `  




#### `ListAssetsExportJobs`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListAssetsExportJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.assetsExportJobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListAssetsExportJobs" `  




#### `ListDiscoveryClients`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListDiscoveryClients`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.discoveryClients.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListDiscoveryClients" `  




#### `ListErrorFrames`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListErrorFrames`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.errorFrames.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListErrorFrames" `  




#### `ListGroups`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.groups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListGroups" `  




#### `ListImportDataFiles`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListImportDataFiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.importDataFiles.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListImportDataFiles" `  




#### `ListImportJobs`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListImportJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.importJobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListImportJobs" `  




#### `ListPreferenceSets`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListPreferenceSets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.preferenceSets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListPreferenceSets" `  




#### `ListRelations`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListRelations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.relations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListRelations" `  




#### `ListReportConfigs`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListReportConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.reportConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListReportConfigs" `  




#### `ListReportExportJobs`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListReportExportJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.reportExportJobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListReportExportJobs" `  




#### `ListReports`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListReports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.reports.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListReports" `  




#### `ListSources`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListSources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.sources.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.ListSources" `  




#### `RemoveAssetsFromGroup`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.RemoveAssetsFromGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.groups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.RemoveAssetsFromGroup" `  




#### `ReportAssetFrames`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.ReportAssetFrames`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.assets.reportFrames - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.ReportAssetFrames" `  




#### `RunAssetsExportJob`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.RunAssetsExportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.assetsExportJobs.run - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.RunAssetsExportJob" `  




#### `RunImportJob`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.RunImportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.importJobs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.RunImportJob" `  




#### `RunReportExportJob`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.RunReportExportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.reportExportJobs.run - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.RunReportExportJob" `  




#### `SendDiscoveryClientHeartbeat`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.SendDiscoveryClientHeartbeat`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.discoveryClients.sendHeartbeat - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.SendDiscoveryClientHeartbeat" `  




#### `UpdateAsset`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdateAsset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.assets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdateAsset" `  




#### `UpdateDiscoveryClient`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdateDiscoveryClient`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.discoveryClients.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdateDiscoveryClient" `  




#### `UpdateGroup`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdateGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.groups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdateGroup" `  




#### `UpdateImportJob`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdateImportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.importJobs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdateImportJob" `  




#### `UpdatePreferenceSet`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdatePreferenceSet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.preferenceSets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdatePreferenceSet" `  




#### `UpdateSettings`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdateSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.settings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdateSettings" `  




#### `UpdateSource`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdateSource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.sources.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.UpdateSource" `  




#### `ValidateImportJob`

  * **Method** : `google.cloud.migrationcenter.v1alpha1.MigrationCenter.ValidateImportJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.importJobs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.migrationcenter.v1alpha1.MigrationCenter.ValidateImportJob" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `migrationcenter.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `migrationcenter.operations.list - ADMIN_READ`
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

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
