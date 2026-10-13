---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterManagerGrpc
title: Class ClusterManagerGrpc (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:25:06.938802+00:00
---

# Class ClusterManagerGrpc (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterManagerGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ClusterManagerGrpc (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public final class ClusterManagerGrpc

Google Kubernetes Engine Cluster Manager v1

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ClusterManagerGrpc

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

## Static Fields 

### SERVICE_NAME
    
    
    public static final String SERVICE_NAME

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### bindService(ClusterManagerGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(ClusterManagerGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[ClusterManagerGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterManagerGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getCancelOperationMethod()
    
    
    public static MethodDescriptor<CancelOperationRequest,Empty> getCancelOperationMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CancelOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CancelOperationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getCheckAutopilotCompatibilityMethod()
    
    
    public static MethodDescriptor<CheckAutopilotCompatibilityRequest,CheckAutopilotCompatibilityResponse> getCheckAutopilotCompatibilityMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CheckAutopilotCompatibilityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CheckAutopilotCompatibilityRequest),[CheckAutopilotCompatibilityResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CheckAutopilotCompatibilityResponse)>` |   
  
### getCompleteControlPlaneUpgradeMethod()
    
    
    public static MethodDescriptor<CompleteControlPlaneUpgradeRequest,Operation> getCompleteControlPlaneUpgradeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CompleteControlPlaneUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CompleteControlPlaneUpgradeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getCompleteIPRotationMethod()
    
    
    public static MethodDescriptor<CompleteIPRotationRequest,Operation> getCompleteIPRotationMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CompleteIPRotationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CompleteIPRotationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getCompleteNodePoolUpgradeMethod()
    
    
    public static MethodDescriptor<CompleteNodePoolUpgradeRequest,Empty> getCompleteNodePoolUpgradeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CompleteNodePoolUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CompleteNodePoolUpgradeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getCreateClusterMethod()
    
    
    public static MethodDescriptor<CreateClusterRequest,Operation> getCreateClusterMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CreateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getCreateNodePoolMethod()
    
    
    public static MethodDescriptor<CreateNodePoolRequest,Operation> getCreateNodePoolMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CreateNodePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getDeleteClusterMethod()
    
    
    public static MethodDescriptor<DeleteClusterRequest,Operation> getDeleteClusterMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DeleteClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getDeleteNodePoolMethod()
    
    
    public static MethodDescriptor<DeleteNodePoolRequest,Operation> getDeleteNodePoolMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DeleteNodePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getFetchClusterUpgradeInfoMethod()
    
    
    public static MethodDescriptor<FetchClusterUpgradeInfoRequest,ClusterUpgradeInfo> getFetchClusterUpgradeInfoMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[FetchClusterUpgradeInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.FetchClusterUpgradeInfoRequest),[ClusterUpgradeInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterUpgradeInfo)>` |   
  
### getFetchNodePoolUpgradeInfoMethod()
    
    
    public static MethodDescriptor<FetchNodePoolUpgradeInfoRequest,NodePoolUpgradeInfo> getFetchNodePoolUpgradeInfoMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[FetchNodePoolUpgradeInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.FetchNodePoolUpgradeInfoRequest),[NodePoolUpgradeInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePoolUpgradeInfo)>` |   
  
### getGetClusterMethod()
    
    
    public static MethodDescriptor<GetClusterRequest,Cluster> getGetClusterMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Cluster)>` |   
  
### getGetJSONWebKeysMethod()
    
    
    public static MethodDescriptor<GetJSONWebKeysRequest,GetJSONWebKeysResponse> getGetJSONWebKeysMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetJSONWebKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetJSONWebKeysRequest),[GetJSONWebKeysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetJSONWebKeysResponse)>` |   
  
### getGetNodePoolMethod()
    
    
    public static MethodDescriptor<GetNodePoolRequest,NodePool> getGetNodePoolMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetNodePoolRequest),[NodePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePool)>` |   
  
### getGetOperationMethod()
    
    
    public static MethodDescriptor<GetOperationRequest,Operation> getGetOperationMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetOperationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getGetServerConfigMethod()
    
    
    public static MethodDescriptor<GetServerConfigRequest,ServerConfig> getGetServerConfigMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetServerConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetServerConfigRequest),[ServerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ServerConfig)>` |   
  
### getListClustersMethod()
    
    
    public static MethodDescriptor<ListClustersRequest,ListClustersResponse> getListClustersMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListClustersRequest),[ListClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListClustersResponse)>` |   
  
### getListNodePoolsMethod()
    
    
    public static MethodDescriptor<ListNodePoolsRequest,ListNodePoolsResponse> getListNodePoolsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListNodePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListNodePoolsRequest),[ListNodePoolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListNodePoolsResponse)>` |   
  
### getListOperationsMethod()
    
    
    public static MethodDescriptor<ListOperationsRequest,ListOperationsResponse> getListOperationsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListOperationsRequest),[ListOperationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListOperationsResponse)>` |   
  
### getListUsableSubnetworksMethod()
    
    
    public static MethodDescriptor<ListUsableSubnetworksRequest,ListUsableSubnetworksResponse> getListUsableSubnetworksMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListUsableSubnetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListUsableSubnetworksRequest),[ListUsableSubnetworksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListUsableSubnetworksResponse)>` |   
  
### getRollbackNodePoolUpgradeMethod()
    
    
    public static MethodDescriptor<RollbackNodePoolUpgradeRequest,Operation> getRollbackNodePoolUpgradeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[RollbackNodePoolUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.RollbackNodePoolUpgradeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getSetAddonsConfigMethod()
    
    
    public static MethodDescriptor<SetAddonsConfigRequest,Operation> getSetAddonsConfigMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SetAddonsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetAddonsConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getSetLabelsMethod()
    
    
    public static MethodDescriptor<SetLabelsRequest,Operation> getSetLabelsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SetLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetLabelsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getSetLegacyAbacMethod()
    
    
    public static MethodDescriptor<SetLegacyAbacRequest,Operation> getSetLegacyAbacMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SetLegacyAbacRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetLegacyAbacRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getSetLocationsMethod()
    
    
    public static MethodDescriptor<SetLocationsRequest,Operation> getSetLocationsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SetLocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetLocationsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getSetLoggingServiceMethod()
    
    
    public static MethodDescriptor<SetLoggingServiceRequest,Operation> getSetLoggingServiceMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SetLoggingServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetLoggingServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getSetMaintenancePolicyMethod()
    
    
    public static MethodDescriptor<SetMaintenancePolicyRequest,Operation> getSetMaintenancePolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SetMaintenancePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetMaintenancePolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getSetMasterAuthMethod()
    
    
    public static MethodDescriptor<SetMasterAuthRequest,Operation> getSetMasterAuthMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SetMasterAuthRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetMasterAuthRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getSetMonitoringServiceMethod()
    
    
    public static MethodDescriptor<SetMonitoringServiceRequest,Operation> getSetMonitoringServiceMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SetMonitoringServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetMonitoringServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getSetNetworkPolicyMethod()
    
    
    public static MethodDescriptor<SetNetworkPolicyRequest,Operation> getSetNetworkPolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SetNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetNetworkPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getSetNodePoolAutoscalingMethod()
    
    
    public static MethodDescriptor<SetNodePoolAutoscalingRequest,Operation> getSetNodePoolAutoscalingMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SetNodePoolAutoscalingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetNodePoolAutoscalingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getSetNodePoolManagementMethod()
    
    
    public static MethodDescriptor<SetNodePoolManagementRequest,Operation> getSetNodePoolManagementMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SetNodePoolManagementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetNodePoolManagementRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getSetNodePoolSizeMethod()
    
    
    public static MethodDescriptor<SetNodePoolSizeRequest,Operation> getSetNodePoolSizeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SetNodePoolSizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetNodePoolSizeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getStartIPRotationMethod()
    
    
    public static MethodDescriptor<StartIPRotationRequest,Operation> getStartIPRotationMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[StartIPRotationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.StartIPRotationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getUpdateClusterMethod()
    
    
    public static MethodDescriptor<UpdateClusterRequest,Operation> getUpdateClusterMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UpdateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getUpdateMasterMethod()
    
    
    public static MethodDescriptor<UpdateMasterRequest,Operation> getUpdateMasterMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateMasterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UpdateMasterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getUpdateNodePoolMethod()
    
    
    public static MethodDescriptor<UpdateNodePoolRequest,Operation> getUpdateNodePoolMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UpdateNodePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static ClusterManagerGrpc.ClusterManagerBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterManagerGrpc.ClusterManagerBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterManagerGrpc.ClusterManagerBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static ClusterManagerGrpc.ClusterManagerBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterManagerGrpc.ClusterManagerBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterManagerGrpc.ClusterManagerBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static ClusterManagerGrpc.ClusterManagerFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterManagerGrpc.ClusterManagerFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterManagerGrpc.ClusterManagerFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static ClusterManagerGrpc.ClusterManagerStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterManagerGrpc.ClusterManagerStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterManagerGrpc.ClusterManagerStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
