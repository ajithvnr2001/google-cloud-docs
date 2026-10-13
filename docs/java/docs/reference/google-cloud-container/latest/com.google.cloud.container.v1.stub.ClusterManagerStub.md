---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.stub.ClusterManagerStub
title: Class ClusterManagerStub (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:41:51.385277+00:00
---

# Class ClusterManagerStub (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.stub.ClusterManagerStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ClusterManagerStub (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public abstract class ClusterManagerStub implements BackgroundResource

Base stub class for the ClusterManager service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ClusterManagerStub

## Implements

[BackgroundResource](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.BackgroundResource.html)

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Constructors 

### ClusterManagerStub()
    
    
    public ClusterManagerStub()

## Methods 

### cancelOperationCallable()
    
    
    public UnaryCallable<CancelOperationRequest,Empty> cancelOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CancelOperationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### checkAutopilotCompatibilityCallable()
    
    
    public UnaryCallable<CheckAutopilotCompatibilityRequest,CheckAutopilotCompatibilityResponse> checkAutopilotCompatibilityCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CheckAutopilotCompatibilityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CheckAutopilotCompatibilityRequest),[CheckAutopilotCompatibilityResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CheckAutopilotCompatibilityResponse)>` |   
  
### close()
    
    
    public abstract void close()

### completeControlPlaneUpgradeCallable()
    
    
    public UnaryCallable<CompleteControlPlaneUpgradeRequest,Operation> completeControlPlaneUpgradeCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CompleteControlPlaneUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CompleteControlPlaneUpgradeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### completeIPRotationCallable()
    
    
    public UnaryCallable<CompleteIPRotationRequest,Operation> completeIPRotationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CompleteIPRotationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CompleteIPRotationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### completeNodePoolUpgradeCallable()
    
    
    public UnaryCallable<CompleteNodePoolUpgradeRequest,Empty> completeNodePoolUpgradeCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CompleteNodePoolUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CompleteNodePoolUpgradeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### createClusterCallable()
    
    
    public UnaryCallable<CreateClusterRequest,Operation> createClusterCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CreateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### createNodePoolCallable()
    
    
    public UnaryCallable<CreateNodePoolRequest,Operation> createNodePoolCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CreateNodePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### deleteClusterCallable()
    
    
    public UnaryCallable<DeleteClusterRequest,Operation> deleteClusterCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DeleteClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### deleteNodePoolCallable()
    
    
    public UnaryCallable<DeleteNodePoolRequest,Operation> deleteNodePoolCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DeleteNodePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### fetchClusterUpgradeInfoCallable()
    
    
    public UnaryCallable<FetchClusterUpgradeInfoRequest,ClusterUpgradeInfo> fetchClusterUpgradeInfoCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchClusterUpgradeInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.FetchClusterUpgradeInfoRequest),[ClusterUpgradeInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterUpgradeInfo)>` |   
  
### fetchNodePoolUpgradeInfoCallable()
    
    
    public UnaryCallable<FetchNodePoolUpgradeInfoRequest,NodePoolUpgradeInfo> fetchNodePoolUpgradeInfoCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchNodePoolUpgradeInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.FetchNodePoolUpgradeInfoRequest),[NodePoolUpgradeInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePoolUpgradeInfo)>` |   
  
### getClusterCallable()
    
    
    public UnaryCallable<GetClusterRequest,Cluster> getClusterCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Cluster)>` |   
  
### getJSONWebKeysCallable()
    
    
    public UnaryCallable<GetJSONWebKeysRequest,GetJSONWebKeysResponse> getJSONWebKeysCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetJSONWebKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetJSONWebKeysRequest),[GetJSONWebKeysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetJSONWebKeysResponse)>` |   
  
### getNodePoolCallable()
    
    
    public UnaryCallable<GetNodePoolRequest,NodePool> getNodePoolCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetNodePoolRequest),[NodePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePool)>` |   
  
### getOperationCallable()
    
    
    public UnaryCallable<GetOperationRequest,Operation> getOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetOperationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getServerConfigCallable()
    
    
    public UnaryCallable<GetServerConfigRequest,ServerConfig> getServerConfigCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetServerConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetServerConfigRequest),[ServerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ServerConfig)>` |   
  
### listClustersCallable()
    
    
    public UnaryCallable<ListClustersRequest,ListClustersResponse> listClustersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListClustersRequest),[ListClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListClustersResponse)>` |   
  
### listNodePoolsCallable()
    
    
    public UnaryCallable<ListNodePoolsRequest,ListNodePoolsResponse> listNodePoolsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNodePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListNodePoolsRequest),[ListNodePoolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListNodePoolsResponse)>` |   
  
### listOperationsCallable()
    
    
    public UnaryCallable<ListOperationsRequest,ListOperationsResponse> listOperationsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListOperationsRequest),[ListOperationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListOperationsResponse)>` |   
  
### listUsableSubnetworksCallable()
    
    
    public UnaryCallable<ListUsableSubnetworksRequest,ListUsableSubnetworksResponse> listUsableSubnetworksCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUsableSubnetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListUsableSubnetworksRequest),[ListUsableSubnetworksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListUsableSubnetworksResponse)>` |   
  
### listUsableSubnetworksPagedCallable()
    
    
    public UnaryCallable<ListUsableSubnetworksRequest,ClusterManagerClient.ListUsableSubnetworksPagedResponse> listUsableSubnetworksPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUsableSubnetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListUsableSubnetworksRequest),[ListUsableSubnetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.ClusterManagerClient.ListUsableSubnetworksPagedResponse)>` |   
  
### rollbackNodePoolUpgradeCallable()
    
    
    public UnaryCallable<RollbackNodePoolUpgradeRequest,Operation> rollbackNodePoolUpgradeCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RollbackNodePoolUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.RollbackNodePoolUpgradeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setAddonsConfigCallable()
    
    
    public UnaryCallable<SetAddonsConfigRequest,Operation> setAddonsConfigCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetAddonsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetAddonsConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setLabelsCallable()
    
    
    public UnaryCallable<SetLabelsRequest,Operation> setLabelsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetLabelsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setLegacyAbacCallable()
    
    
    public UnaryCallable<SetLegacyAbacRequest,Operation> setLegacyAbacCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetLegacyAbacRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetLegacyAbacRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setLocationsCallable() (deprecated)
    
    
    public UnaryCallable<SetLocationsRequest,Operation> setLocationsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetLocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetLocationsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setLoggingServiceCallable()
    
    
    public UnaryCallable<SetLoggingServiceRequest,Operation> setLoggingServiceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetLoggingServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetLoggingServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setMaintenancePolicyCallable()
    
    
    public UnaryCallable<SetMaintenancePolicyRequest,Operation> setMaintenancePolicyCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetMaintenancePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetMaintenancePolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setMasterAuthCallable()
    
    
    public UnaryCallable<SetMasterAuthRequest,Operation> setMasterAuthCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetMasterAuthRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetMasterAuthRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setMonitoringServiceCallable()
    
    
    public UnaryCallable<SetMonitoringServiceRequest,Operation> setMonitoringServiceCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetMonitoringServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetMonitoringServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setNetworkPolicyCallable()
    
    
    public UnaryCallable<SetNetworkPolicyRequest,Operation> setNetworkPolicyCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetNetworkPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setNodePoolAutoscalingCallable()
    
    
    public UnaryCallable<SetNodePoolAutoscalingRequest,Operation> setNodePoolAutoscalingCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetNodePoolAutoscalingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetNodePoolAutoscalingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setNodePoolManagementCallable()
    
    
    public UnaryCallable<SetNodePoolManagementRequest,Operation> setNodePoolManagementCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetNodePoolManagementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetNodePoolManagementRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setNodePoolSizeCallable()
    
    
    public UnaryCallable<SetNodePoolSizeRequest,Operation> setNodePoolSizeCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetNodePoolSizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetNodePoolSizeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### startIPRotationCallable()
    
    
    public UnaryCallable<StartIPRotationRequest,Operation> startIPRotationCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StartIPRotationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.StartIPRotationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### updateClusterCallable()
    
    
    public UnaryCallable<UpdateClusterRequest,Operation> updateClusterCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UpdateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### updateMasterCallable()
    
    
    public UnaryCallable<UpdateMasterRequest,Operation> updateMasterCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateMasterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UpdateMasterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### updateNodePoolCallable()
    
    
    public UnaryCallable<UpdateNodePoolRequest,Operation> updateNodePoolCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UpdateNodePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
