---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/audit-logging/
title: Audit Logging \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:27.093951+00:00
---

# Audit Logging  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Audit Logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Customer Engagement Suite. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Customer Engagement Suite audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="ces.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Customer Engagement Suite generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.ces.v1.AgentService.ExportApp` (LRO)  
`google.cloud.ces.v1.AgentService.FetchGitStatus`  
`google.cloud.ces.v1.AgentService.GetApp`  
`google.cloud.ces.v1.AgentService.GetBranch`  
`google.cloud.ces.v1.AgentService.GetIamPolicy`  
`google.cloud.ces.v1.AgentService.GetPullRequest`  
`google.cloud.ces.v1.AgentService.ListApps`  
`google.cloud.ces.v1.AgentService.ListBranches`  
`google.cloud.ces.v1.AgentService.ListPullRequests`  
`google.cloud.ces.v1.AgentService.TestIamPermissions`  
`google.cloud.ces.v1beta.AgentService.ExportApp` (LRO)  
`google.cloud.ces.v1beta.AgentService.GetApp`  
`google.cloud.ces.v1beta.AgentService.GetSecuritySettings`  
`google.cloud.ces.v1beta.AgentService.ListApps`  
`google.cloud.ces.v1beta.EvaluationService.TestPersonaVoice`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`lf.a2a.v1.A2AService.GetExtendedAgentCard`  
`ADMIN_WRITE` | `google.cloud.ces.v1.AgentService.CommitAndPushAppConfig`  
`google.cloud.ces.v1.AgentService.CopyApp`  
`google.cloud.ces.v1.AgentService.CreateApp` (LRO)  
`google.cloud.ces.v1.AgentService.CreateBranch`  
`google.cloud.ces.v1.AgentService.CreatePullRequest`  
`google.cloud.ces.v1.AgentService.DeleteApp` (LRO)  
`google.cloud.ces.v1.AgentService.DeleteBranch`  
`google.cloud.ces.v1.AgentService.ImportApp` (LRO)  
`google.cloud.ces.v1.AgentService.ResolveGitOpsConflicts`  
`google.cloud.ces.v1.AgentService.SetIamPolicy`  
`google.cloud.ces.v1.AgentService.SyncAppConfig`  
`google.cloud.ces.v1.AgentService.UpdateApp`  
`google.cloud.ces.v1.AgentService.UpdatePullRequest`  
`google.cloud.ces.v1beta.AgentService.CreateApp` (LRO)  
`google.cloud.ces.v1beta.AgentService.DeleteApp` (LRO)  
`google.cloud.ces.v1beta.AgentService.GenerateAppResource` (LRO)  
`google.cloud.ces.v1beta.AgentService.ImportApp` (LRO)  
`google.cloud.ces.v1beta.AgentService.UpdateApp`  
`google.cloud.ces.v1beta.AgentService.UpdateSecuritySettings`  
`google.cloud.ces.v1beta.AssistantService.ChatAiAssistant`  
`google.cloud.ces.v1beta.AssistantService.RunAssistant`  
`google.cloud.ces.v1beta.EvaluationService.RunEvaluation` (LRO)  
`google.longrunning.Operations.DeleteOperation`  
`DATA_READ` | `google.cloud.ces.v1.AgentService.GetAgent`  
`google.cloud.ces.v1.AgentService.GetAgentContract`  
`google.cloud.ces.v1.AgentService.GetAppVersion`  
`google.cloud.ces.v1.AgentService.GetChangelog`  
`google.cloud.ces.v1.AgentService.GetConversation`  
`google.cloud.ces.v1.AgentService.GetDashboard`  
`google.cloud.ces.v1.AgentService.GetDeployment`  
`google.cloud.ces.v1.AgentService.GetExample`  
`google.cloud.ces.v1.AgentService.GetGuardrail`  
`google.cloud.ces.v1.AgentService.GetLogMetric`  
`google.cloud.ces.v1.AgentService.GetPythonEnvFile`  
`google.cloud.ces.v1.AgentService.GetTool`  
`google.cloud.ces.v1.AgentService.GetToolset`  
`google.cloud.ces.v1.AgentService.GetWorkflow`  
`google.cloud.ces.v1.AgentService.ListAgentContractRevisions`  
`google.cloud.ces.v1.AgentService.ListAgents`  
`google.cloud.ces.v1.AgentService.ListAppVersions`  
`google.cloud.ces.v1.AgentService.ListChangelogs`  
`google.cloud.ces.v1.AgentService.ListConversations`  
`google.cloud.ces.v1.AgentService.ListDashboards`  
`google.cloud.ces.v1.AgentService.ListDeployments`  
`google.cloud.ces.v1.AgentService.ListExamples`  
`google.cloud.ces.v1.AgentService.ListGuardrails`  
`google.cloud.ces.v1.AgentService.ListLogMetrics`  
`google.cloud.ces.v1.AgentService.ListPythonEnvFiles`  
`google.cloud.ces.v1.AgentService.ListTools`  
`google.cloud.ces.v1.AgentService.ListToolsets`  
`google.cloud.ces.v1.AgentService.ListWorkflows`  
`google.cloud.ces.v1.SessionService.CancelAssistantTurn`  
`google.cloud.ces.v1.SessionService.GenerateOnboardingSuggestions`  
`google.cloud.ces.v1.SessionService.StreamChatAiAssistant`  
`google.cloud.ces.v1.ToolService.RetrieveToolSchema`  
`google.cloud.ces.v1.ToolService.RetrieveTools`  
`google.cloud.ces.v1beta.AgentService.GetAgent`  
`google.cloud.ces.v1beta.AgentService.GetAppVersion`  
`google.cloud.ces.v1beta.AgentService.GetChangelog`  
`google.cloud.ces.v1beta.AgentService.GetConversation`  
`google.cloud.ces.v1beta.AgentService.GetDeployment`  
`google.cloud.ces.v1beta.AgentService.GetExample`  
`google.cloud.ces.v1beta.AgentService.GetGuardrail`  
`google.cloud.ces.v1beta.AgentService.GetTool`  
`google.cloud.ces.v1beta.AgentService.GetToolset`  
`google.cloud.ces.v1beta.AgentService.ListAgents`  
`google.cloud.ces.v1beta.AgentService.ListAppVersions`  
`google.cloud.ces.v1beta.AgentService.ListChangelogs`  
`google.cloud.ces.v1beta.AgentService.ListConversations`  
`google.cloud.ces.v1beta.AgentService.ListDeployments`  
`google.cloud.ces.v1beta.AgentService.ListExamples`  
`google.cloud.ces.v1beta.AgentService.ListGuardrails`  
`google.cloud.ces.v1beta.AgentService.ListTools`  
`google.cloud.ces.v1beta.AgentService.ListToolsets`  
`google.cloud.ces.v1beta.AssistantService.GetAssistantSession`  
`google.cloud.ces.v1beta.AssistantService.ListAssistantSessions`  
`google.cloud.ces.v1beta.EvaluationService.ExportEvaluationResults` (LRO)  
`google.cloud.ces.v1beta.EvaluationService.ExportEvaluationRuns` (LRO)  
`google.cloud.ces.v1beta.EvaluationService.ExportEvaluations` (LRO)  
`google.cloud.ces.v1beta.EvaluationService.GenerateEvaluation` (LRO)  
`google.cloud.ces.v1beta.EvaluationService.GetEvaluation`  
`google.cloud.ces.v1beta.EvaluationService.GetEvaluationDataset`  
`google.cloud.ces.v1beta.EvaluationService.GetEvaluationExpectation`  
`google.cloud.ces.v1beta.EvaluationService.GetEvaluationRun`  
`google.cloud.ces.v1beta.EvaluationService.GetScheduledEvaluationRun`  
`google.cloud.ces.v1beta.EvaluationService.ListEvaluationDatasets`  
`google.cloud.ces.v1beta.EvaluationService.ListEvaluationExpectations`  
`google.cloud.ces.v1beta.EvaluationService.ListEvaluationResults`  
`google.cloud.ces.v1beta.EvaluationService.ListEvaluationRuns`  
`google.cloud.ces.v1beta.EvaluationService.ListEvaluations`  
`google.cloud.ces.v1beta.EvaluationService.ListScheduledEvaluationRuns`  
`google.cloud.ces.v1beta.SessionService.CancelAssistantTurn`  
`google.cloud.ces.v1beta.SessionService.GenerateOnboardingSuggestions`  
`google.cloud.ces.v1beta.SessionService.StreamChatAiAssistant`  
`google.cloud.ces.v1beta.ToolService.RetrieveToolSchema`  
`google.cloud.ces.v1beta.ToolService.RetrieveTools`  
`DATA_WRITE` | `google.cloud.ces.v1.AgentService.ActivateAgentContractRevision`  
`google.cloud.ces.v1.AgentService.BatchDeleteConversations` (LRO)  
`google.cloud.ces.v1.AgentService.CreateAgent`  
`google.cloud.ces.v1.AgentService.CreateAppVersion`  
`google.cloud.ces.v1.AgentService.CreateDashboard`  
`google.cloud.ces.v1.AgentService.CreateDeployment`  
`google.cloud.ces.v1.AgentService.CreateExample`  
`google.cloud.ces.v1.AgentService.CreateGuardrail`  
`google.cloud.ces.v1.AgentService.CreateLogMetric`  
`google.cloud.ces.v1.AgentService.CreatePythonEnvFile`  
`google.cloud.ces.v1.AgentService.CreateTool`  
`google.cloud.ces.v1.AgentService.CreateToolset`  
`google.cloud.ces.v1.AgentService.CreateWorkflow`  
`google.cloud.ces.v1.AgentService.DeleteAgent`  
`google.cloud.ces.v1.AgentService.DeleteAppVersion`  
`google.cloud.ces.v1.AgentService.DeleteConversation`  
`google.cloud.ces.v1.AgentService.DeleteDashboard`  
`google.cloud.ces.v1.AgentService.DeleteDeployment`  
`google.cloud.ces.v1.AgentService.DeleteExample`  
`google.cloud.ces.v1.AgentService.DeleteGuardrail`  
`google.cloud.ces.v1.AgentService.DeleteLogMetric`  
`google.cloud.ces.v1.AgentService.DeletePythonEnvFile`  
`google.cloud.ces.v1.AgentService.DeleteTool`  
`google.cloud.ces.v1.AgentService.DeleteToolset`  
`google.cloud.ces.v1.AgentService.DeleteWorkflow`  
`google.cloud.ces.v1.AgentService.RestoreAppVersion` (LRO)  
`google.cloud.ces.v1.AgentService.UpdateAgent`  
`google.cloud.ces.v1.AgentService.UpdateAppVersion`  
`google.cloud.ces.v1.AgentService.UpdateDeployment`  
`google.cloud.ces.v1.AgentService.UpdateExample`  
`google.cloud.ces.v1.AgentService.UpdateGuardrail`  
`google.cloud.ces.v1.AgentService.UpdateTool`  
`google.cloud.ces.v1.AgentService.UpdateToolset`  
`google.cloud.ces.v1.AgentService.ValidateAgent`  
`google.cloud.ces.v1.SessionService.BidiRunSession`  
`google.cloud.ces.v1.SessionService.InitializeSession`  
`google.cloud.ces.v1.SessionService.PublishEvents`  
`google.cloud.ces.v1.SessionService.RunSession`  
`google.cloud.ces.v1.SessionService.StreamRunSession`  
`google.cloud.ces.v1.ToolService.ExecuteTool`  
`google.cloud.ces.v1beta.AgentService.CreateAgent`  
`google.cloud.ces.v1beta.AgentService.CreateAppVersion`  
`google.cloud.ces.v1beta.AgentService.CreateDeployment`  
`google.cloud.ces.v1beta.AgentService.CreateExample`  
`google.cloud.ces.v1beta.AgentService.CreateGuardrail`  
`google.cloud.ces.v1beta.AgentService.CreateTool`  
`google.cloud.ces.v1beta.AgentService.CreateToolset`  
`google.cloud.ces.v1beta.AgentService.DeleteAgent`  
`google.cloud.ces.v1beta.AgentService.DeleteAppVersion`  
`google.cloud.ces.v1beta.AgentService.DeleteConversation`  
`google.cloud.ces.v1beta.AgentService.DeleteDeployment`  
`google.cloud.ces.v1beta.AgentService.DeleteExample`  
`google.cloud.ces.v1beta.AgentService.DeleteGuardrail`  
`google.cloud.ces.v1beta.AgentService.DeleteTool`  
`google.cloud.ces.v1beta.AgentService.DeleteToolset`  
`google.cloud.ces.v1beta.AgentService.RestoreAppVersion` (LRO)  
`google.cloud.ces.v1beta.AgentService.UpdateAgent`  
`google.cloud.ces.v1beta.AgentService.UpdateAppVersion`  
`google.cloud.ces.v1beta.AgentService.UpdateDeployment`  
`google.cloud.ces.v1beta.AgentService.UpdateExample`  
`google.cloud.ces.v1beta.AgentService.UpdateGuardrail`  
`google.cloud.ces.v1beta.AgentService.UpdateTool`  
`google.cloud.ces.v1beta.AgentService.UpdateToolset`  
`google.cloud.ces.v1beta.AssistantService.CreateAssistantSession`  
`google.cloud.ces.v1beta.AssistantService.DeleteAssistantSession`  
`google.cloud.ces.v1beta.EvaluationService.CreateEvaluation`  
`google.cloud.ces.v1beta.EvaluationService.CreateEvaluationDataset`  
`google.cloud.ces.v1beta.EvaluationService.CreateEvaluationExpectation`  
`google.cloud.ces.v1beta.EvaluationService.CreateScheduledEvaluationRun`  
`google.cloud.ces.v1beta.EvaluationService.DeleteEvaluation`  
`google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationDataset`  
`google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationExpectation`  
`google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationRun` (LRO)  
`google.cloud.ces.v1beta.EvaluationService.DeleteScheduledEvaluationRun`  
`google.cloud.ces.v1beta.EvaluationService.ImportEvaluations` (LRO)  
`google.cloud.ces.v1beta.EvaluationService.RunEvaluationResultMetrics` (LRO)  
`google.cloud.ces.v1beta.EvaluationService.UpdateEvaluation`  
`google.cloud.ces.v1beta.EvaluationService.UpdateEvaluationDataset`  
`google.cloud.ces.v1beta.EvaluationService.UpdateEvaluationExpectation`  
`google.cloud.ces.v1beta.EvaluationService.UpdateScheduledEvaluationRun`  
`google.cloud.ces.v1beta.EvaluationService.UploadEvaluationAudio`  
`google.cloud.ces.v1beta.SessionService.BidiRunSession`  
`google.cloud.ces.v1beta.SessionService.RunSession`  
`google.cloud.ces.v1beta.SessionService.StreamRunSession`  
`google.cloud.ces.v1beta.ToolService.ExecuteTool`  
`lf.a2a.v1.A2AService.SendMessage`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Customer Engagement Suite.

### `google.cloud.ces.v1.AgentService`

The following audit logs are associated with methods belonging to `google.cloud.ces.v1.AgentService`.

#### `ActivateAgentContractRevision`

  * **Method** : `google.cloud.ces.v1.AgentService.ActivateAgentContractRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.agentContract.activate - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ActivateAgentContractRevision" `  




#### `BatchDeleteConversations`

  * **Method** : `google.cloud.ces.v1.AgentService.BatchDeleteConversations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.conversations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.BatchDeleteConversations" `  




#### `CommitAndPushAppConfig`

  * **Method** : `google.cloud.ces.v1.AgentService.CommitAndPushAppConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.apps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.CommitAndPushAppConfig" `  




#### `CopyApp`

  * **Method** : `google.cloud.ces.v1.AgentService.CopyApp`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.apps.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.CopyApp" `  




#### `CreateAgent`

  * **Method** : `google.cloud.ces.v1.AgentService.CreateAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.agents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.CreateAgent" `  




#### `CreateApp`

  * **Method** : `google.cloud.ces.v1.AgentService.CreateApp`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.apps.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.CreateApp" `  




#### `CreateAppVersion`

  * **Method** : `google.cloud.ces.v1.AgentService.CreateAppVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.appVersions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.CreateAppVersion" `  




#### `CreateBranch`

  * **Method** : `google.cloud.ces.v1.AgentService.CreateBranch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.apps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.CreateBranch" `  




#### `CreateDashboard`

  * **Method** : `google.cloud.ces.v1.AgentService.CreateDashboard`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.dashboards.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.CreateDashboard" `  




#### `CreateDeployment`

  * **Method** : `google.cloud.ces.v1.AgentService.CreateDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.deployments.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.CreateDeployment" `  




#### `CreateExample`

  * **Method** : `google.cloud.ces.v1.AgentService.CreateExample`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.examples.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.CreateExample" `  




#### `CreateGuardrail`

  * **Method** : `google.cloud.ces.v1.AgentService.CreateGuardrail`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.guardrails.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.CreateGuardrail" `  




#### `CreateLogMetric`

  * **Method** : `google.cloud.ces.v1.AgentService.CreateLogMetric`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.logMetrics.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.CreateLogMetric" `  




#### `CreatePullRequest`

  * **Method** : `google.cloud.ces.v1.AgentService.CreatePullRequest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.apps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.CreatePullRequest" `  




#### `CreatePythonEnvFile`

  * **Method** : `google.cloud.ces.v1.AgentService.CreatePythonEnvFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.pythonEnvFiles.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.CreatePythonEnvFile" `  




#### `CreateTool`

  * **Method** : `google.cloud.ces.v1.AgentService.CreateTool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.tools.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.CreateTool" `  




#### `CreateToolset`

  * **Method** : `google.cloud.ces.v1.AgentService.CreateToolset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.toolsets.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.CreateToolset" `  




#### `CreateWorkflow`

  * **Method** : `google.cloud.ces.v1.AgentService.CreateWorkflow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.workflows.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.CreateWorkflow" `  




#### `DeleteAgent`

  * **Method** : `google.cloud.ces.v1.AgentService.DeleteAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.agents.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.DeleteAgent" `  




#### `DeleteApp`

  * **Method** : `google.cloud.ces.v1.AgentService.DeleteApp`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.apps.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.DeleteApp" `  




#### `DeleteAppVersion`

  * **Method** : `google.cloud.ces.v1.AgentService.DeleteAppVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.appVersions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.DeleteAppVersion" `  




#### `DeleteBranch`

  * **Method** : `google.cloud.ces.v1.AgentService.DeleteBranch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.branches.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.DeleteBranch" `  




#### `DeleteConversation`

  * **Method** : `google.cloud.ces.v1.AgentService.DeleteConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.conversations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.DeleteConversation" `  




#### `DeleteDashboard`

  * **Method** : `google.cloud.ces.v1.AgentService.DeleteDashboard`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.dashboards.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.DeleteDashboard" `  




#### `DeleteDeployment`

  * **Method** : `google.cloud.ces.v1.AgentService.DeleteDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.deployments.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.DeleteDeployment" `  




#### `DeleteExample`

  * **Method** : `google.cloud.ces.v1.AgentService.DeleteExample`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.examples.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.DeleteExample" `  




#### `DeleteGuardrail`

  * **Method** : `google.cloud.ces.v1.AgentService.DeleteGuardrail`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.guardrails.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.DeleteGuardrail" `  




#### `DeleteLogMetric`

  * **Method** : `google.cloud.ces.v1.AgentService.DeleteLogMetric`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.logMetrics.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.DeleteLogMetric" `  




#### `DeletePythonEnvFile`

  * **Method** : `google.cloud.ces.v1.AgentService.DeletePythonEnvFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.pythonEnvFiles.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.DeletePythonEnvFile" `  




#### `DeleteTool`

  * **Method** : `google.cloud.ces.v1.AgentService.DeleteTool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.tools.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.DeleteTool" `  




#### `DeleteToolset`

  * **Method** : `google.cloud.ces.v1.AgentService.DeleteToolset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.toolsets.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.DeleteToolset" `  




#### `DeleteWorkflow`

  * **Method** : `google.cloud.ces.v1.AgentService.DeleteWorkflow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.workflows.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.DeleteWorkflow" `  




#### `ExportApp`

  * **Method** : `google.cloud.ces.v1.AgentService.ExportApp`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.apps.export - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ExportApp" `  




#### `FetchGitStatus`

  * **Method** : `google.cloud.ces.v1.AgentService.FetchGitStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.apps.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.FetchGitStatus" `  




#### `GetAgent`

  * **Method** : `google.cloud.ces.v1.AgentService.GetAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.agents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.GetAgent" `  




#### `GetAgentContract`

  * **Method** : `google.cloud.ces.v1.AgentService.GetAgentContract`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.agentContract.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.GetAgentContract" `  




#### `GetApp`

  * **Method** : `google.cloud.ces.v1.AgentService.GetApp`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.apps.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.GetApp" `  




#### `GetAppVersion`

  * **Method** : `google.cloud.ces.v1.AgentService.GetAppVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.appVersions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.GetAppVersion" `  




#### `GetBranch`

  * **Method** : `google.cloud.ces.v1.AgentService.GetBranch`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.branches.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.GetBranch" `  




#### `GetChangelog`

  * **Method** : `google.cloud.ces.v1.AgentService.GetChangelog`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.changelogs.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.GetChangelog" `  




#### `GetConversation`

  * **Method** : `google.cloud.ces.v1.AgentService.GetConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.conversations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.GetConversation" `  




#### `GetDashboard`

  * **Method** : `google.cloud.ces.v1.AgentService.GetDashboard`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.dashboards.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.GetDashboard" `  




#### `GetDeployment`

  * **Method** : `google.cloud.ces.v1.AgentService.GetDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.deployments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.GetDeployment" `  




#### `GetExample`

  * **Method** : `google.cloud.ces.v1.AgentService.GetExample`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.examples.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.GetExample" `  




#### `GetGuardrail`

  * **Method** : `google.cloud.ces.v1.AgentService.GetGuardrail`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.guardrails.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.GetGuardrail" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.ces.v1.AgentService.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.apps.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.GetIamPolicy" `  




#### `GetLogMetric`

  * **Method** : `google.cloud.ces.v1.AgentService.GetLogMetric`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.logMetrics.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.GetLogMetric" `  




#### `GetPullRequest`

  * **Method** : `google.cloud.ces.v1.AgentService.GetPullRequest`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.pullRequests.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.GetPullRequest" `  




#### `GetPythonEnvFile`

  * **Method** : `google.cloud.ces.v1.AgentService.GetPythonEnvFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.pythonEnvFiles.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.GetPythonEnvFile" `  




#### `GetTool`

  * **Method** : `google.cloud.ces.v1.AgentService.GetTool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.tools.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.GetTool" `  




#### `GetToolset`

  * **Method** : `google.cloud.ces.v1.AgentService.GetToolset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.toolsets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.GetToolset" `  




#### `GetWorkflow`

  * **Method** : `google.cloud.ces.v1.AgentService.GetWorkflow`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.workflows.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.GetWorkflow" `  




#### `ImportApp`

  * **Method** : `google.cloud.ces.v1.AgentService.ImportApp`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.apps.import - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ImportApp" `  




#### `ListAgentContractRevisions`

  * **Method** : `google.cloud.ces.v1.AgentService.ListAgentContractRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.agentContract.listRevisions - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ListAgentContractRevisions" `  




#### `ListAgents`

  * **Method** : `google.cloud.ces.v1.AgentService.ListAgents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.agents.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ListAgents" `  




#### `ListAppVersions`

  * **Method** : `google.cloud.ces.v1.AgentService.ListAppVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.appVersions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ListAppVersions" `  




#### `ListApps`

  * **Method** : `google.cloud.ces.v1.AgentService.ListApps`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.apps.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ListApps" `  




#### `ListBranches`

  * **Method** : `google.cloud.ces.v1.AgentService.ListBranches`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.branches.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ListBranches" `  




#### `ListChangelogs`

  * **Method** : `google.cloud.ces.v1.AgentService.ListChangelogs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.changelogs.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ListChangelogs" `  




#### `ListConversations`

  * **Method** : `google.cloud.ces.v1.AgentService.ListConversations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.conversations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ListConversations" `  




#### `ListDashboards`

  * **Method** : `google.cloud.ces.v1.AgentService.ListDashboards`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.dashboards.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ListDashboards" `  




#### `ListDeployments`

  * **Method** : `google.cloud.ces.v1.AgentService.ListDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.deployments.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ListDeployments" `  




#### `ListExamples`

  * **Method** : `google.cloud.ces.v1.AgentService.ListExamples`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.examples.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ListExamples" `  




#### `ListGuardrails`

  * **Method** : `google.cloud.ces.v1.AgentService.ListGuardrails`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.guardrails.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ListGuardrails" `  




#### `ListLogMetrics`

  * **Method** : `google.cloud.ces.v1.AgentService.ListLogMetrics`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.logMetrics.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ListLogMetrics" `  




#### `ListPullRequests`

  * **Method** : `google.cloud.ces.v1.AgentService.ListPullRequests`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.pullRequests.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ListPullRequests" `  




#### `ListPythonEnvFiles`

  * **Method** : `google.cloud.ces.v1.AgentService.ListPythonEnvFiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.pythonEnvFiles.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ListPythonEnvFiles" `  




#### `ListTools`

  * **Method** : `google.cloud.ces.v1.AgentService.ListTools`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.tools.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ListTools" `  




#### `ListToolsets`

  * **Method** : `google.cloud.ces.v1.AgentService.ListToolsets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.toolsets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ListToolsets" `  




#### `ListWorkflows`

  * **Method** : `google.cloud.ces.v1.AgentService.ListWorkflows`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.workflows.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ListWorkflows" `  




#### `ResolveGitOpsConflicts`

  * **Method** : `google.cloud.ces.v1.AgentService.ResolveGitOpsConflicts`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.apps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ResolveGitOpsConflicts" `  




#### `RestoreAppVersion`

  * **Method** : `google.cloud.ces.v1.AgentService.RestoreAppVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.appVersions.restore - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.RestoreAppVersion" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.ces.v1.AgentService.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.apps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.SetIamPolicy" `  




#### `SyncAppConfig`

  * **Method** : `google.cloud.ces.v1.AgentService.SyncAppConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.apps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.SyncAppConfig" `  




#### `TestIamPermissions`

  * **Method** : `google.cloud.ces.v1.AgentService.TestIamPermissions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.apps.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.TestIamPermissions" `  




#### `UpdateAgent`

  * **Method** : `google.cloud.ces.v1.AgentService.UpdateAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.agents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.UpdateAgent" `  




#### `UpdateApp`

  * **Method** : `google.cloud.ces.v1.AgentService.UpdateApp`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.apps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.UpdateApp" `  




#### `UpdateAppVersion`

  * **Method** : `google.cloud.ces.v1.AgentService.UpdateAppVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.appVersions.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.UpdateAppVersion" `  




#### `UpdateDeployment`

  * **Method** : `google.cloud.ces.v1.AgentService.UpdateDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.deployments.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.UpdateDeployment" `  




#### `UpdateExample`

  * **Method** : `google.cloud.ces.v1.AgentService.UpdateExample`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.examples.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.UpdateExample" `  




#### `UpdateGuardrail`

  * **Method** : `google.cloud.ces.v1.AgentService.UpdateGuardrail`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.guardrails.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.UpdateGuardrail" `  




#### `UpdatePullRequest`

  * **Method** : `google.cloud.ces.v1.AgentService.UpdatePullRequest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.pullRequests.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.UpdatePullRequest" `  




#### `UpdateTool`

  * **Method** : `google.cloud.ces.v1.AgentService.UpdateTool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.tools.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.UpdateTool" `  




#### `UpdateToolset`

  * **Method** : `google.cloud.ces.v1.AgentService.UpdateToolset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.toolsets.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.UpdateToolset" `  




#### `ValidateAgent`

  * **Method** : `google.cloud.ces.v1.AgentService.ValidateAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.agents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.AgentService.ValidateAgent" `  




### `google.cloud.ces.v1.SessionService`

The following audit logs are associated with methods belonging to `google.cloud.ces.v1.SessionService`.

#### `BidiRunSession`

  * **Method** : `google.cloud.ces.v1.SessionService.BidiRunSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.sessions.bidiRunSession - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.SessionService.BidiRunSession" `  




#### `CancelAssistantTurn`

  * **Method** : `google.cloud.ces.v1.SessionService.CancelAssistantTurn`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.assistantSessions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.SessionService.CancelAssistantTurn" `  




#### `GenerateOnboardingSuggestions`

  * **Method** : `google.cloud.ces.v1.SessionService.GenerateOnboardingSuggestions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.assistantSessions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.SessionService.GenerateOnboardingSuggestions" `  




#### `InitializeSession`

  * **Method** : `google.cloud.ces.v1.SessionService.InitializeSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.sessions.runSession - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.SessionService.InitializeSession" `  




#### `PublishEvents`

  * **Method** : `google.cloud.ces.v1.SessionService.PublishEvents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.sessions.runSession - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.SessionService.PublishEvents" `  




#### `RunSession`

  * **Method** : `google.cloud.ces.v1.SessionService.RunSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.sessions.runSession - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.SessionService.RunSession" `  




#### `StreamChatAiAssistant`

  * **Method** : `google.cloud.ces.v1.SessionService.StreamChatAiAssistant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.assistantSessions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.SessionService.StreamChatAiAssistant" `  




#### `StreamRunSession`

  * **Method** : `google.cloud.ces.v1.SessionService.StreamRunSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.sessions.runSession - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.SessionService.StreamRunSession" `  




### `google.cloud.ces.v1.ToolService`

The following audit logs are associated with methods belonging to `google.cloud.ces.v1.ToolService`.

#### `ExecuteTool`

  * **Method** : `google.cloud.ces.v1.ToolService.ExecuteTool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.tools.execute - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.ToolService.ExecuteTool" `  




#### `RetrieveToolSchema`

  * **Method** : `google.cloud.ces.v1.ToolService.RetrieveToolSchema`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.tools.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.ToolService.RetrieveToolSchema" `  




#### `RetrieveTools`

  * **Method** : `google.cloud.ces.v1.ToolService.RetrieveTools`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.toolsets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1.ToolService.RetrieveTools" `  




### `google.cloud.ces.v1beta.AgentService`

The following audit logs are associated with methods belonging to `google.cloud.ces.v1beta.AgentService`.

#### `CreateAgent`

  * **Method** : `google.cloud.ces.v1beta.AgentService.CreateAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.agents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.CreateAgent" `  




#### `CreateApp`

  * **Method** : `google.cloud.ces.v1beta.AgentService.CreateApp`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.apps.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.CreateApp" `  




#### `CreateAppVersion`

  * **Method** : `google.cloud.ces.v1beta.AgentService.CreateAppVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.appVersions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.CreateAppVersion" `  




#### `CreateDeployment`

  * **Method** : `google.cloud.ces.v1beta.AgentService.CreateDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.deployments.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.CreateDeployment" `  




#### `CreateExample`

  * **Method** : `google.cloud.ces.v1beta.AgentService.CreateExample`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.examples.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.CreateExample" `  




#### `CreateGuardrail`

  * **Method** : `google.cloud.ces.v1beta.AgentService.CreateGuardrail`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.guardrails.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.CreateGuardrail" `  




#### `CreateTool`

  * **Method** : `google.cloud.ces.v1beta.AgentService.CreateTool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.tools.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.CreateTool" `  




#### `CreateToolset`

  * **Method** : `google.cloud.ces.v1beta.AgentService.CreateToolset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.toolsets.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.CreateToolset" `  




#### `DeleteAgent`

  * **Method** : `google.cloud.ces.v1beta.AgentService.DeleteAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.agents.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.DeleteAgent" `  




#### `DeleteApp`

  * **Method** : `google.cloud.ces.v1beta.AgentService.DeleteApp`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.apps.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.DeleteApp" `  




#### `DeleteAppVersion`

  * **Method** : `google.cloud.ces.v1beta.AgentService.DeleteAppVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.appVersions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.DeleteAppVersion" `  




#### `DeleteConversation`

  * **Method** : `google.cloud.ces.v1beta.AgentService.DeleteConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.conversations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.DeleteConversation" `  




#### `DeleteDeployment`

  * **Method** : `google.cloud.ces.v1beta.AgentService.DeleteDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.deployments.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.DeleteDeployment" `  




#### `DeleteExample`

  * **Method** : `google.cloud.ces.v1beta.AgentService.DeleteExample`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.examples.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.DeleteExample" `  




#### `DeleteGuardrail`

  * **Method** : `google.cloud.ces.v1beta.AgentService.DeleteGuardrail`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.guardrails.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.DeleteGuardrail" `  




#### `DeleteTool`

  * **Method** : `google.cloud.ces.v1beta.AgentService.DeleteTool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.tools.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.DeleteTool" `  




#### `DeleteToolset`

  * **Method** : `google.cloud.ces.v1beta.AgentService.DeleteToolset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.toolsets.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.DeleteToolset" `  




#### `ExportApp`

  * **Method** : `google.cloud.ces.v1beta.AgentService.ExportApp`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.apps.export - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.ExportApp" `  




#### `GenerateAppResource`

  * **Method** : `google.cloud.ces.v1beta.AgentService.GenerateAppResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.apps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.GenerateAppResource" `  




#### `GetAgent`

  * **Method** : `google.cloud.ces.v1beta.AgentService.GetAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.agents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.GetAgent" `  




#### `GetApp`

  * **Method** : `google.cloud.ces.v1beta.AgentService.GetApp`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.apps.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.GetApp" `  




#### `GetAppVersion`

  * **Method** : `google.cloud.ces.v1beta.AgentService.GetAppVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.appVersions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.GetAppVersion" `  




#### `GetChangelog`

  * **Method** : `google.cloud.ces.v1beta.AgentService.GetChangelog`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.changelogs.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.GetChangelog" `  




#### `GetConversation`

  * **Method** : `google.cloud.ces.v1beta.AgentService.GetConversation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.conversations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.GetConversation" `  




#### `GetDeployment`

  * **Method** : `google.cloud.ces.v1beta.AgentService.GetDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.deployments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.GetDeployment" `  




#### `GetExample`

  * **Method** : `google.cloud.ces.v1beta.AgentService.GetExample`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.examples.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.GetExample" `  




#### `GetGuardrail`

  * **Method** : `google.cloud.ces.v1beta.AgentService.GetGuardrail`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.guardrails.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.GetGuardrail" `  




#### `GetSecuritySettings`

  * **Method** : `google.cloud.ces.v1beta.AgentService.GetSecuritySettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.securitySettings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.GetSecuritySettings" `  




#### `GetTool`

  * **Method** : `google.cloud.ces.v1beta.AgentService.GetTool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.tools.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.GetTool" `  




#### `GetToolset`

  * **Method** : `google.cloud.ces.v1beta.AgentService.GetToolset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.toolsets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.GetToolset" `  




#### `ImportApp`

  * **Method** : `google.cloud.ces.v1beta.AgentService.ImportApp`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.apps.import - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.ImportApp" `  




#### `ListAgents`

  * **Method** : `google.cloud.ces.v1beta.AgentService.ListAgents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.agents.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.ListAgents" `  




#### `ListAppVersions`

  * **Method** : `google.cloud.ces.v1beta.AgentService.ListAppVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.appVersions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.ListAppVersions" `  




#### `ListApps`

  * **Method** : `google.cloud.ces.v1beta.AgentService.ListApps`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.apps.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.ListApps" `  




#### `ListChangelogs`

  * **Method** : `google.cloud.ces.v1beta.AgentService.ListChangelogs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.changelogs.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.ListChangelogs" `  




#### `ListConversations`

  * **Method** : `google.cloud.ces.v1beta.AgentService.ListConversations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.conversations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.ListConversations" `  




#### `ListDeployments`

  * **Method** : `google.cloud.ces.v1beta.AgentService.ListDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.deployments.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.ListDeployments" `  




#### `ListExamples`

  * **Method** : `google.cloud.ces.v1beta.AgentService.ListExamples`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.examples.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.ListExamples" `  




#### `ListGuardrails`

  * **Method** : `google.cloud.ces.v1beta.AgentService.ListGuardrails`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.guardrails.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.ListGuardrails" `  




#### `ListTools`

  * **Method** : `google.cloud.ces.v1beta.AgentService.ListTools`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.tools.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.ListTools" `  




#### `ListToolsets`

  * **Method** : `google.cloud.ces.v1beta.AgentService.ListToolsets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.toolsets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.ListToolsets" `  




#### `RestoreAppVersion`

  * **Method** : `google.cloud.ces.v1beta.AgentService.RestoreAppVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.appVersions.restore - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.RestoreAppVersion" `  




#### `UpdateAgent`

  * **Method** : `google.cloud.ces.v1beta.AgentService.UpdateAgent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.agents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.UpdateAgent" `  




#### `UpdateApp`

  * **Method** : `google.cloud.ces.v1beta.AgentService.UpdateApp`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.apps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.UpdateApp" `  




#### `UpdateAppVersion`

  * **Method** : `google.cloud.ces.v1beta.AgentService.UpdateAppVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.appVersions.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.UpdateAppVersion" `  




#### `UpdateDeployment`

  * **Method** : `google.cloud.ces.v1beta.AgentService.UpdateDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.deployments.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.UpdateDeployment" `  




#### `UpdateExample`

  * **Method** : `google.cloud.ces.v1beta.AgentService.UpdateExample`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.examples.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.UpdateExample" `  




#### `UpdateGuardrail`

  * **Method** : `google.cloud.ces.v1beta.AgentService.UpdateGuardrail`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.guardrails.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.UpdateGuardrail" `  




#### `UpdateSecuritySettings`

  * **Method** : `google.cloud.ces.v1beta.AgentService.UpdateSecuritySettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.securitySettings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.UpdateSecuritySettings" `  




#### `UpdateTool`

  * **Method** : `google.cloud.ces.v1beta.AgentService.UpdateTool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.tools.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.UpdateTool" `  




#### `UpdateToolset`

  * **Method** : `google.cloud.ces.v1beta.AgentService.UpdateToolset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.toolsets.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AgentService.UpdateToolset" `  




### `google.cloud.ces.v1beta.AssistantService`

The following audit logs are associated with methods belonging to `google.cloud.ces.v1beta.AssistantService`.

#### `ChatAiAssistant`

  * **Method** : `google.cloud.ces.v1beta.AssistantService.ChatAiAssistant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.apps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AssistantService.ChatAiAssistant" `  




#### `CreateAssistantSession`

  * **Method** : `google.cloud.ces.v1beta.AssistantService.CreateAssistantSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.assistantSessions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AssistantService.CreateAssistantSession" `  




#### `DeleteAssistantSession`

  * **Method** : `google.cloud.ces.v1beta.AssistantService.DeleteAssistantSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.assistantSessions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AssistantService.DeleteAssistantSession" `  




#### `GetAssistantSession`

  * **Method** : `google.cloud.ces.v1beta.AssistantService.GetAssistantSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.assistantSessions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AssistantService.GetAssistantSession" `  




#### `ListAssistantSessions`

  * **Method** : `google.cloud.ces.v1beta.AssistantService.ListAssistantSessions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.assistantSessions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AssistantService.ListAssistantSessions" `  




#### `RunAssistant`

  * **Method** : `google.cloud.ces.v1beta.AssistantService.RunAssistant`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.apps.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.AssistantService.RunAssistant" `  




### `google.cloud.ces.v1beta.EvaluationService`

The following audit logs are associated with methods belonging to `google.cloud.ces.v1beta.EvaluationService`.

#### `CreateEvaluation`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.CreateEvaluation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.CreateEvaluation" `  




#### `CreateEvaluationDataset`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.CreateEvaluationDataset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluationDatasets.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.CreateEvaluationDataset" `  




#### `CreateEvaluationExpectation`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.CreateEvaluationExpectation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluationExpectations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.CreateEvaluationExpectation" `  




#### `CreateScheduledEvaluationRun`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.CreateScheduledEvaluationRun`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.scheduledEvaluationRuns.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.CreateScheduledEvaluationRun" `  




#### `DeleteEvaluation`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.DeleteEvaluation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.DeleteEvaluation" `  




#### `DeleteEvaluationDataset`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationDataset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluationDatasets.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationDataset" `  




#### `DeleteEvaluationExpectation`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationExpectation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluationExpectations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationExpectation" `  




#### `DeleteEvaluationRun`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationRun`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluationRuns.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationRun" `  




#### `DeleteScheduledEvaluationRun`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.DeleteScheduledEvaluationRun`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.scheduledEvaluationRuns.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.DeleteScheduledEvaluationRun" `  




#### `ExportEvaluationResults`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.ExportEvaluationResults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluations.export - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.ExportEvaluationResults" `  




#### `ExportEvaluationRuns`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.ExportEvaluationRuns`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluationRuns.get - DATA_READ`
    * `ces.evaluations.export - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.ExportEvaluationRuns" `  




#### `ExportEvaluations`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.ExportEvaluations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluations.export - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.ExportEvaluations" `  




#### `GenerateEvaluation`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.GenerateEvaluation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.conversations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.GenerateEvaluation" `  




#### `GetEvaluation`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.GetEvaluation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.GetEvaluation" `  




#### `GetEvaluationDataset`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.GetEvaluationDataset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluationDatasets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.GetEvaluationDataset" `  




#### `GetEvaluationExpectation`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.GetEvaluationExpectation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluationExpectations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.GetEvaluationExpectation" `  




#### `GetEvaluationRun`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.GetEvaluationRun`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluationRuns.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.GetEvaluationRun" `  




#### `GetScheduledEvaluationRun`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.GetScheduledEvaluationRun`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.scheduledEvaluationRuns.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.GetScheduledEvaluationRun" `  




#### `ImportEvaluations`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.ImportEvaluations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluations.create - DATA_WRITE`
    * `ces.evaluations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.ImportEvaluations" `  




#### `ListEvaluationDatasets`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.ListEvaluationDatasets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluationDatasets.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.ListEvaluationDatasets" `  




#### `ListEvaluationExpectations`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.ListEvaluationExpectations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluationExpectations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.ListEvaluationExpectations" `  




#### `ListEvaluationResults`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.ListEvaluationResults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluationResults.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.ListEvaluationResults" `  




#### `ListEvaluationRuns`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.ListEvaluationRuns`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluationRuns.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.ListEvaluationRuns" `  




#### `ListEvaluations`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.ListEvaluations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.ListEvaluations" `  




#### `ListScheduledEvaluationRuns`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.ListScheduledEvaluationRuns`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.scheduledEvaluationRuns.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.ListScheduledEvaluationRuns" `  




#### `RunEvaluation`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.RunEvaluation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.apps.runEvaluation - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.RunEvaluation" `  




#### `RunEvaluationResultMetrics`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.RunEvaluationResultMetrics`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluationResults.runEvaluationResultMetrics - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.RunEvaluationResultMetrics" `  




#### `TestPersonaVoice`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.TestPersonaVoice`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.apps.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.TestPersonaVoice" `  




#### `UpdateEvaluation`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.UpdateEvaluation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.UpdateEvaluation" `  




#### `UpdateEvaluationDataset`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.UpdateEvaluationDataset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluationDatasets.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.UpdateEvaluationDataset" `  




#### `UpdateEvaluationExpectation`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.UpdateEvaluationExpectation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluationExpectations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.UpdateEvaluationExpectation" `  




#### `UpdateScheduledEvaluationRun`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.UpdateScheduledEvaluationRun`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.scheduledEvaluationRuns.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.UpdateScheduledEvaluationRun" `  




#### `UploadEvaluationAudio`

  * **Method** : `google.cloud.ces.v1beta.EvaluationService.UploadEvaluationAudio`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.evaluations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.EvaluationService.UploadEvaluationAudio" `  




### `google.cloud.ces.v1beta.SessionService`

The following audit logs are associated with methods belonging to `google.cloud.ces.v1beta.SessionService`.

#### `BidiRunSession`

  * **Method** : `google.cloud.ces.v1beta.SessionService.BidiRunSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.sessions.bidiRunSession - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.SessionService.BidiRunSession" `  




#### `CancelAssistantTurn`

  * **Method** : `google.cloud.ces.v1beta.SessionService.CancelAssistantTurn`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.assistantSessions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.SessionService.CancelAssistantTurn" `  




#### `GenerateOnboardingSuggestions`

  * **Method** : `google.cloud.ces.v1beta.SessionService.GenerateOnboardingSuggestions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.assistantSessions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.SessionService.GenerateOnboardingSuggestions" `  




#### `RunSession`

  * **Method** : `google.cloud.ces.v1beta.SessionService.RunSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.sessions.runSession - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.SessionService.RunSession" `  




#### `StreamChatAiAssistant`

  * **Method** : `google.cloud.ces.v1beta.SessionService.StreamChatAiAssistant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.assistantSessions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.SessionService.StreamChatAiAssistant" `  




#### `StreamRunSession`

  * **Method** : `google.cloud.ces.v1beta.SessionService.StreamRunSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.sessions.runSession - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.SessionService.StreamRunSession" `  




### `google.cloud.ces.v1beta.ToolService`

The following audit logs are associated with methods belonging to `google.cloud.ces.v1beta.ToolService`.

#### `ExecuteTool`

  * **Method** : `google.cloud.ces.v1beta.ToolService.ExecuteTool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.tools.execute - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.ToolService.ExecuteTool" `  




#### `RetrieveToolSchema`

  * **Method** : `google.cloud.ces.v1beta.ToolService.RetrieveToolSchema`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.tools.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.ToolService.RetrieveToolSchema" `  




#### `RetrieveTools`

  * **Method** : `google.cloud.ces.v1beta.ToolService.RetrieveTools`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.toolsets.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.ces.v1beta.ToolService.RetrieveTools" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `ces.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




### `lf.a2a.v1.A2AService`

The following audit logs are associated with methods belonging to `lf.a2a.v1.A2AService`.

#### `GetExtendedAgentCard`

  * **Method** : `lf.a2a.v1.A2AService.GetExtendedAgentCard`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.apps.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="lf.a2a.v1.A2AService.GetExtendedAgentCard" `  




#### `SendMessage`

  * **Method** : `lf.a2a.v1.A2AService.SendMessage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `ces.sessions.runSession - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="lf.a2a.v1.A2AService.SendMessage" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.ces.v1.SessionService.GeneratePrompts`
  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.longrunning.Operations.WaitOperation`
  * `lf.a2a.v1.A2AService.CancelTask`
  * `lf.a2a.v1.A2AService.CreateTaskPushNotificationConfig`
  * `lf.a2a.v1.A2AService.DeleteTaskPushNotificationConfig`
  * `lf.a2a.v1.A2AService.GetTask`
  * `lf.a2a.v1.A2AService.GetTaskPushNotificationConfig`
  * `lf.a2a.v1.A2AService.ListTaskPushNotificationConfigs`
  * `lf.a2a.v1.A2AService.ListTasks`
  * `lf.a2a.v1.A2AService.SendStreamingMessage`
  * `lf.a2a.v1.A2AService.SubscribeToTask`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
