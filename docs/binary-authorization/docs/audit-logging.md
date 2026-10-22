---
url: https://docs.cloud.google.com/binary-authorization/docs/audit-logging/
title: Binary Authorization audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:05.392434+00:00
---

# Binary Authorization audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Binary Authorization audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Binary Authorization. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Binary Authorization audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="binaryauthorization.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Binary Authorization generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.GetAttestor`  
`google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.GetPolicy`  
`google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.ListAttestors`  
`google.cloud.binaryauthorization.v1.PlatformPolicyManagementService.GetPlatformPolicy`  
`google.cloud.binaryauthorization.v1.PlatformPolicyManagementService.ListPlatformPolicies`  
`google.cloud.binaryauthorization.v1.ValidationHelperV1.ValidateAttestationOccurrence`  
`google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.GetAttestor`  
`google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.GetPolicy`  
`google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.ListAttestors`  
`google.iam.v1.IAMPolicy.GetIamPolicy`  
`ADMIN_WRITE` | `google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.CreateAttestor`  
`google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.DeleteAttestor`  
`google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.UpdateAttestor`  
`google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.UpdatePolicy`  
`google.cloud.binaryauthorization.v1.PlatformPolicyManagementService.CreatePlatformPolicy`  
`google.cloud.binaryauthorization.v1.PlatformPolicyManagementService.DeletePlatformPolicy`  
`google.cloud.binaryauthorization.v1.PlatformPolicyManagementService.ReplacePlatformPolicy`  
`google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.CreateAttestor`  
`google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.DeleteAttestor`  
`google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.UpdateAttestor`  
`google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.UpdatePolicy`  
`google.iam.v1.IAMPolicy.SetIamPolicy`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Binary Authorization.

### `google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1`

The following audit logs are associated with methods belonging to `google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1`.

#### `CreateAttestor`

  * **Method** : `google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.CreateAttestor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `binaryauthorization.attestors.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.CreateAttestor" `  




#### `DeleteAttestor`

  * **Method** : `google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.DeleteAttestor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `binaryauthorization.attestors.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.DeleteAttestor" `  




#### `GetAttestor`

  * **Method** : `google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.GetAttestor`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `binaryauthorization.attestors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.GetAttestor" `  




#### `GetPolicy`

  * **Method** : `google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.GetPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `binaryauthorization.policy.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.GetPolicy" `  




#### `ListAttestors`

  * **Method** : `google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.ListAttestors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `binaryauthorization.attestors.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.ListAttestors" `  




#### `UpdateAttestor`

  * **Method** : `google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.UpdateAttestor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `binaryauthorization.attestors.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.UpdateAttestor" `  




#### `UpdatePolicy`

  * **Method** : `google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.UpdatePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `binaryauthorization.attestors.get - ADMIN_READ`
    * `binaryauthorization.attestors.list - ADMIN_READ`
    * `binaryauthorization.policy.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.UpdatePolicy" `  




### `google.cloud.binaryauthorization.v1.PlatformPolicyManagementService`

The following audit logs are associated with methods belonging to `google.cloud.binaryauthorization.v1.PlatformPolicyManagementService`.

#### `CreatePlatformPolicy`

  * **Method** : `google.cloud.binaryauthorization.v1.PlatformPolicyManagementService.CreatePlatformPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `binaryauthorization.platformPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.binaryauthorization.v1.PlatformPolicyManagementService.CreatePlatformPolicy" `  




#### `DeletePlatformPolicy`

  * **Method** : `google.cloud.binaryauthorization.v1.PlatformPolicyManagementService.DeletePlatformPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `binaryauthorization.platformPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.binaryauthorization.v1.PlatformPolicyManagementService.DeletePlatformPolicy" `  




#### `GetPlatformPolicy`

  * **Method** : `google.cloud.binaryauthorization.v1.PlatformPolicyManagementService.GetPlatformPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `binaryauthorization.platformPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.binaryauthorization.v1.PlatformPolicyManagementService.GetPlatformPolicy" `  




#### `ListPlatformPolicies`

  * **Method** : `google.cloud.binaryauthorization.v1.PlatformPolicyManagementService.ListPlatformPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `binaryauthorization.platformPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.binaryauthorization.v1.PlatformPolicyManagementService.ListPlatformPolicies" `  




#### `ReplacePlatformPolicy`

  * **Method** : `google.cloud.binaryauthorization.v1.PlatformPolicyManagementService.ReplacePlatformPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `binaryauthorization.platformPolicies.replace - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.binaryauthorization.v1.PlatformPolicyManagementService.ReplacePlatformPolicy" `  




### `google.cloud.binaryauthorization.v1.ValidationHelperV1`

The following audit logs are associated with methods belonging to `google.cloud.binaryauthorization.v1.ValidationHelperV1`.

#### `ValidateAttestationOccurrence`

  * **Method** : `google.cloud.binaryauthorization.v1.ValidationHelperV1.ValidateAttestationOccurrence`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `binaryauthorization.attestors.verifyImageAttested - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.binaryauthorization.v1.ValidationHelperV1.ValidateAttestationOccurrence" `  




### `google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1`

The following audit logs are associated with methods belonging to `google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1`.

#### `CreateAttestor`

  * **Method** : `google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.CreateAttestor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `binaryauthorization.attestors.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.CreateAttestor" `  




#### `DeleteAttestor`

  * **Method** : `google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.DeleteAttestor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `binaryauthorization.attestors.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.DeleteAttestor" `  




#### `GetAttestor`

  * **Method** : `google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.GetAttestor`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `binaryauthorization.attestors.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.GetAttestor" `  




#### `GetPolicy`

  * **Method** : `google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.GetPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `binaryauthorization.policy.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.GetPolicy" `  




#### `ListAttestors`

  * **Method** : `google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.ListAttestors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `binaryauthorization.attestors.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.ListAttestors" `  




#### `UpdateAttestor`

  * **Method** : `google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.UpdateAttestor`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `binaryauthorization.attestors.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.UpdateAttestor" `  




#### `UpdatePolicy`

  * **Method** : `google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.UpdatePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `binaryauthorization.policy.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.binaryauthorization.v1beta1.BinauthzManagementServiceV1Beta1.UpdatePolicy" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `google.iam.v1.IAMPolicy.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `binaryauthorization.attestors.getIamPolicy - ADMIN_READ`
    * `binaryauthorization.policy.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.IAMPolicy.GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `google.iam.v1.IAMPolicy.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `binaryauthorization.attestors.setIamPolicy - ADMIN_WRITE`
    * `binaryauthorization.policy.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.IAMPolicy.SetIamPolicy" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.binaryauthorization.v1.PlatformPolicyEvaluationService.EvaluateGkePolicy`
  * `google.cloud.binaryauthorization.v1.SystemPolicyV1.GetSystemPolicy`
  * `google.cloud.binaryauthorization.v1beta1.SystemPolicyV1Beta1.GetSystemPolicy`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
