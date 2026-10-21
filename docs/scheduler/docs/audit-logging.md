---
url: https://docs.cloud.google.com/scheduler/docs/audit-logging/
title: Cloud Scheduler audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:49:47.838737+00:00
---

# Cloud Scheduler audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/scheduler/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Scheduler ](https://docs.cloud.google.com/scheduler/docs)
  * [ Guides ](https://docs.cloud.google.com/scheduler/docs/overview)



Send feedback 

#  Cloud Scheduler audit logging Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Scheduler audit logs let you track administrative and access activities across your scheduled jobs. You can analyze these audit trails to determine who took what action, where, and when to maintain security and compliance. To view Cloud Scheduler logs, see [View logs](https://docs.cloud.google.com/scheduler/docs/viewing-logs). 

This document describes audit logging for Cloud Scheduler. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Cloud Scheduler audit logs use the service name `cloudscheduler.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="cloudscheduler.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Scheduler generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.scheduler.v1.CloudScheduler.GetJob`  
`google.cloud.scheduler.v1.CloudScheduler.ListJobs`  
`google.cloud.scheduler.v1alpha1.CloudScheduler.GetJob`  
`google.cloud.scheduler.v1alpha1.CloudScheduler.ListJobs`  
`google.cloud.scheduler.v1beta1.CloudScheduler.GetJob`  
`google.cloud.scheduler.v1beta1.CloudScheduler.ListJobs`  
`ADMIN_WRITE` | `google.cloud.scheduler.v1.CloudScheduler.CreateJob`  
`google.cloud.scheduler.v1.CloudScheduler.DeleteJob`  
`google.cloud.scheduler.v1.CloudScheduler.PauseJob`  
`google.cloud.scheduler.v1.CloudScheduler.ResumeJob`  
`google.cloud.scheduler.v1.CloudScheduler.RunJob`  
`google.cloud.scheduler.v1.CloudScheduler.UpdateJob`  
`google.cloud.scheduler.v1alpha1.CloudScheduler.CreateJob`  
`google.cloud.scheduler.v1alpha1.CloudScheduler.DeleteJob`  
`google.cloud.scheduler.v1alpha1.CloudScheduler.PauseJob`  
`google.cloud.scheduler.v1alpha1.CloudScheduler.ResumeJob`  
`google.cloud.scheduler.v1alpha1.CloudScheduler.RunJob`  
`google.cloud.scheduler.v1alpha1.CloudScheduler.UpdateJob`  
`google.cloud.scheduler.v1alpha1.CloudScheduler.UploadCronYaml`  
`google.cloud.scheduler.v1beta1.CloudScheduler.CreateJob`  
`google.cloud.scheduler.v1beta1.CloudScheduler.DeleteJob`  
`google.cloud.scheduler.v1beta1.CloudScheduler.PauseJob`  
`google.cloud.scheduler.v1beta1.CloudScheduler.ResumeJob`  
`google.cloud.scheduler.v1beta1.CloudScheduler.RunJob`  
`google.cloud.scheduler.v1beta1.CloudScheduler.UpdateJob`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Scheduler.

### `google.cloud.scheduler.v1.CloudScheduler`

The following audit logs are associated with methods belonging to `google.cloud.scheduler.v1.CloudScheduler`.

#### `CreateJob`

  * **Method** : `google.cloud.scheduler.v1.CloudScheduler.CreateJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudscheduler.jobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1.CloudScheduler.CreateJob" `  




#### `DeleteJob`

  * **Method** : `google.cloud.scheduler.v1.CloudScheduler.DeleteJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudscheduler.jobs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1.CloudScheduler.DeleteJob" `  




#### `GetJob`

  * **Method** : `google.cloud.scheduler.v1.CloudScheduler.GetJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudscheduler.jobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1.CloudScheduler.GetJob" `  




#### `ListJobs`

  * **Method** : `google.cloud.scheduler.v1.CloudScheduler.ListJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudscheduler.jobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1.CloudScheduler.ListJobs" `  




#### `PauseJob`

  * **Method** : `google.cloud.scheduler.v1.CloudScheduler.PauseJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudscheduler.jobs.pause - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1.CloudScheduler.PauseJob" `  




#### `ResumeJob`

  * **Method** : `google.cloud.scheduler.v1.CloudScheduler.ResumeJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudscheduler.jobs.enable - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1.CloudScheduler.ResumeJob" `  




#### `RunJob`

  * **Method** : `google.cloud.scheduler.v1.CloudScheduler.RunJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudscheduler.jobs.run - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1.CloudScheduler.RunJob" `  




#### `UpdateJob`

  * **Method** : `google.cloud.scheduler.v1.CloudScheduler.UpdateJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudscheduler.jobs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1.CloudScheduler.UpdateJob" `  




### `google.cloud.scheduler.v1alpha1.CloudScheduler`

The following audit logs are associated with methods belonging to `google.cloud.scheduler.v1alpha1.CloudScheduler`.

#### `CreateJob`

  * **Method** : `google.cloud.scheduler.v1alpha1.CloudScheduler.CreateJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudscheduler.jobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1alpha1.CloudScheduler.CreateJob" `  




#### `DeleteJob`

  * **Method** : `google.cloud.scheduler.v1alpha1.CloudScheduler.DeleteJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudscheduler.jobs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1alpha1.CloudScheduler.DeleteJob" `  




#### `GetJob`

  * **Method** : `google.cloud.scheduler.v1alpha1.CloudScheduler.GetJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudscheduler.jobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1alpha1.CloudScheduler.GetJob" `  




#### `ListJobs`

  * **Method** : `google.cloud.scheduler.v1alpha1.CloudScheduler.ListJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudscheduler.jobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1alpha1.CloudScheduler.ListJobs" `  




#### `PauseJob`

  * **Method** : `google.cloud.scheduler.v1alpha1.CloudScheduler.PauseJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudscheduler.jobs.pause - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1alpha1.CloudScheduler.PauseJob" `  




#### `ResumeJob`

  * **Method** : `google.cloud.scheduler.v1alpha1.CloudScheduler.ResumeJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudscheduler.jobs.enable - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1alpha1.CloudScheduler.ResumeJob" `  




#### `RunJob`

  * **Method** : `google.cloud.scheduler.v1alpha1.CloudScheduler.RunJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudscheduler.jobs.run - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1alpha1.CloudScheduler.RunJob" `  




#### `UpdateJob`

  * **Method** : `google.cloud.scheduler.v1alpha1.CloudScheduler.UpdateJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudscheduler.jobs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1alpha1.CloudScheduler.UpdateJob" `  




#### `UploadCronYaml`

  * **Method** : `google.cloud.scheduler.v1alpha1.CloudScheduler.UploadCronYaml`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudscheduler.jobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1alpha1.CloudScheduler.UploadCronYaml" `  




### `google.cloud.scheduler.v1beta1.CloudScheduler`

The following audit logs are associated with methods belonging to `google.cloud.scheduler.v1beta1.CloudScheduler`.

#### `CreateJob`

  * **Method** : `google.cloud.scheduler.v1beta1.CloudScheduler.CreateJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudscheduler.jobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1beta1.CloudScheduler.CreateJob" `  




#### `DeleteJob`

  * **Method** : `google.cloud.scheduler.v1beta1.CloudScheduler.DeleteJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudscheduler.jobs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1beta1.CloudScheduler.DeleteJob" `  




#### `GetJob`

  * **Method** : `google.cloud.scheduler.v1beta1.CloudScheduler.GetJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudscheduler.jobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1beta1.CloudScheduler.GetJob" `  




#### `ListJobs`

  * **Method** : `google.cloud.scheduler.v1beta1.CloudScheduler.ListJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudscheduler.jobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1beta1.CloudScheduler.ListJobs" `  




#### `PauseJob`

  * **Method** : `google.cloud.scheduler.v1beta1.CloudScheduler.PauseJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudscheduler.jobs.pause - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1beta1.CloudScheduler.PauseJob" `  




#### `ResumeJob`

  * **Method** : `google.cloud.scheduler.v1beta1.CloudScheduler.ResumeJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudscheduler.jobs.enable - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1beta1.CloudScheduler.ResumeJob" `  




#### `RunJob`

  * **Method** : `google.cloud.scheduler.v1beta1.CloudScheduler.RunJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudscheduler.jobs.run - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1beta1.CloudScheduler.RunJob" `  




#### `UpdateJob`

  * **Method** : `google.cloud.scheduler.v1beta1.CloudScheduler.UpdateJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudscheduler.jobs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.scheduler.v1beta1.CloudScheduler.UpdateJob" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.DeleteOperation`
  * `google.longrunning.Operations.GetOperation`
  * `google.longrunning.Operations.ListOperations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
