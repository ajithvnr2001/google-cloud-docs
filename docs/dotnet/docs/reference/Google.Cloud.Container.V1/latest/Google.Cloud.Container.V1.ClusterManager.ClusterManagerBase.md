---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.ClusterManager.ClusterManagerBase
title: Google Kubernetes Engine v1 API - Class ClusterManager.ClusterManagerBase (3.40.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:40.049319+00:00
---

# Google Kubernetes Engine v1 API - Class ClusterManager.ClusterManagerBase (3.40.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.ClusterManager.ClusterManagerBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Kubernetes Engine v1 API - Class ClusterManager.ClusterManagerBase (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0 
    
    
    [BindServiceMethod(typeof(ClusterManager), "BindService")]
    public abstract class ClusterManager.ClusterManagerBase

Reference documentation and code samples for the Google Kubernetes Engine v1 API class ClusterManager.ClusterManagerBase.

Base class for server-side implementations of ClusterManager

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ClusterManager.ClusterManagerBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Container.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1)

## Assembly

Google.Cloud.Container.V1.dll

## Methods 

### CancelOperation(CancelOperationRequest, ServerCallContext)
    
    
    public virtual Task<Empty> CancelOperation(CancelOperationRequest request, ServerCallContext context)

Cancels the specified operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.CancelOperationRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### CheckAutopilotCompatibility(CheckAutopilotCompatibilityRequest, ServerCallContext)
    
    
    public virtual Task<CheckAutopilotCompatibilityResponse> CheckAutopilotCompatibility(CheckAutopilotCompatibilityRequest request, ServerCallContext context)

Checks the cluster compatibility with Autopilot mode, and returns a list of compatibility issues.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckAutopilotCompatibilityRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.CheckAutopilotCompatibilityRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CheckAutopilotCompatibilityResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.CheckAutopilotCompatibilityResponse)` | The response to send back to the client (wrapped by a task).  
  
### CompleteControlPlaneUpgrade(CompleteControlPlaneUpgradeRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CompleteControlPlaneUpgrade(CompleteControlPlaneUpgradeRequest request, ServerCallContext context)

CompleteControlPlaneUpgrade completes the rollback-safe upgrade by performing the step two upgrade for a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CompleteControlPlaneUpgradeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.CompleteControlPlaneUpgradeRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### CompleteIPRotation(CompleteIPRotationRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CompleteIPRotation(CompleteIPRotationRequest request, ServerCallContext context)

Completes master IP rotation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CompleteIPRotationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.CompleteIPRotationRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### CompleteNodePoolUpgrade(CompleteNodePoolUpgradeRequest, ServerCallContext)
    
    
    public virtual Task<Empty> CompleteNodePoolUpgrade(CompleteNodePoolUpgradeRequest request, ServerCallContext context)

CompleteNodePoolUpgrade will signal an on-going node pool upgrade to complete.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CompleteNodePoolUpgradeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.CompleteNodePoolUpgradeRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response to send back to the client (wrapped by a task).  
  
### CreateCluster(CreateClusterRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateCluster(CreateClusterRequest request, ServerCallContext context)

Creates a cluster, consisting of the specified number and type of Google Compute Engine instances.

By default, the cluster is created in the project's [default network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks).

One firewall is added for the cluster. After cluster creation, the kubelet creates routes for each node to allow the containers on that node to communicate with all other instances in the cluster.

Finally, an entry is added to the project's global metadata indicating which CIDR range the cluster is using.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.CreateClusterRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### CreateNodePool(CreateNodePoolRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateNodePool(CreateNodePoolRequest request, ServerCallContext context)

Creates a node pool for a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateNodePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.CreateNodePoolRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### DeleteCluster(DeleteClusterRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteCluster(DeleteClusterRequest request, ServerCallContext context)

Deletes the cluster, including the Kubernetes endpoint and all worker nodes.

Firewalls and routes that were configured during cluster creation are also deleted.

Other Google Compute Engine resources that might be in use by the cluster, such as load balancer resources, are not deleted if they weren't present when the cluster was initially created.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.DeleteClusterRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### DeleteNodePool(DeleteNodePoolRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteNodePool(DeleteNodePoolRequest request, ServerCallContext context)

Deletes a node pool from a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteNodePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.DeleteNodePoolRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### FetchClusterUpgradeInfo(FetchClusterUpgradeInfoRequest, ServerCallContext)
    
    
    public virtual Task<ClusterUpgradeInfo> FetchClusterUpgradeInfo(FetchClusterUpgradeInfoRequest request, ServerCallContext context)

Fetch upgrade information of a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchClusterUpgradeInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.FetchClusterUpgradeInfoRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ClusterUpgradeInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.ClusterUpgradeInfo)` | The response to send back to the client (wrapped by a task).  
  
### FetchNodePoolUpgradeInfo(FetchNodePoolUpgradeInfoRequest, ServerCallContext)
    
    
    public virtual Task<NodePoolUpgradeInfo> FetchNodePoolUpgradeInfo(FetchNodePoolUpgradeInfoRequest request, ServerCallContext context)

Fetch upgrade information of a specific node pool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchNodePoolUpgradeInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.FetchNodePoolUpgradeInfoRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[NodePoolUpgradeInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.NodePoolUpgradeInfo)` | The response to send back to the client (wrapped by a task).  
  
### GetCluster(GetClusterRequest, ServerCallContext)
    
    
    public virtual Task<Cluster> GetCluster(GetClusterRequest request, ServerCallContext context)

Gets the details of a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.GetClusterRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Cluster)` | The response to send back to the client (wrapped by a task).  
  
### GetJSONWebKeys(GetJSONWebKeysRequest, ServerCallContext)
    
    
    public virtual Task<GetJSONWebKeysResponse> GetJSONWebKeys(GetJSONWebKeysRequest request, ServerCallContext context)

Gets the public component of the cluster signing keys in JSON Web Key format.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetJSONWebKeysRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.GetJSONWebKeysRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GetJSONWebKeysResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.GetJSONWebKeysResponse)` | The response to send back to the client (wrapped by a task).  
  
### GetNodePool(GetNodePoolRequest, ServerCallContext)
    
    
    public virtual Task<NodePool> GetNodePool(GetNodePoolRequest request, ServerCallContext context)

Retrieves the requested node pool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetNodePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.GetNodePoolRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[NodePool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.NodePool)` | The response to send back to the client (wrapped by a task).  
  
### GetOperation(GetOperationRequest, ServerCallContext)
    
    
    public virtual Task<Operation> GetOperation(GetOperationRequest request, ServerCallContext context)

Gets the specified operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.GetOperationRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### GetServerConfig(GetServerConfigRequest, ServerCallContext)
    
    
    public virtual Task<ServerConfig> GetServerConfig(GetServerConfigRequest request, ServerCallContext context)

Returns configuration info about the Google Kubernetes Engine service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServerConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.GetServerConfigRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ServerConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.ServerConfig)` | The response to send back to the client (wrapped by a task).  
  
### ListClusters(ListClustersRequest, ServerCallContext)
    
    
    public virtual Task<ListClustersResponse> ListClusters(ListClustersRequest request, ServerCallContext context)

Lists all clusters owned by a project in either the specified zone or all zones.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.ListClustersRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.ListClustersResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListNodePools(ListNodePoolsRequest, ServerCallContext)
    
    
    public virtual Task<ListNodePoolsResponse> ListNodePools(ListNodePoolsRequest request, ServerCallContext context)

Lists the node pools for a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListNodePoolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.ListNodePoolsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListNodePoolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.ListNodePoolsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListOperations(ListOperationsRequest, ServerCallContext)
    
    
    public virtual Task<ListOperationsResponse> ListOperations(ListOperationsRequest request, ServerCallContext context)

Lists all operations in a project in a specific zone or all zones.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOperationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.ListOperationsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListOperationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.ListOperationsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListUsableSubnetworks(ListUsableSubnetworksRequest, ServerCallContext)
    
    
    public virtual Task<ListUsableSubnetworksResponse> ListUsableSubnetworks(ListUsableSubnetworksRequest request, ServerCallContext context)

Lists subnetworks that are usable for creating clusters in a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUsableSubnetworksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.ListUsableSubnetworksRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListUsableSubnetworksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.ListUsableSubnetworksResponse)` | The response to send back to the client (wrapped by a task).  
  
### RollbackNodePoolUpgrade(RollbackNodePoolUpgradeRequest, ServerCallContext)
    
    
    public virtual Task<Operation> RollbackNodePoolUpgrade(RollbackNodePoolUpgradeRequest request, ServerCallContext context)

Rolls back a previously Aborted or Failed NodePool upgrade. This makes no changes if the last upgrade successfully completed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RollbackNodePoolUpgradeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.RollbackNodePoolUpgradeRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### SetAddonsConfig(SetAddonsConfigRequest, ServerCallContext)
    
    
    public virtual Task<Operation> SetAddonsConfig(SetAddonsConfigRequest request, ServerCallContext context)

Sets the addons for a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetAddonsConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.SetAddonsConfigRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### SetLabels(SetLabelsRequest, ServerCallContext)
    
    
    public virtual Task<Operation> SetLabels(SetLabelsRequest request, ServerCallContext context)

Sets labels on a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetLabelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.SetLabelsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### SetLegacyAbac(SetLegacyAbacRequest, ServerCallContext)
    
    
    public virtual Task<Operation> SetLegacyAbac(SetLegacyAbacRequest request, ServerCallContext context)

Enables or disables the ABAC authorization mechanism on a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetLegacyAbacRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.SetLegacyAbacRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### SetLocations(SetLocationsRequest, ServerCallContext)
    
    
    [Obsolete]
    public virtual Task<Operation> SetLocations(SetLocationsRequest request, ServerCallContext context)

Sets the locations for a specific cluster. Deprecated. Use [projects.locations.clusters.update](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/update) instead.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetLocationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.SetLocationsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### SetLoggingService(SetLoggingServiceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> SetLoggingService(SetLoggingServiceRequest request, ServerCallContext context)

Sets the logging service for a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetLoggingServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.SetLoggingServiceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### SetMaintenancePolicy(SetMaintenancePolicyRequest, ServerCallContext)
    
    
    public virtual Task<Operation> SetMaintenancePolicy(SetMaintenancePolicyRequest request, ServerCallContext context)

Sets the maintenance policy for a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetMaintenancePolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.SetMaintenancePolicyRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### SetMasterAuth(SetMasterAuthRequest, ServerCallContext)
    
    
    public virtual Task<Operation> SetMasterAuth(SetMasterAuthRequest request, ServerCallContext context)

Sets master auth materials. Currently supports changing the admin password or a specific cluster, either via password generation or explicitly setting the password.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetMasterAuthRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.SetMasterAuthRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### SetMonitoringService(SetMonitoringServiceRequest, ServerCallContext)
    
    
    public virtual Task<Operation> SetMonitoringService(SetMonitoringServiceRequest request, ServerCallContext context)

Sets the monitoring service for a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetMonitoringServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.SetMonitoringServiceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### SetNetworkPolicy(SetNetworkPolicyRequest, ServerCallContext)
    
    
    public virtual Task<Operation> SetNetworkPolicy(SetNetworkPolicyRequest request, ServerCallContext context)

Enables or disables Network Policy for a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetNetworkPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.SetNetworkPolicyRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### SetNodePoolAutoscaling(SetNodePoolAutoscalingRequest, ServerCallContext)
    
    
    public virtual Task<Operation> SetNodePoolAutoscaling(SetNodePoolAutoscalingRequest request, ServerCallContext context)

Sets the autoscaling settings for the specified node pool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetNodePoolAutoscalingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.SetNodePoolAutoscalingRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### SetNodePoolManagement(SetNodePoolManagementRequest, ServerCallContext)
    
    
    public virtual Task<Operation> SetNodePoolManagement(SetNodePoolManagementRequest request, ServerCallContext context)

Sets the NodeManagement options for a node pool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetNodePoolManagementRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.SetNodePoolManagementRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### SetNodePoolSize(SetNodePoolSizeRequest, ServerCallContext)
    
    
    public virtual Task<Operation> SetNodePoolSize(SetNodePoolSizeRequest request, ServerCallContext context)

Sets the size for a specific node pool. The new size will be used for all replicas, including future replicas created by modifying [NodePool.locations][google.container.v1.NodePool.locations].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetNodePoolSizeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.SetNodePoolSizeRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### StartIPRotation(StartIPRotationRequest, ServerCallContext)
    
    
    public virtual Task<Operation> StartIPRotation(StartIPRotationRequest request, ServerCallContext context)

Starts master IP rotation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartIPRotationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.StartIPRotationRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### UpdateCluster(UpdateClusterRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateCluster(UpdateClusterRequest request, ServerCallContext context)

Updates the settings of a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.UpdateClusterRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### UpdateMaster(UpdateMasterRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateMaster(UpdateMasterRequest request, ServerCallContext context)

Updates the master for a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMasterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.UpdateMasterRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
### UpdateNodePool(UpdateNodePoolRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateNodePool(UpdateNodePoolRequest request, ServerCallContext context)

Updates the version and/or image type for the specified node pool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateNodePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.UpdateNodePoolRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.Operation)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-25 UTC."],[],[]] 
