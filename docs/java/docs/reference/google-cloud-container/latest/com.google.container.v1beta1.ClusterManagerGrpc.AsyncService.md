---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterManagerGrpc.AsyncService
title: Interface ClusterManagerGrpc.AsyncService (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:49.143525+00:00
---

# Interface ClusterManagerGrpc.AsyncService (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterManagerGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ClusterManagerGrpc.AsyncService (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public static interface ClusterManagerGrpc.AsyncService

Google Kubernetes Engine Cluster Manager v1beta1

## Methods 

### cancelOperation(CancelOperationRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void cancelOperation(CancelOperationRequest request, StreamObserver<Empty> responseObserver)

Cancels the specified operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CancelOperationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### checkAutopilotCompatibility(CheckAutopilotCompatibilityRequest request, StreamObserver<CheckAutopilotCompatibilityResponse> responseObserver)
    
    
    public default void checkAutopilotCompatibility(CheckAutopilotCompatibilityRequest request, StreamObserver<CheckAutopilotCompatibilityResponse> responseObserver)

Checks the cluster compatibility with Autopilot mode, and returns a list of compatibility issues.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckAutopilotCompatibilityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CheckAutopilotCompatibilityRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CheckAutopilotCompatibilityResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CheckAutopilotCompatibilityResponse)>`  
  
  
### completeControlPlaneUpgrade(CompleteControlPlaneUpgradeRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void completeControlPlaneUpgrade(CompleteControlPlaneUpgradeRequest request, StreamObserver<Operation> responseObserver)

CompleteControlPlaneUpgrade completes the rollback-safe upgrade by performing the step two upgrade for a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CompleteControlPlaneUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CompleteControlPlaneUpgradeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### completeIPRotation(CompleteIPRotationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void completeIPRotation(CompleteIPRotationRequest request, StreamObserver<Operation> responseObserver)

Completes master IP rotation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CompleteIPRotationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CompleteIPRotationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### completeNodePoolUpgrade(CompleteNodePoolUpgradeRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void completeNodePoolUpgrade(CompleteNodePoolUpgradeRequest request, StreamObserver<Empty> responseObserver)

CompleteNodePoolUpgrade will signal an on-going node pool upgrade to complete.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CompleteNodePoolUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CompleteNodePoolUpgradeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### createCluster(CreateClusterRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createCluster(CreateClusterRequest request, StreamObserver<Operation> responseObserver)

Creates a cluster, consisting of the specified number and type of Google Compute Engine instances. By default, the cluster is created in the project's [default network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks). One firewall is added for the cluster. After cluster creation, the kubelet creates routes for each node to allow the containers on that node to communicate with all other instances in the cluster. Finally, an entry is added to the project's global metadata indicating which CIDR range the cluster is using.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CreateClusterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### createNodePool(CreateNodePoolRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createNodePool(CreateNodePoolRequest request, StreamObserver<Operation> responseObserver)

Creates a node pool for a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CreateNodePoolRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### deleteCluster(DeleteClusterRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteCluster(DeleteClusterRequest request, StreamObserver<Operation> responseObserver)

Deletes the cluster, including the Kubernetes endpoint and all worker nodes. Firewalls and routes that were configured during cluster creation are also deleted. Other Google Compute Engine resources that might be in use by the cluster, such as load balancer resources, are not deleted if they weren't present when the cluster was initially created.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DeleteClusterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### deleteNodePool(DeleteNodePoolRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteNodePool(DeleteNodePoolRequest request, StreamObserver<Operation> responseObserver)

Deletes a node pool from a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DeleteNodePoolRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### fetchClusterUpgradeInfo(FetchClusterUpgradeInfoRequest request, StreamObserver<ClusterUpgradeInfo> responseObserver)
    
    
    public default void fetchClusterUpgradeInfo(FetchClusterUpgradeInfoRequest request, StreamObserver<ClusterUpgradeInfo> responseObserver)

Fetch upgrade information of a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchClusterUpgradeInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.FetchClusterUpgradeInfoRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ClusterUpgradeInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpgradeInfo)>`  
  
  
### fetchNodePoolUpgradeInfo(FetchNodePoolUpgradeInfoRequest request, StreamObserver<NodePoolUpgradeInfo> responseObserver)
    
    
    public default void fetchNodePoolUpgradeInfo(FetchNodePoolUpgradeInfoRequest request, StreamObserver<NodePoolUpgradeInfo> responseObserver)

Fetch upgrade information of a specific node pool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchNodePoolUpgradeInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.FetchNodePoolUpgradeInfoRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[NodePoolUpgradeInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolUpgradeInfo)>`  
  
  
### getCluster(GetClusterRequest request, StreamObserver<Cluster> responseObserver)
    
    
    public default void getCluster(GetClusterRequest request, StreamObserver<Cluster> responseObserver)

Gets the details for a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GetClusterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Cluster)>`  
  
  
### getJSONWebKeys(GetJSONWebKeysRequest request, StreamObserver<GetJSONWebKeysResponse> responseObserver)
    
    
    public default void getJSONWebKeys(GetJSONWebKeysRequest request, StreamObserver<GetJSONWebKeysResponse> responseObserver)

Gets the public component of the cluster signing keys in JSON Web Key format.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetJSONWebKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GetJSONWebKeysRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[GetJSONWebKeysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GetJSONWebKeysResponse)>`  
  
  
### getNodePool(GetNodePoolRequest request, StreamObserver<NodePool> responseObserver)
    
    
    public default void getNodePool(GetNodePoolRequest request, StreamObserver<NodePool> responseObserver)

Retrieves the requested node pool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GetNodePoolRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[NodePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePool)>`  
  
  
### getOperation(GetOperationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void getOperation(GetOperationRequest request, StreamObserver<Operation> responseObserver)

Gets the specified operation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GetOperationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### getServerConfig(GetServerConfigRequest request, StreamObserver<ServerConfig> responseObserver)
    
    
    public default void getServerConfig(GetServerConfigRequest request, StreamObserver<ServerConfig> responseObserver)

Returns configuration info about the Google Kubernetes Engine service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServerConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GetServerConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ServerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ServerConfig)>`  
  
  
### listClusters(ListClustersRequest request, StreamObserver<ListClustersResponse> responseObserver)
    
    
    public default void listClusters(ListClustersRequest request, StreamObserver<ListClustersResponse> responseObserver)

Lists all clusters owned by a project in either the specified zone or all zones.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ListClustersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ListClustersResponse)>`  
  
  
### listLocations(ListLocationsRequest request, StreamObserver<ListLocationsResponse> responseObserver)
    
    
    public default void listLocations(ListLocationsRequest request, StreamObserver<ListLocationsResponse> responseObserver)

Fetches locations that offer Google Kubernetes Engine.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListLocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ListLocationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListLocationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ListLocationsResponse)>`  
  
  
### listNodePools(ListNodePoolsRequest request, StreamObserver<ListNodePoolsResponse> responseObserver)
    
    
    public default void listNodePools(ListNodePoolsRequest request, StreamObserver<ListNodePoolsResponse> responseObserver)

Lists the node pools for a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListNodePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ListNodePoolsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListNodePoolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ListNodePoolsResponse)>`  
  
  
### listOperations(ListOperationsRequest request, StreamObserver<ListOperationsResponse> responseObserver)
    
    
    public default void listOperations(ListOperationsRequest request, StreamObserver<ListOperationsResponse> responseObserver)

Lists all operations in a project in the specified zone or all zones.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ListOperationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListOperationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ListOperationsResponse)>`  
  
  
### listUsableSubnetworks(ListUsableSubnetworksRequest request, StreamObserver<ListUsableSubnetworksResponse> responseObserver)
    
    
    public default void listUsableSubnetworks(ListUsableSubnetworksRequest request, StreamObserver<ListUsableSubnetworksResponse> responseObserver)

Lists subnetworks that can be used for creating clusters in a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUsableSubnetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ListUsableSubnetworksRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListUsableSubnetworksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ListUsableSubnetworksResponse)>`  
  
  
### rollbackNodePoolUpgrade(RollbackNodePoolUpgradeRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void rollbackNodePoolUpgrade(RollbackNodePoolUpgradeRequest request, StreamObserver<Operation> responseObserver)

Rolls back a previously Aborted or Failed NodePool upgrade. This makes no changes if the last upgrade successfully completed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RollbackNodePoolUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.RollbackNodePoolUpgradeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### setAddonsConfig(SetAddonsConfigRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void setAddonsConfig(SetAddonsConfigRequest request, StreamObserver<Operation> responseObserver)

Sets the addons for a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetAddonsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SetAddonsConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### setLabels(SetLabelsRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void setLabels(SetLabelsRequest request, StreamObserver<Operation> responseObserver)

Sets labels on a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SetLabelsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### setLegacyAbac(SetLegacyAbacRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void setLegacyAbac(SetLegacyAbacRequest request, StreamObserver<Operation> responseObserver)

Enables or disables the ABAC authorization mechanism on a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetLegacyAbacRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SetLegacyAbacRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### setLocations(SetLocationsRequest request, StreamObserver<Operation> responseObserver) (deprecated)
    
    
    public default void setLocations(SetLocationsRequest request, StreamObserver<Operation> responseObserver)

Sets the locations for a specific cluster. Deprecated. Use [projects.locations.clusters.update](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/update) instead.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetLocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SetLocationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### setLoggingService(SetLoggingServiceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void setLoggingService(SetLoggingServiceRequest request, StreamObserver<Operation> responseObserver)

Sets the logging service for a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetLoggingServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SetLoggingServiceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### setMaintenancePolicy(SetMaintenancePolicyRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void setMaintenancePolicy(SetMaintenancePolicyRequest request, StreamObserver<Operation> responseObserver)

Sets the maintenance policy for a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetMaintenancePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SetMaintenancePolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### setMasterAuth(SetMasterAuthRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void setMasterAuth(SetMasterAuthRequest request, StreamObserver<Operation> responseObserver)

Sets master auth materials. Currently supports changing the admin password or a specific cluster, either via password generation or explicitly setting the password.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetMasterAuthRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SetMasterAuthRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### setMonitoringService(SetMonitoringServiceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void setMonitoringService(SetMonitoringServiceRequest request, StreamObserver<Operation> responseObserver)

Sets the monitoring service for a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetMonitoringServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SetMonitoringServiceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### setNetworkPolicy(SetNetworkPolicyRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void setNetworkPolicy(SetNetworkPolicyRequest request, StreamObserver<Operation> responseObserver)

Enables or disables Network Policy for a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SetNetworkPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### setNodePoolAutoscaling(SetNodePoolAutoscalingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void setNodePoolAutoscaling(SetNodePoolAutoscalingRequest request, StreamObserver<Operation> responseObserver)

Sets the autoscaling settings of a specific node pool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetNodePoolAutoscalingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SetNodePoolAutoscalingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### setNodePoolManagement(SetNodePoolManagementRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void setNodePoolManagement(SetNodePoolManagementRequest request, StreamObserver<Operation> responseObserver)

Sets the NodeManagement options for a node pool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetNodePoolManagementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SetNodePoolManagementRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### setNodePoolSize(SetNodePoolSizeRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void setNodePoolSize(SetNodePoolSizeRequest request, StreamObserver<Operation> responseObserver)

SetNodePoolSizeRequest sets the size of a node pool. The new size will be used for all replicas, including future replicas created by modifying NodePool.locations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetNodePoolSizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SetNodePoolSizeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### startIPRotation(StartIPRotationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void startIPRotation(StartIPRotationRequest request, StreamObserver<Operation> responseObserver)

Starts master IP rotation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartIPRotationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.StartIPRotationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### updateCluster(UpdateClusterRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateCluster(UpdateClusterRequest request, StreamObserver<Operation> responseObserver)

Updates the settings for a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.UpdateClusterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### updateMaster(UpdateMasterRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateMaster(UpdateMasterRequest request, StreamObserver<Operation> responseObserver)

Updates the master for a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMasterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.UpdateMasterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
### updateNodePool(UpdateNodePoolRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateNodePool(UpdateNodePoolRequest request, StreamObserver<Operation> responseObserver)

Updates the version and/or image type of a specific node pool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.UpdateNodePoolRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Operation)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
