---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/audit-logging/
title: Network Connectivity Center audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:45.048769+00:00
---

# Network Connectivity Center audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Network Connectivity Center audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Network Connectivity Center. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Network Connectivity Center audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="networkconnectivity.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Network Connectivity Center generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetAutomatedDnsRecord`  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetPscAuthorizationPolicy`  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetServiceClass`  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetServiceConnectionMap`  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetServiceConnectionPolicy`  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetServiceConnectionToken`  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListAutomatedDnsRecords`  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListPscAuthorizationPolicies`  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListServiceClasses`  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListServiceConnectionMaps`  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListServiceConnectionPolicies`  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListServiceConnectionTokens`  
`google.cloud.networkconnectivity.v1.DataTransferService.GetDestination`  
`google.cloud.networkconnectivity.v1.DataTransferService.GetMulticloudDataTransferConfig`  
`google.cloud.networkconnectivity.v1.DataTransferService.GetMulticloudDataTransferSupportedService`  
`google.cloud.networkconnectivity.v1.DataTransferService.ListDestinations`  
`google.cloud.networkconnectivity.v1.DataTransferService.ListMulticloudDataTransferConfigs`  
`google.cloud.networkconnectivity.v1.DataTransferService.ListMulticloudDataTransferSupportedServices`  
`google.cloud.networkconnectivity.v1.HubService.GetGatewayAdvertisedRoute`  
`google.cloud.networkconnectivity.v1.HubService.GetGroup`  
`google.cloud.networkconnectivity.v1.HubService.GetHub`  
`google.cloud.networkconnectivity.v1.HubService.GetRoute`  
`google.cloud.networkconnectivity.v1.HubService.GetRouteTable`  
`google.cloud.networkconnectivity.v1.HubService.GetSpoke`  
`google.cloud.networkconnectivity.v1.HubService.ListGatewayAdvertisedRoutes`  
`google.cloud.networkconnectivity.v1.HubService.ListGroups`  
`google.cloud.networkconnectivity.v1.HubService.ListHubSpokes`  
`google.cloud.networkconnectivity.v1.HubService.ListHubs`  
`google.cloud.networkconnectivity.v1.HubService.ListRouteTables`  
`google.cloud.networkconnectivity.v1.HubService.ListRoutes`  
`google.cloud.networkconnectivity.v1.HubService.ListSpokes`  
`google.cloud.networkconnectivity.v1.HubService.QueryHubStatus`  
`google.cloud.networkconnectivity.v1.InternalRangeService.GetInternalRange`  
`google.cloud.networkconnectivity.v1.InternalRangeService.ListInternalRanges`  
`google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.GetPolicyBasedRoute`  
`google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.ListPolicyBasedRoutes`  
`google.cloud.networkconnectivity.v1.RegionalEndpointService.GetRegionalEndpoint`  
`google.cloud.networkconnectivity.v1.RegionalEndpointService.ListRegionalEndpoints`  
`google.cloud.networkconnectivity.v1.TransportManager.GetRemoteTransportProfile`  
`google.cloud.networkconnectivity.v1.TransportManager.GetTransport`  
`google.cloud.networkconnectivity.v1.TransportManager.ListRemoteTransportProfiles`  
`google.cloud.networkconnectivity.v1.TransportManager.ListTransports`  
`google.cloud.networkconnectivity.v1alpha1.HubService.GetHub`  
`google.cloud.networkconnectivity.v1alpha1.HubService.GetSpoke`  
`google.cloud.networkconnectivity.v1alpha1.HubService.ListHubs`  
`google.cloud.networkconnectivity.v1alpha1.HubService.ListSpokes`  
`google.cloud.networkconnectivity.v1alpha1.InternalRangeService.GetInternalRange`  
`google.cloud.networkconnectivity.v1alpha1.InternalRangeService.ListInternalRanges`  
`google.cloud.networkconnectivity.v1beta.DataTransferService.GetDestination`  
`google.cloud.networkconnectivity.v1beta.DataTransferService.GetMulticloudDataTransferConfig`  
`google.cloud.networkconnectivity.v1beta.DataTransferService.GetMulticloudDataTransferSupportedService`  
`google.cloud.networkconnectivity.v1beta.DataTransferService.ListDestinations`  
`google.cloud.networkconnectivity.v1beta.DataTransferService.ListMulticloudDataTransferConfigs`  
`google.cloud.networkconnectivity.v1beta.DataTransferService.ListMulticloudDataTransferSupportedServices`  
`google.cloud.networkconnectivity.v1beta.HubService.GetGatewayAdvertisedRoute`  
`google.cloud.networkconnectivity.v1beta.HubService.GetGroup`  
`google.cloud.networkconnectivity.v1beta.HubService.GetHub`  
`google.cloud.networkconnectivity.v1beta.HubService.GetRoute`  
`google.cloud.networkconnectivity.v1beta.HubService.GetRouteTable`  
`google.cloud.networkconnectivity.v1beta.HubService.GetSpoke`  
`google.cloud.networkconnectivity.v1beta.HubService.ListGatewayAdvertisedRoutes`  
`google.cloud.networkconnectivity.v1beta.HubService.ListGroups`  
`google.cloud.networkconnectivity.v1beta.HubService.ListHubSpokes`  
`google.cloud.networkconnectivity.v1beta.HubService.ListHubs`  
`google.cloud.networkconnectivity.v1beta.HubService.ListRouteTables`  
`google.cloud.networkconnectivity.v1beta.HubService.ListRoutes`  
`google.cloud.networkconnectivity.v1beta.HubService.ListSpokes`  
`google.cloud.networkconnectivity.v1beta.HubService.QueryHubStatus`  
`google.cloud.networkconnectivity.v1beta.PolicyBasedRoutingService.GetPolicyBasedRoute`  
`google.cloud.networkconnectivity.v1beta.PolicyBasedRoutingService.ListPolicyBasedRoutes`  
`google.cloud.networkconnectivity.v1beta.RegionalEndpointService.GetRegionalEndpoint`  
`google.cloud.networkconnectivity.v1beta.RegionalEndpointService.ListRegionalEndpoints`  
`google.cloud.networkconnectivity.v1beta.TransportManager.GetRemoteTransportProfile`  
`google.cloud.networkconnectivity.v1beta.TransportManager.GetStatus`  
`google.cloud.networkconnectivity.v1beta.TransportManager.GetTransport`  
`google.cloud.networkconnectivity.v1beta.TransportManager.ListRemoteTransportProfiles`  
`google.cloud.networkconnectivity.v1beta.TransportManager.ListTransports`  
`google.cloud.networkconnectivity.v1beta.TransportManager.ParseFromActivationKey`  
`GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CheckConsumerConfig`  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CreateAutomatedDnsRecord` (LRO)  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CreatePscAuthorizationPolicy` (LRO)  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CreateServiceConnectionMap` (LRO)  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CreateServiceConnectionPolicy` (LRO)  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CreateServiceConnectionToken` (LRO)  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeleteAutomatedDnsRecord` (LRO)  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeletePscAuthorizationPolicy` (LRO)  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeleteServiceClass` (LRO)  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeleteServiceConnectionMap` (LRO)  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeleteServiceConnectionPolicy` (LRO)  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeleteServiceConnectionToken` (LRO)  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.UpdateServiceClass` (LRO)  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.UpdateServiceConnectionMap` (LRO)  
`google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.UpdateServiceConnectionPolicy` (LRO)  
`google.cloud.networkconnectivity.v1.DataTransferService.CreateDestination` (LRO)  
`google.cloud.networkconnectivity.v1.DataTransferService.CreateMulticloudDataTransferConfig` (LRO)  
`google.cloud.networkconnectivity.v1.DataTransferService.DeleteDestination` (LRO)  
`google.cloud.networkconnectivity.v1.DataTransferService.DeleteMulticloudDataTransferConfig` (LRO)  
`google.cloud.networkconnectivity.v1.DataTransferService.UpdateDestination` (LRO)  
`google.cloud.networkconnectivity.v1.DataTransferService.UpdateMulticloudDataTransferConfig` (LRO)  
`google.cloud.networkconnectivity.v1.HubService.AcceptHubSpoke` (LRO)  
`google.cloud.networkconnectivity.v1.HubService.AcceptSpokeUpdate` (LRO)  
`google.cloud.networkconnectivity.v1.HubService.CreateGatewayAdvertisedRoute` (LRO)  
`google.cloud.networkconnectivity.v1.HubService.CreateHub` (LRO)  
`google.cloud.networkconnectivity.v1.HubService.CreateSpoke` (LRO)  
`google.cloud.networkconnectivity.v1.HubService.DeleteGatewayAdvertisedRoute` (LRO)  
`google.cloud.networkconnectivity.v1.HubService.DeleteHub` (LRO)  
`google.cloud.networkconnectivity.v1.HubService.DeleteSpoke` (LRO)  
`google.cloud.networkconnectivity.v1.HubService.RejectHubSpoke` (LRO)  
`google.cloud.networkconnectivity.v1.HubService.RejectSpokeUpdate` (LRO)  
`google.cloud.networkconnectivity.v1.HubService.UpdateGatewayAdvertisedRoute` (LRO)  
`google.cloud.networkconnectivity.v1.HubService.UpdateGroup` (LRO)  
`google.cloud.networkconnectivity.v1.HubService.UpdateHub` (LRO)  
`google.cloud.networkconnectivity.v1.HubService.UpdateSpoke` (LRO)  
`google.cloud.networkconnectivity.v1.InternalRangeService.CreateInternalRange` (LRO)  
`google.cloud.networkconnectivity.v1.InternalRangeService.DeleteInternalRange` (LRO)  
`google.cloud.networkconnectivity.v1.InternalRangeService.UpdateInternalRange` (LRO)  
`google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.CreatePolicyBasedRoute` (LRO)  
`google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.DeletePolicyBasedRoute` (LRO)  
`google.cloud.networkconnectivity.v1.RegionalEndpointService.CreateRegionalEndpoint` (LRO)  
`google.cloud.networkconnectivity.v1.RegionalEndpointService.DeleteRegionalEndpoint` (LRO)  
`google.cloud.networkconnectivity.v1.TransportManager.CreateTransport` (LRO)  
`google.cloud.networkconnectivity.v1.TransportManager.DeleteTransport` (LRO)  
`google.cloud.networkconnectivity.v1.TransportManager.UpdateTransport` (LRO)  
`google.cloud.networkconnectivity.v1alpha1.HubService.CreateHub` (LRO)  
`google.cloud.networkconnectivity.v1alpha1.HubService.CreateSpoke` (LRO)  
`google.cloud.networkconnectivity.v1alpha1.HubService.DeleteHub` (LRO)  
`google.cloud.networkconnectivity.v1alpha1.HubService.DeleteSpoke` (LRO)  
`google.cloud.networkconnectivity.v1alpha1.HubService.UpdateHub` (LRO)  
`google.cloud.networkconnectivity.v1alpha1.HubService.UpdateSpoke` (LRO)  
`google.cloud.networkconnectivity.v1alpha1.InternalRangeService.CreateInternalRange` (LRO)  
`google.cloud.networkconnectivity.v1alpha1.InternalRangeService.DeleteInternalRange` (LRO)  
`google.cloud.networkconnectivity.v1alpha1.InternalRangeService.UpdateInternalRange` (LRO)  
`google.cloud.networkconnectivity.v1beta.DataTransferService.CreateDestination` (LRO)  
`google.cloud.networkconnectivity.v1beta.DataTransferService.CreateMulticloudDataTransferConfig` (LRO)  
`google.cloud.networkconnectivity.v1beta.DataTransferService.DeleteDestination` (LRO)  
`google.cloud.networkconnectivity.v1beta.DataTransferService.DeleteMulticloudDataTransferConfig` (LRO)  
`google.cloud.networkconnectivity.v1beta.DataTransferService.UpdateDestination` (LRO)  
`google.cloud.networkconnectivity.v1beta.DataTransferService.UpdateMulticloudDataTransferConfig` (LRO)  
`google.cloud.networkconnectivity.v1beta.HubService.AcceptHubSpoke` (LRO)  
`google.cloud.networkconnectivity.v1beta.HubService.AcceptSpokeUpdate` (LRO)  
`google.cloud.networkconnectivity.v1beta.HubService.CreateGatewayAdvertisedRoute` (LRO)  
`google.cloud.networkconnectivity.v1beta.HubService.CreateHub` (LRO)  
`google.cloud.networkconnectivity.v1beta.HubService.CreateSpoke` (LRO)  
`google.cloud.networkconnectivity.v1beta.HubService.DeleteGatewayAdvertisedRoute` (LRO)  
`google.cloud.networkconnectivity.v1beta.HubService.DeleteHub` (LRO)  
`google.cloud.networkconnectivity.v1beta.HubService.DeleteSpoke` (LRO)  
`google.cloud.networkconnectivity.v1beta.HubService.RejectHubSpoke` (LRO)  
`google.cloud.networkconnectivity.v1beta.HubService.UpdateGatewayAdvertisedRoute` (LRO)  
`google.cloud.networkconnectivity.v1beta.HubService.UpdateGroup` (LRO)  
`google.cloud.networkconnectivity.v1beta.HubService.UpdateHub` (LRO)  
`google.cloud.networkconnectivity.v1beta.HubService.UpdateSpoke` (LRO)  
`google.cloud.networkconnectivity.v1beta.PolicyBasedRoutingService.CreatePolicyBasedRoute` (LRO)  
`google.cloud.networkconnectivity.v1beta.PolicyBasedRoutingService.DeletePolicyBasedRoute` (LRO)  
`google.cloud.networkconnectivity.v1beta.RegionalEndpointService.CreateRegionalEndpoint` (LRO)  
`google.cloud.networkconnectivity.v1beta.RegionalEndpointService.DeleteRegionalEndpoint` (LRO)  
`google.cloud.networkconnectivity.v1beta.TransportManager.CreateTransport` (LRO)  
`google.cloud.networkconnectivity.v1beta.TransportManager.DeleteTransport` (LRO)  
`google.cloud.networkconnectivity.v1beta.TransportManager.UpdateTransport` (LRO)  
`SetIamPolicy`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Network Connectivity Center.

### `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService`

The following audit logs are associated with methods belonging to `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService`.

#### `CheckConsumerConfig`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CheckConsumerConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.serviceClasses.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CheckConsumerConfig" `  




#### `CreateAutomatedDnsRecord`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CreateAutomatedDnsRecord`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.automatedDnsRecords.create - ADMIN_WRITE`
    * `networkconnectivity.serviceClasses.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CreateAutomatedDnsRecord" `  




#### `CreatePscAuthorizationPolicy`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CreatePscAuthorizationPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.pscAuthorizationPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CreatePscAuthorizationPolicy" `  




#### `CreateServiceConnectionMap`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CreateServiceConnectionMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.serviceClasses.use - ADMIN_WRITE`
    * `networkconnectivity.serviceConnectionMaps.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CreateServiceConnectionMap" `  




#### `CreateServiceConnectionPolicy`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CreateServiceConnectionPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.serviceConnectionPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CreateServiceConnectionPolicy" `  




#### `CreateServiceConnectionToken`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CreateServiceConnectionToken`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.serviceConnectionTokens.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.CreateServiceConnectionToken" `  




#### `DeleteAutomatedDnsRecord`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeleteAutomatedDnsRecord`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.automatedDnsRecords.delete - ADMIN_WRITE`
    * `networkconnectivity.serviceClasses.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeleteAutomatedDnsRecord" `  




#### `DeletePscAuthorizationPolicy`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeletePscAuthorizationPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.pscAuthorizationPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeletePscAuthorizationPolicy" `  




#### `DeleteServiceClass`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeleteServiceClass`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.serviceClasses.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeleteServiceClass" `  




#### `DeleteServiceConnectionMap`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeleteServiceConnectionMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.serviceConnectionMaps.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeleteServiceConnectionMap" `  




#### `DeleteServiceConnectionPolicy`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeleteServiceConnectionPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.serviceConnectionPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeleteServiceConnectionPolicy" `  




#### `DeleteServiceConnectionToken`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeleteServiceConnectionToken`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.serviceConnectionTokens.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.DeleteServiceConnectionToken" `  




#### `GetAutomatedDnsRecord`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetAutomatedDnsRecord`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.automatedDnsRecords.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetAutomatedDnsRecord" `  




#### `GetPscAuthorizationPolicy`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetPscAuthorizationPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.pscAuthorizationPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetPscAuthorizationPolicy" `  




#### `GetServiceClass`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetServiceClass`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.serviceClasses.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetServiceClass" `  




#### `GetServiceConnectionMap`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetServiceConnectionMap`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.serviceConnectionMaps.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetServiceConnectionMap" `  




#### `GetServiceConnectionPolicy`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetServiceConnectionPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.serviceConnectionPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetServiceConnectionPolicy" `  




#### `GetServiceConnectionToken`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetServiceConnectionToken`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.serviceConnectionTokens.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.GetServiceConnectionToken" `  




#### `ListAutomatedDnsRecords`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListAutomatedDnsRecords`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.automatedDnsRecords.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListAutomatedDnsRecords" `  




#### `ListPscAuthorizationPolicies`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListPscAuthorizationPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.pscAuthorizationPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListPscAuthorizationPolicies" `  




#### `ListServiceClasses`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListServiceClasses`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.serviceClasses.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListServiceClasses" `  




#### `ListServiceConnectionMaps`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListServiceConnectionMaps`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.serviceConnectionMaps.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListServiceConnectionMaps" `  




#### `ListServiceConnectionPolicies`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListServiceConnectionPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.serviceConnectionPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListServiceConnectionPolicies" `  




#### `ListServiceConnectionTokens`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListServiceConnectionTokens`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.serviceConnectionTokens.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.ListServiceConnectionTokens" `  




#### `UpdateServiceClass`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.UpdateServiceClass`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.serviceClasses.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.UpdateServiceClass" `  




#### `UpdateServiceConnectionMap`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.UpdateServiceConnectionMap`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.serviceClasses.use - ADMIN_WRITE`
    * `networkconnectivity.serviceConnectionMaps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.UpdateServiceConnectionMap" `  




#### `UpdateServiceConnectionPolicy`

  * **Method** : `google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.UpdateServiceConnectionPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.serviceConnectionPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.CrossNetworkAutomationService.UpdateServiceConnectionPolicy" `  




### `google.cloud.networkconnectivity.v1.DataTransferService`

The following audit logs are associated with methods belonging to `google.cloud.networkconnectivity.v1.DataTransferService`.

#### `CreateDestination`

  * **Method** : `google.cloud.networkconnectivity.v1.DataTransferService.CreateDestination`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferDestinations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.DataTransferService.CreateDestination" `  




#### `CreateMulticloudDataTransferConfig`

  * **Method** : `google.cloud.networkconnectivity.v1.DataTransferService.CreateMulticloudDataTransferConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.DataTransferService.CreateMulticloudDataTransferConfig" `  




#### `DeleteDestination`

  * **Method** : `google.cloud.networkconnectivity.v1.DataTransferService.DeleteDestination`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferDestinations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.DataTransferService.DeleteDestination" `  




#### `DeleteMulticloudDataTransferConfig`

  * **Method** : `google.cloud.networkconnectivity.v1.DataTransferService.DeleteMulticloudDataTransferConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.DataTransferService.DeleteMulticloudDataTransferConfig" `  




#### `GetDestination`

  * **Method** : `google.cloud.networkconnectivity.v1.DataTransferService.GetDestination`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferDestinations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.DataTransferService.GetDestination" `  




#### `GetMulticloudDataTransferConfig`

  * **Method** : `google.cloud.networkconnectivity.v1.DataTransferService.GetMulticloudDataTransferConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.DataTransferService.GetMulticloudDataTransferConfig" `  




#### `GetMulticloudDataTransferSupportedService`

  * **Method** : `google.cloud.networkconnectivity.v1.DataTransferService.GetMulticloudDataTransferSupportedService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferSupportedServices.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.DataTransferService.GetMulticloudDataTransferSupportedService" `  




#### `ListDestinations`

  * **Method** : `google.cloud.networkconnectivity.v1.DataTransferService.ListDestinations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferDestinations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.DataTransferService.ListDestinations" `  




#### `ListMulticloudDataTransferConfigs`

  * **Method** : `google.cloud.networkconnectivity.v1.DataTransferService.ListMulticloudDataTransferConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.DataTransferService.ListMulticloudDataTransferConfigs" `  




#### `ListMulticloudDataTransferSupportedServices`

  * **Method** : `google.cloud.networkconnectivity.v1.DataTransferService.ListMulticloudDataTransferSupportedServices`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferSupportedServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.DataTransferService.ListMulticloudDataTransferSupportedServices" `  




#### `UpdateDestination`

  * **Method** : `google.cloud.networkconnectivity.v1.DataTransferService.UpdateDestination`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferDestinations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.DataTransferService.UpdateDestination" `  




#### `UpdateMulticloudDataTransferConfig`

  * **Method** : `google.cloud.networkconnectivity.v1.DataTransferService.UpdateMulticloudDataTransferConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.DataTransferService.UpdateMulticloudDataTransferConfig" `  




### `google.cloud.networkconnectivity.v1.HubService`

The following audit logs are associated with methods belonging to `google.cloud.networkconnectivity.v1.HubService`.

#### `AcceptHubSpoke`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.AcceptHubSpoke`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.groups.acceptSpoke - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.AcceptHubSpoke" `  




#### `AcceptSpokeUpdate`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.AcceptSpokeUpdate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.groups.acceptSpokeUpdate - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.AcceptSpokeUpdate" `  




#### `CreateGatewayAdvertisedRoute`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.CreateGatewayAdvertisedRoute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.gatewayAdvertisedRoutes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.CreateGatewayAdvertisedRoute" `  




#### `CreateHub`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.CreateHub`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.hubs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.CreateHub" `  




#### `CreateSpoke`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.CreateSpoke`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.spokes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.CreateSpoke" `  




#### `DeleteGatewayAdvertisedRoute`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.DeleteGatewayAdvertisedRoute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.gatewayAdvertisedRoutes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.DeleteGatewayAdvertisedRoute" `  




#### `DeleteHub`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.DeleteHub`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.hubs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.DeleteHub" `  




#### `DeleteSpoke`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.DeleteSpoke`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.spokes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.DeleteSpoke" `  




#### `GetGatewayAdvertisedRoute`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.GetGatewayAdvertisedRoute`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.gatewayAdvertisedRoutes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.GetGatewayAdvertisedRoute" `  




#### `GetGroup`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.GetGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.groups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.GetGroup" `  




#### `GetHub`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.GetHub`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.hubs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.GetHub" `  




#### `GetRoute`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.GetRoute`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.hubRoutes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.GetRoute" `  




#### `GetRouteTable`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.GetRouteTable`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.hubRouteTables.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.GetRouteTable" `  




#### `GetSpoke`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.GetSpoke`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.spokes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.GetSpoke" `  




#### `ListGatewayAdvertisedRoutes`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.ListGatewayAdvertisedRoutes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.gatewayAdvertisedRoutes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.ListGatewayAdvertisedRoutes" `  




#### `ListGroups`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.ListGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.groups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.ListGroups" `  




#### `ListHubSpokes`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.ListHubSpokes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.hubs.listSpokes - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.ListHubSpokes" `  




#### `ListHubs`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.ListHubs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.hubs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.ListHubs" `  




#### `ListRouteTables`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.ListRouteTables`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.hubRouteTables.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.ListRouteTables" `  




#### `ListRoutes`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.ListRoutes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.hubRoutes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.ListRoutes" `  




#### `ListSpokes`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.ListSpokes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.spokes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.ListSpokes" `  




#### `QueryHubStatus`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.QueryHubStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.hubs.queryStatus - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.QueryHubStatus" `  




#### `RejectHubSpoke`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.RejectHubSpoke`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.groups.rejectSpoke - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.RejectHubSpoke" `  




#### `RejectSpokeUpdate`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.RejectSpokeUpdate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.groups.rejectSpokeUpdate - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.RejectSpokeUpdate" `  




#### `UpdateGatewayAdvertisedRoute`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.UpdateGatewayAdvertisedRoute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.gatewayAdvertisedRoutes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.UpdateGatewayAdvertisedRoute" `  




#### `UpdateGroup`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.UpdateGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.groups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.UpdateGroup" `  




#### `UpdateHub`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.UpdateHub`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.hubs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.UpdateHub" `  




#### `UpdateSpoke`

  * **Method** : `google.cloud.networkconnectivity.v1.HubService.UpdateSpoke`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.spokes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.HubService.UpdateSpoke" `  




### `google.cloud.networkconnectivity.v1.InternalRangeService`

The following audit logs are associated with methods belonging to `google.cloud.networkconnectivity.v1.InternalRangeService`.

#### `CreateInternalRange`

  * **Method** : `google.cloud.networkconnectivity.v1.InternalRangeService.CreateInternalRange`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.internalRanges.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.InternalRangeService.CreateInternalRange" `  




#### `DeleteInternalRange`

  * **Method** : `google.cloud.networkconnectivity.v1.InternalRangeService.DeleteInternalRange`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.internalRanges.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.InternalRangeService.DeleteInternalRange" `  




#### `GetInternalRange`

  * **Method** : `google.cloud.networkconnectivity.v1.InternalRangeService.GetInternalRange`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.internalRanges.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.InternalRangeService.GetInternalRange" `  




#### `ListInternalRanges`

  * **Method** : `google.cloud.networkconnectivity.v1.InternalRangeService.ListInternalRanges`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.internalRanges.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.InternalRangeService.ListInternalRanges" `  




#### `UpdateInternalRange`

  * **Method** : `google.cloud.networkconnectivity.v1.InternalRangeService.UpdateInternalRange`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.internalRanges.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.InternalRangeService.UpdateInternalRange" `  




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




### `google.cloud.networkconnectivity.v1.RegionalEndpointService`

The following audit logs are associated with methods belonging to `google.cloud.networkconnectivity.v1.RegionalEndpointService`.

#### `CreateRegionalEndpoint`

  * **Method** : `google.cloud.networkconnectivity.v1.RegionalEndpointService.CreateRegionalEndpoint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.regionalEndpoints.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.RegionalEndpointService.CreateRegionalEndpoint" `  




#### `DeleteRegionalEndpoint`

  * **Method** : `google.cloud.networkconnectivity.v1.RegionalEndpointService.DeleteRegionalEndpoint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.regionalEndpoints.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.RegionalEndpointService.DeleteRegionalEndpoint" `  




#### `GetRegionalEndpoint`

  * **Method** : `google.cloud.networkconnectivity.v1.RegionalEndpointService.GetRegionalEndpoint`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.regionalEndpoints.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.RegionalEndpointService.GetRegionalEndpoint" `  




#### `ListRegionalEndpoints`

  * **Method** : `google.cloud.networkconnectivity.v1.RegionalEndpointService.ListRegionalEndpoints`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.regionalEndpoints.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.RegionalEndpointService.ListRegionalEndpoints" `  




### `google.cloud.networkconnectivity.v1.TransportManager`

The following audit logs are associated with methods belonging to `google.cloud.networkconnectivity.v1.TransportManager`.

#### `CreateTransport`

  * **Method** : `google.cloud.networkconnectivity.v1.TransportManager.CreateTransport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.transports.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.TransportManager.CreateTransport" `  




#### `DeleteTransport`

  * **Method** : `google.cloud.networkconnectivity.v1.TransportManager.DeleteTransport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.transports.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.TransportManager.DeleteTransport" `  




#### `GetRemoteTransportProfile`

  * **Method** : `google.cloud.networkconnectivity.v1.TransportManager.GetRemoteTransportProfile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.remoteTransportProfiles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.TransportManager.GetRemoteTransportProfile" `  




#### `GetTransport`

  * **Method** : `google.cloud.networkconnectivity.v1.TransportManager.GetTransport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.transports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.TransportManager.GetTransport" `  




#### `ListRemoteTransportProfiles`

  * **Method** : `google.cloud.networkconnectivity.v1.TransportManager.ListRemoteTransportProfiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.remoteTransportProfiles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.TransportManager.ListRemoteTransportProfiles" `  




#### `ListTransports`

  * **Method** : `google.cloud.networkconnectivity.v1.TransportManager.ListTransports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.transports.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.TransportManager.ListTransports" `  




#### `UpdateTransport`

  * **Method** : `google.cloud.networkconnectivity.v1.TransportManager.UpdateTransport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.transports.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1.TransportManager.UpdateTransport" `  




### `google.cloud.networkconnectivity.v1alpha1.HubService`

The following audit logs are associated with methods belonging to `google.cloud.networkconnectivity.v1alpha1.HubService`.

#### `CreateHub`

  * **Method** : `google.cloud.networkconnectivity.v1alpha1.HubService.CreateHub`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.hubs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1alpha1.HubService.CreateHub" `  




#### `CreateSpoke`

  * **Method** : `google.cloud.networkconnectivity.v1alpha1.HubService.CreateSpoke`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.spokes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1alpha1.HubService.CreateSpoke" `  




#### `DeleteHub`

  * **Method** : `google.cloud.networkconnectivity.v1alpha1.HubService.DeleteHub`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.hubs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1alpha1.HubService.DeleteHub" `  




#### `DeleteSpoke`

  * **Method** : `google.cloud.networkconnectivity.v1alpha1.HubService.DeleteSpoke`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.spokes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1alpha1.HubService.DeleteSpoke" `  




#### `GetHub`

  * **Method** : `google.cloud.networkconnectivity.v1alpha1.HubService.GetHub`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.hubs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1alpha1.HubService.GetHub" `  




#### `GetSpoke`

  * **Method** : `google.cloud.networkconnectivity.v1alpha1.HubService.GetSpoke`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.spokes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1alpha1.HubService.GetSpoke" `  




#### `ListHubs`

  * **Method** : `google.cloud.networkconnectivity.v1alpha1.HubService.ListHubs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.hubs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1alpha1.HubService.ListHubs" `  




#### `ListSpokes`

  * **Method** : `google.cloud.networkconnectivity.v1alpha1.HubService.ListSpokes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.spokes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1alpha1.HubService.ListSpokes" `  




#### `UpdateHub`

  * **Method** : `google.cloud.networkconnectivity.v1alpha1.HubService.UpdateHub`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.hubs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1alpha1.HubService.UpdateHub" `  




#### `UpdateSpoke`

  * **Method** : `google.cloud.networkconnectivity.v1alpha1.HubService.UpdateSpoke`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.spokes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1alpha1.HubService.UpdateSpoke" `  




### `google.cloud.networkconnectivity.v1alpha1.InternalRangeService`

The following audit logs are associated with methods belonging to `google.cloud.networkconnectivity.v1alpha1.InternalRangeService`.

#### `CreateInternalRange`

  * **Method** : `google.cloud.networkconnectivity.v1alpha1.InternalRangeService.CreateInternalRange`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.internalRanges.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1alpha1.InternalRangeService.CreateInternalRange" `  




#### `DeleteInternalRange`

  * **Method** : `google.cloud.networkconnectivity.v1alpha1.InternalRangeService.DeleteInternalRange`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.internalRanges.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1alpha1.InternalRangeService.DeleteInternalRange" `  




#### `GetInternalRange`

  * **Method** : `google.cloud.networkconnectivity.v1alpha1.InternalRangeService.GetInternalRange`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.internalRanges.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1alpha1.InternalRangeService.GetInternalRange" `  




#### `ListInternalRanges`

  * **Method** : `google.cloud.networkconnectivity.v1alpha1.InternalRangeService.ListInternalRanges`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.internalRanges.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1alpha1.InternalRangeService.ListInternalRanges" `  




#### `UpdateInternalRange`

  * **Method** : `google.cloud.networkconnectivity.v1alpha1.InternalRangeService.UpdateInternalRange`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.internalRanges.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1alpha1.InternalRangeService.UpdateInternalRange" `  




### `google.cloud.networkconnectivity.v1beta.DataTransferService`

The following audit logs are associated with methods belonging to `google.cloud.networkconnectivity.v1beta.DataTransferService`.

#### `CreateDestination`

  * **Method** : `google.cloud.networkconnectivity.v1beta.DataTransferService.CreateDestination`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferDestinations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.DataTransferService.CreateDestination" `  




#### `CreateMulticloudDataTransferConfig`

  * **Method** : `google.cloud.networkconnectivity.v1beta.DataTransferService.CreateMulticloudDataTransferConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.DataTransferService.CreateMulticloudDataTransferConfig" `  




#### `DeleteDestination`

  * **Method** : `google.cloud.networkconnectivity.v1beta.DataTransferService.DeleteDestination`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferDestinations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.DataTransferService.DeleteDestination" `  




#### `DeleteMulticloudDataTransferConfig`

  * **Method** : `google.cloud.networkconnectivity.v1beta.DataTransferService.DeleteMulticloudDataTransferConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.DataTransferService.DeleteMulticloudDataTransferConfig" `  




#### `GetDestination`

  * **Method** : `google.cloud.networkconnectivity.v1beta.DataTransferService.GetDestination`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferDestinations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.DataTransferService.GetDestination" `  




#### `GetMulticloudDataTransferConfig`

  * **Method** : `google.cloud.networkconnectivity.v1beta.DataTransferService.GetMulticloudDataTransferConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.DataTransferService.GetMulticloudDataTransferConfig" `  




#### `GetMulticloudDataTransferSupportedService`

  * **Method** : `google.cloud.networkconnectivity.v1beta.DataTransferService.GetMulticloudDataTransferSupportedService`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferSupportedServices.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.DataTransferService.GetMulticloudDataTransferSupportedService" `  




#### `ListDestinations`

  * **Method** : `google.cloud.networkconnectivity.v1beta.DataTransferService.ListDestinations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferDestinations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.DataTransferService.ListDestinations" `  




#### `ListMulticloudDataTransferConfigs`

  * **Method** : `google.cloud.networkconnectivity.v1beta.DataTransferService.ListMulticloudDataTransferConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.DataTransferService.ListMulticloudDataTransferConfigs" `  




#### `ListMulticloudDataTransferSupportedServices`

  * **Method** : `google.cloud.networkconnectivity.v1beta.DataTransferService.ListMulticloudDataTransferSupportedServices`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferSupportedServices.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.DataTransferService.ListMulticloudDataTransferSupportedServices" `  




#### `UpdateDestination`

  * **Method** : `google.cloud.networkconnectivity.v1beta.DataTransferService.UpdateDestination`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferDestinations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.DataTransferService.UpdateDestination" `  




#### `UpdateMulticloudDataTransferConfig`

  * **Method** : `google.cloud.networkconnectivity.v1beta.DataTransferService.UpdateMulticloudDataTransferConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.multicloudDataTransferConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.DataTransferService.UpdateMulticloudDataTransferConfig" `  




### `google.cloud.networkconnectivity.v1beta.HubService`

The following audit logs are associated with methods belonging to `google.cloud.networkconnectivity.v1beta.HubService`.

#### `AcceptHubSpoke`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.AcceptHubSpoke`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.groups.acceptSpoke - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.AcceptHubSpoke" `  




#### `AcceptSpokeUpdate`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.AcceptSpokeUpdate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.groups.acceptSpokeUpdate - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.AcceptSpokeUpdate" `  




#### `CreateGatewayAdvertisedRoute`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.CreateGatewayAdvertisedRoute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.gatewayAdvertisedRoutes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.CreateGatewayAdvertisedRoute" `  




#### `CreateHub`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.CreateHub`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.hubs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.CreateHub" `  




#### `CreateSpoke`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.CreateSpoke`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.spokes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.CreateSpoke" `  




#### `DeleteGatewayAdvertisedRoute`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.DeleteGatewayAdvertisedRoute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.gatewayAdvertisedRoutes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.DeleteGatewayAdvertisedRoute" `  




#### `DeleteHub`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.DeleteHub`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.hubs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.DeleteHub" `  




#### `DeleteSpoke`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.DeleteSpoke`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.spokes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.DeleteSpoke" `  




#### `GetGatewayAdvertisedRoute`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.GetGatewayAdvertisedRoute`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.gatewayAdvertisedRoutes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.GetGatewayAdvertisedRoute" `  




#### `GetGroup`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.GetGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.groups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.GetGroup" `  




#### `GetHub`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.GetHub`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.hubs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.GetHub" `  




#### `GetRoute`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.GetRoute`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.hubRoutes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.GetRoute" `  




#### `GetRouteTable`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.GetRouteTable`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.hubRouteTables.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.GetRouteTable" `  




#### `GetSpoke`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.GetSpoke`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.spokes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.GetSpoke" `  




#### `ListGatewayAdvertisedRoutes`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.ListGatewayAdvertisedRoutes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.gatewayAdvertisedRoutes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.ListGatewayAdvertisedRoutes" `  




#### `ListGroups`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.ListGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.groups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.ListGroups" `  




#### `ListHubSpokes`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.ListHubSpokes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.hubs.listSpokes - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.ListHubSpokes" `  




#### `ListHubs`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.ListHubs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.hubs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.ListHubs" `  




#### `ListRouteTables`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.ListRouteTables`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.hubRouteTables.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.ListRouteTables" `  




#### `ListRoutes`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.ListRoutes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.hubRoutes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.ListRoutes" `  




#### `ListSpokes`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.ListSpokes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.spokes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.ListSpokes" `  




#### `QueryHubStatus`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.QueryHubStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.hubs.queryStatus - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.QueryHubStatus" `  




#### `RejectHubSpoke`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.RejectHubSpoke`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.groups.rejectSpoke - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.RejectHubSpoke" `  




#### `UpdateGatewayAdvertisedRoute`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.UpdateGatewayAdvertisedRoute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.gatewayAdvertisedRoutes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.UpdateGatewayAdvertisedRoute" `  




#### `UpdateGroup`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.UpdateGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.groups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.UpdateGroup" `  




#### `UpdateHub`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.UpdateHub`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.hubs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.UpdateHub" `  




#### `UpdateSpoke`

  * **Method** : `google.cloud.networkconnectivity.v1beta.HubService.UpdateSpoke`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.spokes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.HubService.UpdateSpoke" `  




### `google.cloud.networkconnectivity.v1beta.PolicyBasedRoutingService`

The following audit logs are associated with methods belonging to `google.cloud.networkconnectivity.v1beta.PolicyBasedRoutingService`.

#### `CreatePolicyBasedRoute`

  * **Method** : `google.cloud.networkconnectivity.v1beta.PolicyBasedRoutingService.CreatePolicyBasedRoute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.policyBasedRoutes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.PolicyBasedRoutingService.CreatePolicyBasedRoute" `  




#### `DeletePolicyBasedRoute`

  * **Method** : `google.cloud.networkconnectivity.v1beta.PolicyBasedRoutingService.DeletePolicyBasedRoute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.policyBasedRoutes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.PolicyBasedRoutingService.DeletePolicyBasedRoute" `  




#### `GetPolicyBasedRoute`

  * **Method** : `google.cloud.networkconnectivity.v1beta.PolicyBasedRoutingService.GetPolicyBasedRoute`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.policyBasedRoutes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.PolicyBasedRoutingService.GetPolicyBasedRoute" `  




#### `ListPolicyBasedRoutes`

  * **Method** : `google.cloud.networkconnectivity.v1beta.PolicyBasedRoutingService.ListPolicyBasedRoutes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.policyBasedRoutes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.PolicyBasedRoutingService.ListPolicyBasedRoutes" `  




### `google.cloud.networkconnectivity.v1beta.RegionalEndpointService`

The following audit logs are associated with methods belonging to `google.cloud.networkconnectivity.v1beta.RegionalEndpointService`.

#### `CreateRegionalEndpoint`

  * **Method** : `google.cloud.networkconnectivity.v1beta.RegionalEndpointService.CreateRegionalEndpoint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.regionalEndpoints.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.RegionalEndpointService.CreateRegionalEndpoint" `  




#### `DeleteRegionalEndpoint`

  * **Method** : `google.cloud.networkconnectivity.v1beta.RegionalEndpointService.DeleteRegionalEndpoint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.regionalEndpoints.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.RegionalEndpointService.DeleteRegionalEndpoint" `  




#### `GetRegionalEndpoint`

  * **Method** : `google.cloud.networkconnectivity.v1beta.RegionalEndpointService.GetRegionalEndpoint`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.regionalEndpoints.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.RegionalEndpointService.GetRegionalEndpoint" `  




#### `ListRegionalEndpoints`

  * **Method** : `google.cloud.networkconnectivity.v1beta.RegionalEndpointService.ListRegionalEndpoints`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.regionalEndpoints.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.RegionalEndpointService.ListRegionalEndpoints" `  




### `google.cloud.networkconnectivity.v1beta.TransportManager`

The following audit logs are associated with methods belonging to `google.cloud.networkconnectivity.v1beta.TransportManager`.

#### `CreateTransport`

  * **Method** : `google.cloud.networkconnectivity.v1beta.TransportManager.CreateTransport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.transports.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.TransportManager.CreateTransport" `  




#### `DeleteTransport`

  * **Method** : `google.cloud.networkconnectivity.v1beta.TransportManager.DeleteTransport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.transports.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.TransportManager.DeleteTransport" `  




#### `GetRemoteTransportProfile`

  * **Method** : `google.cloud.networkconnectivity.v1beta.TransportManager.GetRemoteTransportProfile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.remoteTransportProfiles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.TransportManager.GetRemoteTransportProfile" `  




#### `GetStatus`

  * **Method** : `google.cloud.networkconnectivity.v1beta.TransportManager.GetStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.transports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.TransportManager.GetStatus" `  




#### `GetTransport`

  * **Method** : `google.cloud.networkconnectivity.v1beta.TransportManager.GetTransport`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.transports.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.TransportManager.GetTransport" `  




#### `ListRemoteTransportProfiles`

  * **Method** : `google.cloud.networkconnectivity.v1beta.TransportManager.ListRemoteTransportProfiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.remoteTransportProfiles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.TransportManager.ListRemoteTransportProfiles" `  




#### `ListTransports`

  * **Method** : `google.cloud.networkconnectivity.v1beta.TransportManager.ListTransports`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.transports.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.TransportManager.ListTransports" `  




#### `ParseFromActivationKey`

  * **Method** : `google.cloud.networkconnectivity.v1beta.TransportManager.ParseFromActivationKey`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.remoteTransportProfiles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.TransportManager.ParseFromActivationKey" `  




#### `UpdateTransport`

  * **Method** : `google.cloud.networkconnectivity.v1beta.TransportManager.UpdateTransport`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.transports.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networkconnectivity.v1beta.TransportManager.UpdateTransport" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.hubs.getIamPolicy - ADMIN_READ`
    * `networkconnectivity.spokes.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.groups.setIamPolicy - ADMIN_WRITE`
    * `networkconnectivity.hubs.setIamPolicy - ADMIN_WRITE`
    * `networkconnectivity.policyBasedRoutes.setIamPolicy - ADMIN_WRITE`
    * `networkconnectivity.spokes.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networkconnectivity.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networkconnectivity.operations.list - ADMIN_READ`
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
