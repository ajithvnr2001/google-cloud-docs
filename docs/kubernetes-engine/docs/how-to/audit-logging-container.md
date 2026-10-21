---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging-container/
title: Google Kubernetes Engine audit logging \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:15.854182+00:00
---

# Google Kubernetes Engine audit logging  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging-container/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Google Kubernetes Engine audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Google Kubernetes Engine. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Google Kubernetes Engine audit logs use the service name `container.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="container.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Google Kubernetes Engine generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.container.v1.ClusterManager.CheckAutopilotCompatibility`  
`google.container.v1.ClusterManager.GetCluster`  
`google.container.v1.ClusterManager.GetNodePool`  
`google.container.v1.ClusterManager.GetOperation`  
`google.container.v1.ClusterManager.GetServerConfig`  
`google.container.v1.ClusterManager.ListClusters`  
`google.container.v1.ClusterManager.ListNodePools`  
`google.container.v1.ClusterManager.ListOperations`  
`google.container.v1beta1.ClusterManager.CheckAutopilotCompatibility`  
`google.container.v1beta1.ClusterManager.GetCluster`  
`google.container.v1beta1.ClusterManager.GetNodePool`  
`google.container.v1beta1.ClusterManager.GetOperation`  
`google.container.v1beta1.ClusterManager.GetServerConfig`  
`google.container.v1beta1.ClusterManager.ListClusters`  
`google.container.v1beta1.ClusterManager.ListNodePools`  
`google.container.v1beta1.ClusterManager.ListOperations`  
`ADMIN_WRITE` | `google.container.v1.ClusterManager.CancelOperation`  
`google.container.v1.ClusterManager.CompleteIPRotation` (LRO)  
`google.container.v1.ClusterManager.CompleteNodePoolUpgrade`  
`google.container.v1.ClusterManager.CreateCluster` (LRO)  
`google.container.v1.ClusterManager.CreateNodePool` (LRO)  
`google.container.v1.ClusterManager.DeleteCluster` (LRO)  
`google.container.v1.ClusterManager.DeleteNodePool` (LRO)  
`google.container.v1.ClusterManager.ListUsableSubnetworks`  
`google.container.v1.ClusterManager.RollbackNodePoolUpgrade` (LRO)  
`google.container.v1.ClusterManager.SetAddonsConfig` (LRO)  
`google.container.v1.ClusterManager.SetLabels` (LRO)  
`google.container.v1.ClusterManager.SetLegacyAbac` (LRO)  
`google.container.v1.ClusterManager.SetLocations` (LRO)  
`google.container.v1.ClusterManager.SetLoggingService` (LRO)  
`google.container.v1.ClusterManager.SetMaintenancePolicy` (LRO)  
`google.container.v1.ClusterManager.SetMasterAuth` (LRO)  
`google.container.v1.ClusterManager.SetMonitoringService` (LRO)  
`google.container.v1.ClusterManager.SetNetworkPolicy` (LRO)  
`google.container.v1.ClusterManager.SetNodePoolAutoscaling` (LRO)  
`google.container.v1.ClusterManager.SetNodePoolManagement` (LRO)  
`google.container.v1.ClusterManager.SetNodePoolSize` (LRO)  
`google.container.v1.ClusterManager.StartIPRotation` (LRO)  
`google.container.v1.ClusterManager.UpdateCluster` (LRO)  
`google.container.v1.ClusterManager.UpdateMaster` (LRO)  
`google.container.v1.ClusterManager.UpdateNodePool` (LRO)  
`google.container.v1beta1.ClusterManager.CancelOperation`  
`google.container.v1beta1.ClusterManager.CompleteIPRotation` (LRO)  
`google.container.v1beta1.ClusterManager.CompleteNodePoolUpgrade`  
`google.container.v1beta1.ClusterManager.CreateCluster` (LRO)  
`google.container.v1beta1.ClusterManager.CreateNodePool` (LRO)  
`google.container.v1beta1.ClusterManager.DeleteCluster` (LRO)  
`google.container.v1beta1.ClusterManager.DeleteNodePool` (LRO)  
`google.container.v1beta1.ClusterManager.ListUsableSubnetworks`  
`google.container.v1beta1.ClusterManager.RollbackNodePoolUpgrade` (LRO)  
`google.container.v1beta1.ClusterManager.SetLabels` (LRO)  
`google.container.v1beta1.ClusterManager.SetLegacyAbac` (LRO)  
`google.container.v1beta1.ClusterManager.SetLocations` (LRO)  
`google.container.v1beta1.ClusterManager.SetLoggingService` (LRO)  
`google.container.v1beta1.ClusterManager.SetMaintenancePolicy` (LRO)  
`google.container.v1beta1.ClusterManager.SetMasterAuth` (LRO)  
`google.container.v1beta1.ClusterManager.SetNetworkPolicy` (LRO)  
`google.container.v1beta1.ClusterManager.SetNodePoolAutoscaling` (LRO)  
`google.container.v1beta1.ClusterManager.SetNodePoolManagement` (LRO)  
`google.container.v1beta1.ClusterManager.SetNodePoolSize` (LRO)  
`google.container.v1beta1.ClusterManager.StartIPRotation` (LRO)  
`google.container.v1beta1.ClusterManager.UpdateCluster` (LRO)  
`google.container.v1beta1.ClusterManager.UpdateMaster` (LRO)  
`google.container.v1beta1.ClusterManager.UpdateNodePool` (LRO)  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Google Kubernetes Engine.

### `google.container.v1.ClusterManager`

The following audit logs are associated with methods belonging to `google.container.v1.ClusterManager`.

#### `CancelOperation`

  * **Method** : `google.container.v1.ClusterManager.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.CancelOperation" `  




#### `CheckAutopilotCompatibility`

  * **Method** : `google.container.v1.ClusterManager.CheckAutopilotCompatibility`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `container.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.CheckAutopilotCompatibility" `  




#### `CompleteIPRotation`

  * **Method** : `google.container.v1.ClusterManager.CompleteIPRotation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.CompleteIPRotation" `  




#### `CompleteNodePoolUpgrade`

  * **Method** : `google.container.v1.ClusterManager.CompleteNodePoolUpgrade`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.CompleteNodePoolUpgrade" `  




#### `CreateCluster`

  * **Method** : `google.container.v1.ClusterManager.CreateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.CreateCluster" `  




#### `CreateNodePool`

  * **Method** : `google.container.v1.ClusterManager.CreateNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.CreateNodePool" `  




#### `DeleteCluster`

  * **Method** : `google.container.v1.ClusterManager.DeleteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.DeleteCluster" `  




#### `DeleteNodePool`

  * **Method** : `google.container.v1.ClusterManager.DeleteNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.DeleteNodePool" `  




#### `GetCluster`

  * **Method** : `google.container.v1.ClusterManager.GetCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `container.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.GetCluster" `  




#### `GetNodePool`

  * **Method** : `google.container.v1.ClusterManager.GetNodePool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `container.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.GetNodePool" `  




#### `GetOperation`

  * **Method** : `google.container.v1.ClusterManager.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `container.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.GetOperation" `  




#### `GetServerConfig`

  * **Method** : `google.container.v1.ClusterManager.GetServerConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `container.clusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.GetServerConfig" `  




#### `ListClusters`

  * **Method** : `google.container.v1.ClusterManager.ListClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `container.clusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.ListClusters" `  




#### `ListNodePools`

  * **Method** : `google.container.v1.ClusterManager.ListNodePools`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `container.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.ListNodePools" `  




#### `ListOperations`

  * **Method** : `google.container.v1.ClusterManager.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `container.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.ListOperations" `  




#### `ListUsableSubnetworks`

  * **Method** : `google.container.v1.ClusterManager.ListUsableSubnetworks`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.ListUsableSubnetworks" `  




#### `RollbackNodePoolUpgrade`

  * **Method** : `google.container.v1.ClusterManager.RollbackNodePoolUpgrade`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.RollbackNodePoolUpgrade" `  




#### `SetAddonsConfig`

  * **Method** : `google.container.v1.ClusterManager.SetAddonsConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.SetAddonsConfig" `  




#### `SetLabels`

  * **Method** : `google.container.v1.ClusterManager.SetLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.SetLabels" `  




#### `SetLegacyAbac`

  * **Method** : `google.container.v1.ClusterManager.SetLegacyAbac`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.SetLegacyAbac" `  




#### `SetLocations`

  * **Method** : `google.container.v1.ClusterManager.SetLocations`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.SetLocations" `  




#### `SetLoggingService`

  * **Method** : `google.container.v1.ClusterManager.SetLoggingService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.SetLoggingService" `  




#### `SetMaintenancePolicy`

  * **Method** : `google.container.v1.ClusterManager.SetMaintenancePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.SetMaintenancePolicy" `  




#### `SetMasterAuth`

  * **Method** : `google.container.v1.ClusterManager.SetMasterAuth`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.SetMasterAuth" `  




#### `SetMonitoringService`

  * **Method** : `google.container.v1.ClusterManager.SetMonitoringService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.SetMonitoringService" `  




#### `SetNetworkPolicy`

  * **Method** : `google.container.v1.ClusterManager.SetNetworkPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.SetNetworkPolicy" `  




#### `SetNodePoolAutoscaling`

  * **Method** : `google.container.v1.ClusterManager.SetNodePoolAutoscaling`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.SetNodePoolAutoscaling" `  




#### `SetNodePoolManagement`

  * **Method** : `google.container.v1.ClusterManager.SetNodePoolManagement`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.SetNodePoolManagement" `  




#### `SetNodePoolSize`

  * **Method** : `google.container.v1.ClusterManager.SetNodePoolSize`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.SetNodePoolSize" `  




#### `StartIPRotation`

  * **Method** : `google.container.v1.ClusterManager.StartIPRotation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.StartIPRotation" `  




#### `UpdateCluster`

  * **Method** : `google.container.v1.ClusterManager.UpdateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.UpdateCluster" `  




#### `UpdateMaster`

  * **Method** : `google.container.v1.ClusterManager.UpdateMaster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.UpdateMaster" `  




#### `UpdateNodePool`

  * **Method** : `google.container.v1.ClusterManager.UpdateNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1.ClusterManager.UpdateNodePool" `  




### `google.container.v1beta1.ClusterManager`

The following audit logs are associated with methods belonging to `google.container.v1beta1.ClusterManager`.

#### `CancelOperation`

  * **Method** : `google.container.v1beta1.ClusterManager.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.CancelOperation" `  




#### `CheckAutopilotCompatibility`

  * **Method** : `google.container.v1beta1.ClusterManager.CheckAutopilotCompatibility`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `container.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.CheckAutopilotCompatibility" `  




#### `CompleteIPRotation`

  * **Method** : `google.container.v1beta1.ClusterManager.CompleteIPRotation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.CompleteIPRotation" `  




#### `CompleteNodePoolUpgrade`

  * **Method** : `google.container.v1beta1.ClusterManager.CompleteNodePoolUpgrade`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.CompleteNodePoolUpgrade" `  




#### `CreateCluster`

  * **Method** : `google.container.v1beta1.ClusterManager.CreateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.CreateCluster" `  




#### `CreateNodePool`

  * **Method** : `google.container.v1beta1.ClusterManager.CreateNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.CreateNodePool" `  




#### `DeleteCluster`

  * **Method** : `google.container.v1beta1.ClusterManager.DeleteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.DeleteCluster" `  




#### `DeleteNodePool`

  * **Method** : `google.container.v1beta1.ClusterManager.DeleteNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.DeleteNodePool" `  




#### `GetCluster`

  * **Method** : `google.container.v1beta1.ClusterManager.GetCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `container.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.GetCluster" `  




#### `GetNodePool`

  * **Method** : `google.container.v1beta1.ClusterManager.GetNodePool`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `container.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.GetNodePool" `  




#### `GetOperation`

  * **Method** : `google.container.v1beta1.ClusterManager.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `container.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.GetOperation" `  




#### `GetServerConfig`

  * **Method** : `google.container.v1beta1.ClusterManager.GetServerConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `container.clusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.GetServerConfig" `  




#### `ListClusters`

  * **Method** : `google.container.v1beta1.ClusterManager.ListClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `container.clusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.ListClusters" `  




#### `ListNodePools`

  * **Method** : `google.container.v1beta1.ClusterManager.ListNodePools`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `container.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.ListNodePools" `  




#### `ListOperations`

  * **Method** : `google.container.v1beta1.ClusterManager.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `container.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.ListOperations" `  




#### `ListUsableSubnetworks`

  * **Method** : `google.container.v1beta1.ClusterManager.ListUsableSubnetworks`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.ListUsableSubnetworks" `  




#### `RollbackNodePoolUpgrade`

  * **Method** : `google.container.v1beta1.ClusterManager.RollbackNodePoolUpgrade`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.RollbackNodePoolUpgrade" `  




#### `SetLabels`

  * **Method** : `google.container.v1beta1.ClusterManager.SetLabels`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.SetLabels" `  




#### `SetLegacyAbac`

  * **Method** : `google.container.v1beta1.ClusterManager.SetLegacyAbac`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.SetLegacyAbac" `  




#### `SetLocations`

  * **Method** : `google.container.v1beta1.ClusterManager.SetLocations`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.SetLocations" `  




#### `SetLoggingService`

  * **Method** : `google.container.v1beta1.ClusterManager.SetLoggingService`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.SetLoggingService" `  




#### `SetMaintenancePolicy`

  * **Method** : `google.container.v1beta1.ClusterManager.SetMaintenancePolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.SetMaintenancePolicy" `  




#### `SetMasterAuth`

  * **Method** : `google.container.v1beta1.ClusterManager.SetMasterAuth`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.SetMasterAuth" `  




#### `SetNetworkPolicy`

  * **Method** : `google.container.v1beta1.ClusterManager.SetNetworkPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.SetNetworkPolicy" `  




#### `SetNodePoolAutoscaling`

  * **Method** : `google.container.v1beta1.ClusterManager.SetNodePoolAutoscaling`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.SetNodePoolAutoscaling" `  




#### `SetNodePoolManagement`

  * **Method** : `google.container.v1beta1.ClusterManager.SetNodePoolManagement`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.SetNodePoolManagement" `  




#### `SetNodePoolSize`

  * **Method** : `google.container.v1beta1.ClusterManager.SetNodePoolSize`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.SetNodePoolSize" `  




#### `StartIPRotation`

  * **Method** : `google.container.v1beta1.ClusterManager.StartIPRotation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.StartIPRotation" `  




#### `UpdateCluster`

  * **Method** : `google.container.v1beta1.ClusterManager.UpdateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.UpdateCluster" `  




#### `UpdateMaster`

  * **Method** : `google.container.v1beta1.ClusterManager.UpdateMaster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.UpdateMaster" `  




#### `UpdateNodePool`

  * **Method** : `google.container.v1beta1.ClusterManager.UpdateNodePool`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `container.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.container.v1beta1.ClusterManager.UpdateNodePool" `  




## System events

System Event audit logs are generated by GCP systems, not direct user action. For more information, see [System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event).

Method Name | Filter For This Event | Notes  
---|---|---  
google.cloud.gkeauth.v1.Auth.IssueInternalClusterCertificate |  ` protoPayload.methodName="google.cloud.gkeauth.v1.Auth.IssueInternalClusterCertificate" ` |   
google.cloud.gkeauth.v1.Auth.IssueInternalEtcdClientCertificate |  ` protoPayload.methodName="google.cloud.gkeauth.v1.Auth.IssueInternalEtcdClientCertificate" ` |   
google.cloud.gkeauth.v1.Auth.IssueInternalEtcdPeerCertificate |  ` protoPayload.methodName="google.cloud.gkeauth.v1.Auth.IssueInternalEtcdPeerCertificate" ` |   
google.cloud.gkeauth.v1.Auth.IssueInternalEtcdServerCertificate |  ` protoPayload.methodName="google.cloud.gkeauth.v1.Auth.IssueInternalEtcdServerCertificate" ` |   
google.cloud.gkeauth.v1.Auth.SignCertificate |  ` protoPayload.methodName="google.cloud.gkeauth.v1.Auth.SignCertificate" ` |   
google.cloud.gkeauth.v1.Auth.SignServiceAccountJWT |  ` protoPayload.methodName="google.cloud.gkeauth.v1.Auth.SignServiceAccountJWT" ` |   
  
## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.container.v1.ClusterManager.GetJSONWebKeys`
  * `google.container.v1.ClusterManager.GetOpenIDConfig`
  * `google.container.v1beta1.ClusterManager.GetJSONWebKeys`
  * `google.container.v1beta1.ClusterManager.GetOpenIDConfig`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
