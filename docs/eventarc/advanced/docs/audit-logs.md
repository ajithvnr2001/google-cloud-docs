---
url: https://docs.cloud.google.com/eventarc/advanced/docs/audit-logs/
title: Eventarc audit logging \u00a0|\u00a0 Eventarc Advanced \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:03.559482+00:00
---

# Eventarc audit logging  |  Eventarc Advanced  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/advanced/docs/audit-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)



Send feedback 

#  Eventarc audit logging Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview) [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

This document lists the audited methods for Eventarc. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Eventarc audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="eventarc.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Eventarc generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.eventarc.v1.Eventarc.GetEnrollment`  
`google.cloud.eventarc.v1.Eventarc.GetGoogleApiSource`  
`google.cloud.eventarc.v1.Eventarc.GetMessageBus`  
`google.cloud.eventarc.v1.Eventarc.GetPipeline`  
`google.cloud.eventarc.v1.Eventarc.ListEnrollments`  
`google.cloud.eventarc.v1.Eventarc.ListGoogleApiSources`  
`google.cloud.eventarc.v1.Eventarc.ListMessageBusEnrollments`  
`google.cloud.eventarc.v1.Eventarc.ListMessageBuses`  
`google.cloud.eventarc.v1.Eventarc.ListPipelines`  
`GetIamPolicy`  
`ADMIN_WRITE` | `google.cloud.eventarc.v1.Eventarc.CreateEnrollment` (LRO)  
`google.cloud.eventarc.v1.Eventarc.CreateGoogleApiSource` (LRO)  
`google.cloud.eventarc.v1.Eventarc.CreateMessageBus` (LRO)  
`google.cloud.eventarc.v1.Eventarc.CreatePipeline` (LRO)  
`google.cloud.eventarc.v1.Eventarc.DeleteEnrollment` (LRO)  
`google.cloud.eventarc.v1.Eventarc.DeleteGoogleApiSource` (LRO)  
`google.cloud.eventarc.v1.Eventarc.DeleteMessageBus` (LRO)  
`google.cloud.eventarc.v1.Eventarc.DeletePipeline` (LRO)  
`google.cloud.eventarc.v1.Eventarc.UpdateEnrollment` (LRO)  
`google.cloud.eventarc.v1.Eventarc.UpdateGoogleApiSource` (LRO)  
`google.cloud.eventarc.v1.Eventarc.UpdateMessageBus` (LRO)  
`google.cloud.eventarc.v1.Eventarc.UpdatePipeline` (LRO)  
`SetIamPolicy`  
`DATA_READ` | `google.cloud.eventarc.v1.Eventarc.GetChannel`  
`google.cloud.eventarc.v1.Eventarc.GetChannelConnection`  
`google.cloud.eventarc.v1.Eventarc.GetGoogleChannelConfig`  
`google.cloud.eventarc.v1.Eventarc.GetProvider`  
`google.cloud.eventarc.v1.Eventarc.GetTrigger`  
`google.cloud.eventarc.v1.Eventarc.ListChannelConnections`  
`google.cloud.eventarc.v1.Eventarc.ListChannels`  
`google.cloud.eventarc.v1.Eventarc.ListProviders`  
`google.cloud.eventarc.v1.Eventarc.ListTriggers`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`DATA_WRITE` | `google.cloud.eventarc.v1.Eventarc.CreateChannel` (LRO)  
`google.cloud.eventarc.v1.Eventarc.CreateChannelConnection` (LRO)  
`google.cloud.eventarc.v1.Eventarc.CreateTrigger` (LRO)  
`google.cloud.eventarc.v1.Eventarc.DeleteChannel` (LRO)  
`google.cloud.eventarc.v1.Eventarc.DeleteChannelConnection`  
`google.cloud.eventarc.v1.Eventarc.DeleteTrigger` (LRO)  
`google.cloud.eventarc.v1.Eventarc.UpdateChannel` (LRO)  
`google.cloud.eventarc.v1.Eventarc.UpdateGoogleChannelConfig`  
`google.cloud.eventarc.v1.Eventarc.UpdateTrigger` (LRO)  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Eventarc.

### `google.cloud.eventarc.v1.Eventarc`

The following audit logs are associated with methods belonging to `google.cloud.eventarc.v1.Eventarc`.

#### `CreateChannel`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.CreateChannel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.channels.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.CreateChannel" `  




#### `CreateChannelConnection`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.CreateChannelConnection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.channelConnections.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.CreateChannelConnection" `  




#### `CreateEnrollment`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.CreateEnrollment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `eventarc.enrollments.create - ADMIN_WRITE`
    * `eventarc.messageBuses.use - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.CreateEnrollment" `  




#### `CreateGoogleApiSource`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.CreateGoogleApiSource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `eventarc.googleApiSources.create - ADMIN_WRITE`
    * `eventarc.messageBuses.use - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.CreateGoogleApiSource" `  




#### `CreateMessageBus`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.CreateMessageBus`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `eventarc.messageBuses.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.CreateMessageBus" `  




#### `CreatePipeline`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.CreatePipeline`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `eventarc.pipelines.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.CreatePipeline" `  




#### `CreateTrigger`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.CreateTrigger`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.triggers.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.CreateTrigger" `  




#### `DeleteChannel`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.DeleteChannel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.channels.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.DeleteChannel" `  




#### `DeleteChannelConnection`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.DeleteChannelConnection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.channelConnections.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.DeleteChannelConnection" `  




#### `DeleteEnrollment`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.DeleteEnrollment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `eventarc.enrollments.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.DeleteEnrollment" `  




#### `DeleteGoogleApiSource`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.DeleteGoogleApiSource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `eventarc.googleApiSources.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.DeleteGoogleApiSource" `  




#### `DeleteMessageBus`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.DeleteMessageBus`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `eventarc.messageBuses.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.DeleteMessageBus" `  




#### `DeletePipeline`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.DeletePipeline`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `eventarc.pipelines.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.DeletePipeline" `  




#### `DeleteTrigger`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.DeleteTrigger`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.triggers.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.DeleteTrigger" `  




#### `GetChannel`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.GetChannel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.channels.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.GetChannel" `  




#### `GetChannelConnection`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.GetChannelConnection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.channelConnections.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.GetChannelConnection" `  




#### `GetEnrollment`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.GetEnrollment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.enrollments.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.GetEnrollment" `  




#### `GetGoogleApiSource`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.GetGoogleApiSource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.googleApiSources.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.GetGoogleApiSource" `  




#### `GetGoogleChannelConfig`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.GetGoogleChannelConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.googleChannelConfigs.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.GetGoogleChannelConfig" `  




#### `GetMessageBus`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.GetMessageBus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.messageBuses.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.GetMessageBus" `  




#### `GetPipeline`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.GetPipeline`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.pipelines.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.GetPipeline" `  




#### `GetProvider`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.GetProvider`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.providers.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.GetProvider" `  




#### `GetTrigger`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.GetTrigger`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.triggers.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.GetTrigger" `  




#### `ListChannelConnections`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.ListChannelConnections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.channelConnections.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.ListChannelConnections" `  




#### `ListChannels`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.ListChannels`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.channels.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.ListChannels" `  




#### `ListEnrollments`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.ListEnrollments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.enrollments.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.ListEnrollments" `  




#### `ListGoogleApiSources`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.ListGoogleApiSources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.googleApiSources.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.ListGoogleApiSources" `  




#### `ListMessageBusEnrollments`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.ListMessageBusEnrollments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.messageBuses.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.ListMessageBusEnrollments" `  




#### `ListMessageBuses`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.ListMessageBuses`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.messageBuses.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.ListMessageBuses" `  




#### `ListPipelines`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.ListPipelines`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.pipelines.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.ListPipelines" `  




#### `ListProviders`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.ListProviders`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.providers.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.ListProviders" `  




#### `ListTriggers`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.ListTriggers`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.triggers.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.ListTriggers" `  




#### `UpdateChannel`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.UpdateChannel`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.channels.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.UpdateChannel" `  




#### `UpdateEnrollment`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.UpdateEnrollment`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `eventarc.enrollments.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.UpdateEnrollment" `  




#### `UpdateGoogleApiSource`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.UpdateGoogleApiSource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `eventarc.googleApiSources.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.UpdateGoogleApiSource" `  




#### `UpdateGoogleChannelConfig`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.UpdateGoogleChannelConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.googleChannelConfigs.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.UpdateGoogleChannelConfig" `  




#### `UpdateMessageBus`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.UpdateMessageBus`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `eventarc.messageBuses.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.UpdateMessageBus" `  




#### `UpdatePipeline`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.UpdatePipeline`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `eventarc.pipelines.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.UpdatePipeline" `  




#### `UpdateTrigger`

  * **Method** : `google.cloud.eventarc.v1.Eventarc.UpdateTrigger`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.triggers.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.v1.Eventarc.UpdateTrigger" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.triggers.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : See IAM documentation for permissions.
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.operations.cancel - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.operations.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.operations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.operations.list - DATA_READ`
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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
