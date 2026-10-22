---
url: https://docs.cloud.google.com/nat/docs/audit-logging/
title: Cloud NAT audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:54.607199+00:00
---

# Cloud NAT audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nat/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NAT ](https://docs.cloud.google.com/nat/docs)
  * [ Guides ](https://docs.cloud.google.com/nat/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud NAT audit logging

This document describes audit logging for Cloud NAT. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Cloud NAT audit logs use the service name `compute.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="compute.googleapis.com"
      

## Methods by permission type

For the following API methods, there is also a `beta` and `alpha` version available that is not listed here. When the `beta` or `alpha` version of the API is called the method name will start with `beta` or `alpha` respectively.

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud NAT generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

Permission type | Methods  
---|---  
`ADMIN_READ` | `v1.compute.routers.aggregatedList`  
`v1.compute.routers.get`  
`v1.compute.routers.getNatIpInfo`  
`v1.compute.routers.getNatMappingInfo`  
`v1.compute.routers.getRoutePolicy`  
`v1.compute.routers.getRouterStatus`  
`v1.compute.routers.list`  
`v1.compute.routers.listBgpRoutes`  
`v1.compute.routers.listRoutePolicies`  
`v1.compute.routers.preview`  
`ADMIN_WRITE` | `v1.compute.routers.delete`  
`v1.compute.routers.deleteRoutePolicy`  
`v1.compute.routers.insert`  
`v1.compute.routers.patch`  
`v1.compute.routers.patchRoutePolicy`  
`v1.compute.routers.update`  
`v1.compute.routers.updateRoutePolicy`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud NAT.

### `compute.v1.RegionRoutersService`

The following audit logs are associated with methods belonging to `compute.v1.RegionRoutersService`.

#### `aggregatedList`

  * **Method** : `v1.compute.routers.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.routers.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.routers.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.delete" `  




#### `deleteRoutePolicy`

  * **Method** : `v1.compute.routers.deleteRoutePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.routers.deleteRoutePolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.deleteRoutePolicy" `  




#### `get`

  * **Method** : `v1.compute.routers.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.get" `  




#### `getNatIpInfo`

  * **Method** : `v1.compute.routers.getNatIpInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.getNatIpInfo" `  




#### `getNatMappingInfo`

  * **Method** : `v1.compute.routers.getNatMappingInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.getNatMappingInfo" `  




#### `getRoutePolicy`

  * **Method** : `v1.compute.routers.getRoutePolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routers.getRoutePolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.getRoutePolicy" `  




#### `getRouterStatus`

  * **Method** : `v1.compute.routers.getRouterStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.getRouterStatus" `  




#### `insert`

  * **Method** : `v1.compute.routers.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.updatePolicy - ADMIN_WRITE`
    * `compute.routers.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.insert" `  




#### `list`

  * **Method** : `v1.compute.routers.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.list" `  




#### `listBgpRoutes`

  * **Method** : `v1.compute.routers.listBgpRoutes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routers.listBgpRoutes - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.listBgpRoutes" `  




#### `listRoutePolicies`

  * **Method** : `v1.compute.routers.listRoutePolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routers.listRoutePolicies - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.listRoutePolicies" `  




#### `patch`

  * **Method** : `v1.compute.routers.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.updatePolicy - ADMIN_WRITE`
    * `compute.routers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.patch" `  




#### `patchRoutePolicy`

  * **Method** : `v1.compute.routers.patchRoutePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.routers.updateRoutePolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.patchRoutePolicy" `  




#### `preview`

  * **Method** : `v1.compute.routers.preview`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.preview" `  




#### `update`

  * **Method** : `v1.compute.routers.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.updatePolicy - ADMIN_WRITE`
    * `compute.routers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.update" `  




#### `updateRoutePolicy`

  * **Method** : `v1.compute.routers.updateRoutePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.routers.updateRoutePolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routers.updateRoutePolicy" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
