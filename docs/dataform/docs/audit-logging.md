---
url: https://docs.cloud.google.com/dataform/docs/audit-logging/
title: Dataform audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:47.746167+00:00
---

# Dataform audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  Dataform audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Dataform. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Dataform audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="dataform.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Dataform generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.dataform.v1.Dataform.ComputeRepositoryAccessTokenStatus`  
`google.cloud.dataform.v1.Dataform.FetchRemoteBranches`  
`google.cloud.dataform.v1.Dataform.GetFolder`  
`google.cloud.dataform.v1.Dataform.GetIamPolicy`  
`google.cloud.dataform.v1.Dataform.GetReleaseConfig`  
`google.cloud.dataform.v1.Dataform.GetRepository`  
`google.cloud.dataform.v1.Dataform.GetTeamFolder`  
`google.cloud.dataform.v1.Dataform.GetWorkflowConfig`  
`google.cloud.dataform.v1.Dataform.GetWorkspace`  
`google.cloud.dataform.v1.Dataform.ListReleaseConfigs`  
`google.cloud.dataform.v1.Dataform.ListRepositories`  
`google.cloud.dataform.v1.Dataform.ListWorkflowConfigs`  
`google.cloud.dataform.v1.Dataform.ListWorkspaces`  
`google.cloud.dataform.v1.Dataform.QueryFolderContents`  
`google.cloud.dataform.v1.Dataform.QueryTeamFolderContents`  
`google.cloud.dataform.v1beta1.Dataform.ComputeRepositoryAccessTokenStatus`  
`google.cloud.dataform.v1beta1.Dataform.FetchRemoteBranches`  
`google.cloud.dataform.v1beta1.Dataform.GetFolder`  
`google.cloud.dataform.v1beta1.Dataform.GetIamPolicy`  
`google.cloud.dataform.v1beta1.Dataform.GetReleaseConfig`  
`google.cloud.dataform.v1beta1.Dataform.GetRepository`  
`google.cloud.dataform.v1beta1.Dataform.GetTeamFolder`  
`google.cloud.dataform.v1beta1.Dataform.GetWorkflowConfig`  
`google.cloud.dataform.v1beta1.Dataform.GetWorkspace`  
`google.cloud.dataform.v1beta1.Dataform.ListReleaseConfigs`  
`google.cloud.dataform.v1beta1.Dataform.ListRepositories`  
`google.cloud.dataform.v1beta1.Dataform.ListWorkflowConfigs`  
`google.cloud.dataform.v1beta1.Dataform.ListWorkspaces`  
`google.cloud.dataform.v1beta1.Dataform.QueryFolderContents`  
`google.cloud.dataform.v1beta1.Dataform.QueryTeamFolderContents`  
`google.iam.v1.IAMPolicy.GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.dataform.v1.Dataform.CreateFolder`  
`google.cloud.dataform.v1.Dataform.CreateReleaseConfig`  
`google.cloud.dataform.v1.Dataform.CreateRepository`  
`google.cloud.dataform.v1.Dataform.CreateTeamFolder`  
`google.cloud.dataform.v1.Dataform.CreateWorkflowConfig`  
`google.cloud.dataform.v1.Dataform.CreateWorkspace`  
`google.cloud.dataform.v1.Dataform.DeleteFolder`  
`google.cloud.dataform.v1.Dataform.DeleteFolderTree` (LRO)  
`google.cloud.dataform.v1.Dataform.DeleteReleaseConfig`  
`google.cloud.dataform.v1.Dataform.DeleteRepository`  
`google.cloud.dataform.v1.Dataform.DeleteTeamFolder`  
`google.cloud.dataform.v1.Dataform.DeleteTeamFolderTree` (LRO)  
`google.cloud.dataform.v1.Dataform.DeleteWorkflowConfig`  
`google.cloud.dataform.v1.Dataform.DeleteWorkspace`  
`google.cloud.dataform.v1.Dataform.MoveFolder` (LRO)  
`google.cloud.dataform.v1.Dataform.MoveRepository` (LRO)  
`google.cloud.dataform.v1.Dataform.SetIamPolicy`  
`google.cloud.dataform.v1.Dataform.UpdateFolder`  
`google.cloud.dataform.v1.Dataform.UpdateReleaseConfig`  
`google.cloud.dataform.v1.Dataform.UpdateRepository`  
`google.cloud.dataform.v1.Dataform.UpdateTeamFolder`  
`google.cloud.dataform.v1.Dataform.UpdateWorkflowConfig`  
`google.cloud.dataform.v1beta1.Dataform.CreateFolder`  
`google.cloud.dataform.v1beta1.Dataform.CreateReleaseConfig`  
`google.cloud.dataform.v1beta1.Dataform.CreateRepository`  
`google.cloud.dataform.v1beta1.Dataform.CreateTeamFolder`  
`google.cloud.dataform.v1beta1.Dataform.CreateWorkflowConfig`  
`google.cloud.dataform.v1beta1.Dataform.CreateWorkspace`  
`google.cloud.dataform.v1beta1.Dataform.DeleteFolder`  
`google.cloud.dataform.v1beta1.Dataform.DeleteFolderTree` (LRO)  
`google.cloud.dataform.v1beta1.Dataform.DeleteReleaseConfig`  
`google.cloud.dataform.v1beta1.Dataform.DeleteRepository`  
`google.cloud.dataform.v1beta1.Dataform.DeleteRepositoryLongRunning` (LRO)  
`google.cloud.dataform.v1beta1.Dataform.DeleteTeamFolder`  
`google.cloud.dataform.v1beta1.Dataform.DeleteTeamFolderTree` (LRO)  
`google.cloud.dataform.v1beta1.Dataform.DeleteWorkflowConfig`  
`google.cloud.dataform.v1beta1.Dataform.DeleteWorkspace`  
`google.cloud.dataform.v1beta1.Dataform.MoveFolder` (LRO)  
`google.cloud.dataform.v1beta1.Dataform.MoveRepository` (LRO)  
`google.cloud.dataform.v1beta1.Dataform.SetIamPolicy`  
`google.cloud.dataform.v1beta1.Dataform.UpdateFolder`  
`google.cloud.dataform.v1beta1.Dataform.UpdateReleaseConfig`  
`google.cloud.dataform.v1beta1.Dataform.UpdateRepository`  
`google.cloud.dataform.v1beta1.Dataform.UpdateTeamFolder`  
`google.cloud.dataform.v1beta1.Dataform.UpdateWorkflowConfig`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
`DATA_READ` | `google.cloud.dataform.v1.Dataform.FetchFileDiff`  
`google.cloud.dataform.v1.Dataform.FetchFileGitStatuses`  
`google.cloud.dataform.v1.Dataform.FetchGitAheadBehind`  
`google.cloud.dataform.v1.Dataform.FetchRepositoryHistory`  
`google.cloud.dataform.v1.Dataform.GetCompilationResult`  
`google.cloud.dataform.v1.Dataform.GetConfig`  
`google.cloud.dataform.v1.Dataform.GetWorkflowInvocation`  
`google.cloud.dataform.v1.Dataform.ListCompilationResults`  
`google.cloud.dataform.v1.Dataform.ListWorkflowInvocations`  
`google.cloud.dataform.v1.Dataform.PushGitCommits`  
`google.cloud.dataform.v1.Dataform.QueryCompilationResultActions`  
`google.cloud.dataform.v1.Dataform.QueryDirectoryContents`  
`google.cloud.dataform.v1.Dataform.QueryRepositoryDirectoryContents`  
`google.cloud.dataform.v1.Dataform.QueryWorkflowInvocationActions`  
`google.cloud.dataform.v1.Dataform.ReadFile`  
`google.cloud.dataform.v1.Dataform.ReadRepositoryFile`  
`google.cloud.dataform.v1.Dataform.SearchFiles`  
`google.cloud.dataform.v1beta1.Dataform.FetchCurrentWorkspaceBranch`  
`google.cloud.dataform.v1beta1.Dataform.FetchFileDiff`  
`google.cloud.dataform.v1beta1.Dataform.FetchFileGitStatuses`  
`google.cloud.dataform.v1beta1.Dataform.FetchGitAheadBehind`  
`google.cloud.dataform.v1beta1.Dataform.FetchRepositoryHistory`  
`google.cloud.dataform.v1beta1.Dataform.FetchWorkspaceBranches`  
`google.cloud.dataform.v1beta1.Dataform.GetCompilationResult`  
`google.cloud.dataform.v1beta1.Dataform.GetConfig`  
`google.cloud.dataform.v1beta1.Dataform.GetWorkflowInvocation`  
`google.cloud.dataform.v1beta1.Dataform.ListCompilationResults`  
`google.cloud.dataform.v1beta1.Dataform.ListWorkflowInvocations`  
`google.cloud.dataform.v1beta1.Dataform.PushGitCommits`  
`google.cloud.dataform.v1beta1.Dataform.QueryCompilationResultActions`  
`google.cloud.dataform.v1beta1.Dataform.QueryDirectoryContents`  
`google.cloud.dataform.v1beta1.Dataform.QueryRepositoryDirectoryContents`  
`google.cloud.dataform.v1beta1.Dataform.QueryWorkflowInvocationActions`  
`google.cloud.dataform.v1beta1.Dataform.ReadFile`  
`google.cloud.dataform.v1beta1.Dataform.ReadRepositoryFile`  
`google.cloud.dataform.v1beta1.Dataform.SearchFiles`  
`DATA_WRITE` | `google.cloud.dataform.v1.Dataform.CancelWorkflowInvocation`  
`google.cloud.dataform.v1.Dataform.CommitRepositoryChanges`  
`google.cloud.dataform.v1.Dataform.CommitWorkspaceChanges`  
`google.cloud.dataform.v1.Dataform.CreateCompilationResult`  
`google.cloud.dataform.v1.Dataform.CreateWorkflowInvocation`  
`google.cloud.dataform.v1.Dataform.DeleteWorkflowInvocation`  
`google.cloud.dataform.v1.Dataform.InstallNpmPackages`  
`google.cloud.dataform.v1.Dataform.MakeDirectory`  
`google.cloud.dataform.v1.Dataform.MoveDirectory`  
`google.cloud.dataform.v1.Dataform.MoveFile`  
`google.cloud.dataform.v1.Dataform.PullGitCommits`  
`google.cloud.dataform.v1.Dataform.RemoveDirectory`  
`google.cloud.dataform.v1.Dataform.RemoveFile`  
`google.cloud.dataform.v1.Dataform.ResetWorkspaceChanges`  
`google.cloud.dataform.v1.Dataform.UpdateConfig`  
`google.cloud.dataform.v1.Dataform.WriteFile`  
`google.cloud.dataform.v1beta1.Dataform.CancelWorkflowInvocation`  
`google.cloud.dataform.v1beta1.Dataform.CheckoutWorkspaceBranch`  
`google.cloud.dataform.v1beta1.Dataform.CommitRepositoryChanges`  
`google.cloud.dataform.v1beta1.Dataform.CommitWorkspaceChanges`  
`google.cloud.dataform.v1beta1.Dataform.CreateCompilationResult`  
`google.cloud.dataform.v1beta1.Dataform.CreateWorkflowInvocation`  
`google.cloud.dataform.v1beta1.Dataform.DeleteBranch`  
`google.cloud.dataform.v1beta1.Dataform.DeleteWorkflowInvocation`  
`google.cloud.dataform.v1beta1.Dataform.InstallNpmPackages`  
`google.cloud.dataform.v1beta1.Dataform.MakeDirectory`  
`google.cloud.dataform.v1beta1.Dataform.MoveDirectory`  
`google.cloud.dataform.v1beta1.Dataform.MoveFile`  
`google.cloud.dataform.v1beta1.Dataform.PullGitCommits`  
`google.cloud.dataform.v1beta1.Dataform.RemoveDirectory`  
`google.cloud.dataform.v1beta1.Dataform.RemoveFile`  
`google.cloud.dataform.v1beta1.Dataform.ResetWorkspaceChanges`  
`google.cloud.dataform.v1beta1.Dataform.SyncWorkspaceRefs`  
`google.cloud.dataform.v1beta1.Dataform.UpdateConfig`  
`google.cloud.dataform.v1beta1.Dataform.WriteFile`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the [Identity and Access Management documentation](https://docs.cloud.google.com/dataform/docs/access-control) for Dataform.

### `google.cloud.dataform.v1.Dataform`

The following audit logs are associated with methods belonging to `google.cloud.dataform.v1.Dataform`.

#### `CancelWorkflowInvocation`

  * **Method** : `google.cloud.dataform.v1.Dataform.CancelWorkflowInvocation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workflowInvocations.cancel - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.CancelWorkflowInvocation" `  




#### `CommitRepositoryChanges`

  * **Method** : `google.cloud.dataform.v1.Dataform.CommitRepositoryChanges`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.repositories.commit - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.CommitRepositoryChanges" `  




#### `CommitWorkspaceChanges`

  * **Method** : `google.cloud.dataform.v1.Dataform.CommitWorkspaceChanges`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.commit - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.CommitWorkspaceChanges" `  




#### `ComputeRepositoryAccessTokenStatus`

  * **Method** : `google.cloud.dataform.v1.Dataform.ComputeRepositoryAccessTokenStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.repositories.computeAccessTokenStatus - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.ComputeRepositoryAccessTokenStatus" `  




#### `CreateCompilationResult`

  * **Method** : `google.cloud.dataform.v1.Dataform.CreateCompilationResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.compilationResults.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.CreateCompilationResult" `  




#### `CreateFolder`

  * **Method** : `google.cloud.dataform.v1.Dataform.CreateFolder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.folders.addContents - ADMIN_WRITE`
    * `dataform.folders.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.CreateFolder" `  




#### `CreateReleaseConfig`

  * **Method** : `google.cloud.dataform.v1.Dataform.CreateReleaseConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.releaseConfigs.create - ADMIN_WRITE`
    * `dataform.repositories.scheduleRelease - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.CreateReleaseConfig" `  




#### `CreateRepository`

  * **Method** : `google.cloud.dataform.v1.Dataform.CreateRepository`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.folders.addContents - ADMIN_WRITE`
    * `dataform.repositories.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.CreateRepository" `  




#### `CreateTeamFolder`

  * **Method** : `google.cloud.dataform.v1.Dataform.CreateTeamFolder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.teamFolders.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.CreateTeamFolder" `  




#### `CreateWorkflowConfig`

  * **Method** : `google.cloud.dataform.v1.Dataform.CreateWorkflowConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.repositories.scheduleWorkflow - ADMIN_WRITE`
    * `dataform.workflowConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.CreateWorkflowConfig" `  




#### `CreateWorkflowInvocation`

  * **Method** : `google.cloud.dataform.v1.Dataform.CreateWorkflowInvocation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workflowInvocations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.CreateWorkflowInvocation" `  




#### `CreateWorkspace`

  * **Method** : `google.cloud.dataform.v1.Dataform.CreateWorkspace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.workspaces.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.CreateWorkspace" `  




#### `DeleteFolder`

  * **Method** : `google.cloud.dataform.v1.Dataform.DeleteFolder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.folders.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.DeleteFolder" `  




#### `DeleteFolderTree`

  * **Method** : `google.cloud.dataform.v1.Dataform.DeleteFolderTree`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.folders.deleteTree - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.DeleteFolderTree" `  




#### `DeleteReleaseConfig`

  * **Method** : `google.cloud.dataform.v1.Dataform.DeleteReleaseConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.releaseConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.DeleteReleaseConfig" `  




#### `DeleteRepository`

  * **Method** : `google.cloud.dataform.v1.Dataform.DeleteRepository`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.repositories.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.DeleteRepository" `  




#### `DeleteTeamFolder`

  * **Method** : `google.cloud.dataform.v1.Dataform.DeleteTeamFolder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.teamFolders.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.DeleteTeamFolder" `  




#### `DeleteTeamFolderTree`

  * **Method** : `google.cloud.dataform.v1.Dataform.DeleteTeamFolderTree`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.teamFolders.deleteTree - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.DeleteTeamFolderTree" `  




#### `DeleteWorkflowConfig`

  * **Method** : `google.cloud.dataform.v1.Dataform.DeleteWorkflowConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.workflowConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.DeleteWorkflowConfig" `  




#### `DeleteWorkflowInvocation`

  * **Method** : `google.cloud.dataform.v1.Dataform.DeleteWorkflowInvocation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workflowInvocations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.DeleteWorkflowInvocation" `  




#### `DeleteWorkspace`

  * **Method** : `google.cloud.dataform.v1.Dataform.DeleteWorkspace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.workspaces.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.DeleteWorkspace" `  




#### `FetchFileDiff`

  * **Method** : `google.cloud.dataform.v1.Dataform.FetchFileDiff`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.fetchFileDiff - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.FetchFileDiff" `  




#### `FetchFileGitStatuses`

  * **Method** : `google.cloud.dataform.v1.Dataform.FetchFileGitStatuses`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.fetchFileGitStatuses - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.FetchFileGitStatuses" `  




#### `FetchGitAheadBehind`

  * **Method** : `google.cloud.dataform.v1.Dataform.FetchGitAheadBehind`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.fetchGitAheadBehind - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.FetchGitAheadBehind" `  




#### `FetchRemoteBranches`

  * **Method** : `google.cloud.dataform.v1.Dataform.FetchRemoteBranches`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.repositories.fetchRemoteBranches - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.FetchRemoteBranches" `  




#### `FetchRepositoryHistory`

  * **Method** : `google.cloud.dataform.v1.Dataform.FetchRepositoryHistory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.repositories.fetchHistory - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.FetchRepositoryHistory" `  




#### `GetCompilationResult`

  * **Method** : `google.cloud.dataform.v1.Dataform.GetCompilationResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.compilationResults.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.GetCompilationResult" `  




#### `GetConfig`

  * **Method** : `google.cloud.dataform.v1.Dataform.GetConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.config.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.GetConfig" `  




#### `GetFolder`

  * **Method** : `google.cloud.dataform.v1.Dataform.GetFolder`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.folders.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.GetFolder" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.dataform.v1.Dataform.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.repositories.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.GetIamPolicy" `  




#### `GetReleaseConfig`

  * **Method** : `google.cloud.dataform.v1.Dataform.GetReleaseConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.releaseConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.GetReleaseConfig" `  




#### `GetRepository`

  * **Method** : `google.cloud.dataform.v1.Dataform.GetRepository`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.repositories.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.GetRepository" `  




#### `GetTeamFolder`

  * **Method** : `google.cloud.dataform.v1.Dataform.GetTeamFolder`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.teamFolders.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.GetTeamFolder" `  




#### `GetWorkflowConfig`

  * **Method** : `google.cloud.dataform.v1.Dataform.GetWorkflowConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workflowConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.GetWorkflowConfig" `  




#### `GetWorkflowInvocation`

  * **Method** : `google.cloud.dataform.v1.Dataform.GetWorkflowInvocation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workflowInvocations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.GetWorkflowInvocation" `  




#### `GetWorkspace`

  * **Method** : `google.cloud.dataform.v1.Dataform.GetWorkspace`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.GetWorkspace" `  




#### `InstallNpmPackages`

  * **Method** : `google.cloud.dataform.v1.Dataform.InstallNpmPackages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.installNpmPackages - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.InstallNpmPackages" `  




#### `ListCompilationResults`

  * **Method** : `google.cloud.dataform.v1.Dataform.ListCompilationResults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.compilationResults.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.ListCompilationResults" `  




#### `ListReleaseConfigs`

  * **Method** : `google.cloud.dataform.v1.Dataform.ListReleaseConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.releaseConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.ListReleaseConfigs" `  




#### `ListRepositories`

  * **Method** : `google.cloud.dataform.v1.Dataform.ListRepositories`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.repositories.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.ListRepositories" `  




#### `ListWorkflowConfigs`

  * **Method** : `google.cloud.dataform.v1.Dataform.ListWorkflowConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workflowConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.ListWorkflowConfigs" `  




#### `ListWorkflowInvocations`

  * **Method** : `google.cloud.dataform.v1.Dataform.ListWorkflowInvocations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workflowInvocations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.ListWorkflowInvocations" `  




#### `ListWorkspaces`

  * **Method** : `google.cloud.dataform.v1.Dataform.ListWorkspaces`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.ListWorkspaces" `  




#### `MakeDirectory`

  * **Method** : `google.cloud.dataform.v1.Dataform.MakeDirectory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.makeDirectory - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.MakeDirectory" `  




#### `MoveDirectory`

  * **Method** : `google.cloud.dataform.v1.Dataform.MoveDirectory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.moveDirectory - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.MoveDirectory" `  




#### `MoveFile`

  * **Method** : `google.cloud.dataform.v1.Dataform.MoveFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.moveFile - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.MoveFile" `  




#### `MoveFolder`

  * **Method** : `google.cloud.dataform.v1.Dataform.MoveFolder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.folders.addContents - ADMIN_WRITE`
    * `dataform.folders.move - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.MoveFolder" `  




#### `MoveRepository`

  * **Method** : `google.cloud.dataform.v1.Dataform.MoveRepository`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.repositories.move - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.MoveRepository" `  




#### `PullGitCommits`

  * **Method** : `google.cloud.dataform.v1.Dataform.PullGitCommits`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.pull - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.PullGitCommits" `  




#### `PushGitCommits`

  * **Method** : `google.cloud.dataform.v1.Dataform.PushGitCommits`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.push - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.PushGitCommits" `  




#### `QueryCompilationResultActions`

  * **Method** : `google.cloud.dataform.v1.Dataform.QueryCompilationResultActions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.compilationResults.query - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.QueryCompilationResultActions" `  




#### `QueryDirectoryContents`

  * **Method** : `google.cloud.dataform.v1.Dataform.QueryDirectoryContents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.queryDirectoryContents - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.QueryDirectoryContents" `  




#### `QueryFolderContents`

  * **Method** : `google.cloud.dataform.v1.Dataform.QueryFolderContents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.folders.queryContents - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.QueryFolderContents" `  




#### `QueryRepositoryDirectoryContents`

  * **Method** : `google.cloud.dataform.v1.Dataform.QueryRepositoryDirectoryContents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.repositories.queryDirectoryContents - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.QueryRepositoryDirectoryContents" `  




#### `QueryTeamFolderContents`

  * **Method** : `google.cloud.dataform.v1.Dataform.QueryTeamFolderContents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.folders.queryContents - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.QueryTeamFolderContents" `  




#### `QueryWorkflowInvocationActions`

  * **Method** : `google.cloud.dataform.v1.Dataform.QueryWorkflowInvocationActions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workflowInvocations.query - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.QueryWorkflowInvocationActions" `  




#### `ReadFile`

  * **Method** : `google.cloud.dataform.v1.Dataform.ReadFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.readFile - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.ReadFile" `  




#### `ReadRepositoryFile`

  * **Method** : `google.cloud.dataform.v1.Dataform.ReadRepositoryFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.repositories.readFile - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.ReadRepositoryFile" `  




#### `RemoveDirectory`

  * **Method** : `google.cloud.dataform.v1.Dataform.RemoveDirectory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.removeDirectory - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.RemoveDirectory" `  




#### `RemoveFile`

  * **Method** : `google.cloud.dataform.v1.Dataform.RemoveFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.removeFile - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.RemoveFile" `  




#### `ResetWorkspaceChanges`

  * **Method** : `google.cloud.dataform.v1.Dataform.ResetWorkspaceChanges`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.reset - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.ResetWorkspaceChanges" `  




#### `SearchFiles`

  * **Method** : `google.cloud.dataform.v1.Dataform.SearchFiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.searchFiles - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.SearchFiles" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.dataform.v1.Dataform.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.folders.setIamPolicy - ADMIN_WRITE`
    * `dataform.repositories.setIamPolicy - ADMIN_WRITE`
    * `dataform.workspaces.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.SetIamPolicy" `  




#### `UpdateConfig`

  * **Method** : `google.cloud.dataform.v1.Dataform.UpdateConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.config.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.UpdateConfig" `  




#### `UpdateFolder`

  * **Method** : `google.cloud.dataform.v1.Dataform.UpdateFolder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.folders.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.UpdateFolder" `  




#### `UpdateReleaseConfig`

  * **Method** : `google.cloud.dataform.v1.Dataform.UpdateReleaseConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.releaseConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.UpdateReleaseConfig" `  




#### `UpdateRepository`

  * **Method** : `google.cloud.dataform.v1.Dataform.UpdateRepository`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.repositories.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.UpdateRepository" `  




#### `UpdateTeamFolder`

  * **Method** : `google.cloud.dataform.v1.Dataform.UpdateTeamFolder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.teamFolders.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.UpdateTeamFolder" `  




#### `UpdateWorkflowConfig`

  * **Method** : `google.cloud.dataform.v1.Dataform.UpdateWorkflowConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.workflowConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.UpdateWorkflowConfig" `  




#### `WriteFile`

  * **Method** : `google.cloud.dataform.v1.Dataform.WriteFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.writeFile - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1.Dataform.WriteFile" `  




### `google.cloud.dataform.v1beta1.Dataform`

The following audit logs are associated with methods belonging to `google.cloud.dataform.v1beta1.Dataform`.

#### `CancelWorkflowInvocation`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.CancelWorkflowInvocation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workflowInvocations.cancel - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.CancelWorkflowInvocation" `  




#### `CheckoutWorkspaceBranch`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.CheckoutWorkspaceBranch`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.checkoutBranch - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.CheckoutWorkspaceBranch" `  




#### `CommitRepositoryChanges`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.CommitRepositoryChanges`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.repositories.commit - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.CommitRepositoryChanges" `  




#### `CommitWorkspaceChanges`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.CommitWorkspaceChanges`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.commit - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.CommitWorkspaceChanges" `  




#### `ComputeRepositoryAccessTokenStatus`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.ComputeRepositoryAccessTokenStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.repositories.computeAccessTokenStatus - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.ComputeRepositoryAccessTokenStatus" `  




#### `CreateCompilationResult`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.CreateCompilationResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.compilationResults.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.CreateCompilationResult" `  




#### `CreateFolder`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.CreateFolder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.folders.addContents - ADMIN_WRITE`
    * `dataform.folders.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.CreateFolder" `  




#### `CreateReleaseConfig`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.CreateReleaseConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.releaseConfigs.create - ADMIN_WRITE`
    * `dataform.repositories.scheduleRelease - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.CreateReleaseConfig" `  




#### `CreateRepository`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.CreateRepository`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.folders.addContents - ADMIN_WRITE`
    * `dataform.repositories.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.CreateRepository" `  




#### `CreateTeamFolder`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.CreateTeamFolder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.teamFolders.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.CreateTeamFolder" `  




#### `CreateWorkflowConfig`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.CreateWorkflowConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.workflowConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.CreateWorkflowConfig" `  




#### `CreateWorkflowInvocation`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.CreateWorkflowInvocation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workflowInvocations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.CreateWorkflowInvocation" `  




#### `CreateWorkspace`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.CreateWorkspace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.workspaces.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.CreateWorkspace" `  




#### `DeleteBranch`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.DeleteBranch`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.deleteBranch - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.DeleteBranch" `  




#### `DeleteFolder`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.DeleteFolder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.folders.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.DeleteFolder" `  




#### `DeleteFolderTree`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.DeleteFolderTree`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.folders.deleteTree - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.DeleteFolderTree" `  




#### `DeleteReleaseConfig`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.DeleteReleaseConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.releaseConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.DeleteReleaseConfig" `  




#### `DeleteRepository`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.DeleteRepository`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.repositories.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.DeleteRepository" `  




#### `DeleteRepositoryLongRunning`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.DeleteRepositoryLongRunning`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.repositories.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.DeleteRepositoryLongRunning" `  




#### `DeleteTeamFolder`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.DeleteTeamFolder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.teamFolders.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.DeleteTeamFolder" `  




#### `DeleteTeamFolderTree`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.DeleteTeamFolderTree`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.teamFolders.deleteTree - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.DeleteTeamFolderTree" `  




#### `DeleteWorkflowConfig`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.DeleteWorkflowConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.workflowConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.DeleteWorkflowConfig" `  




#### `DeleteWorkflowInvocation`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.DeleteWorkflowInvocation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workflowInvocations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.DeleteWorkflowInvocation" `  




#### `DeleteWorkspace`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.DeleteWorkspace`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.workspaces.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.DeleteWorkspace" `  




#### `FetchCurrentWorkspaceBranch`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.FetchCurrentWorkspaceBranch`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.fetchCurrentBranch - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.FetchCurrentWorkspaceBranch" `  




#### `FetchFileDiff`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.FetchFileDiff`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.fetchFileDiff - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.FetchFileDiff" `  




#### `FetchFileGitStatuses`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.FetchFileGitStatuses`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.fetchFileGitStatuses - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.FetchFileGitStatuses" `  




#### `FetchGitAheadBehind`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.FetchGitAheadBehind`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.fetchGitAheadBehind - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.FetchGitAheadBehind" `  




#### `FetchRemoteBranches`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.FetchRemoteBranches`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.repositories.fetchRemoteBranches - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.FetchRemoteBranches" `  




#### `FetchRepositoryHistory`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.FetchRepositoryHistory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.repositories.fetchHistory - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.FetchRepositoryHistory" `  




#### `FetchWorkspaceBranches`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.FetchWorkspaceBranches`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.fetchBranches - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.FetchWorkspaceBranches" `  




#### `GetCompilationResult`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.GetCompilationResult`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.compilationResults.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.GetCompilationResult" `  




#### `GetConfig`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.GetConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.config.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.GetConfig" `  




#### `GetFolder`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.GetFolder`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.folders.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.GetFolder" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.folders.getIamPolicy - ADMIN_READ`
    * `dataform.repositories.getIamPolicy - ADMIN_READ`
    * `dataform.teamFolders.getIamPolicy - ADMIN_READ`
    * `dataform.workspaces.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.GetIamPolicy" `  




#### `GetReleaseConfig`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.GetReleaseConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.releaseConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.GetReleaseConfig" `  




#### `GetRepository`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.GetRepository`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.repositories.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.GetRepository" `  




#### `GetTeamFolder`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.GetTeamFolder`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.teamFolders.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.GetTeamFolder" `  




#### `GetWorkflowConfig`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.GetWorkflowConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workflowConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.GetWorkflowConfig" `  




#### `GetWorkflowInvocation`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.GetWorkflowInvocation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workflowInvocations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.GetWorkflowInvocation" `  




#### `GetWorkspace`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.GetWorkspace`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.GetWorkspace" `  




#### `InstallNpmPackages`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.InstallNpmPackages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.installNpmPackages - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.InstallNpmPackages" `  




#### `ListCompilationResults`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.ListCompilationResults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.compilationResults.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.ListCompilationResults" `  




#### `ListReleaseConfigs`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.ListReleaseConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.releaseConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.ListReleaseConfigs" `  




#### `ListRepositories`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.ListRepositories`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.repositories.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.ListRepositories" `  




#### `ListWorkflowConfigs`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.ListWorkflowConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workflowConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.ListWorkflowConfigs" `  




#### `ListWorkflowInvocations`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.ListWorkflowInvocations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workflowInvocations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.ListWorkflowInvocations" `  




#### `ListWorkspaces`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.ListWorkspaces`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.ListWorkspaces" `  




#### `MakeDirectory`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.MakeDirectory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.makeDirectory - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.MakeDirectory" `  




#### `MoveDirectory`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.MoveDirectory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.moveDirectory - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.MoveDirectory" `  




#### `MoveFile`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.MoveFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.moveFile - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.MoveFile" `  




#### `MoveFolder`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.MoveFolder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.folders.addContents - ADMIN_WRITE`
    * `dataform.folders.move - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.MoveFolder" `  




#### `MoveRepository`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.MoveRepository`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.repositories.move - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.MoveRepository" `  




#### `PullGitCommits`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.PullGitCommits`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.pull - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.PullGitCommits" `  




#### `PushGitCommits`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.PushGitCommits`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.push - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.PushGitCommits" `  




#### `QueryCompilationResultActions`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.QueryCompilationResultActions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.compilationResults.query - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.QueryCompilationResultActions" `  




#### `QueryDirectoryContents`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.QueryDirectoryContents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.queryDirectoryContents - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.QueryDirectoryContents" `  




#### `QueryFolderContents`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.QueryFolderContents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.folders.queryContents - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.QueryFolderContents" `  




#### `QueryRepositoryDirectoryContents`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.QueryRepositoryDirectoryContents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.repositories.queryDirectoryContents - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.QueryRepositoryDirectoryContents" `  




#### `QueryTeamFolderContents`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.QueryTeamFolderContents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.folders.queryContents - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.QueryTeamFolderContents" `  




#### `QueryWorkflowInvocationActions`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.QueryWorkflowInvocationActions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workflowInvocations.query - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.QueryWorkflowInvocationActions" `  




#### `ReadFile`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.ReadFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.readFile - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.ReadFile" `  




#### `ReadRepositoryFile`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.ReadRepositoryFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.repositories.readFile - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.ReadRepositoryFile" `  




#### `RemoveDirectory`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.RemoveDirectory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.removeDirectory - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.RemoveDirectory" `  




#### `RemoveFile`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.RemoveFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.removeFile - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.RemoveFile" `  




#### `ResetWorkspaceChanges`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.ResetWorkspaceChanges`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.reset - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.ResetWorkspaceChanges" `  




#### `SearchFiles`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.SearchFiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.searchFiles - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.SearchFiles" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.folders.setIamPolicy - ADMIN_WRITE`
    * `dataform.repositories.setIamPolicy - ADMIN_WRITE`
    * `dataform.workspaces.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.SetIamPolicy" `  




#### `SyncWorkspaceRefs`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.SyncWorkspaceRefs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.syncRefs - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.SyncWorkspaceRefs" `  




#### `UpdateConfig`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.UpdateConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.config.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.UpdateConfig" `  




#### `UpdateFolder`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.UpdateFolder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.folders.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.UpdateFolder" `  




#### `UpdateReleaseConfig`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.UpdateReleaseConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.releaseConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.UpdateReleaseConfig" `  




#### `UpdateRepository`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.UpdateRepository`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.repositories.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.UpdateRepository" `  




#### `UpdateTeamFolder`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.UpdateTeamFolder`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.teamFolders.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.UpdateTeamFolder" `  




#### `UpdateWorkflowConfig`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.UpdateWorkflowConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.workflowConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.UpdateWorkflowConfig" `  




#### `WriteFile`

  * **Method** : `google.cloud.dataform.v1beta1.Dataform.WriteFile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.workspaces.writeFile - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataform.v1beta1.Dataform.WriteFile" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `google.iam.v1.IAMPolicy.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.repositories.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.IAMPolicy.GetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataform.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataform.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.dataform.v1.Dataform.TestIamPermissions`
  * `google.cloud.dataform.v1beta1.Dataform.TestIamPermissions`
  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
