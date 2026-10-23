---
url: https://docs.cloud.google.com/managed-spark/docs/guides/dataprocrm-audit-logging/
title: Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:32.442625+00:00
---

# Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/dataprocrm-audit-logging/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resource Manager audit logging

This document lists the audited methods for Dataproc Resource Manager. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Dataproc Resource Manager audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="dataprocrm.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Dataproc Resource Manager generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.dataproc.rm.v1.DataprocResourceManager.GetNode`  
`google.cloud.dataproc.rm.v1.DataprocResourceManager.GetNodePool`  
`google.cloud.dataproc.rm.v1.DataprocResourceManager.GetWorkload`  
`google.cloud.dataproc.rm.v1.DataprocResourceManager.ListNodePools`  
`google.cloud.dataproc.rm.v1.DataprocResourceManager.ListNodes`  
`google.cloud.dataproc.rm.v1.DataprocResourceManager.ListWorkloads`  
`ADMIN_WRITE` | `google.cloud.dataproc.rm.v1.DataprocResourceManager.CancelWorkload`  
`google.cloud.dataproc.rm.v1.DataprocResourceManager.CreateNodePool` (LRO)  
`google.cloud.dataproc.rm.v1.DataprocResourceManager.CreateWorkload` (LRO)  
`google.cloud.dataproc.rm.v1.DataprocResourceManager.DeleteNodePool` (LRO)  
`google.cloud.dataproc.rm.v1.DataprocResourceManager.DeleteNodes` (LRO)  
`google.cloud.dataproc.rm.v1.DataprocResourceManager.DeleteWorkload` (LRO)  
`google.cloud.dataproc.rm.v1.DataprocResourceManager.HeartbeatNode`  
`google.cloud.dataproc.rm.v1.DataprocResourceManager.ResizeNodePool` (LRO)  
`DATA_READ` | `google.cloud.dataproc.rm.v1.DataprocResourceManager.MintOAuthToken`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Dataproc Resource Manager.

### `google.cloud.dataproc.rm.v1.DataprocResourceManager`

The following audit logs are associated with methods belonging to `google.cloud.dataproc.rm.v1.DataprocResourceManager`.

#### `CancelWorkload`

  * **Method** : `google.cloud.dataproc.rm.v1.DataprocResourceManager.CancelWorkload`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataprocrm.workloads.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.rm.v1.DataprocResourceManager.CancelWorkload" `  




#### `CreateNodePool`

  * **Method** : `google.cloud.dataproc.rm.v1.DataprocResourceManager.CreateNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataprocrm.nodePools.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.rm.v1.DataprocResourceManager.CreateNodePool" `  




#### `CreateWorkload`

  * **Method** : `google.cloud.dataproc.rm.v1.DataprocResourceManager.CreateWorkload`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataprocrm.workloads.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.rm.v1.DataprocResourceManager.CreateWorkload" `  




#### `DeleteNodePool`

  * **Method** : `google.cloud.dataproc.rm.v1.DataprocResourceManager.DeleteNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataprocrm.nodePools.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.rm.v1.DataprocResourceManager.DeleteNodePool" `  




#### `DeleteNodes`

  * **Method** : `google.cloud.dataproc.rm.v1.DataprocResourceManager.DeleteNodes`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataprocrm.nodePools.deleteNodes - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.rm.v1.DataprocResourceManager.DeleteNodes" `  




#### `DeleteWorkload`

  * **Method** : `google.cloud.dataproc.rm.v1.DataprocResourceManager.DeleteWorkload`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataprocrm.workloads.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.rm.v1.DataprocResourceManager.DeleteWorkload" `  




#### `GetNode`

  * **Method** : `google.cloud.dataproc.rm.v1.DataprocResourceManager.GetNode`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataprocrm.nodes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.rm.v1.DataprocResourceManager.GetNode" `  




#### `GetNodePool`

  * **Method** : `google.cloud.dataproc.rm.v1.DataprocResourceManager.GetNodePool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataprocrm.nodePools.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.rm.v1.DataprocResourceManager.GetNodePool" `  




#### `GetWorkload`

  * **Method** : `google.cloud.dataproc.rm.v1.DataprocResourceManager.GetWorkload`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataprocrm.workloads.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.rm.v1.DataprocResourceManager.GetWorkload" `  




#### `HeartbeatNode`

  * **Method** : `google.cloud.dataproc.rm.v1.DataprocResourceManager.HeartbeatNode`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataprocrm.nodes.heartbeat - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.rm.v1.DataprocResourceManager.HeartbeatNode" `  




#### `ListNodePools`

  * **Method** : `google.cloud.dataproc.rm.v1.DataprocResourceManager.ListNodePools`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataprocrm.nodePools.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.rm.v1.DataprocResourceManager.ListNodePools" `  




#### `ListNodes`

  * **Method** : `google.cloud.dataproc.rm.v1.DataprocResourceManager.ListNodes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataprocrm.nodes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.rm.v1.DataprocResourceManager.ListNodes" `  




#### `ListWorkloads`

  * **Method** : `google.cloud.dataproc.rm.v1.DataprocResourceManager.ListWorkloads`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataprocrm.workloads.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.rm.v1.DataprocResourceManager.ListWorkloads" `  




#### `MintOAuthToken`

  * **Method** : `google.cloud.dataproc.rm.v1.DataprocResourceManager.MintOAuthToken`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `dataprocrm.nodes.mintOAuthToken - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.rm.v1.DataprocResourceManager.MintOAuthToken" `  




#### `ResizeNodePool`

  * **Method** : `google.cloud.dataproc.rm.v1.DataprocResourceManager.ResizeNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `dataprocrm.nodePools.resize - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.dataproc.rm.v1.DataprocResourceManager.ResizeNodePool" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
