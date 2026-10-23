---
url: https://docs.cloud.google.com/livestream/docs/how-to/audit-logging/
title: Live Stream API audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:40.554861+00:00
---

# Live Stream API audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/how-to/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Guides ](https://docs.cloud.google.com/livestream/docs/overview)



Send feedback 

#  Live Stream API audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Live Stream API. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Live Stream API audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="livestream.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Live Stream API generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.video.livestream.v1.LivestreamService.GetAsset`  
`google.cloud.video.livestream.v1.LivestreamService.GetChannel`  
`google.cloud.video.livestream.v1.LivestreamService.GetClip`  
`google.cloud.video.livestream.v1.LivestreamService.GetDvrSession`  
`google.cloud.video.livestream.v1.LivestreamService.GetEvent`  
`google.cloud.video.livestream.v1.LivestreamService.GetInput`  
`google.cloud.video.livestream.v1.LivestreamService.GetPool`  
`google.cloud.video.livestream.v1.LivestreamService.ListAssets`  
`google.cloud.video.livestream.v1.LivestreamService.ListChannels`  
`google.cloud.video.livestream.v1.LivestreamService.ListClips`  
`google.cloud.video.livestream.v1.LivestreamService.ListDvrSessions`  
`google.cloud.video.livestream.v1.LivestreamService.ListEvents`  
`google.cloud.video.livestream.v1.LivestreamService.ListInputs`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.video.livestream.v1.LivestreamService.CreateAsset` (LRO)  
`google.cloud.video.livestream.v1.LivestreamService.CreateChannel` (LRO)  
`google.cloud.video.livestream.v1.LivestreamService.CreateClip` (LRO)  
`google.cloud.video.livestream.v1.LivestreamService.CreateDvrSession` (LRO)  
`google.cloud.video.livestream.v1.LivestreamService.CreateEvent`  
`google.cloud.video.livestream.v1.LivestreamService.CreateInput` (LRO)  
`google.cloud.video.livestream.v1.LivestreamService.DeleteAsset` (LRO)  
`google.cloud.video.livestream.v1.LivestreamService.DeleteChannel` (LRO)  
`google.cloud.video.livestream.v1.LivestreamService.DeleteClip` (LRO)  
`google.cloud.video.livestream.v1.LivestreamService.DeleteDvrSession` (LRO)  
`google.cloud.video.livestream.v1.LivestreamService.DeleteEvent`  
`google.cloud.video.livestream.v1.LivestreamService.DeleteInput` (LRO)  
`google.cloud.video.livestream.v1.LivestreamService.StartChannel` (LRO)  
`google.cloud.video.livestream.v1.LivestreamService.StartDistribution` (LRO)  
`google.cloud.video.livestream.v1.LivestreamService.StopChannel` (LRO)  
`google.cloud.video.livestream.v1.LivestreamService.StopDistribution` (LRO)  
`google.cloud.video.livestream.v1.LivestreamService.UpdateChannel` (LRO)  
`google.cloud.video.livestream.v1.LivestreamService.UpdateDvrSession` (LRO)  
`google.cloud.video.livestream.v1.LivestreamService.UpdateInput` (LRO)  
`google.cloud.video.livestream.v1.LivestreamService.UpdatePool` (LRO)  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
`DATA_READ` | `google.cloud.video.livestream.v1.LivestreamService.PreviewInput`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Live Stream API.

### `google.cloud.video.livestream.v1.LivestreamService`

The following audit logs are associated with methods belonging to `google.cloud.video.livestream.v1.LivestreamService`.

#### `CreateAsset`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.CreateAsset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.assets.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.CreateAsset" `  




#### `CreateChannel`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.CreateChannel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.channels.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.CreateChannel" `  




#### `CreateClip`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.CreateClip`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.clips.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.CreateClip" `  




#### `CreateDvrSession`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.CreateDvrSession`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.dvrSessions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.CreateDvrSession" `  




#### `CreateEvent`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.CreateEvent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.events.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.CreateEvent" `  




#### `CreateInput`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.CreateInput`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.inputs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.CreateInput" `  




#### `DeleteAsset`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.DeleteAsset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.assets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.DeleteAsset" `  




#### `DeleteChannel`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.DeleteChannel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.channels.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.DeleteChannel" `  




#### `DeleteClip`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.DeleteClip`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.clips.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.DeleteClip" `  




#### `DeleteDvrSession`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.DeleteDvrSession`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.dvrSessions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.DeleteDvrSession" `  




#### `DeleteEvent`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.DeleteEvent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.events.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.DeleteEvent" `  




#### `DeleteInput`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.DeleteInput`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.inputs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.DeleteInput" `  




#### `GetAsset`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.GetAsset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `livestream.assets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.GetAsset" `  




#### `GetChannel`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.GetChannel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `livestream.channels.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.GetChannel" `  




#### `GetClip`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.GetClip`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `livestream.clips.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.GetClip" `  




#### `GetDvrSession`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.GetDvrSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `livestream.dvrSessions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.GetDvrSession" `  




#### `GetEvent`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.GetEvent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `livestream.events.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.GetEvent" `  




#### `GetInput`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.GetInput`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `livestream.inputs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.GetInput" `  




#### `GetPool`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.GetPool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `livestream.pools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.GetPool" `  




#### `ListAssets`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.ListAssets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `livestream.assets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.ListAssets" `  




#### `ListChannels`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.ListChannels`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `livestream.channels.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.ListChannels" `  




#### `ListClips`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.ListClips`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `livestream.clips.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.ListClips" `  




#### `ListDvrSessions`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.ListDvrSessions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `livestream.dvrSessions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.ListDvrSessions" `  




#### `ListEvents`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.ListEvents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `livestream.events.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.ListEvents" `  




#### `ListInputs`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.ListInputs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `livestream.inputs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.ListInputs" `  




#### `PreviewInput`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.PreviewInput`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `livestream.inputs.preview - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.PreviewInput" `  




#### `StartChannel`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.StartChannel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.channels.start - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.StartChannel" `  




#### `StartDistribution`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.StartDistribution`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.channels.startdistribution - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.StartDistribution" `  




#### `StopChannel`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.StopChannel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.channels.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.StopChannel" `  




#### `StopDistribution`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.StopDistribution`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.channels.stopdistribution - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.StopDistribution" `  




#### `UpdateChannel`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.UpdateChannel`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.channels.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.UpdateChannel" `  




#### `UpdateDvrSession`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.UpdateDvrSession`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.dvrSessions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.UpdateDvrSession" `  




#### `UpdateInput`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.UpdateInput`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.inputs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.UpdateInput" `  




#### `UpdatePool`

  * **Method** : `google.cloud.video.livestream.v1.LivestreamService.UpdatePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.pools.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.livestream.v1.LivestreamService.UpdatePool" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `livestream.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `livestream.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `livestream.operations.list - ADMIN_READ`
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
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
