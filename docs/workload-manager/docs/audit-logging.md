---
url: https://docs.cloud.google.com/workload-manager/docs/audit-logging/
title: Workload Manager audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:44.914548+00:00
---

# Workload Manager audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/workload-manager/docs/authentication)



Send feedback 

#  Workload Manager audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Workload Manager. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Workload Manager audit logs use the service name `workloadmanager.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="workloadmanager.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Workload Manager generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.workloadmanager.v1.WorkloadManager.GetEvaluation`  
`google.cloud.workloadmanager.v1.WorkloadManager.GetExecution`  
`google.cloud.workloadmanager.v1.WorkloadManager.ListEvaluations`  
`google.cloud.workloadmanager.v1.WorkloadManager.ListExecutionResults`  
`google.cloud.workloadmanager.v1.WorkloadManager.ListExecutions`  
`google.cloud.workloadmanager.v1.WorkloadManager.ListRules`  
`google.cloud.workloadmanager.v1.WorkloadManager.ListScannedResources`  
`google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.GetActuation`  
`google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.GetDeployment`  
`google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.ListActuations`  
`google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.ListDeployments`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.workloadmanager.v1.WorkloadManager.CreateEvaluation` (LRO)  
`google.cloud.workloadmanager.v1.WorkloadManager.DeleteEvaluation` (LRO)  
`google.cloud.workloadmanager.v1.WorkloadManager.DeleteExecution` (LRO)  
`google.cloud.workloadmanager.v1.WorkloadManager.RunEvaluation` (LRO)  
`google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.CreateActuation` (LRO)  
`google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.CreateDeployment` (LRO)  
`google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.DeleteActuation` (LRO)  
`google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.DeleteDeployment` (LRO)  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Workload Manager.

### `google.cloud.workloadmanager.v1.WorkloadManager`

The following audit logs are associated with methods belonging to `google.cloud.workloadmanager.v1.WorkloadManager`.

#### `CreateEvaluation`

  * **Method** : `google.cloud.workloadmanager.v1.WorkloadManager.CreateEvaluation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workloadmanager.evaluations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workloadmanager.v1.WorkloadManager.CreateEvaluation" `  




#### `DeleteEvaluation`

  * **Method** : `google.cloud.workloadmanager.v1.WorkloadManager.DeleteEvaluation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workloadmanager.evaluations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workloadmanager.v1.WorkloadManager.DeleteEvaluation" `  




#### `DeleteExecution`

  * **Method** : `google.cloud.workloadmanager.v1.WorkloadManager.DeleteExecution`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workloadmanager.executions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workloadmanager.v1.WorkloadManager.DeleteExecution" `  




#### `GetEvaluation`

  * **Method** : `google.cloud.workloadmanager.v1.WorkloadManager.GetEvaluation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workloadmanager.evaluations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workloadmanager.v1.WorkloadManager.GetEvaluation" `  




#### `GetExecution`

  * **Method** : `google.cloud.workloadmanager.v1.WorkloadManager.GetExecution`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workloadmanager.executions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workloadmanager.v1.WorkloadManager.GetExecution" `  




#### `ListEvaluations`

  * **Method** : `google.cloud.workloadmanager.v1.WorkloadManager.ListEvaluations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workloadmanager.evaluations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workloadmanager.v1.WorkloadManager.ListEvaluations" `  




#### `ListExecutionResults`

  * **Method** : `google.cloud.workloadmanager.v1.WorkloadManager.ListExecutionResults`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workloadmanager.results.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workloadmanager.v1.WorkloadManager.ListExecutionResults" `  




#### `ListExecutions`

  * **Method** : `google.cloud.workloadmanager.v1.WorkloadManager.ListExecutions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workloadmanager.executions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workloadmanager.v1.WorkloadManager.ListExecutions" `  




#### `ListRules`

  * **Method** : `google.cloud.workloadmanager.v1.WorkloadManager.ListRules`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workloadmanager.rules.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workloadmanager.v1.WorkloadManager.ListRules" `  




#### `ListScannedResources`

  * **Method** : `google.cloud.workloadmanager.v1.WorkloadManager.ListScannedResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workloadmanager.results.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workloadmanager.v1.WorkloadManager.ListScannedResources" `  




#### `RunEvaluation`

  * **Method** : `google.cloud.workloadmanager.v1.WorkloadManager.RunEvaluation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workloadmanager.evaluations.run - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workloadmanager.v1.WorkloadManager.RunEvaluation" `  




### `google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment`

The following audit logs are associated with methods belonging to `google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment`.

#### `CreateActuation`

  * **Method** : `google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.CreateActuation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workloadmanager.actuations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.CreateActuation" `  




#### `CreateDeployment`

  * **Method** : `google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.CreateDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workloadmanager.deployments.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.CreateDeployment" `  




#### `DeleteActuation`

  * **Method** : `google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.DeleteActuation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workloadmanager.actuations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.DeleteActuation" `  




#### `DeleteDeployment`

  * **Method** : `google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.DeleteDeployment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workloadmanager.deployments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.DeleteDeployment" `  




#### `GetActuation`

  * **Method** : `google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.GetActuation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workloadmanager.actuations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.GetActuation" `  




#### `GetDeployment`

  * **Method** : `google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.GetDeployment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workloadmanager.deployments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.GetDeployment" `  




#### `ListActuations`

  * **Method** : `google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.ListActuations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workloadmanager.actuations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.ListActuations" `  




#### `ListDeployments`

  * **Method** : `google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.ListDeployments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workloadmanager.deployments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workloadmanager.v1alpha.WorkloadManagerDeployment.ListDeployments" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workloadmanager.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workloadmanager.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workloadmanager.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workloadmanager.operations.list - ADMIN_READ`
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
  * `google.cloud.workloadmanager.datawarehouse.v1.DataCollectService.WriteInsight`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
