---
url: https://docs.cloud.google.com/app-hub/docs/audit-logging/
title: App Hub audit logs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:17.296913+00:00
---

# App Hub audit logs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Guides ](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

#  App Hub audit logs Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for App Hub. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the App Hub audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="apphub.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, App Hub generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.apphub.v1.AppHub.GetApplication`  
`google.cloud.apphub.v1.AppHub.GetDiscoveredService`  
`google.cloud.apphub.v1.AppHub.GetDiscoveredWorkload`  
`google.cloud.apphub.v1.AppHub.GetExtendedMetadataSchema`  
`google.cloud.apphub.v1.AppHub.GetService`  
`google.cloud.apphub.v1.AppHub.GetServiceProjectAttachment`  
`google.cloud.apphub.v1.AppHub.GetWorkload`  
`google.cloud.apphub.v1.AppHub.ListApplications`  
`google.cloud.apphub.v1.AppHub.ListDiscoveredServices`  
`google.cloud.apphub.v1.AppHub.ListDiscoveredWorkloads`  
`google.cloud.apphub.v1.AppHub.ListExtendedMetadataSchemas`  
`google.cloud.apphub.v1.AppHub.ListServiceProjectAttachments`  
`google.cloud.apphub.v1.AppHub.ListServices`  
`google.cloud.apphub.v1.AppHub.ListWorkloads`  
`google.cloud.apphub.v1.AppHub.LookupDiscoveredService`  
`google.cloud.apphub.v1.AppHub.LookupDiscoveredWorkload`  
`google.cloud.apphub.v1.AppHub.LookupServiceProjectAttachment`  
`google.cloud.apphub.v1alpha.AppHub.FindUnregisteredServices`  
`google.cloud.apphub.v1alpha.AppHub.FindUnregisteredWorkloads`  
`google.cloud.apphub.v1alpha.AppHub.GetApplication`  
`google.cloud.apphub.v1alpha.AppHub.GetDiscoveredService`  
`google.cloud.apphub.v1alpha.AppHub.GetDiscoveredWorkload`  
`google.cloud.apphub.v1alpha.AppHub.GetExtendedMetadataSchema`  
`google.cloud.apphub.v1alpha.AppHub.GetService`  
`google.cloud.apphub.v1alpha.AppHub.GetServiceProjectAttachment`  
`google.cloud.apphub.v1alpha.AppHub.GetWorkload`  
`google.cloud.apphub.v1alpha.AppHub.ListApplications`  
`google.cloud.apphub.v1alpha.AppHub.ListDiscoveredServices`  
`google.cloud.apphub.v1alpha.AppHub.ListDiscoveredWorkloads`  
`google.cloud.apphub.v1alpha.AppHub.ListExtendedMetadataSchemas`  
`google.cloud.apphub.v1alpha.AppHub.ListServiceProjectAttachments`  
`google.cloud.apphub.v1alpha.AppHub.ListServices`  
`google.cloud.apphub.v1alpha.AppHub.ListWorkloads`  
`google.cloud.apphub.v1alpha.AppHub.LookupDiscoveredService`  
`google.cloud.apphub.v1alpha.AppHub.LookupDiscoveredWorkload`  
`google.cloud.apphub.v1alpha.AppHub.LookupServiceProjectAttachment`  
`GetIamPolicy`  
`ADMIN_WRITE` | `google.cloud.apphub.v1.AppHub.CreateApplication` (LRO)  
`google.cloud.apphub.v1.AppHub.CreateService` (LRO)  
`google.cloud.apphub.v1.AppHub.CreateServiceProjectAttachment` (LRO)  
`google.cloud.apphub.v1.AppHub.CreateWorkload` (LRO)  
`google.cloud.apphub.v1.AppHub.DeleteApplication` (LRO)  
`google.cloud.apphub.v1.AppHub.DeleteService` (LRO)  
`google.cloud.apphub.v1.AppHub.DeleteServiceProjectAttachment` (LRO)  
`google.cloud.apphub.v1.AppHub.DeleteWorkload` (LRO)  
`google.cloud.apphub.v1.AppHub.DetachServiceProjectAttachment`  
`google.cloud.apphub.v1.AppHub.UpdateApplication` (LRO)  
`google.cloud.apphub.v1.AppHub.UpdateService` (LRO)  
`google.cloud.apphub.v1.AppHub.UpdateWorkload` (LRO)  
`google.cloud.apphub.v1alpha.AppHub.CreateApplication` (LRO)  
`google.cloud.apphub.v1alpha.AppHub.CreateService` (LRO)  
`google.cloud.apphub.v1alpha.AppHub.CreateServiceProjectAttachment` (LRO)  
`google.cloud.apphub.v1alpha.AppHub.CreateWorkload` (LRO)  
`google.cloud.apphub.v1alpha.AppHub.DeleteApplication` (LRO)  
`google.cloud.apphub.v1alpha.AppHub.DeleteService` (LRO)  
`google.cloud.apphub.v1alpha.AppHub.DeleteServiceProjectAttachment` (LRO)  
`google.cloud.apphub.v1alpha.AppHub.DeleteWorkload` (LRO)  
`google.cloud.apphub.v1alpha.AppHub.DetachServiceProjectAttachment`  
`google.cloud.apphub.v1alpha.AppHub.UpdateApplication` (LRO)  
`google.cloud.apphub.v1alpha.AppHub.UpdateService` (LRO)  
`google.cloud.apphub.v1alpha.AppHub.UpdateWorkload` (LRO)  
`SetIamPolicy`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for App Hub.

### `google.cloud.apphub.v1.AppHub`

The following audit logs are associated with methods belonging to `google.cloud.apphub.v1.AppHub`.

#### `CreateApplication`

  * **Method** : `google.cloud.apphub.v1.AppHub.CreateApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.applications.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.CreateApplication" `  




#### `CreateService`

  * **Method** : `google.cloud.apphub.v1.AppHub.CreateService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.discoveredServices.register - ADMIN_WRITE`
    * `apphub.services.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.CreateService" `  




#### `CreateServiceProjectAttachment`

  * **Method** : `google.cloud.apphub.v1.AppHub.CreateServiceProjectAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.serviceProjectAttachments.attach - ADMIN_WRITE`
    * `apphub.serviceProjectAttachments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.CreateServiceProjectAttachment" `  




#### `CreateWorkload`

  * **Method** : `google.cloud.apphub.v1.AppHub.CreateWorkload`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.discoveredWorkloads.register - ADMIN_WRITE`
    * `apphub.workloads.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.CreateWorkload" `  




#### `DeleteApplication`

  * **Method** : `google.cloud.apphub.v1.AppHub.DeleteApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.applications.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.DeleteApplication" `  




#### `DeleteService`

  * **Method** : `google.cloud.apphub.v1.AppHub.DeleteService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.services.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.DeleteService" `  




#### `DeleteServiceProjectAttachment`

  * **Method** : `google.cloud.apphub.v1.AppHub.DeleteServiceProjectAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.serviceProjectAttachments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.DeleteServiceProjectAttachment" `  




#### `DeleteWorkload`

  * **Method** : `google.cloud.apphub.v1.AppHub.DeleteWorkload`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.workloads.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.DeleteWorkload" `  




#### `DetachServiceProjectAttachment`

  * **Method** : `google.cloud.apphub.v1.AppHub.DetachServiceProjectAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.serviceProjectAttachments.detach - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.DetachServiceProjectAttachment" `  




#### `GetApplication`

  * **Method** : `google.cloud.apphub.v1.AppHub.GetApplication`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.applications.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.GetApplication" `  




#### `GetDiscoveredService`

  * **Method** : `google.cloud.apphub.v1.AppHub.GetDiscoveredService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.discoveredServices.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.GetDiscoveredService" `  




#### `GetDiscoveredWorkload`

  * **Method** : `google.cloud.apphub.v1.AppHub.GetDiscoveredWorkload`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.discoveredWorkloads.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.GetDiscoveredWorkload" `  




#### `GetExtendedMetadataSchema`

  * **Method** : `google.cloud.apphub.v1.AppHub.GetExtendedMetadataSchema`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.extendedMetadataSchemas.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.GetExtendedMetadataSchema" `  




#### `GetService`

  * **Method** : `google.cloud.apphub.v1.AppHub.GetService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.services.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.GetService" `  




#### `GetServiceProjectAttachment`

  * **Method** : `google.cloud.apphub.v1.AppHub.GetServiceProjectAttachment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.serviceProjectAttachments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.GetServiceProjectAttachment" `  




#### `GetWorkload`

  * **Method** : `google.cloud.apphub.v1.AppHub.GetWorkload`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.workloads.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.GetWorkload" `  




#### `ListApplications`

  * **Method** : `google.cloud.apphub.v1.AppHub.ListApplications`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.applications.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.ListApplications" `  




#### `ListDiscoveredServices`

  * **Method** : `google.cloud.apphub.v1.AppHub.ListDiscoveredServices`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.discoveredServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.ListDiscoveredServices" `  




#### `ListDiscoveredWorkloads`

  * **Method** : `google.cloud.apphub.v1.AppHub.ListDiscoveredWorkloads`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.discoveredWorkloads.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.ListDiscoveredWorkloads" `  




#### `ListExtendedMetadataSchemas`

  * **Method** : `google.cloud.apphub.v1.AppHub.ListExtendedMetadataSchemas`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.extendedMetadataSchemas.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.ListExtendedMetadataSchemas" `  




#### `ListServiceProjectAttachments`

  * **Method** : `google.cloud.apphub.v1.AppHub.ListServiceProjectAttachments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.serviceProjectAttachments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.ListServiceProjectAttachments" `  




#### `ListServices`

  * **Method** : `google.cloud.apphub.v1.AppHub.ListServices`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.services.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.ListServices" `  




#### `ListWorkloads`

  * **Method** : `google.cloud.apphub.v1.AppHub.ListWorkloads`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.workloads.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.ListWorkloads" `  




#### `LookupDiscoveredService`

  * **Method** : `google.cloud.apphub.v1.AppHub.LookupDiscoveredService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.discoveredServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.LookupDiscoveredService" `  




#### `LookupDiscoveredWorkload`

  * **Method** : `google.cloud.apphub.v1.AppHub.LookupDiscoveredWorkload`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.discoveredWorkloads.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.LookupDiscoveredWorkload" `  




#### `LookupServiceProjectAttachment`

  * **Method** : `google.cloud.apphub.v1.AppHub.LookupServiceProjectAttachment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.serviceProjectAttachments.lookup - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.LookupServiceProjectAttachment" `  




#### `UpdateApplication`

  * **Method** : `google.cloud.apphub.v1.AppHub.UpdateApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.UpdateApplication" `  




#### `UpdateService`

  * **Method** : `google.cloud.apphub.v1.AppHub.UpdateService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.services.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.UpdateService" `  




#### `UpdateWorkload`

  * **Method** : `google.cloud.apphub.v1.AppHub.UpdateWorkload`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.workloads.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1.AppHub.UpdateWorkload" `  




### `google.cloud.apphub.v1alpha.AppHub`

The following audit logs are associated with methods belonging to `google.cloud.apphub.v1alpha.AppHub`.

#### `CreateApplication`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.CreateApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.applications.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.CreateApplication" `  




#### `CreateService`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.CreateService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.discoveredServices.register - ADMIN_WRITE`
    * `apphub.services.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.CreateService" `  




#### `CreateServiceProjectAttachment`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.CreateServiceProjectAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.serviceProjectAttachments.attach - ADMIN_WRITE`
    * `apphub.serviceProjectAttachments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.CreateServiceProjectAttachment" `  




#### `CreateWorkload`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.CreateWorkload`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.discoveredWorkloads.register - ADMIN_WRITE`
    * `apphub.workloads.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.CreateWorkload" `  




#### `DeleteApplication`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.DeleteApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.applications.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.DeleteApplication" `  




#### `DeleteService`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.DeleteService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.services.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.DeleteService" `  




#### `DeleteServiceProjectAttachment`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.DeleteServiceProjectAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.serviceProjectAttachments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.DeleteServiceProjectAttachment" `  




#### `DeleteWorkload`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.DeleteWorkload`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.workloads.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.DeleteWorkload" `  




#### `DetachServiceProjectAttachment`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.DetachServiceProjectAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.serviceProjectAttachments.detach - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.DetachServiceProjectAttachment" `  




#### `FindUnregisteredServices`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.FindUnregisteredServices`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.discoveredServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.FindUnregisteredServices" `  




#### `FindUnregisteredWorkloads`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.FindUnregisteredWorkloads`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.discoveredWorkloads.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.FindUnregisteredWorkloads" `  




#### `GetApplication`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.GetApplication`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.applications.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.GetApplication" `  




#### `GetDiscoveredService`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.GetDiscoveredService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.discoveredServices.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.GetDiscoveredService" `  




#### `GetDiscoveredWorkload`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.GetDiscoveredWorkload`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.discoveredWorkloads.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.GetDiscoveredWorkload" `  




#### `GetExtendedMetadataSchema`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.GetExtendedMetadataSchema`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.extendedMetadataSchemas.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.GetExtendedMetadataSchema" `  




#### `GetService`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.GetService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.services.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.GetService" `  




#### `GetServiceProjectAttachment`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.GetServiceProjectAttachment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.serviceProjectAttachments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.GetServiceProjectAttachment" `  




#### `GetWorkload`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.GetWorkload`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.workloads.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.GetWorkload" `  




#### `ListApplications`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.ListApplications`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.applications.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.ListApplications" `  




#### `ListDiscoveredServices`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.ListDiscoveredServices`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.discoveredServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.ListDiscoveredServices" `  




#### `ListDiscoveredWorkloads`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.ListDiscoveredWorkloads`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.discoveredWorkloads.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.ListDiscoveredWorkloads" `  




#### `ListExtendedMetadataSchemas`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.ListExtendedMetadataSchemas`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.extendedMetadataSchemas.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.ListExtendedMetadataSchemas" `  




#### `ListServiceProjectAttachments`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.ListServiceProjectAttachments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.serviceProjectAttachments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.ListServiceProjectAttachments" `  




#### `ListServices`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.ListServices`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.services.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.ListServices" `  




#### `ListWorkloads`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.ListWorkloads`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.workloads.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.ListWorkloads" `  




#### `LookupDiscoveredService`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.LookupDiscoveredService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.discoveredServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.LookupDiscoveredService" `  




#### `LookupDiscoveredWorkload`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.LookupDiscoveredWorkload`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.discoveredWorkloads.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.LookupDiscoveredWorkload" `  




#### `LookupServiceProjectAttachment`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.LookupServiceProjectAttachment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.serviceProjectAttachments.lookup - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.LookupServiceProjectAttachment" `  




#### `UpdateApplication`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.UpdateApplication`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.applications.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.UpdateApplication" `  




#### `UpdateService`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.UpdateService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.services.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.UpdateService" `  




#### `UpdateWorkload`

  * **Method** : `google.cloud.apphub.v1alpha.AppHub.UpdateWorkload`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.workloads.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apphub.v1alpha.AppHub.UpdateWorkload" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apphub.applications.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apphub.applications.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.apphub.v1.AppHub.GetBoundary`
  * `google.cloud.apphub.v1.AppHub.UpdateBoundary`
  * `google.cloud.apphub.v1alpha.AppHub.GetBoundary`
  * `google.cloud.apphub.v1alpha.AppHub.UpdateBoundary`
  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.DeleteOperation`
  * `google.longrunning.Operations.GetOperation`
  * `google.longrunning.Operations.ListOperations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
