---
url: https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/simulator-audit-logging/
title: Policy Simulator audit logging \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:52.374562+00:00
---

# Policy Simulator audit logging  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/audit-logging/simulator-audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/policy-intelligence/docs/overview)



Send feedback 

#  Policy Simulator audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Policy Simulator. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Policy Simulator audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="policysimulator.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Policy Simulator generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.policysimulator.v1.AccessPolicySimulator.ListAccessPolicySimulationResults`  
`google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.GetOrgPolicyViolationsPreview`  
`google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.ListOrgPolicyViolations`  
`google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.ListOrgPolicyViolationsPreviews`  
`google.cloud.policysimulator.v1.Simulator.GetReplay`  
`google.cloud.policysimulator.v1.Simulator.ListReplayResults`  
`google.cloud.policysimulator.v1beta.AccessPolicySimulator.ListAccessPolicySimulationResults`  
`google.cloud.policysimulator.v1beta.OrgPolicyViolationsPreviewService.GetOrgPolicyViolationsPreview`  
`google.cloud.policysimulator.v1beta.OrgPolicyViolationsPreviewService.ListOrgPolicyViolations`  
`google.cloud.policysimulator.v1beta.OrgPolicyViolationsPreviewService.ListOrgPolicyViolationsPreviews`  
`google.cloud.policysimulator.v1beta.Simulator.GetReplay`  
`google.cloud.policysimulator.v1beta.Simulator.ListReplayResults`  
`ADMIN_WRITE` | `google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.CreateOrgPolicyViolationsPreview` (LRO)  
`google.cloud.policysimulator.v1.Simulator.CreateReplay` (LRO)  
`google.cloud.policysimulator.v1beta.OrgPolicyViolationsPreviewService.CreateOrgPolicyViolationsPreview` (LRO)  
`google.cloud.policysimulator.v1beta.OrgPolicyViolationsPreviewService.GenerateOrgPolicyViolationsPreview` (LRO)  
`google.cloud.policysimulator.v1beta.Simulator.CreateReplay` (LRO)  
  
## Audit logs for each API interface

### `google.cloud.policysimulator.v1.AccessPolicySimulator`

The following audit logs are associated with methods belonging to `google.cloud.policysimulator.v1.AccessPolicySimulator`.

#### `ListAccessPolicySimulationResults`

  * **Method** : `google.cloud.policysimulator.v1.AccessPolicySimulator.ListAccessPolicySimulationResults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `policysimulator.accessPolicySimulationResults.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.policysimulator.v1.AccessPolicySimulator.ListAccessPolicySimulationResults" `  




### `google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService`

The following audit logs are associated with methods belonging to `google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService`.

#### `CreateOrgPolicyViolationsPreview`

  * **Method** : `google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.CreateOrgPolicyViolationsPreview`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `policysimulator.orgPolicyViolationsPreviews.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.CreateOrgPolicyViolationsPreview" `  




#### `GetOrgPolicyViolationsPreview`

  * **Method** : `google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.GetOrgPolicyViolationsPreview`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `policysimulator.orgPolicyViolationsPreviews.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.GetOrgPolicyViolationsPreview" `  




#### `ListOrgPolicyViolations`

  * **Method** : `google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.ListOrgPolicyViolations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `policysimulator.orgPolicyViolations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.ListOrgPolicyViolations" `  




#### `ListOrgPolicyViolationsPreviews`

  * **Method** : `google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.ListOrgPolicyViolationsPreviews`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `policysimulator.orgPolicyViolationsPreviews.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.ListOrgPolicyViolationsPreviews" `  




### `google.cloud.policysimulator.v1.Simulator`

The following audit logs are associated with methods belonging to `google.cloud.policysimulator.v1.Simulator`.

#### `CreateReplay`

  * **Method** : `google.cloud.policysimulator.v1.Simulator.CreateReplay`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `policysimulator.replays.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.policysimulator.v1.Simulator.CreateReplay" `  




#### `GetReplay`

  * **Method** : `google.cloud.policysimulator.v1.Simulator.GetReplay`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `policysimulator.replays.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.policysimulator.v1.Simulator.GetReplay" `  




#### `ListReplayResults`

  * **Method** : `google.cloud.policysimulator.v1.Simulator.ListReplayResults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `policysimulator.replayResults.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.policysimulator.v1.Simulator.ListReplayResults" `  




### `google.cloud.policysimulator.v1beta.AccessPolicySimulator`

The following audit logs are associated with methods belonging to `google.cloud.policysimulator.v1beta.AccessPolicySimulator`.

#### `ListAccessPolicySimulationResults`

  * **Method** : `google.cloud.policysimulator.v1beta.AccessPolicySimulator.ListAccessPolicySimulationResults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `policysimulator.accessPolicySimulationResults.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.policysimulator.v1beta.AccessPolicySimulator.ListAccessPolicySimulationResults" `  




### `google.cloud.policysimulator.v1beta.OrgPolicyViolationsPreviewService`

The following audit logs are associated with methods belonging to `google.cloud.policysimulator.v1beta.OrgPolicyViolationsPreviewService`.

#### `CreateOrgPolicyViolationsPreview`

  * **Method** : `google.cloud.policysimulator.v1beta.OrgPolicyViolationsPreviewService.CreateOrgPolicyViolationsPreview`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `policysimulator.orgPolicyViolationsPreviews.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.policysimulator.v1beta.OrgPolicyViolationsPreviewService.CreateOrgPolicyViolationsPreview" `  




#### `GenerateOrgPolicyViolationsPreview`

  * **Method** : `google.cloud.policysimulator.v1beta.OrgPolicyViolationsPreviewService.GenerateOrgPolicyViolationsPreview`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `policysimulator.orgPolicyViolationsPreviews.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.policysimulator.v1beta.OrgPolicyViolationsPreviewService.GenerateOrgPolicyViolationsPreview" `  




#### `GetOrgPolicyViolationsPreview`

  * **Method** : `google.cloud.policysimulator.v1beta.OrgPolicyViolationsPreviewService.GetOrgPolicyViolationsPreview`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `policysimulator.orgPolicyViolationsPreviews.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.policysimulator.v1beta.OrgPolicyViolationsPreviewService.GetOrgPolicyViolationsPreview" `  




#### `ListOrgPolicyViolations`

  * **Method** : `google.cloud.policysimulator.v1beta.OrgPolicyViolationsPreviewService.ListOrgPolicyViolations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `policysimulator.orgPolicyViolations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.policysimulator.v1beta.OrgPolicyViolationsPreviewService.ListOrgPolicyViolations" `  




#### `ListOrgPolicyViolationsPreviews`

  * **Method** : `google.cloud.policysimulator.v1beta.OrgPolicyViolationsPreviewService.ListOrgPolicyViolationsPreviews`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `policysimulator.orgPolicyViolationsPreviews.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.policysimulator.v1beta.OrgPolicyViolationsPreviewService.ListOrgPolicyViolationsPreviews" `  




### `google.cloud.policysimulator.v1beta.Simulator`

The following audit logs are associated with methods belonging to `google.cloud.policysimulator.v1beta.Simulator`.

#### `CreateReplay`

  * **Method** : `google.cloud.policysimulator.v1beta.Simulator.CreateReplay`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `policysimulator.replays.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.policysimulator.v1beta.Simulator.CreateReplay" `  




#### `GetReplay`

  * **Method** : `google.cloud.policysimulator.v1beta.Simulator.GetReplay`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `policysimulator.replays.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.policysimulator.v1beta.Simulator.GetReplay" `  




#### `ListReplayResults`

  * **Method** : `google.cloud.policysimulator.v1beta.Simulator.ListReplayResults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `policysimulator.replayResults.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.policysimulator.v1beta.Simulator.ListReplayResults" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.policysimulator.v1beta.Simulator.ListReplays`
  * `google.longrunning.Operations.GetOperation`
  * `google.longrunning.Operations.ListOperations`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
