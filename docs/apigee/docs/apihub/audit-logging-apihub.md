---
url: https://docs.cloud.google.com/apigee/docs/apihub/audit-logging-apihub/
title: Audit logging for API hub \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:47:42.388964+00:00
---

# Audit logging for API hub  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/audit-logging-apihub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Audit logging for API hub Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This document describes audit logging for API hub. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

API hub audit logs use the service name `apihub.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="apihub.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, API hub generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.apihub.v1.ApiHubPlugin.GetPlugin`  
`google.cloud.apihub.v1.Provisioning.LookupApiHubInstance`  
`google.cloud.apihub.v1.RuntimeProjectAttachmentService.ListRuntimeProjectAttachments`  
`google.cloud.apihub.v1.RuntimeProjectAttachmentService.LookupRuntimeProjectAttachment`  
`ADMIN_WRITE` | `google.cloud.apihub.v1.ApiHubPlugin.DisablePlugin`  
`google.cloud.apihub.v1.ApiHubPlugin.EnablePlugin`  
`google.cloud.apihub.v1.HostProjectRegistrationService.CreateHostProjectRegistration`  
`google.cloud.apihub.v1.Provisioning.CreateApiHubInstance` (LRO)  
`google.cloud.apihub.v1.RuntimeProjectAttachmentService.CreateRuntimeProjectAttachment`  
`DATA_READ` | `google.cloud.apihub.v1.ApiHub.GetApi`  
`google.cloud.apihub.v1.ApiHub.GetAttribute`  
`google.cloud.apihub.v1.ApiHub.GetDeployment`  
`google.cloud.apihub.v1.ApiHub.GetExternalApi`  
`google.cloud.apihub.v1.ApiHub.GetSpec`  
`google.cloud.apihub.v1.ApiHub.GetSpecContents`  
`google.cloud.apihub.v1.ApiHub.GetVersion`  
`google.cloud.apihub.v1.ApiHub.ListApis`  
`google.cloud.apihub.v1.ApiHub.ListAttributes`  
`google.cloud.apihub.v1.ApiHub.ListDeployments`  
`google.cloud.apihub.v1.ApiHub.ListExternalApis`  
`google.cloud.apihub.v1.ApiHub.ListSpecs`  
`google.cloud.apihub.v1.ApiHub.ListVersions`  
`DATA_WRITE` | `google.cloud.apihub.v1.ApiHub.CreateApi`  
`google.cloud.apihub.v1.ApiHub.CreateAttribute`  
`google.cloud.apihub.v1.ApiHub.CreateDeployment`  
`google.cloud.apihub.v1.ApiHub.CreateExternalApi`  
`google.cloud.apihub.v1.ApiHub.CreateSpec`  
`google.cloud.apihub.v1.ApiHub.CreateVersion`  
`google.cloud.apihub.v1.ApiHub.DeleteApi`  
`google.cloud.apihub.v1.ApiHub.DeleteAttribute`  
`google.cloud.apihub.v1.ApiHub.DeleteDeployment`  
`google.cloud.apihub.v1.ApiHub.DeleteExternalApi`  
`google.cloud.apihub.v1.ApiHub.DeleteSpec`  
`google.cloud.apihub.v1.ApiHub.DeleteVersion`  
`google.cloud.apihub.v1.ApiHub.UpdateApi`  
`google.cloud.apihub.v1.ApiHub.UpdateAttribute`  
`google.cloud.apihub.v1.ApiHub.UpdateDeployment`  
`google.cloud.apihub.v1.ApiHub.UpdateExternalApi`  
`google.cloud.apihub.v1.ApiHub.UpdateSpec`  
`google.cloud.apihub.v1.ApiHub.UpdateVersion`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for API hub.

### `google.cloud.apihub.v1.ApiHub`

The following audit logs are associated with methods belonging to `google.cloud.apihub.v1.ApiHub`.

#### `CreateApi`

  * **Method** : `google.cloud.apihub.v1.ApiHub.CreateApi`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.apis.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.CreateApi" `  




#### `CreateAttribute`

  * **Method** : `google.cloud.apihub.v1.ApiHub.CreateAttribute`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.attributes.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.CreateAttribute" `  




#### `CreateDeployment`

  * **Method** : `google.cloud.apihub.v1.ApiHub.CreateDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.deployments.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.CreateDeployment" `  




#### `CreateExternalApi`

  * **Method** : `google.cloud.apihub.v1.ApiHub.CreateExternalApi`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.externalApis.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.CreateExternalApi" `  




#### `CreateSpec`

  * **Method** : `google.cloud.apihub.v1.ApiHub.CreateSpec`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.specs.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.CreateSpec" `  




#### `CreateVersion`

  * **Method** : `google.cloud.apihub.v1.ApiHub.CreateVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.versions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.CreateVersion" `  




#### `DeleteApi`

  * **Method** : `google.cloud.apihub.v1.ApiHub.DeleteApi`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.apis.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.DeleteApi" `  




#### `DeleteAttribute`

  * **Method** : `google.cloud.apihub.v1.ApiHub.DeleteAttribute`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.attributes.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.DeleteAttribute" `  




#### `DeleteDeployment`

  * **Method** : `google.cloud.apihub.v1.ApiHub.DeleteDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.deployments.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.DeleteDeployment" `  




#### `DeleteExternalApi`

  * **Method** : `google.cloud.apihub.v1.ApiHub.DeleteExternalApi`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.externalApis.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.DeleteExternalApi" `  




#### `DeleteSpec`

  * **Method** : `google.cloud.apihub.v1.ApiHub.DeleteSpec`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.specs.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.DeleteSpec" `  




#### `DeleteVersion`

  * **Method** : `google.cloud.apihub.v1.ApiHub.DeleteVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.versions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.DeleteVersion" `  




#### `GetApi`

  * **Method** : `google.cloud.apihub.v1.ApiHub.GetApi`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.apis.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.GetApi" `  




#### `GetAttribute`

  * **Method** : `google.cloud.apihub.v1.ApiHub.GetAttribute`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.attributes.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.GetAttribute" `  




#### `GetDeployment`

  * **Method** : `google.cloud.apihub.v1.ApiHub.GetDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.deployments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.GetDeployment" `  




#### `GetExternalApi`

  * **Method** : `google.cloud.apihub.v1.ApiHub.GetExternalApi`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.externalApis.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.GetExternalApi" `  




#### `GetSpec`

  * **Method** : `google.cloud.apihub.v1.ApiHub.GetSpec`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.specs.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.GetSpec" `  




#### `GetSpecContents`

  * **Method** : `google.cloud.apihub.v1.ApiHub.GetSpecContents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.specs.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.GetSpecContents" `  




#### `GetVersion`

  * **Method** : `google.cloud.apihub.v1.ApiHub.GetVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.versions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.GetVersion" `  




#### `ListApis`

  * **Method** : `google.cloud.apihub.v1.ApiHub.ListApis`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.apis.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.ListApis" `  




#### `ListAttributes`

  * **Method** : `google.cloud.apihub.v1.ApiHub.ListAttributes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.attributes.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.ListAttributes" `  




#### `ListDeployments`

  * **Method** : `google.cloud.apihub.v1.ApiHub.ListDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.deployments.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.ListDeployments" `  




#### `ListExternalApis`

  * **Method** : `google.cloud.apihub.v1.ApiHub.ListExternalApis`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.externalApis.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.ListExternalApis" `  




#### `ListSpecs`

  * **Method** : `google.cloud.apihub.v1.ApiHub.ListSpecs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.specs.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.ListSpecs" `  




#### `ListVersions`

  * **Method** : `google.cloud.apihub.v1.ApiHub.ListVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.versions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.ListVersions" `  




#### `UpdateApi`

  * **Method** : `google.cloud.apihub.v1.ApiHub.UpdateApi`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.apis.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.UpdateApi" `  




#### `UpdateAttribute`

  * **Method** : `google.cloud.apihub.v1.ApiHub.UpdateAttribute`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.attributes.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.UpdateAttribute" `  




#### `UpdateDeployment`

  * **Method** : `google.cloud.apihub.v1.ApiHub.UpdateDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.deployments.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.UpdateDeployment" `  




#### `UpdateExternalApi`

  * **Method** : `google.cloud.apihub.v1.ApiHub.UpdateExternalApi`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.externalApis.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.UpdateExternalApi" `  




#### `UpdateSpec`

  * **Method** : `google.cloud.apihub.v1.ApiHub.UpdateSpec`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.specs.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.UpdateSpec" `  




#### `UpdateVersion`

  * **Method** : `google.cloud.apihub.v1.ApiHub.UpdateVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.versions.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHub.UpdateVersion" `  




### `google.cloud.apihub.v1.ApiHubPlugin`

The following audit logs are associated with methods belonging to `google.cloud.apihub.v1.ApiHubPlugin`.

#### `DisablePlugin`

  * **Method** : `google.cloud.apihub.v1.ApiHubPlugin.DisablePlugin`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apihub.plugins.disable - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHubPlugin.DisablePlugin" `  




#### `EnablePlugin`

  * **Method** : `google.cloud.apihub.v1.ApiHubPlugin.EnablePlugin`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apihub.plugins.enable - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHubPlugin.EnablePlugin" `  




#### `GetPlugin`

  * **Method** : `google.cloud.apihub.v1.ApiHubPlugin.GetPlugin`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.plugins.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.ApiHubPlugin.GetPlugin" `  




### `google.cloud.apihub.v1.HostProjectRegistrationService`

The following audit logs are associated with methods belonging to `google.cloud.apihub.v1.HostProjectRegistrationService`.

#### `CreateHostProjectRegistration`

  * **Method** : `google.cloud.apihub.v1.HostProjectRegistrationService.CreateHostProjectRegistration`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apihub.runTimeProjectAttachments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.HostProjectRegistrationService.CreateHostProjectRegistration" `  




### `google.cloud.apihub.v1.Provisioning`

The following audit logs are associated with methods belonging to `google.cloud.apihub.v1.Provisioning`.

#### `CreateApiHubInstance`

  * **Method** : `google.cloud.apihub.v1.Provisioning.CreateApiHubInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apihub.apiHubInstances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.Provisioning.CreateApiHubInstance" `  




#### `LookupApiHubInstance`

  * **Method** : `google.cloud.apihub.v1.Provisioning.LookupApiHubInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.apiHubInstances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.Provisioning.LookupApiHubInstance" `  




### `google.cloud.apihub.v1.RuntimeProjectAttachmentService`

The following audit logs are associated with methods belonging to `google.cloud.apihub.v1.RuntimeProjectAttachmentService`.

#### `CreateRuntimeProjectAttachment`

  * **Method** : `google.cloud.apihub.v1.RuntimeProjectAttachmentService.CreateRuntimeProjectAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apihub.runTimeProjectAttachments.attach - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.RuntimeProjectAttachmentService.CreateRuntimeProjectAttachment" `  




#### `ListRuntimeProjectAttachments`

  * **Method** : `google.cloud.apihub.v1.RuntimeProjectAttachmentService.ListRuntimeProjectAttachments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.runTimeProjectAttachments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.RuntimeProjectAttachmentService.ListRuntimeProjectAttachments" `  




#### `LookupRuntimeProjectAttachment`

  * **Method** : `google.cloud.apihub.v1.RuntimeProjectAttachmentService.LookupRuntimeProjectAttachment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apihub.runTimeProjectAttachments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apihub.v1.RuntimeProjectAttachmentService.LookupRuntimeProjectAttachment" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
