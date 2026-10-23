---
url: https://docs.cloud.google.com/vmware-engine/docs/audit-logging/
title: Google Cloud VMware Engine audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:36.658834+00:00
---

# Google Cloud VMware Engine audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google Cloud VMware Engine audit logging

This document describes audit logging for Google Cloud VMware Engine. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Google Cloud VMware Engine audit logs use the service name `vmwareengine.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="vmwareengine.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Google Cloud VMware Engine generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.vmwareengine.v1.VmwareEngine.FetchNetworkPolicyExternalAddresses`  
`google.cloud.vmwareengine.v1.VmwareEngine.GetCluster`  
`google.cloud.vmwareengine.v1.VmwareEngine.GetDnsBindPermission`  
`google.cloud.vmwareengine.v1.VmwareEngine.GetDnsForwarding`  
`google.cloud.vmwareengine.v1.VmwareEngine.GetExternalAccessRule`  
`google.cloud.vmwareengine.v1.VmwareEngine.GetExternalAddress`  
`google.cloud.vmwareengine.v1.VmwareEngine.GetHcxActivationKey`  
`google.cloud.vmwareengine.v1.VmwareEngine.GetLoggingServer`  
`google.cloud.vmwareengine.v1.VmwareEngine.GetManagementDnsZoneBinding`  
`google.cloud.vmwareengine.v1.VmwareEngine.GetNetworkPeering`  
`google.cloud.vmwareengine.v1.VmwareEngine.GetNetworkPolicy`  
`google.cloud.vmwareengine.v1.VmwareEngine.GetNode`  
`google.cloud.vmwareengine.v1.VmwareEngine.GetNodeType`  
`google.cloud.vmwareengine.v1.VmwareEngine.GetPrivateCloud`  
`google.cloud.vmwareengine.v1.VmwareEngine.GetPrivateConnection`  
`google.cloud.vmwareengine.v1.VmwareEngine.GetSubnet`  
`google.cloud.vmwareengine.v1.VmwareEngine.GetVmwareEngineNetwork`  
`google.cloud.vmwareengine.v1.VmwareEngine.ListClusters`  
`google.cloud.vmwareengine.v1.VmwareEngine.ListExternalAccessRules`  
`google.cloud.vmwareengine.v1.VmwareEngine.ListExternalAddresses`  
`google.cloud.vmwareengine.v1.VmwareEngine.ListHcxActivationKeys`  
`google.cloud.vmwareengine.v1.VmwareEngine.ListLoggingServers`  
`google.cloud.vmwareengine.v1.VmwareEngine.ListManagementDnsZoneBindings`  
`google.cloud.vmwareengine.v1.VmwareEngine.ListNetworkPeerings`  
`google.cloud.vmwareengine.v1.VmwareEngine.ListNetworkPolicies`  
`google.cloud.vmwareengine.v1.VmwareEngine.ListNodeTypes`  
`google.cloud.vmwareengine.v1.VmwareEngine.ListNodes`  
`google.cloud.vmwareengine.v1.VmwareEngine.ListPeeringRoutes`  
`google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateClouds`  
`google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateConnectionPeeringRoutes`  
`google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateConnections`  
`google.cloud.vmwareengine.v1.VmwareEngine.ListSubnets`  
`google.cloud.vmwareengine.v1.VmwareEngine.ListVmwareEngineNetworks`  
`google.cloud.vmwareengine.v1.VmwareEngine.ShowNsxCredentials`  
`google.cloud.vmwareengine.v1.VmwareEngine.ShowVcenterCredentials`  
`GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.vmwareengine.v1.VmwareEngine.CreateCluster` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.CreateExternalAccessRule` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.CreateExternalAddress` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.CreateHcxActivationKey` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.CreateLoggingServer` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.CreateManagementDnsZoneBinding` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.CreateNetworkPeering` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.CreateNetworkPolicy` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.CreatePrivateCloud` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.CreatePrivateConnection` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.CreateVmwareEngineNetwork` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.DeleteCluster` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.DeleteExternalAccessRule` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.DeleteExternalAddress` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.DeleteLoggingServer` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.DeleteManagementDnsZoneBinding` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.DeleteNetworkPeering` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.DeleteNetworkPolicy` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.DeletePrivateCloud` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.DeletePrivateConnection` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.DeleteVmwareEngineNetwork` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.GrantDnsBindPermission` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.RepairManagementDnsZoneBinding`  
`google.cloud.vmwareengine.v1.VmwareEngine.ResetNsxCredentials` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.ResetVcenterCredentials` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.RevokeDnsBindPermission` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.UndeletePrivateCloud` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.UpdateCluster` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.UpdateDnsForwarding` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.UpdateExternalAccessRule` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.UpdateExternalAddress` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.UpdateLoggingServer` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.UpdateManagementDnsZoneBinding` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.UpdateNetworkPeering` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.UpdateNetworkPolicy` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.UpdatePrivateCloud` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.UpdatePrivateConnection` (LRO)  
`google.cloud.vmwareengine.v1.VmwareEngine.UpdateSubnet`  
`google.cloud.vmwareengine.v1.VmwareEngine.UpdateVmwareEngineNetwork` (LRO)  
`SetIamPolicy`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Google Cloud VMware Engine.

### `google.cloud.vmwareengine.v1.VmwareEngine`

The following audit logs are associated with methods belonging to `google.cloud.vmwareengine.v1.VmwareEngine`.

#### `CreateCluster`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.CreateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.CreateCluster" `  




#### `CreateExternalAccessRule`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.CreateExternalAccessRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.externalAccessRules.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.CreateExternalAccessRule" `  




#### `CreateExternalAddress`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.CreateExternalAddress`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.externalAddresses.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.CreateExternalAddress" `  




#### `CreateHcxActivationKey`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.CreateHcxActivationKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.hcxActivationKeys.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.CreateHcxActivationKey" `  




#### `CreateLoggingServer`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.CreateLoggingServer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.loggingServers.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.CreateLoggingServer" `  




#### `CreateManagementDnsZoneBinding`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.CreateManagementDnsZoneBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.managementDnsZoneBindings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.CreateManagementDnsZoneBinding" `  




#### `CreateNetworkPeering`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.CreateNetworkPeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.networkPeerings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.CreateNetworkPeering" `  




#### `CreateNetworkPolicy`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.CreateNetworkPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.networkPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.CreateNetworkPolicy" `  




#### `CreatePrivateCloud`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.CreatePrivateCloud`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.privateClouds.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.CreatePrivateCloud" `  




#### `CreatePrivateConnection`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.CreatePrivateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.privateConnections.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.CreatePrivateConnection" `  




#### `CreateVmwareEngineNetwork`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.CreateVmwareEngineNetwork`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.vmwareEngineNetworks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.CreateVmwareEngineNetwork" `  




#### `DeleteCluster`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.DeleteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.clusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.DeleteCluster" `  




#### `DeleteExternalAccessRule`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.DeleteExternalAccessRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.externalAccessRules.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.DeleteExternalAccessRule" `  




#### `DeleteExternalAddress`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.DeleteExternalAddress`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.externalAddresses.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.DeleteExternalAddress" `  




#### `DeleteLoggingServer`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.DeleteLoggingServer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.loggingServers.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.DeleteLoggingServer" `  




#### `DeleteManagementDnsZoneBinding`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.DeleteManagementDnsZoneBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.managementDnsZoneBindings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.DeleteManagementDnsZoneBinding" `  




#### `DeleteNetworkPeering`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.DeleteNetworkPeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.networkPeerings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.DeleteNetworkPeering" `  




#### `DeleteNetworkPolicy`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.DeleteNetworkPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.networkPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.DeleteNetworkPolicy" `  




#### `DeletePrivateCloud`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.DeletePrivateCloud`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.privateClouds.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.DeletePrivateCloud" `  




#### `DeletePrivateConnection`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.DeletePrivateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.privateConnections.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.DeletePrivateConnection" `  




#### `DeleteVmwareEngineNetwork`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.DeleteVmwareEngineNetwork`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.vmwareEngineNetworks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.DeleteVmwareEngineNetwork" `  




#### `FetchNetworkPolicyExternalAddresses`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.FetchNetworkPolicyExternalAddresses`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.networkPolicies.fetchExternalAddresses - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.FetchNetworkPolicyExternalAddresses" `  




#### `GetCluster`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.GetCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.GetCluster" `  




#### `GetDnsBindPermission`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.GetDnsBindPermission`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.dnsBindPermission.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.GetDnsBindPermission" `  




#### `GetDnsForwarding`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.GetDnsForwarding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.dnsForwarding.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.GetDnsForwarding" `  




#### `GetExternalAccessRule`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.GetExternalAccessRule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.externalAccessRules.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.GetExternalAccessRule" `  




#### `GetExternalAddress`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.GetExternalAddress`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.externalAddresses.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.GetExternalAddress" `  




#### `GetHcxActivationKey`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.GetHcxActivationKey`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.hcxActivationKeys.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.GetHcxActivationKey" `  




#### `GetLoggingServer`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.GetLoggingServer`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.loggingServers.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.GetLoggingServer" `  




#### `GetManagementDnsZoneBinding`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.GetManagementDnsZoneBinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.managementDnsZoneBindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.GetManagementDnsZoneBinding" `  




#### `GetNetworkPeering`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.GetNetworkPeering`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.networkPeerings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.GetNetworkPeering" `  




#### `GetNetworkPolicy`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.GetNetworkPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.networkPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.GetNetworkPolicy" `  




#### `GetNode`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.GetNode`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.nodes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.GetNode" `  




#### `GetNodeType`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.GetNodeType`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.nodeTypes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.GetNodeType" `  




#### `GetPrivateCloud`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.GetPrivateCloud`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.privateClouds.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.GetPrivateCloud" `  




#### `GetPrivateConnection`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.GetPrivateConnection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.privateConnections.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.GetPrivateConnection" `  




#### `GetSubnet`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.GetSubnet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.subnets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.GetSubnet" `  




#### `GetVmwareEngineNetwork`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.GetVmwareEngineNetwork`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.vmwareEngineNetworks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.GetVmwareEngineNetwork" `  




#### `GrantDnsBindPermission`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.GrantDnsBindPermission`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.dnsBindPermission.grant - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.GrantDnsBindPermission" `  




#### `ListClusters`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.ListClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.clusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.ListClusters" `  




#### `ListExternalAccessRules`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.ListExternalAccessRules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.externalAccessRules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.ListExternalAccessRules" `  




#### `ListExternalAddresses`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.ListExternalAddresses`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.externalAddresses.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.ListExternalAddresses" `  




#### `ListHcxActivationKeys`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.ListHcxActivationKeys`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.hcxActivationKeys.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.ListHcxActivationKeys" `  




#### `ListLoggingServers`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.ListLoggingServers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.loggingServers.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.ListLoggingServers" `  




#### `ListManagementDnsZoneBindings`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.ListManagementDnsZoneBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.managementDnsZoneBindings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.ListManagementDnsZoneBindings" `  




#### `ListNetworkPeerings`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.ListNetworkPeerings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.networkPeerings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.ListNetworkPeerings" `  




#### `ListNetworkPolicies`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.ListNetworkPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.networkPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.ListNetworkPolicies" `  




#### `ListNodeTypes`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.ListNodeTypes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.nodeTypes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.ListNodeTypes" `  




#### `ListNodes`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.ListNodes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.nodes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.ListNodes" `  




#### `ListPeeringRoutes`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.ListPeeringRoutes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.networkPeerings.listPeeringRoutes - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.ListPeeringRoutes" `  




#### `ListPrivateClouds`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateClouds`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.privateClouds.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateClouds" `  




#### `ListPrivateConnectionPeeringRoutes`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateConnectionPeeringRoutes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.privateConnections.listPeeringRoutes - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateConnectionPeeringRoutes" `  




#### `ListPrivateConnections`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateConnections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.privateConnections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateConnections" `  




#### `ListSubnets`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.ListSubnets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.subnets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.ListSubnets" `  




#### `ListVmwareEngineNetworks`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.ListVmwareEngineNetworks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.vmwareEngineNetworks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.ListVmwareEngineNetworks" `  




#### `RepairManagementDnsZoneBinding`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.RepairManagementDnsZoneBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.managementDnsZoneBindings.repair - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.RepairManagementDnsZoneBinding" `  




#### `ResetNsxCredentials`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.ResetNsxCredentials`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.privateClouds.resetNsxCredentials - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.ResetNsxCredentials" `  




#### `ResetVcenterCredentials`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.ResetVcenterCredentials`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.privateClouds.resetVcenterCredentials - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.ResetVcenterCredentials" `  




#### `RevokeDnsBindPermission`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.RevokeDnsBindPermission`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.dnsBindPermission.revoke - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.RevokeDnsBindPermission" `  




#### `ShowNsxCredentials`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.ShowNsxCredentials`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.privateClouds.showNsxCredentials - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.ShowNsxCredentials" `  




#### `ShowVcenterCredentials`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.ShowVcenterCredentials`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.privateClouds.showVcenterCredentials - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.ShowVcenterCredentials" `  




#### `UndeletePrivateCloud`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.UndeletePrivateCloud`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.privateClouds.undelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.UndeletePrivateCloud" `  




#### `UpdateCluster`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.UpdateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.UpdateCluster" `  




#### `UpdateDnsForwarding`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.UpdateDnsForwarding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.dnsForwarding.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.UpdateDnsForwarding" `  




#### `UpdateExternalAccessRule`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.UpdateExternalAccessRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.externalAccessRules.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.UpdateExternalAccessRule" `  




#### `UpdateExternalAddress`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.UpdateExternalAddress`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.externalAddresses.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.UpdateExternalAddress" `  




#### `UpdateLoggingServer`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.UpdateLoggingServer`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.loggingServers.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.UpdateLoggingServer" `  




#### `UpdateManagementDnsZoneBinding`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.UpdateManagementDnsZoneBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.managementDnsZoneBindings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.UpdateManagementDnsZoneBinding" `  




#### `UpdateNetworkPeering`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.UpdateNetworkPeering`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.networkPeerings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.UpdateNetworkPeering" `  




#### `UpdateNetworkPolicy`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.UpdateNetworkPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.networkPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.UpdateNetworkPolicy" `  




#### `UpdatePrivateCloud`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.UpdatePrivateCloud`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.privateClouds.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.UpdatePrivateCloud" `  




#### `UpdatePrivateConnection`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.UpdatePrivateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.privateConnections.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.UpdatePrivateConnection" `  




#### `UpdateSubnet`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.UpdateSubnet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.subnets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.UpdateSubnet" `  




#### `UpdateVmwareEngineNetwork`

  * **Method** : `google.cloud.vmwareengine.v1.VmwareEngine.UpdateVmwareEngineNetwork`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.vmwareEngineNetworks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.vmwareengine.v1.VmwareEngine.UpdateVmwareEngineNetwork" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.privateClouds.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.clusters.setIamPolicy - ADMIN_WRITE`
    * `vmwareengine.hcxActivationKeys.setIamPolicy - ADMIN_WRITE`
    * `vmwareengine.privateClouds.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `vmwareengine.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `vmwareengine.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## System events

System Event audit logs are generated by GCP systems, not direct user action. For more information, see [System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event).

Method Name | Filter For This Event | Notes  
---|---|---  
system.privateCloud.addNodes |  ` protoPayload.methodName="system.privateCloud.addNodes" ` |   
  
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

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
