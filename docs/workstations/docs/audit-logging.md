---
url: https://docs.cloud.google.com/workstations/docs/audit-logging/
title: Cloud Workstations audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:07:02.364494+00:00
---

# Cloud Workstations audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Cloud Workstations audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Cloud Workstations. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Cloud Workstations audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="workstations.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Workstations generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.workstations.v1.Workstations.GenerateAccessToken`  
`google.cloud.workstations.v1.Workstations.GetWorkstation`  
`google.cloud.workstations.v1.Workstations.GetWorkstationCluster`  
`google.cloud.workstations.v1.Workstations.GetWorkstationConfig`  
`google.cloud.workstations.v1.Workstations.ListWorkstationClusters`  
`google.cloud.workstations.v1.Workstations.ListWorkstationConfigs`  
`google.cloud.workstations.v1.Workstations.ListWorkstations`  
`google.cloud.workstations.v1beta.Workstations.GenerateAccessToken`  
`google.cloud.workstations.v1beta.Workstations.GetWorkstation`  
`google.cloud.workstations.v1beta.Workstations.GetWorkstationCluster`  
`google.cloud.workstations.v1beta.Workstations.GetWorkstationConfig`  
`google.cloud.workstations.v1beta.Workstations.ListWorkstationClusters`  
`google.cloud.workstations.v1beta.Workstations.ListWorkstationConfigs`  
`google.cloud.workstations.v1beta.Workstations.ListWorkstations`  
`google.cloud.workstations.v1beta.Workstations.PushCredentials` (LRO)  
`GetIamPolicy`  
`ADMIN_WRITE` | `google.cloud.workstations.v1.Workstations.CreateWorkstation` (LRO)  
`google.cloud.workstations.v1.Workstations.CreateWorkstationCluster` (LRO)  
`google.cloud.workstations.v1.Workstations.CreateWorkstationConfig` (LRO)  
`google.cloud.workstations.v1.Workstations.DeleteWorkstation` (LRO)  
`google.cloud.workstations.v1.Workstations.DeleteWorkstationCluster` (LRO)  
`google.cloud.workstations.v1.Workstations.DeleteWorkstationConfig` (LRO)  
`google.cloud.workstations.v1.Workstations.StartWorkstation` (LRO)  
`google.cloud.workstations.v1.Workstations.StopWorkstation` (LRO)  
`google.cloud.workstations.v1.Workstations.SuspendWorkstation`  
`google.cloud.workstations.v1.Workstations.UpdateWorkstation` (LRO)  
`google.cloud.workstations.v1.Workstations.UpdateWorkstationCluster` (LRO)  
`google.cloud.workstations.v1.Workstations.UpdateWorkstationConfig` (LRO)  
`google.cloud.workstations.v1beta.Workstations.CreateWorkstation` (LRO)  
`google.cloud.workstations.v1beta.Workstations.CreateWorkstationCluster` (LRO)  
`google.cloud.workstations.v1beta.Workstations.CreateWorkstationConfig` (LRO)  
`google.cloud.workstations.v1beta.Workstations.DeleteWorkstation` (LRO)  
`google.cloud.workstations.v1beta.Workstations.DeleteWorkstationCluster` (LRO)  
`google.cloud.workstations.v1beta.Workstations.DeleteWorkstationConfig` (LRO)  
`google.cloud.workstations.v1beta.Workstations.StartWorkstation` (LRO)  
`google.cloud.workstations.v1beta.Workstations.StopWorkstation` (LRO)  
`google.cloud.workstations.v1beta.Workstations.SuspendWorkstation` (LRO)  
`google.cloud.workstations.v1beta.Workstations.UpdateWorkstation` (LRO)  
`google.cloud.workstations.v1beta.Workstations.UpdateWorkstationCluster` (LRO)  
`google.cloud.workstations.v1beta.Workstations.UpdateWorkstationConfig` (LRO)  
`SetIamPolicy`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the [Identity and Access Management documentation](https://docs.cloud.google.com/workstations/docs/access-control) for Cloud Workstations.

### `google.cloud.workstations.v1.Workstations`

The following audit logs are associated with methods belonging to `google.cloud.workstations.v1.Workstations`.

#### `CreateWorkstation`

  * **Method** : `google.cloud.workstations.v1.Workstations.CreateWorkstation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1.Workstations.CreateWorkstation" `  




#### `CreateWorkstationCluster`

  * **Method** : `google.cloud.workstations.v1.Workstations.CreateWorkstationCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstationClusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1.Workstations.CreateWorkstationCluster" `  




#### `CreateWorkstationConfig`

  * **Method** : `google.cloud.workstations.v1.Workstations.CreateWorkstationConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstationConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1.Workstations.CreateWorkstationConfig" `  




#### `DeleteWorkstation`

  * **Method** : `google.cloud.workstations.v1.Workstations.DeleteWorkstation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1.Workstations.DeleteWorkstation" `  




#### `DeleteWorkstationCluster`

  * **Method** : `google.cloud.workstations.v1.Workstations.DeleteWorkstationCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstationClusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1.Workstations.DeleteWorkstationCluster" `  




#### `DeleteWorkstationConfig`

  * **Method** : `google.cloud.workstations.v1.Workstations.DeleteWorkstationConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstationConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1.Workstations.DeleteWorkstationConfig" `  




#### `GenerateAccessToken`

  * **Method** : `google.cloud.workstations.v1.Workstations.GenerateAccessToken`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workstations.workstations.use - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1.Workstations.GenerateAccessToken" `  




#### `GetWorkstation`

  * **Method** : `google.cloud.workstations.v1.Workstations.GetWorkstation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workstations.workstations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1.Workstations.GetWorkstation" `  




#### `GetWorkstationCluster`

  * **Method** : `google.cloud.workstations.v1.Workstations.GetWorkstationCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workstations.workstationClusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1.Workstations.GetWorkstationCluster" `  




#### `GetWorkstationConfig`

  * **Method** : `google.cloud.workstations.v1.Workstations.GetWorkstationConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workstations.workstationConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1.Workstations.GetWorkstationConfig" `  




#### `ListWorkstationClusters`

  * **Method** : `google.cloud.workstations.v1.Workstations.ListWorkstationClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workstations.workstationClusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1.Workstations.ListWorkstationClusters" `  




#### `ListWorkstationConfigs`

  * **Method** : `google.cloud.workstations.v1.Workstations.ListWorkstationConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workstations.workstationConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1.Workstations.ListWorkstationConfigs" `  




#### `ListWorkstations`

  * **Method** : `google.cloud.workstations.v1.Workstations.ListWorkstations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workstations.workstations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1.Workstations.ListWorkstations" `  




#### `StartWorkstation`

  * **Method** : `google.cloud.workstations.v1.Workstations.StartWorkstation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstations.start - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1.Workstations.StartWorkstation" `  




#### `StopWorkstation`

  * **Method** : `google.cloud.workstations.v1.Workstations.StopWorkstation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstations.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1.Workstations.StopWorkstation" `  




#### `SuspendWorkstation`

  * **Method** : `google.cloud.workstations.v1.Workstations.SuspendWorkstation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstations.suspend - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1.Workstations.SuspendWorkstation" `  




#### `UpdateWorkstation`

  * **Method** : `google.cloud.workstations.v1.Workstations.UpdateWorkstation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1.Workstations.UpdateWorkstation" `  




#### `UpdateWorkstationCluster`

  * **Method** : `google.cloud.workstations.v1.Workstations.UpdateWorkstationCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstationClusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1.Workstations.UpdateWorkstationCluster" `  




#### `UpdateWorkstationConfig`

  * **Method** : `google.cloud.workstations.v1.Workstations.UpdateWorkstationConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstationConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1.Workstations.UpdateWorkstationConfig" `  




### `google.cloud.workstations.v1beta.Workstations`

The following audit logs are associated with methods belonging to `google.cloud.workstations.v1beta.Workstations`.

#### `CreateWorkstation`

  * **Method** : `google.cloud.workstations.v1beta.Workstations.CreateWorkstation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstations.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1beta.Workstations.CreateWorkstation" `  




#### `CreateWorkstationCluster`

  * **Method** : `google.cloud.workstations.v1beta.Workstations.CreateWorkstationCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstationClusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1beta.Workstations.CreateWorkstationCluster" `  




#### `CreateWorkstationConfig`

  * **Method** : `google.cloud.workstations.v1beta.Workstations.CreateWorkstationConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstationConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1beta.Workstations.CreateWorkstationConfig" `  




#### `DeleteWorkstation`

  * **Method** : `google.cloud.workstations.v1beta.Workstations.DeleteWorkstation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1beta.Workstations.DeleteWorkstation" `  




#### `DeleteWorkstationCluster`

  * **Method** : `google.cloud.workstations.v1beta.Workstations.DeleteWorkstationCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstationClusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1beta.Workstations.DeleteWorkstationCluster" `  




#### `DeleteWorkstationConfig`

  * **Method** : `google.cloud.workstations.v1beta.Workstations.DeleteWorkstationConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstationConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1beta.Workstations.DeleteWorkstationConfig" `  




#### `GenerateAccessToken`

  * **Method** : `google.cloud.workstations.v1beta.Workstations.GenerateAccessToken`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workstations.workstations.use - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1beta.Workstations.GenerateAccessToken" `  




#### `GetWorkstation`

  * **Method** : `google.cloud.workstations.v1beta.Workstations.GetWorkstation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workstations.workstations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1beta.Workstations.GetWorkstation" `  




#### `GetWorkstationCluster`

  * **Method** : `google.cloud.workstations.v1beta.Workstations.GetWorkstationCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workstations.workstationClusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1beta.Workstations.GetWorkstationCluster" `  




#### `GetWorkstationConfig`

  * **Method** : `google.cloud.workstations.v1beta.Workstations.GetWorkstationConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workstations.workstationConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1beta.Workstations.GetWorkstationConfig" `  




#### `ListWorkstationClusters`

  * **Method** : `google.cloud.workstations.v1beta.Workstations.ListWorkstationClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workstations.workstationClusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1beta.Workstations.ListWorkstationClusters" `  




#### `ListWorkstationConfigs`

  * **Method** : `google.cloud.workstations.v1beta.Workstations.ListWorkstationConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workstations.workstationConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1beta.Workstations.ListWorkstationConfigs" `  




#### `ListWorkstations`

  * **Method** : `google.cloud.workstations.v1beta.Workstations.ListWorkstations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workstations.workstations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1beta.Workstations.ListWorkstations" `  




#### `PushCredentials`

  * **Method** : `google.cloud.workstations.v1beta.Workstations.PushCredentials`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workstations.workstations.use - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1beta.Workstations.PushCredentials" `  




#### `StartWorkstation`

  * **Method** : `google.cloud.workstations.v1beta.Workstations.StartWorkstation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstations.start - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1beta.Workstations.StartWorkstation" `  




#### `StopWorkstation`

  * **Method** : `google.cloud.workstations.v1beta.Workstations.StopWorkstation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstations.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1beta.Workstations.StopWorkstation" `  




#### `SuspendWorkstation`

  * **Method** : `google.cloud.workstations.v1beta.Workstations.SuspendWorkstation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstations.suspend - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1beta.Workstations.SuspendWorkstation" `  




#### `UpdateWorkstation`

  * **Method** : `google.cloud.workstations.v1beta.Workstations.UpdateWorkstation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstations.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1beta.Workstations.UpdateWorkstation" `  




#### `UpdateWorkstationCluster`

  * **Method** : `google.cloud.workstations.v1beta.Workstations.UpdateWorkstationCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstationClusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1beta.Workstations.UpdateWorkstationCluster" `  




#### `UpdateWorkstationConfig`

  * **Method** : `google.cloud.workstations.v1beta.Workstations.UpdateWorkstationConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstationConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.workstations.v1beta.Workstations.UpdateWorkstationConfig" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `workstations.workstations.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `workstations.workstations.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="SetIamPolicy" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.cloud.workstations.v1.Workstations.ListUsableWorkstationConfigs`
  * `google.cloud.workstations.v1.Workstations.ListUsableWorkstations`
  * `google.cloud.workstations.v1beta.Workstations.ListUsableWorkstationConfigs`
  * `google.cloud.workstations.v1beta.Workstations.ListUsableWorkstations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
