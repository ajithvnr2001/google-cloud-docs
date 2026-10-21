---
url: https://docs.cloud.google.com/secure-source-manager/docs/audit-logging/
title: Secure Source Manager audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:43.410115+00:00
---

# Secure Source Manager audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Secure Source Manager audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Secure Source Manager. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Secure Source Manager audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="securesourcemanager.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Secure Source Manager generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.securesourcemanager.v1.SecureSourceManager.GetIamPolicyRepo`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.GetInstance`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.ListInstances`  
`GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.securesourcemanager.v1.SecureSourceManager.CreateInstance` (LRO)  
`google.cloud.securesourcemanager.v1.SecureSourceManager.DeleteInstance` (LRO)  
`google.cloud.securesourcemanager.v1.SecureSourceManager.SetIamPolicyRepo`  
`SetIamPolicy`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
`DATA_READ` | `google.cloud.securesourcemanager.v1.SecureSourceManager.FetchBlob`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.FetchRefs`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.FetchTree`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.GetBranchRule`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.GetHook`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.GetIssue`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.GetIssueComment`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.GetPullRequest`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.GetPullRequestComment`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.GetRepository`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.ListBranchRules`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.ListHooks`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.ListIssueComments`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.ListIssues`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.ListPullRequestComments`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.ListPullRequestFileDiffs`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.ListPullRequests`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.ListRepositories`  
`DATA_WRITE` | `google.cloud.securesourcemanager.v1.SecureSourceManager.BatchCreatePullRequestComments`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.CloseIssue`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.ClosePullRequest`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.CreateBranchRule`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.CreateHook`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.CreateIssue`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.CreateIssueComment`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.CreatePullRequest`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.CreatePullRequestComment`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.CreateRepository`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.DeleteBranchRule`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.DeleteHook`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.DeleteIssue`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.DeleteIssueComment`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.DeletePullRequestComment`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.DeleteRepository`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.MergePullRequest`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.OpenIssue`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.OpenPullRequest`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.ResolvePullRequestComments`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.UnresolvePullRequestComments`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.UpdateBranchRule`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.UpdateHook`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.UpdateIssue`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.UpdateIssueComment`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.UpdatePullRequest`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.UpdatePullRequestComment`  
`google.cloud.securesourcemanager.v1.SecureSourceManager.UpdateRepository`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Secure Source Manager.

### `google.cloud.securesourcemanager.v1.SecureSourceManager`

The following audit logs are associated with methods belonging to `google.cloud.securesourcemanager.v1.SecureSourceManager`.

#### `BatchCreatePullRequestComments`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.BatchCreatePullRequestComments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.prcomments.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.BatchCreatePullRequestComments" `  




#### `CloseIssue`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.CloseIssue`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.issues.close - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.CloseIssue" `  




#### `ClosePullRequest`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.ClosePullRequest`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.pullRequests.close - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.ClosePullRequest" `  




#### `CreateBranchRule`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.CreateBranchRule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.branchRules.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.CreateBranchRule" `  




#### `CreateHook`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.CreateHook`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.hooks.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.CreateHook" `  




#### `CreateInstance`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.CreateInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securesourcemanager.instances.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.CreateInstance" `  




#### `CreateIssue`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.CreateIssue`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.issues.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.CreateIssue" `  




#### `CreateIssueComment`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.CreateIssueComment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.issuecomments.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.CreateIssueComment" `  




#### `CreatePullRequest`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.CreatePullRequest`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.pullRequests.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.CreatePullRequest" `  




#### `CreatePullRequestComment`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.CreatePullRequestComment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.prcomments.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.CreatePullRequestComment" `  




#### `CreateRepository`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.CreateRepository`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.repositories.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.CreateRepository" `  




#### `DeleteBranchRule`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.DeleteBranchRule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.branchRules.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.DeleteBranchRule" `  




#### `DeleteHook`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.DeleteHook`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.hooks.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.DeleteHook" `  




#### `DeleteInstance`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.DeleteInstance`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securesourcemanager.instances.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.DeleteInstance" `  




#### `DeleteIssue`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.DeleteIssue`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.issues.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.DeleteIssue" `  




#### `DeleteIssueComment`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.DeleteIssueComment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.issuecomments.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.DeleteIssueComment" `  




#### `DeletePullRequestComment`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.DeletePullRequestComment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.prcomments.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.DeletePullRequestComment" `  




#### `DeleteRepository`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.DeleteRepository`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.repositories.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.DeleteRepository" `  




#### `FetchBlob`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.FetchBlob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.repositories.fetch - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.FetchBlob" `  




#### `FetchRefs`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.FetchRefs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.repositories.fetch - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.FetchRefs" `  




#### `FetchTree`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.FetchTree`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.repositories.fetch - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.FetchTree" `  




#### `GetBranchRule`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.GetBranchRule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.branchRules.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.GetBranchRule" `  




#### `GetHook`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.GetHook`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.hooks.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.GetHook" `  




#### `GetIamPolicyRepo`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.GetIamPolicyRepo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.repositories.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.GetIamPolicyRepo" `  




#### `GetInstance`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.GetInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.instances.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.GetInstance" `  




#### `GetIssue`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.GetIssue`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.issues.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.GetIssue" `  




#### `GetIssueComment`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.GetIssueComment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.issuecomments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.GetIssueComment" `  




#### `GetPullRequest`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.GetPullRequest`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.pullRequests.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.GetPullRequest" `  




#### `GetPullRequestComment`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.GetPullRequestComment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.prcomments.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.GetPullRequestComment" `  




#### `GetRepository`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.GetRepository`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.repositories.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.GetRepository" `  




#### `ListBranchRules`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.ListBranchRules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.branchRules.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.ListBranchRules" `  




#### `ListHooks`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.ListHooks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.hooks.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.ListHooks" `  




#### `ListInstances`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.ListInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.instances.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.ListInstances" `  




#### `ListIssueComments`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.ListIssueComments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.issuecomments.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.ListIssueComments" `  




#### `ListIssues`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.ListIssues`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.issues.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.ListIssues" `  




#### `ListPullRequestComments`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.ListPullRequestComments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.prcomments.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.ListPullRequestComments" `  




#### `ListPullRequestFileDiffs`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.ListPullRequestFileDiffs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.pullRequests.listFileDiffs - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.ListPullRequestFileDiffs" `  




#### `ListPullRequests`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.ListPullRequests`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.pullRequests.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.ListPullRequests" `  




#### `ListRepositories`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.ListRepositories`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.repositories.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.ListRepositories" `  




#### `MergePullRequest`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.MergePullRequest`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.pullRequests.merge - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.MergePullRequest" `  




#### `OpenIssue`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.OpenIssue`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.issues.open - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.OpenIssue" `  




#### `OpenPullRequest`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.OpenPullRequest`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.pullRequests.open - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.OpenPullRequest" `  




#### `ResolvePullRequestComments`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.ResolvePullRequestComments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.prcomments.resolve - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.ResolvePullRequestComments" `  




#### `SetIamPolicyRepo`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.SetIamPolicyRepo`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securesourcemanager.repositories.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.SetIamPolicyRepo" `  




#### `UnresolvePullRequestComments`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.UnresolvePullRequestComments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.prcomments.unresolve - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.UnresolvePullRequestComments" `  




#### `UpdateBranchRule`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.UpdateBranchRule`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.branchRules.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.UpdateBranchRule" `  




#### `UpdateHook`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.UpdateHook`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.hooks.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.UpdateHook" `  




#### `UpdateIssue`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.UpdateIssue`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.issues.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.UpdateIssue" `  




#### `UpdateIssueComment`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.UpdateIssueComment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.issuecomments.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.UpdateIssueComment" `  




#### `UpdatePullRequest`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.UpdatePullRequest`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.pullRequests.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.UpdatePullRequest" `  




#### `UpdatePullRequestComment`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.UpdatePullRequestComment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.prcomments.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.UpdatePullRequestComment" `  




#### `UpdateRepository`

  * **Method** : `google.cloud.securesourcemanager.v1.SecureSourceManager.UpdateRepository`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.repositories.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.securesourcemanager.v1.SecureSourceManager.UpdateRepository" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.instances.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securesourcemanager.instances.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securesourcemanager.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `securesourcemanager.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `securesourcemanager.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.cloud.securesourcemanager.v1.SecureSourceManager.TestIamPermissionsRepo`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
