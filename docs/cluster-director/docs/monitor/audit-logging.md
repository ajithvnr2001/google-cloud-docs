---
url: https://docs.cloud.google.com/cluster-director/docs/monitor/audit-logging/
title: Audit Logging \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:00.464192+00:00
---

# Audit Logging  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/monitor/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Audit Logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Cluster Director. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Cluster Director audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="hypercomputecluster.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cluster Director generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.hypercomputecluster.v1.HypercomputeCluster.GetCluster`  
`google.cloud.hypercomputecluster.v1.HypercomputeCluster.ListClusters`  
`google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.GetCluster`  
`google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.GetNode`  
`google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.ListClusters`  
`google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.ListNodes`  
`google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.GetMachineLearningRun`  
`google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.GetProfilerTarget`  
`google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.ListMachineLearningRuns`  
`google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.ListProfileSessions`  
`google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.ListProfilerTargets`  
`google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.GetCluster`  
`google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.ListClusters`  
`google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.ListNodes`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.hypercomputecluster.v1.HypercomputeCluster.CreateCluster` (LRO)  
`google.cloud.hypercomputecluster.v1.HypercomputeCluster.DeleteCluster` (LRO)  
`google.cloud.hypercomputecluster.v1.HypercomputeCluster.UpdateCluster` (LRO)  
`google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.CreateCluster` (LRO)  
`google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.DeleteCluster` (LRO)  
`google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.UpdateCluster` (LRO)  
`google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.CreateMachineLearningRun` (LRO)  
`google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.CreateProfilerTarget` (LRO)  
`google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.DeleteMachineLearningRun` (LRO)  
`google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.DeleteProfilerTarget`  
`google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.StartContinuousProfiling` (LRO)  
`google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.StopContinuousProfiling`  
`google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.UpdateMachineLearningRun` (LRO)  
`google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.CreateCluster` (LRO)  
`google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.DeleteCluster` (LRO)  
`google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.UpdateCluster` (LRO)  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cluster Director.

### `google.cloud.hypercomputecluster.v1.HypercomputeCluster`

The following audit logs are associated with methods belonging to `google.cloud.hypercomputecluster.v1.HypercomputeCluster`.

#### `CreateCluster`

  * **Method** : `google.cloud.hypercomputecluster.v1.HypercomputeCluster.CreateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `hypercomputecluster.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1.HypercomputeCluster.CreateCluster" `  




#### `DeleteCluster`

  * **Method** : `google.cloud.hypercomputecluster.v1.HypercomputeCluster.DeleteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `hypercomputecluster.clusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1.HypercomputeCluster.DeleteCluster" `  




#### `GetCluster`

  * **Method** : `google.cloud.hypercomputecluster.v1.HypercomputeCluster.GetCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `hypercomputecluster.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1.HypercomputeCluster.GetCluster" `  




#### `ListClusters`

  * **Method** : `google.cloud.hypercomputecluster.v1.HypercomputeCluster.ListClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `hypercomputecluster.clusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1.HypercomputeCluster.ListClusters" `  




#### `UpdateCluster`

  * **Method** : `google.cloud.hypercomputecluster.v1.HypercomputeCluster.UpdateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `hypercomputecluster.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1.HypercomputeCluster.UpdateCluster" `  




### `google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster`

The following audit logs are associated with methods belonging to `google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster`.

#### `CreateCluster`

  * **Method** : `google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.CreateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `hypercomputecluster.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.CreateCluster" `  




#### `DeleteCluster`

  * **Method** : `google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.DeleteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `hypercomputecluster.clusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.DeleteCluster" `  




#### `GetCluster`

  * **Method** : `google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.GetCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `hypercomputecluster.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.GetCluster" `  




#### `GetNode`

  * **Method** : `google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.GetNode`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `hypercomputecluster.nodes.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.GetNode" `  




#### `ListClusters`

  * **Method** : `google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.ListClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `hypercomputecluster.clusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.ListClusters" `  




#### `ListNodes`

  * **Method** : `google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.ListNodes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `hypercomputecluster.nodes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.ListNodes" `  




#### `UpdateCluster`

  * **Method** : `google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.UpdateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `hypercomputecluster.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1alpha.HypercomputeCluster.UpdateCluster" `  




### `google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns`

The following audit logs are associated with methods belonging to `google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns`.

#### `CreateMachineLearningRun`

  * **Method** : `google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.CreateMachineLearningRun`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `hypercomputecluster.machineLearningRuns.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.CreateMachineLearningRun" `  




#### `CreateProfilerTarget`

  * **Method** : `google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.CreateProfilerTarget`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `hypercomputecluster.profilerTargets.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.CreateProfilerTarget" `  




#### `DeleteMachineLearningRun`

  * **Method** : `google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.DeleteMachineLearningRun`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `hypercomputecluster.machineLearningRuns.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.DeleteMachineLearningRun" `  




#### `DeleteProfilerTarget`

  * **Method** : `google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.DeleteProfilerTarget`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `hypercomputecluster.profilerTargets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.DeleteProfilerTarget" `  




#### `GetMachineLearningRun`

  * **Method** : `google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.GetMachineLearningRun`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `hypercomputecluster.machineLearningRuns.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.GetMachineLearningRun" `  




#### `GetProfilerTarget`

  * **Method** : `google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.GetProfilerTarget`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `hypercomputecluster.profilerTargets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.GetProfilerTarget" `  




#### `ListMachineLearningRuns`

  * **Method** : `google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.ListMachineLearningRuns`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `hypercomputecluster.machineLearningRuns.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.ListMachineLearningRuns" `  




#### `ListProfileSessions`

  * **Method** : `google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.ListProfileSessions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `hypercomputecluster.machineLearningRuns.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.ListProfileSessions" `  




#### `ListProfilerTargets`

  * **Method** : `google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.ListProfilerTargets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `hypercomputecluster.profilerTargets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.ListProfilerTargets" `  




#### `StartContinuousProfiling`

  * **Method** : `google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.StartContinuousProfiling`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `hypercomputecluster.machineLearningRuns.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.StartContinuousProfiling" `  




#### `StopContinuousProfiling`

  * **Method** : `google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.StopContinuousProfiling`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `hypercomputecluster.machineLearningRuns.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.StopContinuousProfiling" `  




#### `UpdateMachineLearningRun`

  * **Method** : `google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.UpdateMachineLearningRun`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `hypercomputecluster.machineLearningRuns.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1alpha.MachineLearningRuns.UpdateMachineLearningRun" `  




### `google.cloud.hypercomputecluster.v1beta.HypercomputeCluster`

The following audit logs are associated with methods belonging to `google.cloud.hypercomputecluster.v1beta.HypercomputeCluster`.

#### `CreateCluster`

  * **Method** : `google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.CreateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `hypercomputecluster.clusters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.CreateCluster" `  




#### `DeleteCluster`

  * **Method** : `google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.DeleteCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `hypercomputecluster.clusters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.DeleteCluster" `  




#### `GetCluster`

  * **Method** : `google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.GetCluster`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `hypercomputecluster.clusters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.GetCluster" `  




#### `ListClusters`

  * **Method** : `google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.ListClusters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `hypercomputecluster.clusters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.ListClusters" `  




#### `ListNodes`

  * **Method** : `google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.ListNodes`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `hypercomputecluster.nodes.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.ListNodes" `  




#### `UpdateCluster`

  * **Method** : `google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.UpdateCluster`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `hypercomputecluster.clusters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.UpdateCluster" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `hypercomputecluster.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `hypercomputecluster.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `hypercomputecluster.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `hypercomputecluster.operations.list - ADMIN_READ`
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
