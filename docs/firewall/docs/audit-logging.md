---
url: https://docs.cloud.google.com/firewall/docs/audit-logging/
title: Cloud NGFW audit logging \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:59.768502+00:00
---

# Cloud NGFW audit logging  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Cloud NGFW audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Cloud Next Generation Firewall. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Cloud Next Generation Firewall audit logs use the service name `networksecurity.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="networksecurity.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Next Generation Firewall generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.networksecurity.v1.AddressGroupService.GetAddressGroup`  
`google.cloud.networksecurity.v1.AddressGroupService.ListAddressGroupReferences`  
`google.cloud.networksecurity.v1.AddressGroupService.ListAddressGroups`  
`google.cloud.networksecurity.v1.FirewallActivation.GetFirewallEndpoint`  
`google.cloud.networksecurity.v1.FirewallActivation.GetFirewallEndpointAssociation`  
`google.cloud.networksecurity.v1.FirewallActivation.ListFirewallEndpointAssociations`  
`google.cloud.networksecurity.v1.FirewallActivation.ListFirewallEndpoints`  
`google.cloud.networksecurity.v1.Intercept.GetInterceptDeployment`  
`google.cloud.networksecurity.v1.Intercept.GetInterceptDeploymentGroup`  
`google.cloud.networksecurity.v1.Intercept.GetInterceptEndpointGroup`  
`google.cloud.networksecurity.v1.Intercept.GetInterceptEndpointGroupAssociation`  
`google.cloud.networksecurity.v1.Intercept.ListInterceptDeploymentGroups`  
`google.cloud.networksecurity.v1.Intercept.ListInterceptDeployments`  
`google.cloud.networksecurity.v1.Intercept.ListInterceptEndpointGroupAssociations`  
`google.cloud.networksecurity.v1.Intercept.ListInterceptEndpointGroups`  
`google.cloud.networksecurity.v1.Mirroring.GetMirroringDeployment`  
`google.cloud.networksecurity.v1.Mirroring.GetMirroringDeploymentGroup`  
`google.cloud.networksecurity.v1.Mirroring.GetMirroringEndpointGroup`  
`google.cloud.networksecurity.v1.Mirroring.GetMirroringEndpointGroupAssociation`  
`google.cloud.networksecurity.v1.Mirroring.ListMirroringDeploymentGroups`  
`google.cloud.networksecurity.v1.Mirroring.ListMirroringDeployments`  
`google.cloud.networksecurity.v1.Mirroring.ListMirroringEndpointGroupAssociations`  
`google.cloud.networksecurity.v1.Mirroring.ListMirroringEndpointGroups`  
`google.cloud.networksecurity.v1.NetworkSecurity.GetAuthorizationPolicy`  
`google.cloud.networksecurity.v1.NetworkSecurity.GetAuthzPolicy`  
`google.cloud.networksecurity.v1.NetworkSecurity.GetBackendAuthenticationConfig`  
`google.cloud.networksecurity.v1.NetworkSecurity.GetClientTlsPolicy`  
`google.cloud.networksecurity.v1.NetworkSecurity.GetGatewaySecurityPolicy`  
`google.cloud.networksecurity.v1.NetworkSecurity.GetGatewaySecurityPolicyRule`  
`google.cloud.networksecurity.v1.NetworkSecurity.GetServerTlsPolicy`  
`google.cloud.networksecurity.v1.NetworkSecurity.GetTlsInspectionPolicy`  
`google.cloud.networksecurity.v1.NetworkSecurity.GetUrlList`  
`google.cloud.networksecurity.v1.NetworkSecurity.ListAuthorizationPolicies`  
`google.cloud.networksecurity.v1.NetworkSecurity.ListAuthzPolicies`  
`google.cloud.networksecurity.v1.NetworkSecurity.ListBackendAuthenticationConfigs`  
`google.cloud.networksecurity.v1.NetworkSecurity.ListClientTlsPolicies`  
`google.cloud.networksecurity.v1.NetworkSecurity.ListGatewaySecurityPolicies`  
`google.cloud.networksecurity.v1.NetworkSecurity.ListGatewaySecurityPolicyRules`  
`google.cloud.networksecurity.v1.NetworkSecurity.ListServerTlsPolicies`  
`google.cloud.networksecurity.v1.NetworkSecurity.ListTlsInspectionPolicies`  
`google.cloud.networksecurity.v1.NetworkSecurity.ListUrlLists`  
`google.cloud.networksecurity.v1.OrganizationAddressGroupService.GetAddressGroup`  
`google.cloud.networksecurity.v1.OrganizationAddressGroupService.ListAddressGroups`  
`google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.GetSecurityProfile`  
`google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.GetSecurityProfileGroup`  
`google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.ListSecurityProfileGroups`  
`google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.ListSecurityProfiles`  
`google.cloud.networksecurity.v1alpha1.Intercept.GetInterceptDeployment`  
`google.cloud.networksecurity.v1alpha1.Intercept.GetInterceptDeploymentGroup`  
`google.cloud.networksecurity.v1alpha1.Intercept.GetInterceptEndpointGroup`  
`google.cloud.networksecurity.v1alpha1.Intercept.GetInterceptEndpointGroupAssociation`  
`google.cloud.networksecurity.v1alpha1.Intercept.ListInterceptDeploymentGroups`  
`google.cloud.networksecurity.v1alpha1.Intercept.ListInterceptDeployments`  
`google.cloud.networksecurity.v1alpha1.Intercept.ListInterceptEndpointGroupAssociations`  
`google.cloud.networksecurity.v1alpha1.Intercept.ListInterceptEndpointGroups`  
`google.cloud.networksecurity.v1alpha1.Mirroring.GetMirroringDeployment`  
`google.cloud.networksecurity.v1alpha1.Mirroring.GetMirroringDeploymentGroup`  
`google.cloud.networksecurity.v1alpha1.Mirroring.GetMirroringEndpointGroup`  
`google.cloud.networksecurity.v1alpha1.Mirroring.GetMirroringEndpointGroupAssociation`  
`google.cloud.networksecurity.v1alpha1.Mirroring.ListMirroringDeploymentGroups`  
`google.cloud.networksecurity.v1alpha1.Mirroring.ListMirroringDeployments`  
`google.cloud.networksecurity.v1alpha1.Mirroring.ListMirroringEndpointGroupAssociations`  
`google.cloud.networksecurity.v1alpha1.Mirroring.ListMirroringEndpointGroups`  
`google.cloud.networksecurity.v1alpha1.SSEGatewayService.GetPartnerSSEGateway`  
`google.cloud.networksecurity.v1alpha1.SSERealmService.ListSACAttachments`  
`google.cloud.networksecurity.v1beta1.Intercept.GetInterceptDeployment`  
`google.cloud.networksecurity.v1beta1.Intercept.GetInterceptDeploymentGroup`  
`google.cloud.networksecurity.v1beta1.Intercept.GetInterceptEndpointGroup`  
`google.cloud.networksecurity.v1beta1.Intercept.GetInterceptEndpointGroupAssociation`  
`google.cloud.networksecurity.v1beta1.Intercept.ListInterceptDeploymentGroups`  
`google.cloud.networksecurity.v1beta1.Intercept.ListInterceptDeployments`  
`google.cloud.networksecurity.v1beta1.Intercept.ListInterceptEndpointGroupAssociations`  
`google.cloud.networksecurity.v1beta1.Intercept.ListInterceptEndpointGroups`  
`google.cloud.networksecurity.v1beta1.Mirroring.GetMirroringDeployment`  
`google.cloud.networksecurity.v1beta1.Mirroring.GetMirroringDeploymentGroup`  
`google.cloud.networksecurity.v1beta1.Mirroring.GetMirroringEndpointGroup`  
`google.cloud.networksecurity.v1beta1.Mirroring.GetMirroringEndpointGroupAssociation`  
`google.cloud.networksecurity.v1beta1.Mirroring.ListMirroringDeploymentGroups`  
`google.cloud.networksecurity.v1beta1.Mirroring.ListMirroringDeployments`  
`google.cloud.networksecurity.v1beta1.Mirroring.ListMirroringEndpointGroupAssociations`  
`google.cloud.networksecurity.v1beta1.Mirroring.ListMirroringEndpointGroups`  
`google.cloud.networksecurity.v1beta1.SSERealmService.ListSACAttachments`  
`google.cloud.networksecurity.v1beta1.SSERealmService.ListSACRealms`  
`GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.networksecurity.v1.AddressGroupService.AddAddressGroupItems` (LRO)  
`google.cloud.networksecurity.v1.AddressGroupService.CloneAddressGroupItems` (LRO)  
`google.cloud.networksecurity.v1.AddressGroupService.CreateAddressGroup` (LRO)  
`google.cloud.networksecurity.v1.AddressGroupService.DeleteAddressGroup` (LRO)  
`google.cloud.networksecurity.v1.AddressGroupService.RemoveAddressGroupItems` (LRO)  
`google.cloud.networksecurity.v1.AddressGroupService.UpdateAddressGroup` (LRO)  
`google.cloud.networksecurity.v1.FirewallActivation.CreateFirewallEndpoint` (LRO)  
`google.cloud.networksecurity.v1.FirewallActivation.CreateFirewallEndpointAssociation` (LRO)  
`google.cloud.networksecurity.v1.FirewallActivation.DeleteFirewallEndpoint` (LRO)  
`google.cloud.networksecurity.v1.FirewallActivation.DeleteFirewallEndpointAssociation` (LRO)  
`google.cloud.networksecurity.v1.FirewallActivation.UpdateFirewallEndpoint` (LRO)  
`google.cloud.networksecurity.v1.FirewallActivation.UpdateFirewallEndpointAssociation` (LRO)  
`google.cloud.networksecurity.v1.Intercept.CreateInterceptDeployment` (LRO)  
`google.cloud.networksecurity.v1.Intercept.CreateInterceptDeploymentGroup` (LRO)  
`google.cloud.networksecurity.v1.Intercept.CreateInterceptEndpointGroup` (LRO)  
`google.cloud.networksecurity.v1.Intercept.CreateInterceptEndpointGroupAssociation` (LRO)  
`google.cloud.networksecurity.v1.Intercept.DeleteInterceptDeployment` (LRO)  
`google.cloud.networksecurity.v1.Intercept.DeleteInterceptDeploymentGroup` (LRO)  
`google.cloud.networksecurity.v1.Intercept.DeleteInterceptEndpointGroup` (LRO)  
`google.cloud.networksecurity.v1.Intercept.DeleteInterceptEndpointGroupAssociation` (LRO)  
`google.cloud.networksecurity.v1.Intercept.UpdateInterceptDeployment` (LRO)  
`google.cloud.networksecurity.v1.Intercept.UpdateInterceptDeploymentGroup` (LRO)  
`google.cloud.networksecurity.v1.Intercept.UpdateInterceptEndpointGroup` (LRO)  
`google.cloud.networksecurity.v1.Intercept.UpdateInterceptEndpointGroupAssociation` (LRO)  
`google.cloud.networksecurity.v1.Mirroring.CreateMirroringDeployment` (LRO)  
`google.cloud.networksecurity.v1.Mirroring.CreateMirroringDeploymentGroup` (LRO)  
`google.cloud.networksecurity.v1.Mirroring.CreateMirroringEndpointGroup` (LRO)  
`google.cloud.networksecurity.v1.Mirroring.CreateMirroringEndpointGroupAssociation` (LRO)  
`google.cloud.networksecurity.v1.Mirroring.DeleteMirroringDeployment` (LRO)  
`google.cloud.networksecurity.v1.Mirroring.DeleteMirroringDeploymentGroup` (LRO)  
`google.cloud.networksecurity.v1.Mirroring.DeleteMirroringEndpointGroup` (LRO)  
`google.cloud.networksecurity.v1.Mirroring.DeleteMirroringEndpointGroupAssociation` (LRO)  
`google.cloud.networksecurity.v1.Mirroring.UpdateMirroringDeployment` (LRO)  
`google.cloud.networksecurity.v1.Mirroring.UpdateMirroringDeploymentGroup` (LRO)  
`google.cloud.networksecurity.v1.Mirroring.UpdateMirroringEndpointGroup` (LRO)  
`google.cloud.networksecurity.v1.Mirroring.UpdateMirroringEndpointGroupAssociation` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.CreateAuthorizationPolicy` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.CreateAuthzPolicy` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.CreateBackendAuthenticationConfig` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.CreateClientTlsPolicy` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.CreateGatewaySecurityPolicy` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.CreateGatewaySecurityPolicyRule` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.CreateServerTlsPolicy` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.CreateUrlList` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.DeleteAuthorizationPolicy` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.DeleteAuthzPolicy` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.DeleteBackendAuthenticationConfig` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.DeleteClientTlsPolicy` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.DeleteGatewaySecurityPolicy` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.DeleteGatewaySecurityPolicyRule` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.DeleteServerTlsPolicy` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.DeleteUrlList` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.UpdateAuthorizationPolicy` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.UpdateAuthzPolicy` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.UpdateBackendAuthenticationConfig` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.UpdateClientTlsPolicy` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.UpdateGatewaySecurityPolicy` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.UpdateGatewaySecurityPolicyRule` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.UpdateServerTlsPolicy` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.UpdateUrlList` (LRO)  
`google.cloud.networksecurity.v1.OrganizationAddressGroupService.AddAddressGroupItems` (LRO)  
`google.cloud.networksecurity.v1.OrganizationAddressGroupService.CloneAddressGroupItems` (LRO)  
`google.cloud.networksecurity.v1.OrganizationAddressGroupService.CreateAddressGroup` (LRO)  
`google.cloud.networksecurity.v1.OrganizationAddressGroupService.DeleteAddressGroup` (LRO)  
`google.cloud.networksecurity.v1.OrganizationAddressGroupService.RemoveAddressGroupItems` (LRO)  
`google.cloud.networksecurity.v1.OrganizationAddressGroupService.UpdateAddressGroup` (LRO)  
`google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.CreateSecurityProfile` (LRO)  
`google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.CreateSecurityProfileGroup` (LRO)  
`google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.DeleteSecurityProfile` (LRO)  
`google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.DeleteSecurityProfileGroup` (LRO)  
`google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.UpdateSecurityProfile` (LRO)  
`google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.UpdateSecurityProfileGroup` (LRO)  
`google.cloud.networksecurity.v1alpha1.Intercept.CreateInterceptDeployment` (LRO)  
`google.cloud.networksecurity.v1alpha1.Intercept.CreateInterceptDeploymentGroup` (LRO)  
`google.cloud.networksecurity.v1alpha1.Intercept.CreateInterceptEndpointGroup` (LRO)  
`google.cloud.networksecurity.v1alpha1.Intercept.CreateInterceptEndpointGroupAssociation` (LRO)  
`google.cloud.networksecurity.v1alpha1.Intercept.DeleteInterceptDeployment` (LRO)  
`google.cloud.networksecurity.v1alpha1.Intercept.DeleteInterceptDeploymentGroup` (LRO)  
`google.cloud.networksecurity.v1alpha1.Intercept.DeleteInterceptEndpointGroup` (LRO)  
`google.cloud.networksecurity.v1alpha1.Intercept.DeleteInterceptEndpointGroupAssociation` (LRO)  
`google.cloud.networksecurity.v1alpha1.Intercept.UpdateInterceptDeployment` (LRO)  
`google.cloud.networksecurity.v1alpha1.Intercept.UpdateInterceptDeploymentGroup` (LRO)  
`google.cloud.networksecurity.v1alpha1.Intercept.UpdateInterceptEndpointGroup` (LRO)  
`google.cloud.networksecurity.v1alpha1.Intercept.UpdateInterceptEndpointGroupAssociation` (LRO)  
`google.cloud.networksecurity.v1alpha1.Mirroring.CreateMirroringDeployment` (LRO)  
`google.cloud.networksecurity.v1alpha1.Mirroring.CreateMirroringDeploymentGroup` (LRO)  
`google.cloud.networksecurity.v1alpha1.Mirroring.CreateMirroringEndpointGroup` (LRO)  
`google.cloud.networksecurity.v1alpha1.Mirroring.CreateMirroringEndpointGroupAssociation` (LRO)  
`google.cloud.networksecurity.v1alpha1.Mirroring.DeleteMirroringDeployment` (LRO)  
`google.cloud.networksecurity.v1alpha1.Mirroring.DeleteMirroringDeploymentGroup` (LRO)  
`google.cloud.networksecurity.v1alpha1.Mirroring.DeleteMirroringEndpointGroup` (LRO)  
`google.cloud.networksecurity.v1alpha1.Mirroring.DeleteMirroringEndpointGroupAssociation` (LRO)  
`google.cloud.networksecurity.v1alpha1.Mirroring.UpdateMirroringDeployment` (LRO)  
`google.cloud.networksecurity.v1alpha1.Mirroring.UpdateMirroringDeploymentGroup` (LRO)  
`google.cloud.networksecurity.v1alpha1.Mirroring.UpdateMirroringEndpointGroup` (LRO)  
`google.cloud.networksecurity.v1alpha1.Mirroring.UpdateMirroringEndpointGroupAssociation` (LRO)  
`google.cloud.networksecurity.v1alpha1.SSEGatewayService.CreatePartnerSSEGateway` (LRO)  
`google.cloud.networksecurity.v1alpha1.SSEGatewayService.DeletePartnerSSEGateway` (LRO)  
`google.cloud.networksecurity.v1alpha1.SSEGatewayService.UpdatePartnerSSEGateway` (LRO)  
`google.cloud.networksecurity.v1alpha1.SSERealmService.CreatePartnerSSERealm` (LRO)  
`google.cloud.networksecurity.v1alpha1.SSERealmService.CreateSACAttachment` (LRO)  
`google.cloud.networksecurity.v1alpha1.SSERealmService.CreateSACRealm` (LRO)  
`google.cloud.networksecurity.v1alpha1.SSERealmService.DeletePartnerSSERealm` (LRO)  
`google.cloud.networksecurity.v1alpha1.SSERealmService.DeleteSACAttachment` (LRO)  
`google.cloud.networksecurity.v1alpha1.SSERealmService.DeleteSACRealm` (LRO)  
`google.cloud.networksecurity.v1beta1.Intercept.CreateInterceptDeployment` (LRO)  
`google.cloud.networksecurity.v1beta1.Intercept.CreateInterceptDeploymentGroup` (LRO)  
`google.cloud.networksecurity.v1beta1.Intercept.CreateInterceptEndpointGroup` (LRO)  
`google.cloud.networksecurity.v1beta1.Intercept.CreateInterceptEndpointGroupAssociation` (LRO)  
`google.cloud.networksecurity.v1beta1.Intercept.DeleteInterceptDeployment` (LRO)  
`google.cloud.networksecurity.v1beta1.Intercept.DeleteInterceptDeploymentGroup` (LRO)  
`google.cloud.networksecurity.v1beta1.Intercept.DeleteInterceptEndpointGroup` (LRO)  
`google.cloud.networksecurity.v1beta1.Intercept.DeleteInterceptEndpointGroupAssociation` (LRO)  
`google.cloud.networksecurity.v1beta1.Intercept.UpdateInterceptDeployment` (LRO)  
`google.cloud.networksecurity.v1beta1.Intercept.UpdateInterceptDeploymentGroup` (LRO)  
`google.cloud.networksecurity.v1beta1.Intercept.UpdateInterceptEndpointGroup` (LRO)  
`google.cloud.networksecurity.v1beta1.Intercept.UpdateInterceptEndpointGroupAssociation` (LRO)  
`google.cloud.networksecurity.v1beta1.Mirroring.CreateMirroringDeployment` (LRO)  
`google.cloud.networksecurity.v1beta1.Mirroring.CreateMirroringDeploymentGroup` (LRO)  
`google.cloud.networksecurity.v1beta1.Mirroring.CreateMirroringEndpointGroup` (LRO)  
`google.cloud.networksecurity.v1beta1.Mirroring.CreateMirroringEndpointGroupAssociation` (LRO)  
`google.cloud.networksecurity.v1beta1.Mirroring.DeleteMirroringDeployment` (LRO)  
`google.cloud.networksecurity.v1beta1.Mirroring.DeleteMirroringDeploymentGroup` (LRO)  
`google.cloud.networksecurity.v1beta1.Mirroring.DeleteMirroringEndpointGroup` (LRO)  
`google.cloud.networksecurity.v1beta1.Mirroring.DeleteMirroringEndpointGroupAssociation` (LRO)  
`google.cloud.networksecurity.v1beta1.Mirroring.UpdateMirroringDeployment` (LRO)  
`google.cloud.networksecurity.v1beta1.Mirroring.UpdateMirroringDeploymentGroup` (LRO)  
`google.cloud.networksecurity.v1beta1.Mirroring.UpdateMirroringEndpointGroup` (LRO)  
`google.cloud.networksecurity.v1beta1.Mirroring.UpdateMirroringEndpointGroupAssociation` (LRO)  
`google.cloud.networksecurity.v1beta1.SSERealmService.CreateSACAttachment` (LRO)  
`google.cloud.networksecurity.v1beta1.SSERealmService.CreateSACRealm` (LRO)  
`google.cloud.networksecurity.v1beta1.SSERealmService.DeleteSACAttachment` (LRO)  
`google.cloud.networksecurity.v1beta1.SSERealmService.DeleteSACRealm` (LRO)  
`SetIamPolicy`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
`DATA_WRITE` | `google.cloud.networksecurity.v1.NetworkSecurity.CreateTlsInspectionPolicy` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.DeleteTlsInspectionPolicy` (LRO)  
`google.cloud.networksecurity.v1.NetworkSecurity.UpdateTlsInspectionPolicy` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Next Generation Firewall.

### `google.cloud.networksecurity.v1.AddressGroupService`

The following audit logs are associated with methods belonging to `google.cloud.networksecurity.v1.AddressGroupService`.

#### `AddAddressGroupItems`

  * **Method** : `google.cloud.networksecurity.v1.AddressGroupService.AddAddressGroupItems`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.addressGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.AddressGroupService.AddAddressGroupItems" `  




#### `CloneAddressGroupItems`

  * **Method** : `google.cloud.networksecurity.v1.AddressGroupService.CloneAddressGroupItems`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.addressGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.AddressGroupService.CloneAddressGroupItems" `  




#### `CreateAddressGroup`

  * **Method** : `google.cloud.networksecurity.v1.AddressGroupService.CreateAddressGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.addressGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.AddressGroupService.CreateAddressGroup" `  




#### `DeleteAddressGroup`

  * **Method** : `google.cloud.networksecurity.v1.AddressGroupService.DeleteAddressGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.addressGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.AddressGroupService.DeleteAddressGroup" `  




#### `GetAddressGroup`

  * **Method** : `google.cloud.networksecurity.v1.AddressGroupService.GetAddressGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.addressGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.AddressGroupService.GetAddressGroup" `  




#### `ListAddressGroupReferences`

  * **Method** : `google.cloud.networksecurity.v1.AddressGroupService.ListAddressGroupReferences`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.addressGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.AddressGroupService.ListAddressGroupReferences" `  




#### `ListAddressGroups`

  * **Method** : `google.cloud.networksecurity.v1.AddressGroupService.ListAddressGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.addressGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.AddressGroupService.ListAddressGroups" `  




#### `RemoveAddressGroupItems`

  * **Method** : `google.cloud.networksecurity.v1.AddressGroupService.RemoveAddressGroupItems`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.addressGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.AddressGroupService.RemoveAddressGroupItems" `  




#### `UpdateAddressGroup`

  * **Method** : `google.cloud.networksecurity.v1.AddressGroupService.UpdateAddressGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.addressGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.AddressGroupService.UpdateAddressGroup" `  




### `google.cloud.networksecurity.v1.FirewallActivation`

The following audit logs are associated with methods belonging to `google.cloud.networksecurity.v1.FirewallActivation`.

#### `CreateFirewallEndpoint`

  * **Method** : `google.cloud.networksecurity.v1.FirewallActivation.CreateFirewallEndpoint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.firewallEndpoints.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.FirewallActivation.CreateFirewallEndpoint" `  




#### `CreateFirewallEndpointAssociation`

  * **Method** : `google.cloud.networksecurity.v1.FirewallActivation.CreateFirewallEndpointAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.firewallEndpointAssociations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.FirewallActivation.CreateFirewallEndpointAssociation" `  




#### `DeleteFirewallEndpoint`

  * **Method** : `google.cloud.networksecurity.v1.FirewallActivation.DeleteFirewallEndpoint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.firewallEndpoints.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.FirewallActivation.DeleteFirewallEndpoint" `  




#### `DeleteFirewallEndpointAssociation`

  * **Method** : `google.cloud.networksecurity.v1.FirewallActivation.DeleteFirewallEndpointAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.firewallEndpointAssociations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.FirewallActivation.DeleteFirewallEndpointAssociation" `  




#### `GetFirewallEndpoint`

  * **Method** : `google.cloud.networksecurity.v1.FirewallActivation.GetFirewallEndpoint`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.firewallEndpoints.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.FirewallActivation.GetFirewallEndpoint" `  




#### `GetFirewallEndpointAssociation`

  * **Method** : `google.cloud.networksecurity.v1.FirewallActivation.GetFirewallEndpointAssociation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.firewallEndpointAssociations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.FirewallActivation.GetFirewallEndpointAssociation" `  




#### `ListFirewallEndpointAssociations`

  * **Method** : `google.cloud.networksecurity.v1.FirewallActivation.ListFirewallEndpointAssociations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.firewallEndpointAssociations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.FirewallActivation.ListFirewallEndpointAssociations" `  




#### `ListFirewallEndpoints`

  * **Method** : `google.cloud.networksecurity.v1.FirewallActivation.ListFirewallEndpoints`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.firewallEndpoints.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.FirewallActivation.ListFirewallEndpoints" `  




#### `UpdateFirewallEndpoint`

  * **Method** : `google.cloud.networksecurity.v1.FirewallActivation.UpdateFirewallEndpoint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.firewallEndpoints.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.FirewallActivation.UpdateFirewallEndpoint" `  




#### `UpdateFirewallEndpointAssociation`

  * **Method** : `google.cloud.networksecurity.v1.FirewallActivation.UpdateFirewallEndpointAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.firewallEndpointAssociations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.FirewallActivation.UpdateFirewallEndpointAssociation" `  




### `google.cloud.networksecurity.v1.Intercept`

The following audit logs are associated with methods belonging to `google.cloud.networksecurity.v1.Intercept`.

#### `CreateInterceptDeployment`

  * **Method** : `google.cloud.networksecurity.v1.Intercept.CreateInterceptDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptDeployments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Intercept.CreateInterceptDeployment" `  




#### `CreateInterceptDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1.Intercept.CreateInterceptDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptDeploymentGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Intercept.CreateInterceptDeploymentGroup" `  




#### `CreateInterceptEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1.Intercept.CreateInterceptEndpointGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Intercept.CreateInterceptEndpointGroup" `  




#### `CreateInterceptEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1.Intercept.CreateInterceptEndpointGroupAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroupAssociations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Intercept.CreateInterceptEndpointGroupAssociation" `  




#### `DeleteInterceptDeployment`

  * **Method** : `google.cloud.networksecurity.v1.Intercept.DeleteInterceptDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptDeployments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Intercept.DeleteInterceptDeployment" `  




#### `DeleteInterceptDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1.Intercept.DeleteInterceptDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptDeploymentGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Intercept.DeleteInterceptDeploymentGroup" `  




#### `DeleteInterceptEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1.Intercept.DeleteInterceptEndpointGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Intercept.DeleteInterceptEndpointGroup" `  




#### `DeleteInterceptEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1.Intercept.DeleteInterceptEndpointGroupAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroupAssociations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Intercept.DeleteInterceptEndpointGroupAssociation" `  




#### `GetInterceptDeployment`

  * **Method** : `google.cloud.networksecurity.v1.Intercept.GetInterceptDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptDeployments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Intercept.GetInterceptDeployment" `  




#### `GetInterceptDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1.Intercept.GetInterceptDeploymentGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptDeploymentGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Intercept.GetInterceptDeploymentGroup" `  




#### `GetInterceptEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1.Intercept.GetInterceptEndpointGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Intercept.GetInterceptEndpointGroup" `  




#### `GetInterceptEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1.Intercept.GetInterceptEndpointGroupAssociation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroupAssociations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Intercept.GetInterceptEndpointGroupAssociation" `  




#### `ListInterceptDeploymentGroups`

  * **Method** : `google.cloud.networksecurity.v1.Intercept.ListInterceptDeploymentGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptDeploymentGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Intercept.ListInterceptDeploymentGroups" `  




#### `ListInterceptDeployments`

  * **Method** : `google.cloud.networksecurity.v1.Intercept.ListInterceptDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptDeployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Intercept.ListInterceptDeployments" `  




#### `ListInterceptEndpointGroupAssociations`

  * **Method** : `google.cloud.networksecurity.v1.Intercept.ListInterceptEndpointGroupAssociations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroupAssociations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Intercept.ListInterceptEndpointGroupAssociations" `  




#### `ListInterceptEndpointGroups`

  * **Method** : `google.cloud.networksecurity.v1.Intercept.ListInterceptEndpointGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Intercept.ListInterceptEndpointGroups" `  




#### `UpdateInterceptDeployment`

  * **Method** : `google.cloud.networksecurity.v1.Intercept.UpdateInterceptDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptDeployments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Intercept.UpdateInterceptDeployment" `  




#### `UpdateInterceptDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1.Intercept.UpdateInterceptDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptDeploymentGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Intercept.UpdateInterceptDeploymentGroup" `  




#### `UpdateInterceptEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1.Intercept.UpdateInterceptEndpointGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Intercept.UpdateInterceptEndpointGroup" `  




#### `UpdateInterceptEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1.Intercept.UpdateInterceptEndpointGroupAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroupAssociations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Intercept.UpdateInterceptEndpointGroupAssociation" `  




### `google.cloud.networksecurity.v1.Mirroring`

The following audit logs are associated with methods belonging to `google.cloud.networksecurity.v1.Mirroring`.

#### `CreateMirroringDeployment`

  * **Method** : `google.cloud.networksecurity.v1.Mirroring.CreateMirroringDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringDeployments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Mirroring.CreateMirroringDeployment" `  




#### `CreateMirroringDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1.Mirroring.CreateMirroringDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringDeploymentGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Mirroring.CreateMirroringDeploymentGroup" `  




#### `CreateMirroringEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1.Mirroring.CreateMirroringEndpointGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Mirroring.CreateMirroringEndpointGroup" `  




#### `CreateMirroringEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1.Mirroring.CreateMirroringEndpointGroupAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroupAssociations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Mirroring.CreateMirroringEndpointGroupAssociation" `  




#### `DeleteMirroringDeployment`

  * **Method** : `google.cloud.networksecurity.v1.Mirroring.DeleteMirroringDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringDeployments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Mirroring.DeleteMirroringDeployment" `  




#### `DeleteMirroringDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1.Mirroring.DeleteMirroringDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringDeploymentGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Mirroring.DeleteMirroringDeploymentGroup" `  




#### `DeleteMirroringEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1.Mirroring.DeleteMirroringEndpointGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Mirroring.DeleteMirroringEndpointGroup" `  




#### `DeleteMirroringEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1.Mirroring.DeleteMirroringEndpointGroupAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroupAssociations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Mirroring.DeleteMirroringEndpointGroupAssociation" `  




#### `GetMirroringDeployment`

  * **Method** : `google.cloud.networksecurity.v1.Mirroring.GetMirroringDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringDeployments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Mirroring.GetMirroringDeployment" `  




#### `GetMirroringDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1.Mirroring.GetMirroringDeploymentGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringDeploymentGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Mirroring.GetMirroringDeploymentGroup" `  




#### `GetMirroringEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1.Mirroring.GetMirroringEndpointGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Mirroring.GetMirroringEndpointGroup" `  




#### `GetMirroringEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1.Mirroring.GetMirroringEndpointGroupAssociation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroupAssociations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Mirroring.GetMirroringEndpointGroupAssociation" `  




#### `ListMirroringDeploymentGroups`

  * **Method** : `google.cloud.networksecurity.v1.Mirroring.ListMirroringDeploymentGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringDeploymentGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Mirroring.ListMirroringDeploymentGroups" `  




#### `ListMirroringDeployments`

  * **Method** : `google.cloud.networksecurity.v1.Mirroring.ListMirroringDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringDeployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Mirroring.ListMirroringDeployments" `  




#### `ListMirroringEndpointGroupAssociations`

  * **Method** : `google.cloud.networksecurity.v1.Mirroring.ListMirroringEndpointGroupAssociations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroupAssociations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Mirroring.ListMirroringEndpointGroupAssociations" `  




#### `ListMirroringEndpointGroups`

  * **Method** : `google.cloud.networksecurity.v1.Mirroring.ListMirroringEndpointGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Mirroring.ListMirroringEndpointGroups" `  




#### `UpdateMirroringDeployment`

  * **Method** : `google.cloud.networksecurity.v1.Mirroring.UpdateMirroringDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringDeployments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Mirroring.UpdateMirroringDeployment" `  




#### `UpdateMirroringDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1.Mirroring.UpdateMirroringDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringDeploymentGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Mirroring.UpdateMirroringDeploymentGroup" `  




#### `UpdateMirroringEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1.Mirroring.UpdateMirroringEndpointGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Mirroring.UpdateMirroringEndpointGroup" `  




#### `UpdateMirroringEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1.Mirroring.UpdateMirroringEndpointGroupAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroupAssociations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.Mirroring.UpdateMirroringEndpointGroupAssociation" `  




### `google.cloud.networksecurity.v1.NetworkSecurity`

The following audit logs are associated with methods belonging to `google.cloud.networksecurity.v1.NetworkSecurity`.

#### `CreateAuthorizationPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.CreateAuthorizationPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.authorizationPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.CreateAuthorizationPolicy" `  




#### `CreateAuthzPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.CreateAuthzPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.authzPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.CreateAuthzPolicy" `  




#### `CreateBackendAuthenticationConfig`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.CreateBackendAuthenticationConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.backendAuthenticationConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.CreateBackendAuthenticationConfig" `  




#### `CreateClientTlsPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.CreateClientTlsPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.clientTlsPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.CreateClientTlsPolicy" `  




#### `CreateGatewaySecurityPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.CreateGatewaySecurityPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.gatewaySecurityPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.CreateGatewaySecurityPolicy" `  




#### `CreateGatewaySecurityPolicyRule`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.CreateGatewaySecurityPolicyRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.gatewaySecurityPolicyRules.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.CreateGatewaySecurityPolicyRule" `  




#### `CreateServerTlsPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.CreateServerTlsPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.serverTlsPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.CreateServerTlsPolicy" `  




#### `CreateTlsInspectionPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.CreateTlsInspectionPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.tlsInspectionPolicies.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.CreateTlsInspectionPolicy" `  




#### `CreateUrlList`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.CreateUrlList`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.urlLists.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.CreateUrlList" `  




#### `DeleteAuthorizationPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.DeleteAuthorizationPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.authorizationPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.DeleteAuthorizationPolicy" `  




#### `DeleteAuthzPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.DeleteAuthzPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.authzPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.DeleteAuthzPolicy" `  




#### `DeleteBackendAuthenticationConfig`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.DeleteBackendAuthenticationConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.backendAuthenticationConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.DeleteBackendAuthenticationConfig" `  




#### `DeleteClientTlsPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.DeleteClientTlsPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.clientTlsPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.DeleteClientTlsPolicy" `  




#### `DeleteGatewaySecurityPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.DeleteGatewaySecurityPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.gatewaySecurityPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.DeleteGatewaySecurityPolicy" `  




#### `DeleteGatewaySecurityPolicyRule`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.DeleteGatewaySecurityPolicyRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.gatewaySecurityPolicyRules.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.DeleteGatewaySecurityPolicyRule" `  




#### `DeleteServerTlsPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.DeleteServerTlsPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.serverTlsPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.DeleteServerTlsPolicy" `  




#### `DeleteTlsInspectionPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.DeleteTlsInspectionPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.tlsInspectionPolicies.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.DeleteTlsInspectionPolicy" `  




#### `DeleteUrlList`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.DeleteUrlList`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.urlLists.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.DeleteUrlList" `  




#### `GetAuthorizationPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.GetAuthorizationPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.authorizationPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.GetAuthorizationPolicy" `  




#### `GetAuthzPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.GetAuthzPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.authzPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.GetAuthzPolicy" `  




#### `GetBackendAuthenticationConfig`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.GetBackendAuthenticationConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.backendAuthenticationConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.GetBackendAuthenticationConfig" `  




#### `GetClientTlsPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.GetClientTlsPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.clientTlsPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.GetClientTlsPolicy" `  




#### `GetGatewaySecurityPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.GetGatewaySecurityPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.gatewaySecurityPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.GetGatewaySecurityPolicy" `  




#### `GetGatewaySecurityPolicyRule`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.GetGatewaySecurityPolicyRule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.gatewaySecurityPolicyRules.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.GetGatewaySecurityPolicyRule" `  




#### `GetServerTlsPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.GetServerTlsPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.serverTlsPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.GetServerTlsPolicy" `  




#### `GetTlsInspectionPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.GetTlsInspectionPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.tlsInspectionPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.GetTlsInspectionPolicy" `  




#### `GetUrlList`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.GetUrlList`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.urlLists.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.GetUrlList" `  




#### `ListAuthorizationPolicies`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.ListAuthorizationPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.authorizationPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.ListAuthorizationPolicies" `  




#### `ListAuthzPolicies`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.ListAuthzPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.authzPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.ListAuthzPolicies" `  




#### `ListBackendAuthenticationConfigs`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.ListBackendAuthenticationConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.backendAuthenticationConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.ListBackendAuthenticationConfigs" `  




#### `ListClientTlsPolicies`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.ListClientTlsPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.clientTlsPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.ListClientTlsPolicies" `  




#### `ListGatewaySecurityPolicies`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.ListGatewaySecurityPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.gatewaySecurityPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.ListGatewaySecurityPolicies" `  




#### `ListGatewaySecurityPolicyRules`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.ListGatewaySecurityPolicyRules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.gatewaySecurityPolicyRules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.ListGatewaySecurityPolicyRules" `  




#### `ListServerTlsPolicies`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.ListServerTlsPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.serverTlsPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.ListServerTlsPolicies" `  




#### `ListTlsInspectionPolicies`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.ListTlsInspectionPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.tlsInspectionPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.ListTlsInspectionPolicies" `  




#### `ListUrlLists`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.ListUrlLists`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.urlLists.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.ListUrlLists" `  




#### `UpdateAuthorizationPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.UpdateAuthorizationPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.authorizationPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.UpdateAuthorizationPolicy" `  




#### `UpdateAuthzPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.UpdateAuthzPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.authzPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.UpdateAuthzPolicy" `  




#### `UpdateBackendAuthenticationConfig`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.UpdateBackendAuthenticationConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.backendAuthenticationConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.UpdateBackendAuthenticationConfig" `  




#### `UpdateClientTlsPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.UpdateClientTlsPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.clientTlsPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.UpdateClientTlsPolicy" `  




#### `UpdateGatewaySecurityPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.UpdateGatewaySecurityPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.gatewaySecurityPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.UpdateGatewaySecurityPolicy" `  




#### `UpdateGatewaySecurityPolicyRule`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.UpdateGatewaySecurityPolicyRule`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.gatewaySecurityPolicyRules.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.UpdateGatewaySecurityPolicyRule" `  




#### `UpdateServerTlsPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.UpdateServerTlsPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.serverTlsPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.UpdateServerTlsPolicy" `  




#### `UpdateTlsInspectionPolicy`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.UpdateTlsInspectionPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.tlsInspectionPolicies.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.UpdateTlsInspectionPolicy" `  




#### `UpdateUrlList`

  * **Method** : `google.cloud.networksecurity.v1.NetworkSecurity.UpdateUrlList`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.urlLists.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.NetworkSecurity.UpdateUrlList" `  




### `google.cloud.networksecurity.v1.OrganizationAddressGroupService`

The following audit logs are associated with methods belonging to `google.cloud.networksecurity.v1.OrganizationAddressGroupService`.

#### `AddAddressGroupItems`

  * **Method** : `google.cloud.networksecurity.v1.OrganizationAddressGroupService.AddAddressGroupItems`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.addressGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.OrganizationAddressGroupService.AddAddressGroupItems" `  




#### `CloneAddressGroupItems`

  * **Method** : `google.cloud.networksecurity.v1.OrganizationAddressGroupService.CloneAddressGroupItems`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.addressGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.OrganizationAddressGroupService.CloneAddressGroupItems" `  




#### `CreateAddressGroup`

  * **Method** : `google.cloud.networksecurity.v1.OrganizationAddressGroupService.CreateAddressGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.addressGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.OrganizationAddressGroupService.CreateAddressGroup" `  




#### `DeleteAddressGroup`

  * **Method** : `google.cloud.networksecurity.v1.OrganizationAddressGroupService.DeleteAddressGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.addressGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.OrganizationAddressGroupService.DeleteAddressGroup" `  




#### `GetAddressGroup`

  * **Method** : `google.cloud.networksecurity.v1.OrganizationAddressGroupService.GetAddressGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.addressGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.OrganizationAddressGroupService.GetAddressGroup" `  




#### `ListAddressGroups`

  * **Method** : `google.cloud.networksecurity.v1.OrganizationAddressGroupService.ListAddressGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.addressGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.OrganizationAddressGroupService.ListAddressGroups" `  




#### `RemoveAddressGroupItems`

  * **Method** : `google.cloud.networksecurity.v1.OrganizationAddressGroupService.RemoveAddressGroupItems`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.addressGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.OrganizationAddressGroupService.RemoveAddressGroupItems" `  




#### `UpdateAddressGroup`

  * **Method** : `google.cloud.networksecurity.v1.OrganizationAddressGroupService.UpdateAddressGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.addressGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.OrganizationAddressGroupService.UpdateAddressGroup" `  




### `google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService`

The following audit logs are associated with methods belonging to `google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService`.

#### `CreateSecurityProfile`

  * **Method** : `google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.CreateSecurityProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.securityProfiles.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.CreateSecurityProfile" `  




#### `CreateSecurityProfileGroup`

  * **Method** : `google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.CreateSecurityProfileGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.securityProfileGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.CreateSecurityProfileGroup" `  




#### `DeleteSecurityProfile`

  * **Method** : `google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.DeleteSecurityProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.securityProfiles.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.DeleteSecurityProfile" `  




#### `DeleteSecurityProfileGroup`

  * **Method** : `google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.DeleteSecurityProfileGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.securityProfileGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.DeleteSecurityProfileGroup" `  




#### `GetSecurityProfile`

  * **Method** : `google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.GetSecurityProfile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.securityProfiles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.GetSecurityProfile" `  




#### `GetSecurityProfileGroup`

  * **Method** : `google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.GetSecurityProfileGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.securityProfileGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.GetSecurityProfileGroup" `  




#### `ListSecurityProfileGroups`

  * **Method** : `google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.ListSecurityProfileGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.securityProfileGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.ListSecurityProfileGroups" `  




#### `ListSecurityProfiles`

  * **Method** : `google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.ListSecurityProfiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.securityProfiles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.ListSecurityProfiles" `  




#### `UpdateSecurityProfile`

  * **Method** : `google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.UpdateSecurityProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.securityProfiles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.UpdateSecurityProfile" `  




#### `UpdateSecurityProfileGroup`

  * **Method** : `google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.UpdateSecurityProfileGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.securityProfileGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1.OrganizationSecurityProfileGroupService.UpdateSecurityProfileGroup" `  




### `google.cloud.networksecurity.v1alpha1.Intercept`

The following audit logs are associated with methods belonging to `google.cloud.networksecurity.v1alpha1.Intercept`.

#### `CreateInterceptDeployment`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Intercept.CreateInterceptDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptDeployments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Intercept.CreateInterceptDeployment" `  




#### `CreateInterceptDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Intercept.CreateInterceptDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptDeploymentGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Intercept.CreateInterceptDeploymentGroup" `  




#### `CreateInterceptEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Intercept.CreateInterceptEndpointGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Intercept.CreateInterceptEndpointGroup" `  




#### `CreateInterceptEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Intercept.CreateInterceptEndpointGroupAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroupAssociations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Intercept.CreateInterceptEndpointGroupAssociation" `  




#### `DeleteInterceptDeployment`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Intercept.DeleteInterceptDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptDeployments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Intercept.DeleteInterceptDeployment" `  




#### `DeleteInterceptDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Intercept.DeleteInterceptDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptDeploymentGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Intercept.DeleteInterceptDeploymentGroup" `  




#### `DeleteInterceptEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Intercept.DeleteInterceptEndpointGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Intercept.DeleteInterceptEndpointGroup" `  




#### `DeleteInterceptEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Intercept.DeleteInterceptEndpointGroupAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroupAssociations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Intercept.DeleteInterceptEndpointGroupAssociation" `  




#### `GetInterceptDeployment`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Intercept.GetInterceptDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptDeployments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Intercept.GetInterceptDeployment" `  




#### `GetInterceptDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Intercept.GetInterceptDeploymentGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptDeploymentGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Intercept.GetInterceptDeploymentGroup" `  




#### `GetInterceptEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Intercept.GetInterceptEndpointGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Intercept.GetInterceptEndpointGroup" `  




#### `GetInterceptEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Intercept.GetInterceptEndpointGroupAssociation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroupAssociations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Intercept.GetInterceptEndpointGroupAssociation" `  




#### `ListInterceptDeploymentGroups`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Intercept.ListInterceptDeploymentGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptDeploymentGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Intercept.ListInterceptDeploymentGroups" `  




#### `ListInterceptDeployments`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Intercept.ListInterceptDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptDeployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Intercept.ListInterceptDeployments" `  




#### `ListInterceptEndpointGroupAssociations`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Intercept.ListInterceptEndpointGroupAssociations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroupAssociations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Intercept.ListInterceptEndpointGroupAssociations" `  




#### `ListInterceptEndpointGroups`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Intercept.ListInterceptEndpointGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Intercept.ListInterceptEndpointGroups" `  




#### `UpdateInterceptDeployment`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Intercept.UpdateInterceptDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptDeployments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Intercept.UpdateInterceptDeployment" `  




#### `UpdateInterceptDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Intercept.UpdateInterceptDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptDeploymentGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Intercept.UpdateInterceptDeploymentGroup" `  




#### `UpdateInterceptEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Intercept.UpdateInterceptEndpointGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Intercept.UpdateInterceptEndpointGroup" `  




#### `UpdateInterceptEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Intercept.UpdateInterceptEndpointGroupAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroupAssociations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Intercept.UpdateInterceptEndpointGroupAssociation" `  




### `google.cloud.networksecurity.v1alpha1.Mirroring`

The following audit logs are associated with methods belonging to `google.cloud.networksecurity.v1alpha1.Mirroring`.

#### `CreateMirroringDeployment`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Mirroring.CreateMirroringDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringDeployments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Mirroring.CreateMirroringDeployment" `  




#### `CreateMirroringDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Mirroring.CreateMirroringDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringDeploymentGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Mirroring.CreateMirroringDeploymentGroup" `  




#### `CreateMirroringEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Mirroring.CreateMirroringEndpointGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Mirroring.CreateMirroringEndpointGroup" `  




#### `CreateMirroringEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Mirroring.CreateMirroringEndpointGroupAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroupAssociations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Mirroring.CreateMirroringEndpointGroupAssociation" `  




#### `DeleteMirroringDeployment`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Mirroring.DeleteMirroringDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringDeployments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Mirroring.DeleteMirroringDeployment" `  




#### `DeleteMirroringDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Mirroring.DeleteMirroringDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringDeploymentGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Mirroring.DeleteMirroringDeploymentGroup" `  




#### `DeleteMirroringEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Mirroring.DeleteMirroringEndpointGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Mirroring.DeleteMirroringEndpointGroup" `  




#### `DeleteMirroringEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Mirroring.DeleteMirroringEndpointGroupAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroupAssociations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Mirroring.DeleteMirroringEndpointGroupAssociation" `  




#### `GetMirroringDeployment`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Mirroring.GetMirroringDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringDeployments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Mirroring.GetMirroringDeployment" `  




#### `GetMirroringDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Mirroring.GetMirroringDeploymentGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringDeploymentGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Mirroring.GetMirroringDeploymentGroup" `  




#### `GetMirroringEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Mirroring.GetMirroringEndpointGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Mirroring.GetMirroringEndpointGroup" `  




#### `GetMirroringEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Mirroring.GetMirroringEndpointGroupAssociation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroupAssociations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Mirroring.GetMirroringEndpointGroupAssociation" `  




#### `ListMirroringDeploymentGroups`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Mirroring.ListMirroringDeploymentGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringDeploymentGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Mirroring.ListMirroringDeploymentGroups" `  




#### `ListMirroringDeployments`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Mirroring.ListMirroringDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringDeployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Mirroring.ListMirroringDeployments" `  




#### `ListMirroringEndpointGroupAssociations`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Mirroring.ListMirroringEndpointGroupAssociations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroupAssociations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Mirroring.ListMirroringEndpointGroupAssociations" `  




#### `ListMirroringEndpointGroups`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Mirroring.ListMirroringEndpointGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Mirroring.ListMirroringEndpointGroups" `  




#### `UpdateMirroringDeployment`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Mirroring.UpdateMirroringDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringDeployments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Mirroring.UpdateMirroringDeployment" `  




#### `UpdateMirroringDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Mirroring.UpdateMirroringDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringDeploymentGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Mirroring.UpdateMirroringDeploymentGroup" `  




#### `UpdateMirroringEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Mirroring.UpdateMirroringEndpointGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Mirroring.UpdateMirroringEndpointGroup" `  




#### `UpdateMirroringEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1alpha1.Mirroring.UpdateMirroringEndpointGroupAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroupAssociations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.Mirroring.UpdateMirroringEndpointGroupAssociation" `  




### `google.cloud.networksecurity.v1alpha1.SSEGatewayService`

The following audit logs are associated with methods belonging to `google.cloud.networksecurity.v1alpha1.SSEGatewayService`.

#### `CreatePartnerSSEGateway`

  * **Method** : `google.cloud.networksecurity.v1alpha1.SSEGatewayService.CreatePartnerSSEGateway`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.partnerSSEGateways.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.SSEGatewayService.CreatePartnerSSEGateway" `  




#### `DeletePartnerSSEGateway`

  * **Method** : `google.cloud.networksecurity.v1alpha1.SSEGatewayService.DeletePartnerSSEGateway`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.partnerSSEGateways.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.SSEGatewayService.DeletePartnerSSEGateway" `  




#### `GetPartnerSSEGateway`

  * **Method** : `google.cloud.networksecurity.v1alpha1.SSEGatewayService.GetPartnerSSEGateway`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.partnerSSEGateways.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.SSEGatewayService.GetPartnerSSEGateway" `  




#### `UpdatePartnerSSEGateway`

  * **Method** : `google.cloud.networksecurity.v1alpha1.SSEGatewayService.UpdatePartnerSSEGateway`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.partnerSSEGateways.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.SSEGatewayService.UpdatePartnerSSEGateway" `  




### `google.cloud.networksecurity.v1alpha1.SSERealmService`

The following audit logs are associated with methods belonging to `google.cloud.networksecurity.v1alpha1.SSERealmService`.

#### `CreatePartnerSSERealm`

  * **Method** : `google.cloud.networksecurity.v1alpha1.SSERealmService.CreatePartnerSSERealm`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.partnerSSERealms.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.SSERealmService.CreatePartnerSSERealm" `  




#### `CreateSACAttachment`

  * **Method** : `google.cloud.networksecurity.v1alpha1.SSERealmService.CreateSACAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.sacAttachments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.SSERealmService.CreateSACAttachment" `  




#### `CreateSACRealm`

  * **Method** : `google.cloud.networksecurity.v1alpha1.SSERealmService.CreateSACRealm`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.sacRealms.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.SSERealmService.CreateSACRealm" `  




#### `DeletePartnerSSERealm`

  * **Method** : `google.cloud.networksecurity.v1alpha1.SSERealmService.DeletePartnerSSERealm`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.partnerSSERealms.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.SSERealmService.DeletePartnerSSERealm" `  




#### `DeleteSACAttachment`

  * **Method** : `google.cloud.networksecurity.v1alpha1.SSERealmService.DeleteSACAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.sacAttachments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.SSERealmService.DeleteSACAttachment" `  




#### `DeleteSACRealm`

  * **Method** : `google.cloud.networksecurity.v1alpha1.SSERealmService.DeleteSACRealm`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.sacRealms.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.SSERealmService.DeleteSACRealm" `  




#### `ListSACAttachments`

  * **Method** : `google.cloud.networksecurity.v1alpha1.SSERealmService.ListSACAttachments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.sacAttachments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1alpha1.SSERealmService.ListSACAttachments" `  




### `google.cloud.networksecurity.v1beta1.Intercept`

The following audit logs are associated with methods belonging to `google.cloud.networksecurity.v1beta1.Intercept`.

#### `CreateInterceptDeployment`

  * **Method** : `google.cloud.networksecurity.v1beta1.Intercept.CreateInterceptDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptDeployments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Intercept.CreateInterceptDeployment" `  




#### `CreateInterceptDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1beta1.Intercept.CreateInterceptDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptDeploymentGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Intercept.CreateInterceptDeploymentGroup" `  




#### `CreateInterceptEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1beta1.Intercept.CreateInterceptEndpointGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Intercept.CreateInterceptEndpointGroup" `  




#### `CreateInterceptEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1beta1.Intercept.CreateInterceptEndpointGroupAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroupAssociations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Intercept.CreateInterceptEndpointGroupAssociation" `  




#### `DeleteInterceptDeployment`

  * **Method** : `google.cloud.networksecurity.v1beta1.Intercept.DeleteInterceptDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptDeployments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Intercept.DeleteInterceptDeployment" `  




#### `DeleteInterceptDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1beta1.Intercept.DeleteInterceptDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptDeploymentGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Intercept.DeleteInterceptDeploymentGroup" `  




#### `DeleteInterceptEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1beta1.Intercept.DeleteInterceptEndpointGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Intercept.DeleteInterceptEndpointGroup" `  




#### `DeleteInterceptEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1beta1.Intercept.DeleteInterceptEndpointGroupAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroupAssociations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Intercept.DeleteInterceptEndpointGroupAssociation" `  




#### `GetInterceptDeployment`

  * **Method** : `google.cloud.networksecurity.v1beta1.Intercept.GetInterceptDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptDeployments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Intercept.GetInterceptDeployment" `  




#### `GetInterceptDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1beta1.Intercept.GetInterceptDeploymentGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptDeploymentGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Intercept.GetInterceptDeploymentGroup" `  




#### `GetInterceptEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1beta1.Intercept.GetInterceptEndpointGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Intercept.GetInterceptEndpointGroup" `  




#### `GetInterceptEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1beta1.Intercept.GetInterceptEndpointGroupAssociation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroupAssociations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Intercept.GetInterceptEndpointGroupAssociation" `  




#### `ListInterceptDeploymentGroups`

  * **Method** : `google.cloud.networksecurity.v1beta1.Intercept.ListInterceptDeploymentGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptDeploymentGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Intercept.ListInterceptDeploymentGroups" `  




#### `ListInterceptDeployments`

  * **Method** : `google.cloud.networksecurity.v1beta1.Intercept.ListInterceptDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptDeployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Intercept.ListInterceptDeployments" `  




#### `ListInterceptEndpointGroupAssociations`

  * **Method** : `google.cloud.networksecurity.v1beta1.Intercept.ListInterceptEndpointGroupAssociations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroupAssociations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Intercept.ListInterceptEndpointGroupAssociations" `  




#### `ListInterceptEndpointGroups`

  * **Method** : `google.cloud.networksecurity.v1beta1.Intercept.ListInterceptEndpointGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Intercept.ListInterceptEndpointGroups" `  




#### `UpdateInterceptDeployment`

  * **Method** : `google.cloud.networksecurity.v1beta1.Intercept.UpdateInterceptDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptDeployments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Intercept.UpdateInterceptDeployment" `  




#### `UpdateInterceptDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1beta1.Intercept.UpdateInterceptDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptDeploymentGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Intercept.UpdateInterceptDeploymentGroup" `  




#### `UpdateInterceptEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1beta1.Intercept.UpdateInterceptEndpointGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Intercept.UpdateInterceptEndpointGroup" `  




#### `UpdateInterceptEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1beta1.Intercept.UpdateInterceptEndpointGroupAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.interceptEndpointGroupAssociations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Intercept.UpdateInterceptEndpointGroupAssociation" `  




### `google.cloud.networksecurity.v1beta1.Mirroring`

The following audit logs are associated with methods belonging to `google.cloud.networksecurity.v1beta1.Mirroring`.

#### `CreateMirroringDeployment`

  * **Method** : `google.cloud.networksecurity.v1beta1.Mirroring.CreateMirroringDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringDeployments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Mirroring.CreateMirroringDeployment" `  




#### `CreateMirroringDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1beta1.Mirroring.CreateMirroringDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringDeploymentGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Mirroring.CreateMirroringDeploymentGroup" `  




#### `CreateMirroringEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1beta1.Mirroring.CreateMirroringEndpointGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Mirroring.CreateMirroringEndpointGroup" `  




#### `CreateMirroringEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1beta1.Mirroring.CreateMirroringEndpointGroupAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroupAssociations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Mirroring.CreateMirroringEndpointGroupAssociation" `  




#### `DeleteMirroringDeployment`

  * **Method** : `google.cloud.networksecurity.v1beta1.Mirroring.DeleteMirroringDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringDeployments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Mirroring.DeleteMirroringDeployment" `  




#### `DeleteMirroringDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1beta1.Mirroring.DeleteMirroringDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringDeploymentGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Mirroring.DeleteMirroringDeploymentGroup" `  




#### `DeleteMirroringEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1beta1.Mirroring.DeleteMirroringEndpointGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroups.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Mirroring.DeleteMirroringEndpointGroup" `  




#### `DeleteMirroringEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1beta1.Mirroring.DeleteMirroringEndpointGroupAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroupAssociations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Mirroring.DeleteMirroringEndpointGroupAssociation" `  




#### `GetMirroringDeployment`

  * **Method** : `google.cloud.networksecurity.v1beta1.Mirroring.GetMirroringDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringDeployments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Mirroring.GetMirroringDeployment" `  




#### `GetMirroringDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1beta1.Mirroring.GetMirroringDeploymentGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringDeploymentGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Mirroring.GetMirroringDeploymentGroup" `  




#### `GetMirroringEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1beta1.Mirroring.GetMirroringEndpointGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Mirroring.GetMirroringEndpointGroup" `  




#### `GetMirroringEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1beta1.Mirroring.GetMirroringEndpointGroupAssociation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroupAssociations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Mirroring.GetMirroringEndpointGroupAssociation" `  




#### `ListMirroringDeploymentGroups`

  * **Method** : `google.cloud.networksecurity.v1beta1.Mirroring.ListMirroringDeploymentGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringDeploymentGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Mirroring.ListMirroringDeploymentGroups" `  




#### `ListMirroringDeployments`

  * **Method** : `google.cloud.networksecurity.v1beta1.Mirroring.ListMirroringDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringDeployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Mirroring.ListMirroringDeployments" `  




#### `ListMirroringEndpointGroupAssociations`

  * **Method** : `google.cloud.networksecurity.v1beta1.Mirroring.ListMirroringEndpointGroupAssociations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroupAssociations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Mirroring.ListMirroringEndpointGroupAssociations" `  




#### `ListMirroringEndpointGroups`

  * **Method** : `google.cloud.networksecurity.v1beta1.Mirroring.ListMirroringEndpointGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroups.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Mirroring.ListMirroringEndpointGroups" `  




#### `UpdateMirroringDeployment`

  * **Method** : `google.cloud.networksecurity.v1beta1.Mirroring.UpdateMirroringDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringDeployments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Mirroring.UpdateMirroringDeployment" `  




#### `UpdateMirroringDeploymentGroup`

  * **Method** : `google.cloud.networksecurity.v1beta1.Mirroring.UpdateMirroringDeploymentGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringDeploymentGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Mirroring.UpdateMirroringDeploymentGroup" `  




#### `UpdateMirroringEndpointGroup`

  * **Method** : `google.cloud.networksecurity.v1beta1.Mirroring.UpdateMirroringEndpointGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Mirroring.UpdateMirroringEndpointGroup" `  




#### `UpdateMirroringEndpointGroupAssociation`

  * **Method** : `google.cloud.networksecurity.v1beta1.Mirroring.UpdateMirroringEndpointGroupAssociation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.mirroringEndpointGroupAssociations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.Mirroring.UpdateMirroringEndpointGroupAssociation" `  




### `google.cloud.networksecurity.v1beta1.SSERealmService`

The following audit logs are associated with methods belonging to `google.cloud.networksecurity.v1beta1.SSERealmService`.

#### `CreateSACAttachment`

  * **Method** : `google.cloud.networksecurity.v1beta1.SSERealmService.CreateSACAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.sacAttachments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.SSERealmService.CreateSACAttachment" `  




#### `CreateSACRealm`

  * **Method** : `google.cloud.networksecurity.v1beta1.SSERealmService.CreateSACRealm`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.sacRealms.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.SSERealmService.CreateSACRealm" `  




#### `DeleteSACAttachment`

  * **Method** : `google.cloud.networksecurity.v1beta1.SSERealmService.DeleteSACAttachment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.sacAttachments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.SSERealmService.DeleteSACAttachment" `  




#### `DeleteSACRealm`

  * **Method** : `google.cloud.networksecurity.v1beta1.SSERealmService.DeleteSACRealm`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.sacRealms.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.SSERealmService.DeleteSACRealm" `  




#### `ListSACAttachments`

  * **Method** : `google.cloud.networksecurity.v1beta1.SSERealmService.ListSACAttachments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.sacAttachments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.SSERealmService.ListSACAttachments" `  




#### `ListSACRealms`

  * **Method** : `google.cloud.networksecurity.v1beta1.SSERealmService.ListSACRealms`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.sacRealms.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.networksecurity.v1beta1.SSERealmService.ListSACRealms" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.clientTlsPolicies.getIamPolicy - ADMIN_READ`
    * `networksecurity.serverTlsPolicies.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.addressGroups.setIamPolicy - ADMIN_WRITE`
    * `networksecurity.authorizationPolicies.setIamPolicy - ADMIN_WRITE`
    * `networksecurity.authzPolicies.setIamPolicy - ADMIN_WRITE`
    * `networksecurity.clientTlsPolicies.setIamPolicy - ADMIN_WRITE`
    * `networksecurity.serverTlsPolicies.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `networksecurity.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `networksecurity.operations.list - ADMIN_READ`
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



## Available audit logs

The following types of audit logs are available for Cloud Next Generation Firewall:

  * Admin Activity audit logs 

Includes "admin write" operations that write metadata or configuration information. 

You can't disable Admin Activity audit logs. 

  * Data Access audit logs 

Includes "admin read" operations that read metadata or configuration information. 

To receive Data Access audit logs, you must [ explicitly enable](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable) them. 




For fuller descriptions of the audit log types, see [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types).

## Audit log format

Audit log entries include the following objects:

  * The log entry itself, which is an object of type [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry). Useful fields include the following:

    * The `logName` contains the resource ID and audit log type.
    * The `resource` contains the target of the audited operation.
    * The `timeStamp` contains the time of the audited operation.
    * The `protoPayload` contains the audited information.
  * The audit logging data, which is an [`AuditLog`](https://docs.cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog) object held in the `protoPayload` field of the log entry.

  * Optional service-specific audit information, which is a service-specific object. For earlier integrations, this object is held in the `serviceData` field of the `AuditLog` object; later integrations use the `metadata` field.




For other fields in these objects, and how to interpret them, review [Understand audit logs](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs).

### Log name

Cloud Audit Logs log names include resource identifiers indicating the Google Cloud project or other Google Cloud entity that owns the audit logs, and whether the log contains Admin Activity, Data Access, Policy Denied, or System Event audit logging data.

The following are the audit log names, including variables for the resource identifiers:
    
    
       projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity
       projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fdata_access
       projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event
       projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fpolicy
    
       folders/FOLDER_ID/logs/cloudaudit.googleapis.com%2Factivity
       folders/FOLDER_ID/logs/cloudaudit.googleapis.com%2Fdata_access
       folders/FOLDER_ID/logs/cloudaudit.googleapis.com%2Fsystem_event
       folders/FOLDER_ID/logs/cloudaudit.googleapis.com%2Fpolicy
    
       billingAccounts/BILLING_ACCOUNT_ID/logs/cloudaudit.googleapis.com%2Factivity
       billingAccounts/BILLING_ACCOUNT_ID/logs/cloudaudit.googleapis.com%2Fdata_access
       billingAccounts/BILLING_ACCOUNT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event
       billingAccounts/BILLING_ACCOUNT_ID/logs/cloudaudit.googleapis.com%2Fpolicy
    
       organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Factivity
       organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Fdata_access
       organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Fsystem_event
       organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Fpolicy
    

**Note:** The part of the log name following `/logs/` must be URL-encoded. The forward-slash character, `/`, must be written as `%2F`.

## Enable audit logging

Admin Activity audit logs are always enabled; you can't disable them.

Data Access audit logs are disabled by default and aren't written unless explicitly enabled (the exception is Data Access audit logs for BigQuery, which can't be disabled).

For information about enabling some or all of your Data Access audit logs, see [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).

## View audit logs

You can query for all audit logs or you can query for logs by their audit log name. The audit log name includes the [resource identifier](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project, folder, billing account, or organization for which you want to view audit logging information. Your queries can specify indexed [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) fields, and if you use the **Log Analytics** page, which supports SQL queries, then you can [view your query results as a chart](https://docs.cloud.google.com/logging/docs/analyze/charts).

For more information about querying your logs, see the following pages:

  * [Build queries in the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries).
  * [Query and view logs in Observability Analytics](https://docs.cloud.google.com/logging/docs/analyze/query-and-view).
  * [Sample queries for security insights](https://docs.cloud.google.com/logging/docs/analyze/analyze-audit-logs).



You can view audit logs in Cloud Logging by using the Google Cloud console, the Google Cloud CLI, or the Logging API.

### Console

In the Google Cloud console, you can use the Logs Explorer to retrieve your audit log entries for your Google Cloud project, folder, or organization:

**Note:** You can't view audit logs for Cloud Billing accounts in the Google Cloud console. You must use the API or the gcloud CLI.

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Select an existing Google Cloud project, folder, or organization.

  3. To display all audit logs, enter either of the following queries into the query-editor field, and then click **Run query** :
         
         logName:"cloudaudit.googleapis.com"
         
         
         protoPayload."@type"="type.googleapis.com/google.cloud.audit.AuditLog"
         

  4. To display the audit logs for a specific resource and audit log type, in the **Query builder** pane, do the following:

     * In **Resource type** , select the Google Cloud resource whose audit logs you want to see.

     * In **Log name** , select the audit log type that you want to see:

       * For Admin Activity audit logs, select **activity**.
       * For Data Access audit logs, select **data_access**.
       * For System Event audit logs, select **system_event**.
       * For Policy Denied audit logs, select **policy**.
     * Click **Run query**.

If you don't see these options, then there aren't any audit logs of that type available in the Google Cloud project, folder, or organization.

If you're experiencing issues when trying to view logs in the Logs Explorer, see the [troubleshooting](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#troubleshooting) information.

For more information about querying by using the Logs Explorer, see [Build queries in the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries). For information about summarizing log entries in the Logs Explorer by using Gemini, see [Summarize log entries with Gemini assistance](https://docs.cloud.google.com/logging/docs/view/summarize-log-entries-gemini).




### gcloud

The Google Cloud CLI provides a command-line interface to the Logging API. Supply a valid resource identifier in each of the log names. For example, if your query includes a PROJECT_ID, then the project identifier you supply must refer to the currently selected Google Cloud project.

To read your Google Cloud project-level audit log entries, run the following command:
    
    
    gcloud logging read "logName : projects/PROJECT_ID/logs/cloudaudit.googleapis.com" \
        --project=PROJECT_ID
    

To read your folder-level audit log entries, run the following command:
    
    
    gcloud logging read "logName : folders/FOLDER_ID/logs/cloudaudit.googleapis.com" \
        --folder=FOLDER_ID
    

To read your organization-level audit log entries, run the following command:
    
    
    gcloud logging read "logName : organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com" \
        --organization=ORGANIZATION_ID
    

To read your Cloud Billing account-level audit log entries, run the following command:
    
    
    gcloud logging read "logName : billingAccounts/BILLING_ACCOUNT_ID/logs/cloudaudit.googleapis.com" \
        --billing-account=BILLING_ACCOUNT_ID
    

Add the [`--freshness` flag](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read#--freshness) to your command to read logs that are more than 1 day old.

For more information about using the gcloud CLI, see [`gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read).

### API

When building your queries, supply a valid resource identifier in each of the log names. For example, if your query includes a PROJECT_ID, then the project identifier you supply must refer to the currently selected Google Cloud project.

For example, to use the Logging API to view your project-level audit log entries, do the following:

  1. Go to the **Try this API** section in the documentation for the [`entries.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list) method.

  2. Put the following into the **Request body** part of the **Try this API** form. Clicking this [prepopulated form](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list?apix_params=%7B%22resource%22%3A%7B%22resourceNames%22%3A%5B%22projects%2F%5BPROJECT_ID%5D%22%5D%2C%22pageSize%22%3A5%2C%22filter%22%3A%22logName%3D\(projects%2F%5BPROJECT_ID%5D%2Flogs%2Fcloudaudit.googleapis.com%252Factivity%20OR%20projects%2F%5BPROJECT_ID%5D%2Flogs%2Fcloudaudit.googleapis.com%252Fsystem_events%20OR%20projects%2F%5BPROJECT_ID%5D%2Flogs%2Fcloudaudit.googleapis.com%252Fdata_access\)%22%7D%7D) automatically fills the request body, but you need to supply a valid PROJECT_ID in each of the log names.
         
         {
           "resourceNames": [
             "projects/PROJECT_ID"
           ],
           "pageSize": 5,
           "filter": "logName : projects/PROJECT_ID/logs/cloudaudit.googleapis.com"
         }
         

  3. Click **Execute**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
