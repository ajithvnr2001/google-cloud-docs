---
url: https://docs.cloud.google.com/logging/docs/audit-logging/
title: Cloud Logging audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:46.040378+00:00
---

# Cloud Logging audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Cloud Logging audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Cloud Logging. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Cloud Logging audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="logging.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Logging generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.location.Locations.GetLocation`  
`google.cloud.location.Locations.ListLocations`  
`google.iam.v1.IAMPolicy.GetIamPolicy`  
`google.logging.v2.ConfigServiceV2.GetBucket`  
`google.logging.v2.ConfigServiceV2.GetCmekSettings`  
`google.logging.v2.ConfigServiceV2.GetExclusion`  
`google.logging.v2.ConfigServiceV2.GetLink`  
`google.logging.v2.ConfigServiceV2.GetLogScope`  
`google.logging.v2.ConfigServiceV2.GetSettings`  
`google.logging.v2.ConfigServiceV2.GetSink`  
`google.logging.v2.ConfigServiceV2.GetView`  
`google.logging.v2.ConfigServiceV2.ListBuckets`  
`google.logging.v2.ConfigServiceV2.ListExclusions`  
`google.logging.v2.ConfigServiceV2.ListLinks`  
`google.logging.v2.ConfigServiceV2.ListLogScopes`  
`google.logging.v2.ConfigServiceV2.ListSinks`  
`google.logging.v2.ConfigServiceV2.ListViews`  
`google.logging.v2.LoggingServiceV2.ListLogs`  
`google.logging.v2.MetricsServiceV2.GetLogMetric`  
`google.logging.v2.MetricsServiceV2.ListLogMetrics`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.iam.v1.IAMPolicy.SetIamPolicy`  
`google.logging.v2.ConfigServiceV2.CreateBucket`  
`google.logging.v2.ConfigServiceV2.CreateBucketAsync` (LRO)  
`google.logging.v2.ConfigServiceV2.CreateExclusion`  
`google.logging.v2.ConfigServiceV2.CreateLink` (LRO)  
`google.logging.v2.ConfigServiceV2.CreateLogScope`  
`google.logging.v2.ConfigServiceV2.CreateSink`  
`google.logging.v2.ConfigServiceV2.CreateView`  
`google.logging.v2.ConfigServiceV2.DeleteBucket`  
`google.logging.v2.ConfigServiceV2.DeleteExclusion`  
`google.logging.v2.ConfigServiceV2.DeleteLink` (LRO)  
`google.logging.v2.ConfigServiceV2.DeleteLogScope`  
`google.logging.v2.ConfigServiceV2.DeleteSink`  
`google.logging.v2.ConfigServiceV2.DeleteView`  
`google.logging.v2.ConfigServiceV2.UndeleteBucket`  
`google.logging.v2.ConfigServiceV2.UpdateBucket`  
`google.logging.v2.ConfigServiceV2.UpdateBucketAsync` (LRO)  
`google.logging.v2.ConfigServiceV2.UpdateCmekSettings`  
`google.logging.v2.ConfigServiceV2.UpdateExclusion`  
`google.logging.v2.ConfigServiceV2.UpdateLogScope`  
`google.logging.v2.ConfigServiceV2.UpdateSettings`  
`google.logging.v2.ConfigServiceV2.UpdateSink`  
`google.logging.v2.ConfigServiceV2.UpdateView`  
`google.logging.v2.LoggingServiceV2.DeleteLog`  
`google.logging.v2.MetricsServiceV2.CreateLogMetric`  
`google.logging.v2.MetricsServiceV2.DeleteLogMetric`  
`google.logging.v2.MetricsServiceV2.UpdateLogMetric`  
`google.longrunning.Operations.CancelOperation`  
`DATA_READ` | `google.logging.v2.ConfigServiceV2.CopyLogEntries` (LRO)  
`google.logging.v2.LoggingServiceV2.ListLogEntries`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Logging.

### `google.cloud.location.Locations`

The following audit logs are associated with methods belonging to `google.cloud.location.Locations`.

#### `GetLocation`

  * **Method** : `google.cloud.location.Locations.GetLocation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.locations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.location.Locations.GetLocation" `  




#### `ListLocations`

  * **Method** : `google.cloud.location.Locations.ListLocations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.locations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.location.Locations.ListLocations" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `google.iam.v1.IAMPolicy.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.views.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.IAMPolicy.GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `google.iam.v1.IAMPolicy.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.views.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.IAMPolicy.SetIamPolicy" `  




### `google.logging.v2.ConfigServiceV2`

The following audit logs are associated with methods belonging to `google.logging.v2.ConfigServiceV2`.

#### `CopyLogEntries`

  * **Method** : `google.logging.v2.ConfigServiceV2.CopyLogEntries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.buckets.copyLogEntries - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.CopyLogEntries" `  




#### `CreateBucket`

  * **Method** : `google.logging.v2.ConfigServiceV2.CreateBucket`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.buckets.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.CreateBucket" `  




#### `CreateBucketAsync`

  * **Method** : `google.logging.v2.ConfigServiceV2.CreateBucketAsync`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.buckets.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.CreateBucketAsync" `  




#### `CreateExclusion`

  * **Method** : `google.logging.v2.ConfigServiceV2.CreateExclusion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.exclusions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.CreateExclusion" `  




#### `CreateLink`

  * **Method** : `google.logging.v2.ConfigServiceV2.CreateLink`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.links.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.CreateLink" `  




#### `CreateLogScope`

  * **Method** : `google.logging.v2.ConfigServiceV2.CreateLogScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.logScopes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.CreateLogScope" `  




#### `CreateSink`

  * **Method** : `google.logging.v2.ConfigServiceV2.CreateSink`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.sinks.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.CreateSink" `  




#### `CreateView`

  * **Method** : `google.logging.v2.ConfigServiceV2.CreateView`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.views.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.CreateView" `  




#### `DeleteBucket`

  * **Method** : `google.logging.v2.ConfigServiceV2.DeleteBucket`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.buckets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.DeleteBucket" `  




#### `DeleteExclusion`

  * **Method** : `google.logging.v2.ConfigServiceV2.DeleteExclusion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.exclusions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.DeleteExclusion" `  




#### `DeleteLink`

  * **Method** : `google.logging.v2.ConfigServiceV2.DeleteLink`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.links.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.DeleteLink" `  




#### `DeleteLogScope`

  * **Method** : `google.logging.v2.ConfigServiceV2.DeleteLogScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.logScopes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.DeleteLogScope" `  




#### `DeleteSink`

  * **Method** : `google.logging.v2.ConfigServiceV2.DeleteSink`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.sinks.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.DeleteSink" `  




#### `DeleteView`

  * **Method** : `google.logging.v2.ConfigServiceV2.DeleteView`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.views.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.DeleteView" `  




#### `GetBucket`

  * **Method** : `google.logging.v2.ConfigServiceV2.GetBucket`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.buckets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.GetBucket" `  




#### `GetCmekSettings`

  * **Method** : `google.logging.v2.ConfigServiceV2.GetCmekSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.settings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.GetCmekSettings" `  




#### `GetExclusion`

  * **Method** : `google.logging.v2.ConfigServiceV2.GetExclusion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.exclusions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.GetExclusion" `  




#### `GetLink`

  * **Method** : `google.logging.v2.ConfigServiceV2.GetLink`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.links.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.GetLink" `  




#### `GetLogScope`

  * **Method** : `google.logging.v2.ConfigServiceV2.GetLogScope`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.logScopes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.GetLogScope" `  




#### `GetSettings`

  * **Method** : `google.logging.v2.ConfigServiceV2.GetSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.settings.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.GetSettings" `  




#### `GetSink`

  * **Method** : `google.logging.v2.ConfigServiceV2.GetSink`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.sinks.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.GetSink" `  




#### `GetView`

  * **Method** : `google.logging.v2.ConfigServiceV2.GetView`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.views.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.GetView" `  




#### `ListBuckets`

  * **Method** : `google.logging.v2.ConfigServiceV2.ListBuckets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.buckets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.ListBuckets" `  




#### `ListExclusions`

  * **Method** : `google.logging.v2.ConfigServiceV2.ListExclusions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.exclusions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.ListExclusions" `  




#### `ListLinks`

  * **Method** : `google.logging.v2.ConfigServiceV2.ListLinks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.links.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.ListLinks" `  




#### `ListLogScopes`

  * **Method** : `google.logging.v2.ConfigServiceV2.ListLogScopes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.logScopes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.ListLogScopes" `  




#### `ListSinks`

  * **Method** : `google.logging.v2.ConfigServiceV2.ListSinks`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.sinks.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.ListSinks" `  




#### `ListViews`

  * **Method** : `google.logging.v2.ConfigServiceV2.ListViews`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.views.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.ListViews" `  




#### `UndeleteBucket`

  * **Method** : `google.logging.v2.ConfigServiceV2.UndeleteBucket`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.buckets.undelete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.UndeleteBucket" `  




#### `UpdateBucket`

  * **Method** : `google.logging.v2.ConfigServiceV2.UpdateBucket`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.buckets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.UpdateBucket" `  




#### `UpdateBucketAsync`

  * **Method** : `google.logging.v2.ConfigServiceV2.UpdateBucketAsync`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.buckets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.UpdateBucketAsync" `  




#### `UpdateCmekSettings`

  * **Method** : `google.logging.v2.ConfigServiceV2.UpdateCmekSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.settings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.UpdateCmekSettings" `  




#### `UpdateExclusion`

  * **Method** : `google.logging.v2.ConfigServiceV2.UpdateExclusion`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.exclusions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.UpdateExclusion" `  




#### `UpdateLogScope`

  * **Method** : `google.logging.v2.ConfigServiceV2.UpdateLogScope`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.logScopes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.UpdateLogScope" `  




#### `UpdateSettings`

  * **Method** : `google.logging.v2.ConfigServiceV2.UpdateSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.settings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.UpdateSettings" `  




#### `UpdateSink`

  * **Method** : `google.logging.v2.ConfigServiceV2.UpdateSink`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.sinks.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.UpdateSink" `  




#### `UpdateView`

  * **Method** : `google.logging.v2.ConfigServiceV2.UpdateView`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.views.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.ConfigServiceV2.UpdateView" `  




### `google.logging.v2.LoggingServiceV2`

The following audit logs are associated with methods belonging to `google.logging.v2.LoggingServiceV2`.

#### `DeleteLog`

  * **Method** : `google.logging.v2.LoggingServiceV2.DeleteLog`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.logs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.LoggingServiceV2.DeleteLog" `  




#### `ListLogEntries`

  * **Method** : `google.logging.v2.LoggingServiceV2.ListLogEntries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.logEntries.list - DATA_READ`
    * `logging.privateLogEntries.list - DATA_READ`
    * `logging.views.access - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.LoggingServiceV2.ListLogEntries" `  




#### `ListLogs`

  * **Method** : `google.logging.v2.LoggingServiceV2.ListLogs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.logs.list - ADMIN_READ`
    * `logging.views.listLogs - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.LoggingServiceV2.ListLogs" `  




### `google.logging.v2.MetricsServiceV2`

The following audit logs are associated with methods belonging to `google.logging.v2.MetricsServiceV2`.

#### `CreateLogMetric`

  * **Method** : `google.logging.v2.MetricsServiceV2.CreateLogMetric`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.logMetrics.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.MetricsServiceV2.CreateLogMetric" `  




#### `DeleteLogMetric`

  * **Method** : `google.logging.v2.MetricsServiceV2.DeleteLogMetric`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.logMetrics.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.MetricsServiceV2.DeleteLogMetric" `  




#### `GetLogMetric`

  * **Method** : `google.logging.v2.MetricsServiceV2.GetLogMetric`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.logMetrics.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.MetricsServiceV2.GetLogMetric" `  




#### `ListLogMetrics`

  * **Method** : `google.logging.v2.MetricsServiceV2.ListLogMetrics`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.logMetrics.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.MetricsServiceV2.ListLogMetrics" `  




#### `UpdateLogMetric`

  * **Method** : `google.logging.v2.MetricsServiceV2.UpdateLogMetric`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.logMetrics.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.logging.v2.MetricsServiceV2.UpdateLogMetric" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `logging.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `logging.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.logging.v1.LoggingService.WriteLogEntries`
  * `google.logging.v2.ConfigServiceV2.CreateSavedQuery`
  * `google.logging.v2.ConfigServiceV2.DeleteSavedQuery`
  * `google.logging.v2.ConfigServiceV2.GetSavedQuery`
  * `google.logging.v2.ConfigServiceV2.ListRecentQueries`
  * `google.logging.v2.ConfigServiceV2.ListSavedQueries`
  * `google.logging.v2.ConfigServiceV2.UpdateSavedQuery`
  * `google.logging.v2.LoggingServiceV2.ListMonitoredResourceDescriptors`
  * `google.logging.v2.LoggingServiceV2.TailLogEntries`
  * `google.logging.v2.LoggingServiceV2.WriteLogEntries`
  * `google.longrunning.Operations.DeleteOperation`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
