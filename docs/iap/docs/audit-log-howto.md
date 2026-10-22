---
url: https://docs.cloud.google.com/iap/docs/audit-log-howto/
title: Identity-Aware Proxy audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:53.034027+00:00
---

# Identity-Aware Proxy audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/audit-log-howto/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Identity-Aware Proxy audit logging Stay organized with collections  Save and categorize content based on your preferences. 

**Important:**

On February 14, 2024, the Cloud Audit Logging (CAL) type was inadvertently changed from `DATA_ACCESS` to `ADMIN_ACTIVITY`. This change causes a change in the log name and log bucket location for the `UpdateIapSettings` and `ValidateIapAttributeExpression` methods. 

The CAL type has been changed back to `DATA_ACCESS`.

This document lists the audited methods for Identity-Aware Proxy. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Notes

The fields section describes important details about some fields in the audit log.

## Service name

To view the Identity-Aware Proxy audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="iap.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Identity-Aware Proxy generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.iap.v1.IdentityAwareProxyAdminService.GetIamPolicy`  
`google.cloud.iap.v1.IdentityAwareProxyAdminService.GetIapSettings`  
`google.cloud.iap.v1beta1.IdentityAwareProxyAdminV1Beta1.GetIamPolicy`  
`ADMIN_WRITE` | `google.cloud.iap.v1.IdentityAwareProxyAdminService.SetIamPolicy`  
`google.cloud.iap.v1beta1.IdentityAwareProxyAdminV1Beta1.SetIamPolicy`  
`DATA_READ` | `google.cloud.iap.v1.IdentityAwareProxyAdminService.GetTunnelDestGroup`  
`google.cloud.iap.v1.IdentityAwareProxyAdminService.ListTunnelDestGroups`  
`DATA_WRITE` | `google.cloud.iap.v1.IdentityAwareProxyAdminService.CreateTunnelDestGroup`  
`google.cloud.iap.v1.IdentityAwareProxyAdminService.DeleteTunnelDestGroup`  
`google.cloud.iap.v1.IdentityAwareProxyAdminService.UpdateIapSettings`  
`google.cloud.iap.v1.IdentityAwareProxyAdminService.UpdateTunnelDestGroup`  
`google.cloud.iap.v1.IdentityAwareProxyAdminService.ValidateIapAttributeExpression`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Identity-Aware Proxy.

### `google.cloud.iap.v1.IdentityAwareProxyAdminService`

The following audit logs are associated with methods belonging to `google.cloud.iap.v1.IdentityAwareProxyAdminService`.

#### `CreateTunnelDestGroup`

  * **Method** : `google.cloud.iap.v1.IdentityAwareProxyAdminService.CreateTunnelDestGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iap.tunnelDestGroups.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.iap.v1.IdentityAwareProxyAdminService.CreateTunnelDestGroup" `  




#### `DeleteTunnelDestGroup`

  * **Method** : `google.cloud.iap.v1.IdentityAwareProxyAdminService.DeleteTunnelDestGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iap.tunnelDestGroups.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.iap.v1.IdentityAwareProxyAdminService.DeleteTunnelDestGroup" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.iap.v1.IdentityAwareProxyAdminService.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iap.tunnelServices.getIamPolicy - ADMIN_READ`
    * `iap.web.getIamPolicy - ADMIN_READ`
    * `iap.webServiceVersions.getIamPolicy - ADMIN_READ`
    * `iap.webServices.getIamPolicy - ADMIN_READ`
    * `iap.webTypes.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.iap.v1.IdentityAwareProxyAdminService.GetIamPolicy" `  




#### `GetIapSettings`

  * **Method** : `google.cloud.iap.v1.IdentityAwareProxyAdminService.GetIapSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iap.projects.getSettings - ADMIN_READ`
    * `iap.web.getSettings - ADMIN_READ`
    * `iap.webServiceVersions.getSettings - ADMIN_READ`
    * `iap.webServices.getSettings - ADMIN_READ`
    * `iap.webTypes.getSettings - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.iap.v1.IdentityAwareProxyAdminService.GetIapSettings" `  




#### `GetTunnelDestGroup`

  * **Method** : `google.cloud.iap.v1.IdentityAwareProxyAdminService.GetTunnelDestGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iap.tunnelDestGroups.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.iap.v1.IdentityAwareProxyAdminService.GetTunnelDestGroup" `  




#### `ListTunnelDestGroups`

  * **Method** : `google.cloud.iap.v1.IdentityAwareProxyAdminService.ListTunnelDestGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iap.tunnelDestGroups.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.iap.v1.IdentityAwareProxyAdminService.ListTunnelDestGroups" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.iap.v1.IdentityAwareProxyAdminService.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iap.tunnelServices.setIamPolicy - ADMIN_WRITE`
    * `iap.web.setIamPolicy - ADMIN_WRITE`
    * `iap.webServiceVersions.setIamPolicy - ADMIN_WRITE`
    * `iap.webServices.setIamPolicy - ADMIN_WRITE`
    * `iap.webTypes.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.iap.v1.IdentityAwareProxyAdminService.SetIamPolicy" `  




#### `UpdateIapSettings`

  * **Method** : `google.cloud.iap.v1.IdentityAwareProxyAdminService.UpdateIapSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iap.projects.updateSettings - DATA_WRITE`
    * `iap.web.updateSettings - DATA_WRITE`
    * `iap.webServiceVersions.updateSettings - DATA_WRITE`
    * `iap.webServices.updateSettings - DATA_WRITE`
    * `iap.webTypes.updateSettings - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.iap.v1.IdentityAwareProxyAdminService.UpdateIapSettings" `  




#### `UpdateTunnelDestGroup`

  * **Method** : `google.cloud.iap.v1.IdentityAwareProxyAdminService.UpdateTunnelDestGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iap.tunnelDestGroups.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.iap.v1.IdentityAwareProxyAdminService.UpdateTunnelDestGroup" `  




#### `ValidateIapAttributeExpression`

  * **Method** : `google.cloud.iap.v1.IdentityAwareProxyAdminService.ValidateIapAttributeExpression`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iap.projects.updateSettings - DATA_WRITE`
    * `iap.web.updateSettings - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.iap.v1.IdentityAwareProxyAdminService.ValidateIapAttributeExpression" `  




### `google.cloud.iap.v1beta1.IdentityAwareProxyAdminV1Beta1`

The following audit logs are associated with methods belonging to `google.cloud.iap.v1beta1.IdentityAwareProxyAdminV1Beta1`.

#### `GetIamPolicy`

  * **Method** : `google.cloud.iap.v1beta1.IdentityAwareProxyAdminV1Beta1.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `iap.tunnelServices.getIamPolicy - ADMIN_READ`
    * `iap.web.getIamPolicy - ADMIN_READ`
    * `iap.webServiceVersions.getIamPolicy - ADMIN_READ`
    * `iap.webServices.getIamPolicy - ADMIN_READ`
    * `iap.webTypes.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.iap.v1beta1.IdentityAwareProxyAdminV1Beta1.GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.iap.v1beta1.IdentityAwareProxyAdminV1Beta1.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `iap.tunnelServices.setIamPolicy - ADMIN_WRITE`
    * `iap.webServiceVersions.setIamPolicy - ADMIN_WRITE`
    * `iap.webServices.setIamPolicy - ADMIN_WRITE`
    * `iap.webTypes.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.iap.v1beta1.IdentityAwareProxyAdminV1Beta1.SetIamPolicy" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.iap.v1.IdentityAwareProxyOAuthService.CreateBrand`
  * `google.cloud.iap.v1.IdentityAwareProxyOAuthService.CreateIdentityAwareProxyClient`
  * `google.cloud.iap.v1.IdentityAwareProxyOAuthService.DeleteIdentityAwareProxyClient`
  * `google.cloud.iap.v1.IdentityAwareProxyOAuthService.GetBrand`
  * `google.cloud.iap.v1.IdentityAwareProxyOAuthService.GetIdentityAwareProxyClient`
  * `google.cloud.iap.v1.IdentityAwareProxyOAuthService.ListBrands`
  * `google.cloud.iap.v1.IdentityAwareProxyOAuthService.ListIdentityAwareProxyClients`
  * `google.cloud.iap.v1.IdentityAwareProxyOAuthService.ResetIdentityAwareProxyClientSecret`
  * `google.cloud.iap.v1beta1.IdentityAwareProxyAdminV1Beta1.TestIamPermissions`



## Fields

The logs only contain information about the [access levels](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels) that a user has met. Access levels that blocked an unauthorized request are not listed in the log entry. To determine what conditions are required to make a successful request for a given resource, check the access levels for the resource.

The following are important details about some fields in the log:

Field | Value  
---|---  
`authenticationInfo` | The email of the user who tried to access the resource as `principalEmail`. This information is not present in logs for unauthenticated requests.  
`requestMetadata.callerIp` | The IP address the request originated from.  
`requestMetadata.requestAttributes` | The request method and URL.  
`authorizationInfo.resource` | The resource being accessed.  
`authorizationInfo.granted` | A boolean representing whether IAP permitted the requested access.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
