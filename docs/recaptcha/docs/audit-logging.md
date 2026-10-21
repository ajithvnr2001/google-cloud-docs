---
url: https://docs.cloud.google.com/recaptcha/docs/audit-logging/
title: Google Cloud Fraud Defense audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:50:31.517138+00:00
---

# Google Cloud Fraud Defense audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/audit-logging/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Google Cloud Fraud Defense audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Fraud Defense. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Fraud Defense audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="recaptchaenterprise.googleapis.com"
           




## Methods by permission type

`DATA_WRITE` audit logs for `CreateAssessment` and `AnnotateAssessment` methods are deprecated. To disable `DATA_WRITE` audit logs see [Configure Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access). To view logs for the `CreateAssessment` and `AnnotateAssessment` methods see [Platform logs](https://docs.cloud.google.com/recaptcha-enterprise/docs/platform-logging).

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Google Cloud Fraud Defense generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.GetFirewallPolicy`  
`google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.GetKey`  
`google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.GetMetrics`  
`google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.GetPolicy`  
`google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.ListFirewallPolicies`  
`google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.ListIpOverrides`  
`google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.ListKeys`  
`google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.RetrieveLegacySecretKey`  
`google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.SearchRelatedAccountGroupMemberships`  
`ADMIN_WRITE` | `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.AddIpOverride`  
`google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.CreateFirewallPolicy`  
`google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.CreateKey`  
`google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.DeleteFirewallPolicy`  
`google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.DeleteKey`  
`google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.MigrateKey`  
`google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.RemoveIpOverride`  
`google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.ReorderFirewallPolicies`  
`google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.UpdateFirewallPolicy`  
`google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.UpdateKey`  
`google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.UpdatePolicy`  
`DATA_WRITE` | `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.CreateAssessment`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Fraud Defense.

### `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService`

The following audit logs are associated with methods belonging to `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService`.

#### `AddIpOverride`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.AddIpOverride`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `recaptchaenterprise.keys.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.AddIpOverride" `  




#### `AnnotateAssessment`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.AnnotateAssessment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `recaptchaenterprise.assessments.annotate - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.AnnotateAssessment" `  


**Note:** This audit log has been deprecated. To view logs for this method see [Platform logs](https://docs.cloud.google.com/recaptcha-enterprise/docs/platform-logging).

#### `CreateAssessment`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.CreateAssessment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `recaptchaenterprise.assessments.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.CreateAssessment" `  


**Note:** This audit log has been deprecated. To view logs for this method see [Platform logs](https://docs.cloud.google.com/recaptcha-enterprise/docs/platform-logging).

#### `CreateFirewallPolicy`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.CreateFirewallPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `recaptchaenterprise.firewallpolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.CreateFirewallPolicy" `  




#### `CreateKey`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.CreateKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `recaptchaenterprise.keys.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.CreateKey" `  




#### `DeleteFirewallPolicy`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.DeleteFirewallPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `recaptchaenterprise.firewallpolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.DeleteFirewallPolicy" `  




#### `DeleteKey`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.DeleteKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `recaptchaenterprise.keys.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.DeleteKey" `  




#### `GetFirewallPolicy`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.GetFirewallPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `recaptchaenterprise.firewallpolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.GetFirewallPolicy" `  




#### `GetKey`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.GetKey`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `recaptchaenterprise.keys.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.GetKey" `  




#### `GetMetrics`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.GetMetrics`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `recaptchaenterprise.metrics.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.GetMetrics" `  




#### `GetPolicy`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.GetPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `recaptchaenterprise.policies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.GetPolicy" `  




#### `ListFirewallPolicies`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.ListFirewallPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `recaptchaenterprise.firewallpolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.ListFirewallPolicies" `  




#### `ListIpOverrides`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.ListIpOverrides`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `recaptchaenterprise.keys.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.ListIpOverrides" `  




#### `ListKeys`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.ListKeys`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `recaptchaenterprise.keys.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.ListKeys" `  




#### `ListRelatedAccountGroupMemberships`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.ListRelatedAccountGroupMemberships`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.ListRelatedAccountGroupMemberships" `  




#### `ListRelatedAccountGroups`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.ListRelatedAccountGroups`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.ListRelatedAccountGroups" `  




#### `MigrateKey`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.MigrateKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `recaptchaenterprise.keys.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.MigrateKey" `  




#### `RemoveIpOverride`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.RemoveIpOverride`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `recaptchaenterprise.keys.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.RemoveIpOverride" `  




#### `ReorderFirewallPolicies`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.ReorderFirewallPolicies`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `recaptchaenterprise.firewallpolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.ReorderFirewallPolicies" `  




#### `RetrieveLegacySecretKey`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.RetrieveLegacySecretKey`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `recaptchaenterprise.keys.retrievelegacysecretkey - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.RetrieveLegacySecretKey" `  




#### `SearchRelatedAccountGroupMemberships`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.SearchRelatedAccountGroupMemberships`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `recaptchaenterprise.relatedaccountgroupmemberships.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.SearchRelatedAccountGroupMemberships" `  




#### `UpdateFirewallPolicy`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.UpdateFirewallPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `recaptchaenterprise.firewallpolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.UpdateFirewallPolicy" `  




#### `UpdateKey`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.UpdateKey`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `recaptchaenterprise.keys.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.UpdateKey" `  




#### `UpdatePolicy`

  * **Method** : `google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.UpdatePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `recaptchaenterprise.policies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService.UpdatePolicy" `  




### `google.cloud.recaptchaenterprise.v1beta1.RecaptchaEnterpriseServiceV1Beta1`

The following audit logs are associated with methods belonging to `google.cloud.recaptchaenterprise.v1beta1.RecaptchaEnterpriseServiceV1Beta1`.

#### `CreateAssessment`

  * **Method** : `google.cloud.recaptchaenterprise.v1beta1.RecaptchaEnterpriseServiceV1Beta1.CreateAssessment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `recaptchaenterprise.assessments.create - PERMISSION_TYPE_UNSPECIFIED`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recaptchaenterprise.v1beta1.RecaptchaEnterpriseServiceV1Beta1.CreateAssessment" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.recaptchaenterprise.v1beta1.RecaptchaEnterpriseServiceV1Beta1.AnnotateAssessment`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
