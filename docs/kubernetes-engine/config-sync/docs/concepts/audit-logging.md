---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/audit-logging/
title: ConfigDelivery audit logging \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:20:22.276406+00:00
---

# ConfigDelivery audit logging  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  ConfigDelivery audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Config Delivery. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Config Delivery audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="configdelivery.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Config Delivery generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.configdelivery.v1.ConfigDelivery.GetRelease`  
`google.cloud.configdelivery.v1.ConfigDelivery.GetResourceBundle`  
`google.cloud.configdelivery.v1.ConfigDelivery.ListReleases`  
`google.cloud.configdelivery.v1.ConfigDelivery.ListResourceBundles`  
`google.cloud.configdelivery.v1beta.ConfigDelivery.GetRelease`  
`google.cloud.configdelivery.v1beta.ConfigDelivery.GetResourceBundle`  
`google.cloud.configdelivery.v1beta.ConfigDelivery.ListReleases`  
`google.cloud.configdelivery.v1beta.ConfigDelivery.ListResourceBundles`  
`ADMIN_WRITE` | `google.cloud.configdelivery.v1.ConfigDelivery.CreateRelease` (LRO)  
`google.cloud.configdelivery.v1.ConfigDelivery.CreateResourceBundle` (LRO)  
`google.cloud.configdelivery.v1.ConfigDelivery.DeleteRelease` (LRO)  
`google.cloud.configdelivery.v1.ConfigDelivery.DeleteResourceBundle` (LRO)  
`google.cloud.configdelivery.v1.ConfigDelivery.UpdateRelease` (LRO)  
`google.cloud.configdelivery.v1.ConfigDelivery.UpdateResourceBundle` (LRO)  
`google.cloud.configdelivery.v1beta.ConfigDelivery.CreateRelease` (LRO)  
`google.cloud.configdelivery.v1beta.ConfigDelivery.CreateResourceBundle` (LRO)  
`google.cloud.configdelivery.v1beta.ConfigDelivery.DeleteRelease` (LRO)  
`google.cloud.configdelivery.v1beta.ConfigDelivery.DeleteResourceBundle` (LRO)  
`google.cloud.configdelivery.v1beta.ConfigDelivery.UpdateRelease` (LRO)  
`google.cloud.configdelivery.v1beta.ConfigDelivery.UpdateResourceBundle` (LRO)  
`DATA_READ` | `google.cloud.configdelivery.v1.ConfigDelivery.GetFleetPackage`  
`google.cloud.configdelivery.v1.ConfigDelivery.GetRollout`  
`google.cloud.configdelivery.v1.ConfigDelivery.GetVariant`  
`google.cloud.configdelivery.v1.ConfigDelivery.ListFleetPackages`  
`google.cloud.configdelivery.v1.ConfigDelivery.ListRollouts`  
`google.cloud.configdelivery.v1.ConfigDelivery.ListVariants`  
`google.cloud.configdelivery.v1beta.ConfigDelivery.GetFleetPackage`  
`google.cloud.configdelivery.v1beta.ConfigDelivery.GetRollout`  
`google.cloud.configdelivery.v1beta.ConfigDelivery.GetVariant`  
`google.cloud.configdelivery.v1beta.ConfigDelivery.ListFleetPackages`  
`google.cloud.configdelivery.v1beta.ConfigDelivery.ListRollouts`  
`google.cloud.configdelivery.v1beta.ConfigDelivery.ListVariants`  
`DATA_WRITE` | `google.cloud.configdelivery.v1.ConfigDelivery.AbortRollout` (LRO)  
`google.cloud.configdelivery.v1.ConfigDelivery.CreateFleetPackage` (LRO)  
`google.cloud.configdelivery.v1.ConfigDelivery.CreateVariant` (LRO)  
`google.cloud.configdelivery.v1.ConfigDelivery.DeleteFleetPackage` (LRO)  
`google.cloud.configdelivery.v1.ConfigDelivery.DeleteVariant` (LRO)  
`google.cloud.configdelivery.v1.ConfigDelivery.ResumeRollout` (LRO)  
`google.cloud.configdelivery.v1.ConfigDelivery.SuspendRollout` (LRO)  
`google.cloud.configdelivery.v1.ConfigDelivery.UpdateFleetPackage` (LRO)  
`google.cloud.configdelivery.v1.ConfigDelivery.UpdateVariant` (LRO)  
`google.cloud.configdelivery.v1beta.ConfigDelivery.AbortRollout` (LRO)  
`google.cloud.configdelivery.v1beta.ConfigDelivery.CreateFleetPackage` (LRO)  
`google.cloud.configdelivery.v1beta.ConfigDelivery.CreateVariant` (LRO)  
`google.cloud.configdelivery.v1beta.ConfigDelivery.DeleteFleetPackage` (LRO)  
`google.cloud.configdelivery.v1beta.ConfigDelivery.DeleteVariant` (LRO)  
`google.cloud.configdelivery.v1beta.ConfigDelivery.ResumeRollout` (LRO)  
`google.cloud.configdelivery.v1beta.ConfigDelivery.SuspendRollout` (LRO)  
`google.cloud.configdelivery.v1beta.ConfigDelivery.UpdateFleetPackage` (LRO)  
`google.cloud.configdelivery.v1beta.ConfigDelivery.UpdateVariant` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Config Delivery.

### `google.cloud.configdelivery.v1.ConfigDelivery`

The following audit logs are associated with methods belonging to `google.cloud.configdelivery.v1.ConfigDelivery`.

#### `AbortRollout`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.AbortRollout`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.rollouts.abort - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.AbortRollout" `  




#### `CreateFleetPackage`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.CreateFleetPackage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.fleetPackages.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.CreateFleetPackage" `  




#### `CreateRelease`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.CreateRelease`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `configdelivery.releases.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.CreateRelease" `  




#### `CreateResourceBundle`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.CreateResourceBundle`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `configdelivery.resourceBundles.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.CreateResourceBundle" `  




#### `CreateVariant`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.CreateVariant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.variants.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.CreateVariant" `  




#### `DeleteFleetPackage`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.DeleteFleetPackage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.fleetPackages.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.DeleteFleetPackage" `  




#### `DeleteRelease`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.DeleteRelease`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `configdelivery.releases.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.DeleteRelease" `  




#### `DeleteResourceBundle`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.DeleteResourceBundle`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `configdelivery.resourceBundles.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.DeleteResourceBundle" `  




#### `DeleteVariant`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.DeleteVariant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.variants.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.DeleteVariant" `  




#### `GetFleetPackage`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.GetFleetPackage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.fleetPackages.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.GetFleetPackage" `  




#### `GetRelease`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.GetRelease`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.releases.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.GetRelease" `  




#### `GetResourceBundle`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.GetResourceBundle`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.resourceBundles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.GetResourceBundle" `  




#### `GetRollout`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.GetRollout`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.rollouts.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.GetRollout" `  




#### `GetVariant`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.GetVariant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.variants.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.GetVariant" `  




#### `ListFleetPackages`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.ListFleetPackages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.fleetPackages.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.ListFleetPackages" `  




#### `ListReleases`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.ListReleases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.releases.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.ListReleases" `  




#### `ListResourceBundles`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.ListResourceBundles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.resourceBundles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.ListResourceBundles" `  




#### `ListRollouts`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.ListRollouts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.rollouts.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.ListRollouts" `  




#### `ListVariants`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.ListVariants`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.variants.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.ListVariants" `  




#### `ResumeRollout`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.ResumeRollout`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.rollouts.resume - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.ResumeRollout" `  




#### `SuspendRollout`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.SuspendRollout`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.rollouts.suspend - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.SuspendRollout" `  




#### `UpdateFleetPackage`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.UpdateFleetPackage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.fleetPackages.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.UpdateFleetPackage" `  




#### `UpdateRelease`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.UpdateRelease`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `configdelivery.releases.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.UpdateRelease" `  




#### `UpdateResourceBundle`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.UpdateResourceBundle`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `configdelivery.resourceBundles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.UpdateResourceBundle" `  




#### `UpdateVariant`

  * **Method** : `google.cloud.configdelivery.v1.ConfigDelivery.UpdateVariant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.variants.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1.ConfigDelivery.UpdateVariant" `  




### `google.cloud.configdelivery.v1beta.ConfigDelivery`

The following audit logs are associated with methods belonging to `google.cloud.configdelivery.v1beta.ConfigDelivery`.

#### `AbortRollout`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.AbortRollout`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.rollouts.abort - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.AbortRollout" `  




#### `CreateFleetPackage`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.CreateFleetPackage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.fleetPackages.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.CreateFleetPackage" `  




#### `CreateRelease`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.CreateRelease`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `configdelivery.releases.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.CreateRelease" `  




#### `CreateResourceBundle`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.CreateResourceBundle`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `configdelivery.resourceBundles.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.CreateResourceBundle" `  




#### `CreateVariant`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.CreateVariant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.variants.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.CreateVariant" `  




#### `DeleteFleetPackage`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.DeleteFleetPackage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.fleetPackages.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.DeleteFleetPackage" `  




#### `DeleteRelease`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.DeleteRelease`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `configdelivery.releases.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.DeleteRelease" `  




#### `DeleteResourceBundle`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.DeleteResourceBundle`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `configdelivery.resourceBundles.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.DeleteResourceBundle" `  




#### `DeleteVariant`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.DeleteVariant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.variants.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.DeleteVariant" `  




#### `GetFleetPackage`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.GetFleetPackage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.fleetPackages.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.GetFleetPackage" `  




#### `GetRelease`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.GetRelease`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.releases.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.GetRelease" `  




#### `GetResourceBundle`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.GetResourceBundle`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.resourceBundles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.GetResourceBundle" `  




#### `GetRollout`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.GetRollout`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.rollouts.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.GetRollout" `  




#### `GetVariant`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.GetVariant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.variants.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.GetVariant" `  




#### `ListFleetPackages`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.ListFleetPackages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.fleetPackages.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.ListFleetPackages" `  




#### `ListReleases`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.ListReleases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.releases.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.ListReleases" `  




#### `ListResourceBundles`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.ListResourceBundles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.resourceBundles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.ListResourceBundles" `  




#### `ListRollouts`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.ListRollouts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.rollouts.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.ListRollouts" `  




#### `ListVariants`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.ListVariants`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.variants.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.ListVariants" `  




#### `ResumeRollout`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.ResumeRollout`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.rollouts.resume - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.ResumeRollout" `  




#### `SuspendRollout`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.SuspendRollout`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.rollouts.suspend - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.SuspendRollout" `  




#### `UpdateFleetPackage`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.UpdateFleetPackage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.fleetPackages.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.UpdateFleetPackage" `  




#### `UpdateRelease`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.UpdateRelease`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `configdelivery.releases.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.UpdateRelease" `  




#### `UpdateResourceBundle`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.UpdateResourceBundle`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `configdelivery.resourceBundles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.UpdateResourceBundle" `  




#### `UpdateVariant`

  * **Method** : `google.cloud.configdelivery.v1beta.ConfigDelivery.UpdateVariant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `configdelivery.variants.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.configdelivery.v1beta.ConfigDelivery.UpdateVariant" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
