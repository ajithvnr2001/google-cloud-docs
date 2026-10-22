---
url: https://docs.cloud.google.com/number-registry/audit-logging/
title: Cloud Number Registry audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:14.390709+00:00
---

# Cloud Number Registry audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Guides ](https://docs.cloud.google.com/number-registry/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Number Registry audit logging

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document lists the audited methods for Cloud Number Registry. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Cloud Number Registry audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="cloudnumberregistry.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Number Registry generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CheckAvailabilityIpamAdminScopes`  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.FindCustomRangeFreeIpRanges`  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.FindDiscoveredRangeFreeIpRanges`  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.GetCustomRange`  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.GetDiscoveredRange`  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.GetIpamAdminScope`  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.GetOrgNumberRegistry`  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.GetRealm`  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.GetRegistryBook`  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ListCustomRanges`  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ListDiscoveredRanges`  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ListIpamAdminScopes`  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ListOrgNumberRegistries`  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ListRealms`  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ListRegistryBooks`  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.SearchIpResources`  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ShowCustomRangeUtilization`  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ShowDiscoveredRangeUtilization`  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.CheckAvailabilityIpamAdminScopes`  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.FindCustomRangeFreeIpRanges`  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.FindDiscoveredRangeFreeIpRanges`  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.GetCustomRange`  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.GetDiscoveredRange`  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.GetIpamAdminScope`  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.GetOrgNumberRegistry`  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.GetRealm`  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.GetRegistryBook`  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.ListCustomRanges`  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.ListDiscoveredRanges`  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.ListIpamAdminScopes`  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.ListOrgNumberRegistries`  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.ListRealms`  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.ListRegistryBooks`  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.SearchIpResources`  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.ShowCustomRangeUtilization`  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.ShowDiscoveredRangeUtilization`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CleanupIpamAdminScope` (LRO)  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CreateCustomRange` (LRO)  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CreateIpamAdminScope` (LRO)  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CreateOrgNumberRegistry` (LRO)  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CreateRealm` (LRO)  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CreateRegistryBook` (LRO)  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.DeleteCustomRange` (LRO)  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.DeleteIpamAdminScope` (LRO)  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.DeleteOrgNumberRegistry` (LRO)  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.DeleteRealm` (LRO)  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.DeleteRegistryBook` (LRO)  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.DisableIpamAdminScope` (LRO)  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.UpdateCustomRange` (LRO)  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.UpdateIpamAdminScope` (LRO)  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.UpdateRealm` (LRO)  
`google.cloud.numberregistry.v1alpha.CloudNumberRegistry.UpdateRegistryBook` (LRO)  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.CleanupIpamAdminScope` (LRO)  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.CreateCustomRange` (LRO)  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.CreateIpamAdminScope` (LRO)  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.CreateOrgNumberRegistry`  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.CreateRealm` (LRO)  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.CreateRegistryBook` (LRO)  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.DeleteCustomRange` (LRO)  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.DeleteIpamAdminScope` (LRO)  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.DeleteOrgNumberRegistry`  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.DeleteRealm` (LRO)  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.DeleteRegistryBook` (LRO)  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.DisableIpamAdminScope` (LRO)  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.UpdateCustomRange` (LRO)  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.UpdateIpamAdminScope` (LRO)  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.UpdateRealm` (LRO)  
`google.cloud.numberregistry.v1beta.CloudNumberRegistry.UpdateRegistryBook` (LRO)  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Number Registry.

### `google.cloud.numberregistry.v1alpha.CloudNumberRegistry`

The following audit logs are associated with methods belonging to `google.cloud.numberregistry.v1alpha.CloudNumberRegistry`.

#### `CheckAvailabilityIpamAdminScopes`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CheckAvailabilityIpamAdminScopes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.ipamAdminScopes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CheckAvailabilityIpamAdminScopes" `  




#### `CleanupIpamAdminScope`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CleanupIpamAdminScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.ipamAdminScopes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CleanupIpamAdminScope" `  




#### `CreateCustomRange`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CreateCustomRange`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.customRanges.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CreateCustomRange" `  




#### `CreateIpamAdminScope`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CreateIpamAdminScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.ipamAdminScopes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CreateIpamAdminScope" `  




#### `CreateOrgNumberRegistry`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CreateOrgNumberRegistry`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.orgNumberRegistries.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CreateOrgNumberRegistry" `  




#### `CreateRealm`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CreateRealm`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.realms.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CreateRealm" `  




#### `CreateRegistryBook`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CreateRegistryBook`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.registryBooks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.CreateRegistryBook" `  




#### `DeleteCustomRange`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.DeleteCustomRange`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.customRanges.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.DeleteCustomRange" `  




#### `DeleteIpamAdminScope`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.DeleteIpamAdminScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.ipamAdminScopes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.DeleteIpamAdminScope" `  




#### `DeleteOrgNumberRegistry`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.DeleteOrgNumberRegistry`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.orgNumberRegistries.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.DeleteOrgNumberRegistry" `  




#### `DeleteRealm`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.DeleteRealm`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.realms.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.DeleteRealm" `  




#### `DeleteRegistryBook`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.DeleteRegistryBook`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.registryBooks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.DeleteRegistryBook" `  




#### `DisableIpamAdminScope`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.DisableIpamAdminScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.ipamAdminScopes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.DisableIpamAdminScope" `  




#### `FindCustomRangeFreeIpRanges`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.FindCustomRangeFreeIpRanges`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.customRanges.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.FindCustomRangeFreeIpRanges" `  




#### `FindDiscoveredRangeFreeIpRanges`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.FindDiscoveredRangeFreeIpRanges`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.discoveredRanges.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.FindDiscoveredRangeFreeIpRanges" `  




#### `GetCustomRange`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.GetCustomRange`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.customRanges.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.GetCustomRange" `  




#### `GetDiscoveredRange`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.GetDiscoveredRange`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.discoveredRanges.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.GetDiscoveredRange" `  




#### `GetIpamAdminScope`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.GetIpamAdminScope`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.ipamAdminScopes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.GetIpamAdminScope" `  




#### `GetOrgNumberRegistry`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.GetOrgNumberRegistry`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.orgNumberRegistries.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.GetOrgNumberRegistry" `  




#### `GetRealm`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.GetRealm`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.realms.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.GetRealm" `  




#### `GetRegistryBook`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.GetRegistryBook`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.registryBooks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.GetRegistryBook" `  




#### `ListCustomRanges`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ListCustomRanges`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.customRanges.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ListCustomRanges" `  




#### `ListDiscoveredRanges`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ListDiscoveredRanges`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.discoveredRanges.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ListDiscoveredRanges" `  




#### `ListIpamAdminScopes`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ListIpamAdminScopes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.ipamAdminScopes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ListIpamAdminScopes" `  




#### `ListOrgNumberRegistries`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ListOrgNumberRegistries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.orgNumberRegistries.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ListOrgNumberRegistries" `  




#### `ListRealms`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ListRealms`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.realms.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ListRealms" `  




#### `ListRegistryBooks`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ListRegistryBooks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.registryBooks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ListRegistryBooks" `  




#### `SearchIpResources`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.SearchIpResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.registryBooks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.SearchIpResources" `  




#### `ShowCustomRangeUtilization`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ShowCustomRangeUtilization`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.customRanges.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ShowCustomRangeUtilization" `  




#### `ShowDiscoveredRangeUtilization`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ShowDiscoveredRangeUtilization`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.discoveredRanges.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ShowDiscoveredRangeUtilization" `  




#### `UpdateCustomRange`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.UpdateCustomRange`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.customRanges.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.UpdateCustomRange" `  




#### `UpdateIpamAdminScope`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.UpdateIpamAdminScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.ipamAdminScopes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.UpdateIpamAdminScope" `  




#### `UpdateRealm`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.UpdateRealm`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.realms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.UpdateRealm" `  




#### `UpdateRegistryBook`

  * **Method** : `google.cloud.numberregistry.v1alpha.CloudNumberRegistry.UpdateRegistryBook`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.registryBooks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1alpha.CloudNumberRegistry.UpdateRegistryBook" `  




### `google.cloud.numberregistry.v1beta.CloudNumberRegistry`

The following audit logs are associated with methods belonging to `google.cloud.numberregistry.v1beta.CloudNumberRegistry`.

#### `CheckAvailabilityIpamAdminScopes`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.CheckAvailabilityIpamAdminScopes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.ipamAdminScopes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.CheckAvailabilityIpamAdminScopes" `  




#### `CleanupIpamAdminScope`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.CleanupIpamAdminScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.ipamAdminScopes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.CleanupIpamAdminScope" `  




#### `CreateCustomRange`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.CreateCustomRange`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.customRanges.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.CreateCustomRange" `  




#### `CreateIpamAdminScope`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.CreateIpamAdminScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.ipamAdminScopes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.CreateIpamAdminScope" `  




#### `CreateOrgNumberRegistry`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.CreateOrgNumberRegistry`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.orgNumberRegistries.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.CreateOrgNumberRegistry" `  




#### `CreateRealm`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.CreateRealm`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.realms.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.CreateRealm" `  




#### `CreateRegistryBook`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.CreateRegistryBook`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.registryBooks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.CreateRegistryBook" `  




#### `DeleteCustomRange`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.DeleteCustomRange`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.customRanges.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.DeleteCustomRange" `  




#### `DeleteIpamAdminScope`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.DeleteIpamAdminScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.ipamAdminScopes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.DeleteIpamAdminScope" `  




#### `DeleteOrgNumberRegistry`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.DeleteOrgNumberRegistry`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.orgNumberRegistries.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.DeleteOrgNumberRegistry" `  




#### `DeleteRealm`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.DeleteRealm`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.realms.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.DeleteRealm" `  




#### `DeleteRegistryBook`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.DeleteRegistryBook`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.registryBooks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.DeleteRegistryBook" `  




#### `DisableIpamAdminScope`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.DisableIpamAdminScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.ipamAdminScopes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.DisableIpamAdminScope" `  




#### `FindCustomRangeFreeIpRanges`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.FindCustomRangeFreeIpRanges`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.customRanges.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.FindCustomRangeFreeIpRanges" `  




#### `FindDiscoveredRangeFreeIpRanges`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.FindDiscoveredRangeFreeIpRanges`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.discoveredRanges.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.FindDiscoveredRangeFreeIpRanges" `  




#### `GetCustomRange`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.GetCustomRange`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.customRanges.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.GetCustomRange" `  




#### `GetDiscoveredRange`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.GetDiscoveredRange`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.discoveredRanges.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.GetDiscoveredRange" `  




#### `GetIpamAdminScope`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.GetIpamAdminScope`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.ipamAdminScopes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.GetIpamAdminScope" `  




#### `GetOrgNumberRegistry`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.GetOrgNumberRegistry`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.orgNumberRegistries.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.GetOrgNumberRegistry" `  




#### `GetRealm`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.GetRealm`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.realms.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.GetRealm" `  




#### `GetRegistryBook`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.GetRegistryBook`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.registryBooks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.GetRegistryBook" `  




#### `ListCustomRanges`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.ListCustomRanges`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.customRanges.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.ListCustomRanges" `  




#### `ListDiscoveredRanges`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.ListDiscoveredRanges`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.discoveredRanges.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.ListDiscoveredRanges" `  




#### `ListIpamAdminScopes`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.ListIpamAdminScopes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.ipamAdminScopes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.ListIpamAdminScopes" `  




#### `ListOrgNumberRegistries`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.ListOrgNumberRegistries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.orgNumberRegistries.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.ListOrgNumberRegistries" `  




#### `ListRealms`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.ListRealms`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.realms.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.ListRealms" `  




#### `ListRegistryBooks`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.ListRegistryBooks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.registryBooks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.ListRegistryBooks" `  




#### `SearchIpResources`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.SearchIpResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.registryBooks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.SearchIpResources" `  




#### `ShowCustomRangeUtilization`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.ShowCustomRangeUtilization`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.customRanges.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.ShowCustomRangeUtilization" `  




#### `ShowDiscoveredRangeUtilization`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.ShowDiscoveredRangeUtilization`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.discoveredRanges.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.ShowDiscoveredRangeUtilization" `  




#### `UpdateCustomRange`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.UpdateCustomRange`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.customRanges.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.UpdateCustomRange" `  




#### `UpdateIpamAdminScope`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.UpdateIpamAdminScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.ipamAdminScopes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.UpdateIpamAdminScope" `  




#### `UpdateRealm`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.UpdateRealm`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.realms.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.UpdateRealm" `  




#### `UpdateRegistryBook`

  * **Method** : `google.cloud.numberregistry.v1beta.CloudNumberRegistry.UpdateRegistryBook`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.registryBooks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.numberregistry.v1beta.CloudNumberRegistry.UpdateRegistryBook" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudnumberregistry.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudnumberregistry.operations.list - ADMIN_READ`
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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
