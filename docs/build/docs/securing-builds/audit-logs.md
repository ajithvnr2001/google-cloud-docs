---
url: https://docs.cloud.google.com/build/docs/securing-builds/audit-logs/
title: Cloud Build Audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:12.348179+00:00
---

# Cloud Build Audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/securing-builds/audit-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Cloud Build Audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Cloud Build. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Cloud Build audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="cloudbuild.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Build generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.devtools.cloudbuild.v1.CloudBuild.GetBuild`  
`google.devtools.cloudbuild.v1.CloudBuild.GetBuildTrigger`  
`google.devtools.cloudbuild.v1.CloudBuild.GetDefaultServiceAccount`  
`google.devtools.cloudbuild.v1.CloudBuild.GetWorkerPool`  
`google.devtools.cloudbuild.v1.CloudBuild.ListBitbucketServerRepositories`  
`google.devtools.cloudbuild.v1.CloudBuild.ListBuildTriggers`  
`google.devtools.cloudbuild.v1.CloudBuild.ListBuilds`  
`google.devtools.cloudbuild.v1.CloudBuild.ListWorkerPools`  
`google.devtools.cloudbuild.v2.RepositoryManager.FetchLinkableRepositories`  
`google.devtools.cloudbuild.v2.RepositoryManager.GetConnection`  
`google.devtools.cloudbuild.v2.RepositoryManager.GetRepository`  
`google.devtools.cloudbuild.v2.RepositoryManager.ListConnections`  
`google.devtools.cloudbuild.v2.RepositoryManager.ListRepositories`  
`GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`ADMIN_WRITE` | `google.devtools.cloudbuild.v1.CloudBuild.ApproveBuild` (LRO)  
`google.devtools.cloudbuild.v1.CloudBuild.CancelBuild`  
`google.devtools.cloudbuild.v1.CloudBuild.CreateBuild` (LRO)  
`google.devtools.cloudbuild.v1.CloudBuild.CreateBuildTrigger`  
`google.devtools.cloudbuild.v1.CloudBuild.CreateWorkerPool` (LRO)  
`google.devtools.cloudbuild.v1.CloudBuild.DeleteBuildTrigger`  
`google.devtools.cloudbuild.v1.CloudBuild.DeleteWorkerPool` (LRO)  
`google.devtools.cloudbuild.v1.CloudBuild.RetryBuild` (LRO)  
`google.devtools.cloudbuild.v1.CloudBuild.RunBuildTrigger` (LRO)  
`google.devtools.cloudbuild.v1.CloudBuild.UpdateBuildTrigger`  
`google.devtools.cloudbuild.v1.CloudBuild.UpdateWorkerPool` (LRO)  
`google.devtools.cloudbuild.v2.RepositoryManager.BatchCreateRepositories` (LRO)  
`google.devtools.cloudbuild.v2.RepositoryManager.CreateConnection` (LRO)  
`google.devtools.cloudbuild.v2.RepositoryManager.CreateRepository` (LRO)  
`google.devtools.cloudbuild.v2.RepositoryManager.DeleteConnection` (LRO)  
`google.devtools.cloudbuild.v2.RepositoryManager.DeleteRepository` (LRO)  
`google.devtools.cloudbuild.v2.RepositoryManager.UpdateConnection` (LRO)  
`SetIamPolicy`  
`google.longrunning.Operations.CancelOperation`  
`DATA_READ` | `google.devtools.cloudbuild.v1.CloudBuild.GetBitbucketServerConfig`  
`google.devtools.cloudbuild.v1.CloudBuild.GetGitHubEnterpriseConfig`  
`google.devtools.cloudbuild.v1.CloudBuild.GetGitLabConfig`  
`google.devtools.cloudbuild.v1.CloudBuild.ListBitbucketServerConfigs`  
`google.devtools.cloudbuild.v1.CloudBuild.ListBitbucketServerRepositories`  
`google.devtools.cloudbuild.v1.CloudBuild.ListGitHubEnterpriseConfigs`  
`google.devtools.cloudbuild.v1.CloudBuild.ListGitLabConfigs`  
`google.devtools.cloudbuild.v1.CloudBuild.ListGitLabRepositories`  
`google.devtools.cloudbuild.v1.CloudBuild.RemoveBitbucketServerConnectedRepository`  
`google.devtools.cloudbuild.v2.RepositoryManager.FetchGitRefs`  
`google.devtools.cloudbuild.v2.RepositoryManager.FetchReadToken`  
`google.devtools.cloudbuild.v2.RepositoryManager.FetchReadWriteToken`  
`DATA_WRITE` | `google.devtools.cloudbuild.v1.CloudBuild.CreateGitHubEnterpriseConfig` (LRO)  
`google.devtools.cloudbuild.v1.CloudBuild.DeleteGitHubEnterpriseConfig` (LRO)  
`google.devtools.cloudbuild.v1.CloudBuild.DeleteGitLabConfig`  
`google.devtools.cloudbuild.v1.CloudBuild.RemoveBitbucketServerConnectedRepository`  
`google.devtools.cloudbuild.v1.CloudBuild.UpdateBitbucketServerConfig` (LRO)  
`google.devtools.cloudbuild.v1.CloudBuild.UpdateGitHubEnterpriseConfig` (LRO)  
`google.devtools.cloudbuild.v1.CloudBuild.UpdateGitLabConfig` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Build.

### `google.devtools.cloudbuild.v1.CloudBuild`

The following audit logs are associated with methods belonging to `google.devtools.cloudbuild.v1.CloudBuild`.

#### `ApproveBuild`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.ApproveBuild`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudbuild.builds.approve - ADMIN_WRITE`
    * `cloudbuild.builds.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.ApproveBuild" `  




#### `BatchCreateBitbucketServerConnectedRepositories`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.BatchCreateBitbucketServerConnectedRepositories`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.BatchCreateBitbucketServerConnectedRepositories" `  




#### `CancelBuild`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.CancelBuild`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudbuild.builds.create - ADMIN_WRITE`
    * `cloudbuild.builds.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.CancelBuild" `  




#### `CreateBitbucketServerConfig`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.CreateBitbucketServerConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.integrations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.CreateBitbucketServerConfig" `  




#### `CreateBuild`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.CreateBuild`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudbuild.builds.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.CreateBuild" `  




#### `CreateBuildTrigger`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.CreateBuildTrigger`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudbuild.builds.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.CreateBuildTrigger" `  




#### `CreateGitHubEnterpriseConfig`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.CreateGitHubEnterpriseConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.integrations.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.CreateGitHubEnterpriseConfig" `  




#### `CreateWorkerPool`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.CreateWorkerPool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudbuild.workerpools.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.CreateWorkerPool" `  




#### `DeleteBitbucketServerConfig`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.DeleteBitbucketServerConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.integrations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.DeleteBitbucketServerConfig" `  




#### `DeleteBuildTrigger`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.DeleteBuildTrigger`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudbuild.builds.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.DeleteBuildTrigger" `  




#### `DeleteGitHubEnterpriseConfig`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.DeleteGitHubEnterpriseConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.integrations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.DeleteGitHubEnterpriseConfig" `  




#### `DeleteGitLabConfig`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.DeleteGitLabConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.integrations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.DeleteGitLabConfig" `  




#### `DeleteWorkerPool`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.DeleteWorkerPool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudbuild.workerpools.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.DeleteWorkerPool" `  




#### `GetBitbucketServerConfig`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.GetBitbucketServerConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.integrations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.GetBitbucketServerConfig" `  




#### `GetBuild`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.GetBuild`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.builds.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.GetBuild" `  




#### `GetBuildTrigger`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.GetBuildTrigger`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.builds.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.GetBuildTrigger" `  




#### `GetDefaultServiceAccount`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.GetDefaultServiceAccount`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.builds.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.GetDefaultServiceAccount" `  




#### `GetGitHubEnterpriseConfig`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.GetGitHubEnterpriseConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.integrations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.GetGitHubEnterpriseConfig" `  




#### `GetGitLabConfig`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.GetGitLabConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.integrations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.GetGitLabConfig" `  




#### `GetWorkerPool`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.GetWorkerPool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.workerpools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.GetWorkerPool" `  




#### `ListBitbucketServerConfigs`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.ListBitbucketServerConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.integrations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.ListBitbucketServerConfigs" `  




#### `ListBitbucketServerRepositories`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.ListBitbucketServerRepositories`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.builds.get - ADMIN_READ`
    * `cloudbuild.integrations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.ListBitbucketServerRepositories" `  




#### `ListBuildTriggers`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.ListBuildTriggers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.builds.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.ListBuildTriggers" `  




#### `ListBuilds`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.ListBuilds`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.builds.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.ListBuilds" `  




#### `ListGitHubEnterpriseConfigs`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.ListGitHubEnterpriseConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.integrations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.ListGitHubEnterpriseConfigs" `  




#### `ListGitLabConfigs`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.ListGitLabConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.integrations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.ListGitLabConfigs" `  




#### `ListGitLabRepositories`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.ListGitLabRepositories`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.integrations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.ListGitLabRepositories" `  




#### `ListWorkerPools`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.ListWorkerPools`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.workerpools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.ListWorkerPools" `  




#### `RemoveBitbucketServerConnectedRepository`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.RemoveBitbucketServerConnectedRepository`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.integrations.delete - DATA_WRITE`
    * `cloudbuild.integrations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.RemoveBitbucketServerConnectedRepository" `  




#### `RetryBuild`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.RetryBuild`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudbuild.builds.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.RetryBuild" `  




#### `RunBuildTrigger`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.RunBuildTrigger`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudbuild.builds.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.RunBuildTrigger" `  




#### `UpdateBitbucketServerConfig`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.UpdateBitbucketServerConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.integrations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.UpdateBitbucketServerConfig" `  




#### `UpdateBuildTrigger`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.UpdateBuildTrigger`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudbuild.builds.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.UpdateBuildTrigger" `  




#### `UpdateGitHubEnterpriseConfig`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.UpdateGitHubEnterpriseConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.integrations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.UpdateGitHubEnterpriseConfig" `  




#### `UpdateGitLabConfig`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.UpdateGitLabConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.integrations.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.UpdateGitLabConfig" `  




#### `UpdateWorkerPool`

  * **Method** : `google.devtools.cloudbuild.v1.CloudBuild.UpdateWorkerPool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudbuild.workerpools.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v1.CloudBuild.UpdateWorkerPool" `  




### `google.devtools.cloudbuild.v2.RepositoryManager`

The following audit logs are associated with methods belonging to `google.devtools.cloudbuild.v2.RepositoryManager`.

#### `BatchCreateRepositories`

  * **Method** : `google.devtools.cloudbuild.v2.RepositoryManager.BatchCreateRepositories`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudbuild.repositories.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v2.RepositoryManager.BatchCreateRepositories" `  




#### `CreateConnection`

  * **Method** : `google.devtools.cloudbuild.v2.RepositoryManager.CreateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudbuild.connections.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v2.RepositoryManager.CreateConnection" `  




#### `CreateRepository`

  * **Method** : `google.devtools.cloudbuild.v2.RepositoryManager.CreateRepository`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudbuild.repositories.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v2.RepositoryManager.CreateRepository" `  




#### `DeleteConnection`

  * **Method** : `google.devtools.cloudbuild.v2.RepositoryManager.DeleteConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudbuild.connections.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v2.RepositoryManager.DeleteConnection" `  




#### `DeleteRepository`

  * **Method** : `google.devtools.cloudbuild.v2.RepositoryManager.DeleteRepository`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudbuild.repositories.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v2.RepositoryManager.DeleteRepository" `  




#### `FetchGitRefs`

  * **Method** : `google.devtools.cloudbuild.v2.RepositoryManager.FetchGitRefs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.repositories.fetchGitRefs - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v2.RepositoryManager.FetchGitRefs" `  




#### `FetchLinkableRepositories`

  * **Method** : `google.devtools.cloudbuild.v2.RepositoryManager.FetchLinkableRepositories`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.connections.fetchLinkableRepositories - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v2.RepositoryManager.FetchLinkableRepositories" `  




#### `FetchReadToken`

  * **Method** : `google.devtools.cloudbuild.v2.RepositoryManager.FetchReadToken`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.repositories.accessReadToken - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v2.RepositoryManager.FetchReadToken" `  




#### `FetchReadWriteToken`

  * **Method** : `google.devtools.cloudbuild.v2.RepositoryManager.FetchReadWriteToken`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.repositories.accessReadWriteToken - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v2.RepositoryManager.FetchReadWriteToken" `  




#### `GetConnection`

  * **Method** : `google.devtools.cloudbuild.v2.RepositoryManager.GetConnection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.connections.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v2.RepositoryManager.GetConnection" `  




#### `GetRepository`

  * **Method** : `google.devtools.cloudbuild.v2.RepositoryManager.GetRepository`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.repositories.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v2.RepositoryManager.GetRepository" `  




#### `ListConnections`

  * **Method** : `google.devtools.cloudbuild.v2.RepositoryManager.ListConnections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.connections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v2.RepositoryManager.ListConnections" `  




#### `ListRepositories`

  * **Method** : `google.devtools.cloudbuild.v2.RepositoryManager.ListRepositories`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.repositories.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v2.RepositoryManager.ListRepositories" `  




#### `UpdateConnection`

  * **Method** : `google.devtools.cloudbuild.v2.RepositoryManager.UpdateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudbuild.connections.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.devtools.cloudbuild.v2.RepositoryManager.UpdateConnection" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.connections.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudbuild.connections.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudbuild.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudbuild.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.devtools.cloudbuild.v1.CloudBuild.ReceiveGitHubDotComWebhook`
  * `google.devtools.cloudbuild.v1.CloudBuild.ReceiveRegionalWebhook`
  * `google.devtools.cloudbuild.v1.CloudBuild.ReceiveTriggerWebhook`
  * `google.devtools.cloudbuild.v1.CloudBuild.ReceiveWebhook`
  * `google.devtools.cloudbuild.v2.RepositoryManager.ProcessWebhook`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
