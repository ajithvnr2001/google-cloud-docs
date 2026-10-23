---
url: https://docs.cloud.google.com/iam/docs/audit-logging/
title: Identity and Access Management audit logging \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:39.499719+00:00
---

# Identity and Access Management audit logging  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Identity and Access Management audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Identity and Access Management. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Notes

You can also view examples of [audit log entries for service accounts](https://docs.cloud.google.com/iam/docs/audit-logging/examples-service-accounts).

## Service name

To view the Identity and Access Management audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="iam.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Identity and Access Management generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.iam.admin.v1.GetIAMPolicy`  
`google.iam.admin.v1.GetRole`  
`google.iam.admin.v1.GetServiceAccount`  
`google.iam.admin.v1.GetServiceAccountKey`  
`google.iam.admin.v1.ListRoles`  
`google.iam.admin.v1.ListServiceAccountKeys`  
`google.iam.admin.v1.ListServiceAccounts`  
`google.iam.admin.v1.TestIAMPermissions`  
`google.iam.admin.v1.OauthClients.GetOauthClient`  
`google.iam.admin.v1.OauthClients.GetOauthClientCredential`  
`google.iam.admin.v1.OauthClients.ListOauthClientCredentials`  
`google.iam.admin.v1.OauthClients.ListOauthClients`  
`google.iam.admin.v1.WorkforcePools.GetIamPolicy`  
`google.iam.admin.v1.WorkforcePools.GetWorkforcePool`  
`google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProvider`  
`google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProviderKey`  
`google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProviderScimTenant`  
`google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProviderScimToken`  
`google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviderKeys`  
`google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviderScimTenants`  
`google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviderScimTokens`  
`google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviders`  
`google.iam.admin.v1.WorkforcePools.ListWorkforcePools`  
`google.iam.v1.WorkloadIdentityPools.GetIamPolicy`  
`google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPool`  
`google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPoolManagedIdentity`  
`google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPoolNamespace`  
`google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPoolProvider`  
`google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPoolProviderKey`  
`google.iam.v1.WorkloadIdentityPools.ListAttestationRules`  
`google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPoolManagedIdentities`  
`google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPoolNamespaces`  
`google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPoolProviderKeys`  
`google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPoolProviders`  
`google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPools`  
`google.iam.v1beta.WorkloadIdentityPools.GetWorkloadIdentityPool`  
`google.iam.v1beta.WorkloadIdentityPools.GetWorkloadIdentityPoolProvider`  
`google.iam.v1beta.WorkloadIdentityPools.ListWorkloadIdentityPoolProviders`  
`google.iam.v1beta.WorkloadIdentityPools.ListWorkloadIdentityPools`  
`google.iam.v2.Policies.GetPolicy`  
`google.iam.v2.Policies.ListPolicies`  
`google.iam.v2alpha.Policies.GetPolicy`  
`google.iam.v2alpha.Policies.ListPolicies`  
`google.iam.v2beta.Policies.GetPolicy`  
`google.iam.v2beta.Policies.ListPolicies`  
`google.iam.v3.PolicyBindings.GetPolicyBinding`  
`google.iam.v3.PolicyBindings.ListPolicyBindings`  
`google.iam.v3.PolicyBindings.SearchTargetPolicyBindings`  
`google.iam.v3.PrincipalAccessBoundaryPolicies.GetPrincipalAccessBoundaryPolicy`  
`google.iam.v3.PrincipalAccessBoundaryPolicies.ListPrincipalAccessBoundaryPolicies`  
`google.iam.v3.PrincipalAccessBoundaryPolicies.SearchPrincipalAccessBoundaryPolicyBindings`  
`google.iam.v3beta.AccessPolicies.GetAccessPolicy`  
`google.iam.v3beta.AccessPolicies.ListAccessPolicies`  
`google.iam.v3beta.AccessPolicies.SearchAccessPolicyBindings`  
`google.iam.v3beta.PolicyBindings.GetPolicyBinding`  
`google.iam.v3beta.PolicyBindings.ListPolicyBindings`  
`google.iam.v3beta.PolicyBindings.SearchTargetPolicyBindings`  
`google.iam.v3beta.PrincipalAccessBoundaryPolicies.GetPrincipalAccessBoundaryPolicy`  
`google.iam.v3beta.PrincipalAccessBoundaryPolicies.ListPrincipalAccessBoundaryPolicies`  
`google.iam.v3beta.PrincipalAccessBoundaryPolicies.SearchPrincipalAccessBoundaryPolicyBindings`  
`google.longrunning.Operations.GetOperation`  
`ADMIN_WRITE` | `google.iam.admin.v1.CreateRole`  
`google.iam.admin.v1.CreateServiceAccount`  
`google.iam.admin.v1.CreateServiceAccountKey`  
`google.iam.admin.v1.DeleteRole`  
`google.iam.admin.v1.DeleteServiceAccount`  
`google.iam.admin.v1.DeleteServiceAccountKey`  
`google.iam.admin.v1.DisableServiceAccount`  
`google.iam.admin.v1.DisableServiceAccountKey`  
`google.iam.admin.v1.EnableServiceAccount`  
`google.iam.admin.v1.EnableServiceAccountKey`  
`google.iam.admin.v1.PatchServiceAccount`  
`google.iam.admin.v1.SetIAMPolicy`  
`google.iam.admin.v1.UndeleteRole`  
`google.iam.admin.v1.UndeleteServiceAccount`  
`google.iam.admin.v1.UpdateRole`  
`google.iam.admin.v1.UpdateServiceAccount`  
`google.iam.admin.v1.UploadServiceAccountKey`  
`google.iam.admin.v1.OauthClients.CreateOauthClient`  
`google.iam.admin.v1.OauthClients.CreateOauthClientCredential`  
`google.iam.admin.v1.OauthClients.DeleteOauthClient`  
`google.iam.admin.v1.OauthClients.DeleteOauthClientCredential`  
`google.iam.admin.v1.OauthClients.UndeleteOauthClient`  
`google.iam.admin.v1.OauthClients.UpdateOauthClient`  
`google.iam.admin.v1.OauthClients.UpdateOauthClientCredential`  
`google.iam.admin.v1.WorkforcePools.CreateWorkforcePool` (LRO)  
`google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProvider` (LRO)  
`google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProviderKey` (LRO)  
`google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProviderScimTenant`  
`google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProviderScimToken`  
`google.iam.admin.v1.WorkforcePools.DeleteWorkforcePool` (LRO)  
`google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProvider` (LRO)  
`google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProviderKey` (LRO)  
`google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProviderScimTenant`  
`google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProviderScimToken`  
`google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolSubject` (LRO)  
`google.iam.admin.v1.WorkforcePools.SetIamPolicy`  
`google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePool` (LRO)  
`google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolProvider` (LRO)  
`google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolProviderKey` (LRO)  
`google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolProviderScimTenant`  
`google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolSubject` (LRO)  
`google.iam.admin.v1.WorkforcePools.UpdateWorkforcePool` (LRO)  
`google.iam.admin.v1.WorkforcePools.UpdateWorkforcePoolProvider` (LRO)  
`google.iam.admin.v1.WorkforcePools.UpdateWorkforcePoolProviderScimTenant`  
`google.iam.admin.v1.WorkforcePools.UpdateWorkforcePoolProviderScimToken`  
`google.iam.v1.WorkloadIdentityPools.AddAttestationRule` (LRO)  
`google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPool` (LRO)  
`google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPoolManagedIdentity` (LRO)  
`google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPoolNamespace` (LRO)  
`google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPoolProvider` (LRO)  
`google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPoolProviderKey` (LRO)  
`google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPool` (LRO)  
`google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPoolManagedIdentity` (LRO)  
`google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPoolNamespace` (LRO)  
`google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPoolProvider` (LRO)  
`google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPoolProviderKey` (LRO)  
`google.iam.v1.WorkloadIdentityPools.RemoveAttestationRule` (LRO)  
`google.iam.v1.WorkloadIdentityPools.SetAttestationRules` (LRO)  
`google.iam.v1.WorkloadIdentityPools.SetIamPolicy`  
`google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPool` (LRO)  
`google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolManagedIdentity` (LRO)  
`google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolNamespace` (LRO)  
`google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolProvider` (LRO)  
`google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolProviderKey` (LRO)  
`google.iam.v1.WorkloadIdentityPools.UpdateWorkloadIdentityPool` (LRO)  
`google.iam.v1.WorkloadIdentityPools.UpdateWorkloadIdentityPoolManagedIdentity` (LRO)  
`google.iam.v1.WorkloadIdentityPools.UpdateWorkloadIdentityPoolNamespace` (LRO)  
`google.iam.v1.WorkloadIdentityPools.UpdateWorkloadIdentityPoolProvider` (LRO)  
`google.iam.v1beta.WorkloadIdentityPools.CreateWorkloadIdentityPool` (LRO)  
`google.iam.v1beta.WorkloadIdentityPools.CreateWorkloadIdentityPoolProvider` (LRO)  
`google.iam.v1beta.WorkloadIdentityPools.DeleteWorkloadIdentityPool` (LRO)  
`google.iam.v1beta.WorkloadIdentityPools.DeleteWorkloadIdentityPoolProvider` (LRO)  
`google.iam.v1beta.WorkloadIdentityPools.UndeleteWorkloadIdentityPool` (LRO)  
`google.iam.v1beta.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolProvider` (LRO)  
`google.iam.v1beta.WorkloadIdentityPools.UpdateWorkloadIdentityPool` (LRO)  
`google.iam.v1beta.WorkloadIdentityPools.UpdateWorkloadIdentityPoolProvider` (LRO)  
`google.iam.v2.Policies.CreatePolicy` (LRO)  
`google.iam.v2.Policies.DeletePolicy` (LRO)  
`google.iam.v2.Policies.UpdatePolicy` (LRO)  
`google.iam.v2alpha.Policies.CreatePolicy` (LRO)  
`google.iam.v2alpha.Policies.DeletePolicy` (LRO)  
`google.iam.v2alpha.Policies.UpdatePolicy` (LRO)  
`google.iam.v2beta.Policies.CreatePolicy` (LRO)  
`google.iam.v2beta.Policies.DeletePolicy` (LRO)  
`google.iam.v2beta.Policies.UpdatePolicy` (LRO)  
`google.iam.v3.PolicyBindings.CreatePolicyBinding` (LRO)  
`google.iam.v3.PolicyBindings.DeletePolicyBinding` (LRO)  
`google.iam.v3.PolicyBindings.UpdatePolicyBinding` (LRO)  
`google.iam.v3.PrincipalAccessBoundaryPolicies.CreatePrincipalAccessBoundaryPolicy` (LRO)  
`google.iam.v3.PrincipalAccessBoundaryPolicies.DeletePrincipalAccessBoundaryPolicy` (LRO)  
`google.iam.v3.PrincipalAccessBoundaryPolicies.UpdatePrincipalAccessBoundaryPolicy` (LRO)  
`google.iam.v3beta.AccessPolicies.CreateAccessPolicy` (LRO)  
`google.iam.v3beta.AccessPolicies.DeleteAccessPolicy` (LRO)  
`google.iam.v3beta.AccessPolicies.UpdateAccessPolicy` (LRO)  
`google.iam.v3beta.PolicyBindings.CreatePolicyBinding` (LRO)  
`google.iam.v3beta.PolicyBindings.DeletePolicyBinding` (LRO)  
`google.iam.v3beta.PolicyBindings.UpdatePolicyBinding` (LRO)  
`google.iam.v3beta.PrincipalAccessBoundaryPolicies.CreatePrincipalAccessBoundaryPolicy` (LRO)  
`google.iam.v3beta.PrincipalAccessBoundaryPolicies.DeletePrincipalAccessBoundaryPolicy` (LRO)  
`google.iam.v3beta.PrincipalAccessBoundaryPolicies.UpdatePrincipalAccessBoundaryPolicy` (LRO)  
`OTHER` | `google.iam.admin.v1.QueryGrantableRoles`: To enable this log, enable `ADMIN_READ` under the service `cloudresourcemanager.googleapis.com`.  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Identity and Access Management.

### `google.iam.admin.v1.IAM`

The following audit logs are associated with methods belonging to `google.iam.admin.v1.IAM`.

#### `CreateRole`

  * **Method** : `[google.iam.admin.v1.CreateRole](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.CreateRole)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.roles.create - ADMIN_WRITE`
    * `iam.roles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.CreateRole" `  




#### `CreateServiceAccount`

  * **Method** : `[google.iam.admin.v1.CreateServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.CreateServiceAccount)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.serviceAccounts.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.CreateServiceAccount" `  




#### `CreateServiceAccountKey`

  * **Method** : `[google.iam.admin.v1.CreateServiceAccountKey](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.CreateServiceAccountKey)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.serviceAccountKeys.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.CreateServiceAccountKey" `  




#### `DeleteRole`

  * **Method** : `[google.iam.admin.v1.DeleteRole](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.DeleteRole)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.roles.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.DeleteRole" `  




#### `DeleteServiceAccount`

  * **Method** : `[google.iam.admin.v1.DeleteServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.DeleteServiceAccount)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.serviceAccounts.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.DeleteServiceAccount" `  




#### `DeleteServiceAccountKey`

  * **Method** : `[google.iam.admin.v1.DeleteServiceAccountKey](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.DeleteServiceAccountKey)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.serviceAccountKeys.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.DeleteServiceAccountKey" `  




#### `DisableServiceAccount`

  * **Method** : `[google.iam.admin.v1.DisableServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.DisableServiceAccount)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.serviceAccounts.disable - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.DisableServiceAccount" `  




#### `DisableServiceAccountKey`

  * **Method** : `[google.iam.admin.v1.DisableServiceAccountKey](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.DisableServiceAccountKey)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.serviceAccountKeys.disable - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.DisableServiceAccountKey" `  




#### `EnableServiceAccount`

  * **Method** : `[google.iam.admin.v1.EnableServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.EnableServiceAccount)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.serviceAccounts.enable - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.EnableServiceAccount" `  




#### `EnableServiceAccountKey`

  * **Method** : `[google.iam.admin.v1.EnableServiceAccountKey](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.EnableServiceAccountKey)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.serviceAccountKeys.enable - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.EnableServiceAccountKey" `  




#### `GetIAMPolicy`

  * **Method** : `[google.iam.admin.v1.GetIAMPolicy](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.GetIamPolicy)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.serviceAccounts.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.GetIAMPolicy" `  




#### `GetRole`

  * **Method** : `[google.iam.admin.v1.GetRole](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.GetRole)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.roles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.GetRole" `  




#### `GetServiceAccount`

  * **Method** : `[google.iam.admin.v1.GetServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.GetServiceAccount)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.serviceAccounts.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.GetServiceAccount" `  




#### `GetServiceAccountKey`

  * **Method** : `[google.iam.admin.v1.GetServiceAccountKey](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.GetServiceAccountKey)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.serviceAccountKeys.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.GetServiceAccountKey" `  




#### `ListRoles`

  * **Method** : `[google.iam.admin.v1.ListRoles](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.ListRoles)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.roles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.ListRoles" `  




#### `ListServiceAccountKeys`

  * **Method** : `[google.iam.admin.v1.ListServiceAccountKeys](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.ListServiceAccountKeys)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.serviceAccountKeys.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.ListServiceAccountKeys" `  




#### `ListServiceAccounts`

  * **Method** : `[google.iam.admin.v1.ListServiceAccounts](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.ListServiceAccounts)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.serviceAccounts.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.ListServiceAccounts" `  




#### `PatchServiceAccount`

  * **Method** : `[google.iam.admin.v1.PatchServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.PatchServiceAccount)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.serviceAccounts.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.PatchServiceAccount" `  




#### `QueryGrantableRoles`

  * **Method** : `[google.iam.admin.v1.QueryGrantableRoles](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.QueryGrantableRoles)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `resourcemanager.projects.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.QueryGrantableRoles" `  


**Note:** This method can cause a **getIamPolicy** method to be called in other services' APIs. For example, if this method needs to check the allow policy for a Compute Engine instance, then the **[instances.getIamPolicy method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/getIamPolicy)** in the Compute Engine API is called. To receive audit logs for these additional services, you must enable `ADMIN_READ` audit logs for the other services' APIs.

#### `SetIAMPolicy`

  * **Method** : `[google.iam.admin.v1.SetIAMPolicy](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.SetIamPolicy)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.serviceAccounts.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.SetIAMPolicy" `  




#### `TestIAMPermissions`

  * **Method** : `[google.iam.admin.v1.TestIAMPermissions](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.TestIamPermissions)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.serviceAccounts.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.TestIAMPermissions" `  




#### `UndeleteRole`

  * **Method** : `[google.iam.admin.v1.UndeleteRole](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.UndeleteRole)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.roles.list - ADMIN_READ`
    * `iam.roles.undelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.UndeleteRole" `  




#### `UndeleteServiceAccount`

  * **Method** : `[google.iam.admin.v1.UndeleteServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.UndeleteServiceAccount)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.serviceAccounts.undelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.UndeleteServiceAccount" `  




#### `UpdateRole`

  * **Method** : `[google.iam.admin.v1.UpdateRole](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.UpdateRole)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.roles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.UpdateRole" `  




#### `UpdateServiceAccount`

  * **Method** : `[google.iam.admin.v1.UpdateServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.UpdateServiceAccount)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.serviceAccounts.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.UpdateServiceAccount" `  




#### `UploadServiceAccountKey`

  * **Method** : `[google.iam.admin.v1.UploadServiceAccountKey](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.IAM.UploadServiceAccountKey)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.serviceAccountKeys.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.UploadServiceAccountKey" `  




### `google.iam.admin.v1.OauthClients`

The following audit logs are associated with methods belonging to `google.iam.admin.v1.OauthClients`.

#### `CreateOauthClient`

  * **Method** : `[google.iam.admin.v1.OauthClients.CreateOauthClient](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.OauthClients.CreateOauthClient)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.oauthClients.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.OauthClients.CreateOauthClient" `  




#### `CreateOauthClientCredential`

  * **Method** : `[google.iam.admin.v1.OauthClients.CreateOauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.OauthClients.CreateOauthClientCredential)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.oauthClientCredentials.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.OauthClients.CreateOauthClientCredential" `  




#### `DeleteOauthClient`

  * **Method** : `[google.iam.admin.v1.OauthClients.DeleteOauthClient](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.OauthClients.DeleteOauthClient)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.oauthClients.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.OauthClients.DeleteOauthClient" `  




#### `DeleteOauthClientCredential`

  * **Method** : `[google.iam.admin.v1.OauthClients.DeleteOauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.OauthClients.DeleteOauthClientCredential)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.oauthClientCredentials.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.OauthClients.DeleteOauthClientCredential" `  




#### `GetOauthClient`

  * **Method** : `[google.iam.admin.v1.OauthClients.GetOauthClient](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.OauthClients.GetOauthClient)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.oauthClients.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.OauthClients.GetOauthClient" `  




#### `GetOauthClientCredential`

  * **Method** : `[google.iam.admin.v1.OauthClients.GetOauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.OauthClients.GetOauthClientCredential)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.oauthClientCredentials.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.OauthClients.GetOauthClientCredential" `  




#### `ListOauthClientCredentials`

  * **Method** : `[google.iam.admin.v1.OauthClients.ListOauthClientCredentials](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.OauthClients.ListOauthClientCredentials)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.oauthClientCredentials.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.OauthClients.ListOauthClientCredentials" `  




#### `ListOauthClients`

  * **Method** : `[google.iam.admin.v1.OauthClients.ListOauthClients](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.OauthClients.ListOauthClients)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.oauthClients.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.OauthClients.ListOauthClients" `  




#### `UndeleteOauthClient`

  * **Method** : `[google.iam.admin.v1.OauthClients.UndeleteOauthClient](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.OauthClients.UndeleteOauthClient)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.oauthClients.undelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.OauthClients.UndeleteOauthClient" `  




#### `UpdateOauthClient`

  * **Method** : `[google.iam.admin.v1.OauthClients.UpdateOauthClient](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.OauthClients.UpdateOauthClient)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.oauthClients.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.OauthClients.UpdateOauthClient" `  




#### `UpdateOauthClientCredential`

  * **Method** : `[google.iam.admin.v1.OauthClients.UpdateOauthClientCredential](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.OauthClients.UpdateOauthClientCredential)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.oauthClientCredentials.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.OauthClients.UpdateOauthClientCredential" `  




### `google.iam.admin.v1.WorkforcePools`

The following audit logs are associated with methods belonging to `google.iam.admin.v1.WorkforcePools`.

#### `CreateWorkforcePool`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.CreateWorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.CreateWorkforcePool)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePools.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.CreateWorkforcePool" `  




#### `CreateWorkforcePoolProvider`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProvider](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProvider)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePoolProviders.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProvider" `  




#### `CreateWorkforcePoolProviderKey`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProviderKey)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePoolProviderKeys.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProviderKey" `  




#### `CreateWorkforcePoolProviderScimTenant`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProviderScimTenant](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProviderScimTenant)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePoolProviderScimTenants.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProviderScimTenant" `  




#### `CreateWorkforcePoolProviderScimToken`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProviderScimToken](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProviderScimToken)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePoolProviderScimTokens.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProviderScimToken" `  




#### `DeleteWorkforcePool`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.DeleteWorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.DeleteWorkforcePool)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePools.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.DeleteWorkforcePool" `  




#### `DeleteWorkforcePoolProvider`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProvider](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProvider)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePoolProviders.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProvider" `  




#### `DeleteWorkforcePoolProviderKey`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProviderKey)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePoolProviderKeys.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProviderKey" `  




#### `DeleteWorkforcePoolProviderScimTenant`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProviderScimTenant](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProviderScimTenant)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePoolProviderScimTenants.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProviderScimTenant" `  




#### `DeleteWorkforcePoolProviderScimToken`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProviderScimToken](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProviderScimToken)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePoolProviderScimTokens.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProviderScimToken" `  




#### `DeleteWorkforcePoolSubject`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolSubject](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolSubject)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePoolSubjects.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolSubject" `  




#### `GetIamPolicy`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.GetIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.GetIamPolicy)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workforcePools.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.GetIamPolicy" `  




#### `GetWorkforcePool`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.GetWorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.GetWorkforcePool)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workforcePools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.GetWorkforcePool" `  




#### `GetWorkforcePoolProvider`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProvider](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProvider)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workforcePoolProviders.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProvider" `  




#### `GetWorkforcePoolProviderKey`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProviderKey)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workforcePoolProviderKeys.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProviderKey" `  




#### `GetWorkforcePoolProviderScimTenant`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProviderScimTenant](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProviderScimTenant)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workforcePoolProviderScimTenants.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProviderScimTenant" `  




#### `GetWorkforcePoolProviderScimToken`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProviderScimToken](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProviderScimToken)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workforcePoolProviderScimTokens.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProviderScimToken" `  




#### `ListWorkforcePoolProviderKeys`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviderKeys](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviderKeys)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workforcePoolProviderKeys.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviderKeys" `  




#### `ListWorkforcePoolProviderScimTenants`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviderScimTenants](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviderScimTenants)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workforcePoolProviderScimTenants.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviderScimTenants" `  




#### `ListWorkforcePoolProviderScimTokens`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviderScimTokens](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviderScimTokens)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workforcePoolProviderScimTokens.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviderScimTokens" `  




#### `ListWorkforcePoolProviders`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviders](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviders)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workforcePoolProviders.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviders" `  




#### `ListWorkforcePools`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.ListWorkforcePools](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.ListWorkforcePools)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workforcePools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.ListWorkforcePools" `  




#### `SetIamPolicy`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.SetIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.SetIamPolicy)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePools.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.SetIamPolicy" `  




#### `UndeleteWorkforcePool`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePool)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePools.undelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePool" `  




#### `UndeleteWorkforcePoolProvider`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolProvider](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolProvider)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePoolProviders.undelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolProvider" `  




#### `UndeleteWorkforcePoolProviderKey`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolProviderKey)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePoolProviderKeys.undelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolProviderKey" `  




#### `UndeleteWorkforcePoolProviderScimTenant`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolProviderScimTenant](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolProviderScimTenant)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePoolProviderScimTenants.undelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolProviderScimTenant" `  




#### `UndeleteWorkforcePoolSubject`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolSubject](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolSubject)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePoolSubjects.undelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolSubject" `  




#### `UpdateWorkforcePool`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.UpdateWorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.UpdateWorkforcePool)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePools.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.UpdateWorkforcePool" `  




#### `UpdateWorkforcePoolProvider`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.UpdateWorkforcePoolProvider](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.UpdateWorkforcePoolProvider)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePoolProviders.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.UpdateWorkforcePoolProvider" `  




#### `UpdateWorkforcePoolProviderScimTenant`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.UpdateWorkforcePoolProviderScimTenant](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.UpdateWorkforcePoolProviderScimTenant)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePoolProviderScimTenants.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.UpdateWorkforcePoolProviderScimTenant" `  




#### `UpdateWorkforcePoolProviderScimToken`

  * **Method** : `[google.iam.admin.v1.WorkforcePools.UpdateWorkforcePoolProviderScimToken](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#google.iam.admin.v1.WorkforcePools.UpdateWorkforcePoolProviderScimToken)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workforcePoolProviderScimTokens.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.admin.v1.WorkforcePools.UpdateWorkforcePoolProviderScimToken" `  




### `google.iam.v1.WorkloadIdentityPools`

The following audit logs are associated with methods belonging to `google.iam.v1.WorkloadIdentityPools`.

#### `AddAttestationRule`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.AddAttestationRule](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.AddAttestationRule)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolManagedIdentities.setAttestationRules - ADMIN_WRITE`
    * `iam.workloadIdentityPools.setAttestationRules - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.AddAttestationRule" `  




#### `CreateWorkloadIdentityPool`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPool)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPools.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPool" `  




#### `CreateWorkloadIdentityPoolManagedIdentity`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPoolManagedIdentity)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolManagedIdentities.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPoolManagedIdentity" `  




#### `CreateWorkloadIdentityPoolNamespace`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPoolNamespace)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolNamespaces.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPoolNamespace" `  




#### `CreateWorkloadIdentityPoolProvider`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPoolProvider)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolProviders.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPoolProvider" `  




#### `CreateWorkloadIdentityPoolProviderKey`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPoolProviderKey)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolProviderKeys.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.CreateWorkloadIdentityPoolProviderKey" `  




#### `DeleteWorkloadIdentityPool`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPool)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPools.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPool" `  




#### `DeleteWorkloadIdentityPoolManagedIdentity`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPoolManagedIdentity)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolManagedIdentities.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPoolManagedIdentity" `  




#### `DeleteWorkloadIdentityPoolNamespace`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPoolNamespace)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolNamespaces.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPoolNamespace" `  




#### `DeleteWorkloadIdentityPoolProvider`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPoolProvider)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolProviders.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPoolProvider" `  




#### `DeleteWorkloadIdentityPoolProviderKey`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPoolProviderKey)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolProviderKeys.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.DeleteWorkloadIdentityPoolProviderKey" `  




#### `GetIamPolicy`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.GetIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.GetIamPolicy)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workloadIdentityPools.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.GetIamPolicy" `  




#### `GetWorkloadIdentityPool`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPool)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workloadIdentityPools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPool" `  




#### `GetWorkloadIdentityPoolManagedIdentity`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPoolManagedIdentity)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolManagedIdentities.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPoolManagedIdentity" `  




#### `GetWorkloadIdentityPoolNamespace`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPoolNamespace)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolNamespaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPoolNamespace" `  




#### `GetWorkloadIdentityPoolProvider`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPoolProvider)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolProviders.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPoolProvider" `  




#### `GetWorkloadIdentityPoolProviderKey`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPoolProviderKey)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolProviderKeys.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.GetWorkloadIdentityPoolProviderKey" `  




#### `ListAttestationRules`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.ListAttestationRules](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.ListAttestationRules)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolManagedIdentities.getAttestationRules - ADMIN_READ`
    * `iam.workloadIdentityPools.getAttestationRules - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.ListAttestationRules" `  




#### `ListWorkloadIdentityPoolManagedIdentities`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPoolManagedIdentities](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPoolManagedIdentities)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolManagedIdentities.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPoolManagedIdentities" `  




#### `ListWorkloadIdentityPoolNamespaces`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPoolNamespaces](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPoolNamespaces)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolNamespaces.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPoolNamespaces" `  




#### `ListWorkloadIdentityPoolProviderKeys`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPoolProviderKeys](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPoolProviderKeys)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolProviderKeys.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPoolProviderKeys" `  




#### `ListWorkloadIdentityPoolProviders`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPoolProviders](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPoolProviders)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolProviders.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPoolProviders" `  




#### `ListWorkloadIdentityPools`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPools](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPools)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workloadIdentityPools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.ListWorkloadIdentityPools" `  




#### `RemoveAttestationRule`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.RemoveAttestationRule](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.RemoveAttestationRule)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolManagedIdentities.setAttestationRules - ADMIN_WRITE`
    * `iam.workloadIdentityPools.setAttestationRules - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.RemoveAttestationRule" `  




#### `SetAttestationRules`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.SetAttestationRules](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.SetAttestationRules)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolManagedIdentities.setAttestationRules - ADMIN_WRITE`
    * `iam.workloadIdentityPools.setAttestationRules - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.SetAttestationRules" `  




#### `SetIamPolicy`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.SetIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.SetIamPolicy)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPools.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.SetIamPolicy" `  




#### `UndeleteWorkloadIdentityPool`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPool)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPools.undelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPool" `  




#### `UndeleteWorkloadIdentityPoolManagedIdentity`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolManagedIdentity)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolManagedIdentities.undelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolManagedIdentity" `  




#### `UndeleteWorkloadIdentityPoolNamespace`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolNamespace)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolNamespaces.undelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolNamespace" `  




#### `UndeleteWorkloadIdentityPoolProvider`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolProvider)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolProviders.undelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolProvider" `  




#### `UndeleteWorkloadIdentityPoolProviderKey`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolProviderKey](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolProviderKey)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolProviderKeys.undelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolProviderKey" `  




#### `UpdateWorkloadIdentityPool`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.UpdateWorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.UpdateWorkloadIdentityPool)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPools.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.UpdateWorkloadIdentityPool" `  




#### `UpdateWorkloadIdentityPoolManagedIdentity`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.UpdateWorkloadIdentityPoolManagedIdentity](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.UpdateWorkloadIdentityPoolManagedIdentity)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolManagedIdentities.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.UpdateWorkloadIdentityPoolManagedIdentity" `  




#### `UpdateWorkloadIdentityPoolNamespace`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.UpdateWorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.UpdateWorkloadIdentityPoolNamespace)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolNamespaces.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.UpdateWorkloadIdentityPoolNamespace" `  




#### `UpdateWorkloadIdentityPoolProvider`

  * **Method** : `[google.iam.v1.WorkloadIdentityPools.UpdateWorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1#google.iam.v1.WorkloadIdentityPools.UpdateWorkloadIdentityPoolProvider)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolProviders.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.WorkloadIdentityPools.UpdateWorkloadIdentityPoolProvider" `  




### `google.iam.v1beta.WorkloadIdentityPools`

The following audit logs are associated with methods belonging to `google.iam.v1beta.WorkloadIdentityPools`.

#### `CreateWorkloadIdentityPool`

  * **Method** : `[google.iam.v1beta.WorkloadIdentityPools.CreateWorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1beta#google.iam.v1beta.WorkloadIdentityPools.CreateWorkloadIdentityPool)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPools.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1beta.WorkloadIdentityPools.CreateWorkloadIdentityPool" `  




#### `CreateWorkloadIdentityPoolProvider`

  * **Method** : `[google.iam.v1beta.WorkloadIdentityPools.CreateWorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1beta#google.iam.v1beta.WorkloadIdentityPools.CreateWorkloadIdentityPoolProvider)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolProviders.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1beta.WorkloadIdentityPools.CreateWorkloadIdentityPoolProvider" `  




#### `DeleteWorkloadIdentityPool`

  * **Method** : `[google.iam.v1beta.WorkloadIdentityPools.DeleteWorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1beta#google.iam.v1beta.WorkloadIdentityPools.DeleteWorkloadIdentityPool)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPools.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1beta.WorkloadIdentityPools.DeleteWorkloadIdentityPool" `  




#### `DeleteWorkloadIdentityPoolProvider`

  * **Method** : `[google.iam.v1beta.WorkloadIdentityPools.DeleteWorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1beta#google.iam.v1beta.WorkloadIdentityPools.DeleteWorkloadIdentityPoolProvider)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolProviders.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1beta.WorkloadIdentityPools.DeleteWorkloadIdentityPoolProvider" `  




#### `GetWorkloadIdentityPool`

  * **Method** : `[google.iam.v1beta.WorkloadIdentityPools.GetWorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1beta#google.iam.v1beta.WorkloadIdentityPools.GetWorkloadIdentityPool)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workloadIdentityPools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1beta.WorkloadIdentityPools.GetWorkloadIdentityPool" `  




#### `GetWorkloadIdentityPoolProvider`

  * **Method** : `[google.iam.v1beta.WorkloadIdentityPools.GetWorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1beta#google.iam.v1beta.WorkloadIdentityPools.GetWorkloadIdentityPoolProvider)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolProviders.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1beta.WorkloadIdentityPools.GetWorkloadIdentityPoolProvider" `  




#### `ListWorkloadIdentityPoolProviders`

  * **Method** : `[google.iam.v1beta.WorkloadIdentityPools.ListWorkloadIdentityPoolProviders](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1beta#google.iam.v1beta.WorkloadIdentityPools.ListWorkloadIdentityPoolProviders)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolProviders.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1beta.WorkloadIdentityPools.ListWorkloadIdentityPoolProviders" `  




#### `ListWorkloadIdentityPools`

  * **Method** : `[google.iam.v1beta.WorkloadIdentityPools.ListWorkloadIdentityPools](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1beta#google.iam.v1beta.WorkloadIdentityPools.ListWorkloadIdentityPools)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.workloadIdentityPools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1beta.WorkloadIdentityPools.ListWorkloadIdentityPools" `  




#### `UndeleteWorkloadIdentityPool`

  * **Method** : `[google.iam.v1beta.WorkloadIdentityPools.UndeleteWorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1beta#google.iam.v1beta.WorkloadIdentityPools.UndeleteWorkloadIdentityPool)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPools.undelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1beta.WorkloadIdentityPools.UndeleteWorkloadIdentityPool" `  




#### `UndeleteWorkloadIdentityPoolProvider`

  * **Method** : `[google.iam.v1beta.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1beta#google.iam.v1beta.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolProvider)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolProviders.undelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1beta.WorkloadIdentityPools.UndeleteWorkloadIdentityPoolProvider" `  




#### `UpdateWorkloadIdentityPool`

  * **Method** : `[google.iam.v1beta.WorkloadIdentityPools.UpdateWorkloadIdentityPool](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1beta#google.iam.v1beta.WorkloadIdentityPools.UpdateWorkloadIdentityPool)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPools.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1beta.WorkloadIdentityPools.UpdateWorkloadIdentityPool" `  




#### `UpdateWorkloadIdentityPoolProvider`

  * **Method** : `[google.iam.v1beta.WorkloadIdentityPools.UpdateWorkloadIdentityPoolProvider](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v1beta#google.iam.v1beta.WorkloadIdentityPools.UpdateWorkloadIdentityPoolProvider)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.workloadIdentityPoolProviders.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1beta.WorkloadIdentityPools.UpdateWorkloadIdentityPoolProvider" `  




### `google.iam.v2.Policies`

The following audit logs are associated with methods belonging to `google.iam.v2.Policies`.

#### `CreatePolicy`

  * **Method** : `[google.iam.v2.Policies.CreatePolicy](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v2#google.iam.v2.Policies.CreatePolicy)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.googleapis.com/accessboundarypolicies.create - ADMIN_WRITE`
    * `iam.googleapis.com/denypolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v2.Policies.CreatePolicy" `  




#### `DeletePolicy`

  * **Method** : `[google.iam.v2.Policies.DeletePolicy](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v2#google.iam.v2.Policies.DeletePolicy)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.googleapis.com/accessboundarypolicies.delete - ADMIN_WRITE`
    * `iam.googleapis.com/denypolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v2.Policies.DeletePolicy" `  




#### `GetPolicy`

  * **Method** : `[google.iam.v2.Policies.GetPolicy](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v2#google.iam.v2.Policies.GetPolicy)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.googleapis.com/denypolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v2.Policies.GetPolicy" `  




#### `ListPolicies`

  * **Method** : `[google.iam.v2.Policies.ListPolicies](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v2#google.iam.v2.Policies.ListPolicies)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.googleapis.com/denypolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v2.Policies.ListPolicies" `  




#### `UpdatePolicy`

  * **Method** : `[google.iam.v2.Policies.UpdatePolicy](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v2#google.iam.v2.Policies.UpdatePolicy)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.googleapis.com/accessboundarypolicies.update - ADMIN_WRITE`
    * `iam.googleapis.com/denypolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v2.Policies.UpdatePolicy" `  




### `google.iam.v2alpha.Policies`

The following audit logs are associated with methods belonging to `google.iam.v2alpha.Policies`.

#### `CreatePolicy`

  * **Method** : `google.iam.v2alpha.Policies.CreatePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.googleapis.com/denypolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v2alpha.Policies.CreatePolicy" `  




#### `DeletePolicy`

  * **Method** : `google.iam.v2alpha.Policies.DeletePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.googleapis.com/denypolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v2alpha.Policies.DeletePolicy" `  




#### `GetPolicy`

  * **Method** : `google.iam.v2alpha.Policies.GetPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.googleapis.com/denypolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v2alpha.Policies.GetPolicy" `  




#### `ListPolicies`

  * **Method** : `google.iam.v2alpha.Policies.ListPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.googleapis.com/denypolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v2alpha.Policies.ListPolicies" `  




#### `UpdatePolicy`

  * **Method** : `google.iam.v2alpha.Policies.UpdatePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.googleapis.com/denypolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v2alpha.Policies.UpdatePolicy" `  




### `google.iam.v2beta.Policies`

The following audit logs are associated with methods belonging to `google.iam.v2beta.Policies`.

#### `CreatePolicy`

  * **Method** : `[google.iam.v2beta.Policies.CreatePolicy](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v2beta#google.iam.v2beta.Policies.CreatePolicy)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.googleapis.com/denypolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v2beta.Policies.CreatePolicy" `  




#### `DeletePolicy`

  * **Method** : `[google.iam.v2beta.Policies.DeletePolicy](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v2beta#google.iam.v2beta.Policies.DeletePolicy)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.googleapis.com/denypolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v2beta.Policies.DeletePolicy" `  




#### `GetPolicy`

  * **Method** : `[google.iam.v2beta.Policies.GetPolicy](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v2beta#google.iam.v2beta.Policies.GetPolicy)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.googleapis.com/accessboundarypolicies.get - ADMIN_READ`
    * `iam.googleapis.com/denypolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v2beta.Policies.GetPolicy" `  




#### `ListPolicies`

  * **Method** : `[google.iam.v2beta.Policies.ListPolicies](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v2beta#google.iam.v2beta.Policies.ListPolicies)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.googleapis.com/denypolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v2beta.Policies.ListPolicies" `  




#### `UpdatePolicy`

  * **Method** : `[google.iam.v2beta.Policies.UpdatePolicy](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v2beta#google.iam.v2beta.Policies.UpdatePolicy)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.googleapis.com/denypolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v2beta.Policies.UpdatePolicy" `  




### `google.iam.v3.PolicyBindings`

The following audit logs are associated with methods belonging to `google.iam.v3.PolicyBindings`.

#### `CreatePolicyBinding`

  * **Method** : `google.iam.v3.PolicyBindings.CreatePolicyBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudresourcemanager.googleapis.com/projects.createPolicyBinding - ADMIN_WRITE`
    * `iam.googleapis.com/principalaccessboundarypolicies.bind - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3.PolicyBindings.CreatePolicyBinding" `  




#### `DeletePolicyBinding`

  * **Method** : `google.iam.v3.PolicyBindings.DeletePolicyBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudresourcemanager.googleapis.com/projects.deletePolicyBinding - ADMIN_WRITE`
    * `iam.googleapis.com/principalaccessboundarypolicies.unbind - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3.PolicyBindings.DeletePolicyBinding" `  




#### `GetPolicyBinding`

  * **Method** : `google.iam.v3.PolicyBindings.GetPolicyBinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.policybindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3.PolicyBindings.GetPolicyBinding" `  




#### `ListPolicyBindings`

  * **Method** : `google.iam.v3.PolicyBindings.ListPolicyBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.policybindings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3.PolicyBindings.ListPolicyBindings" `  




#### `SearchTargetPolicyBindings`

  * **Method** : `google.iam.v3.PolicyBindings.SearchTargetPolicyBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudresourcemanager.googleapis.com/projects.searchPolicyBindings - ADMIN_READ`
    * `iam.googleapis.com/workloadIdentityPools.searchPolicyBindings - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3.PolicyBindings.SearchTargetPolicyBindings" `  




#### `UpdatePolicyBinding`

  * **Method** : `google.iam.v3.PolicyBindings.UpdatePolicyBinding`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudresourcemanager.googleapis.com/projects.updatePolicyBinding - ADMIN_WRITE`
    * `iam.googleapis.com/principalaccessboundarypolicies.bind - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3.PolicyBindings.UpdatePolicyBinding" `  




### `google.iam.v3.PrincipalAccessBoundaryPolicies`

The following audit logs are associated with methods belonging to `google.iam.v3.PrincipalAccessBoundaryPolicies`.

#### `CreatePrincipalAccessBoundaryPolicy`

  * **Method** : `google.iam.v3.PrincipalAccessBoundaryPolicies.CreatePrincipalAccessBoundaryPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.principalaccessboundarypolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3.PrincipalAccessBoundaryPolicies.CreatePrincipalAccessBoundaryPolicy" `  




#### `DeletePrincipalAccessBoundaryPolicy`

  * **Method** : `google.iam.v3.PrincipalAccessBoundaryPolicies.DeletePrincipalAccessBoundaryPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.principalaccessboundarypolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3.PrincipalAccessBoundaryPolicies.DeletePrincipalAccessBoundaryPolicy" `  




#### `GetPrincipalAccessBoundaryPolicy`

  * **Method** : `google.iam.v3.PrincipalAccessBoundaryPolicies.GetPrincipalAccessBoundaryPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.principalaccessboundarypolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3.PrincipalAccessBoundaryPolicies.GetPrincipalAccessBoundaryPolicy" `  




#### `ListPrincipalAccessBoundaryPolicies`

  * **Method** : `google.iam.v3.PrincipalAccessBoundaryPolicies.ListPrincipalAccessBoundaryPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.principalaccessboundarypolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3.PrincipalAccessBoundaryPolicies.ListPrincipalAccessBoundaryPolicies" `  




#### `SearchPrincipalAccessBoundaryPolicyBindings`

  * **Method** : `google.iam.v3.PrincipalAccessBoundaryPolicies.SearchPrincipalAccessBoundaryPolicyBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.principalaccessboundarypolicies.searchPolicyBindings - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3.PrincipalAccessBoundaryPolicies.SearchPrincipalAccessBoundaryPolicyBindings" `  




#### `UpdatePrincipalAccessBoundaryPolicy`

  * **Method** : `google.iam.v3.PrincipalAccessBoundaryPolicies.UpdatePrincipalAccessBoundaryPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.principalaccessboundarypolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3.PrincipalAccessBoundaryPolicies.UpdatePrincipalAccessBoundaryPolicy" `  




### `google.iam.v3beta.AccessPolicies`

The following audit logs are associated with methods belonging to `google.iam.v3beta.AccessPolicies`.

#### `CreateAccessPolicy`

  * **Method** : `google.iam.v3beta.AccessPolicies.CreateAccessPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.accesspolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3beta.AccessPolicies.CreateAccessPolicy" `  




#### `DeleteAccessPolicy`

  * **Method** : `google.iam.v3beta.AccessPolicies.DeleteAccessPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.accesspolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3beta.AccessPolicies.DeleteAccessPolicy" `  




#### `GetAccessPolicy`

  * **Method** : `google.iam.v3beta.AccessPolicies.GetAccessPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.accesspolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3beta.AccessPolicies.GetAccessPolicy" `  




#### `ListAccessPolicies`

  * **Method** : `google.iam.v3beta.AccessPolicies.ListAccessPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.accesspolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3beta.AccessPolicies.ListAccessPolicies" `  




#### `SearchAccessPolicyBindings`

  * **Method** : `google.iam.v3beta.AccessPolicies.SearchAccessPolicyBindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.accesspolicies.searchPolicyBindings - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3beta.AccessPolicies.SearchAccessPolicyBindings" `  




#### `UpdateAccessPolicy`

  * **Method** : `google.iam.v3beta.AccessPolicies.UpdateAccessPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.accesspolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3beta.AccessPolicies.UpdateAccessPolicy" `  




### `google.iam.v3beta.PolicyBindings`

The following audit logs are associated with methods belonging to `google.iam.v3beta.PolicyBindings`.

#### `CreatePolicyBinding`

  * **Method** : `[google.iam.v3beta.PolicyBindings.CreatePolicyBinding](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v3beta#google.iam.v3beta.PolicyBindings.CreatePolicyBinding)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudresourcemanager.googleapis.com/projects.createPolicyBinding - ADMIN_WRITE`
    * `iam.googleapis.com/principalaccessboundarypolicies.bind - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3beta.PolicyBindings.CreatePolicyBinding" `  




#### `DeletePolicyBinding`

  * **Method** : `[google.iam.v3beta.PolicyBindings.DeletePolicyBinding](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v3beta#google.iam.v3beta.PolicyBindings.DeletePolicyBinding)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudresourcemanager.googleapis.com/projects.deletePolicyBinding - ADMIN_WRITE`
    * `iam.googleapis.com/principalaccessboundarypolicies.unbind - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3beta.PolicyBindings.DeletePolicyBinding" `  




#### `GetPolicyBinding`

  * **Method** : `[google.iam.v3beta.PolicyBindings.GetPolicyBinding](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v3beta#google.iam.v3beta.PolicyBindings.GetPolicyBinding)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.policybindings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3beta.PolicyBindings.GetPolicyBinding" `  




#### `ListPolicyBindings`

  * **Method** : `[google.iam.v3beta.PolicyBindings.ListPolicyBindings](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v3beta#google.iam.v3beta.PolicyBindings.ListPolicyBindings)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.policybindings.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3beta.PolicyBindings.ListPolicyBindings" `  




#### `SearchTargetPolicyBindings`

  * **Method** : `[google.iam.v3beta.PolicyBindings.SearchTargetPolicyBindings](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v3beta#google.iam.v3beta.PolicyBindings.SearchTargetPolicyBindings)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudresourcemanager.googleapis.com/folders.searchPolicyBindings - ADMIN_READ`
    * `cloudresourcemanager.googleapis.com/organizations.searchPolicyBindings - ADMIN_READ`
    * `cloudresourcemanager.googleapis.com/projects.searchPolicyBindings - ADMIN_READ`
    * `iam.googleapis.com/workspacePools.searchPolicyBindings - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3beta.PolicyBindings.SearchTargetPolicyBindings" `  




#### `UpdatePolicyBinding`

  * **Method** : `[google.iam.v3beta.PolicyBindings.UpdatePolicyBinding](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v3beta#google.iam.v3beta.PolicyBindings.UpdatePolicyBinding)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudresourcemanager.googleapis.com/projects.updatePolicyBinding - ADMIN_WRITE`
    * `iam.googleapis.com/principalaccessboundarypolicies.bind - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3beta.PolicyBindings.UpdatePolicyBinding" `  




### `google.iam.v3beta.PrincipalAccessBoundaryPolicies`

The following audit logs are associated with methods belonging to `google.iam.v3beta.PrincipalAccessBoundaryPolicies`.

#### `CreatePrincipalAccessBoundaryPolicy`

  * **Method** : `[google.iam.v3beta.PrincipalAccessBoundaryPolicies.CreatePrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v3beta#google.iam.v3beta.PrincipalAccessBoundaryPolicies.CreatePrincipalAccessBoundaryPolicy)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.principalaccessboundarypolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3beta.PrincipalAccessBoundaryPolicies.CreatePrincipalAccessBoundaryPolicy" `  




#### `DeletePrincipalAccessBoundaryPolicy`

  * **Method** : `[google.iam.v3beta.PrincipalAccessBoundaryPolicies.DeletePrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v3beta#google.iam.v3beta.PrincipalAccessBoundaryPolicies.DeletePrincipalAccessBoundaryPolicy)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.principalaccessboundarypolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3beta.PrincipalAccessBoundaryPolicies.DeletePrincipalAccessBoundaryPolicy" `  




#### `GetPrincipalAccessBoundaryPolicy`

  * **Method** : `[google.iam.v3beta.PrincipalAccessBoundaryPolicies.GetPrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v3beta#google.iam.v3beta.PrincipalAccessBoundaryPolicies.GetPrincipalAccessBoundaryPolicy)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.principalaccessboundarypolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3beta.PrincipalAccessBoundaryPolicies.GetPrincipalAccessBoundaryPolicy" `  




#### `ListPrincipalAccessBoundaryPolicies`

  * **Method** : `[google.iam.v3beta.PrincipalAccessBoundaryPolicies.ListPrincipalAccessBoundaryPolicies](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v3beta#google.iam.v3beta.PrincipalAccessBoundaryPolicies.ListPrincipalAccessBoundaryPolicies)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.principalaccessboundarypolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3beta.PrincipalAccessBoundaryPolicies.ListPrincipalAccessBoundaryPolicies" `  




#### `SearchPrincipalAccessBoundaryPolicyBindings`

  * **Method** : `[google.iam.v3beta.PrincipalAccessBoundaryPolicies.SearchPrincipalAccessBoundaryPolicyBindings](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v3beta#google.iam.v3beta.PrincipalAccessBoundaryPolicies.SearchPrincipalAccessBoundaryPolicyBindings)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.principalaccessboundarypolicies.searchPolicyBindings - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3beta.PrincipalAccessBoundaryPolicies.SearchPrincipalAccessBoundaryPolicyBindings" `  




#### `UpdatePrincipalAccessBoundaryPolicy`

  * **Method** : `[google.iam.v3beta.PrincipalAccessBoundaryPolicies.UpdatePrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/iam/docs/reference/rpc/google.iam.v3beta#google.iam.v3beta.PrincipalAccessBoundaryPolicies.UpdatePrincipalAccessBoundaryPolicy)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iam.principalaccessboundarypolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v3beta.PrincipalAccessBoundaryPolicies.UpdatePrincipalAccessBoundaryPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `GetOperation`

  * **Method** : `[google.longrunning.Operations.GetOperation](https://docs.cloud.google.com/iam/docs/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iam.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.iam.admin.v1.IAM.LintPolicy`
  * `google.iam.admin.v1.IAM.QueryAuditableServices`
  * `google.iam.admin.v1.IAM.QueryTestablePermissions`
  * `google.iam.admin.v1.IAM.SignBlob`
  * `google.iam.admin.v1.IAM.SignJwt`
  * `google.iam.admin.v1.WorkforcePools.TestIamPermissions`



## Sample queries

To use the sample queries in the following table, complete these steps:

  1. Replace the variables in the query expression with your own project information, then copy the expression using the clipboard icon _content_copy_.

  2. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  3. Enable **Show query** to open the query-editor field, then paste the expression into the query-editor field:

![The query editor where you enter sample queries.](https://docs.cloud.google.com/static/logging/docs/images/query-pane-2.png)

  4. Click **Run query**. Logs that match your query are listed in the **Query results** pane.




To find audit logs for Identity and Access Management, use the following queries in the Logs Explorer:

Before using the sample queries, replace the following values:

  * `SERVICE_ACCOUNT_SHORT_ID`: Everything preceding the `@` symbol in the service account's email address. For example, the service account ID of the service account `service-account@example.iam.gserviceaccount.com` is `service-account`.
  * `SERVICE_ACCOUNT_EMAIL`: The full email address of the service account. For example, `service-account@example.iam.gserviceaccount.com`.
  * `ROLE_NAME`: The full role name, including any `organizations/`, `projects/`, or `roles/` prefixes. For example, `organizations/123456789012/roles/myCompanyAdmin`.

Query name | Expression  
---|---  
Service account created | 
    
    
    resource.type = "service_account"
    protoPayload.serviceName = "iam.googleapis.com"
    protoPayload.methodName:"CreateServiceAccount"
    log_id("cloudaudit.googleapis.com/activity")
    (protoPayload.request.account_id:"SERVICE_ACCOUNT_SHORT_ID"
      OR protoPayload.response.email:"SERVICE_ACCOUNT_EMAIL")
      
  
Service account deleted | 
    
    
    resource.type = "service_account"
    protoPayload.serviceName = "iam.googleapis.com"
    protoPayload.methodName:"DeleteServiceAccount"
    log_id("cloudaudit.googleapis.com/activity")
    resource.labels.email_id:"SERVICE_ACCOUNT_EMAIL"
      
  
Service account key created | 
    
    
    resource.type = "service_account"
    protoPayload.serviceName = "iam.googleapis.com"
    protoPayload.methodName:"CreateServiceAccountKey"
    log_id("cloudaudit.googleapis.com/activity")
    resource.labels.email_id:"SERVICE_ACCOUNT_EMAIL"
      
  
Service account key deleted | 
    
    
    resource.type = "service_account"
    protoPayload.serviceName = "iam.googleapis.com"
    protoPayload.methodName:"DeleteServiceAccountKey"
    log_id("cloudaudit.googleapis.com/activity")
    resource.labels.email_id:"SERVICE_ACCOUNT_EMAIL"
      
  
Any resource created, modified, or deleted | 
    
    
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.methodName:("create" OR "delete" OR "update")
      
  
Custom role updated | 
    
    
    log_id("cloudaudit.googleapis.com/activity")
    resource.type = "iam_role"
    protoPayload.serviceName = "iam.googleapis.com"
    protoPayload.methodName:"UpdateRole"
    resource.labels.role_name:"ROLE_NAME"
      
  
Project-level allow policy updated | 
    
    
    resource.type = "project" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.methodName:"SetIamPolicy"
      
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
