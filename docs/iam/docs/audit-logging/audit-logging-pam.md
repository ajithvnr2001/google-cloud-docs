---
url: https://docs.cloud.google.com/iam/docs/audit-logging/audit-logging-pam/
title: Privileged Access Manager audit logging \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:40.797562+00:00
---

# Privileged Access Manager audit logging  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/audit-logging/audit-logging-pam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Privileged Access Manager audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Privileged Access Manager. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Privileged Access Manager audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="privilegedaccessmanager.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Privileged Access Manager generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.CheckOnboardingStatus`  
`google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.GetEntitlement`  
`google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.GetGrant`  
`google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.ListEntitlements`  
`google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.ListGrants`  
`google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.CheckOnboardingStatus`  
`google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.FetchEffectiveSettings`  
`google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.GetEntitlement`  
`google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.GetGrant`  
`google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.GetSettings`  
`google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.ListEntitlements`  
`google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.ListGrants`  
`google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.CheckOnboardingStatus`  
`google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.FetchEffectiveSettings`  
`google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.GetEntitlement`  
`google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.GetGrant`  
`google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.GetSettings`  
`google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.ListEntitlements`  
`google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.ListGrants`  
`ADMIN_WRITE` | `google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.ApproveGrant`  
`google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.CreateEntitlement` (LRO)  
`google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.CreateGrant`  
`google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.DeleteEntitlement` (LRO)  
`google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.DenyGrant`  
`google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.RevokeGrant` (LRO)  
`google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.UpdateEntitlement` (LRO)  
`google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.ApproveGrant`  
`google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.CreateEntitlement` (LRO)  
`google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.CreateGrant`  
`google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.DeleteEntitlement` (LRO)  
`google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.DenyGrant`  
`google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.RevokeGrant` (LRO)  
`google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.UpdateEntitlement` (LRO)  
`google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.UpdateSettings` (LRO)  
`google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.WithdrawGrant` (LRO)  
`google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.ApproveGrant`  
`google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.CreateEntitlement` (LRO)  
`google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.CreateGrant`  
`google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.DeleteEntitlement` (LRO)  
`google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.DenyGrant`  
`google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.RevokeGrant` (LRO)  
`google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.UpdateEntitlement` (LRO)  
`google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.UpdateSettings` (LRO)  
`google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.WithdrawGrant` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Privileged Access Manager.

### `google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager`

The following audit logs are associated with methods belonging to `google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager`.

#### `ApproveGrant`

  * **Method** : `google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.ApproveGrant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.grants.approve - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.ApproveGrant" `  




#### `CheckOnboardingStatus`

  * **Method** : `google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.CheckOnboardingStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privilegedaccessmanager.locations.checkOnboardingStatus - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.CheckOnboardingStatus" `  




#### `CreateEntitlement`

  * **Method** : `google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.CreateEntitlement`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.entitlements.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.CreateEntitlement" `  




#### `CreateGrant`

  * **Method** : `google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.CreateGrant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.grants.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.CreateGrant" `  




#### `DeleteEntitlement`

  * **Method** : `google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.DeleteEntitlement`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.entitlements.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.DeleteEntitlement" `  




#### `DenyGrant`

  * **Method** : `google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.DenyGrant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.grants.deny - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.DenyGrant" `  




#### `GetEntitlement`

  * **Method** : `google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.GetEntitlement`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privilegedaccessmanager.entitlements.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.GetEntitlement" `  




#### `GetGrant`

  * **Method** : `google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.GetGrant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privilegedaccessmanager.grants.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.GetGrant" `  




#### `ListEntitlements`

  * **Method** : `google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.ListEntitlements`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privilegedaccessmanager.entitlements.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.ListEntitlements" `  




#### `ListGrants`

  * **Method** : `google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.ListGrants`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privilegedaccessmanager.grants.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.ListGrants" `  




#### `RevokeGrant`

  * **Method** : `google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.RevokeGrant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.grants.revoke - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.RevokeGrant" `  




#### `UpdateEntitlement`

  * **Method** : `google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.UpdateEntitlement`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.entitlements.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.UpdateEntitlement" `  




### `google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager`

The following audit logs are associated with methods belonging to `google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager`.

#### `ApproveGrant`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.ApproveGrant](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1alpha#google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.ApproveGrant)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.grants.approve - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.ApproveGrant" `  




#### `CheckOnboardingStatus`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.CheckOnboardingStatus](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1alpha#google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.CheckOnboardingStatus)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privilegedaccessmanager.locations.checkOnboardingStatus - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.CheckOnboardingStatus" `  




#### `CreateEntitlement`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.CreateEntitlement](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1alpha#google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.CreateEntitlement)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.entitlements.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.CreateEntitlement" `  




#### `CreateGrant`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.CreateGrant](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1alpha#google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.CreateGrant)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.grants.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.CreateGrant" `  




#### `DeleteEntitlement`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.DeleteEntitlement](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1alpha#google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.DeleteEntitlement)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.entitlements.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.DeleteEntitlement" `  




#### `DenyGrant`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.DenyGrant](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1alpha#google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.DenyGrant)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.grants.deny - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.DenyGrant" `  




#### `FetchEffectiveSettings`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.FetchEffectiveSettings](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1alpha#google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.FetchEffectiveSettings)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privilegedaccessmanager.settings.fetchEffective - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.FetchEffectiveSettings" `  




#### `GetEntitlement`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.GetEntitlement](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1alpha#google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.GetEntitlement)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privilegedaccessmanager.entitlements.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.GetEntitlement" `  




#### `GetGrant`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.GetGrant](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1alpha#google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.GetGrant)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privilegedaccessmanager.grants.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.GetGrant" `  




#### `GetSettings`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.GetSettings](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1alpha#google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.GetSettings)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privilegedaccessmanager.settings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.GetSettings" `  




#### `ListEntitlements`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.ListEntitlements](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1alpha#google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.ListEntitlements)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privilegedaccessmanager.entitlements.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.ListEntitlements" `  




#### `ListGrants`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.ListGrants](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1alpha#google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.ListGrants)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privilegedaccessmanager.grants.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.ListGrants" `  




#### `RevokeGrant`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.RevokeGrant](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1alpha#google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.RevokeGrant)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.grants.revoke - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.RevokeGrant" `  




#### `UpdateEntitlement`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.UpdateEntitlement](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1alpha#google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.UpdateEntitlement)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.entitlements.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.UpdateEntitlement" `  




#### `UpdateSettings`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.UpdateSettings](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1alpha#google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.UpdateSettings)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.settings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.UpdateSettings" `  




#### `WithdrawGrant`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.WithdrawGrant](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1alpha#google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.WithdrawGrant)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.grants.withdraw - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.WithdrawGrant" `  




### `google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager`

The following audit logs are associated with methods belonging to `google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager`.

#### `ApproveGrant`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.ApproveGrant](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1beta#google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.ApproveGrant)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.grants.approve - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.ApproveGrant" `  




#### `CheckOnboardingStatus`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.CheckOnboardingStatus](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1beta#google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.CheckOnboardingStatus)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privilegedaccessmanager.locations.checkOnboardingStatus - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.CheckOnboardingStatus" `  




#### `CreateEntitlement`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.CreateEntitlement](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1beta#google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.CreateEntitlement)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.entitlements.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.CreateEntitlement" `  




#### `CreateGrant`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.CreateGrant](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1beta#google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.CreateGrant)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.grants.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.CreateGrant" `  




#### `DeleteEntitlement`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.DeleteEntitlement](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1beta#google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.DeleteEntitlement)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.entitlements.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.DeleteEntitlement" `  




#### `DenyGrant`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.DenyGrant](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1beta#google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.DenyGrant)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.grants.deny - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.DenyGrant" `  




#### `FetchEffectiveSettings`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.FetchEffectiveSettings](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1beta#google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.FetchEffectiveSettings)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privilegedaccessmanager.settings.fetchEffective - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.FetchEffectiveSettings" `  




#### `GetEntitlement`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.GetEntitlement](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1beta#google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.GetEntitlement)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privilegedaccessmanager.entitlements.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.GetEntitlement" `  




#### `GetGrant`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.GetGrant](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1beta#google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.GetGrant)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privilegedaccessmanager.grants.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.GetGrant" `  




#### `GetSettings`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.GetSettings](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1beta#google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.GetSettings)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privilegedaccessmanager.settings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.GetSettings" `  




#### `ListEntitlements`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.ListEntitlements](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1beta#google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.ListEntitlements)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privilegedaccessmanager.entitlements.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.ListEntitlements" `  




#### `ListGrants`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.ListGrants](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1beta#google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.ListGrants)`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `privilegedaccessmanager.grants.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.ListGrants" `  




#### `RevokeGrant`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.RevokeGrant](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1beta#google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.RevokeGrant)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.grants.revoke - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.RevokeGrant" `  




#### `UpdateEntitlement`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.UpdateEntitlement](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1beta#google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.UpdateEntitlement)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.entitlements.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.UpdateEntitlement" `  




#### `UpdateSettings`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.UpdateSettings](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1beta#google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.UpdateSettings)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.settings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.UpdateSettings" `  




#### `WithdrawGrant`

  * **Method** : `[google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.WithdrawGrant](https://docs.cloud.google.com/iam/docs/reference/pam/rpc/google.cloud.privilegedaccessmanager.v1beta#google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.WithdrawGrant)`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `privilegedaccessmanager.grants.withdraw - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.WithdrawGrant" `  




## System events

System Event audit logs are generated by GCP systems, not direct user action. For more information, see [System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event).

Method Name | Filter For This Event | Notes  
---|---|---  
PAMActivateGrant |  ` protoPayload.methodName="PAMActivateGrant" ` |   
PAMDeleteGrant |  ` protoPayload.methodName="PAMDeleteGrant" ` |   
PAMEndGrant |  ` protoPayload.methodName="PAMEndGrant" ` |   
PAMExpireGrant |  ` protoPayload.methodName="PAMExpireGrant" ` |   
PAMReportExternalGrantModification |  ` protoPayload.methodName="PAMReportExternalGrantModification" ` |   
  
## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.SearchEntitlements`
  * `google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.SearchGrants`
  * `google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.SearchEntitlements`
  * `google.cloud.privilegedaccessmanager.v1alpha.PrivilegedAccessManager.SearchGrants`
  * `google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.SearchEntitlements`
  * `google.cloud.privilegedaccessmanager.v1beta.PrivilegedAccessManager.SearchGrants`
  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.DeleteOperation`
  * `google.longrunning.Operations.GetOperation`
  * `google.longrunning.Operations.ListOperations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
