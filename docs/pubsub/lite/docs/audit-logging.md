---
url: https://docs.cloud.google.com/pubsub/lite/docs/audit-logging/
title: Pub/Sub Lite audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:39:10.010793+00:00
---

# Pub/Sub Lite audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/lite/docs/publish-receive-messages-console)



Send feedback 

#  Pub/Sub Lite audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Pub/Sub Lite. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Pub/Sub Lite audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="pubsublite.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Pub/Sub Lite generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.pubsublite.v1.AdminService.GetReservation`  
`google.cloud.pubsublite.v1.AdminService.GetSubscription`  
`google.cloud.pubsublite.v1.AdminService.GetTopic`  
`google.cloud.pubsublite.v1.AdminService.GetTopicPartitions`  
`google.cloud.pubsublite.v1.AdminService.ListReservationTopics`  
`google.cloud.pubsublite.v1.AdminService.ListReservations`  
`google.cloud.pubsublite.v1.AdminService.ListSubscriptions`  
`google.cloud.pubsublite.v1.AdminService.ListTopicSubscriptions`  
`google.cloud.pubsublite.v1.AdminService.ListTopics`  
`google.cloud.pubsublite.v1.TopicStatsService.ComputeHeadCursor`  
`google.cloud.pubsublite.v1.TopicStatsService.ComputeTimeCursor`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.pubsublite.v1.AdminService.CreateReservation`  
`google.cloud.pubsublite.v1.AdminService.CreateSubscription`  
`google.cloud.pubsublite.v1.AdminService.CreateTopic`  
`google.cloud.pubsublite.v1.AdminService.DeleteReservation`  
`google.cloud.pubsublite.v1.AdminService.DeleteSubscription`  
`google.cloud.pubsublite.v1.AdminService.DeleteTopic`  
`google.cloud.pubsublite.v1.AdminService.UpdateReservation`  
`google.cloud.pubsublite.v1.AdminService.UpdateSubscription`  
`google.cloud.pubsublite.v1.AdminService.UpdateTopic`  
`DATA_READ` | `google.cloud.pubsublite.v1.CursorService.ListPartitionCursors`  
`google.cloud.pubsublite.v1.PartitionAssignmentService.AssignPartitions`  
`google.cloud.pubsublite.v1.TopicStatsService.ComputeMessageStats`  
`DATA_WRITE` | `google.cloud.pubsublite.v1.AdminService.SeekSubscription` (LRO)  
`google.cloud.pubsublite.v1.CursorService.CommitCursor`  
`google.cloud.pubsublite.v1.CursorService.StreamingCommitCursor`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Pub/Sub Lite.

### `google.cloud.pubsublite.v1.AdminService`

The following audit logs are associated with methods belonging to `google.cloud.pubsublite.v1.AdminService`.

#### `CreateReservation`

  * **Method** : `google.cloud.pubsublite.v1.AdminService.CreateReservation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `pubsublite.reservations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.AdminService.CreateReservation" `  




#### `CreateSubscription`

  * **Method** : `google.cloud.pubsublite.v1.AdminService.CreateSubscription`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `pubsublite.subscriptions.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.AdminService.CreateSubscription" `  




#### `CreateTopic`

  * **Method** : `google.cloud.pubsublite.v1.AdminService.CreateTopic`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `pubsublite.topics.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.AdminService.CreateTopic" `  




#### `DeleteReservation`

  * **Method** : `google.cloud.pubsublite.v1.AdminService.DeleteReservation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `pubsublite.reservations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.AdminService.DeleteReservation" `  




#### `DeleteSubscription`

  * **Method** : `google.cloud.pubsublite.v1.AdminService.DeleteSubscription`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `pubsublite.subscriptions.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.AdminService.DeleteSubscription" `  




#### `DeleteTopic`

  * **Method** : `google.cloud.pubsublite.v1.AdminService.DeleteTopic`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `pubsublite.topics.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.AdminService.DeleteTopic" `  




#### `GetReservation`

  * **Method** : `google.cloud.pubsublite.v1.AdminService.GetReservation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `pubsublite.reservations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.AdminService.GetReservation" `  




#### `GetSubscription`

  * **Method** : `google.cloud.pubsublite.v1.AdminService.GetSubscription`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `pubsublite.subscriptions.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.AdminService.GetSubscription" `  




#### `GetTopic`

  * **Method** : `google.cloud.pubsublite.v1.AdminService.GetTopic`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `pubsublite.topics.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.AdminService.GetTopic" `  




#### `GetTopicPartitions`

  * **Method** : `google.cloud.pubsublite.v1.AdminService.GetTopicPartitions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `pubsublite.topics.getPartitions - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.AdminService.GetTopicPartitions" `  




#### `ListReservationTopics`

  * **Method** : `google.cloud.pubsublite.v1.AdminService.ListReservationTopics`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `pubsublite.reservations.listTopics - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.AdminService.ListReservationTopics" `  




#### `ListReservations`

  * **Method** : `google.cloud.pubsublite.v1.AdminService.ListReservations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `pubsublite.reservations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.AdminService.ListReservations" `  




#### `ListSubscriptions`

  * **Method** : `google.cloud.pubsublite.v1.AdminService.ListSubscriptions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `pubsublite.subscriptions.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.AdminService.ListSubscriptions" `  




#### `ListTopicSubscriptions`

  * **Method** : `google.cloud.pubsublite.v1.AdminService.ListTopicSubscriptions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `pubsublite.topics.listSubscriptions - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.AdminService.ListTopicSubscriptions" `  




#### `ListTopics`

  * **Method** : `google.cloud.pubsublite.v1.AdminService.ListTopics`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `pubsublite.topics.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.AdminService.ListTopics" `  




#### `SeekSubscription`

  * **Method** : `google.cloud.pubsublite.v1.AdminService.SeekSubscription`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `pubsublite.subscriptions.seek - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.AdminService.SeekSubscription" `  




#### `UpdateReservation`

  * **Method** : `google.cloud.pubsublite.v1.AdminService.UpdateReservation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `pubsublite.reservations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.AdminService.UpdateReservation" `  




#### `UpdateSubscription`

  * **Method** : `google.cloud.pubsublite.v1.AdminService.UpdateSubscription`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `pubsublite.subscriptions.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.AdminService.UpdateSubscription" `  




#### `UpdateTopic`

  * **Method** : `google.cloud.pubsublite.v1.AdminService.UpdateTopic`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `pubsublite.topics.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.AdminService.UpdateTopic" `  




### `google.cloud.pubsublite.v1.CursorService`

The following audit logs are associated with methods belonging to `google.cloud.pubsublite.v1.CursorService`.

#### `CommitCursor`

  * **Method** : `google.cloud.pubsublite.v1.CursorService.CommitCursor`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `pubsublite.subscriptions.setCursor - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.CursorService.CommitCursor" `  




#### `ListPartitionCursors`

  * **Method** : `google.cloud.pubsublite.v1.CursorService.ListPartitionCursors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `pubsublite.subscriptions.getCursor - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.CursorService.ListPartitionCursors" `  




#### `StreamingCommitCursor`

  * **Method** : `google.cloud.pubsublite.v1.CursorService.StreamingCommitCursor`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `pubsublite.subscriptions.setCursor - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.CursorService.StreamingCommitCursor" `  




### `google.cloud.pubsublite.v1.PartitionAssignmentService`

The following audit logs are associated with methods belonging to `google.cloud.pubsublite.v1.PartitionAssignmentService`.

#### `AssignPartitions`

  * **Method** : `google.cloud.pubsublite.v1.PartitionAssignmentService.AssignPartitions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `pubsublite.subscriptions.subscribe - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.PartitionAssignmentService.AssignPartitions" `  




### `google.cloud.pubsublite.v1.TopicStatsService`

The following audit logs are associated with methods belonging to `google.cloud.pubsublite.v1.TopicStatsService`.

#### `ComputeHeadCursor`

  * **Method** : `google.cloud.pubsublite.v1.TopicStatsService.ComputeHeadCursor`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `pubsublite.topics.computeHeadCursor - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.TopicStatsService.ComputeHeadCursor" `  




#### `ComputeMessageStats`

  * **Method** : `google.cloud.pubsublite.v1.TopicStatsService.ComputeMessageStats`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `pubsublite.topics.computeMessageStats - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.TopicStatsService.ComputeMessageStats" `  




#### `ComputeTimeCursor`

  * **Method** : `google.cloud.pubsublite.v1.TopicStatsService.ComputeTimeCursor`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `pubsublite.topics.computeTimeCursor - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.pubsublite.v1.TopicStatsService.ComputeTimeCursor" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `pubsublite.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `pubsublite.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.DeleteOperation`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
