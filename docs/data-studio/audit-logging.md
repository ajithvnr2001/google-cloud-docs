---
url: https://docs.cloud.google.com/data-studio/audit-logging/
title: Data Studio Pro audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:10.431329+00:00
---

# Data Studio Pro audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/audit-logging/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Data Studio Pro audit logging Stay organized with collections  Save and categorize content based on your preferences. 

**Data Studio Pro feature**

The features and functionality described in this page are available to Data Studio Pro users.

[Get Data Studio Pro.](https://docs.cloud.google.com/data-studio/about-pro)

This document describes audit logging for Looker Studio. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Looker Studio audit logs use the service name `datastudio.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="datastudio.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Looker Studio generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `GetCloudSharing`  
`google.analytics.datastudio.v1.DataStudioService.GetPermissions`  
`ADMIN_WRITE` | `CloudOwnershipTransfer`  
`ConvertEmbeddedDatasourceToShareable`  
`CopyDatasourceAndRedirect`  
`CopyReport`  
`CreateBlockDatasource`  
`CreateReport`  
`CreateSubscription`  
`GetProjectLicense`  
`GetProjectLicenseInformation`  
`MoveAsset`  
`RestoreProjectSubscription`  
`RestoreSubscription`  
`Subscribe`  
`TerminateProjectSubscription`  
`TerminateSubscription`  
`UpdateCloudSharing`  
`UpdateProjectLicense`  
`UpdateProjectSubscription`  
`ValidateAddOnLicenses`  
`google.analytics.datastudio.v1.DataStudioService.RevokeAllPermissions`  
`google.analytics.datastudio.v1.DataStudioService.UpdatePermissions`  
`DATA_READ` | `BatchedDataActionV2`  
`CopyDatasource`  
`CreateAlert`  
`CreateShortLink`  
`ExportDatasource`  
`ExportToSlides`  
`GetBlockDatasource`  
`GetClaimedDatasources`  
`GetDatasourceSchema`  
`GetEntityScheduleList`  
`GetReport`  
`GetWorkspace`  
`ListAlerts`  
`PersistTempReport`  
`ReadShareableImage`  
`Report`  
`UpdateAlert`  
`google.analytics.datastudio.v1.DataStudioService.GetAsset`  
`DATA_WRITE` | `BatchSchedule`  
`BatchedClaimDatasourceForReport`  
`ClaimDatasourceForReport`  
`CopyDatasource`  
`CreateNamedRevision`  
`CreatePages`  
`CreateWorkspace`  
`DeleteClaim`  
`DeletePages`  
`DeleteRevision`  
`DeleteShareable`  
`GetClaimedReports`  
`GetPdf`  
`GetReportDatasourcesPermission`  
`GetRevision`  
`GetRevisions`  
`PublishDatasource`  
`PublishReport`  
`RenameDatasource`  
`RenameWorkspace`  
`RestoreRevision`  
`ToggleScheduleStatus`  
`TriggerSchedule`  
`UpdateDataAccessControl`  
`UpdatePage`  
`UpdateRemovedState`  
`UpdateReport`  
`UpdateReportLayout`  
`UpdateReportNavigationInfo`  
`UpdateRevision`  
`UploadShareableImage`  
`google.analytics.datastudio.v1.DataStudioService.AddMembers`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Looker Studio.

### `google.analytics.datastudio.v1.DataStudioService`

The following audit logs are associated with methods belonging to `google.analytics.datastudio.v1.DataStudioService`.

#### `AddMembers`

  * **Method** : `google.analytics.datastudio.v1.DataStudioService.AddMembers`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastudio.reports.legacyOwner - ADMIN_WRITE`
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.analytics.datastudio.v1.DataStudioService.AddMembers" `  




#### `GetAsset`

  * **Method** : `google.analytics.datastudio.v1.DataStudioService.GetAsset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.datasources.get - DATA_READ`
    * `datastudio.reports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.analytics.datastudio.v1.DataStudioService.GetAsset" `  




#### `GetPermissions`

  * **Method** : `google.analytics.datastudio.v1.DataStudioService.GetPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.datasources.getIamPolicy - ADMIN_READ`
    * `datastudio.reports.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.analytics.datastudio.v1.DataStudioService.GetPermissions" `  




#### `RevokeAllPermissions`

  * **Method** : `google.analytics.datastudio.v1.DataStudioService.RevokeAllPermissions`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastudio.datasources.legacyOwner - ADMIN_WRITE`
    * `datastudio.datasources.update - DATA_WRITE`
    * `datastudio.reports.legacyOwner - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.analytics.datastudio.v1.DataStudioService.RevokeAllPermissions" `  




#### `UpdatePermissions`

  * **Method** : `google.analytics.datastudio.v1.DataStudioService.UpdatePermissions`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastudio.datasources.legacyOwner - ADMIN_WRITE`
    * `datastudio.datasources.update - DATA_WRITE`
    * `datastudio.reports.legacyOwner - ADMIN_WRITE`
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.analytics.datastudio.v1.DataStudioService.UpdatePermissions" `  




### `other`

The following audit logs are associated with methods belonging to `other`.

#### `BatchSchedule`

  * **Method** : `BatchSchedule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.createSchedule - DATA_WRITE`
    * `datastudio.reports.deleteSchedule - DATA_WRITE`
    * `datastudio.reports.updateSchedule - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="BatchSchedule" `  




#### `BatchedClaimDatasourceForReport`

  * **Method** : `BatchedClaimDatasourceForReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.datasources.get - DATA_READ`
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="BatchedClaimDatasourceForReport" `  




#### `BatchedDataActionV2`

  * **Method** : `BatchedDataActionV2`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="BatchedDataActionV2" `  




#### `ClaimDatasourceForReport`

  * **Method** : `ClaimDatasourceForReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.datasources.get - DATA_READ`
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ClaimDatasourceForReport" `  




#### `CloudOwnershipTransfer`

  * **Method** : `CloudOwnershipTransfer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastudio.datasources.setIamPolicy - ADMIN_WRITE`
    * `datastudio.reports.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CloudOwnershipTransfer" `  




#### `ConvertEmbeddedDatasourceToShareable`

  * **Method** : `ConvertEmbeddedDatasourceToShareable`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastudio.datasources.setIamPolicy - ADMIN_WRITE`
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ConvertEmbeddedDatasourceToShareable" `  




#### `CopyDatasource`

  * **Method** : `CopyDatasource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.datasources.get - DATA_READ`
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CopyDatasource" `  




#### `CopyDatasourceAndRedirect`

  * **Method** : `CopyDatasourceAndRedirect`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastudio.datasources.get - DATA_READ`
    * `datastudio.datasources.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CopyDatasourceAndRedirect" `  




#### `CopyReport`

  * **Method** : `CopyReport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastudio.datasources.get - DATA_READ`
    * `datastudio.reports.get - DATA_READ`
    * `datastudio.reports.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CopyReport" `  




#### `CreateAlert`

  * **Method** : `CreateAlert`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CreateAlert" `  




#### `CreateBlockDatasource`

  * **Method** : `CreateBlockDatasource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastudio.datasources.setIamPolicy - ADMIN_WRITE`
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CreateBlockDatasource" `  




#### `CreateNamedRevision`

  * **Method** : `CreateNamedRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CreateNamedRevision" `  




#### `CreatePages`

  * **Method** : `CreatePages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CreatePages" `  




#### `CreateReport`

  * **Method** : `CreateReport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastudio.reports.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CreateReport" `  




#### `CreateShortLink`

  * **Method** : `CreateShortLink`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CreateShortLink" `  




#### `CreateSubscription`

  * **Method** : `CreateSubscription`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lookerstudio.pro.manage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CreateSubscription" `  




#### `CreateWorkspace`

  * **Method** : `CreateWorkspace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastudio.folders1.createUnder - DATA_WRITE`
    * `datastudio.workspaces.createUnder - DATA_WRITE`
    * `datastudio.workspaces.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="CreateWorkspace" `  




#### `DeleteClaim`

  * **Method** : `DeleteClaim`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="DeleteClaim" `  




#### `DeletePages`

  * **Method** : `DeletePages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="DeletePages" `  




#### `DeleteRevision`

  * **Method** : `DeleteRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="DeleteRevision" `  




#### `DeleteShareable`

  * **Method** : `DeleteShareable`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.folders1.delete - DATA_WRITE`
    * `datastudio.reports.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="DeleteShareable" `  




#### `ExportDatasource`

  * **Method** : `ExportDatasource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ExportDatasource" `  




#### `ExportToSlides`

  * **Method** : `ExportToSlides`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ExportToSlides" `  




#### `GetBlockDatasource`

  * **Method** : `GetBlockDatasource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.datasources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetBlockDatasource" `  




#### `GetClaimedDatasources`

  * **Method** : `GetClaimedDatasources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetClaimedDatasources" `  




#### `GetClaimedReports`

  * **Method** : `GetClaimedReports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.datasources.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetClaimedReports" `  




#### `GetCloudSharing`

  * **Method** : `GetCloudSharing`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.folders1.getIamPolicy - ADMIN_READ`
    * `datastudio.reports.getIamPolicy - ADMIN_READ`
    * `datastudio.workspaces.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetCloudSharing" `  




#### `GetDatasourceSchema`

  * **Method** : `GetDatasourceSchema`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetDatasourceSchema" `  




#### `GetEntityScheduleList`

  * **Method** : `GetEntityScheduleList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.listSchedule - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetEntityScheduleList" `  




#### `GetPdf`

  * **Method** : `GetPdf`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetPdf" `  




#### `GetProjectLicense`

  * **Method** : `GetProjectLicense`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lookerstudio.pro.manage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetProjectLicense" `  




#### `GetProjectLicenseInformation`

  * **Method** : `GetProjectLicenseInformation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lookerstudio.pro.manage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetProjectLicenseInformation" `  




#### `GetReport`

  * **Method** : `GetReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetReport" `  




#### `GetReportDatasourcesPermission`

  * **Method** : `GetReportDatasourcesPermission`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetReportDatasourcesPermission" `  




#### `GetRevision`

  * **Method** : `GetRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetRevision" `  




#### `GetRevisions`

  * **Method** : `GetRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetRevisions" `  




#### `GetWorkspace`

  * **Method** : `GetWorkspace`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.folders1.get - DATA_READ`
    * `datastudio.workspaces.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetWorkspace" `  




#### `ListAlerts`

  * **Method** : `ListAlerts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ListAlerts" `  




#### `MoveAsset`

  * **Method** : `MoveAsset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastudio.datasources.legacyOwner - ADMIN_WRITE`
    * `datastudio.folders1.moveIn - DATA_WRITE`
    * `datastudio.reports.legacyOwner - ADMIN_WRITE`
    * `datastudio.workspaces.moveIn - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="MoveAsset" `  




#### `PersistTempReport`

  * **Method** : `PersistTempReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="PersistTempReport" `  




#### `PublishDatasource`

  * **Method** : `PublishDatasource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.datasources.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="PublishDatasource" `  




#### `PublishReport`

  * **Method** : `PublishReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="PublishReport" `  




#### `ReadShareableImage`

  * **Method** : `ReadShareableImage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ReadShareableImage" `  




#### `RenameDatasource`

  * **Method** : `RenameDatasource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.datasources.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="RenameDatasource" `  




#### `RenameWorkspace`

  * **Method** : `RenameWorkspace`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.folders1.update - DATA_WRITE`
    * `datastudio.workspaces.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="RenameWorkspace" `  




#### `Report`

  * **Method** : `Report`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="Report" `  




#### `RestoreProjectSubscription`

  * **Method** : `RestoreProjectSubscription`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lookerstudio.pro.manage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="RestoreProjectSubscription" `  




#### `RestoreRevision`

  * **Method** : `RestoreRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="RestoreRevision" `  




#### `RestoreSubscription`

  * **Method** : `RestoreSubscription`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lookerstudio.pro.manage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="RestoreSubscription" `  




#### `Subscribe`

  * **Method** : `Subscribe`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lookerstudio.pro.manage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="Subscribe" `  




#### `TerminateProjectSubscription`

  * **Method** : `TerminateProjectSubscription`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lookerstudio.pro.manage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="TerminateProjectSubscription" `  




#### `TerminateSubscription`

  * **Method** : `TerminateSubscription`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lookerstudio.pro.manage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="TerminateSubscription" `  




#### `ToggleScheduleStatus`

  * **Method** : `ToggleScheduleStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.updateSchedule - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ToggleScheduleStatus" `  




#### `TriggerSchedule`

  * **Method** : `TriggerSchedule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.createSchedule - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="TriggerSchedule" `  




#### `UpdateAlert`

  * **Method** : `UpdateAlert`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateAlert" `  




#### `UpdateCloudSharing`

  * **Method** : `UpdateCloudSharing`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastudio.reports.legacyOwner - ADMIN_WRITE`
    * `datastudio.reports.update - DATA_WRITE`
    * `datastudio.workspaces.getIamPolicy - ADMIN_READ`
    * `datastudio.workspaces.shareCM - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateCloudSharing" `  




#### `UpdateDataAccessControl`

  * **Method** : `UpdateDataAccessControl`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.datasources.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateDataAccessControl" `  




#### `UpdatePage`

  * **Method** : `UpdatePage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdatePage" `  




#### `UpdateProjectLicense`

  * **Method** : `UpdateProjectLicense`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lookerstudio.pro.manage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateProjectLicense" `  




#### `UpdateProjectSubscription`

  * **Method** : `UpdateProjectSubscription`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lookerstudio.pro.manage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateProjectSubscription" `  




#### `UpdateRemovedState`

  * **Method** : `UpdateRemovedState`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.datasources.trash - DATA_WRITE`
    * `datastudio.reports.trash - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateRemovedState" `  




#### `UpdateReport`

  * **Method** : `UpdateReport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateReport" `  




#### `UpdateReportLayout`

  * **Method** : `UpdateReportLayout`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateReportLayout" `  




#### `UpdateReportNavigationInfo`

  * **Method** : `UpdateReportNavigationInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateReportNavigationInfo" `  




#### `UpdateRevision`

  * **Method** : `UpdateRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UpdateRevision" `  




#### `UploadShareableImage`

  * **Method** : `UploadShareableImage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastudio.reports.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="UploadShareableImage" `  




#### `ValidateAddOnLicenses`

  * **Method** : `ValidateAddOnLicenses`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `lookerstudio.pro.manage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="ValidateAddOnLicenses" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
