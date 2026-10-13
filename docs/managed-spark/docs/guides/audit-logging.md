---
url: https://docs.cloud.google.com/managed-spark/docs/guides/audit-logging/
title: Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:33.851966+00:00
---

# Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Managed Service for Apache Spark audit logging

This document lists the audited methods for Managed Service for Apache Spark and Managed Service for Apache Spark. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Managed Service for Apache Spark and Managed Service for Apache Spark audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="dataproc.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Managed Service for Apache Spark and Managed Service for Apache Spark generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.dataproc.v1.AutoscalingPolicyService.GetAutoscalingPolicy`  
`google.cloud.dataproc.v1.AutoscalingPolicyService.ListAutoscalingPolicies`  
`google.cloud.dataproc.v1.BatchController.GetBatch`  
`google.cloud.dataproc.v1.BatchController.ListBatches`  
`google.cloud.dataproc.v1.ClusterController.GetCluster`  
`google.cloud.dataproc.v1.ClusterController.ListClusters`  
`google.cloud.dataproc.v1.JobController.GetJob`  
`google.cloud.dataproc.v1.JobController.ListJobs`  
`google.cloud.dataproc.v1.NodeGroupController.GetNodeGroup`  
`google.cloud.dataproc.v1.SessionController.GetSession`  
`google.cloud.dataproc.v1.SessionController.ListSessions`  
`google.cloud.dataproc.v1.SessionTemplateController.GetSessionTemplate`  
`google.cloud.dataproc.v1.SessionTemplateController.ListSessionTemplates`  
`google.cloud.dataproc.v1.WorkflowTemplateService.GetWorkflowTemplate`  
`google.cloud.dataproc.v1.WorkflowTemplateService.ListWorkflowTemplates`  
`google.cloud.dataproc.v1beta2.AutoscalingPolicyService.GetAutoscalingPolicy`  
`google.cloud.dataproc.v1beta2.AutoscalingPolicyService.ListAutoscalingPolicies`  
`google.cloud.dataproc.v1beta2.ClusterController.GetCluster`  
`google.cloud.dataproc.v1beta2.ClusterController.ListClusters`  
`google.cloud.dataproc.v1beta2.JobController.GetJob`  
`google.cloud.dataproc.v1beta2.JobController.ListJobs`  
`google.cloud.dataproc.v1beta2.WorkflowTemplateService.GetWorkflowTemplate`  
`google.cloud.dataproc.v1beta2.WorkflowTemplateService.ListWorkflowTemplates`  
`google.iam.v1.IAMPolicy.GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.dataproc.v1.AnalysisService.AnalyzeBatch` (LRO)  
`google.cloud.dataproc.v1.AutoscalingPolicyService.CreateAutoscalingPolicy`  
`google.cloud.dataproc.v1.AutoscalingPolicyService.DeleteAutoscalingPolicy`  
`google.cloud.dataproc.v1.AutoscalingPolicyService.UpdateAutoscalingPolicy`  
`google.cloud.dataproc.v1.BatchController.ComputeTuningConfig`  
`google.cloud.dataproc.v1.BatchController.CreateBatch` (LRO)  
`google.cloud.dataproc.v1.BatchController.DeleteBatch`  
`google.cloud.dataproc.v1.ClusterController.CreateCluster` (LRO)  
`google.cloud.dataproc.v1.ClusterController.DeleteCluster` (LRO)  
`google.cloud.dataproc.v1.ClusterController.DiagnoseCluster` (LRO)  
`google.cloud.dataproc.v1.ClusterController.InjectCredentials` (LRO)  
`google.cloud.dataproc.v1.ClusterController.RepairCluster` (LRO)  
`google.cloud.dataproc.v1.ClusterController.StartCluster` (LRO)  
`google.cloud.dataproc.v1.ClusterController.StopCluster` (LRO)  
`google.cloud.dataproc.v1.ClusterController.UpdateCluster` (LRO)  
`google.cloud.dataproc.v1.JobController.CancelJob`  
`google.cloud.dataproc.v1.JobController.DeleteJob`  
`google.cloud.dataproc.v1.JobController.SubmitJob` (LRO)  
`google.cloud.dataproc.v1.JobController.SubmitJobAsOperation` (LRO)  
`google.cloud.dataproc.v1.JobController.UpdateJob`  
`google.cloud.dataproc.v1.NodeGroupController.CreateNodeGroup` (LRO)  
`google.cloud.dataproc.v1.NodeGroupController.RepairNodeGroup` (LRO)  
`google.cloud.dataproc.v1.NodeGroupController.ResizeNodeGroup` (LRO)  
`google.cloud.dataproc.v1.SessionController.CreateSession` (LRO)  
`google.cloud.dataproc.v1.SessionController.DeleteSession` (LRO)  
`google.cloud.dataproc.v1.SessionController.TerminateSession` (LRO)  
`google.cloud.dataproc.v1.SessionTemplateController.CreateSessionTemplate`  
`google.cloud.dataproc.v1.SessionTemplateController.DeleteSessionTemplate`  
`google.cloud.dataproc.v1.SessionTemplateController.UpdateSessionTemplate`  
`google.cloud.dataproc.v1.WorkflowTemplateService.CreateWorkflowTemplate`  
`google.cloud.dataproc.v1.WorkflowTemplateService.DeleteWorkflowTemplate`  
`google.cloud.dataproc.v1.WorkflowTemplateService.InstantiateInlineWorkflowTemplate` (LRO)  
`google.cloud.dataproc.v1.WorkflowTemplateService.InstantiateWorkflowTemplate` (LRO)  
`google.cloud.dataproc.v1.WorkflowTemplateService.UpdateWorkflowTemplate`  
`google.cloud.dataproc.v1beta2.AutoscalingPolicyService.CreateAutoscalingPolicy`  
`google.cloud.dataproc.v1beta2.AutoscalingPolicyService.DeleteAutoscalingPolicy`  
`google.cloud.dataproc.v1beta2.AutoscalingPolicyService.UpdateAutoscalingPolicy`  
`google.cloud.dataproc.v1beta2.ClusterController.CreateCluster` (LRO)  
`google.cloud.dataproc.v1beta2.ClusterController.DeleteCluster` (LRO)  
`google.cloud.dataproc.v1beta2.ClusterController.DiagnoseCluster` (LRO)  
`google.cloud.dataproc.v1beta2.ClusterController.StartCluster` (LRO)  
`google.cloud.dataproc.v1beta2.ClusterController.StopCluster` (LRO)  
`google.cloud.dataproc.v1beta2.ClusterController.UpdateCluster` (LRO)  
`google.cloud.dataproc.v1beta2.JobController.CancelJob`  
`google.cloud.dataproc.v1beta2.JobController.DeleteJob`  
`google.cloud.dataproc.v1beta2.JobController.SubmitJob` (LRO)  
`google.cloud.dataproc.v1beta2.JobController.SubmitJobAsOperation` (LRO)  
`google.cloud.dataproc.v1beta2.JobController.UpdateJob`  
`google.cloud.dataproc.v1beta2.WorkflowTemplateService.CreateWorkflowTemplate`  
`google.cloud.dataproc.v1beta2.WorkflowTemplateService.DeleteWorkflowTemplate`  
`google.cloud.dataproc.v1beta2.WorkflowTemplateService.InstantiateInlineWorkflowTemplate` (LRO)  
`google.cloud.dataproc.v1beta2.WorkflowTemplateService.InstantiateWorkflowTemplate` (LRO)  
`google.cloud.dataproc.v1beta2.WorkflowTemplateService.UpdateWorkflowTemplate`  
`google.iam.v1.IAMPolicy.SetIamPolicy`  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
`DATA_READ` | `google.cloud.dataproc.v1.BatchController.AccessSparkApplication`  
`google.cloud.dataproc.v1.BatchController.AccessSparkApplicationEnvironmentInfo`  
`google.cloud.dataproc.v1.BatchController.AccessSparkApplicationJob`  
`google.cloud.dataproc.v1.BatchController.AccessSparkApplicationNativeBuildInfo`  
`google.cloud.dataproc.v1.BatchController.AccessSparkApplicationNativeSqlQuery`  
`google.cloud.dataproc.v1.BatchController.AccessSparkApplicationSqlQuery`  
`google.cloud.dataproc.v1.BatchController.AccessSparkApplicationStageAttempt`  
`google.cloud.dataproc.v1.BatchController.SearchSparkApplicationExecutors`  
`google.cloud.dataproc.v1.BatchController.SearchSparkApplicationJobs`  
`google.cloud.dataproc.v1.BatchController.SearchSparkApplicationNativeSqlQueries`  
`google.cloud.dataproc.v1.BatchController.SearchSparkApplicationSqlQueries`  
`google.cloud.dataproc.v1.BatchController.SearchSparkApplicationStageAttemptTasks`  
`google.cloud.dataproc.v1.BatchController.SearchSparkApplicationStageAttempts`  
`google.cloud.dataproc.v1.BatchController.SearchSparkApplicationStages`  
`google.cloud.dataproc.v1.BatchController.SearchSparkApplications`  
`google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplication`  
`google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationEnvironmentInfo`  
`google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationJob`  
`google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationNativeBuildInfo`  
`google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationNativeSqlQuery`  
`google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationSqlQuery`  
`google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationSqlSparkPlanGraph`  
`google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationStageAttempt`  
`google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationStageRddOperationGraph`  
`google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationExecutorStageSummary`  
`google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationExecutors`  
`google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationJobs`  
`google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationNativeSqlQueries`  
`google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationSqlQueries`  
`google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationStageAttemptTasks`  
`google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationStageAttempts`  
`google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationStages`  
`google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplications`  
`google.cloud.dataproc.v1.SessionController.SummarizeSessionSparkApplicationExecutors`  
`google.cloud.dataproc.v1.SessionController.SummarizeSessionSparkApplicationJobs`  
`google.cloud.dataproc.v1.SessionController.SummarizeSessionSparkApplicationStageAttemptTasks`  
`google.cloud.dataproc.v1.SessionController.SummarizeSessionSparkApplicationStages`  
`DATA_WRITE` | `google.cloud.dataproc.v1.BatchController.WriteSparkApplicationContext`  
`google.cloud.dataproc.v1.SessionController.WriteSessionSparkApplicationContext`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the [Identity and Access Management documentation](https://docs.cloud.google.com/dataproc/docs/concepts/iam/iam) for Managed Service for Apache Spark and Managed Service for Apache Spark.

### `google.cloud.dataproc.v1.AnalysisService`

The following audit logs are associated with methods belonging to `google.cloud.dataproc.v1.AnalysisService`.

#### `AnalyzeBatch`

  * **Method** : `google.cloud.dataproc.v1.AnalysisService.AnalyzeBatch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.batches.analyze - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.AnalysisService.AnalyzeBatch" `  




### `google.cloud.dataproc.v1.AutoscalingPolicyService`

The following audit logs are associated with methods belonging to `google.cloud.dataproc.v1.AutoscalingPolicyService`.

#### `CreateAutoscalingPolicy`

  * **Method** : `google.cloud.dataproc.v1.AutoscalingPolicyService.CreateAutoscalingPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.autoscalingPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.AutoscalingPolicyService.CreateAutoscalingPolicy" `  




#### `DeleteAutoscalingPolicy`

  * **Method** : `google.cloud.dataproc.v1.AutoscalingPolicyService.DeleteAutoscalingPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.autoscalingPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.AutoscalingPolicyService.DeleteAutoscalingPolicy" `  




#### `GetAutoscalingPolicy`

  * **Method** : `google.cloud.dataproc.v1.AutoscalingPolicyService.GetAutoscalingPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.autoscalingPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.AutoscalingPolicyService.GetAutoscalingPolicy" `  




#### `ListAutoscalingPolicies`

  * **Method** : `google.cloud.dataproc.v1.AutoscalingPolicyService.ListAutoscalingPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.autoscalingPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.AutoscalingPolicyService.ListAutoscalingPolicies" `  




#### `UpdateAutoscalingPolicy`

  * **Method** : `google.cloud.dataproc.v1.AutoscalingPolicyService.UpdateAutoscalingPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.autoscalingPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.AutoscalingPolicyService.UpdateAutoscalingPolicy" `  




### `google.cloud.dataproc.v1.BatchController`

The following audit logs are associated with methods belonging to `google.cloud.dataproc.v1.BatchController`.

#### `AccessSparkApplication`

  * **Method** : `google.cloud.dataproc.v1.BatchController.AccessSparkApplication`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.batches.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.AccessSparkApplication" `  




#### `AccessSparkApplicationEnvironmentInfo`

  * **Method** : `google.cloud.dataproc.v1.BatchController.AccessSparkApplicationEnvironmentInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.batches.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.AccessSparkApplicationEnvironmentInfo" `  




#### `AccessSparkApplicationJob`

  * **Method** : `google.cloud.dataproc.v1.BatchController.AccessSparkApplicationJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.batches.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.AccessSparkApplicationJob" `  




#### `AccessSparkApplicationNativeBuildInfo`

  * **Method** : `google.cloud.dataproc.v1.BatchController.AccessSparkApplicationNativeBuildInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.batches.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.AccessSparkApplicationNativeBuildInfo" `  




#### `AccessSparkApplicationNativeSqlQuery`

  * **Method** : `google.cloud.dataproc.v1.BatchController.AccessSparkApplicationNativeSqlQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.batches.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.AccessSparkApplicationNativeSqlQuery" `  




#### `AccessSparkApplicationSqlQuery`

  * **Method** : `google.cloud.dataproc.v1.BatchController.AccessSparkApplicationSqlQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.batches.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.AccessSparkApplicationSqlQuery" `  




#### `AccessSparkApplicationStageAttempt`

  * **Method** : `google.cloud.dataproc.v1.BatchController.AccessSparkApplicationStageAttempt`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.batches.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.AccessSparkApplicationStageAttempt" `  




#### `ComputeTuningConfig`

  * **Method** : `google.cloud.dataproc.v1.BatchController.ComputeTuningConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.batches.computeTuningConfig - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.ComputeTuningConfig" `  




#### `CreateBatch`

  * **Method** : `google.cloud.dataproc.v1.BatchController.CreateBatch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.batches.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.CreateBatch" `  




#### `DeleteBatch`

  * **Method** : `google.cloud.dataproc.v1.BatchController.DeleteBatch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.batches.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.DeleteBatch" `  




#### `GetBatch`

  * **Method** : `google.cloud.dataproc.v1.BatchController.GetBatch`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.batches.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.GetBatch" `  




#### `ListBatches`

  * **Method** : `google.cloud.dataproc.v1.BatchController.ListBatches`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.batches.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.ListBatches" `  




#### `SearchSparkApplicationExecutors`

  * **Method** : `google.cloud.dataproc.v1.BatchController.SearchSparkApplicationExecutors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.batches.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.SearchSparkApplicationExecutors" `  




#### `SearchSparkApplicationJobs`

  * **Method** : `google.cloud.dataproc.v1.BatchController.SearchSparkApplicationJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.batches.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.SearchSparkApplicationJobs" `  




#### `SearchSparkApplicationNativeSqlQueries`

  * **Method** : `google.cloud.dataproc.v1.BatchController.SearchSparkApplicationNativeSqlQueries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.batches.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.SearchSparkApplicationNativeSqlQueries" `  




#### `SearchSparkApplicationSqlQueries`

  * **Method** : `google.cloud.dataproc.v1.BatchController.SearchSparkApplicationSqlQueries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.batches.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.SearchSparkApplicationSqlQueries" `  




#### `SearchSparkApplicationStageAttemptTasks`

  * **Method** : `google.cloud.dataproc.v1.BatchController.SearchSparkApplicationStageAttemptTasks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.batches.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.SearchSparkApplicationStageAttemptTasks" `  




#### `SearchSparkApplicationStageAttempts`

  * **Method** : `google.cloud.dataproc.v1.BatchController.SearchSparkApplicationStageAttempts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.batches.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.SearchSparkApplicationStageAttempts" `  




#### `SearchSparkApplicationStages`

  * **Method** : `google.cloud.dataproc.v1.BatchController.SearchSparkApplicationStages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.batches.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.SearchSparkApplicationStages" `  




#### `SearchSparkApplications`

  * **Method** : `google.cloud.dataproc.v1.BatchController.SearchSparkApplications`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.batches.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.SearchSparkApplications" `  




#### `WriteSparkApplicationContext`

  * **Method** : `google.cloud.dataproc.v1.BatchController.WriteSparkApplicationContext`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.batches.sparkApplicationWrite - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.BatchController.WriteSparkApplicationContext" `  




### `google.cloud.dataproc.v1.ClusterController`

The following audit logs are associated with methods belonging to `google.cloud.dataproc.v1.ClusterController`.

#### `CreateCluster`

  * **Method** : `google.cloud.dataproc.v1.ClusterController.CreateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.autoscalingPolicies.use - ADMIN_READ`
    * `dataproc.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.ClusterController.CreateCluster" `  




#### `DeleteCluster`

  * **Method** : `google.cloud.dataproc.v1.ClusterController.DeleteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.clusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.ClusterController.DeleteCluster" `  




#### `DiagnoseCluster`

  * **Method** : `google.cloud.dataproc.v1.ClusterController.DiagnoseCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.clusters.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.ClusterController.DiagnoseCluster" `  




#### `GetCluster`

  * **Method** : `google.cloud.dataproc.v1.ClusterController.GetCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.ClusterController.GetCluster" `  




#### `InjectCredentials`

  * **Method** : `google.cloud.dataproc.v1.ClusterController.InjectCredentials`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.clusters.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.ClusterController.InjectCredentials" `  




#### `ListClusters`

  * **Method** : `google.cloud.dataproc.v1.ClusterController.ListClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.clusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.ClusterController.ListClusters" `  




#### `RepairCluster`

  * **Method** : `google.cloud.dataproc.v1.ClusterController.RepairCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.googleapis.com/clusters.repair - ADMIN_WRITE`
    * `dataproc.googleapis.com/clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.ClusterController.RepairCluster" `  




#### `StartCluster`

  * **Method** : `google.cloud.dataproc.v1.ClusterController.StartCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.clusters.start - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.ClusterController.StartCluster" `  




#### `StopCluster`

  * **Method** : `google.cloud.dataproc.v1.ClusterController.StopCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.clusters.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.ClusterController.StopCluster" `  




#### `UpdateCluster`

  * **Method** : `google.cloud.dataproc.v1.ClusterController.UpdateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.ClusterController.UpdateCluster" `  




### `google.cloud.dataproc.v1.JobController`

The following audit logs are associated with methods belonging to `google.cloud.dataproc.v1.JobController`.

#### `CancelJob`

  * **Method** : `google.cloud.dataproc.v1.JobController.CancelJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.jobs.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.JobController.CancelJob" `  




#### `DeleteJob`

  * **Method** : `google.cloud.dataproc.v1.JobController.DeleteJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.jobs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.JobController.DeleteJob" `  




#### `GetJob`

  * **Method** : `google.cloud.dataproc.v1.JobController.GetJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.jobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.JobController.GetJob" `  




#### `ListJobs`

  * **Method** : `google.cloud.dataproc.v1.JobController.ListJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.jobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.JobController.ListJobs" `  




#### `SubmitJob`

  * **Method** : `google.cloud.dataproc.v1.JobController.SubmitJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.clusters.use - ADMIN_WRITE`
    * `dataproc.jobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.JobController.SubmitJob" `  




#### `SubmitJobAsOperation`

  * **Method** : `google.cloud.dataproc.v1.JobController.SubmitJobAsOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.clusters.use - ADMIN_WRITE`
    * `dataproc.jobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.JobController.SubmitJobAsOperation" `  




#### `UpdateJob`

  * **Method** : `google.cloud.dataproc.v1.JobController.UpdateJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.jobs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.JobController.UpdateJob" `  




### `google.cloud.dataproc.v1.NodeGroupController`

The following audit logs are associated with methods belonging to `google.cloud.dataproc.v1.NodeGroupController`.

#### `CreateNodeGroup`

  * **Method** : `google.cloud.dataproc.v1.NodeGroupController.CreateNodeGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.nodeGroups.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.NodeGroupController.CreateNodeGroup" `  




#### `GetNodeGroup`

  * **Method** : `google.cloud.dataproc.v1.NodeGroupController.GetNodeGroup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.nodeGroups.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.NodeGroupController.GetNodeGroup" `  




#### `RepairNodeGroup`

  * **Method** : `google.cloud.dataproc.v1.NodeGroupController.RepairNodeGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.nodeGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.NodeGroupController.RepairNodeGroup" `  




#### `ResizeNodeGroup`

  * **Method** : `google.cloud.dataproc.v1.NodeGroupController.ResizeNodeGroup`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.nodeGroups.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.NodeGroupController.ResizeNodeGroup" `  




### `google.cloud.dataproc.v1.SessionController`

The following audit logs are associated with methods belonging to `google.cloud.dataproc.v1.SessionController`.

#### `AccessSessionSparkApplication`

  * **Method** : `google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplication`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplication" `  




#### `AccessSessionSparkApplicationEnvironmentInfo`

  * **Method** : `google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationEnvironmentInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationEnvironmentInfo" `  




#### `AccessSessionSparkApplicationJob`

  * **Method** : `google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationJob" `  




#### `AccessSessionSparkApplicationNativeBuildInfo`

  * **Method** : `google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationNativeBuildInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationNativeBuildInfo" `  




#### `AccessSessionSparkApplicationNativeSqlQuery`

  * **Method** : `google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationNativeSqlQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationNativeSqlQuery" `  




#### `AccessSessionSparkApplicationSqlQuery`

  * **Method** : `google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationSqlQuery`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationSqlQuery" `  




#### `AccessSessionSparkApplicationSqlSparkPlanGraph`

  * **Method** : `google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationSqlSparkPlanGraph`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationSqlSparkPlanGraph" `  




#### `AccessSessionSparkApplicationStageAttempt`

  * **Method** : `google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationStageAttempt`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationStageAttempt" `  




#### `AccessSessionSparkApplicationStageRddOperationGraph`

  * **Method** : `google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationStageRddOperationGraph`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.AccessSessionSparkApplicationStageRddOperationGraph" `  




#### `CreateSession`

  * **Method** : `google.cloud.dataproc.v1.SessionController.CreateSession`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.sessions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.CreateSession" `  




#### `DeleteSession`

  * **Method** : `google.cloud.dataproc.v1.SessionController.DeleteSession`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.sessions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.DeleteSession" `  




#### `GetSession`

  * **Method** : `google.cloud.dataproc.v1.SessionController.GetSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.GetSession" `  




#### `ListSessions`

  * **Method** : `google.cloud.dataproc.v1.SessionController.ListSessions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.ListSessions" `  




#### `SearchSessionSparkApplicationExecutorStageSummary`

  * **Method** : `google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationExecutorStageSummary`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationExecutorStageSummary" `  




#### `SearchSessionSparkApplicationExecutors`

  * **Method** : `google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationExecutors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationExecutors" `  




#### `SearchSessionSparkApplicationJobs`

  * **Method** : `google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationJobs" `  




#### `SearchSessionSparkApplicationNativeSqlQueries`

  * **Method** : `google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationNativeSqlQueries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationNativeSqlQueries" `  




#### `SearchSessionSparkApplicationSqlQueries`

  * **Method** : `google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationSqlQueries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationSqlQueries" `  




#### `SearchSessionSparkApplicationStageAttemptTasks`

  * **Method** : `google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationStageAttemptTasks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationStageAttemptTasks" `  




#### `SearchSessionSparkApplicationStageAttempts`

  * **Method** : `google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationStageAttempts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationStageAttempts" `  




#### `SearchSessionSparkApplicationStages`

  * **Method** : `google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationStages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplicationStages" `  




#### `SearchSessionSparkApplications`

  * **Method** : `google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplications`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.SearchSessionSparkApplications" `  




#### `SummarizeSessionSparkApplicationExecutors`

  * **Method** : `google.cloud.dataproc.v1.SessionController.SummarizeSessionSparkApplicationExecutors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.SummarizeSessionSparkApplicationExecutors" `  




#### `SummarizeSessionSparkApplicationJobs`

  * **Method** : `google.cloud.dataproc.v1.SessionController.SummarizeSessionSparkApplicationJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.SummarizeSessionSparkApplicationJobs" `  




#### `SummarizeSessionSparkApplicationStageAttemptTasks`

  * **Method** : `google.cloud.dataproc.v1.SessionController.SummarizeSessionSparkApplicationStageAttemptTasks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.SummarizeSessionSparkApplicationStageAttemptTasks" `  




#### `SummarizeSessionSparkApplicationStages`

  * **Method** : `google.cloud.dataproc.v1.SessionController.SummarizeSessionSparkApplicationStages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.SummarizeSessionSparkApplicationStages" `  




#### `TerminateSession`

  * **Method** : `google.cloud.dataproc.v1.SessionController.TerminateSession`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.sessions.terminate - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.TerminateSession" `  




#### `WriteSessionSparkApplicationContext`

  * **Method** : `google.cloud.dataproc.v1.SessionController.WriteSessionSparkApplicationContext`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessions.sparkApplicationWrite - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionController.WriteSessionSparkApplicationContext" `  




### `google.cloud.dataproc.v1.SessionTemplateController`

The following audit logs are associated with methods belonging to `google.cloud.dataproc.v1.SessionTemplateController`.

#### `CreateSessionTemplate`

  * **Method** : `google.cloud.dataproc.v1.SessionTemplateController.CreateSessionTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.sessionTemplates.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionTemplateController.CreateSessionTemplate" `  




#### `DeleteSessionTemplate`

  * **Method** : `google.cloud.dataproc.v1.SessionTemplateController.DeleteSessionTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.sessionTemplates.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionTemplateController.DeleteSessionTemplate" `  




#### `GetSessionTemplate`

  * **Method** : `google.cloud.dataproc.v1.SessionTemplateController.GetSessionTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessionTemplates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionTemplateController.GetSessionTemplate" `  




#### `ListSessionTemplates`

  * **Method** : `google.cloud.dataproc.v1.SessionTemplateController.ListSessionTemplates`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.sessionTemplates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionTemplateController.ListSessionTemplates" `  




#### `UpdateSessionTemplate`

  * **Method** : `google.cloud.dataproc.v1.SessionTemplateController.UpdateSessionTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.sessionTemplates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.SessionTemplateController.UpdateSessionTemplate" `  




### `google.cloud.dataproc.v1.WorkflowTemplateService`

The following audit logs are associated with methods belonging to `google.cloud.dataproc.v1.WorkflowTemplateService`.

#### `CreateWorkflowTemplate`

  * **Method** : `google.cloud.dataproc.v1.WorkflowTemplateService.CreateWorkflowTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.workflowTemplates.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.WorkflowTemplateService.CreateWorkflowTemplate" `  




#### `DeleteWorkflowTemplate`

  * **Method** : `google.cloud.dataproc.v1.WorkflowTemplateService.DeleteWorkflowTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.workflowTemplates.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.WorkflowTemplateService.DeleteWorkflowTemplate" `  




#### `GetWorkflowTemplate`

  * **Method** : `google.cloud.dataproc.v1.WorkflowTemplateService.GetWorkflowTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.workflowTemplates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.WorkflowTemplateService.GetWorkflowTemplate" `  




#### `InstantiateInlineWorkflowTemplate`

  * **Method** : `google.cloud.dataproc.v1.WorkflowTemplateService.InstantiateInlineWorkflowTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.workflowTemplates.instantiateInline - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.WorkflowTemplateService.InstantiateInlineWorkflowTemplate" `  




#### `InstantiateWorkflowTemplate`

  * **Method** : `google.cloud.dataproc.v1.WorkflowTemplateService.InstantiateWorkflowTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.workflowTemplates.instantiate - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.WorkflowTemplateService.InstantiateWorkflowTemplate" `  




#### `ListWorkflowTemplates`

  * **Method** : `google.cloud.dataproc.v1.WorkflowTemplateService.ListWorkflowTemplates`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.workflowTemplates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.WorkflowTemplateService.ListWorkflowTemplates" `  




#### `UpdateWorkflowTemplate`

  * **Method** : `google.cloud.dataproc.v1.WorkflowTemplateService.UpdateWorkflowTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.workflowTemplates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1.WorkflowTemplateService.UpdateWorkflowTemplate" `  




### `google.cloud.dataproc.v1beta2.AutoscalingPolicyService`

The following audit logs are associated with methods belonging to `google.cloud.dataproc.v1beta2.AutoscalingPolicyService`.

#### `CreateAutoscalingPolicy`

  * **Method** : `google.cloud.dataproc.v1beta2.AutoscalingPolicyService.CreateAutoscalingPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.autoscalingPolicies.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.AutoscalingPolicyService.CreateAutoscalingPolicy" `  




#### `DeleteAutoscalingPolicy`

  * **Method** : `google.cloud.dataproc.v1beta2.AutoscalingPolicyService.DeleteAutoscalingPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.autoscalingPolicies.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.AutoscalingPolicyService.DeleteAutoscalingPolicy" `  




#### `GetAutoscalingPolicy`

  * **Method** : `google.cloud.dataproc.v1beta2.AutoscalingPolicyService.GetAutoscalingPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.autoscalingPolicies.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.AutoscalingPolicyService.GetAutoscalingPolicy" `  




#### `ListAutoscalingPolicies`

  * **Method** : `google.cloud.dataproc.v1beta2.AutoscalingPolicyService.ListAutoscalingPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.autoscalingPolicies.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.AutoscalingPolicyService.ListAutoscalingPolicies" `  




#### `UpdateAutoscalingPolicy`

  * **Method** : `google.cloud.dataproc.v1beta2.AutoscalingPolicyService.UpdateAutoscalingPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.autoscalingPolicies.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.AutoscalingPolicyService.UpdateAutoscalingPolicy" `  




### `google.cloud.dataproc.v1beta2.ClusterController`

The following audit logs are associated with methods belonging to `google.cloud.dataproc.v1beta2.ClusterController`.

#### `CreateCluster`

  * **Method** : `google.cloud.dataproc.v1beta2.ClusterController.CreateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.ClusterController.CreateCluster" `  




#### `DeleteCluster`

  * **Method** : `google.cloud.dataproc.v1beta2.ClusterController.DeleteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.clusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.ClusterController.DeleteCluster" `  




#### `DiagnoseCluster`

  * **Method** : `google.cloud.dataproc.v1beta2.ClusterController.DiagnoseCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.clusters.use - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.ClusterController.DiagnoseCluster" `  




#### `GetCluster`

  * **Method** : `google.cloud.dataproc.v1beta2.ClusterController.GetCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.ClusterController.GetCluster" `  




#### `ListClusters`

  * **Method** : `google.cloud.dataproc.v1beta2.ClusterController.ListClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.clusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.ClusterController.ListClusters" `  




#### `StartCluster`

  * **Method** : `google.cloud.dataproc.v1beta2.ClusterController.StartCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.clusters.start - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.ClusterController.StartCluster" `  




#### `StopCluster`

  * **Method** : `google.cloud.dataproc.v1beta2.ClusterController.StopCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.clusters.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.ClusterController.StopCluster" `  




#### `UpdateCluster`

  * **Method** : `google.cloud.dataproc.v1beta2.ClusterController.UpdateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.ClusterController.UpdateCluster" `  




### `google.cloud.dataproc.v1beta2.JobController`

The following audit logs are associated with methods belonging to `google.cloud.dataproc.v1beta2.JobController`.

#### `CancelJob`

  * **Method** : `google.cloud.dataproc.v1beta2.JobController.CancelJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.jobs.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.JobController.CancelJob" `  




#### `DeleteJob`

  * **Method** : `google.cloud.dataproc.v1beta2.JobController.DeleteJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.jobs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.JobController.DeleteJob" `  




#### `GetJob`

  * **Method** : `google.cloud.dataproc.v1beta2.JobController.GetJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.jobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.JobController.GetJob" `  




#### `ListJobs`

  * **Method** : `google.cloud.dataproc.v1beta2.JobController.ListJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.jobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.JobController.ListJobs" `  




#### `SubmitJob`

  * **Method** : `google.cloud.dataproc.v1beta2.JobController.SubmitJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.clusters.use - ADMIN_WRITE`
    * `dataproc.jobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.JobController.SubmitJob" `  




#### `SubmitJobAsOperation`

  * **Method** : `google.cloud.dataproc.v1beta2.JobController.SubmitJobAsOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.clusters.use - ADMIN_WRITE`
    * `dataproc.jobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.JobController.SubmitJobAsOperation" `  




#### `UpdateJob`

  * **Method** : `google.cloud.dataproc.v1beta2.JobController.UpdateJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.jobs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.JobController.UpdateJob" `  




### `google.cloud.dataproc.v1beta2.WorkflowTemplateService`

The following audit logs are associated with methods belonging to `google.cloud.dataproc.v1beta2.WorkflowTemplateService`.

#### `CreateWorkflowTemplate`

  * **Method** : `google.cloud.dataproc.v1beta2.WorkflowTemplateService.CreateWorkflowTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.workflowTemplates.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.WorkflowTemplateService.CreateWorkflowTemplate" `  




#### `DeleteWorkflowTemplate`

  * **Method** : `google.cloud.dataproc.v1beta2.WorkflowTemplateService.DeleteWorkflowTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.workflowTemplates.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.WorkflowTemplateService.DeleteWorkflowTemplate" `  




#### `GetWorkflowTemplate`

  * **Method** : `google.cloud.dataproc.v1beta2.WorkflowTemplateService.GetWorkflowTemplate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.workflowTemplates.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.WorkflowTemplateService.GetWorkflowTemplate" `  




#### `InstantiateInlineWorkflowTemplate`

  * **Method** : `google.cloud.dataproc.v1beta2.WorkflowTemplateService.InstantiateInlineWorkflowTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.workflowTemplates.instantiateInline - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.WorkflowTemplateService.InstantiateInlineWorkflowTemplate" `  




#### `InstantiateWorkflowTemplate`

  * **Method** : `google.cloud.dataproc.v1beta2.WorkflowTemplateService.InstantiateWorkflowTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.workflowTemplates.instantiate - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.WorkflowTemplateService.InstantiateWorkflowTemplate" `  




#### `ListWorkflowTemplates`

  * **Method** : `google.cloud.dataproc.v1beta2.WorkflowTemplateService.ListWorkflowTemplates`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.workflowTemplates.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.WorkflowTemplateService.ListWorkflowTemplates" `  




#### `UpdateWorkflowTemplate`

  * **Method** : `google.cloud.dataproc.v1beta2.WorkflowTemplateService.UpdateWorkflowTemplate`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.workflowTemplates.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.v1beta2.WorkflowTemplateService.UpdateWorkflowTemplate" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `google.iam.v1.IAMPolicy.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.jobs.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.IAMPolicy.GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `google.iam.v1.IAMPolicy.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.clusters.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.IAMPolicy.SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.batches.cancel - ADMIN_WRITE`
    * `dataproc.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataproc.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataproc.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
