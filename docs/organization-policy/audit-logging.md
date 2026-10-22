---
url: https://docs.cloud.google.com/organization-policy/audit-logging/
title: Organization Policy audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:14.806601+00:00
---

# Organization Policy audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Guides ](https://docs.cloud.google.com/organization-policy/overview)



Send feedback 

#  Organization Policy audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Organization Policy Service. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Notes

This document describes audit logging for the service which manages organization policies. For details on Policy Denied logs themselves see [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging). The v1 version of the Organization Policy API is hosted under `cloudresourcemanager.googleapis.com`, see the [Resource Manager audit logging page](https://docs.cloud.google.com/resource-manager/docs/audit-logging) for more details.

## Service name

Organization Policy Service audit logs use the service name `orgpolicy.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="orgpolicy.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Organization Policy Service generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.orgpolicy.v2.OrgPolicy.GetCustomConstraint`  
`google.cloud.orgpolicy.v2.OrgPolicy.GetEffectivePolicy`  
`google.cloud.orgpolicy.v2.OrgPolicy.GetPolicy`  
`google.cloud.orgpolicy.v2.OrgPolicy.ListConstraints`  
`google.cloud.orgpolicy.v2.OrgPolicy.ListCustomConstraints`  
`google.cloud.orgpolicy.v2.OrgPolicy.ListPolicies`  
`ADMIN_WRITE` | `google.cloud.orgpolicy.v2.OrgPolicy.CreateCustomConstraint`  
`google.cloud.orgpolicy.v2.OrgPolicy.CreatePolicy`  
`google.cloud.orgpolicy.v2.OrgPolicy.DeleteCustomConstraint`  
`google.cloud.orgpolicy.v2.OrgPolicy.DeletePolicy`  
`google.cloud.orgpolicy.v2.OrgPolicy.UpdateCustomConstraint`  
`google.cloud.orgpolicy.v2.OrgPolicy.UpdatePolicy`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Organization Policy Service.

### `google.cloud.orgpolicy.v2.OrgPolicy`

The following audit logs are associated with methods belonging to `google.cloud.orgpolicy.v2.OrgPolicy`.

#### `CreateCustomConstraint`

  * **Method** : `google.cloud.orgpolicy.v2.OrgPolicy.CreateCustomConstraint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `orgpolicy.customConstraints.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orgpolicy.v2.OrgPolicy.CreateCustomConstraint" `  




#### `CreatePolicy`

  * **Method** : `google.cloud.orgpolicy.v2.OrgPolicy.CreatePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `orgpolicy.policies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orgpolicy.v2.OrgPolicy.CreatePolicy" `  




#### `DeleteCustomConstraint`

  * **Method** : `google.cloud.orgpolicy.v2.OrgPolicy.DeleteCustomConstraint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `orgpolicy.customConstraints.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orgpolicy.v2.OrgPolicy.DeleteCustomConstraint" `  




#### `DeletePolicy`

  * **Method** : `google.cloud.orgpolicy.v2.OrgPolicy.DeletePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `orgpolicy.policies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orgpolicy.v2.OrgPolicy.DeletePolicy" `  




#### `GetCustomConstraint`

  * **Method** : `google.cloud.orgpolicy.v2.OrgPolicy.GetCustomConstraint`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `orgpolicy.customConstraints.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orgpolicy.v2.OrgPolicy.GetCustomConstraint" `  




#### `GetEffectivePolicy`

  * **Method** : `google.cloud.orgpolicy.v2.OrgPolicy.GetEffectivePolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `orgpolicy.policy.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orgpolicy.v2.OrgPolicy.GetEffectivePolicy" `  




#### `GetPolicy`

  * **Method** : `google.cloud.orgpolicy.v2.OrgPolicy.GetPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `orgpolicy.policy.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orgpolicy.v2.OrgPolicy.GetPolicy" `  




#### `ListConstraints`

  * **Method** : `google.cloud.orgpolicy.v2.OrgPolicy.ListConstraints`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `orgpolicy.constraints.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orgpolicy.v2.OrgPolicy.ListConstraints" `  




#### `ListCustomConstraints`

  * **Method** : `google.cloud.orgpolicy.v2.OrgPolicy.ListCustomConstraints`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `orgpolicy.customConstraints.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orgpolicy.v2.OrgPolicy.ListCustomConstraints" `  




#### `ListPolicies`

  * **Method** : `google.cloud.orgpolicy.v2.OrgPolicy.ListPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `orgpolicy.policies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orgpolicy.v2.OrgPolicy.ListPolicies" `  




#### `UpdateCustomConstraint`

  * **Method** : `google.cloud.orgpolicy.v2.OrgPolicy.UpdateCustomConstraint`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `orgpolicy.customConstraints.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orgpolicy.v2.OrgPolicy.UpdateCustomConstraint" `  




#### `UpdatePolicy`

  * **Method** : `google.cloud.orgpolicy.v2.OrgPolicy.UpdatePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `orgpolicy.policies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.orgpolicy.v2.OrgPolicy.UpdatePolicy" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
