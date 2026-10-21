---
url: https://docs.cloud.google.com/vpc/docs/audit-logging/
title: Virtual Private Cloud audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:10.318454+00:00
---

# Virtual Private Cloud audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Virtual Private Cloud audit logging

This document describes audit logging for Virtual Private Cloud. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Notes

The following methods that start with `google.cloud.networkconnectivity.v1.PolicyBasedRoutingService` use the service name `networkconnectivity.googleapis.com`.

## Service name

Virtual Private Cloud audit logs use the service name `compute.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="compute.googleapis.com"
      

## Methods by permission type

For the following API methods, there is also a `beta` and `alpha` version available that is not listed here. When the `beta` or `alpha` version of the API is called the method name will start with `beta` or `alpha` respectively.

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Virtual Private Cloud generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

Permission type | Methods  
---|---  
`ADMIN_READ` | `v1.compute.firewalls.get`  
`v1.compute.firewalls.list`  
`v1.compute.networks.get`  
`v1.compute.networks.getEffectiveFirewalls`  
`v1.compute.networks.list`  
`v1.compute.networks.listPeeringRoutes`  
`v1.compute.forwardingRules.aggregatedList`  
`v1.compute.forwardingRules.get`  
`v1.compute.forwardingRules.list`  
`v1.compute.routes.get`  
`v1.compute.routes.list`  
`v1.compute.subnetworks.aggregatedList`  
`v1.compute.subnetworks.get`  
`v1.compute.subnetworks.getIamPolicy`  
`v1.compute.subnetworks.list`  
`v1.compute.subnetworks.testIamPermissions`  
`ADMIN_WRITE` | `v1.compute.firewalls.delete`  
`v1.compute.firewalls.insert`  
`v1.compute.firewalls.patch`  
`v1.compute.firewalls.update`  
`v1.compute.networks.addPeering`  
`v1.compute.networks.delete`  
`v1.compute.networks.insert`  
`v1.compute.networks.patch`  
`v1.compute.networks.removePeering`  
`v1.compute.networks.switchToCustomMode`  
`v1.compute.networks.updatePeering`  
`v1.compute.forwardingRules.delete`  
`v1.compute.forwardingRules.insert`  
`v1.compute.forwardingRules.patch`  
`v1.compute.forwardingRules.setLabels`  
`v1.compute.forwardingRules.setTarget`  
`v1.compute.routes.delete`  
`v1.compute.routes.insert`  
`v1.compute.subnetworks.delete`  
`v1.compute.subnetworks.expandIpCidrRange`  
`v1.compute.subnetworks.insert`  
`v1.compute.subnetworks.patch`  
`v1.compute.subnetworks.setIamPolicy`  
`v1.compute.subnetworks.setPrivateIpGoogleAccess`  
`google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.CreatePolicyBasedRoute`  
`google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.DeletePolicyBasedRoute`  
`OTHER` | `google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.GetPolicyBasedRoute`: To enable this log, enable `ADMIN_READ` under the service `networkconnectivity.googleapis.com`.  
`google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.ListPolicyBasedRoutes`: To enable this log, enable `ADMIN_READ` under the service `networkconnectivity.googleapis.com`.  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Virtual Private Cloud.

### `compute.v1.FirewallsService`

The following audit logs are associated with methods belonging to `compute.v1.FirewallsService`.

#### `delete`

  * **Method** : `v1.compute.firewalls.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewalls.delete - ADMIN_WRITE`
    * `compute.networks.updatePolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewalls.delete" `  




#### `get`

  * **Method** : `v1.compute.firewalls.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.firewalls.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewalls.get" `  




#### `insert`

  * **Method** : `v1.compute.firewalls.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewalls.create - ADMIN_WRITE`
    * `compute.networks.updatePolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewalls.insert" `  




#### `list`

  * **Method** : `v1.compute.firewalls.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.firewalls.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewalls.list" `  




#### `patch`

  * **Method** : `v1.compute.firewalls.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewalls.get - ADMIN_READ`
    * `compute.firewalls.update - ADMIN_WRITE`
    * `compute.networks.updatePolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewalls.patch" `  




#### `update`

  * **Method** : `v1.compute.firewalls.update`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.firewalls.update - ADMIN_WRITE`
    * `compute.networks.updatePolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.firewalls.update" `  




### `compute.v1.NetworksService`

The following audit logs are associated with methods belonging to `compute.v1.NetworksService`.

#### `addPeering`

  * **Method** : `v1.compute.networks.addPeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.addPeering - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.addPeering" `  




#### `delete`

  * **Method** : `v1.compute.networks.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.delete" `  




#### `get`

  * **Method** : `v1.compute.networks.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.get" `  




#### `getEffectiveFirewalls`

  * **Method** : `v1.compute.networks.getEffectiveFirewalls`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networks.getEffectiveFirewalls - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.getEffectiveFirewalls" `  




#### `insert`

  * **Method** : `v1.compute.networks.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.insert" `  




#### `list`

  * **Method** : `v1.compute.networks.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.list" `  




#### `listPeeringRoutes`

  * **Method** : `v1.compute.networks.listPeeringRoutes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.networks.listPeeringRoutes - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.listPeeringRoutes" `  




#### `patch`

  * **Method** : `v1.compute.networks.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.get - ADMIN_READ`
    * `compute.networks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.patch" `  




#### `removePeering`

  * **Method** : `v1.compute.networks.removePeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.removePeering - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.removePeering" `  




#### `switchToCustomMode`

  * **Method** : `v1.compute.networks.switchToCustomMode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.switchToCustomMode - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.switchToCustomMode" `  




#### `updatePeering`

  * **Method** : `v1.compute.networks.updatePeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.updatePeering - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.networks.updatePeering" `  




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




### `compute.v1.RoutesService`

The following audit logs are associated with methods belonging to `compute.v1.RoutesService`.

#### `delete`

  * **Method** : `v1.compute.routes.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.routes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routes.delete" `  




#### `get`

  * **Method** : `v1.compute.routes.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routes.get" `  




#### `insert`

  * **Method** : `v1.compute.routes.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.updatePolicy - ADMIN_WRITE`
    * `compute.routes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routes.insert" `  




#### `list`

  * **Method** : `v1.compute.routes.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.routes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.routes.list" `  




### `compute.v1.SubnetworksService`

The following audit logs are associated with methods belonging to `compute.v1.SubnetworksService`.

#### `aggregatedList`

  * **Method** : `v1.compute.subnetworks.aggregatedList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.subnetworks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.aggregatedList" `  




#### `delete`

  * **Method** : `v1.compute.subnetworks.delete`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.subnetworks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.delete" `  




#### `expandIpCidrRange`

  * **Method** : `v1.compute.subnetworks.expandIpCidrRange`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.subnetworks.expandIpCidrRange - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.expandIpCidrRange" `  




#### `get`

  * **Method** : `v1.compute.subnetworks.get`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.subnetworks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.get" `  




#### `getIamPolicy`

  * **Method** : `v1.compute.subnetworks.getIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.subnetworks.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.getIamPolicy" `  




#### `insert`

  * **Method** : `v1.compute.subnetworks.insert`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.networks.updatePolicy - ADMIN_WRITE`
    * `compute.subnetworks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.insert" `  




#### `list`

  * **Method** : `v1.compute.subnetworks.list`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.subnetworks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.list" `  




#### `patch`

  * **Method** : `v1.compute.subnetworks.patch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.subnetworks.get - ADMIN_READ`
    * `compute.subnetworks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.patch" `  




#### `setIamPolicy`

  * **Method** : `v1.compute.subnetworks.setIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.subnetworks.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.setIamPolicy" `  




#### `setPrivateIpGoogleAccess`

  * **Method** : `v1.compute.subnetworks.setPrivateIpGoogleAccess`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `compute.subnetworks.setPrivateIpGoogleAccess - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.setPrivateIpGoogleAccess" `  




#### `testIamPermissions`

  * **Method** : `v1.compute.subnetworks.testIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `compute.subnetworks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="v1.compute.subnetworks.testIamPermissions" `  




### `google.cloud.networkconnectivity.v1.PolicyBasedRoutingService`

The following audit logs are associated with methods belonging to `google.cloud.networkconnectivity.v1.PolicyBasedRoutingService`.

#### `CreatePolicyBasedRoute`

  * **Method** : `google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.CreatePolicyBasedRoute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.policyBasedRoutes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.CreatePolicyBasedRoute" `  




#### `DeletePolicyBasedRoute`

  * **Method** : `google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.DeletePolicyBasedRoute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.policyBasedRoutes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.DeletePolicyBasedRoute" `  




#### `GetPolicyBasedRoute`

  * **Method** : `google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.GetPolicyBasedRoute`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.policyBasedRoutes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.GetPolicyBasedRoute" `  




#### `ListPolicyBasedRoutes`

  * **Method** : `google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.ListPolicyBasedRoutes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.policyBasedRoutes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.ListPolicyBasedRoutes" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
