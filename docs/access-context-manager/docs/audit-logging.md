---
url: https://docs.cloud.google.com/access-context-manager/docs/audit-logging/
title: Access Context Manager audit logging information \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:05.332751+00:00
---

# Access Context Manager audit logging information  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Access Context Manager audit logging information Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Access Context Manager. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Access Context Manager audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="accesscontextmanager.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Access Context Manager generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.identity.accesscontextmanager.v1.AccessContextManager.GetAccessLevel`  
`google.identity.accesscontextmanager.v1.AccessContextManager.GetAccessPolicy`  
`google.identity.accesscontextmanager.v1.AccessContextManager.GetAuthorizedOrgsDesc`  
`google.identity.accesscontextmanager.v1.AccessContextManager.GetGcpUserAccessBinding`  
`google.identity.accesscontextmanager.v1.AccessContextManager.GetIamPolicy`  
`google.identity.accesscontextmanager.v1.AccessContextManager.GetServicePerimeter`  
`google.identity.accesscontextmanager.v1.AccessContextManager.ListAccessLevels`  
`google.identity.accesscontextmanager.v1.AccessContextManager.ListAccessPolicies`  
`google.identity.accesscontextmanager.v1.AccessContextManager.ListAuthorizedOrgsDescs`  
`google.identity.accesscontextmanager.v1.AccessContextManager.ListGcpUserAccessBindings`  
`google.identity.accesscontextmanager.v1.AccessContextManager.ListServicePerimeters`  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.GetAccessLevel`  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.GetAccessPolicy`  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.GetAuthorizedOrgsDesc`  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.GetGcpUserAccessBinding`  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.GetServicePerimeter`  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.ListAccessLevels`  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.ListAccessPolicies`  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.ListGcpUserAccessBindings`  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.ListServicePerimeters`  
`google.longrunning.Operations.GetOperation`  
`ADMIN_WRITE` | `google.identity.accesscontextmanager.v1.AccessContextManager.CommitServicePerimeters` (LRO)  
`google.identity.accesscontextmanager.v1.AccessContextManager.CreateAccessLevel` (LRO)  
`google.identity.accesscontextmanager.v1.AccessContextManager.CreateAccessPolicy` (LRO)  
`google.identity.accesscontextmanager.v1.AccessContextManager.CreateAuthorizedOrgsDesc` (LRO)  
`google.identity.accesscontextmanager.v1.AccessContextManager.CreateGcpUserAccessBinding`  
`google.identity.accesscontextmanager.v1.AccessContextManager.CreateServicePerimeter` (LRO)  
`google.identity.accesscontextmanager.v1.AccessContextManager.DeleteAccessLevel` (LRO)  
`google.identity.accesscontextmanager.v1.AccessContextManager.DeleteAccessPolicy` (LRO)  
`google.identity.accesscontextmanager.v1.AccessContextManager.DeleteAuthorizedOrgsDesc` (LRO)  
`google.identity.accesscontextmanager.v1.AccessContextManager.DeleteGcpUserAccessBinding`  
`google.identity.accesscontextmanager.v1.AccessContextManager.DeleteServicePerimeter` (LRO)  
`google.identity.accesscontextmanager.v1.AccessContextManager.ReplaceAccessLevels` (LRO)  
`google.identity.accesscontextmanager.v1.AccessContextManager.ReplaceServicePerimeters` (LRO)  
`google.identity.accesscontextmanager.v1.AccessContextManager.SetIamPolicy`  
`google.identity.accesscontextmanager.v1.AccessContextManager.UpdateAccessLevel` (LRO)  
`google.identity.accesscontextmanager.v1.AccessContextManager.UpdateAccessPolicy` (LRO)  
`google.identity.accesscontextmanager.v1.AccessContextManager.UpdateAuthorizedOrgsDesc` (LRO)  
`google.identity.accesscontextmanager.v1.AccessContextManager.UpdateGcpUserAccessBinding`  
`google.identity.accesscontextmanager.v1.AccessContextManager.UpdateServicePerimeter` (LRO)  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.CommitServicePerimeters` (LRO)  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.CreateAccessLevel` (LRO)  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.CreateAccessPolicy` (LRO)  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.CreateAuthorizedOrgsDesc` (LRO)  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.CreateGcpUserAccessBinding`  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.CreateServicePerimeter` (LRO)  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.DeleteAccessLevel` (LRO)  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.DeleteAccessPolicy` (LRO)  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.DeleteAuthorizedOrgsDesc` (LRO)  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.DeleteGcpUserAccessBinding`  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.DeleteServicePerimeter` (LRO)  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.ReplaceAccessLevels` (LRO)  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.ReplaceServicePerimeters` (LRO)  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.SetIamPolicy`  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.UpdateAccessLevel` (LRO)  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.UpdateAccessPolicy` (LRO)  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.UpdateAuthorizedOrgsDesc` (LRO)  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.UpdateGcpUserAccessBinding`  
`google.identity.accesscontextmanager.v1alpha.AccessContextManager.UpdateServicePerimeter` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Access Context Manager.

### `google.identity.accesscontextmanager.v1.AccessContextManager`

The following audit logs are associated with methods belonging to `google.identity.accesscontextmanager.v1.AccessContextManager`.

#### `CommitServicePerimeters`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.CommitServicePerimeters`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.servicePerimeters.commit - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.CommitServicePerimeters" `  




#### `CreateAccessLevel`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.CreateAccessLevel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.accessLevels.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.CreateAccessLevel" `  




#### `CreateAccessPolicy`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.CreateAccessPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.policies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.CreateAccessPolicy" `  




#### `CreateAuthorizedOrgsDesc`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.CreateAuthorizedOrgsDesc`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.authorizedOrgsDescs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.CreateAuthorizedOrgsDesc" `  




#### `CreateGcpUserAccessBinding`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.CreateGcpUserAccessBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.gcpUserAccessBindings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.CreateGcpUserAccessBinding" `  




#### `CreateServicePerimeter`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.CreateServicePerimeter`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.servicePerimeters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.CreateServicePerimeter" `  




#### `DeleteAccessLevel`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.DeleteAccessLevel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.accessLevels.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.DeleteAccessLevel" `  




#### `DeleteAccessPolicy`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.DeleteAccessPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.policies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.DeleteAccessPolicy" `  




#### `DeleteAuthorizedOrgsDesc`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.DeleteAuthorizedOrgsDesc`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.authorizedOrgsDescs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.DeleteAuthorizedOrgsDesc" `  




#### `DeleteGcpUserAccessBinding`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.DeleteGcpUserAccessBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.gcpUserAccessBindings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.DeleteGcpUserAccessBinding" `  




#### `DeleteServicePerimeter`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.DeleteServicePerimeter`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.servicePerimeters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.DeleteServicePerimeter" `  




#### `GetAccessLevel`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.GetAccessLevel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.accessLevels.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.GetAccessLevel" `  




#### `GetAccessPolicy`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.GetAccessPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.policies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.GetAccessPolicy" `  




#### `GetAuthorizedOrgsDesc`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.GetAuthorizedOrgsDesc`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.authorizedOrgsDescs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.GetAuthorizedOrgsDesc" `  




#### `GetGcpUserAccessBinding`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.GetGcpUserAccessBinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.gcpUserAccessBindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.GetGcpUserAccessBinding" `  




#### `GetIamPolicy`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.policies.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.GetIamPolicy" `  




#### `GetServicePerimeter`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.GetServicePerimeter`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.servicePerimeters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.GetServicePerimeter" `  




#### `ListAccessLevels`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.ListAccessLevels`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.accessLevels.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.ListAccessLevels" `  




#### `ListAccessPolicies`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.ListAccessPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.policies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.ListAccessPolicies" `  




#### `ListAuthorizedOrgsDescs`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.ListAuthorizedOrgsDescs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.authorizedOrgsDescs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.ListAuthorizedOrgsDescs" `  




#### `ListGcpUserAccessBindings`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.ListGcpUserAccessBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.gcpUserAccessBindings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.ListGcpUserAccessBindings" `  




#### `ListServicePerimeters`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.ListServicePerimeters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.servicePerimeters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.ListServicePerimeters" `  




#### `ReplaceAccessLevels`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.ReplaceAccessLevels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.accessLevels.replaceAll - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.ReplaceAccessLevels" `  




#### `ReplaceServicePerimeters`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.ReplaceServicePerimeters`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.servicePerimeters.replaceAll - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.ReplaceServicePerimeters" `  




#### `SetIamPolicy`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.policies.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.SetIamPolicy" `  




#### `UpdateAccessLevel`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.UpdateAccessLevel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.accessLevels.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.UpdateAccessLevel" `  




#### `UpdateAccessPolicy`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.UpdateAccessPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.policies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.UpdateAccessPolicy" `  




#### `UpdateAuthorizedOrgsDesc`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.UpdateAuthorizedOrgsDesc`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.authorizedOrgsDescs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.UpdateAuthorizedOrgsDesc" `  




#### `UpdateGcpUserAccessBinding`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.UpdateGcpUserAccessBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.gcpUserAccessBindings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.UpdateGcpUserAccessBinding" `  




#### `UpdateServicePerimeter`

  * **Method** : `google.identity.accesscontextmanager.v1.AccessContextManager.UpdateServicePerimeter`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.servicePerimeters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1.AccessContextManager.UpdateServicePerimeter" `  




### `google.identity.accesscontextmanager.v1alpha.AccessContextManager`

The following audit logs are associated with methods belonging to `google.identity.accesscontextmanager.v1alpha.AccessContextManager`.

#### `CommitServicePerimeters`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.CommitServicePerimeters`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.servicePerimeters.commit - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.CommitServicePerimeters" `  




#### `CreateAccessLevel`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.CreateAccessLevel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.accessLevels.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.CreateAccessLevel" `  




#### `CreateAccessPolicy`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.CreateAccessPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.policies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.CreateAccessPolicy" `  




#### `CreateAuthorizedOrgsDesc`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.CreateAuthorizedOrgsDesc`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.authorizedOrgsDescs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.CreateAuthorizedOrgsDesc" `  




#### `CreateGcpUserAccessBinding`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.CreateGcpUserAccessBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.gcpUserAccessBindings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.CreateGcpUserAccessBinding" `  




#### `CreateServicePerimeter`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.CreateServicePerimeter`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.servicePerimeters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.CreateServicePerimeter" `  




#### `DeleteAccessLevel`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.DeleteAccessLevel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.accessLevels.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.DeleteAccessLevel" `  




#### `DeleteAccessPolicy`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.DeleteAccessPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.policies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.DeleteAccessPolicy" `  




#### `DeleteAuthorizedOrgsDesc`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.DeleteAuthorizedOrgsDesc`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.authorizedOrgsDescs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.DeleteAuthorizedOrgsDesc" `  




#### `DeleteGcpUserAccessBinding`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.DeleteGcpUserAccessBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.gcpUserAccessBindings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.DeleteGcpUserAccessBinding" `  




#### `DeleteServicePerimeter`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.DeleteServicePerimeter`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.servicePerimeters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.DeleteServicePerimeter" `  




#### `GetAccessLevel`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.GetAccessLevel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.accessLevels.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.GetAccessLevel" `  




#### `GetAccessPolicy`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.GetAccessPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.policies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.GetAccessPolicy" `  




#### `GetAuthorizedOrgsDesc`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.GetAuthorizedOrgsDesc`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.authorizedOrgsDescs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.GetAuthorizedOrgsDesc" `  




#### `GetGcpUserAccessBinding`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.GetGcpUserAccessBinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.gcpUserAccessBindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.GetGcpUserAccessBinding" `  




#### `GetServicePerimeter`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.GetServicePerimeter`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.servicePerimeters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.GetServicePerimeter" `  




#### `ListAccessLevels`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.ListAccessLevels`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.accessLevels.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.ListAccessLevels" `  




#### `ListAccessPolicies`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.ListAccessPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.policies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.ListAccessPolicies" `  




#### `ListGcpUserAccessBindings`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.ListGcpUserAccessBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.gcpUserAccessBindings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.ListGcpUserAccessBindings" `  




#### `ListServicePerimeters`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.ListServicePerimeters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.servicePerimeters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.ListServicePerimeters" `  




#### `ReplaceAccessLevels`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.ReplaceAccessLevels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.accessLevels.replaceAll - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.ReplaceAccessLevels" `  




#### `ReplaceServicePerimeters`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.ReplaceServicePerimeters`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.servicePerimeters.replaceAll - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.ReplaceServicePerimeters" `  




#### `SetIamPolicy`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.policies.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.SetIamPolicy" `  




#### `UpdateAccessLevel`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.UpdateAccessLevel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.accessLevels.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.UpdateAccessLevel" `  




#### `UpdateAccessPolicy`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.UpdateAccessPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.policies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.UpdateAccessPolicy" `  




#### `UpdateAuthorizedOrgsDesc`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.UpdateAuthorizedOrgsDesc`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.authorizedOrgsDescs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.UpdateAuthorizedOrgsDesc" `  




#### `UpdateGcpUserAccessBinding`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.UpdateGcpUserAccessBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.gcpUserAccessBindings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.UpdateGcpUserAccessBinding" `  




#### `UpdateServicePerimeter`

  * **Method** : `google.identity.accesscontextmanager.v1alpha.AccessContextManager.UpdateServicePerimeter`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accesscontextmanager.servicePerimeters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.identity.accesscontextmanager.v1alpha.AccessContextManager.UpdateServicePerimeter" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `accesscontextmanager.accessLevels.get - ADMIN_READ`
    * `accesscontextmanager.authorizedOrgsDescs.get - ADMIN_READ`
    * `accesscontextmanager.policies.get - ADMIN_READ`
    * `accesscontextmanager.servicePerimeters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.identity.accesscontextmanager.v1.AccessContextManager.GetSupportedService`
  * `google.identity.accesscontextmanager.v1.AccessContextManager.ListSupportedPermissions`
  * `google.identity.accesscontextmanager.v1.AccessContextManager.ListSupportedServices`
  * `google.identity.accesscontextmanager.v1.AccessContextManager.TestIamPermissions`
  * `google.identity.accesscontextmanager.v1alpha.AccessContextManager.GetSupportedService`
  * `google.identity.accesscontextmanager.v1alpha.AccessContextManager.ListSupportedPermissions`
  * `google.identity.accesscontextmanager.v1alpha.AccessContextManager.ListSupportedServices`
  * `google.identity.accesscontextmanager.v1alpha.AccessContextManager.TestIamPermissions`
  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.DeleteOperation`
  * `google.longrunning.Operations.ListOperations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
