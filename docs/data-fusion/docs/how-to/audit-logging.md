---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/audit-logging/
title: Cloud Data Fusion audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:58.297044+00:00
---

# Cloud Data Fusion audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Cloud Data Fusion audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Cloud Data Fusion. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Cloud Data Fusion audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="datafusion.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Data Fusion generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `datafusion.googleapis.com.AppLifecycleHttpHandler.getAllApps`  
`datafusion.googleapis.com.AppLifecycleHttpHandler.getAppInfo`  
`datafusion.googleapis.com.AppLifecycleHttpHandler.getPluginsInfo`  
`datafusion.googleapis.com.AppLifecycleHttpHandler.upgradeApplication`  
`datafusion.googleapis.com.ArtifactHttpHandler.getArtifactInfo`  
`datafusion.googleapis.com.ArtifactHttpHandler.getArtifactPlugin`  
`datafusion.googleapis.com.ArtifactHttpHandler.getArtifactPluginTypes`  
`datafusion.googleapis.com.ArtifactHttpHandler.getArtifactPlugins`  
`datafusion.googleapis.com.ArtifactHttpHandler.getArtifactProperties`  
`datafusion.googleapis.com.ArtifactHttpHandler.getArtifactVersions`  
`datafusion.googleapis.com.ArtifactHttpHandler.getArtifacts`  
`datafusion.googleapis.com.ArtifactHttpHandler.getProperties`  
`datafusion.googleapis.com.DatasetInstanceHandler.dropAll`  
`datafusion.googleapis.com.DatasetInstanceHandler.list`  
`datafusion.googleapis.com.DatasetTypeHandler.deleteModules`  
`datafusion.googleapis.com.MetadataHttpHandler.getTags`  
`datafusion.googleapis.com.MetadataHttpHandler.searchMetadata`  
`datafusion.googleapis.com.MetadataHttpHandler.searchNamespace`  
`datafusion.googleapis.com.MonitorHandler.getBootStatus`  
`datafusion.googleapis.com.MonitorHandler.getServiceSpec`  
`datafusion.googleapis.com.NamespaceHttpHandler.getNamespace`  
`datafusion.googleapis.com.PreferencesHttpHandler.getAppPrefs`  
`datafusion.googleapis.com.PreferencesHttpHandler.getInstancePrefs`  
`datafusion.googleapis.com.PreferencesHttpHandler.getNamespacePrefs`  
`datafusion.googleapis.com.ProgramLifecycleHttpHandler.batchNextRunTimes`  
`datafusion.googleapis.com.ProgramLifecycleHttpHandler.getProgramSchedules`  
`datafusion.googleapis.com.ProgramLifecycleHttpHandler.getProgramStatusSchedules`  
`datafusion.googleapis.com.ProgramLifecycleHttpHandler.getSchedule`  
`datafusion.googleapis.com.ProgramLifecycleHttpHandler.getStatus`  
`datafusion.googleapis.com.ProgramLifecycleHttpHandler.programHistory`  
`datafusion.googleapis.com.ProgramLifecycleHttpHandler.programHistoryVersioned`  
`datafusion.googleapis.com.SecureStoreHandler.get`  
`datafusion.googleapis.com.SecureStoreHandler.list`  
`datafusion.googleapis.com.SourceControlManagementHttpHandler.getRepository`  
`datafusion.googleapis.com.SourceControlManagementHttpHandler.listApplications`  
`datafusion.googleapis.com.SourceControlManagementHttpHandler.pushApp`  
`google.cloud.datafusion.v1.DataFusion.GetInstance`  
`google.cloud.datafusion.v1.DataFusion.ListAvailableVersions`  
`google.cloud.datafusion.v1.DataFusion.ListDnsPeerings`  
`google.cloud.datafusion.v1.DataFusion.ListInstances`  
`google.cloud.datafusion.v1beta1.DataFusion.GetInstance`  
`google.cloud.datafusion.v1beta1.DataFusion.ListAvailableVersions`  
`google.cloud.datafusion.v1beta1.DataFusion.ListDnsPeerings`  
`google.cloud.datafusion.v1beta1.DataFusion.ListInstances`  
`google.cloud.datafusion.v1beta1.DataFusion.ListNamespaces`  
`GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `datafusion.googleapis.com.AppLifecycleHttpHandler.deleteApp`  
`datafusion.googleapis.com.ArtifactHttpHandler.deleteArtifact`  
`datafusion.googleapis.com.ArtifactHttpHandler.writeProperties`  
`datafusion.googleapis.com.NamespaceHttpHandler.create`  
`datafusion.googleapis.com.NamespaceHttpHandler.delete`  
`datafusion.googleapis.com.PreferencesHttpHandler.setInstancePrefs`  
`datafusion.googleapis.com.PreferencesHttpHandler.setNamespacePrefs`  
`datafusion.googleapis.com.PreviewHttpHandler.getPreviewLogsNext`  
`datafusion.googleapis.com.PreviewHttpHandler.getPreviewLogsPrev`  
`datafusion.googleapis.com.PreviewHttpHandler.getStatus`  
`datafusion.googleapis.com.PreviewHttpHandler.getTracersData`  
`datafusion.googleapis.com.PreviewHttpHandler.start`  
`datafusion.googleapis.com.ProfileHttpHandler.deleteSystemProfile`  
`datafusion.googleapis.com.ProfileHttpHandler.disableProfile`  
`datafusion.googleapis.com.ProfileHttpHandler.disableSystemProfile`  
`datafusion.googleapis.com.ProfileHttpHandler.writeProfile`  
`datafusion.googleapis.com.ProfileHttpHandler.writeSystemProfile`  
`datafusion.googleapis.com.ProgramLifecycleHttpHandler.addSchedule`  
`datafusion.googleapis.com.ProgramLifecycleHttpHandler.performAction`  
`datafusion.googleapis.com.ProgramLifecycleHttpHandler.performRunLevelStop`  
`datafusion.googleapis.com.ProgramLifecycleHttpHandler.startPrograms`  
`datafusion.googleapis.com.SecureStoreHandler.create`  
`datafusion.googleapis.com.SecureStoreHandler.delete`  
`datafusion.googleapis.com.SourceControlManagementHttpHandler.deleteRepository`  
`datafusion.googleapis.com.SourceControlManagementHttpHandler.pullApp`  
`datafusion.googleapis.com.SourceControlManagementHttpHandler.setRepository`  
`google.cloud.datafusion.v1.DataFusion.CreateDnsPeering`  
`google.cloud.datafusion.v1.DataFusion.CreateInstance` (LRO)  
`google.cloud.datafusion.v1.DataFusion.DeleteDnsPeering`  
`google.cloud.datafusion.v1.DataFusion.DeleteInstance` (LRO)  
`google.cloud.datafusion.v1.DataFusion.RestartInstance` (LRO)  
`google.cloud.datafusion.v1.DataFusion.UpdateInstance` (LRO)  
`google.cloud.datafusion.v1beta1.DataFusion.CreateDnsPeering`  
`google.cloud.datafusion.v1beta1.DataFusion.CreateInstance` (LRO)  
`google.cloud.datafusion.v1beta1.DataFusion.DeleteDnsPeering`  
`google.cloud.datafusion.v1beta1.DataFusion.DeleteInstance` (LRO)  
`google.cloud.datafusion.v1beta1.DataFusion.RemoveIamPolicy`  
`google.cloud.datafusion.v1beta1.DataFusion.RestartInstance` (LRO)  
`google.cloud.datafusion.v1beta1.DataFusion.UpdateInstance` (LRO)  
`google.cloud.datafusion.v1beta1.DataFusion.UpgradeInstance` (LRO)  
`SetIamPolicy`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Data Fusion.

### `datafusion.googleapis.com.AppLifecycleHttpHandler`

The following audit logs are associated with methods belonging to `datafusion.googleapis.com.AppLifecycleHttpHandler`.

#### `deleteApp`

  * **Method** : `datafusion.googleapis.com.AppLifecycleHttpHandler.deleteApp`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
    * `datafusion.pipelines.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.AppLifecycleHttpHandler.deleteApp" `  




#### `getAllApps`

  * **Method** : `datafusion.googleapis.com.AppLifecycleHttpHandler.getAllApps`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
    * `datafusion.pipelines.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.AppLifecycleHttpHandler.getAllApps" `  




#### `getAppInfo`

  * **Method** : `datafusion.googleapis.com.AppLifecycleHttpHandler.getAppInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
    * `datafusion.pipelines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.AppLifecycleHttpHandler.getAppInfo" `  




#### `getPluginsInfo`

  * **Method** : `datafusion.googleapis.com.AppLifecycleHttpHandler.getPluginsInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.AppLifecycleHttpHandler.getPluginsInfo" `  




#### `upgradeApplication`

  * **Method** : `datafusion.googleapis.com.AppLifecycleHttpHandler.upgradeApplication`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.artifacts.list - ADMIN_READ`
    * `datafusion.namespaces.get - ADMIN_READ`
    * `datafusion.pipelines.create - ADMIN_WRITE`
    * `datafusion.pipelines.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.AppLifecycleHttpHandler.upgradeApplication" `  




### `datafusion.googleapis.com.ArtifactHttpHandler`

The following audit logs are associated with methods belonging to `datafusion.googleapis.com.ArtifactHttpHandler`.

#### `deleteArtifact`

  * **Method** : `datafusion.googleapis.com.ArtifactHttpHandler.deleteArtifact`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.artifacts.delete - ADMIN_WRITE`
    * `datafusion.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ArtifactHttpHandler.deleteArtifact" `  




#### `getArtifactInfo`

  * **Method** : `datafusion.googleapis.com.ArtifactHttpHandler.getArtifactInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.artifacts.get - ADMIN_READ`
    * `datafusion.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ArtifactHttpHandler.getArtifactInfo" `  




#### `getArtifactPlugin`

  * **Method** : `datafusion.googleapis.com.ArtifactHttpHandler.getArtifactPlugin`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ArtifactHttpHandler.getArtifactPlugin" `  




#### `getArtifactPluginTypes`

  * **Method** : `datafusion.googleapis.com.ArtifactHttpHandler.getArtifactPluginTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ArtifactHttpHandler.getArtifactPluginTypes" `  




#### `getArtifactPlugins`

  * **Method** : `datafusion.googleapis.com.ArtifactHttpHandler.getArtifactPlugins`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ArtifactHttpHandler.getArtifactPlugins" `  




#### `getArtifactProperties`

  * **Method** : `datafusion.googleapis.com.ArtifactHttpHandler.getArtifactProperties`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ArtifactHttpHandler.getArtifactProperties" `  




#### `getArtifactVersions`

  * **Method** : `datafusion.googleapis.com.ArtifactHttpHandler.getArtifactVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ArtifactHttpHandler.getArtifactVersions" `  




#### `getArtifacts`

  * **Method** : `datafusion.googleapis.com.ArtifactHttpHandler.getArtifacts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.artifacts.list - ADMIN_READ`
    * `datafusion.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ArtifactHttpHandler.getArtifacts" `  




#### `getProperties`

  * **Method** : `datafusion.googleapis.com.ArtifactHttpHandler.getProperties`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.artifacts.get - ADMIN_READ`
    * `datafusion.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ArtifactHttpHandler.getProperties" `  




#### `writeProperties`

  * **Method** : `datafusion.googleapis.com.ArtifactHttpHandler.writeProperties`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.artifacts.update - ADMIN_WRITE`
    * `datafusion.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ArtifactHttpHandler.writeProperties" `  




### `datafusion.googleapis.com.DatasetInstanceHandler`

The following audit logs are associated with methods belonging to `datafusion.googleapis.com.DatasetInstanceHandler`.

#### `dropAll`

  * **Method** : `datafusion.googleapis.com.DatasetInstanceHandler.dropAll`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.DatasetInstanceHandler.dropAll" `  




#### `list`

  * **Method** : `datafusion.googleapis.com.DatasetInstanceHandler.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.DatasetInstanceHandler.list" `  




### `datafusion.googleapis.com.DatasetTypeHandler`

The following audit logs are associated with methods belonging to `datafusion.googleapis.com.DatasetTypeHandler`.

#### `deleteModules`

  * **Method** : `datafusion.googleapis.com.DatasetTypeHandler.deleteModules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.DatasetTypeHandler.deleteModules" `  




### `datafusion.googleapis.com.MetadataHttpHandler`

The following audit logs are associated with methods belonging to `datafusion.googleapis.com.MetadataHttpHandler`.

#### `getTags`

  * **Method** : `datafusion.googleapis.com.MetadataHttpHandler.getTags`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.pipelines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.MetadataHttpHandler.getTags" `  




#### `searchMetadata`

  * **Method** : `datafusion.googleapis.com.MetadataHttpHandler.searchMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.pipelines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.MetadataHttpHandler.searchMetadata" `  




#### `searchNamespace`

  * **Method** : `datafusion.googleapis.com.MetadataHttpHandler.searchNamespace`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
    * `datafusion.pipelines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.MetadataHttpHandler.searchNamespace" `  




### `datafusion.googleapis.com.MonitorHandler`

The following audit logs are associated with methods belonging to `datafusion.googleapis.com.MonitorHandler`.

#### `getBootStatus`

  * **Method** : `datafusion.googleapis.com.MonitorHandler.getBootStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.MonitorHandler.getBootStatus" `  




#### `getServiceSpec`

  * **Method** : `datafusion.googleapis.com.MonitorHandler.getServiceSpec`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.MonitorHandler.getServiceSpec" `  




### `datafusion.googleapis.com.NamespaceHttpHandler`

The following audit logs are associated with methods belonging to `datafusion.googleapis.com.NamespaceHttpHandler`.

#### `create`

  * **Method** : `datafusion.googleapis.com.NamespaceHttpHandler.create`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.namespaces.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.NamespaceHttpHandler.create" `  




#### `delete`

  * **Method** : `datafusion.googleapis.com.NamespaceHttpHandler.delete`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.delete - ADMIN_WRITE`
    * `datafusion.namespaces.get - ADMIN_READ`
    * `datafusion.namespaces.updateRepositoryMetadata - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.NamespaceHttpHandler.delete" `  




#### `getNamespace`

  * **Method** : `datafusion.googleapis.com.NamespaceHttpHandler.getNamespace`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.NamespaceHttpHandler.getNamespace" `  




### `datafusion.googleapis.com.PreferencesHttpHandler`

The following audit logs are associated with methods belonging to `datafusion.googleapis.com.PreferencesHttpHandler`.

#### `getAppPrefs`

  * **Method** : `datafusion.googleapis.com.PreferencesHttpHandler.getAppPrefs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.pipelines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.PreferencesHttpHandler.getAppPrefs" `  




#### `getInstancePrefs`

  * **Method** : `datafusion.googleapis.com.PreferencesHttpHandler.getInstancePrefs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.PreferencesHttpHandler.getInstancePrefs" `  




#### `getNamespacePrefs`

  * **Method** : `datafusion.googleapis.com.PreferencesHttpHandler.getNamespacePrefs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.PreferencesHttpHandler.getNamespacePrefs" `  




#### `setInstancePrefs`

  * **Method** : `datafusion.googleapis.com.PreferencesHttpHandler.setInstancePrefs`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.PreferencesHttpHandler.setInstancePrefs" `  




#### `setNamespacePrefs`

  * **Method** : `datafusion.googleapis.com.PreferencesHttpHandler.setNamespacePrefs`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.namespaces.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.PreferencesHttpHandler.setNamespacePrefs" `  




### `datafusion.googleapis.com.PreviewHttpHandler`

The following audit logs are associated with methods belonging to `datafusion.googleapis.com.PreviewHttpHandler`.

#### `getPreviewLogsNext`

  * **Method** : `datafusion.googleapis.com.PreviewHttpHandler.getPreviewLogsNext`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.pipelines.preview - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.PreviewHttpHandler.getPreviewLogsNext" `  




#### `getPreviewLogsPrev`

  * **Method** : `datafusion.googleapis.com.PreviewHttpHandler.getPreviewLogsPrev`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.pipelines.preview - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.PreviewHttpHandler.getPreviewLogsPrev" `  




#### `getStatus`

  * **Method** : `datafusion.googleapis.com.PreviewHttpHandler.getStatus`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.pipelines.preview - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.PreviewHttpHandler.getStatus" `  




#### `getTracersData`

  * **Method** : `datafusion.googleapis.com.PreviewHttpHandler.getTracersData`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.pipelines.preview - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.PreviewHttpHandler.getTracersData" `  




#### `start`

  * **Method** : `datafusion.googleapis.com.PreviewHttpHandler.start`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.pipelines.preview - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.PreviewHttpHandler.start" `  




### `datafusion.googleapis.com.ProfileHttpHandler`

The following audit logs are associated with methods belonging to `datafusion.googleapis.com.ProfileHttpHandler`.

#### `deleteSystemProfile`

  * **Method** : `datafusion.googleapis.com.ProfileHttpHandler.deleteSystemProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.profiles.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ProfileHttpHandler.deleteSystemProfile" `  




#### `disableProfile`

  * **Method** : `datafusion.googleapis.com.ProfileHttpHandler.disableProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.profiles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ProfileHttpHandler.disableProfile" `  




#### `disableSystemProfile`

  * **Method** : `datafusion.googleapis.com.ProfileHttpHandler.disableSystemProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.profiles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ProfileHttpHandler.disableSystemProfile" `  




#### `writeProfile`

  * **Method** : `datafusion.googleapis.com.ProfileHttpHandler.writeProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.profiles.create - ADMIN_WRITE`
    * `datafusion.profiles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ProfileHttpHandler.writeProfile" `  




#### `writeSystemProfile`

  * **Method** : `datafusion.googleapis.com.ProfileHttpHandler.writeSystemProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.profiles.create - ADMIN_WRITE`
    * `datafusion.profiles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ProfileHttpHandler.writeSystemProfile" `  




### `datafusion.googleapis.com.ProgramLifecycleHttpHandler`

The following audit logs are associated with methods belonging to `datafusion.googleapis.com.ProgramLifecycleHttpHandler`.

#### `addSchedule`

  * **Method** : `datafusion.googleapis.com.ProgramLifecycleHttpHandler.addSchedule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.pipelines.execute - ADMIN_WRITE`
    * `datafusion.pipelines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ProgramLifecycleHttpHandler.addSchedule" `  




#### `batchNextRunTimes`

  * **Method** : `datafusion.googleapis.com.ProgramLifecycleHttpHandler.batchNextRunTimes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.pipelines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ProgramLifecycleHttpHandler.batchNextRunTimes" `  




#### `getProgramSchedules`

  * **Method** : `datafusion.googleapis.com.ProgramLifecycleHttpHandler.getProgramSchedules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.pipelines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ProgramLifecycleHttpHandler.getProgramSchedules" `  




#### `getProgramStatusSchedules`

  * **Method** : `datafusion.googleapis.com.ProgramLifecycleHttpHandler.getProgramStatusSchedules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.pipelines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ProgramLifecycleHttpHandler.getProgramStatusSchedules" `  




#### `getSchedule`

  * **Method** : `datafusion.googleapis.com.ProgramLifecycleHttpHandler.getSchedule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.pipelines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ProgramLifecycleHttpHandler.getSchedule" `  




#### `getStatus`

  * **Method** : `datafusion.googleapis.com.ProgramLifecycleHttpHandler.getStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.pipelines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ProgramLifecycleHttpHandler.getStatus" `  




#### `performAction`

  * **Method** : `datafusion.googleapis.com.ProgramLifecycleHttpHandler.performAction`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.pipelines.execute - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ProgramLifecycleHttpHandler.performAction" `  




#### `performRunLevelStop`

  * **Method** : `datafusion.googleapis.com.ProgramLifecycleHttpHandler.performRunLevelStop`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.pipelines.execute - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ProgramLifecycleHttpHandler.performRunLevelStop" `  




#### `programHistory`

  * **Method** : `datafusion.googleapis.com.ProgramLifecycleHttpHandler.programHistory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ProgramLifecycleHttpHandler.programHistory" `  




#### `programHistoryVersioned`

  * **Method** : `datafusion.googleapis.com.ProgramLifecycleHttpHandler.programHistoryVersioned`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.pipelines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ProgramLifecycleHttpHandler.programHistoryVersioned" `  




#### `startPrograms`

  * **Method** : `datafusion.googleapis.com.ProgramLifecycleHttpHandler.startPrograms`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.pipelines.execute - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.ProgramLifecycleHttpHandler.startPrograms" `  




### `datafusion.googleapis.com.SecureStoreHandler`

The following audit logs are associated with methods belonging to `datafusion.googleapis.com.SecureStoreHandler`.

#### `create`

  * **Method** : `datafusion.googleapis.com.SecureStoreHandler.create`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
    * `datafusion.secureKeys.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.SecureStoreHandler.create" `  




#### `delete`

  * **Method** : `datafusion.googleapis.com.SecureStoreHandler.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
    * `datafusion.secureKeys.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.SecureStoreHandler.delete" `  




#### `get`

  * **Method** : `datafusion.googleapis.com.SecureStoreHandler.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.SecureStoreHandler.get" `  




#### `list`

  * **Method** : `datafusion.googleapis.com.SecureStoreHandler.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.SecureStoreHandler.list" `  




### `datafusion.googleapis.com.SourceControlManagementHttpHandler`

The following audit logs are associated with methods belonging to `datafusion.googleapis.com.SourceControlManagementHttpHandler`.

#### `deleteRepository`

  * **Method** : `datafusion.googleapis.com.SourceControlManagementHttpHandler.deleteRepository`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.namespaces.updateRepositoryMetadata - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.SourceControlManagementHttpHandler.deleteRepository" `  




#### `getRepository`

  * **Method** : `datafusion.googleapis.com.SourceControlManagementHttpHandler.getRepository`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.SourceControlManagementHttpHandler.getRepository" `  




#### `listApplications`

  * **Method** : `datafusion.googleapis.com.SourceControlManagementHttpHandler.listApplications`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
    * `datafusion.namespaces.readRepository - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.SourceControlManagementHttpHandler.listApplications" `  




#### `pullApp`

  * **Method** : `datafusion.googleapis.com.SourceControlManagementHttpHandler.pullApp`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
    * `datafusion.namespaces.readRepository - ADMIN_READ`
    * `datafusion.pipelines.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.SourceControlManagementHttpHandler.pullApp" `  




#### `pushApp`

  * **Method** : `datafusion.googleapis.com.SourceControlManagementHttpHandler.pushApp`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
    * `datafusion.namespaces.writeRepository - ADMIN_WRITE`
    * `datafusion.pipelines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.SourceControlManagementHttpHandler.pushApp" `  




#### `setRepository`

  * **Method** : `datafusion.googleapis.com.SourceControlManagementHttpHandler.setRepository`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.namespaces.get - ADMIN_READ`
    * `datafusion.namespaces.updateRepositoryMetadata - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="datafusion.googleapis.com.SourceControlManagementHttpHandler.setRepository" `  




### `google.cloud.datafusion.v1.DataFusion`

The following audit logs are associated with methods belonging to `google.cloud.datafusion.v1.DataFusion`.

#### `CreateDnsPeering`

  * **Method** : `google.cloud.datafusion.v1.DataFusion.CreateDnsPeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1.DataFusion.CreateDnsPeering" `  




#### `CreateInstance`

  * **Method** : `google.cloud.datafusion.v1.DataFusion.CreateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1.DataFusion.CreateInstance" `  




#### `DeleteDnsPeering`

  * **Method** : `google.cloud.datafusion.v1.DataFusion.DeleteDnsPeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1.DataFusion.DeleteDnsPeering" `  




#### `DeleteInstance`

  * **Method** : `google.cloud.datafusion.v1.DataFusion.DeleteInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.instances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1.DataFusion.DeleteInstance" `  




#### `GetInstance`

  * **Method** : `google.cloud.datafusion.v1.DataFusion.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1.DataFusion.GetInstance" `  




#### `ListAvailableVersions`

  * **Method** : `google.cloud.datafusion.v1.DataFusion.ListAvailableVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1.DataFusion.ListAvailableVersions" `  




#### `ListDnsPeerings`

  * **Method** : `google.cloud.datafusion.v1.DataFusion.ListDnsPeerings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1.DataFusion.ListDnsPeerings" `  




#### `ListInstances`

  * **Method** : `google.cloud.datafusion.v1.DataFusion.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1.DataFusion.ListInstances" `  




#### `RestartInstance`

  * **Method** : `google.cloud.datafusion.v1.DataFusion.RestartInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.instances.restart - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1.DataFusion.RestartInstance" `  




#### `UpdateInstance`

  * **Method** : `google.cloud.datafusion.v1.DataFusion.UpdateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1.DataFusion.UpdateInstance" `  




### `google.cloud.datafusion.v1beta1.DataFusion`

The following audit logs are associated with methods belonging to `google.cloud.datafusion.v1beta1.DataFusion`.

#### `CreateDnsPeering`

  * **Method** : `google.cloud.datafusion.v1beta1.DataFusion.CreateDnsPeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1beta1.DataFusion.CreateDnsPeering" `  




#### `CreateInstance`

  * **Method** : `google.cloud.datafusion.v1beta1.DataFusion.CreateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1beta1.DataFusion.CreateInstance" `  




#### `DeleteDnsPeering`

  * **Method** : `google.cloud.datafusion.v1beta1.DataFusion.DeleteDnsPeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1beta1.DataFusion.DeleteDnsPeering" `  




#### `DeleteInstance`

  * **Method** : `google.cloud.datafusion.v1beta1.DataFusion.DeleteInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.instances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1beta1.DataFusion.DeleteInstance" `  




#### `GetInstance`

  * **Method** : `google.cloud.datafusion.v1beta1.DataFusion.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1beta1.DataFusion.GetInstance" `  




#### `ListAvailableVersions`

  * **Method** : `google.cloud.datafusion.v1beta1.DataFusion.ListAvailableVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1beta1.DataFusion.ListAvailableVersions" `  




#### `ListDnsPeerings`

  * **Method** : `google.cloud.datafusion.v1beta1.DataFusion.ListDnsPeerings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1beta1.DataFusion.ListDnsPeerings" `  




#### `ListInstances`

  * **Method** : `google.cloud.datafusion.v1beta1.DataFusion.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1beta1.DataFusion.ListInstances" `  




#### `ListNamespaces`

  * **Method** : `google.cloud.datafusion.v1beta1.DataFusion.ListNamespaces`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.namespaces.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1beta1.DataFusion.ListNamespaces" `  




#### `RemoveIamPolicy`

  * **Method** : `google.cloud.datafusion.v1beta1.DataFusion.RemoveIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.instances.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1beta1.DataFusion.RemoveIamPolicy" `  




#### `RestartInstance`

  * **Method** : `google.cloud.datafusion.v1beta1.DataFusion.RestartInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.instances.restart - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1beta1.DataFusion.RestartInstance" `  




#### `UpdateInstance`

  * **Method** : `google.cloud.datafusion.v1beta1.DataFusion.UpdateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.instances.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1beta1.DataFusion.UpdateInstance" `  




#### `UpgradeInstance`

  * **Method** : `google.cloud.datafusion.v1beta1.DataFusion.UpgradeInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.instances.upgrade - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datafusion.v1beta1.DataFusion.UpgradeInstance" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.instances.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.instances.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datafusion.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datafusion.operations.list - ADMIN_READ`
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
