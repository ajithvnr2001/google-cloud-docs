---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.EdgeContainerGrpc.AsyncService
title: Interface EdgeContainerGrpc.AsyncService (0.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:23.994182+00:00
---

# Interface EdgeContainerGrpc.AsyncService (0.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.EdgeContainerGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface EdgeContainerGrpc.AsyncService (0.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.96.0 (latest)  0.92.0  0.91.0  0.90.0  0.88.0  0.85.0  0.84.0  0.82.0  0.80.0  0.79.0  0.78.0  0.77.0  0.75.0  0.73.0  0.72.0  0.71.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.61.0  0.60.0  0.59.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface EdgeContainerGrpc.AsyncService

EdgeContainer API provides management of Kubernetes Clusters on Google Edge Cloud deployments.

## Methods 

### createCluster(CreateClusterRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createCluster(CreateClusterRequest request, StreamObserver<Operation> responseObserver)

Creates a new Cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.CreateClusterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createNodePool(CreateNodePoolRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createNodePool(CreateNodePoolRequest request, StreamObserver<Operation> responseObserver)

Creates a new NodePool in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.CreateNodePoolRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createVpnConnection(CreateVpnConnectionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createVpnConnection(CreateVpnConnectionRequest request, StreamObserver<Operation> responseObserver)

Creates a new VPN connection in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateVpnConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.CreateVpnConnectionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteCluster(DeleteClusterRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteCluster(DeleteClusterRequest request, StreamObserver<Operation> responseObserver)

Deletes a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.DeleteClusterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteNodePool(DeleteNodePoolRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteNodePool(DeleteNodePoolRequest request, StreamObserver<Operation> responseObserver)

Deletes a single NodePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.DeleteNodePoolRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteVpnConnection(DeleteVpnConnectionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteVpnConnection(DeleteVpnConnectionRequest request, StreamObserver<Operation> responseObserver)

Deletes a single VPN connection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteVpnConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.DeleteVpnConnectionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### generateAccessToken(GenerateAccessTokenRequest request, StreamObserver<GenerateAccessTokenResponse> responseObserver)
    
    
    public default void generateAccessToken(GenerateAccessTokenRequest request, StreamObserver<GenerateAccessTokenResponse> responseObserver)

Generates an access token for a Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateAccessTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.GenerateAccessTokenRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[GenerateAccessTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.GenerateAccessTokenResponse)>`  
  
  
### generateOfflineCredential(GenerateOfflineCredentialRequest request, StreamObserver<GenerateOfflineCredentialResponse> responseObserver)
    
    
    public default void generateOfflineCredential(GenerateOfflineCredentialRequest request, StreamObserver<GenerateOfflineCredentialResponse> responseObserver)

Generates an offline credential for a Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateOfflineCredentialRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.GenerateOfflineCredentialRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[GenerateOfflineCredentialResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.GenerateOfflineCredentialResponse)>`  
  
  
### getCluster(GetClusterRequest request, StreamObserver<Cluster> responseObserver)
    
    
    public default void getCluster(GetClusterRequest request, StreamObserver<Cluster> responseObserver)

Gets details of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.GetClusterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.Cluster)>`  
  
  
### getMachine(GetMachineRequest request, StreamObserver<Machine> responseObserver)
    
    
    public default void getMachine(GetMachineRequest request, StreamObserver<Machine> responseObserver)

Gets details of a single Machine.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMachineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.GetMachineRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Machine](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.Machine)>`  
  
  
### getNodePool(GetNodePoolRequest request, StreamObserver<NodePool> responseObserver)
    
    
    public default void getNodePool(GetNodePoolRequest request, StreamObserver<NodePool> responseObserver)

Gets details of a single NodePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.GetNodePoolRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[NodePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.NodePool)>`  
  
  
### getServerConfig(GetServerConfigRequest request, StreamObserver<ServerConfig> responseObserver)
    
    
    public default void getServerConfig(GetServerConfigRequest request, StreamObserver<ServerConfig> responseObserver)

Gets the server config.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServerConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.GetServerConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ServerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.ServerConfig)>`  
  
  
### getVpnConnection(GetVpnConnectionRequest request, StreamObserver<VpnConnection> responseObserver)
    
    
    public default void getVpnConnection(GetVpnConnectionRequest request, StreamObserver<VpnConnection> responseObserver)

Gets details of a single VPN connection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetVpnConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.GetVpnConnectionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[VpnConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.VpnConnection)>`  
  
  
### listClusters(ListClustersRequest request, StreamObserver<ListClustersResponse> responseObserver)
    
    
    public default void listClusters(ListClustersRequest request, StreamObserver<ListClustersResponse> responseObserver)

Lists Clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.ListClustersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.ListClustersResponse)>`  
  
  
### listMachines(ListMachinesRequest request, StreamObserver<ListMachinesResponse> responseObserver)
    
    
    public default void listMachines(ListMachinesRequest request, StreamObserver<ListMachinesResponse> responseObserver)

Lists Machines in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMachinesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.ListMachinesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListMachinesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.ListMachinesResponse)>`  
  
  
### listNodePools(ListNodePoolsRequest request, StreamObserver<ListNodePoolsResponse> responseObserver)
    
    
    public default void listNodePools(ListNodePoolsRequest request, StreamObserver<ListNodePoolsResponse> responseObserver)

Lists NodePools in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListNodePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.ListNodePoolsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListNodePoolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.ListNodePoolsResponse)>`  
  
  
### listVpnConnections(ListVpnConnectionsRequest request, StreamObserver<ListVpnConnectionsResponse> responseObserver)
    
    
    public default void listVpnConnections(ListVpnConnectionsRequest request, StreamObserver<ListVpnConnectionsResponse> responseObserver)

Lists VPN connections in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListVpnConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.ListVpnConnectionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListVpnConnectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.ListVpnConnectionsResponse)>`  
  
  
### updateCluster(UpdateClusterRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateCluster(UpdateClusterRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single Cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.UpdateClusterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateNodePool(UpdateNodePoolRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateNodePool(UpdateNodePoolRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single NodePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.UpdateNodePoolRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### upgradeCluster(UpgradeClusterRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void upgradeCluster(UpgradeClusterRequest request, StreamObserver<Operation> responseObserver)

Upgrades a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpgradeClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-distributedcloudedge/latest/com.google.cloud.edgecontainer.v1.UpgradeClusterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
