---
url: https://docs.cloud.google.com/app-lifecycle-manager/audit-logging/
title: App Lifecycle Manager audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:04.323701+00:00
---

# App Lifecycle Manager audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/audit-logging/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback 

#  App Lifecycle Manager audit logging Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document lists the audited methods for SaaS Service Management. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the SaaS Service Management audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="saasservicemgmt.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, SaaS Service Management generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.GetRelease`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.GetSaas`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.GetTenant`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.GetUnit`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.GetUnitKind`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.GetUnitOperation`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.ListReleases`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.ListSaas`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.ListTenants`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.ListUnitKinds`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.ListUnitOperations`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.ListUnits`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.GetRollout`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.GetRolloutKind`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.ListRolloutKinds`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.ListRollouts`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetRelease`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetSaas`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetSaasRelease`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetTenant`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetUnit`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetUnitGroup`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetUnitGroupOperation`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetUnitKind`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetUnitOperation`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListReleases`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListSaas`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListSaasReleases`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListSaasTypes`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListTenants`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListUnitGroupOperations`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListUnitGroups`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListUnitKinds`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListUnitOperations`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListUnits`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.GetFlag`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.GetFlagAttribute`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.GetFlagRelease`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.GetFlagRevision`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.ListFlagAttributes`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.ListFlagReleases`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.ListFlagRevisions`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.ListFlags`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.GetRollout`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.GetRolloutKind`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.ListRolloutKinds`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.ListRolloutTypes`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.ListRollouts`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.CreateRelease`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.CreateSaas`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.CreateTenant`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.CreateUnit`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.CreateUnitKind`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.CreateUnitOperation`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.DeleteRelease`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.DeleteSaas`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.DeleteTenant`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.DeleteUnit`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.DeleteUnitKind`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.DeleteUnitOperation`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.UpdateRelease`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.UpdateSaas`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.UpdateTenant`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.UpdateUnit`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.UpdateUnitKind`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.UpdateUnitOperation`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.CreateRollout`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.CreateRolloutKind`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.DeleteRollout`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.DeleteRolloutKind`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.UpdateRollout`  
`google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.UpdateRolloutKind`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateRelease`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateSaas`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateSaasRelease`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateSaasType`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateTenant`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateUnit`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateUnitGroup`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateUnitGroupOperation`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateUnitKind`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateUnitOperation`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteRelease`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteSaas`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteSaasRelease`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteSaasType`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteTenant`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteUnit`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteUnitGroup`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteUnitGroupOperation`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteUnitKind`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteUnitOperation`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateRelease`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateSaas`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateSaasRelease`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateSaasType`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateTenant`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateUnit`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateUnitGroup`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateUnitGroupOperation`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateUnitKind`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateUnitOperation`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.CreateFlag`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.CreateFlagAttribute`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.CreateFlagRelease`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.CreateFlagRevision`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.DeleteFlag`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.DeleteFlagAttribute`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.DeleteFlagRelease`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.DeleteFlagRevision`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.UpdateFlag`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.UpdateFlagAttribute`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.UpdateFlagRelease`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.UpdateFlagRevision`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.CreateRollout`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.CreateRolloutKind`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.CreateRolloutType`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.DeleteRollout`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.DeleteRolloutKind`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.DeleteRolloutType`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.UpdateRollout`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.UpdateRolloutKind`  
`google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.UpdateRolloutType`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for SaaS Service Management.

### `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments`

The following audit logs are associated with methods belonging to `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments`.

#### `CreateRelease`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.CreateRelease`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.releases.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.CreateRelease" `  




#### `CreateSaas`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.CreateSaas`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.saas.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.CreateSaas" `  




#### `CreateTenant`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.CreateTenant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.tenants.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.CreateTenant" `  




#### `CreateUnit`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.CreateUnit`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.units.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.CreateUnit" `  




#### `CreateUnitKind`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.CreateUnitKind`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.unitKinds.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.CreateUnitKind" `  




#### `CreateUnitOperation`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.CreateUnitOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.unitOperations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.CreateUnitOperation" `  




#### `DeleteRelease`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.DeleteRelease`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.releases.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.DeleteRelease" `  




#### `DeleteSaas`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.DeleteSaas`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.saas.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.DeleteSaas" `  




#### `DeleteTenant`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.DeleteTenant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.tenants.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.DeleteTenant" `  




#### `DeleteUnit`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.DeleteUnit`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.units.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.DeleteUnit" `  




#### `DeleteUnitKind`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.DeleteUnitKind`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.unitKinds.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.DeleteUnitKind" `  




#### `DeleteUnitOperation`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.DeleteUnitOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.unitOperations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.DeleteUnitOperation" `  




#### `GetRelease`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.GetRelease`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.releases.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.GetRelease" `  




#### `GetSaas`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.GetSaas`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.saas.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.GetSaas" `  




#### `GetTenant`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.GetTenant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.tenants.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.GetTenant" `  




#### `GetUnit`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.GetUnit`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.units.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.GetUnit" `  




#### `GetUnitKind`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.GetUnitKind`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.unitKinds.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.GetUnitKind" `  




#### `GetUnitOperation`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.GetUnitOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.unitOperations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.GetUnitOperation" `  




#### `ListReleases`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.ListReleases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.releases.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.ListReleases" `  




#### `ListSaas`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.ListSaas`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.saas.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.ListSaas" `  




#### `ListTenants`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.ListTenants`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.tenants.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.ListTenants" `  




#### `ListUnitKinds`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.ListUnitKinds`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.unitKinds.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.ListUnitKinds" `  




#### `ListUnitOperations`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.ListUnitOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.unitOperations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.ListUnitOperations" `  




#### `ListUnits`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.ListUnits`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.units.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.ListUnits" `  




#### `UpdateRelease`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.UpdateRelease`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.releases.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.UpdateRelease" `  




#### `UpdateSaas`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.UpdateSaas`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.saas.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.UpdateSaas" `  




#### `UpdateTenant`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.UpdateTenant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.tenants.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.UpdateTenant" `  




#### `UpdateUnit`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.UpdateUnit`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.units.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.UpdateUnit" `  




#### `UpdateUnitKind`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.UpdateUnitKind`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.unitKinds.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.UpdateUnitKind" `  




#### `UpdateUnitOperation`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.UpdateUnitOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.unitOperations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasDeployments.UpdateUnitOperation" `  




### `google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts`

The following audit logs are associated with methods belonging to `google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts`.

#### `CreateRollout`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.CreateRollout`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.rollouts.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.CreateRollout" `  




#### `CreateRolloutKind`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.CreateRolloutKind`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.rolloutKinds.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.CreateRolloutKind" `  




#### `DeleteRollout`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.DeleteRollout`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.rollouts.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.DeleteRollout" `  




#### `DeleteRolloutKind`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.DeleteRolloutKind`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.rolloutKinds.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.DeleteRolloutKind" `  




#### `GetRollout`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.GetRollout`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.rollouts.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.GetRollout" `  




#### `GetRolloutKind`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.GetRolloutKind`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.rolloutKinds.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.GetRolloutKind" `  




#### `ListRolloutKinds`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.ListRolloutKinds`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.rolloutKinds.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.ListRolloutKinds" `  




#### `ListRollouts`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.ListRollouts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.rollouts.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.ListRollouts" `  




#### `UpdateRollout`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.UpdateRollout`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.rollouts.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.UpdateRollout" `  




#### `UpdateRolloutKind`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.UpdateRolloutKind`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.rolloutKinds.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1.SaasRollouts.UpdateRolloutKind" `  




### `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments`

The following audit logs are associated with methods belonging to `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments`.

#### `CreateRelease`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateRelease`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.releases.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateRelease" `  




#### `CreateSaas`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateSaas`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.saas.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateSaas" `  




#### `CreateSaasRelease`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateSaasRelease`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.saasReleases.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateSaasRelease" `  




#### `CreateSaasType`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateSaasType`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.saasTypes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateSaasType" `  




#### `CreateTenant`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateTenant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.tenants.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateTenant" `  




#### `CreateUnit`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateUnit`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.units.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateUnit" `  




#### `CreateUnitGroup`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateUnitGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.unitGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateUnitGroup" `  




#### `CreateUnitGroupOperation`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateUnitGroupOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.unitGroupOperations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateUnitGroupOperation" `  




#### `CreateUnitKind`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateUnitKind`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.unitKinds.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateUnitKind" `  




#### `CreateUnitOperation`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateUnitOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.unitOperations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.CreateUnitOperation" `  




#### `DeleteRelease`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteRelease`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.releases.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteRelease" `  




#### `DeleteSaas`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteSaas`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.saas.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteSaas" `  




#### `DeleteSaasRelease`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteSaasRelease`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.saasReleases.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteSaasRelease" `  




#### `DeleteSaasType`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteSaasType`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.saasTypes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteSaasType" `  




#### `DeleteTenant`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteTenant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.tenants.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteTenant" `  




#### `DeleteUnit`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteUnit`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.units.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteUnit" `  




#### `DeleteUnitGroup`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteUnitGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.unitGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteUnitGroup" `  




#### `DeleteUnitGroupOperation`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteUnitGroupOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.unitGroupOperations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteUnitGroupOperation" `  




#### `DeleteUnitKind`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteUnitKind`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.unitKinds.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteUnitKind" `  




#### `DeleteUnitOperation`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteUnitOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.unitOperations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.DeleteUnitOperation" `  




#### `GetRelease`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetRelease`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.releases.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetRelease" `  




#### `GetSaas`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetSaas`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.saas.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetSaas" `  




#### `GetSaasRelease`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetSaasRelease`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.saasReleases.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetSaasRelease" `  




#### `GetTenant`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetTenant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.tenants.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetTenant" `  




#### `GetUnit`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetUnit`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.units.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetUnit" `  




#### `GetUnitGroup`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetUnitGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.unitGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetUnitGroup" `  




#### `GetUnitGroupOperation`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetUnitGroupOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.unitGroupOperations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetUnitGroupOperation" `  




#### `GetUnitKind`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetUnitKind`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.unitKinds.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetUnitKind" `  




#### `GetUnitOperation`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetUnitOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.unitOperations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.GetUnitOperation" `  




#### `ListReleases`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListReleases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.releases.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListReleases" `  




#### `ListSaas`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListSaas`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.saas.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListSaas" `  




#### `ListSaasReleases`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListSaasReleases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.saasReleases.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListSaasReleases" `  




#### `ListSaasTypes`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListSaasTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.saasTypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListSaasTypes" `  




#### `ListTenants`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListTenants`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.tenants.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListTenants" `  




#### `ListUnitGroupOperations`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListUnitGroupOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.unitGroupOperations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListUnitGroupOperations" `  




#### `ListUnitGroups`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListUnitGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.unitGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListUnitGroups" `  




#### `ListUnitKinds`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListUnitKinds`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.unitKinds.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListUnitKinds" `  




#### `ListUnitOperations`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListUnitOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.unitOperations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListUnitOperations" `  




#### `ListUnits`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListUnits`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.units.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.ListUnits" `  




#### `UpdateRelease`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateRelease`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.releases.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateRelease" `  




#### `UpdateSaas`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateSaas`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.saas.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateSaas" `  




#### `UpdateSaasRelease`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateSaasRelease`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.saasReleases.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateSaasRelease" `  




#### `UpdateSaasType`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateSaasType`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.saasTypes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateSaasType" `  




#### `UpdateTenant`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateTenant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.tenants.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateTenant" `  




#### `UpdateUnit`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateUnit`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.units.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateUnit" `  




#### `UpdateUnitGroup`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateUnitGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.unitGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateUnitGroup" `  




#### `UpdateUnitGroupOperation`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateUnitGroupOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.unitGroupOperations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateUnitGroupOperation" `  




#### `UpdateUnitKind`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateUnitKind`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.unitKinds.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateUnitKind" `  




#### `UpdateUnitOperation`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateUnitOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.unitOperations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasDeployments.UpdateUnitOperation" `  




### `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags`

The following audit logs are associated with methods belonging to `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags`.

#### `CreateFlag`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.CreateFlag`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.flags.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.CreateFlag" `  




#### `CreateFlagAttribute`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.CreateFlagAttribute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.flagAttributes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.CreateFlagAttribute" `  




#### `CreateFlagRelease`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.CreateFlagRelease`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.flagReleases.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.CreateFlagRelease" `  




#### `CreateFlagRevision`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.CreateFlagRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.flagRevisions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.CreateFlagRevision" `  




#### `DeleteFlag`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.DeleteFlag`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.flags.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.DeleteFlag" `  




#### `DeleteFlagAttribute`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.DeleteFlagAttribute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.flagAttributes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.DeleteFlagAttribute" `  




#### `DeleteFlagRelease`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.DeleteFlagRelease`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.flagReleases.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.DeleteFlagRelease" `  




#### `DeleteFlagRevision`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.DeleteFlagRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.flagRevisions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.DeleteFlagRevision" `  




#### `GetFlag`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.GetFlag`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.flags.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.GetFlag" `  




#### `GetFlagAttribute`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.GetFlagAttribute`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.flagAttributes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.GetFlagAttribute" `  




#### `GetFlagRelease`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.GetFlagRelease`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.flagReleases.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.GetFlagRelease" `  




#### `GetFlagRevision`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.GetFlagRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.flagRevisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.GetFlagRevision" `  




#### `ListFlagAttributes`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.ListFlagAttributes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.flagAttributes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.ListFlagAttributes" `  




#### `ListFlagReleases`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.ListFlagReleases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.flagReleases.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.ListFlagReleases" `  




#### `ListFlagRevisions`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.ListFlagRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.flagRevisions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.ListFlagRevisions" `  




#### `ListFlags`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.ListFlags`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.flags.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.ListFlags" `  




#### `UpdateFlag`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.UpdateFlag`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.flags.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.UpdateFlag" `  




#### `UpdateFlagAttribute`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.UpdateFlagAttribute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.flagAttributes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.UpdateFlagAttribute" `  




#### `UpdateFlagRelease`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.UpdateFlagRelease`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.flagReleases.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.UpdateFlagRelease" `  




#### `UpdateFlagRevision`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.UpdateFlagRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.flagRevisions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasFlags.UpdateFlagRevision" `  




### `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts`

The following audit logs are associated with methods belonging to `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts`.

#### `CreateRollout`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.CreateRollout`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.rollouts.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.CreateRollout" `  




#### `CreateRolloutKind`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.CreateRolloutKind`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.rolloutKinds.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.CreateRolloutKind" `  




#### `CreateRolloutType`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.CreateRolloutType`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.rolloutTypes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.CreateRolloutType" `  




#### `DeleteRollout`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.DeleteRollout`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.rollouts.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.DeleteRollout" `  




#### `DeleteRolloutKind`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.DeleteRolloutKind`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.rolloutKinds.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.DeleteRolloutKind" `  




#### `DeleteRolloutType`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.DeleteRolloutType`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.rolloutTypes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.DeleteRolloutType" `  




#### `GetRollout`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.GetRollout`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.rollouts.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.GetRollout" `  




#### `GetRolloutKind`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.GetRolloutKind`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.rolloutKinds.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.GetRolloutKind" `  




#### `ListRolloutKinds`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.ListRolloutKinds`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.rolloutKinds.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.ListRolloutKinds" `  




#### `ListRolloutTypes`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.ListRolloutTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.rolloutTypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.ListRolloutTypes" `  




#### `ListRollouts`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.ListRollouts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.rollouts.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.ListRollouts" `  




#### `UpdateRollout`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.UpdateRollout`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.rollouts.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.UpdateRollout" `  




#### `UpdateRolloutKind`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.UpdateRolloutKind`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.rolloutKinds.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.UpdateRolloutKind" `  




#### `UpdateRolloutType`

  * **Method** : `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.UpdateRolloutType`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.rolloutTypes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.UpdateRolloutType" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `saasservicemgmt.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `saasservicemgmt.operations.list - ADMIN_READ`
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
  * `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.CreateReplicationInternal`
  * `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.DeleteReplicationInternal`
  * `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.GetReplicationInternal`
  * `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.ListReplicationsInternal`
  * `google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts.UpdateReplicationInternal`
  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
