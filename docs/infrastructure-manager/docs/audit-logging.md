---
url: https://docs.cloud.google.com/infrastructure-manager/docs/audit-logging/
title: Infrastructure Manager audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:18.738826+00:00
---

# Infrastructure Manager audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  Infrastructure Manager audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Infrastructure Manager. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Infrastructure Manager audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="config.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Infrastructure Manager generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.config.v1.Config.ExportDeploymentStatefile`  
`google.cloud.config.v1.Config.ExportLockInfo`  
`google.cloud.config.v1.Config.ExportPreviewResult`  
`google.cloud.config.v1.Config.ExportRevisionStatefile`  
`google.cloud.config.v1.Config.GetAutoMigrationConfig`  
`google.cloud.config.v1.Config.GetDeployment`  
`google.cloud.config.v1.Config.GetDeploymentGroup`  
`google.cloud.config.v1.Config.GetDeploymentGroupRevision`  
`google.cloud.config.v1.Config.GetPreview`  
`google.cloud.config.v1.Config.GetResource`  
`google.cloud.config.v1.Config.GetResourceChange`  
`google.cloud.config.v1.Config.GetResourceDrift`  
`google.cloud.config.v1.Config.GetRevision`  
`google.cloud.config.v1.Config.GetTerraformVersion`  
`google.cloud.config.v1.Config.ListDeploymentGroupRevisions`  
`google.cloud.config.v1.Config.ListDeploymentGroups`  
`google.cloud.config.v1.Config.ListDeployments`  
`google.cloud.config.v1.Config.ListPreviews`  
`google.cloud.config.v1.Config.ListResourceChanges`  
`google.cloud.config.v1.Config.ListResourceDrifts`  
`google.cloud.config.v1.Config.ListResources`  
`google.cloud.config.v1.Config.ListRevisions`  
`google.cloud.config.v1.Config.ListTerraformVersions`  
`google.cloud.config.v1alpha2.Config.ExportDeploymentStatefile`  
`google.cloud.config.v1alpha2.Config.ExportLockInfo`  
`google.cloud.config.v1alpha2.Config.ExportPreviewResult`  
`google.cloud.config.v1alpha2.Config.ExportRevisionStatefile`  
`google.cloud.config.v1alpha2.Config.GetAutoMigrationConfig`  
`google.cloud.config.v1alpha2.Config.GetDeployment`  
`google.cloud.config.v1alpha2.Config.GetDeploymentGroup`  
`google.cloud.config.v1alpha2.Config.GetDeploymentGroupRevision`  
`google.cloud.config.v1alpha2.Config.GetPreview`  
`google.cloud.config.v1alpha2.Config.GetResource`  
`google.cloud.config.v1alpha2.Config.GetResourceChange`  
`google.cloud.config.v1alpha2.Config.GetResourceDrift`  
`google.cloud.config.v1alpha2.Config.GetRevision`  
`google.cloud.config.v1alpha2.Config.GetTerraformVersion`  
`google.cloud.config.v1alpha2.Config.ListDeploymentGroupRevisions`  
`google.cloud.config.v1alpha2.Config.ListDeploymentGroups`  
`google.cloud.config.v1alpha2.Config.ListDeployments`  
`google.cloud.config.v1alpha2.Config.ListPreviews`  
`google.cloud.config.v1alpha2.Config.ListResourceChanges`  
`google.cloud.config.v1alpha2.Config.ListResourceDrifts`  
`google.cloud.config.v1alpha2.Config.ListResources`  
`google.cloud.config.v1alpha2.Config.ListRevisions`  
`google.cloud.config.v1alpha2.Config.ListTerraformVersions`  
`GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.config.v1.Config.CreateDeployment` (LRO)  
`google.cloud.config.v1.Config.CreateDeploymentGroup` (LRO)  
`google.cloud.config.v1.Config.CreatePreview` (LRO)  
`google.cloud.config.v1.Config.DeleteDeployment` (LRO)  
`google.cloud.config.v1.Config.DeleteDeploymentGroup` (LRO)  
`google.cloud.config.v1.Config.DeletePreview` (LRO)  
`google.cloud.config.v1.Config.DeleteStatefile`  
`google.cloud.config.v1.Config.DeprovisionDeploymentGroup` (LRO)  
`google.cloud.config.v1.Config.ImportArtifacts`  
`google.cloud.config.v1.Config.ImportStatefile`  
`google.cloud.config.v1.Config.LockDeployment` (LRO)  
`google.cloud.config.v1.Config.ProvisionDeploymentGroup` (LRO)  
`google.cloud.config.v1.Config.UnlockDeployment` (LRO)  
`google.cloud.config.v1.Config.UpdateAutoMigrationConfig` (LRO)  
`google.cloud.config.v1.Config.UpdateDeployment` (LRO)  
`google.cloud.config.v1.Config.UpdateDeploymentGroup` (LRO)  
`google.cloud.config.v1alpha2.Config.CreateDeployment` (LRO)  
`google.cloud.config.v1alpha2.Config.CreateDeploymentGroup` (LRO)  
`google.cloud.config.v1alpha2.Config.CreatePreview` (LRO)  
`google.cloud.config.v1alpha2.Config.DeleteDeployment` (LRO)  
`google.cloud.config.v1alpha2.Config.DeleteDeploymentGroup` (LRO)  
`google.cloud.config.v1alpha2.Config.DeletePreview` (LRO)  
`google.cloud.config.v1alpha2.Config.DeleteStatefile`  
`google.cloud.config.v1alpha2.Config.DeprovisionDeploymentGroup` (LRO)  
`google.cloud.config.v1alpha2.Config.ImportArtifacts`  
`google.cloud.config.v1alpha2.Config.ImportStatefile`  
`google.cloud.config.v1alpha2.Config.LockDeployment` (LRO)  
`google.cloud.config.v1alpha2.Config.ProvisionDeploymentGroup` (LRO)  
`google.cloud.config.v1alpha2.Config.UnlockDeployment` (LRO)  
`google.cloud.config.v1alpha2.Config.UpdateAutoMigrationConfig` (LRO)  
`google.cloud.config.v1alpha2.Config.UpdateDeployment` (LRO)  
`google.cloud.config.v1alpha2.Config.UpdateDeploymentGroup` (LRO)  
`SetIamPolicy`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Infrastructure Manager.

### `google.cloud.config.v1.Config`

The following audit logs are associated with methods belonging to `google.cloud.config.v1.Config`.

#### `CreateDeployment`

  * **Method** : `google.cloud.config.v1.Config.CreateDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deployments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.CreateDeployment" `  




#### `CreateDeploymentGroup`

  * **Method** : `google.cloud.config.v1.Config.CreateDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deploymentgroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.CreateDeploymentGroup" `  




#### `CreatePreview`

  * **Method** : `google.cloud.config.v1.Config.CreatePreview`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.previews.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.CreatePreview" `  




#### `DeleteDeployment`

  * **Method** : `google.cloud.config.v1.Config.DeleteDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deployments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.DeleteDeployment" `  




#### `DeleteDeploymentGroup`

  * **Method** : `google.cloud.config.v1.Config.DeleteDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deploymentgroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.DeleteDeploymentGroup" `  




#### `DeletePreview`

  * **Method** : `google.cloud.config.v1.Config.DeletePreview`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.previews.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.DeletePreview" `  




#### `DeleteStatefile`

  * **Method** : `google.cloud.config.v1.Config.DeleteStatefile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deployments.deleteState - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.DeleteStatefile" `  




#### `DeprovisionDeploymentGroup`

  * **Method** : `google.cloud.config.v1.Config.DeprovisionDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deploymentgroups.deprovision - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.DeprovisionDeploymentGroup" `  




#### `ExportDeploymentStatefile`

  * **Method** : `google.cloud.config.v1.Config.ExportDeploymentStatefile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.deployments.getState - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.ExportDeploymentStatefile" `  




#### `ExportLockInfo`

  * **Method** : `google.cloud.config.v1.Config.ExportLockInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.deployments.getLock - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.ExportLockInfo" `  




#### `ExportPreviewResult`

  * **Method** : `google.cloud.config.v1.Config.ExportPreviewResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.previews.export - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.ExportPreviewResult" `  




#### `ExportRevisionStatefile`

  * **Method** : `google.cloud.config.v1.Config.ExportRevisionStatefile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.revisions.getState - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.ExportRevisionStatefile" `  




#### `GetAutoMigrationConfig`

  * **Method** : `google.cloud.config.v1.Config.GetAutoMigrationConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.automigrationconfig.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.GetAutoMigrationConfig" `  




#### `GetDeployment`

  * **Method** : `google.cloud.config.v1.Config.GetDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.deployments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.GetDeployment" `  




#### `GetDeploymentGroup`

  * **Method** : `google.cloud.config.v1.Config.GetDeploymentGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.deploymentgroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.GetDeploymentGroup" `  




#### `GetDeploymentGroupRevision`

  * **Method** : `google.cloud.config.v1.Config.GetDeploymentGroupRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.deploymentgrouprevisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.GetDeploymentGroupRevision" `  




#### `GetPreview`

  * **Method** : `google.cloud.config.v1.Config.GetPreview`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.previews.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.GetPreview" `  




#### `GetResource`

  * **Method** : `google.cloud.config.v1.Config.GetResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.resources.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.GetResource" `  




#### `GetResourceChange`

  * **Method** : `google.cloud.config.v1.Config.GetResourceChange`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.resourcechanges.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.GetResourceChange" `  




#### `GetResourceDrift`

  * **Method** : `google.cloud.config.v1.Config.GetResourceDrift`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.resourcedrifts.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.GetResourceDrift" `  




#### `GetRevision`

  * **Method** : `google.cloud.config.v1.Config.GetRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.revisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.GetRevision" `  




#### `GetTerraformVersion`

  * **Method** : `google.cloud.config.v1.Config.GetTerraformVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.terraformversions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.GetTerraformVersion" `  




#### `ImportArtifacts`

  * **Method** : `google.cloud.config.v1.Config.ImportArtifacts`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.artifacts.import - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.ImportArtifacts" `  




#### `ImportStatefile`

  * **Method** : `google.cloud.config.v1.Config.ImportStatefile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deployments.updateState - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.ImportStatefile" `  




#### `ListDeploymentGroupRevisions`

  * **Method** : `google.cloud.config.v1.Config.ListDeploymentGroupRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.deploymentgrouprevisions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.ListDeploymentGroupRevisions" `  




#### `ListDeploymentGroups`

  * **Method** : `google.cloud.config.v1.Config.ListDeploymentGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.deploymentgroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.ListDeploymentGroups" `  




#### `ListDeployments`

  * **Method** : `google.cloud.config.v1.Config.ListDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.deployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.ListDeployments" `  




#### `ListPreviews`

  * **Method** : `google.cloud.config.v1.Config.ListPreviews`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.previews.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.ListPreviews" `  




#### `ListResourceChanges`

  * **Method** : `google.cloud.config.v1.Config.ListResourceChanges`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.resourcechanges.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.ListResourceChanges" `  




#### `ListResourceDrifts`

  * **Method** : `google.cloud.config.v1.Config.ListResourceDrifts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.resourcedrifts.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.ListResourceDrifts" `  




#### `ListResources`

  * **Method** : `google.cloud.config.v1.Config.ListResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.resources.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.ListResources" `  




#### `ListRevisions`

  * **Method** : `google.cloud.config.v1.Config.ListRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.revisions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.ListRevisions" `  




#### `ListTerraformVersions`

  * **Method** : `google.cloud.config.v1.Config.ListTerraformVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.terraformversions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.ListTerraformVersions" `  




#### `LockDeployment`

  * **Method** : `google.cloud.config.v1.Config.LockDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deployments.lock - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.LockDeployment" `  




#### `ProvisionDeploymentGroup`

  * **Method** : `google.cloud.config.v1.Config.ProvisionDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deploymentgroups.provision - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.ProvisionDeploymentGroup" `  




#### `UnlockDeployment`

  * **Method** : `google.cloud.config.v1.Config.UnlockDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deployments.unlock - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.UnlockDeployment" `  




#### `UpdateAutoMigrationConfig`

  * **Method** : `google.cloud.config.v1.Config.UpdateAutoMigrationConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.automigrationconfig.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.UpdateAutoMigrationConfig" `  




#### `UpdateDeployment`

  * **Method** : `google.cloud.config.v1.Config.UpdateDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deployments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.UpdateDeployment" `  




#### `UpdateDeploymentGroup`

  * **Method** : `google.cloud.config.v1.Config.UpdateDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deploymentgroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1.Config.UpdateDeploymentGroup" `  




### `google.cloud.config.v1alpha2.Config`

The following audit logs are associated with methods belonging to `google.cloud.config.v1alpha2.Config`.

#### `CreateDeployment`

  * **Method** : `google.cloud.config.v1alpha2.Config.CreateDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deployments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.CreateDeployment" `  




#### `CreateDeploymentGroup`

  * **Method** : `google.cloud.config.v1alpha2.Config.CreateDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deploymentgroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.CreateDeploymentGroup" `  




#### `CreatePreview`

  * **Method** : `google.cloud.config.v1alpha2.Config.CreatePreview`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deployments.getState - ADMIN_READ`
    * `config.deployments.lock - ADMIN_WRITE`
    * `config.deployments.unlock - ADMIN_WRITE`
    * `config.previews.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.CreatePreview" `  




#### `DeleteDeployment`

  * **Method** : `google.cloud.config.v1alpha2.Config.DeleteDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deployments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.DeleteDeployment" `  




#### `DeleteDeploymentGroup`

  * **Method** : `google.cloud.config.v1alpha2.Config.DeleteDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deploymentgroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.DeleteDeploymentGroup" `  




#### `DeletePreview`

  * **Method** : `google.cloud.config.v1alpha2.Config.DeletePreview`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.previews.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.DeletePreview" `  




#### `DeleteStatefile`

  * **Method** : `google.cloud.config.v1alpha2.Config.DeleteStatefile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deployments.deleteState - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.DeleteStatefile" `  




#### `DeprovisionDeploymentGroup`

  * **Method** : `google.cloud.config.v1alpha2.Config.DeprovisionDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deploymentgroups.deprovision - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.DeprovisionDeploymentGroup" `  




#### `ExportDeploymentStatefile`

  * **Method** : `google.cloud.config.v1alpha2.Config.ExportDeploymentStatefile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.deployments.getState - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.ExportDeploymentStatefile" `  




#### `ExportLockInfo`

  * **Method** : `google.cloud.config.v1alpha2.Config.ExportLockInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.deployments.getLock - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.ExportLockInfo" `  




#### `ExportPreviewResult`

  * **Method** : `google.cloud.config.v1alpha2.Config.ExportPreviewResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.previews.export - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.ExportPreviewResult" `  




#### `ExportRevisionStatefile`

  * **Method** : `google.cloud.config.v1alpha2.Config.ExportRevisionStatefile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.revisions.getState - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.ExportRevisionStatefile" `  




#### `GetAutoMigrationConfig`

  * **Method** : `google.cloud.config.v1alpha2.Config.GetAutoMigrationConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.automigrationconfig.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.GetAutoMigrationConfig" `  




#### `GetDeployment`

  * **Method** : `google.cloud.config.v1alpha2.Config.GetDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.deployments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.GetDeployment" `  




#### `GetDeploymentGroup`

  * **Method** : `google.cloud.config.v1alpha2.Config.GetDeploymentGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.deploymentgroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.GetDeploymentGroup" `  




#### `GetDeploymentGroupRevision`

  * **Method** : `google.cloud.config.v1alpha2.Config.GetDeploymentGroupRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.deploymentgrouprevisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.GetDeploymentGroupRevision" `  




#### `GetPreview`

  * **Method** : `google.cloud.config.v1alpha2.Config.GetPreview`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.previews.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.GetPreview" `  




#### `GetResource`

  * **Method** : `google.cloud.config.v1alpha2.Config.GetResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.resources.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.GetResource" `  




#### `GetResourceChange`

  * **Method** : `google.cloud.config.v1alpha2.Config.GetResourceChange`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.resourcechanges.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.GetResourceChange" `  




#### `GetResourceDrift`

  * **Method** : `google.cloud.config.v1alpha2.Config.GetResourceDrift`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.resourcedrifts.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.GetResourceDrift" `  




#### `GetRevision`

  * **Method** : `google.cloud.config.v1alpha2.Config.GetRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.revisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.GetRevision" `  




#### `GetTerraformVersion`

  * **Method** : `google.cloud.config.v1alpha2.Config.GetTerraformVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.terraformversions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.GetTerraformVersion" `  




#### `ImportArtifacts`

  * **Method** : `google.cloud.config.v1alpha2.Config.ImportArtifacts`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.artifacts.import - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.ImportArtifacts" `  




#### `ImportStatefile`

  * **Method** : `google.cloud.config.v1alpha2.Config.ImportStatefile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deployments.updateState - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.ImportStatefile" `  




#### `ListDeploymentGroupRevisions`

  * **Method** : `google.cloud.config.v1alpha2.Config.ListDeploymentGroupRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.deploymentgrouprevisions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.ListDeploymentGroupRevisions" `  




#### `ListDeploymentGroups`

  * **Method** : `google.cloud.config.v1alpha2.Config.ListDeploymentGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.deploymentgroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.ListDeploymentGroups" `  




#### `ListDeployments`

  * **Method** : `google.cloud.config.v1alpha2.Config.ListDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.deployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.ListDeployments" `  




#### `ListPreviews`

  * **Method** : `google.cloud.config.v1alpha2.Config.ListPreviews`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.previews.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.ListPreviews" `  




#### `ListResourceChanges`

  * **Method** : `google.cloud.config.v1alpha2.Config.ListResourceChanges`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.resourcechanges.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.ListResourceChanges" `  




#### `ListResourceDrifts`

  * **Method** : `google.cloud.config.v1alpha2.Config.ListResourceDrifts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.resourcedrifts.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.ListResourceDrifts" `  




#### `ListResources`

  * **Method** : `google.cloud.config.v1alpha2.Config.ListResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.resources.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.ListResources" `  




#### `ListRevisions`

  * **Method** : `google.cloud.config.v1alpha2.Config.ListRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.revisions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.ListRevisions" `  




#### `ListTerraformVersions`

  * **Method** : `google.cloud.config.v1alpha2.Config.ListTerraformVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.terraformversions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.ListTerraformVersions" `  




#### `LockDeployment`

  * **Method** : `google.cloud.config.v1alpha2.Config.LockDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deployments.lock - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.LockDeployment" `  




#### `ProvisionDeploymentGroup`

  * **Method** : `google.cloud.config.v1alpha2.Config.ProvisionDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deploymentgroups.provision - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.ProvisionDeploymentGroup" `  




#### `UnlockDeployment`

  * **Method** : `google.cloud.config.v1alpha2.Config.UnlockDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deployments.unlock - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.UnlockDeployment" `  




#### `UpdateAutoMigrationConfig`

  * **Method** : `google.cloud.config.v1alpha2.Config.UpdateAutoMigrationConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.automigrationconfig.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.UpdateAutoMigrationConfig" `  




#### `UpdateDeployment`

  * **Method** : `google.cloud.config.v1alpha2.Config.UpdateDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deployments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.UpdateDeployment" `  




#### `UpdateDeploymentGroup`

  * **Method** : `google.cloud.config.v1alpha2.Config.UpdateDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deploymentgroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.config.v1alpha2.Config.UpdateDeploymentGroup" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.deployments.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.deployments.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `config.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `config.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.config.v1alpha2.ConfigInternal.GetTerraformModuleMetadata`
  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
