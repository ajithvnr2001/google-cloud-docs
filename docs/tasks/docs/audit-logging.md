---
url: https://docs.cloud.google.com/tasks/docs/audit-logging/
title: Cloud Tasks audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:40.845569+00:00
---

# Cloud Tasks audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Cloud Tasks audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Cloud Tasks. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Cloud Tasks audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="cloudtasks.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Tasks generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.tasks.v2.CloudTasks.GetCmekConfig`  
`google.cloud.tasks.v2.CloudTasks.GetIamPolicy`  
`google.cloud.tasks.v2.CloudTasks.GetQueue`  
`google.cloud.tasks.v2.CloudTasks.ListQueues`  
`google.cloud.tasks.v2beta2.CloudTasks.GetCmekConfig`  
`google.cloud.tasks.v2beta2.CloudTasks.GetIamPolicy`  
`google.cloud.tasks.v2beta2.CloudTasks.GetQueue`  
`google.cloud.tasks.v2beta2.CloudTasks.ListQueues`  
`google.cloud.tasks.v2beta3.CloudTasks.GetCmekConfig`  
`google.cloud.tasks.v2beta3.CloudTasks.GetIamPolicy`  
`google.cloud.tasks.v2beta3.CloudTasks.GetQueue`  
`google.cloud.tasks.v2beta3.CloudTasks.ListQueues`  
`ADMIN_WRITE` | `google.cloud.tasks.v2.CloudTasks.CreateQueue`  
`google.cloud.tasks.v2.CloudTasks.DeleteQueue`  
`google.cloud.tasks.v2.CloudTasks.PauseQueue`  
`google.cloud.tasks.v2.CloudTasks.PurgeQueue`  
`google.cloud.tasks.v2.CloudTasks.ResumeQueue`  
`google.cloud.tasks.v2.CloudTasks.SetIamPolicy`  
`google.cloud.tasks.v2.CloudTasks.UpdateCmekConfig`  
`google.cloud.tasks.v2.CloudTasks.UpdateQueue`  
`google.cloud.tasks.v2beta2.CloudTasks.CreateQueue`  
`google.cloud.tasks.v2beta2.CloudTasks.DeleteQueue`  
`google.cloud.tasks.v2beta2.CloudTasks.PauseQueue`  
`google.cloud.tasks.v2beta2.CloudTasks.PurgeQueue`  
`google.cloud.tasks.v2beta2.CloudTasks.ResumeQueue`  
`google.cloud.tasks.v2beta2.CloudTasks.SetIamPolicy`  
`google.cloud.tasks.v2beta2.CloudTasks.UpdateCmekConfig`  
`google.cloud.tasks.v2beta2.CloudTasks.UpdateQueue`  
`google.cloud.tasks.v2beta2.CloudTasks.UploadQueueYaml`  
`google.cloud.tasks.v2beta3.CloudTasks.CreateQueue`  
`google.cloud.tasks.v2beta3.CloudTasks.DeleteQueue`  
`google.cloud.tasks.v2beta3.CloudTasks.PauseQueue`  
`google.cloud.tasks.v2beta3.CloudTasks.PurgeQueue`  
`google.cloud.tasks.v2beta3.CloudTasks.ResumeQueue`  
`google.cloud.tasks.v2beta3.CloudTasks.SetIamPolicy`  
`google.cloud.tasks.v2beta3.CloudTasks.UpdateCmekConfig`  
`google.cloud.tasks.v2beta3.CloudTasks.UpdateQueue`  
`DATA_READ` | `google.cloud.tasks.v2.CloudTasks.GetTask`  
`google.cloud.tasks.v2.CloudTasks.ListTasks`  
`google.cloud.tasks.v2beta2.CloudTasks.GetTask`  
`google.cloud.tasks.v2beta2.CloudTasks.ListTasks`  
`google.cloud.tasks.v2beta3.CloudTasks.GetTask`  
`google.cloud.tasks.v2beta3.CloudTasks.ListTasks`  
`DATA_WRITE` | `google.cloud.tasks.v2.CloudTasks.BatchDeleteTasks`  
`google.cloud.tasks.v2.CloudTasks.DeleteTask`  
`google.cloud.tasks.v2.CloudTasks.RunTask`  
`google.cloud.tasks.v2beta2.CloudTasks.BatchDeleteTasks`  
`google.cloud.tasks.v2beta2.CloudTasks.DeleteTask`  
`google.cloud.tasks.v2beta2.CloudTasks.RunTask`  
`google.cloud.tasks.v2beta3.CloudTasks.BatchDeleteTasks`  
`google.cloud.tasks.v2beta3.CloudTasks.DeleteTask`  
`google.cloud.tasks.v2beta3.CloudTasks.RunTask`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Tasks.

### `google.cloud.tasks.v2.CloudTasks`

The following audit logs are associated with methods belonging to `google.cloud.tasks.v2.CloudTasks`.

#### `BatchDeleteTasks`

  * **Method** : `google.cloud.tasks.v2.CloudTasks.BatchDeleteTasks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.tasks.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2.CloudTasks.BatchDeleteTasks" `  




#### `CreateQueue`

  * **Method** : `google.cloud.tasks.v2.CloudTasks.CreateQueue`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2.CloudTasks.CreateQueue" `  




#### `DeleteQueue`

  * **Method** : `google.cloud.tasks.v2.CloudTasks.DeleteQueue`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2.CloudTasks.DeleteQueue" `  




#### `DeleteTask`

  * **Method** : `google.cloud.tasks.v2.CloudTasks.DeleteTask`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.tasks.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2.CloudTasks.DeleteTask" `  




#### `GetCmekConfig`

  * **Method** : `google.cloud.tasks.v2.CloudTasks.GetCmekConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.cmekConfig.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2.CloudTasks.GetCmekConfig" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.tasks.v2.CloudTasks.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.queues.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2.CloudTasks.GetIamPolicy" `  




#### `GetQueue`

  * **Method** : `google.cloud.tasks.v2.CloudTasks.GetQueue`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.queues.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2.CloudTasks.GetQueue" `  




#### `GetTask`

  * **Method** : `google.cloud.tasks.v2.CloudTasks.GetTask`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.tasks.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2.CloudTasks.GetTask" `  




#### `ListQueues`

  * **Method** : `google.cloud.tasks.v2.CloudTasks.ListQueues`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.queues.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2.CloudTasks.ListQueues" `  




#### `ListTasks`

  * **Method** : `google.cloud.tasks.v2.CloudTasks.ListTasks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.tasks.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2.CloudTasks.ListTasks" `  




#### `PauseQueue`

  * **Method** : `google.cloud.tasks.v2.CloudTasks.PauseQueue`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.pause - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2.CloudTasks.PauseQueue" `  




#### `PurgeQueue`

  * **Method** : `google.cloud.tasks.v2.CloudTasks.PurgeQueue`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.purge - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2.CloudTasks.PurgeQueue" `  




#### `ResumeQueue`

  * **Method** : `google.cloud.tasks.v2.CloudTasks.ResumeQueue`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.resume - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2.CloudTasks.ResumeQueue" `  




#### `RunTask`

  * **Method** : `google.cloud.tasks.v2.CloudTasks.RunTask`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.tasks.run - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2.CloudTasks.RunTask" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.tasks.v2.CloudTasks.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2.CloudTasks.SetIamPolicy" `  




#### `UpdateCmekConfig`

  * **Method** : `google.cloud.tasks.v2.CloudTasks.UpdateCmekConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.cmekConfig.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2.CloudTasks.UpdateCmekConfig" `  




#### `UpdateQueue`

  * **Method** : `google.cloud.tasks.v2.CloudTasks.UpdateQueue`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2.CloudTasks.UpdateQueue" `  




### `google.cloud.tasks.v2beta2.CloudTasks`

The following audit logs are associated with methods belonging to `google.cloud.tasks.v2beta2.CloudTasks`.

#### `BatchDeleteTasks`

  * **Method** : `google.cloud.tasks.v2beta2.CloudTasks.BatchDeleteTasks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.tasks.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta2.CloudTasks.BatchDeleteTasks" `  




#### `CreateQueue`

  * **Method** : `google.cloud.tasks.v2beta2.CloudTasks.CreateQueue`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta2.CloudTasks.CreateQueue" `  




#### `DeleteQueue`

  * **Method** : `google.cloud.tasks.v2beta2.CloudTasks.DeleteQueue`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta2.CloudTasks.DeleteQueue" `  




#### `DeleteTask`

  * **Method** : `google.cloud.tasks.v2beta2.CloudTasks.DeleteTask`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.tasks.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta2.CloudTasks.DeleteTask" `  




#### `GetCmekConfig`

  * **Method** : `google.cloud.tasks.v2beta2.CloudTasks.GetCmekConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.cmekConfig.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta2.CloudTasks.GetCmekConfig" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.tasks.v2beta2.CloudTasks.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.queues.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta2.CloudTasks.GetIamPolicy" `  




#### `GetQueue`

  * **Method** : `google.cloud.tasks.v2beta2.CloudTasks.GetQueue`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.queues.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta2.CloudTasks.GetQueue" `  




#### `GetTask`

  * **Method** : `google.cloud.tasks.v2beta2.CloudTasks.GetTask`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.tasks.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta2.CloudTasks.GetTask" `  




#### `ListQueues`

  * **Method** : `google.cloud.tasks.v2beta2.CloudTasks.ListQueues`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.queues.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta2.CloudTasks.ListQueues" `  




#### `ListTasks`

  * **Method** : `google.cloud.tasks.v2beta2.CloudTasks.ListTasks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.tasks.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta2.CloudTasks.ListTasks" `  




#### `PauseQueue`

  * **Method** : `google.cloud.tasks.v2beta2.CloudTasks.PauseQueue`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.pause - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta2.CloudTasks.PauseQueue" `  




#### `PurgeQueue`

  * **Method** : `google.cloud.tasks.v2beta2.CloudTasks.PurgeQueue`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.purge - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta2.CloudTasks.PurgeQueue" `  




#### `ResumeQueue`

  * **Method** : `google.cloud.tasks.v2beta2.CloudTasks.ResumeQueue`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.resume - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta2.CloudTasks.ResumeQueue" `  




#### `RunTask`

  * **Method** : `google.cloud.tasks.v2beta2.CloudTasks.RunTask`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.tasks.run - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta2.CloudTasks.RunTask" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.tasks.v2beta2.CloudTasks.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta2.CloudTasks.SetIamPolicy" `  




#### `UpdateCmekConfig`

  * **Method** : `google.cloud.tasks.v2beta2.CloudTasks.UpdateCmekConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.cmekConfig.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta2.CloudTasks.UpdateCmekConfig" `  




#### `UpdateQueue`

  * **Method** : `google.cloud.tasks.v2beta2.CloudTasks.UpdateQueue`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta2.CloudTasks.UpdateQueue" `  




#### `UploadQueueYaml`

  * **Method** : `google.cloud.tasks.v2beta2.CloudTasks.UploadQueueYaml`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.create - ADMIN_WRITE`
    * `cloudtasks.queues.pause - ADMIN_WRITE`
    * `cloudtasks.queues.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta2.CloudTasks.UploadQueueYaml" `  




### `google.cloud.tasks.v2beta3.CloudTasks`

The following audit logs are associated with methods belonging to `google.cloud.tasks.v2beta3.CloudTasks`.

#### `BatchDeleteTasks`

  * **Method** : `google.cloud.tasks.v2beta3.CloudTasks.BatchDeleteTasks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.tasks.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta3.CloudTasks.BatchDeleteTasks" `  




#### `CreateQueue`

  * **Method** : `google.cloud.tasks.v2beta3.CloudTasks.CreateQueue`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta3.CloudTasks.CreateQueue" `  




#### `DeleteQueue`

  * **Method** : `google.cloud.tasks.v2beta3.CloudTasks.DeleteQueue`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta3.CloudTasks.DeleteQueue" `  




#### `DeleteTask`

  * **Method** : `google.cloud.tasks.v2beta3.CloudTasks.DeleteTask`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.tasks.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta3.CloudTasks.DeleteTask" `  




#### `GetCmekConfig`

  * **Method** : `google.cloud.tasks.v2beta3.CloudTasks.GetCmekConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.cmekConfig.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta3.CloudTasks.GetCmekConfig" `  




#### `GetIamPolicy`

  * **Method** : `google.cloud.tasks.v2beta3.CloudTasks.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.queues.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta3.CloudTasks.GetIamPolicy" `  




#### `GetQueue`

  * **Method** : `google.cloud.tasks.v2beta3.CloudTasks.GetQueue`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.queues.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta3.CloudTasks.GetQueue" `  




#### `GetTask`

  * **Method** : `google.cloud.tasks.v2beta3.CloudTasks.GetTask`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.tasks.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta3.CloudTasks.GetTask" `  




#### `ListQueues`

  * **Method** : `google.cloud.tasks.v2beta3.CloudTasks.ListQueues`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.queues.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta3.CloudTasks.ListQueues" `  




#### `ListTasks`

  * **Method** : `google.cloud.tasks.v2beta3.CloudTasks.ListTasks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.tasks.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta3.CloudTasks.ListTasks" `  




#### `PauseQueue`

  * **Method** : `google.cloud.tasks.v2beta3.CloudTasks.PauseQueue`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.pause - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta3.CloudTasks.PauseQueue" `  




#### `PurgeQueue`

  * **Method** : `google.cloud.tasks.v2beta3.CloudTasks.PurgeQueue`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.purge - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta3.CloudTasks.PurgeQueue" `  




#### `ResumeQueue`

  * **Method** : `google.cloud.tasks.v2beta3.CloudTasks.ResumeQueue`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.resume - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta3.CloudTasks.ResumeQueue" `  




#### `RunTask`

  * **Method** : `google.cloud.tasks.v2beta3.CloudTasks.RunTask`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudtasks.tasks.run - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta3.CloudTasks.RunTask" `  




#### `SetIamPolicy`

  * **Method** : `google.cloud.tasks.v2beta3.CloudTasks.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta3.CloudTasks.SetIamPolicy" `  




#### `UpdateCmekConfig`

  * **Method** : `google.cloud.tasks.v2beta3.CloudTasks.UpdateCmekConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.cmekConfig.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta3.CloudTasks.UpdateCmekConfig" `  




#### `UpdateQueue`

  * **Method** : `google.cloud.tasks.v2beta3.CloudTasks.UpdateQueue`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudtasks.queues.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tasks.v2beta3.CloudTasks.UpdateQueue" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.cloud.tasks.v2.CloudTasks.BatchCreateTasks`
  * `google.cloud.tasks.v2.CloudTasks.BufferTask`
  * `google.cloud.tasks.v2.CloudTasks.CreateTask`
  * `google.cloud.tasks.v2.CloudTasks.TestIamPermissions`
  * `google.cloud.tasks.v2beta2.CloudTasks.AcknowledgeTask`
  * `google.cloud.tasks.v2beta2.CloudTasks.BatchCreateTasks`
  * `google.cloud.tasks.v2beta2.CloudTasks.BufferTask`
  * `google.cloud.tasks.v2beta2.CloudTasks.CancelLease`
  * `google.cloud.tasks.v2beta2.CloudTasks.CreateTask`
  * `google.cloud.tasks.v2beta2.CloudTasks.LeaseTasks`
  * `google.cloud.tasks.v2beta2.CloudTasks.RenewLease`
  * `google.cloud.tasks.v2beta2.CloudTasks.TestIamPermissions`
  * `google.cloud.tasks.v2beta3.CloudTasks.BatchCreateTasks`
  * `google.cloud.tasks.v2beta3.CloudTasks.BufferTask`
  * `google.cloud.tasks.v2beta3.CloudTasks.CreateTask`
  * `google.cloud.tasks.v2beta3.CloudTasks.TestIamPermissions`
  * `google.longrunning.Operations.GetOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
