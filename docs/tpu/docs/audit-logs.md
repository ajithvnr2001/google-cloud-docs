---
url: https://docs.cloud.google.com/tpu/docs/audit-logs/
title: Cloud TPU audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:25.799409+00:00
---

# Cloud TPU audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/audit-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud TPU audit logging

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

This document describes audit logging for Cloud TPU. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Cloud TPU audit logs use the service name `tpu.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="tpu.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud TPU generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.tpu.v1.Tpu.GetNode`  
`google.cloud.tpu.v1.Tpu.ListNodes`  
`google.cloud.tpu.v1alpha1.Tpu.GetNode`  
`google.cloud.tpu.v1alpha1.Tpu.ListNodes`  
`google.cloud.tpu.v2.Tpu.GetGuestAttributes`  
`google.cloud.tpu.v2.Tpu.GetNode`  
`google.cloud.tpu.v2.Tpu.GetQueuedResource`  
`google.cloud.tpu.v2.Tpu.ListNodes`  
`google.cloud.tpu.v2.Tpu.ListQueuedResources`  
`google.cloud.tpu.v2alpha1.Tpu.GetGuestAttributes`  
`google.cloud.tpu.v2alpha1.Tpu.GetNode`  
`google.cloud.tpu.v2alpha1.Tpu.GetQueuedResource`  
`google.cloud.tpu.v2alpha1.Tpu.ListNodes`  
`google.cloud.tpu.v2alpha1.Tpu.ListQueuedResources`  
`google.cloud.tpu.v2alpha1.Tpu.ListReservations`  
`ADMIN_WRITE` | `google.cloud.tpu.v1.Tpu.CreateNode` (LRO)  
`google.cloud.tpu.v1.Tpu.DeleteNode` (LRO)  
`google.cloud.tpu.v1.Tpu.ReimageNode`  
`google.cloud.tpu.v1.Tpu.StartNode` (LRO)  
`google.cloud.tpu.v1.Tpu.StopNode` (LRO)  
`google.cloud.tpu.v1alpha1.Tpu.CreateNode` (LRO)  
`google.cloud.tpu.v1alpha1.Tpu.DeleteNode` (LRO)  
`google.cloud.tpu.v1alpha1.Tpu.ReimageNode` (LRO)  
`google.cloud.tpu.v1alpha1.Tpu.StartNode` (LRO)  
`google.cloud.tpu.v1alpha1.Tpu.StopNode` (LRO)  
`google.cloud.tpu.v2.Tpu.CreateNode` (LRO)  
`google.cloud.tpu.v2.Tpu.CreateQueuedResource` (LRO)  
`google.cloud.tpu.v2.Tpu.DeleteNode` (LRO)  
`google.cloud.tpu.v2.Tpu.DeleteQueuedResource` (LRO)  
`google.cloud.tpu.v2.Tpu.ResetQueuedResource` (LRO)  
`google.cloud.tpu.v2.Tpu.StartNode` (LRO)  
`google.cloud.tpu.v2.Tpu.StopNode` (LRO)  
`google.cloud.tpu.v2.Tpu.UpdateNode` (LRO)  
`google.cloud.tpu.v2alpha1.Tpu.CreateNode` (LRO)  
`google.cloud.tpu.v2alpha1.Tpu.CreateQueuedResource` (LRO)  
`google.cloud.tpu.v2alpha1.Tpu.DeleteNode` (LRO)  
`google.cloud.tpu.v2alpha1.Tpu.DeleteQueuedResource` (LRO)  
`google.cloud.tpu.v2alpha1.Tpu.ResetQueuedResource` (LRO)  
`google.cloud.tpu.v2alpha1.Tpu.SimulateMaintenanceEvent` (LRO)  
`google.cloud.tpu.v2alpha1.Tpu.StartNode` (LRO)  
`google.cloud.tpu.v2alpha1.Tpu.StopNode` (LRO)  
`google.cloud.tpu.v2alpha1.Tpu.UpdateNode` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud TPU.

### `google.cloud.tpu.v1.Tpu`

The following audit logs are associated with methods belonging to `google.cloud.tpu.v1.Tpu`.

#### `CreateNode`

  * **Method** : `google.cloud.tpu.v1.Tpu.CreateNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v1.Tpu.CreateNode" `  




#### `DeleteNode`

  * **Method** : `google.cloud.tpu.v1.Tpu.DeleteNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v1.Tpu.DeleteNode" `  




#### `GetNode`

  * **Method** : `google.cloud.tpu.v1.Tpu.GetNode`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `tpu.nodes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v1.Tpu.GetNode" `  




#### `ListNodes`

  * **Method** : `google.cloud.tpu.v1.Tpu.ListNodes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `tpu.nodes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v1.Tpu.ListNodes" `  




#### `ReimageNode`

  * **Method** : `google.cloud.tpu.v1.Tpu.ReimageNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.reimage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v1.Tpu.ReimageNode" `  




#### `StartNode`

  * **Method** : `google.cloud.tpu.v1.Tpu.StartNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.start - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v1.Tpu.StartNode" `  




#### `StopNode`

  * **Method** : `google.cloud.tpu.v1.Tpu.StopNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v1.Tpu.StopNode" `  




### `google.cloud.tpu.v1alpha1.Tpu`

The following audit logs are associated with methods belonging to `google.cloud.tpu.v1alpha1.Tpu`.

#### `CreateNode`

  * **Method** : `google.cloud.tpu.v1alpha1.Tpu.CreateNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v1alpha1.Tpu.CreateNode" `  




#### `DeleteNode`

  * **Method** : `google.cloud.tpu.v1alpha1.Tpu.DeleteNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v1alpha1.Tpu.DeleteNode" `  




#### `GetNode`

  * **Method** : `google.cloud.tpu.v1alpha1.Tpu.GetNode`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `tpu.nodes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v1alpha1.Tpu.GetNode" `  




#### `ListNodes`

  * **Method** : `google.cloud.tpu.v1alpha1.Tpu.ListNodes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `tpu.nodes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v1alpha1.Tpu.ListNodes" `  




#### `ReimageNode`

  * **Method** : `google.cloud.tpu.v1alpha1.Tpu.ReimageNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.reimage - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v1alpha1.Tpu.ReimageNode" `  




#### `StartNode`

  * **Method** : `google.cloud.tpu.v1alpha1.Tpu.StartNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.start - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v1alpha1.Tpu.StartNode" `  




#### `StopNode`

  * **Method** : `google.cloud.tpu.v1alpha1.Tpu.StopNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v1alpha1.Tpu.StopNode" `  




### `google.cloud.tpu.v2.Tpu`

The following audit logs are associated with methods belonging to `google.cloud.tpu.v2.Tpu`.

#### `CreateNode`

  * **Method** : `google.cloud.tpu.v2.Tpu.CreateNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2.Tpu.CreateNode" `  




#### `CreateQueuedResource`

  * **Method** : `google.cloud.tpu.v2.Tpu.CreateQueuedResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2.Tpu.CreateQueuedResource" `  




#### `DeleteNode`

  * **Method** : `google.cloud.tpu.v2.Tpu.DeleteNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2.Tpu.DeleteNode" `  




#### `DeleteQueuedResource`

  * **Method** : `google.cloud.tpu.v2.Tpu.DeleteQueuedResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2.Tpu.DeleteQueuedResource" `  




#### `GetGuestAttributes`

  * **Method** : `google.cloud.tpu.v2.Tpu.GetGuestAttributes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `tpu.nodes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2.Tpu.GetGuestAttributes" `  




#### `GetNode`

  * **Method** : `google.cloud.tpu.v2.Tpu.GetNode`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `tpu.nodes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2.Tpu.GetNode" `  




#### `GetQueuedResource`

  * **Method** : `google.cloud.tpu.v2.Tpu.GetQueuedResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `tpu.nodes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2.Tpu.GetQueuedResource" `  




#### `ListNodes`

  * **Method** : `google.cloud.tpu.v2.Tpu.ListNodes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `tpu.nodes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2.Tpu.ListNodes" `  




#### `ListQueuedResources`

  * **Method** : `google.cloud.tpu.v2.Tpu.ListQueuedResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `tpu.nodes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2.Tpu.ListQueuedResources" `  




#### `ResetQueuedResource`

  * **Method** : `google.cloud.tpu.v2.Tpu.ResetQueuedResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.reset - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2.Tpu.ResetQueuedResource" `  




#### `StartNode`

  * **Method** : `google.cloud.tpu.v2.Tpu.StartNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.start - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2.Tpu.StartNode" `  




#### `StopNode`

  * **Method** : `google.cloud.tpu.v2.Tpu.StopNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2.Tpu.StopNode" `  




#### `UpdateNode`

  * **Method** : `google.cloud.tpu.v2.Tpu.UpdateNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2.Tpu.UpdateNode" `  




### `google.cloud.tpu.v2alpha1.Tpu`

The following audit logs are associated with methods belonging to `google.cloud.tpu.v2alpha1.Tpu`.

#### `CreateNode`

  * **Method** : `google.cloud.tpu.v2alpha1.Tpu.CreateNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2alpha1.Tpu.CreateNode" `  




#### `CreateQueuedResource`

  * **Method** : `google.cloud.tpu.v2alpha1.Tpu.CreateQueuedResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2alpha1.Tpu.CreateQueuedResource" `  




#### `DeleteNode`

  * **Method** : `google.cloud.tpu.v2alpha1.Tpu.DeleteNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2alpha1.Tpu.DeleteNode" `  




#### `DeleteQueuedResource`

  * **Method** : `google.cloud.tpu.v2alpha1.Tpu.DeleteQueuedResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2alpha1.Tpu.DeleteQueuedResource" `  




#### `GetGuestAttributes`

  * **Method** : `google.cloud.tpu.v2alpha1.Tpu.GetGuestAttributes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `tpu.nodes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2alpha1.Tpu.GetGuestAttributes" `  




#### `GetNode`

  * **Method** : `google.cloud.tpu.v2alpha1.Tpu.GetNode`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `tpu.nodes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2alpha1.Tpu.GetNode" `  




#### `GetQueuedResource`

  * **Method** : `google.cloud.tpu.v2alpha1.Tpu.GetQueuedResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `tpu.nodes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2alpha1.Tpu.GetQueuedResource" `  




#### `ListNodes`

  * **Method** : `google.cloud.tpu.v2alpha1.Tpu.ListNodes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `tpu.nodes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2alpha1.Tpu.ListNodes" `  




#### `ListQueuedResources`

  * **Method** : `google.cloud.tpu.v2alpha1.Tpu.ListQueuedResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `tpu.nodes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2alpha1.Tpu.ListQueuedResources" `  




#### `ListReservations`

  * **Method** : `google.cloud.tpu.v2alpha1.Tpu.ListReservations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `tpu.nodes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2alpha1.Tpu.ListReservations" `  




#### `ResetQueuedResource`

  * **Method** : `google.cloud.tpu.v2alpha1.Tpu.ResetQueuedResource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.reset - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2alpha1.Tpu.ResetQueuedResource" `  




#### `SimulateMaintenanceEvent`

  * **Method** : `google.cloud.tpu.v2alpha1.Tpu.SimulateMaintenanceEvent`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.simulateMaintenanceEvent - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2alpha1.Tpu.SimulateMaintenanceEvent" `  




#### `StartNode`

  * **Method** : `google.cloud.tpu.v2alpha1.Tpu.StartNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.start - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2alpha1.Tpu.StartNode" `  




#### `StopNode`

  * **Method** : `google.cloud.tpu.v2alpha1.Tpu.StopNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2alpha1.Tpu.StopNode" `  




#### `UpdateNode`

  * **Method** : `google.cloud.tpu.v2alpha1.Tpu.UpdateNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `tpu.nodes.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.tpu.v2alpha1.Tpu.UpdateNode" `  




## System events

System Event audit logs are generated by GCP systems, not direct user action. For more information, see [System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event).

Method Name | Filter For This Event | Notes  
---|---|---  
tpu.nodes.restart |  ` protoPayload.methodName="tpu.nodes.restart" ` | Occurs when a terminated node is repaired and restarted.  
tpu.nodes.terminate |  ` protoPayload.methodName="tpu.nodes.terminate" ` | Occurs when a node has been terminated involuntarily, such as due to a maintenance event. The reason for termination is available in `protoPayload.metadata.terminateReason`.  
  
## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.cloud.tpu.v1.Tpu.GetAcceleratorType`
  * `google.cloud.tpu.v1.Tpu.GetTensorFlowVersion`
  * `google.cloud.tpu.v1.Tpu.ListAcceleratorTypes`
  * `google.cloud.tpu.v1.Tpu.ListTensorFlowVersions`
  * `google.cloud.tpu.v1alpha1.Tpu.GetAcceleratorType`
  * `google.cloud.tpu.v1alpha1.Tpu.GetTensorFlowVersion`
  * `google.cloud.tpu.v1alpha1.Tpu.ListAcceleratorTypes`
  * `google.cloud.tpu.v1alpha1.Tpu.ListTensorFlowVersions`
  * `google.cloud.tpu.v2.Tpu.GetAcceleratorType`
  * `google.cloud.tpu.v2.Tpu.GetRuntimeVersion`
  * `google.cloud.tpu.v2.Tpu.ListAcceleratorTypes`
  * `google.cloud.tpu.v2.Tpu.ListRuntimeVersions`
  * `google.cloud.tpu.v2alpha1.Tpu.GetAcceleratorType`
  * `google.cloud.tpu.v2alpha1.Tpu.GetRuntimeVersion`
  * `google.cloud.tpu.v2alpha1.Tpu.ListAcceleratorTypes`
  * `google.cloud.tpu.v2alpha1.Tpu.ListRuntimeVersions`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
