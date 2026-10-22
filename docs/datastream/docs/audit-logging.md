---
url: https://docs.cloud.google.com/datastream/docs/audit-logging/
title: Datastream audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:18.919182+00:00
---

# Datastream audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Resources ](https://docs.cloud.google.com/datastream/docs/quotas)



Send feedback 

#  Datastream audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Datastream. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Datastream audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="datastream.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Datastream generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.datastream.v1.Datastream.FetchStaticIps`  
`google.cloud.datastream.v1.Datastream.GetConnectionProfile`  
`google.cloud.datastream.v1.Datastream.GetPrivateConnection`  
`google.cloud.datastream.v1.Datastream.GetRoute`  
`google.cloud.datastream.v1.Datastream.GetStream`  
`google.cloud.datastream.v1.Datastream.GetStreamObject`  
`google.cloud.datastream.v1.Datastream.ListConnectionProfiles`  
`google.cloud.datastream.v1.Datastream.ListPrivateConnections`  
`google.cloud.datastream.v1.Datastream.ListRoutes`  
`google.cloud.datastream.v1.Datastream.ListStreamObjects`  
`google.cloud.datastream.v1.Datastream.ListStreams`  
`google.cloud.datastream.v1.Datastream.LookupStreamObject`  
`google.cloud.datastream.v1alpha1.Datastream.FetchErrors` (LRO)  
`google.cloud.datastream.v1alpha1.Datastream.FetchStaticIps`  
`google.cloud.datastream.v1alpha1.Datastream.GetConnectionProfile`  
`google.cloud.datastream.v1alpha1.Datastream.GetPrivateConnection`  
`google.cloud.datastream.v1alpha1.Datastream.GetRoute`  
`google.cloud.datastream.v1alpha1.Datastream.GetStream`  
`google.cloud.datastream.v1alpha1.Datastream.GetStreamObject`  
`google.cloud.datastream.v1alpha1.Datastream.ListConnectionProfiles`  
`google.cloud.datastream.v1alpha1.Datastream.ListPrivateConnections`  
`google.cloud.datastream.v1alpha1.Datastream.ListRoutes`  
`google.cloud.datastream.v1alpha1.Datastream.ListStreamObjects`  
`google.cloud.datastream.v1alpha1.Datastream.ListStreams`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.datastream.v1.Datastream.CreateConnectionProfile` (LRO)  
`google.cloud.datastream.v1.Datastream.CreatePrivateConnection` (LRO)  
`google.cloud.datastream.v1.Datastream.CreateRoute` (LRO)  
`google.cloud.datastream.v1.Datastream.CreateStream` (LRO)  
`google.cloud.datastream.v1.Datastream.DeleteConnectionProfile` (LRO)  
`google.cloud.datastream.v1.Datastream.DeletePrivateConnection` (LRO)  
`google.cloud.datastream.v1.Datastream.DeleteRoute` (LRO)  
`google.cloud.datastream.v1.Datastream.DeleteStream` (LRO)  
`google.cloud.datastream.v1.Datastream.RunStream` (LRO)  
`google.cloud.datastream.v1.Datastream.StartBackfillJob`  
`google.cloud.datastream.v1.Datastream.StopBackfillJob`  
`google.cloud.datastream.v1.Datastream.UpdateConnectionProfile` (LRO)  
`google.cloud.datastream.v1.Datastream.UpdateStream` (LRO)  
`google.cloud.datastream.v1alpha1.Datastream.CreateConnectionProfile` (LRO)  
`google.cloud.datastream.v1alpha1.Datastream.CreatePrivateConnection` (LRO)  
`google.cloud.datastream.v1alpha1.Datastream.CreateRoute` (LRO)  
`google.cloud.datastream.v1alpha1.Datastream.CreateStream` (LRO)  
`google.cloud.datastream.v1alpha1.Datastream.DeleteConnectionProfile` (LRO)  
`google.cloud.datastream.v1alpha1.Datastream.DeletePrivateConnection` (LRO)  
`google.cloud.datastream.v1alpha1.Datastream.DeleteRoute` (LRO)  
`google.cloud.datastream.v1alpha1.Datastream.DeleteStream` (LRO)  
`google.cloud.datastream.v1alpha1.Datastream.StartBackfillJob`  
`google.cloud.datastream.v1alpha1.Datastream.StopBackfillJob`  
`google.cloud.datastream.v1alpha1.Datastream.UpdateConnectionProfile` (LRO)  
`google.cloud.datastream.v1alpha1.Datastream.UpdateStream` (LRO)  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
`DATA_READ` | `google.cloud.datastream.v1.Datastream.DiscoverConnectionProfile`  
`google.cloud.datastream.v1alpha1.Datastream.DiscoverConnectionProfile`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Datastream.

### `google.cloud.datastream.v1.Datastream`

The following audit logs are associated with methods belonging to `google.cloud.datastream.v1.Datastream`.

#### `CreateConnectionProfile`

  * **Method** : `google.cloud.datastream.v1.Datastream.CreateConnectionProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.connectionProfiles.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.CreateConnectionProfile" `  




#### `CreatePrivateConnection`

  * **Method** : `google.cloud.datastream.v1.Datastream.CreatePrivateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.privateConnections.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.CreatePrivateConnection" `  




#### `CreateRoute`

  * **Method** : `google.cloud.datastream.v1.Datastream.CreateRoute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.routes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.CreateRoute" `  




#### `CreateStream`

  * **Method** : `google.cloud.datastream.v1.Datastream.CreateStream`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.streams.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.CreateStream" `  




#### `DeleteConnectionProfile`

  * **Method** : `google.cloud.datastream.v1.Datastream.DeleteConnectionProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.connectionProfiles.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.DeleteConnectionProfile" `  




#### `DeletePrivateConnection`

  * **Method** : `google.cloud.datastream.v1.Datastream.DeletePrivateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.privateConnections.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.DeletePrivateConnection" `  




#### `DeleteRoute`

  * **Method** : `google.cloud.datastream.v1.Datastream.DeleteRoute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.routes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.DeleteRoute" `  




#### `DeleteStream`

  * **Method** : `google.cloud.datastream.v1.Datastream.DeleteStream`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.streams.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.DeleteStream" `  




#### `DiscoverConnectionProfile`

  * **Method** : `google.cloud.datastream.v1.Datastream.DiscoverConnectionProfile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.connectionProfiles.discover - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.DiscoverConnectionProfile" `  




#### `FetchStaticIps`

  * **Method** : `google.cloud.datastream.v1.Datastream.FetchStaticIps`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.locations.fetchStaticIps - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.FetchStaticIps" `  




#### `GetConnectionProfile`

  * **Method** : `google.cloud.datastream.v1.Datastream.GetConnectionProfile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.connectionProfiles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.GetConnectionProfile" `  




#### `GetPrivateConnection`

  * **Method** : `google.cloud.datastream.v1.Datastream.GetPrivateConnection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.privateConnections.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.GetPrivateConnection" `  




#### `GetRoute`

  * **Method** : `google.cloud.datastream.v1.Datastream.GetRoute`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.routes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.GetRoute" `  




#### `GetStream`

  * **Method** : `google.cloud.datastream.v1.Datastream.GetStream`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.streams.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.GetStream" `  




#### `GetStreamObject`

  * **Method** : `google.cloud.datastream.v1.Datastream.GetStreamObject`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.objects.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.GetStreamObject" `  




#### `ListConnectionProfiles`

  * **Method** : `google.cloud.datastream.v1.Datastream.ListConnectionProfiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.connectionProfiles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.ListConnectionProfiles" `  




#### `ListPrivateConnections`

  * **Method** : `google.cloud.datastream.v1.Datastream.ListPrivateConnections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.privateConnections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.ListPrivateConnections" `  




#### `ListRoutes`

  * **Method** : `google.cloud.datastream.v1.Datastream.ListRoutes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.routes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.ListRoutes" `  




#### `ListStreamObjects`

  * **Method** : `google.cloud.datastream.v1.Datastream.ListStreamObjects`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.objects.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.ListStreamObjects" `  




#### `ListStreams`

  * **Method** : `google.cloud.datastream.v1.Datastream.ListStreams`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.streams.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.ListStreams" `  




#### `LookupStreamObject`

  * **Method** : `google.cloud.datastream.v1.Datastream.LookupStreamObject`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.objects.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.LookupStreamObject" `  




#### `RunStream`

  * **Method** : `google.cloud.datastream.v1.Datastream.RunStream`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.streams.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.RunStream" `  




#### `StartBackfillJob`

  * **Method** : `google.cloud.datastream.v1.Datastream.StartBackfillJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.objects.startBackfillJob - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.StartBackfillJob" `  




#### `StopBackfillJob`

  * **Method** : `google.cloud.datastream.v1.Datastream.StopBackfillJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.objects.stopBackfillJob - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.StopBackfillJob" `  




#### `UpdateConnectionProfile`

  * **Method** : `google.cloud.datastream.v1.Datastream.UpdateConnectionProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.connectionProfiles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.UpdateConnectionProfile" `  




#### `UpdateStream`

  * **Method** : `google.cloud.datastream.v1.Datastream.UpdateStream`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.streams.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1.Datastream.UpdateStream" `  




### `google.cloud.datastream.v1alpha1.Datastream`

The following audit logs are associated with methods belonging to `google.cloud.datastream.v1alpha1.Datastream`.

#### `CreateConnectionProfile`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.CreateConnectionProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.connectionProfiles.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.CreateConnectionProfile" `  




#### `CreatePrivateConnection`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.CreatePrivateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.privateConnections.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.CreatePrivateConnection" `  




#### `CreateRoute`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.CreateRoute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.routes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.CreateRoute" `  




#### `CreateStream`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.CreateStream`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.streams.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.CreateStream" `  




#### `DeleteConnectionProfile`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.DeleteConnectionProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.connectionProfiles.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.DeleteConnectionProfile" `  




#### `DeletePrivateConnection`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.DeletePrivateConnection`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.privateConnections.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.DeletePrivateConnection" `  




#### `DeleteRoute`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.DeleteRoute`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.routes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.DeleteRoute" `  




#### `DeleteStream`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.DeleteStream`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.streams.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.DeleteStream" `  




#### `DiscoverConnectionProfile`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.DiscoverConnectionProfile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.connectionProfiles.discover - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.DiscoverConnectionProfile" `  




#### `FetchErrors`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.FetchErrors`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.streams.fetchErrors - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.FetchErrors" `  




#### `FetchStaticIps`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.FetchStaticIps`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.locations.fetchStaticIps - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.FetchStaticIps" `  




#### `GetConnectionProfile`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.GetConnectionProfile`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.connectionProfiles.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.GetConnectionProfile" `  




#### `GetPrivateConnection`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.GetPrivateConnection`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.privateConnections.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.GetPrivateConnection" `  




#### `GetRoute`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.GetRoute`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.routes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.GetRoute" `  




#### `GetStream`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.GetStream`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.streams.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.GetStream" `  




#### `GetStreamObject`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.GetStreamObject`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.objects.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.GetStreamObject" `  




#### `ListConnectionProfiles`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.ListConnectionProfiles`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.connectionProfiles.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.ListConnectionProfiles" `  




#### `ListPrivateConnections`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.ListPrivateConnections`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.privateConnections.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.ListPrivateConnections" `  




#### `ListRoutes`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.ListRoutes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.routes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.ListRoutes" `  




#### `ListStreamObjects`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.ListStreamObjects`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.objects.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.ListStreamObjects" `  




#### `ListStreams`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.ListStreams`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.streams.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.ListStreams" `  




#### `StartBackfillJob`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.StartBackfillJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.objects.startBackfillJob - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.StartBackfillJob" `  




#### `StopBackfillJob`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.StopBackfillJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.objects.stopBackfillJob - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.StopBackfillJob" `  




#### `UpdateConnectionProfile`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.UpdateConnectionProfile`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.connectionProfiles.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.UpdateConnectionProfile" `  




#### `UpdateStream`

  * **Method** : `google.cloud.datastream.v1alpha1.Datastream.UpdateStream`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.streams.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.datastream.v1alpha1.Datastream.UpdateStream" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `datastream.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `datastream.operations.list - ADMIN_READ`
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
