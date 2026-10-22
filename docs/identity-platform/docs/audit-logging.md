---
url: https://docs.cloud.google.com/identity-platform/docs/audit-logging/
title: Identity Platform audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:53.754272+00:00
---

# Identity Platform audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Reference ](https://docs.cloud.google.com/identity-platform/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Identity Platform audit logging

This document describes audit logging for Identity Platform. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Identity Platform audit logs use the service name `identitytoolkit.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="identitytoolkit.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Identity Platform generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.GetConfig`  
`google.cloud.identitytoolkit.admin.v2.ProjectConfigService.GetDefaultSupportedIdpConfig`  
`google.cloud.identitytoolkit.admin.v2.ProjectConfigService.GetIamPolicy`  
`google.cloud.identitytoolkit.admin.v2.ProjectConfigService.GetInboundSamlConfig`  
`google.cloud.identitytoolkit.admin.v2.ProjectConfigService.GetOAuthIdpConfig`  
`google.cloud.identitytoolkit.admin.v2.ProjectConfigService.ListDefaultSupportedIdpConfigs`  
`google.cloud.identitytoolkit.admin.v2.ProjectConfigService.ListInboundSamlConfigs`  
`google.cloud.identitytoolkit.admin.v2.ProjectConfigService.ListOAuthIdpConfigs`  
`google.cloud.identitytoolkit.admin.v2.TenantManagementService.GetTenant`  
`google.cloud.identitytoolkit.admin.v2.TenantManagementService.ListTenants`  
`google.cloud.identitytoolkit.v1.AccountManagementService.DownloadAccount`  
`google.cloud.identitytoolkit.v2beta1.ProjectConfigService.GetConfig`  
`google.cloud.identitytoolkit.v2beta1.ProjectConfigService.GetDefaultSupportedIdpConfig`  
`google.cloud.identitytoolkit.v2beta1.ProjectConfigService.GetInboundSamlConfig`  
`google.cloud.identitytoolkit.v2beta1.ProjectConfigService.GetOAuthIdpConfig`  
`google.cloud.identitytoolkit.v2beta1.ProjectConfigService.ListDefaultSupportedIdpConfigs`  
`google.cloud.identitytoolkit.v2beta1.ProjectConfigService.ListInboundSamlConfigs`  
`google.cloud.identitytoolkit.v2beta1.ProjectConfigService.ListOAuthIdpConfigs`  
`google.cloud.identitytoolkit.v2beta1.TenantManagementService.GetTenant`  
`google.cloud.identitytoolkit.v2beta1.TenantManagementService.ListTenants`  
`ADMIN_WRITE` | `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.CreateDefaultSupportedIdpConfig`  
`google.cloud.identitytoolkit.admin.v2.ProjectConfigService.CreateInboundSamlConfig`  
`google.cloud.identitytoolkit.admin.v2.ProjectConfigService.CreateOAuthIdpConfig`  
`google.cloud.identitytoolkit.admin.v2.ProjectConfigService.DeleteDefaultSupportedIdpConfig`  
`google.cloud.identitytoolkit.admin.v2.ProjectConfigService.DeleteInboundSamlConfig`  
`google.cloud.identitytoolkit.admin.v2.ProjectConfigService.DeleteOAuthIdpConfig`  
`google.cloud.identitytoolkit.admin.v2.ProjectConfigService.InitializeIdentityPlatform`  
`google.cloud.identitytoolkit.admin.v2.ProjectConfigService.SetIamPolicy`  
`google.cloud.identitytoolkit.admin.v2.ProjectConfigService.UpdateConfig`  
`google.cloud.identitytoolkit.admin.v2.ProjectConfigService.UpdateDefaultSupportedIdpConfig`  
`google.cloud.identitytoolkit.admin.v2.ProjectConfigService.UpdateInboundSamlConfig`  
`google.cloud.identitytoolkit.admin.v2.ProjectConfigService.UpdateOAuthIdpConfig`  
`google.cloud.identitytoolkit.admin.v2.ProjectConfigService.VerifyDomain`  
`google.cloud.identitytoolkit.admin.v2.TenantManagementService.CreateTenant`  
`google.cloud.identitytoolkit.admin.v2.TenantManagementService.DeleteTenant`  
`google.cloud.identitytoolkit.admin.v2.TenantManagementService.UpdateTenant`  
`google.cloud.identitytoolkit.v2beta1.ProjectConfigService.CreateDefaultSupportedIdpConfig`  
`google.cloud.identitytoolkit.v2beta1.ProjectConfigService.CreateInboundSamlConfig`  
`google.cloud.identitytoolkit.v2beta1.ProjectConfigService.CreateOAuthIdpConfig`  
`google.cloud.identitytoolkit.v2beta1.ProjectConfigService.DeleteDefaultSupportedIdpConfig`  
`google.cloud.identitytoolkit.v2beta1.ProjectConfigService.DeleteInboundSamlConfig`  
`google.cloud.identitytoolkit.v2beta1.ProjectConfigService.DeleteOAuthIdpConfig`  
`google.cloud.identitytoolkit.v2beta1.ProjectConfigService.EnableCicp`  
`google.cloud.identitytoolkit.v2beta1.ProjectConfigService.UpdateConfig`  
`google.cloud.identitytoolkit.v2beta1.ProjectConfigService.UpdateDefaultSupportedIdpConfig`  
`google.cloud.identitytoolkit.v2beta1.ProjectConfigService.UpdateInboundSamlConfig`  
`google.cloud.identitytoolkit.v2beta1.ProjectConfigService.UpdateOAuthIdpConfig`  
`google.cloud.identitytoolkit.v2beta1.ProjectConfigService.VerifyDomain`  
`google.cloud.identitytoolkit.v2beta1.TenantManagementService.CreateTenant`  
`google.cloud.identitytoolkit.v2beta1.TenantManagementService.DeleteTenant`  
`google.cloud.identitytoolkit.v2beta1.TenantManagementService.UpdateTenant`  
`DATA_READ` | `google.cloud.identitytoolkit.v1.AccountManagementService.DownloadAccount`  
`google.cloud.identitytoolkit.v1.AccountManagementService.GetAccountInfo`  
`google.cloud.identitytoolkit.v1.AccountManagementService.QueryUserInfo`  
`DATA_WRITE` | `google.cloud.identitytoolkit.v1.AccountManagementService.BatchDeleteAccounts`  
`google.cloud.identitytoolkit.v1.AccountManagementService.DeleteAccount`  
`google.cloud.identitytoolkit.v1.AccountManagementService.GetOobCode`  
`google.cloud.identitytoolkit.v1.AccountManagementService.SetAccountInfo`  
`google.cloud.identitytoolkit.v1.AccountManagementService.UploadAccount`  
`google.cloud.identitytoolkit.v1.AuthenticationService.SignUp`  
`google.cloud.identitytoolkit.v1.SessionManagementService.CreateSessionCookie`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the [Identity and Access Management documentation](https://docs.cloud.google.com/identity-platform/docs/iam) for Identity Platform.

### `google.cloud.identitytoolkit.admin.v2.ProjectConfigService`

The following audit logs are associated with methods belonging to `google.cloud.identitytoolkit.admin.v2.ProjectConfigService`.

#### `CreateDefaultSupportedIdpConfig`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.CreateDefaultSupportedIdpConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.getSecret - ADMIN_READ`
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.CreateDefaultSupportedIdpConfig" `  




#### `CreateInboundSamlConfig`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.CreateInboundSamlConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.CreateInboundSamlConfig" `  




#### `CreateOAuthIdpConfig`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.CreateOAuthIdpConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.getSecret - ADMIN_READ`
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.CreateOAuthIdpConfig" `  




#### `DeleteDefaultSupportedIdpConfig`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.DeleteDefaultSupportedIdpConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.DeleteDefaultSupportedIdpConfig" `  




#### `DeleteInboundSamlConfig`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.DeleteInboundSamlConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.DeleteInboundSamlConfig" `  




#### `DeleteOAuthIdpConfig`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.DeleteOAuthIdpConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.DeleteOAuthIdpConfig" `  




#### `GetConfig`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.GetConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.configs.get - ADMIN_READ`
    * `firebaseauth.configs.getHashConfig - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.GetConfig" `  




#### `GetDefaultSupportedIdpConfig`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.GetDefaultSupportedIdpConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.configs.get - ADMIN_READ`
    * `firebaseauth.configs.getSecret - ADMIN_READ`
    * `identitytoolkit.tenants.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.GetDefaultSupportedIdpConfig" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `identitytoolkit.tenants.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.GetIamPolicy" `  




#### `GetInboundSamlConfig`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.GetInboundSamlConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.configs.get - ADMIN_READ`
    * `identitytoolkit.tenants.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.GetInboundSamlConfig" `  




#### `GetOAuthIdpConfig`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.GetOAuthIdpConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.configs.get - ADMIN_READ`
    * `firebaseauth.configs.getSecret - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.GetOAuthIdpConfig" `  




#### `InitializeIdentityPlatform`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.InitializeIdentityPlatform`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.InitializeIdentityPlatform" `  




#### `ListDefaultSupportedIdpConfigs`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.ListDefaultSupportedIdpConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.configs.get - ADMIN_READ`
    * `firebaseauth.configs.getSecret - ADMIN_READ`
    * `identitytoolkit.tenants.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.ListDefaultSupportedIdpConfigs" `  




#### `ListInboundSamlConfigs`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.ListInboundSamlConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.configs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.ListInboundSamlConfigs" `  




#### `ListOAuthIdpConfigs`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.ListOAuthIdpConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.configs.get - ADMIN_READ`
    * `firebaseauth.configs.getSecret - ADMIN_READ`
    * `identitytoolkit.tenants.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.ListOAuthIdpConfigs" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `identitytoolkit.tenants.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.SetIamPolicy" `  




#### `UpdateConfig`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.UpdateConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.getHashConfig - ADMIN_READ`
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.UpdateConfig" `  




#### `UpdateDefaultSupportedIdpConfig`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.UpdateDefaultSupportedIdpConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.getSecret - ADMIN_READ`
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.UpdateDefaultSupportedIdpConfig" `  




#### `UpdateInboundSamlConfig`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.UpdateInboundSamlConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.UpdateInboundSamlConfig" `  




#### `UpdateOAuthIdpConfig`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.UpdateOAuthIdpConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.getSecret - ADMIN_READ`
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.UpdateOAuthIdpConfig" `  




#### `VerifyDomain`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.VerifyDomain`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.ProjectConfigService.VerifyDomain" `  




### `google.cloud.identitytoolkit.admin.v2.TenantManagementService`

The following audit logs are associated with methods belonging to `google.cloud.identitytoolkit.admin.v2.TenantManagementService`.

#### `CreateTenant`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.TenantManagementService.CreateTenant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `identitytoolkit.tenants.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.TenantManagementService.CreateTenant" `  




#### `DeleteTenant`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.TenantManagementService.DeleteTenant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `identitytoolkit.tenants.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.TenantManagementService.DeleteTenant" `  




#### `GetTenant`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.TenantManagementService.GetTenant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.configs.getHashConfig - ADMIN_READ`
    * `identitytoolkit.tenants.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.TenantManagementService.GetTenant" `  




#### `ListTenants`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.TenantManagementService.ListTenants`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `identitytoolkit.tenants.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.TenantManagementService.ListTenants" `  




#### `UpdateTenant`

  * **Method** : `google.cloud.identitytoolkit.admin.v2.TenantManagementService.UpdateTenant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `identitytoolkit.tenants.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.admin.v2.TenantManagementService.UpdateTenant" `  




### `google.cloud.identitytoolkit.v1.AccountManagementService`

The following audit logs are associated with methods belonging to `google.cloud.identitytoolkit.v1.AccountManagementService`.

#### `BatchDeleteAccounts`

  * **Method** : `google.cloud.identitytoolkit.v1.AccountManagementService.BatchDeleteAccounts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.users.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v1.AccountManagementService.BatchDeleteAccounts" `  




#### `DeleteAccount`

  * **Method** : `google.cloud.identitytoolkit.v1.AccountManagementService.DeleteAccount`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.users.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v1.AccountManagementService.DeleteAccount" `  




#### `DownloadAccount`

  * **Method** : `google.cloud.identitytoolkit.v1.AccountManagementService.DownloadAccount`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.configs.getHashConfig - ADMIN_READ`
    * `firebaseauth.users.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v1.AccountManagementService.DownloadAccount" `  




#### `GetAccountInfo`

  * **Method** : `google.cloud.identitytoolkit.v1.AccountManagementService.GetAccountInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.users.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v1.AccountManagementService.GetAccountInfo" `  




#### `GetOobCode`

  * **Method** : `google.cloud.identitytoolkit.v1.AccountManagementService.GetOobCode`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.users.sendEmail - DATA_WRITE`
    * `identitytoolkit.tenants.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v1.AccountManagementService.GetOobCode" `  




#### `QueryUserInfo`

  * **Method** : `google.cloud.identitytoolkit.v1.AccountManagementService.QueryUserInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.users.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v1.AccountManagementService.QueryUserInfo" `  




#### `SetAccountInfo`

  * **Method** : `google.cloud.identitytoolkit.v1.AccountManagementService.SetAccountInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.users.update - DATA_WRITE`
    * `identitytoolkit.tenants.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v1.AccountManagementService.SetAccountInfo" `  




#### `UploadAccount`

  * **Method** : `google.cloud.identitytoolkit.v1.AccountManagementService.UploadAccount`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.users.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v1.AccountManagementService.UploadAccount" `  




### `google.cloud.identitytoolkit.v1.AuthenticationService`

The following audit logs are associated with methods belonging to `google.cloud.identitytoolkit.v1.AuthenticationService`.

#### `SignUp`

  * **Method** : `google.cloud.identitytoolkit.v1.AuthenticationService.SignUp`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.users.create - DATA_WRITE`
    * `identitytoolkit.tenants.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v1.AuthenticationService.SignUp" `  




### `google.cloud.identitytoolkit.v1.SessionManagementService`

The following audit logs are associated with methods belonging to `google.cloud.identitytoolkit.v1.SessionManagementService`.

#### `CreateSessionCookie`

  * **Method** : `google.cloud.identitytoolkit.v1.SessionManagementService.CreateSessionCookie`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.users.createSession - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v1.SessionManagementService.CreateSessionCookie" `  




### `google.cloud.identitytoolkit.v2beta1.ProjectConfigService`

The following audit logs are associated with methods belonging to `google.cloud.identitytoolkit.v2beta1.ProjectConfigService`.

#### `CreateDefaultSupportedIdpConfig`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.ProjectConfigService.CreateDefaultSupportedIdpConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.getSecret - ADMIN_READ`
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.ProjectConfigService.CreateDefaultSupportedIdpConfig" `  




#### `CreateInboundSamlConfig`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.ProjectConfigService.CreateInboundSamlConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.ProjectConfigService.CreateInboundSamlConfig" `  




#### `CreateOAuthIdpConfig`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.ProjectConfigService.CreateOAuthIdpConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.getSecret - ADMIN_READ`
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.ProjectConfigService.CreateOAuthIdpConfig" `  




#### `DeleteDefaultSupportedIdpConfig`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.ProjectConfigService.DeleteDefaultSupportedIdpConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.ProjectConfigService.DeleteDefaultSupportedIdpConfig" `  




#### `DeleteInboundSamlConfig`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.ProjectConfigService.DeleteInboundSamlConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.ProjectConfigService.DeleteInboundSamlConfig" `  




#### `DeleteOAuthIdpConfig`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.ProjectConfigService.DeleteOAuthIdpConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.ProjectConfigService.DeleteOAuthIdpConfig" `  




#### `EnableCicp`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.ProjectConfigService.EnableCicp`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.ProjectConfigService.EnableCicp" `  




#### `GetConfig`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.ProjectConfigService.GetConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.configs.get - ADMIN_READ`
    * `firebaseauth.configs.getHashConfig - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.ProjectConfigService.GetConfig" `  




#### `GetDefaultSupportedIdpConfig`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.ProjectConfigService.GetDefaultSupportedIdpConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.configs.get - ADMIN_READ`
    * `firebaseauth.configs.getSecret - ADMIN_READ`
    * `identitytoolkit.tenants.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.ProjectConfigService.GetDefaultSupportedIdpConfig" `  




#### `GetInboundSamlConfig`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.ProjectConfigService.GetInboundSamlConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.configs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.ProjectConfigService.GetInboundSamlConfig" `  




#### `GetOAuthIdpConfig`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.ProjectConfigService.GetOAuthIdpConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.configs.get - ADMIN_READ`
    * `firebaseauth.configs.getSecret - ADMIN_READ`
    * `identitytoolkit.tenants.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.ProjectConfigService.GetOAuthIdpConfig" `  




#### `ListDefaultSupportedIdpConfigs`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.ProjectConfigService.ListDefaultSupportedIdpConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.configs.get - ADMIN_READ`
    * `firebaseauth.configs.getSecret - ADMIN_READ`
    * `identitytoolkit.tenants.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.ProjectConfigService.ListDefaultSupportedIdpConfigs" `  




#### `ListInboundSamlConfigs`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.ProjectConfigService.ListInboundSamlConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.configs.get - ADMIN_READ`
    * `identitytoolkit.tenants.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.ProjectConfigService.ListInboundSamlConfigs" `  




#### `ListOAuthIdpConfigs`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.ProjectConfigService.ListOAuthIdpConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.configs.getSecret - ADMIN_READ`
    * `identitytoolkit.tenants.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.ProjectConfigService.ListOAuthIdpConfigs" `  




#### `UpdateConfig`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.ProjectConfigService.UpdateConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.getHashConfig - ADMIN_READ`
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.ProjectConfigService.UpdateConfig" `  




#### `UpdateDefaultSupportedIdpConfig`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.ProjectConfigService.UpdateDefaultSupportedIdpConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.getSecret - ADMIN_READ`
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.ProjectConfigService.UpdateDefaultSupportedIdpConfig" `  




#### `UpdateInboundSamlConfig`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.ProjectConfigService.UpdateInboundSamlConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.ProjectConfigService.UpdateInboundSamlConfig" `  




#### `UpdateOAuthIdpConfig`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.ProjectConfigService.UpdateOAuthIdpConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.getSecret - ADMIN_READ`
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.ProjectConfigService.UpdateOAuthIdpConfig" `  




#### `VerifyDomain`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.ProjectConfigService.VerifyDomain`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `firebaseauth.configs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.ProjectConfigService.VerifyDomain" `  




### `google.cloud.identitytoolkit.v2beta1.TenantManagementService`

The following audit logs are associated with methods belonging to `google.cloud.identitytoolkit.v2beta1.TenantManagementService`.

#### `CreateTenant`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.TenantManagementService.CreateTenant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `identitytoolkit.tenants.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.TenantManagementService.CreateTenant" `  




#### `DeleteTenant`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.TenantManagementService.DeleteTenant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `identitytoolkit.tenants.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.TenantManagementService.DeleteTenant" `  




#### `GetTenant`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.TenantManagementService.GetTenant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `firebaseauth.configs.getHashConfig - ADMIN_READ`
    * `identitytoolkit.tenants.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.TenantManagementService.GetTenant" `  




#### `ListTenants`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.TenantManagementService.ListTenants`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `identitytoolkit.tenants.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.TenantManagementService.ListTenants" `  




#### `UpdateTenant`

  * **Method** : `google.cloud.identitytoolkit.v2beta1.TenantManagementService.UpdateTenant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `identitytoolkit.tenants.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.identitytoolkit.v2beta1.TenantManagementService.UpdateTenant" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.identitytoolkit.admin.v2.ProjectConfigService.TestIamPermissions`
  * `google.cloud.identitytoolkit.v1.AuthenticationService.CreateAuthUri`
  * `google.cloud.identitytoolkit.v1.AuthenticationService.GetPublicKeys`
  * `google.cloud.identitytoolkit.v1.AuthenticationService.GetRecaptchaParam`
  * `google.cloud.identitytoolkit.v1.AuthenticationService.IssueSamlResponse`
  * `google.cloud.identitytoolkit.v1.AuthenticationService.SendVerificationCode`
  * `google.cloud.identitytoolkit.v1.AuthenticationService.SignInWithCustomToken`
  * `google.cloud.identitytoolkit.v1.AuthenticationService.SignInWithEmailLink`
  * `google.cloud.identitytoolkit.v1.AuthenticationService.SignInWithGameCenter`
  * `google.cloud.identitytoolkit.v1.AuthenticationService.SignInWithIdp`
  * `google.cloud.identitytoolkit.v1.AuthenticationService.SignInWithPassword`
  * `google.cloud.identitytoolkit.v1.AuthenticationService.SignInWithPhoneNumber`
  * `google.cloud.identitytoolkit.v1.AuthenticationService.VerifyIosClient`
  * `google.cloud.identitytoolkit.v1.SessionManagementService.GetSessionCookiePublicKeys`
  * `google.cloud.identitytoolkit.v2.AuthenticationService.FinalizeMfaSignIn`
  * `google.cloud.identitytoolkit.v2.AuthenticationService.GetPasswordPolicy`
  * `google.cloud.identitytoolkit.v2.AuthenticationService.GetRecaptchaConfig`
  * `google.cloud.identitytoolkit.v2.AuthenticationService.RevokeToken`
  * `google.cloud.identitytoolkit.v2.AuthenticationService.StartMfaSignIn`
  * `google.cloud.identitytoolkit.v2alpha1.AccountManagementService.FinalizeMfaEnrollment`
  * `google.cloud.identitytoolkit.v2alpha1.AccountManagementService.StartMfaEnrollment`
  * `google.cloud.identitytoolkit.v2alpha1.AccountManagementService.WithdrawMfa`
  * `google.cloud.identitytoolkit.v2alpha1.AuthenticationV2Alpha1Service.FinalizeMfaSignIn`
  * `google.cloud.identitytoolkit.v2alpha1.AuthenticationV2Alpha1Service.StartMfaSignIn`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
