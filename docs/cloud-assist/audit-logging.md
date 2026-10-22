---
url: https://docs.cloud.google.com/cloud-assist/audit-logging/
title: Gemini Cloud Assist audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:59.847482+00:00
---

# Gemini Cloud Assist audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ Guides ](https://docs.cloud.google.com/cloud-assist/overview)



Send feedback 

#  Gemini Cloud Assist audit logging Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** This page covers audit logging information for the `geminicloudassist` API. Gemini Cloud Assist also uses the `cloudaicompanion` API. For information about audit logging for the `cloudaicompanion` API, see [`cloudaicompanion` API audit logging](https://docs.cloud.google.com/gemini/docs/audit-logging).

This document lists the audited methods for Gemini Cloud Assist. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Gemini Cloud Assist audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="geminicloudassist.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Gemini Cloud Assist generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.geminicloudassist.v1.InvestigationService.GetInvestigation`  
`google.cloud.geminicloudassist.v1.InvestigationService.GetInvestigationRevision`  
`google.cloud.geminicloudassist.v1.InvestigationService.ListInvestigationRevisions`  
`google.cloud.geminicloudassist.v1.InvestigationService.ListInvestigations`  
`google.cloud.geminicloudassist.v1alpha.InvestigationService.GetInvestigation`  
`google.cloud.geminicloudassist.v1alpha.InvestigationService.GetInvestigationRevision`  
`google.cloud.geminicloudassist.v1alpha.InvestigationService.ListInvestigationRevisions`  
`google.cloud.geminicloudassist.v1alpha.InvestigationService.ListInvestigations`  
`GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.geminicloudassist.v1.InvestigationService.CreateInvestigation`  
`google.cloud.geminicloudassist.v1.InvestigationService.DeleteInvestigation`  
`google.cloud.geminicloudassist.v1.InvestigationService.DeleteInvestigationRevision`  
`google.cloud.geminicloudassist.v1.InvestigationService.RunInvestigationRevision` (LRO)  
`google.cloud.geminicloudassist.v1.InvestigationService.UpdateInvestigation`  
`google.cloud.geminicloudassist.v1alpha.InvestigationService.CreateInvestigation`  
`google.cloud.geminicloudassist.v1alpha.InvestigationService.CreateInvestigationRevision`  
`google.cloud.geminicloudassist.v1alpha.InvestigationService.DeleteInvestigation`  
`google.cloud.geminicloudassist.v1alpha.InvestigationService.DeleteInvestigationRevision`  
`google.cloud.geminicloudassist.v1alpha.InvestigationService.ModifyInvestigationRevision`  
`google.cloud.geminicloudassist.v1alpha.InvestigationService.RunInvestigationRevision` (LRO)  
`google.cloud.geminicloudassist.v1alpha.InvestigationService.UpdateInvestigation`  
`SetIamPolicy`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Gemini Cloud Assist.

### `google.cloud.geminicloudassist.v1.InvestigationService`

The following audit logs are associated with methods belonging to `google.cloud.geminicloudassist.v1.InvestigationService`.

#### `CreateInvestigation`

  * **Method** : `google.cloud.geminicloudassist.v1.InvestigationService.CreateInvestigation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminicloudassist.investigations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminicloudassist.v1.InvestigationService.CreateInvestigation" `  




#### `DeleteInvestigation`

  * **Method** : `google.cloud.geminicloudassist.v1.InvestigationService.DeleteInvestigation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminicloudassist.investigations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminicloudassist.v1.InvestigationService.DeleteInvestigation" `  




#### `DeleteInvestigationRevision`

  * **Method** : `google.cloud.geminicloudassist.v1.InvestigationService.DeleteInvestigationRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminicloudassist.investigationRevisions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminicloudassist.v1.InvestigationService.DeleteInvestigationRevision" `  




#### `GetInvestigation`

  * **Method** : `google.cloud.geminicloudassist.v1.InvestigationService.GetInvestigation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminicloudassist.investigations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminicloudassist.v1.InvestigationService.GetInvestigation" `  




#### `GetInvestigationRevision`

  * **Method** : `google.cloud.geminicloudassist.v1.InvestigationService.GetInvestigationRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminicloudassist.investigationRevisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminicloudassist.v1.InvestigationService.GetInvestigationRevision" `  




#### `ListInvestigationRevisions`

  * **Method** : `google.cloud.geminicloudassist.v1.InvestigationService.ListInvestigationRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminicloudassist.investigationRevisions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminicloudassist.v1.InvestigationService.ListInvestigationRevisions" `  




#### `ListInvestigations`

  * **Method** : `google.cloud.geminicloudassist.v1.InvestigationService.ListInvestigations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminicloudassist.investigations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminicloudassist.v1.InvestigationService.ListInvestigations" `  




#### `RunInvestigationRevision`

  * **Method** : `google.cloud.geminicloudassist.v1.InvestigationService.RunInvestigationRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminicloudassist.investigationRevisions.run - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminicloudassist.v1.InvestigationService.RunInvestigationRevision" `  




#### `UpdateInvestigation`

  * **Method** : `google.cloud.geminicloudassist.v1.InvestigationService.UpdateInvestigation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminicloudassist.investigations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminicloudassist.v1.InvestigationService.UpdateInvestigation" `  




### `google.cloud.geminicloudassist.v1alpha.InvestigationService`

The following audit logs are associated with methods belonging to `google.cloud.geminicloudassist.v1alpha.InvestigationService`.

#### `CreateInvestigation`

  * **Method** : `google.cloud.geminicloudassist.v1alpha.InvestigationService.CreateInvestigation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminicloudassist.investigations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminicloudassist.v1alpha.InvestigationService.CreateInvestigation" `  




#### `CreateInvestigationRevision`

  * **Method** : `google.cloud.geminicloudassist.v1alpha.InvestigationService.CreateInvestigationRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminicloudassist.investigationRevisions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminicloudassist.v1alpha.InvestigationService.CreateInvestigationRevision" `  




#### `DeleteInvestigation`

  * **Method** : `google.cloud.geminicloudassist.v1alpha.InvestigationService.DeleteInvestigation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminicloudassist.investigations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminicloudassist.v1alpha.InvestigationService.DeleteInvestigation" `  




#### `DeleteInvestigationRevision`

  * **Method** : `google.cloud.geminicloudassist.v1alpha.InvestigationService.DeleteInvestigationRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminicloudassist.investigationRevisions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminicloudassist.v1alpha.InvestigationService.DeleteInvestigationRevision" `  




#### `GetInvestigation`

  * **Method** : `google.cloud.geminicloudassist.v1alpha.InvestigationService.GetInvestigation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminicloudassist.investigations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminicloudassist.v1alpha.InvestigationService.GetInvestigation" `  




#### `GetInvestigationRevision`

  * **Method** : `google.cloud.geminicloudassist.v1alpha.InvestigationService.GetInvestigationRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminicloudassist.investigationRevisions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminicloudassist.v1alpha.InvestigationService.GetInvestigationRevision" `  




#### `ListInvestigationRevisions`

  * **Method** : `google.cloud.geminicloudassist.v1alpha.InvestigationService.ListInvestigationRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminicloudassist.investigationRevisions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminicloudassist.v1alpha.InvestigationService.ListInvestigationRevisions" `  




#### `ListInvestigations`

  * **Method** : `google.cloud.geminicloudassist.v1alpha.InvestigationService.ListInvestigations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminicloudassist.investigations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminicloudassist.v1alpha.InvestigationService.ListInvestigations" `  




#### `ModifyInvestigationRevision`

  * **Method** : `google.cloud.geminicloudassist.v1alpha.InvestigationService.ModifyInvestigationRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminicloudassist.investigationRevisions.modify - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminicloudassist.v1alpha.InvestigationService.ModifyInvestigationRevision" `  




#### `RunInvestigationRevision`

  * **Method** : `google.cloud.geminicloudassist.v1alpha.InvestigationService.RunInvestigationRevision`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminicloudassist.investigationRevisions.run - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminicloudassist.v1alpha.InvestigationService.RunInvestigationRevision" `  




#### `UpdateInvestigation`

  * **Method** : `google.cloud.geminicloudassist.v1alpha.InvestigationService.UpdateInvestigation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminicloudassist.investigations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.geminicloudassist.v1alpha.InvestigationService.UpdateInvestigation" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminicloudassist.investigations.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminicloudassist.investigations.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminicloudassist.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `geminicloudassist.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminicloudassist.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `geminicloudassist.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `a2a.v1.A2AService.CreateTaskPushNotificationConfig`
  * `a2a.v1.A2AService.DeleteTaskPushNotificationConfig`
  * `a2a.v1.A2AService.GetAgentCard`
  * `a2a.v1.A2AService.GetTaskPushNotificationConfig`
  * `a2a.v1.A2AService.ListTaskPushNotificationConfig`
  * `google.cloud.geminicloudassist.v1alpha.McpProxy.AskCloudAssist`
  * `google.cloud.geminicloudassist.v1alpha.McpProxy.AskCloudOperator`
  * `google.cloud.geminicloudassist.v1alpha.McpProxy.DesignInfra`
  * `google.cloud.geminicloudassist.v1alpha.McpProxy.InvestigateIssue`
  * `google.cloud.geminicloudassist.v1alpha.McpProxy.InvokeOperation`
  * `google.cloud.geminicloudassist.v1alpha.McpProxy.OptimizeCosts`
  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.longrunning.Operations.WaitOperation`
  * `lf.a2a.v1.A2AService.CancelTask`
  * `lf.a2a.v1.A2AService.CreateTaskPushNotificationConfig`
  * `lf.a2a.v1.A2AService.DeleteTaskPushNotificationConfig`
  * `lf.a2a.v1.A2AService.GetExtendedAgentCard`
  * `lf.a2a.v1.A2AService.GetTask`
  * `lf.a2a.v1.A2AService.GetTaskPushNotificationConfig`
  * `lf.a2a.v1.A2AService.ListTaskPushNotificationConfigs`
  * `lf.a2a.v1.A2AService.ListTasks`
  * `lf.a2a.v1.A2AService.SendMessage`
  * `lf.a2a.v1.A2AService.SendStreamingMessage`
  * `lf.a2a.v1.A2AService.SubscribeToTask`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
