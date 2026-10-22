---
url: https://docs.cloud.google.com/batch/docs/audit-logging/
title: Batch audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:29.154418+00:00
---

# Batch audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Batch audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Batch. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Batch audit logs use the service name `batch.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="batch.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Batch generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.batch.v1.BatchService.GetTask`  
`google.cloud.batch.v1.BatchService.ListTasks`  
`google.cloud.batch.v1alpha.BatchService.GetTask`  
`google.cloud.batch.v1alpha.BatchService.ListTasks`  
`DATA_READ` | `google.cloud.batch.v1.BatchService.GetJob`  
`google.cloud.batch.v1.BatchService.ListJobs`  
`google.cloud.batch.v1alpha.BatchService.GetJob`  
`google.cloud.batch.v1alpha.BatchService.GetResourceAllowance`  
`google.cloud.batch.v1alpha.BatchService.ListJobs`  
`google.cloud.batch.v1alpha.BatchService.ListResourceAllowances`  
`DATA_WRITE` | `google.cloud.batch.v1.BatchService.CreateJob`  
`google.cloud.batch.v1.BatchService.DeleteJob` (LRO)  
`google.cloud.batch.v1alpha.BatchService.CreateJob`  
`google.cloud.batch.v1alpha.BatchService.CreateResourceAllowance`  
`google.cloud.batch.v1alpha.BatchService.DeleteJob` (LRO)  
`google.cloud.batch.v1alpha.BatchService.DeleteResourceAllowance` (LRO)  
`google.cloud.batch.v1alpha.BatchService.UpdateResourceAllowance`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Batch.

### `google.cloud.batch.v1.BatchService`

The following audit logs are associated with methods belonging to `google.cloud.batch.v1.BatchService`.

#### `CreateJob`

  * **Method** : `google.cloud.batch.v1.BatchService.CreateJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `batch.jobs.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.batch.v1.BatchService.CreateJob" `  




#### `DeleteJob`

  * **Method** : `google.cloud.batch.v1.BatchService.DeleteJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `batch.jobs.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.batch.v1.BatchService.DeleteJob" `  




#### `GetJob`

  * **Method** : `google.cloud.batch.v1.BatchService.GetJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `batch.jobs.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.batch.v1.BatchService.GetJob" `  




#### `GetTask`

  * **Method** : `google.cloud.batch.v1.BatchService.GetTask`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `batch.tasks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.batch.v1.BatchService.GetTask" `  




#### `ListJobs`

  * **Method** : `google.cloud.batch.v1.BatchService.ListJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `batch.jobs.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.batch.v1.BatchService.ListJobs" `  




#### `ListTasks`

  * **Method** : `google.cloud.batch.v1.BatchService.ListTasks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `batch.tasks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.batch.v1.BatchService.ListTasks" `  




### `google.cloud.batch.v1alpha.BatchService`

The following audit logs are associated with methods belonging to `google.cloud.batch.v1alpha.BatchService`.

#### `CreateJob`

  * **Method** : `google.cloud.batch.v1alpha.BatchService.CreateJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `batch.jobs.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.batch.v1alpha.BatchService.CreateJob" `  




#### `CreateResourceAllowance`

  * **Method** : `google.cloud.batch.v1alpha.BatchService.CreateResourceAllowance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `batch.resourceAllowances.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.batch.v1alpha.BatchService.CreateResourceAllowance" `  




#### `DeleteJob`

  * **Method** : `google.cloud.batch.v1alpha.BatchService.DeleteJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `batch.jobs.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.batch.v1alpha.BatchService.DeleteJob" `  




#### `DeleteResourceAllowance`

  * **Method** : `google.cloud.batch.v1alpha.BatchService.DeleteResourceAllowance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `batch.resourceAllowances.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.batch.v1alpha.BatchService.DeleteResourceAllowance" `  




#### `GetJob`

  * **Method** : `google.cloud.batch.v1alpha.BatchService.GetJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `batch.jobs.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.batch.v1alpha.BatchService.GetJob" `  




#### `GetResourceAllowance`

  * **Method** : `google.cloud.batch.v1alpha.BatchService.GetResourceAllowance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `batch.resourceAllowances.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.batch.v1alpha.BatchService.GetResourceAllowance" `  




#### `GetTask`

  * **Method** : `google.cloud.batch.v1alpha.BatchService.GetTask`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `batch.tasks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.batch.v1alpha.BatchService.GetTask" `  




#### `ListJobs`

  * **Method** : `google.cloud.batch.v1alpha.BatchService.ListJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `batch.jobs.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.batch.v1alpha.BatchService.ListJobs" `  




#### `ListResourceAllowances`

  * **Method** : `google.cloud.batch.v1alpha.BatchService.ListResourceAllowances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `batch.resourceAllowances.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.batch.v1alpha.BatchService.ListResourceAllowances" `  




#### `ListTasks`

  * **Method** : `google.cloud.batch.v1alpha.BatchService.ListTasks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `batch.tasks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.batch.v1alpha.BatchService.ListTasks" `  




#### `UpdateResourceAllowance`

  * **Method** : `google.cloud.batch.v1alpha.BatchService.UpdateResourceAllowance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `batch.resourceAllowances.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.batch.v1alpha.BatchService.UpdateResourceAllowance" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.batch.v1.BatchService.ReportAgentState`
  * `google.cloud.batch.v1alpha.BatchService.ReportAgentState`
  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.DeleteOperation`
  * `google.longrunning.Operations.GetOperation`
  * `google.longrunning.Operations.ListOperations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
