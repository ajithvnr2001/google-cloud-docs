---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent/audit-logging-gkehub/
title: GKE Hub audit logging \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:56.214847+00:00
---

# GKE Hub audit logging  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent/audit-logging-gkehub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  GKE Hub audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for GKE Hub. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

GKE Hub audit logs use the service name `gkehub.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="gkehub.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, GKE Hub generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.gkehub.v1.GkeHub.GenerateConnectManifest`  
`google.cloud.gkehub.v1.GkeHub.GenerateMembershipRBACRoleBindingYAML`  
`google.cloud.gkehub.v1.GkeHub.GetFeature`  
`google.cloud.gkehub.v1.GkeHub.GetFleet`  
`google.cloud.gkehub.v1.GkeHub.GetMembership`  
`google.cloud.gkehub.v1.GkeHub.GetMembershipBinding`  
`google.cloud.gkehub.v1.GkeHub.GetMembershipRBACRoleBinding`  
`google.cloud.gkehub.v1.GkeHub.GetScope`  
`google.cloud.gkehub.v1.GkeHub.GetScopeNamespace`  
`google.cloud.gkehub.v1.GkeHub.GetScopeRBACRoleBinding`  
`google.cloud.gkehub.v1.GkeHub.ListBoundMemberships`  
`google.cloud.gkehub.v1.GkeHub.ListFeatures`  
`google.cloud.gkehub.v1.GkeHub.ListMembershipBindings`  
`google.cloud.gkehub.v1.GkeHub.ListMembershipRBACRoleBindings`  
`google.cloud.gkehub.v1.GkeHub.ListMemberships`  
`google.cloud.gkehub.v1.GkeHub.ListScopeNamespaces`  
`google.cloud.gkehub.v1.GkeHub.ListScopeRBACRoleBindings`  
`google.cloud.gkehub.v1.GkeHub.ListScopes`  
`google.cloud.gkehub.v1alpha.GkeHub.GenerateConnectManifest`  
`google.cloud.gkehub.v1alpha.GkeHub.GenerateExclusivityManifest`  
`google.cloud.gkehub.v1alpha.GkeHub.GenerateMembershipRBACRoleBindingYAML`  
`google.cloud.gkehub.v1alpha.GkeHub.GetFeature`  
`google.cloud.gkehub.v1alpha.GkeHub.GetFleet`  
`google.cloud.gkehub.v1alpha.GkeHub.GetMembership`  
`google.cloud.gkehub.v1alpha.GkeHub.GetMembershipBinding`  
`google.cloud.gkehub.v1alpha.GkeHub.GetMembershipRBACRoleBinding`  
`google.cloud.gkehub.v1alpha.GkeHub.GetScope`  
`google.cloud.gkehub.v1alpha.GkeHub.GetScopeNamespace`  
`google.cloud.gkehub.v1alpha.GkeHub.GetScopeRBACRoleBinding`  
`google.cloud.gkehub.v1alpha.GkeHub.ListAdminClusterMemberships`  
`google.cloud.gkehub.v1alpha.GkeHub.ListBoundMemberships`  
`google.cloud.gkehub.v1alpha.GkeHub.ListFeatures`  
`google.cloud.gkehub.v1alpha.GkeHub.ListMembershipBindings`  
`google.cloud.gkehub.v1alpha.GkeHub.ListMembershipRBACRoleBindings`  
`google.cloud.gkehub.v1alpha.GkeHub.ListMemberships`  
`google.cloud.gkehub.v1alpha.GkeHub.ListScopeNamespaces`  
`google.cloud.gkehub.v1alpha.GkeHub.ListScopeRBACRoleBindings`  
`google.cloud.gkehub.v1alpha.GkeHub.ListScopes`  
`google.cloud.gkehub.v1alpha.GkeHub.ValidateExclusivity`  
`google.cloud.gkehub.v1alpha1.GkeHubDomainFeatureService.GetFeature`  
`google.cloud.gkehub.v1alpha1.GkeHubDomainFeatureService.ListFeatures`  
`google.cloud.gkehub.v1beta.GkeHub.GenerateConnectManifest`  
`google.cloud.gkehub.v1beta.GkeHub.GenerateMembershipRBACRoleBindingYAML`  
`google.cloud.gkehub.v1beta.GkeHub.GetFeature`  
`google.cloud.gkehub.v1beta.GkeHub.GetFleet`  
`google.cloud.gkehub.v1beta.GkeHub.GetMembership`  
`google.cloud.gkehub.v1beta.GkeHub.GetMembershipBinding`  
`google.cloud.gkehub.v1beta.GkeHub.GetMembershipRBACRoleBinding`  
`google.cloud.gkehub.v1beta.GkeHub.GetScope`  
`google.cloud.gkehub.v1beta.GkeHub.GetScopeNamespace`  
`google.cloud.gkehub.v1beta.GkeHub.GetScopeRBACRoleBinding`  
`google.cloud.gkehub.v1beta.GkeHub.ListBoundMemberships`  
`google.cloud.gkehub.v1beta.GkeHub.ListFeatures`  
`google.cloud.gkehub.v1beta.GkeHub.ListMembershipBindings`  
`google.cloud.gkehub.v1beta.GkeHub.ListMembershipRBACRoleBindings`  
`google.cloud.gkehub.v1beta.GkeHub.ListMemberships`  
`google.cloud.gkehub.v1beta.GkeHub.ListScopeNamespaces`  
`google.cloud.gkehub.v1beta.GkeHub.ListScopeRBACRoleBindings`  
`google.cloud.gkehub.v1beta.GkeHub.ListScopes`  
`google.cloud.gkehub.v1beta1.GkeHubMembershipService.GenerateConnectManifest`  
`google.cloud.gkehub.v1beta1.GkeHubMembershipService.GenerateExclusivityManifest`  
`google.cloud.gkehub.v1beta1.GkeHubMembershipService.GetMembership`  
`google.cloud.gkehub.v1beta1.GkeHubMembershipService.ListMemberships`  
`google.cloud.gkehub.v1beta1.GkeHubMembershipService.ValidateExclusivity`  
`google.cloud.gkehub.v2.GkeHubFeature.GetMembershipFeature`  
`google.cloud.gkehub.v2.GkeHubFeature.ListMembershipFeatures`  
`google.cloud.gkehub.v2alpha.GkeHubFeature.GetMembershipFeature`  
`google.cloud.gkehub.v2alpha.GkeHubFeature.ListMembershipFeatures`  
`google.cloud.gkehub.v2beta.GkeHubFeature.GetMembershipFeature`  
`google.cloud.gkehub.v2beta.GkeHubFeature.ListMembershipFeatures`  
`GetIamPolicy`  
`ADMIN_WRITE` | `google.cloud.gkehub.v1.GkeHub.CreateFeature` (LRO)  
`google.cloud.gkehub.v1.GkeHub.CreateFleet` (LRO)  
`google.cloud.gkehub.v1.GkeHub.CreateMembership` (LRO)  
`google.cloud.gkehub.v1.GkeHub.CreateMembershipBinding` (LRO)  
`google.cloud.gkehub.v1.GkeHub.CreateMembershipRBACRoleBinding` (LRO)  
`google.cloud.gkehub.v1.GkeHub.CreateScope` (LRO)  
`google.cloud.gkehub.v1.GkeHub.CreateScopeNamespace` (LRO)  
`google.cloud.gkehub.v1.GkeHub.CreateScopeRBACRoleBinding` (LRO)  
`google.cloud.gkehub.v1.GkeHub.DeleteFeature` (LRO)  
`google.cloud.gkehub.v1.GkeHub.DeleteFleet` (LRO)  
`google.cloud.gkehub.v1.GkeHub.DeleteMembership` (LRO)  
`google.cloud.gkehub.v1.GkeHub.DeleteMembershipBinding` (LRO)  
`google.cloud.gkehub.v1.GkeHub.DeleteMembershipRBACRoleBinding` (LRO)  
`google.cloud.gkehub.v1.GkeHub.DeleteScope` (LRO)  
`google.cloud.gkehub.v1.GkeHub.DeleteScopeNamespace` (LRO)  
`google.cloud.gkehub.v1.GkeHub.DeleteScopeRBACRoleBinding` (LRO)  
`google.cloud.gkehub.v1.GkeHub.UpdateFeature` (LRO)  
`google.cloud.gkehub.v1.GkeHub.UpdateFleet` (LRO)  
`google.cloud.gkehub.v1.GkeHub.UpdateMembership` (LRO)  
`google.cloud.gkehub.v1.GkeHub.UpdateMembershipBinding` (LRO)  
`google.cloud.gkehub.v1.GkeHub.UpdateMembershipRBACRoleBinding` (LRO)  
`google.cloud.gkehub.v1.GkeHub.UpdateScope` (LRO)  
`google.cloud.gkehub.v1.GkeHub.UpdateScopeNamespace` (LRO)  
`google.cloud.gkehub.v1.GkeHub.UpdateScopeRBACRoleBinding` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.CreateFeature` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.CreateFleet` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.CreateMembership` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.CreateMembershipBinding` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.CreateMembershipRBACRoleBinding` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.CreateScope` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.CreateScopeNamespace` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.CreateScopeRBACRoleBinding` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.DeleteFeature` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.DeleteFleet` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.DeleteMembership` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.DeleteMembershipBinding` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.DeleteMembershipRBACRoleBinding` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.DeleteScope` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.DeleteScopeNamespace` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.DeleteScopeRBACRoleBinding` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.UpdateFeature` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.UpdateFleet` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.UpdateMembership` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.UpdateMembershipBinding` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.UpdateMembershipRBACRoleBinding` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.UpdateScope` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.UpdateScopeNamespace` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.UpdateScopeRBACRoleBinding` (LRO)  
`google.cloud.gkehub.v1alpha.GkeHub.ValidateCreateMembership`  
`google.cloud.gkehub.v1alpha1.GkeHubDomainFeatureService.CreateFeature` (LRO)  
`google.cloud.gkehub.v1alpha1.GkeHubDomainFeatureService.DeleteFeature` (LRO)  
`google.cloud.gkehub.v1alpha1.GkeHubDomainFeatureService.UpdateFeature` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.CreateFeature` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.CreateFleet` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.CreateMembership` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.CreateMembershipBinding` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.CreateMembershipRBACRoleBinding` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.CreateScope` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.CreateScopeNamespace` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.CreateScopeRBACRoleBinding` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.DeleteFeature` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.DeleteFleet` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.DeleteMembership` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.DeleteMembershipBinding` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.DeleteMembershipRBACRoleBinding` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.DeleteScope` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.DeleteScopeNamespace` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.DeleteScopeRBACRoleBinding` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.UpdateFeature` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.UpdateFleet` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.UpdateMembership` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.UpdateMembershipBinding` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.UpdateMembershipRBACRoleBinding` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.UpdateScope` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.UpdateScopeNamespace` (LRO)  
`google.cloud.gkehub.v1beta.GkeHub.UpdateScopeRBACRoleBinding` (LRO)  
`google.cloud.gkehub.v1beta1.GkeHubMembershipService.CreateMembership` (LRO)  
`google.cloud.gkehub.v1beta1.GkeHubMembershipService.DeleteMembership` (LRO)  
`google.cloud.gkehub.v1beta1.GkeHubMembershipService.UpdateMembership` (LRO)  
`google.cloud.gkehub.v2.GkeHubFeature.CreateMembershipFeature` (LRO)  
`google.cloud.gkehub.v2.GkeHubFeature.DeleteMembershipFeature` (LRO)  
`google.cloud.gkehub.v2.GkeHubFeature.UpdateMembershipFeature` (LRO)  
`google.cloud.gkehub.v2alpha.GkeHubFeature.CreateMembershipFeature` (LRO)  
`google.cloud.gkehub.v2alpha.GkeHubFeature.DeleteMembershipFeature` (LRO)  
`google.cloud.gkehub.v2alpha.GkeHubFeature.UpdateMembershipFeature` (LRO)  
`google.cloud.gkehub.v2beta.GkeHubFeature.CreateMembershipFeature` (LRO)  
`google.cloud.gkehub.v2beta.GkeHubFeature.DeleteMembershipFeature` (LRO)  
`google.cloud.gkehub.v2beta.GkeHubFeature.UpdateMembershipFeature` (LRO)  
`SetIamPolicy`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for GKE Hub.

### `google.cloud.gkehub.v1.GkeHub`

The following audit logs are associated with methods belonging to `google.cloud.gkehub.v1.GkeHub`.

#### `CreateFeature`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.CreateFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.features.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.CreateFeature" `  




#### `CreateFleet`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.CreateFleet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.fleet.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.CreateFleet" `  




#### `CreateMembership`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.CreateMembership`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.memberships.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.CreateMembership" `  




#### `CreateMembershipBinding`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.CreateMembershipBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.membershipbindings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.CreateMembershipBinding" `  




#### `CreateMembershipRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.CreateMembershipRBACRoleBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.CreateMembershipRBACRoleBinding" `  




#### `CreateScope`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.CreateScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.scopes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.CreateScope" `  




#### `CreateScopeNamespace`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.CreateScopeNamespace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.namespaces.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.CreateScopeNamespace" `  




#### `CreateScopeRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.CreateScopeRBACRoleBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.CreateScopeRBACRoleBinding" `  




#### `DeleteFeature`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.DeleteFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.features.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.DeleteFeature" `  




#### `DeleteFleet`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.DeleteFleet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.fleet.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.DeleteFleet" `  




#### `DeleteMembership`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.DeleteMembership`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.memberships.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.DeleteMembership" `  




#### `DeleteMembershipBinding`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.DeleteMembershipBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.membershipbindings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.DeleteMembershipBinding" `  




#### `DeleteMembershipRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.DeleteMembershipRBACRoleBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.DeleteMembershipRBACRoleBinding" `  




#### `DeleteScope`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.DeleteScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.scopes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.DeleteScope" `  




#### `DeleteScopeNamespace`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.DeleteScopeNamespace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.namespaces.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.DeleteScopeNamespace" `  




#### `DeleteScopeRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.DeleteScopeRBACRoleBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.DeleteScopeRBACRoleBinding" `  




#### `GenerateConnectManifest`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.GenerateConnectManifest`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.memberships.generateConnectManifest - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.GenerateConnectManifest" `  




#### `GenerateMembershipRBACRoleBindingYAML`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.GenerateMembershipRBACRoleBindingYAML`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.GenerateMembershipRBACRoleBindingYAML" `  




#### `GetFeature`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.GetFeature`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.features.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.GetFeature" `  




#### `GetFleet`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.GetFleet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.fleet.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.GetFleet" `  




#### `GetMembership`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.GetMembership`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.memberships.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.GetMembership" `  




#### `GetMembershipBinding`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.GetMembershipBinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.membershipbindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.GetMembershipBinding" `  




#### `GetMembershipRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.GetMembershipRBACRoleBinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.GetMembershipRBACRoleBinding" `  




#### `GetScope`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.GetScope`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.scopes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.GetScope" `  




#### `GetScopeNamespace`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.GetScopeNamespace`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.GetScopeNamespace" `  




#### `GetScopeRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.GetScopeRBACRoleBinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.GetScopeRBACRoleBinding" `  




#### `ListBoundMemberships`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.ListBoundMemberships`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.scopes.listBoundMemberships - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.ListBoundMemberships" `  




#### `ListFeatures`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.ListFeatures`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.features.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.ListFeatures" `  




#### `ListMembershipBindings`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.ListMembershipBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.membershipbindings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.ListMembershipBindings" `  




#### `ListMembershipRBACRoleBindings`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.ListMembershipRBACRoleBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.ListMembershipRBACRoleBindings" `  




#### `ListMemberships`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.ListMemberships`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.memberships.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.ListMemberships" `  




#### `ListScopeNamespaces`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.ListScopeNamespaces`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.namespaces.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.ListScopeNamespaces" `  




#### `ListScopeRBACRoleBindings`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.ListScopeRBACRoleBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.ListScopeRBACRoleBindings" `  




#### `ListScopes`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.ListScopes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.scopes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.ListScopes" `  




#### `UpdateFeature`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.UpdateFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.features.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.UpdateFeature" `  




#### `UpdateFleet`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.UpdateFleet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.fleet.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.UpdateFleet" `  




#### `UpdateMembership`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.UpdateMembership`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.memberships.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.UpdateMembership" `  




#### `UpdateMembershipBinding`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.UpdateMembershipBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.membershipbindings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.UpdateMembershipBinding" `  




#### `UpdateMembershipRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.UpdateMembershipRBACRoleBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.UpdateMembershipRBACRoleBinding" `  




#### `UpdateScope`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.UpdateScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.scopes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.UpdateScope" `  




#### `UpdateScopeNamespace`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.UpdateScopeNamespace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.namespaces.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.UpdateScopeNamespace" `  




#### `UpdateScopeRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1.GkeHub.UpdateScopeRBACRoleBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1.GkeHub.UpdateScopeRBACRoleBinding" `  




### `google.cloud.gkehub.v1alpha.GkeHub`

The following audit logs are associated with methods belonging to `google.cloud.gkehub.v1alpha.GkeHub`.

#### `CreateFeature`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.CreateFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.features.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.CreateFeature" `  




#### `CreateFleet`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.CreateFleet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.fleet.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.CreateFleet" `  




#### `CreateMembership`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.CreateMembership`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.memberships.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.CreateMembership" `  




#### `CreateMembershipBinding`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.CreateMembershipBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.membershipbindings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.CreateMembershipBinding" `  




#### `CreateMembershipRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.CreateMembershipRBACRoleBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.CreateMembershipRBACRoleBinding" `  




#### `CreateScope`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.CreateScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.scopes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.CreateScope" `  




#### `CreateScopeNamespace`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.CreateScopeNamespace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.namespaces.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.CreateScopeNamespace" `  




#### `CreateScopeRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.CreateScopeRBACRoleBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.CreateScopeRBACRoleBinding" `  




#### `DeleteFeature`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.DeleteFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.features.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.DeleteFeature" `  




#### `DeleteFleet`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.DeleteFleet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.fleet.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.DeleteFleet" `  




#### `DeleteMembership`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.DeleteMembership`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.memberships.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.DeleteMembership" `  




#### `DeleteMembershipBinding`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.DeleteMembershipBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.membershipbindings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.DeleteMembershipBinding" `  




#### `DeleteMembershipRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.DeleteMembershipRBACRoleBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.DeleteMembershipRBACRoleBinding" `  




#### `DeleteScope`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.DeleteScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.scopes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.DeleteScope" `  




#### `DeleteScopeNamespace`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.DeleteScopeNamespace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.namespaces.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.DeleteScopeNamespace" `  




#### `DeleteScopeRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.DeleteScopeRBACRoleBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.DeleteScopeRBACRoleBinding" `  




#### `GenerateConnectManifest`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.GenerateConnectManifest`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.memberships.generateConnectManifest - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.GenerateConnectManifest" `  




#### `GenerateExclusivityManifest`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.GenerateExclusivityManifest`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.memberships.generateConnectManifest - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.GenerateExclusivityManifest" `  




#### `GenerateMembershipRBACRoleBindingYAML`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.GenerateMembershipRBACRoleBindingYAML`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.GenerateMembershipRBACRoleBindingYAML" `  




#### `GetFeature`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.GetFeature`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.features.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.GetFeature" `  




#### `GetFleet`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.GetFleet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.fleet.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.GetFleet" `  




#### `GetMembership`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.GetMembership`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.memberships.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.GetMembership" `  




#### `GetMembershipBinding`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.GetMembershipBinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.membershipbindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.GetMembershipBinding" `  




#### `GetMembershipRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.GetMembershipRBACRoleBinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.GetMembershipRBACRoleBinding" `  




#### `GetScope`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.GetScope`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.scopes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.GetScope" `  




#### `GetScopeNamespace`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.GetScopeNamespace`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.GetScopeNamespace" `  




#### `GetScopeRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.GetScopeRBACRoleBinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.GetScopeRBACRoleBinding" `  




#### `ListAdminClusterMemberships`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.ListAdminClusterMemberships`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.memberships.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.ListAdminClusterMemberships" `  




#### `ListBoundMemberships`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.ListBoundMemberships`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.scopes.listBoundMemberships - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.ListBoundMemberships" `  




#### `ListFeatures`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.ListFeatures`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.features.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.ListFeatures" `  




#### `ListMembershipBindings`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.ListMembershipBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.membershipbindings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.ListMembershipBindings" `  




#### `ListMembershipRBACRoleBindings`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.ListMembershipRBACRoleBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.ListMembershipRBACRoleBindings" `  




#### `ListMemberships`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.ListMemberships`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.memberships.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.ListMemberships" `  




#### `ListScopeNamespaces`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.ListScopeNamespaces`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.namespaces.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.ListScopeNamespaces" `  




#### `ListScopeRBACRoleBindings`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.ListScopeRBACRoleBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.ListScopeRBACRoleBindings" `  




#### `ListScopes`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.ListScopes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.scopes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.ListScopes" `  




#### `UpdateFeature`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.UpdateFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.features.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.UpdateFeature" `  




#### `UpdateFleet`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.UpdateFleet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.fleet.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.UpdateFleet" `  




#### `UpdateMembership`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.UpdateMembership`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.memberships.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.UpdateMembership" `  




#### `UpdateMembershipBinding`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.UpdateMembershipBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.membershipbindings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.UpdateMembershipBinding" `  




#### `UpdateMembershipRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.UpdateMembershipRBACRoleBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.UpdateMembershipRBACRoleBinding" `  




#### `UpdateScope`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.UpdateScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.scopes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.UpdateScope" `  




#### `UpdateScopeNamespace`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.UpdateScopeNamespace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.namespaces.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.UpdateScopeNamespace" `  




#### `UpdateScopeRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.UpdateScopeRBACRoleBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.UpdateScopeRBACRoleBinding" `  




#### `ValidateCreateMembership`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.ValidateCreateMembership`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.memberships.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.ValidateCreateMembership" `  




#### `ValidateExclusivity`

  * **Method** : `google.cloud.gkehub.v1alpha.GkeHub.ValidateExclusivity`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.memberships.generateConnectManifest - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha.GkeHub.ValidateExclusivity" `  




### `google.cloud.gkehub.v1alpha1.GkeHubDomainFeatureService`

The following audit logs are associated with methods belonging to `google.cloud.gkehub.v1alpha1.GkeHubDomainFeatureService`.

#### `CreateFeature`

  * **Method** : `google.cloud.gkehub.v1alpha1.GkeHubDomainFeatureService.CreateFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.features.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha1.GkeHubDomainFeatureService.CreateFeature" `  




#### `DeleteFeature`

  * **Method** : `google.cloud.gkehub.v1alpha1.GkeHubDomainFeatureService.DeleteFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.features.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha1.GkeHubDomainFeatureService.DeleteFeature" `  




#### `GetFeature`

  * **Method** : `google.cloud.gkehub.v1alpha1.GkeHubDomainFeatureService.GetFeature`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.features.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha1.GkeHubDomainFeatureService.GetFeature" `  




#### `ListFeatures`

  * **Method** : `google.cloud.gkehub.v1alpha1.GkeHubDomainFeatureService.ListFeatures`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.features.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha1.GkeHubDomainFeatureService.ListFeatures" `  




#### `UpdateFeature`

  * **Method** : `google.cloud.gkehub.v1alpha1.GkeHubDomainFeatureService.UpdateFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.features.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1alpha1.GkeHubDomainFeatureService.UpdateFeature" `  




### `google.cloud.gkehub.v1beta.GkeHub`

The following audit logs are associated with methods belonging to `google.cloud.gkehub.v1beta.GkeHub`.

#### `CreateFeature`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.CreateFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.features.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.CreateFeature" `  




#### `CreateFleet`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.CreateFleet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.fleet.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.CreateFleet" `  




#### `CreateMembership`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.CreateMembership`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.memberships.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.CreateMembership" `  




#### `CreateMembershipBinding`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.CreateMembershipBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.membershipbindings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.CreateMembershipBinding" `  




#### `CreateMembershipRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.CreateMembershipRBACRoleBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.CreateMembershipRBACRoleBinding" `  




#### `CreateScope`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.CreateScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.scopes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.CreateScope" `  




#### `CreateScopeNamespace`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.CreateScopeNamespace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.namespaces.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.CreateScopeNamespace" `  




#### `CreateScopeRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.CreateScopeRBACRoleBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.CreateScopeRBACRoleBinding" `  




#### `DeleteFeature`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.DeleteFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.features.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.DeleteFeature" `  




#### `DeleteFleet`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.DeleteFleet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.fleet.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.DeleteFleet" `  




#### `DeleteMembership`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.DeleteMembership`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.memberships.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.DeleteMembership" `  




#### `DeleteMembershipBinding`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.DeleteMembershipBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.membershipbindings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.DeleteMembershipBinding" `  




#### `DeleteMembershipRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.DeleteMembershipRBACRoleBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.DeleteMembershipRBACRoleBinding" `  




#### `DeleteScope`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.DeleteScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.scopes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.DeleteScope" `  




#### `DeleteScopeNamespace`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.DeleteScopeNamespace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.namespaces.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.DeleteScopeNamespace" `  




#### `DeleteScopeRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.DeleteScopeRBACRoleBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.DeleteScopeRBACRoleBinding" `  




#### `GenerateConnectManifest`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.GenerateConnectManifest`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.memberships.generateConnectManifest - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.GenerateConnectManifest" `  




#### `GenerateMembershipRBACRoleBindingYAML`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.GenerateMembershipRBACRoleBindingYAML`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.GenerateMembershipRBACRoleBindingYAML" `  




#### `GetFeature`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.GetFeature`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.features.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.GetFeature" `  




#### `GetFleet`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.GetFleet`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.fleet.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.GetFleet" `  




#### `GetMembership`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.GetMembership`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.memberships.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.GetMembership" `  




#### `GetMembershipBinding`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.GetMembershipBinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.membershipbindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.GetMembershipBinding" `  




#### `GetMembershipRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.GetMembershipRBACRoleBinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.GetMembershipRBACRoleBinding" `  




#### `GetScope`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.GetScope`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.scopes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.GetScope" `  




#### `GetScopeNamespace`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.GetScopeNamespace`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.namespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.GetScopeNamespace" `  




#### `GetScopeRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.GetScopeRBACRoleBinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.GetScopeRBACRoleBinding" `  




#### `ListBoundMemberships`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.ListBoundMemberships`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.scopes.listBoundMemberships - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.ListBoundMemberships" `  




#### `ListFeatures`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.ListFeatures`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.features.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.ListFeatures" `  




#### `ListMembershipBindings`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.ListMembershipBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.membershipbindings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.ListMembershipBindings" `  




#### `ListMembershipRBACRoleBindings`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.ListMembershipRBACRoleBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.ListMembershipRBACRoleBindings" `  




#### `ListMemberships`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.ListMemberships`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.memberships.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.ListMemberships" `  




#### `ListScopeNamespaces`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.ListScopeNamespaces`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.namespaces.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.ListScopeNamespaces" `  




#### `ListScopeRBACRoleBindings`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.ListScopeRBACRoleBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.ListScopeRBACRoleBindings" `  




#### `ListScopes`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.ListScopes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.scopes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.ListScopes" `  




#### `UpdateFeature`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.UpdateFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.features.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.UpdateFeature" `  




#### `UpdateFleet`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.UpdateFleet`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.fleet.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.UpdateFleet" `  




#### `UpdateMembership`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.UpdateMembership`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.memberships.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.UpdateMembership" `  




#### `UpdateMembershipBinding`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.UpdateMembershipBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.membershipbindings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.UpdateMembershipBinding" `  




#### `UpdateMembershipRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.UpdateMembershipRBACRoleBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.UpdateMembershipRBACRoleBinding" `  




#### `UpdateScope`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.UpdateScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.scopes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.UpdateScope" `  




#### `UpdateScopeNamespace`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.UpdateScopeNamespace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.namespaces.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.UpdateScopeNamespace" `  




#### `UpdateScopeRBACRoleBinding`

  * **Method** : `google.cloud.gkehub.v1beta.GkeHub.UpdateScopeRBACRoleBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.rbacrolebindings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta.GkeHub.UpdateScopeRBACRoleBinding" `  




### `google.cloud.gkehub.v1beta1.GkeHubMembershipService`

The following audit logs are associated with methods belonging to `google.cloud.gkehub.v1beta1.GkeHubMembershipService`.

#### `CreateMembership`

  * **Method** : `google.cloud.gkehub.v1beta1.GkeHubMembershipService.CreateMembership`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.memberships.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta1.GkeHubMembershipService.CreateMembership" `  




#### `DeleteMembership`

  * **Method** : `google.cloud.gkehub.v1beta1.GkeHubMembershipService.DeleteMembership`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.memberships.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta1.GkeHubMembershipService.DeleteMembership" `  




#### `GenerateConnectManifest`

  * **Method** : `google.cloud.gkehub.v1beta1.GkeHubMembershipService.GenerateConnectManifest`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.memberships.generateConnectManifest - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta1.GkeHubMembershipService.GenerateConnectManifest" `  




#### `GenerateExclusivityManifest`

  * **Method** : `google.cloud.gkehub.v1beta1.GkeHubMembershipService.GenerateExclusivityManifest`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.memberships.generateConnectManifest - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta1.GkeHubMembershipService.GenerateExclusivityManifest" `  




#### `GetMembership`

  * **Method** : `google.cloud.gkehub.v1beta1.GkeHubMembershipService.GetMembership`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.memberships.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta1.GkeHubMembershipService.GetMembership" `  




#### `ListMemberships`

  * **Method** : `google.cloud.gkehub.v1beta1.GkeHubMembershipService.ListMemberships`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.memberships.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta1.GkeHubMembershipService.ListMemberships" `  




#### `UpdateMembership`

  * **Method** : `google.cloud.gkehub.v1beta1.GkeHubMembershipService.UpdateMembership`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.memberships.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta1.GkeHubMembershipService.UpdateMembership" `  




#### `ValidateExclusivity`

  * **Method** : `google.cloud.gkehub.v1beta1.GkeHubMembershipService.ValidateExclusivity`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.memberships.generateConnectManifest - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v1beta1.GkeHubMembershipService.ValidateExclusivity" `  




### `google.cloud.gkehub.v2.GkeHubFeature`

The following audit logs are associated with methods belonging to `google.cloud.gkehub.v2.GkeHubFeature`.

#### `CreateMembershipFeature`

  * **Method** : `google.cloud.gkehub.v2.GkeHubFeature.CreateMembershipFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.membershipfeatures.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v2.GkeHubFeature.CreateMembershipFeature" `  




#### `DeleteMembershipFeature`

  * **Method** : `google.cloud.gkehub.v2.GkeHubFeature.DeleteMembershipFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.membershipfeatures.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v2.GkeHubFeature.DeleteMembershipFeature" `  




#### `GetMembershipFeature`

  * **Method** : `google.cloud.gkehub.v2.GkeHubFeature.GetMembershipFeature`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.membershipfeatures.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v2.GkeHubFeature.GetMembershipFeature" `  




#### `ListMembershipFeatures`

  * **Method** : `google.cloud.gkehub.v2.GkeHubFeature.ListMembershipFeatures`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.membershipfeatures.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v2.GkeHubFeature.ListMembershipFeatures" `  




#### `UpdateMembershipFeature`

  * **Method** : `google.cloud.gkehub.v2.GkeHubFeature.UpdateMembershipFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.membershipfeatures.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v2.GkeHubFeature.UpdateMembershipFeature" `  




### `google.cloud.gkehub.v2alpha.GkeHubFeature`

The following audit logs are associated with methods belonging to `google.cloud.gkehub.v2alpha.GkeHubFeature`.

#### `CreateMembershipFeature`

  * **Method** : `google.cloud.gkehub.v2alpha.GkeHubFeature.CreateMembershipFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.membershipfeatures.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v2alpha.GkeHubFeature.CreateMembershipFeature" `  




#### `DeleteMembershipFeature`

  * **Method** : `google.cloud.gkehub.v2alpha.GkeHubFeature.DeleteMembershipFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.membershipfeatures.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v2alpha.GkeHubFeature.DeleteMembershipFeature" `  




#### `GetMembershipFeature`

  * **Method** : `google.cloud.gkehub.v2alpha.GkeHubFeature.GetMembershipFeature`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.membershipfeatures.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v2alpha.GkeHubFeature.GetMembershipFeature" `  




#### `ListMembershipFeatures`

  * **Method** : `google.cloud.gkehub.v2alpha.GkeHubFeature.ListMembershipFeatures`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.membershipfeatures.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v2alpha.GkeHubFeature.ListMembershipFeatures" `  




#### `UpdateMembershipFeature`

  * **Method** : `google.cloud.gkehub.v2alpha.GkeHubFeature.UpdateMembershipFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.membershipfeatures.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v2alpha.GkeHubFeature.UpdateMembershipFeature" `  




### `google.cloud.gkehub.v2beta.GkeHubFeature`

The following audit logs are associated with methods belonging to `google.cloud.gkehub.v2beta.GkeHubFeature`.

#### `CreateMembershipFeature`

  * **Method** : `google.cloud.gkehub.v2beta.GkeHubFeature.CreateMembershipFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.membershipfeatures.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v2beta.GkeHubFeature.CreateMembershipFeature" `  




#### `DeleteMembershipFeature`

  * **Method** : `google.cloud.gkehub.v2beta.GkeHubFeature.DeleteMembershipFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.membershipfeatures.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v2beta.GkeHubFeature.DeleteMembershipFeature" `  




#### `GetMembershipFeature`

  * **Method** : `google.cloud.gkehub.v2beta.GkeHubFeature.GetMembershipFeature`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.membershipfeatures.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v2beta.GkeHubFeature.GetMembershipFeature" `  




#### `ListMembershipFeatures`

  * **Method** : `google.cloud.gkehub.v2beta.GkeHubFeature.ListMembershipFeatures`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.membershipfeatures.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v2beta.GkeHubFeature.ListMembershipFeatures" `  




#### `UpdateMembershipFeature`

  * **Method** : `google.cloud.gkehub.v2beta.GkeHubFeature.UpdateMembershipFeature`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.membershipfeatures.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.gkehub.v2beta.GkeHubFeature.UpdateMembershipFeature" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `gkehub.features.getIamPolicy - ADMIN_READ`
    * `gkehub.memberships.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.features.setIamPolicy - ADMIN_WRITE`
    * `gkehub.memberships.setIamPolicy - ADMIN_WRITE`
    * `gkehub.scopes.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `gkehub.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




## Kubernetes audit logging

In addition to Cloud Audit Logs, [Kubernetes audit logging](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/) provides a way for administrators to retain, query, process, and alert on events that occur in registered clusters. Administrators can use the logged information to do forensic analysis and real-time alerting, or for cataloging how a fleet of clusters are being used and by whom.

The Connect Agent talks to the local API server running in the registered cluster, and each cluster will have its own set of Kubernetes audit logs. All actions that users perform from the UI through Connect are logged by that cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
