---
url: https://docs.cloud.google.com/dataflow/docs/audit-logging-data-pipeline/
title: Data Pipelines audit logging \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:49.434868+00:00
---

# Data Pipelines audit logging  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/audit-logging-data-pipeline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Data Pipelines audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Data Pipelines. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Data Pipelines audit logs use the service name `datapipelines.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="datapipelines.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Data Pipelines generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`DATA_READ` | `google.cloud.datapipelines.v1.Pipelines.GetPipeline`  
`google.cloud.datapipelines.v1.Pipelines.ListJobs`  
`google.cloud.datapipelines.v1.Pipelines.ListPipelines`  
`DATA_WRITE` | `google.cloud.datapipelines.v1.Pipelines.CreatePipeline`  
`google.cloud.datapipelines.v1.Pipelines.DeletePipeline`  
`google.cloud.datapipelines.v1.Pipelines.RunPipeline`  
`google.cloud.datapipelines.v1.Pipelines.StopPipeline`  
`google.cloud.datapipelines.v1.Pipelines.UpdatePipeline`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Data Pipelines.

### `google.cloud.datapipelines.v1.Pipelines`

The following audit logs are associated with methods belonging to `google.cloud.datapipelines.v1.Pipelines`.

#### `CreatePipeline`

  * **Method** : `google.cloud.datapipelines.v1.Pipelines.CreatePipeline`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datapipelines.pipelines.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datapipelines.v1.Pipelines.CreatePipeline" `  




#### `DeletePipeline`

  * **Method** : `google.cloud.datapipelines.v1.Pipelines.DeletePipeline`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datapipelines.pipelines.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datapipelines.v1.Pipelines.DeletePipeline" `  




#### `GetPipeline`

  * **Method** : `google.cloud.datapipelines.v1.Pipelines.GetPipeline`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datapipelines.pipelines.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datapipelines.v1.Pipelines.GetPipeline" `  




#### `ListJobs`

  * **Method** : `google.cloud.datapipelines.v1.Pipelines.ListJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datapipelines.jobs.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datapipelines.v1.Pipelines.ListJobs" `  




#### `ListPipelines`

  * **Method** : `google.cloud.datapipelines.v1.Pipelines.ListPipelines`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datapipelines.pipelines.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datapipelines.v1.Pipelines.ListPipelines" `  




#### `RunPipeline`

  * **Method** : `google.cloud.datapipelines.v1.Pipelines.RunPipeline`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datapipelines.pipelines.run - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datapipelines.v1.Pipelines.RunPipeline" `  




#### `StopPipeline`

  * **Method** : `google.cloud.datapipelines.v1.Pipelines.StopPipeline`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datapipelines.pipelines.stop - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datapipelines.v1.Pipelines.StopPipeline" `  




#### `UpdatePipeline`

  * **Method** : `google.cloud.datapipelines.v1.Pipelines.UpdatePipeline`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datapipelines.pipelines.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datapipelines.v1.Pipelines.UpdatePipeline" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
