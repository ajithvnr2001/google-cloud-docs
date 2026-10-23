---
url: https://docs.cloud.google.com/load-balancing/docs/audit-logging/
title: Cloud Load Balancing audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:42.095351+00:00
---

# Cloud Load Balancing audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Cloud Load Balancing audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Cloud Load Balancing. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Cloud Load Balancing audit logs use the service name `compute.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="compute.googleapis.com"
      

## Methods by permission type

For the following API methods, there is also a `beta` and `alpha` version available that is not listed here. When the `beta` or `alpha` version of the API is called the method name will start with `beta` or `alpha` respectively.

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Load Balancing generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

Permission type | Methods  
---|---  
`ADMIN_READ` | `v1.compute.backendServices.aggregatedList`  
`v1.compute.backendServices.get`  
`v1.compute.backendServices.getHealth`  
`v1.compute.backendServices.getIamPolicy`  
`v1.compute.backendServices.list`  
`v1.compute.backendServices.testIamPermissions`  
`v1.compute.forwardingRules.aggregatedList`  
`v1.compute.forwardingRules.get`  
`v1.compute.forwardingRules.list`  
`v1.compute.targetHttpProxies.aggregatedList`  
`v1.compute.targetHttpProxies.get`  
`v1.compute.targetHttpProxies.list`  
`v1.compute.targetPools.aggregatedList`  
`v1.compute.targetPools.get`  
`v1.compute.targetPools.getHealth`  
`v1.compute.targetPools.list`  
`v1.compute.urlMaps.aggregatedList`  
`v1.compute.urlMaps.get`  
`v1.compute.urlMaps.list`  
`ADMIN_WRITE` | `v1.compute.backendServices.addSignedUrlKey`  
`v1.compute.backendServices.delete`  
`v1.compute.backendServices.deleteSignedUrlKey`  
`v1.compute.backendServices.insert`  
`v1.compute.backendServices.patch`  
`v1.compute.backendServices.setEdgeSecurityPolicy`  
`v1.compute.backendServices.setIamPolicy`  
`v1.compute.backendServices.setSecurityPolicy`  
`v1.compute.backendServices.update`  
`v1.compute.forwardingRules.delete`  
`v1.compute.forwardingRules.insert`  
`v1.compute.forwardingRules.patch`  
`v1.compute.forwardingRules.setLabels`  
`v1.compute.forwardingRules.setTarget`  
`v1.compute.targetHttpProxies.delete`  
`v1.compute.targetHttpProxies.insert`  
`v1.compute.targetHttpProxies.patch`  
`v1.compute.targetHttpProxies.setUrlMap`  
`v1.compute.targetPools.addHealthCheck`  
`v1.compute.targetPools.addInstance`  
`v1.compute.targetPools.delete`  
`v1.compute.targetPools.insert`  
`v1.compute.targetPools.removeHealthCheck`  
`v1.compute.targetPools.removeInstance`  
`v1.compute.targetPools.setBackup`  
`v1.compute.targetPools.setSecurityPolicy`  
`v1.compute.urlMaps.delete`  
`v1.compute.urlMaps.insert`  
`v1.compute.urlMaps.invalidateCache`  
`v1.compute.urlMaps.patch`  
`v1.compute.urlMaps.update`  
`v1.compute.urlMaps.validate`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Load Balancing.

### `compute.v1.BackendServicesService`

The following audit logs are associated with methods belonging to `compute.v1.BackendServicesService`.

#### `addSignedUrlKey`

  * **Method** : `v1.compute.backendServices.addSignedUrlKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.addSignedUrlKey - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.addSignedUrlKey" `  




#### `aggregatedList`

  * **Method** : `v1.compute.backendServices.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.backendServices.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.delete" `  




#### `deleteSignedUrlKey`

  * **Method** : `v1.compute.backendServices.deleteSignedUrlKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.deleteSignedUrlKey - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.deleteSignedUrlKey" `  




#### `get`

  * **Method** : `v1.compute.backendServices.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendServices.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.get" `  




#### `getHealth`

  * **Method** : `v1.compute.backendServices.getHealth`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendServices.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.getHealth" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.backendServices.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendServices.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.backendServices.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.create - ADMIN_WRITE`
    * `compute.instanceGroups.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.insert" `  




#### `list`

  * **Method** : `v1.compute.backendServices.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.list" `  




#### `patch`

  * **Method** : `v1.compute.backendServices.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.get - ADMIN_READ`
    * `compute.backendServices.update - ADMIN_WRITE`
    * `compute.healthChecks.useReadOnly - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.patch" `  




#### `setEdgeSecurityPolicy`

  * **Method** : `v1.compute.backendServices.setEdgeSecurityPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.setSecurityPolicy - ADMIN_WRITE`
    * `compute.securityPolicies.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.setEdgeSecurityPolicy" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.backendServices.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.setIamPolicy" `  




#### `setSecurityPolicy`

  * **Method** : `v1.compute.backendServices.setSecurityPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.setSecurityPolicy - ADMIN_WRITE`
    * `compute.securityPolicies.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.setSecurityPolicy" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.backendServices.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.testIamPermissions" `  




#### `update`

  * **Method** : `v1.compute.backendServices.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.update - ADMIN_WRITE`
    * `compute.healthChecks.useReadOnly - ADMIN_READ`
    * `compute.instanceGroups.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.backendServices.update" `  




### `compute.v1.RegionForwardingRulesService`

The following audit logs are associated with methods belonging to `compute.v1.RegionForwardingRulesService`.

#### `aggregatedList`

  * **Method** : `v1.compute.forwardingRules.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.forwardingRules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.forwardingRules.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.forwardingRules.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.forwardingRules.delete - ADMIN_WRITE`
    * `compute.forwardingRules.pscDelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.forwardingRules.delete" `  




#### `get`

  * **Method** : `v1.compute.forwardingRules.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.forwardingRules.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.forwardingRules.get" `  




#### `insert`

  * **Method** : `v1.compute.forwardingRules.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : See IAM documentation for permissions.
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.forwardingRules.insert" `  




#### `list`

  * **Method** : `v1.compute.forwardingRules.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.forwardingRules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.forwardingRules.list" `  




#### `patch`

  * **Method** : `v1.compute.forwardingRules.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.forwardingRules.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.forwardingRules.patch" `  




#### `setLabels`

  * **Method** : `v1.compute.forwardingRules.setLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.forwardingRules.setLabels - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.forwardingRules.setLabels" `  




#### `setTarget`

  * **Method** : `v1.compute.forwardingRules.setTarget`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.forwardingRules.setTarget - ADMIN_WRITE`
    * `compute.regionBackendServices.use - ADMIN_WRITE`
    * `compute.regionTargetHttpsProxies.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.forwardingRules.setTarget" `  




### `compute.v1.TargetHttpProxiesService`

The following audit logs are associated with methods belonging to `compute.v1.TargetHttpProxiesService`.

#### `aggregatedList`

  * **Method** : `v1.compute.targetHttpProxies.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetHttpProxies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpProxies.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.targetHttpProxies.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetHttpProxies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpProxies.delete" `  




#### `get`

  * **Method** : `v1.compute.targetHttpProxies.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetHttpProxies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpProxies.get" `  




#### `insert`

  * **Method** : `v1.compute.targetHttpProxies.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetHttpProxies.create - ADMIN_WRITE`
    * `compute.urlMaps.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpProxies.insert" `  




#### `list`

  * **Method** : `v1.compute.targetHttpProxies.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetHttpProxies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpProxies.list" `  




#### `patch`

  * **Method** : `v1.compute.targetHttpProxies.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetHttpProxies.get - ADMIN_READ`
    * `compute.targetHttpProxies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpProxies.patch" `  




#### `setUrlMap`

  * **Method** : `v1.compute.targetHttpProxies.setUrlMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetHttpProxies.setUrlMap - ADMIN_WRITE`
    * `compute.urlMaps.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetHttpProxies.setUrlMap" `  




### `compute.v1.TargetPoolsService`

The following audit logs are associated with methods belonging to `compute.v1.TargetPoolsService`.

#### `addHealthCheck`

  * **Method** : `v1.compute.targetPools.addHealthCheck`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.httpHealthChecks.useReadOnly - ADMIN_READ`
    * `compute.targetPools.addHealthCheck - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.addHealthCheck" `  




#### `addInstance`

  * **Method** : `v1.compute.targetPools.addInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.use - ADMIN_WRITE`
    * `compute.targetPools.addInstance - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.addInstance" `  




#### `aggregatedList`

  * **Method** : `v1.compute.targetPools.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetPools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.targetPools.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetPools.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.delete" `  




#### `get`

  * **Method** : `v1.compute.targetPools.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetPools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.get" `  




#### `getHealth`

  * **Method** : `v1.compute.targetPools.getHealth`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetPools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.getHealth" `  




#### `insert`

  * **Method** : `v1.compute.targetPools.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.httpHealthChecks.useReadOnly - ADMIN_READ`
    * `compute.instances.use - ADMIN_WRITE`
    * `compute.targetPools.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.insert" `  




#### `list`

  * **Method** : `v1.compute.targetPools.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.targetPools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.list" `  




#### `removeHealthCheck`

  * **Method** : `v1.compute.targetPools.removeHealthCheck`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.httpHealthChecks.useReadOnly - ADMIN_READ`
    * `compute.targetPools.removeHealthCheck - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.removeHealthCheck" `  




#### `removeInstance`

  * **Method** : `v1.compute.targetPools.removeInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.instances.use - ADMIN_WRITE`
    * `compute.targetPools.removeInstance - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.removeInstance" `  




#### `setBackup`

  * **Method** : `v1.compute.targetPools.setBackup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.targetPools.update - ADMIN_WRITE`
    * `compute.targetPools.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.setBackup" `  




#### `setSecurityPolicy`

  * **Method** : `v1.compute.targetPools.setSecurityPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.regionSecurityPolicies.use - ADMIN_WRITE`
    * `compute.targetPools.setSecurityPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.targetPools.setSecurityPolicy" `  




### `compute.v1.UrlMapsService`

The following audit logs are associated with methods belonging to `compute.v1.UrlMapsService`.

#### `aggregatedList`

  * **Method** : `v1.compute.urlMaps.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.urlMaps.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.urlMaps.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.urlMaps.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.urlMaps.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.urlMaps.delete" `  




#### `get`

  * **Method** : `v1.compute.urlMaps.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.urlMaps.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.urlMaps.get" `  




#### `insert`

  * **Method** : `v1.compute.urlMaps.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.use - ADMIN_WRITE`
    * `compute.urlMaps.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.urlMaps.insert" `  




#### `invalidateCache`

  * **Method** : `v1.compute.urlMaps.invalidateCache`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.urlMaps.invalidateCache - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.urlMaps.invalidateCache" `  




#### `list`

  * **Method** : `v1.compute.urlMaps.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.urlMaps.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.urlMaps.list" `  




#### `patch`

  * **Method** : `v1.compute.urlMaps.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.use - ADMIN_WRITE`
    * `compute.urlMaps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.urlMaps.patch" `  




#### `update`

  * **Method** : `v1.compute.urlMaps.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.backendServices.use - ADMIN_WRITE`
    * `compute.urlMaps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.urlMaps.update" `  




#### `validate`

  * **Method** : `v1.compute.urlMaps.validate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.backendBuckets.use - ADMIN_WRITE`
    * `compute.backendServices.use - ADMIN_WRITE`
    * `compute.urlMaps.validate - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.urlMaps.validate" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
