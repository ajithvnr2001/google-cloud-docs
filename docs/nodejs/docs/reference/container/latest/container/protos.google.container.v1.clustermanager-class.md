---
url: https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.clustermanager-class
title: Class protos.google.container.v1.ClusterManager (7.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:37:35.429608+00:00
---

# Class protos.google.container.v1.ClusterManager (7.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.clustermanager-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.container.v1.ClusterManager (7.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.2.1 (latest)  7.1.0  6.8.0  6.7.0  6.1.0  5.19.0  5.17.0  5.15.1  5.14.0  5.10.0  5.9.0  5.8.0  5.6.0  5.5.0  5.4.1  5.1.0  4.11.0  4.10.0  4.9.0  4.7.1  4.4.0  4.3.0  4.2.0  4.1.3  3.0.0  2.6.0  2.5.0  2.4.4  2.3.2 

Represents a ClusterManager

## Inheritance

$protobuf.rpc.Service > protos.google.container.v1.ClusterManager

## Package

[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ClusterManager service.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
  
## Methods 

### cancelOperation(request, callback)
    
    
    public cancelOperation(request: google.container.v1.ICancelOperationRequest, callback: google.container.v1.ClusterManager.CancelOperationCallback): void;

Calls CancelOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.icanceloperationrequest)`   
CancelOperationRequest message or plain object  
`callback` |  `[CancelOperationCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelOperation(request)
    
    
    public cancelOperation(request: google.container.v1.ICancelOperationRequest): Promise<google.protobuf.Empty>;

Calls CancelOperation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.icanceloperationrequest)`   
CancelOperationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.protobuf.empty)>` | Promise  
  
### checkAutopilotCompatibility(request, callback)
    
    
    public checkAutopilotCompatibility(request: google.container.v1.ICheckAutopilotCompatibilityRequest, callback: google.container.v1.ClusterManager.CheckAutopilotCompatibilityCallback): void;

Calls CheckAutopilotCompatibility.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICheckAutopilotCompatibilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.icheckautopilotcompatibilityrequest)`   
CheckAutopilotCompatibilityRequest message or plain object  
`callback` |  `[CheckAutopilotCompatibilityCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and CheckAutopilotCompatibilityResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### checkAutopilotCompatibility(request)
    
    
    public checkAutopilotCompatibility(request: google.container.v1.ICheckAutopilotCompatibilityRequest): Promise<google.container.v1.CheckAutopilotCompatibilityResponse>;

Calls CheckAutopilotCompatibility.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICheckAutopilotCompatibilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.icheckautopilotcompatibilityrequest)`   
CheckAutopilotCompatibilityRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.CheckAutopilotCompatibilityResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.checkautopilotcompatibilityresponse)>` | Promise  
  
### completeControlPlaneUpgrade(request, callback)
    
    
    public completeControlPlaneUpgrade(request: google.container.v1.ICompleteControlPlaneUpgradeRequest, callback: google.container.v1.ClusterManager.CompleteControlPlaneUpgradeCallback): void;

Calls CompleteControlPlaneUpgrade.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICompleteControlPlaneUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.icompletecontrolplaneupgraderequest)`   
CompleteControlPlaneUpgradeRequest message or plain object  
`callback` |  `[CompleteControlPlaneUpgradeCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### completeControlPlaneUpgrade(request)
    
    
    public completeControlPlaneUpgrade(request: google.container.v1.ICompleteControlPlaneUpgradeRequest): Promise<google.container.v1.Operation>;

Calls CompleteControlPlaneUpgrade.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICompleteControlPlaneUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.icompletecontrolplaneupgraderequest)`   
CompleteControlPlaneUpgradeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### completeIPRotation(request, callback)
    
    
    public completeIPRotation(request: google.container.v1.ICompleteIPRotationRequest, callback: google.container.v1.ClusterManager.CompleteIPRotationCallback): void;

Calls CompleteIPRotation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICompleteIPRotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.icompleteiprotationrequest)`   
CompleteIPRotationRequest message or plain object  
`callback` |  `[CompleteIPRotationCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### completeIPRotation(request)
    
    
    public completeIPRotation(request: google.container.v1.ICompleteIPRotationRequest): Promise<google.container.v1.Operation>;

Calls CompleteIPRotation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICompleteIPRotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.icompleteiprotationrequest)`   
CompleteIPRotationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### completeNodePoolUpgrade(request, callback)
    
    
    public completeNodePoolUpgrade(request: google.container.v1.ICompleteNodePoolUpgradeRequest, callback: google.container.v1.ClusterManager.CompleteNodePoolUpgradeCallback): void;

Calls CompleteNodePoolUpgrade.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICompleteNodePoolUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.icompletenodepoolupgraderequest)`   
CompleteNodePoolUpgradeRequest message or plain object  
`callback` |  `[CompleteNodePoolUpgradeCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### completeNodePoolUpgrade(request)
    
    
    public completeNodePoolUpgrade(request: google.container.v1.ICompleteNodePoolUpgradeRequest): Promise<google.protobuf.Empty>;

Calls CompleteNodePoolUpgrade.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICompleteNodePoolUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.icompletenodepoolupgraderequest)`   
CompleteNodePoolUpgradeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.protobuf.empty)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ClusterManager;

Creates new ClusterManager service using the specified rpc implementation.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
**Returns**  
---  
**Type** | **Description**  
`[ClusterManager](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.clustermanager-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createCluster(request, callback)
    
    
    public createCluster(request: google.container.v1.ICreateClusterRequest, callback: google.container.v1.ClusterManager.CreateClusterCallback): void;

Calls CreateCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.icreateclusterrequest)`   
CreateClusterRequest message or plain object  
`callback` |  `[CreateClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCluster(request)
    
    
    public createCluster(request: google.container.v1.ICreateClusterRequest): Promise<google.container.v1.Operation>;

Calls CreateCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.icreateclusterrequest)`   
CreateClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### createNodePool(request, callback)
    
    
    public createNodePool(request: google.container.v1.ICreateNodePoolRequest, callback: google.container.v1.ClusterManager.CreateNodePoolCallback): void;

Calls CreateNodePool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.icreatenodepoolrequest)`   
CreateNodePoolRequest message or plain object  
`callback` |  `[CreateNodePoolCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createNodePool(request)
    
    
    public createNodePool(request: google.container.v1.ICreateNodePoolRequest): Promise<google.container.v1.Operation>;

Calls CreateNodePool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.icreatenodepoolrequest)`   
CreateNodePoolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### deleteCluster(request, callback)
    
    
    public deleteCluster(request: google.container.v1.IDeleteClusterRequest, callback: google.container.v1.ClusterManager.DeleteClusterCallback): void;

Calls DeleteCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.ideleteclusterrequest)`   
DeleteClusterRequest message or plain object  
`callback` |  `[DeleteClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCluster(request)
    
    
    public deleteCluster(request: google.container.v1.IDeleteClusterRequest): Promise<google.container.v1.Operation>;

Calls DeleteCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.ideleteclusterrequest)`   
DeleteClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### deleteNodePool(request, callback)
    
    
    public deleteNodePool(request: google.container.v1.IDeleteNodePoolRequest, callback: google.container.v1.ClusterManager.DeleteNodePoolCallback): void;

Calls DeleteNodePool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.ideletenodepoolrequest)`   
DeleteNodePoolRequest message or plain object  
`callback` |  `[DeleteNodePoolCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteNodePool(request)
    
    
    public deleteNodePool(request: google.container.v1.IDeleteNodePoolRequest): Promise<google.container.v1.Operation>;

Calls DeleteNodePool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.ideletenodepoolrequest)`   
DeleteNodePoolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### fetchClusterUpgradeInfo(request, callback)
    
    
    public fetchClusterUpgradeInfo(request: google.container.v1.IFetchClusterUpgradeInfoRequest, callback: google.container.v1.ClusterManager.FetchClusterUpgradeInfoCallback): void;

Calls FetchClusterUpgradeInfo.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchClusterUpgradeInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.ifetchclusterupgradeinforequest)`   
FetchClusterUpgradeInfoRequest message or plain object  
`callback` |  `[FetchClusterUpgradeInfoCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and ClusterUpgradeInfo  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchClusterUpgradeInfo(request)
    
    
    public fetchClusterUpgradeInfo(request: google.container.v1.IFetchClusterUpgradeInfoRequest): Promise<google.container.v1.ClusterUpgradeInfo>;

Calls FetchClusterUpgradeInfo.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchClusterUpgradeInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.ifetchclusterupgradeinforequest)`   
FetchClusterUpgradeInfoRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.ClusterUpgradeInfo](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.clusterupgradeinfo-class)>` | Promise  
  
### fetchNodePoolUpgradeInfo(request, callback)
    
    
    public fetchNodePoolUpgradeInfo(request: google.container.v1.IFetchNodePoolUpgradeInfoRequest, callback: google.container.v1.ClusterManager.FetchNodePoolUpgradeInfoCallback): void;

Calls FetchNodePoolUpgradeInfo.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchNodePoolUpgradeInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.ifetchnodepoolupgradeinforequest)`   
FetchNodePoolUpgradeInfoRequest message or plain object  
`callback` |  `[FetchNodePoolUpgradeInfoCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and NodePoolUpgradeInfo  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchNodePoolUpgradeInfo(request)
    
    
    public fetchNodePoolUpgradeInfo(request: google.container.v1.IFetchNodePoolUpgradeInfoRequest): Promise<google.container.v1.NodePoolUpgradeInfo>;

Calls FetchNodePoolUpgradeInfo.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchNodePoolUpgradeInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.ifetchnodepoolupgradeinforequest)`   
FetchNodePoolUpgradeInfoRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.NodePoolUpgradeInfo](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.nodepoolupgradeinfo-class)>` | Promise  
  
### getCluster(request, callback)
    
    
    public getCluster(request: google.container.v1.IGetClusterRequest, callback: google.container.v1.ClusterManager.GetClusterCallback): void;

Calls GetCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.igetclusterrequest)`   
GetClusterRequest message or plain object  
`callback` |  `[GetClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Cluster  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCluster(request)
    
    
    public getCluster(request: google.container.v1.IGetClusterRequest): Promise<google.container.v1.Cluster>;

Calls GetCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.igetclusterrequest)`   
GetClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Cluster](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.cluster-class)>` | Promise  
  
### getJSONWebKeys(request, callback)
    
    
    public getJSONWebKeys(request: google.container.v1.IGetJSONWebKeysRequest, callback: google.container.v1.ClusterManager.GetJSONWebKeysCallback): void;

Calls GetJSONWebKeys.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetJSONWebKeysRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.igetjsonwebkeysrequest)`   
GetJSONWebKeysRequest message or plain object  
`callback` |  `[GetJSONWebKeysCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and GetJSONWebKeysResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getJSONWebKeys(request)
    
    
    public getJSONWebKeys(request: google.container.v1.IGetJSONWebKeysRequest): Promise<google.container.v1.GetJSONWebKeysResponse>;

Calls GetJSONWebKeys.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetJSONWebKeysRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.igetjsonwebkeysrequest)`   
GetJSONWebKeysRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.GetJSONWebKeysResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.getjsonwebkeysresponse)>` | Promise  
  
### getNodePool(request, callback)
    
    
    public getNodePool(request: google.container.v1.IGetNodePoolRequest, callback: google.container.v1.ClusterManager.GetNodePoolCallback): void;

Calls GetNodePool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.igetnodepoolrequest)`   
GetNodePoolRequest message or plain object  
`callback` |  `[GetNodePoolCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and NodePool  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getNodePool(request)
    
    
    public getNodePool(request: google.container.v1.IGetNodePoolRequest): Promise<google.container.v1.NodePool>;

Calls GetNodePool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.igetnodepoolrequest)`   
GetNodePoolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.NodePool](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.nodepool-class)>` | Promise  
  
### getOperation(request, callback)
    
    
    public getOperation(request: google.container.v1.IGetOperationRequest, callback: google.container.v1.ClusterManager.GetOperationCallback): void;

Calls GetOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.igetoperationrequest)`   
GetOperationRequest message or plain object  
`callback` |  `[GetOperationCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getOperation(request)
    
    
    public getOperation(request: google.container.v1.IGetOperationRequest): Promise<google.container.v1.Operation>;

Calls GetOperation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.igetoperationrequest)`   
GetOperationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### getServerConfig(request, callback)
    
    
    public getServerConfig(request: google.container.v1.IGetServerConfigRequest, callback: google.container.v1.ClusterManager.GetServerConfigCallback): void;

Calls GetServerConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServerConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.igetserverconfigrequest)`   
GetServerConfigRequest message or plain object  
`callback` |  `[GetServerConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and ServerConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getServerConfig(request)
    
    
    public getServerConfig(request: google.container.v1.IGetServerConfigRequest): Promise<google.container.v1.ServerConfig>;

Calls GetServerConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetServerConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.igetserverconfigrequest)`   
GetServerConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.ServerConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.serverconfig-class)>` | Promise  
  
### listClusters(request, callback)
    
    
    public listClusters(request: google.container.v1.IListClustersRequest, callback: google.container.v1.ClusterManager.ListClustersCallback): void;

Calls ListClusters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.ilistclustersrequest)`   
ListClustersRequest message or plain object  
`callback` |  `[ListClustersCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and ListClustersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listClusters(request)
    
    
    public listClusters(request: google.container.v1.IListClustersRequest): Promise<google.container.v1.ListClustersResponse>;

Calls ListClusters.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.ilistclustersrequest)`   
ListClustersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.ListClustersResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.listclustersresponse)>` | Promise  
  
### listNodePools(request, callback)
    
    
    public listNodePools(request: google.container.v1.IListNodePoolsRequest, callback: google.container.v1.ClusterManager.ListNodePoolsCallback): void;

Calls ListNodePools.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListNodePoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.ilistnodepoolsrequest)`   
ListNodePoolsRequest message or plain object  
`callback` |  `[ListNodePoolsCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and ListNodePoolsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listNodePools(request)
    
    
    public listNodePools(request: google.container.v1.IListNodePoolsRequest): Promise<google.container.v1.ListNodePoolsResponse>;

Calls ListNodePools.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListNodePoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.ilistnodepoolsrequest)`   
ListNodePoolsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.ListNodePoolsResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.listnodepoolsresponse)>` | Promise  
  
### listOperations(request, callback)
    
    
    public listOperations(request: google.container.v1.IListOperationsRequest, callback: google.container.v1.ClusterManager.ListOperationsCallback): void;

Calls ListOperations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.ilistoperationsrequest)`   
ListOperationsRequest message or plain object  
`callback` |  `[ListOperationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and ListOperationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listOperations(request)
    
    
    public listOperations(request: google.container.v1.IListOperationsRequest): Promise<google.container.v1.ListOperationsResponse>;

Calls ListOperations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.ilistoperationsrequest)`   
ListOperationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.ListOperationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.listoperationsresponse)>` | Promise  
  
### listUsableSubnetworks(request, callback)
    
    
    public listUsableSubnetworks(request: google.container.v1.IListUsableSubnetworksRequest, callback: google.container.v1.ClusterManager.ListUsableSubnetworksCallback): void;

Calls ListUsableSubnetworks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUsableSubnetworksRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.ilistusablesubnetworksrequest)`   
ListUsableSubnetworksRequest message or plain object  
`callback` |  `[ListUsableSubnetworksCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and ListUsableSubnetworksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUsableSubnetworks(request)
    
    
    public listUsableSubnetworks(request: google.container.v1.IListUsableSubnetworksRequest): Promise<google.container.v1.ListUsableSubnetworksResponse>;

Calls ListUsableSubnetworks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListUsableSubnetworksRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.ilistusablesubnetworksrequest)`   
ListUsableSubnetworksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.ListUsableSubnetworksResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.listusablesubnetworksresponse)>` | Promise  
  
### rollbackNodePoolUpgrade(request, callback)
    
    
    public rollbackNodePoolUpgrade(request: google.container.v1.IRollbackNodePoolUpgradeRequest, callback: google.container.v1.ClusterManager.RollbackNodePoolUpgradeCallback): void;

Calls RollbackNodePoolUpgrade.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRollbackNodePoolUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.irollbacknodepoolupgraderequest)`   
RollbackNodePoolUpgradeRequest message or plain object  
`callback` |  `[RollbackNodePoolUpgradeCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### rollbackNodePoolUpgrade(request)
    
    
    public rollbackNodePoolUpgrade(request: google.container.v1.IRollbackNodePoolUpgradeRequest): Promise<google.container.v1.Operation>;

Calls RollbackNodePoolUpgrade.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRollbackNodePoolUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.irollbacknodepoolupgraderequest)`   
RollbackNodePoolUpgradeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### setAddonsConfig(request, callback)
    
    
    public setAddonsConfig(request: google.container.v1.ISetAddonsConfigRequest, callback: google.container.v1.ClusterManager.SetAddonsConfigCallback): void;

Calls SetAddonsConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetAddonsConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetaddonsconfigrequest)`   
SetAddonsConfigRequest message or plain object  
`callback` |  `[SetAddonsConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setAddonsConfig(request)
    
    
    public setAddonsConfig(request: google.container.v1.ISetAddonsConfigRequest): Promise<google.container.v1.Operation>;

Calls SetAddonsConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetAddonsConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetaddonsconfigrequest)`   
SetAddonsConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### setLabels(request, callback)
    
    
    public setLabels(request: google.container.v1.ISetLabelsRequest, callback: google.container.v1.ClusterManager.SetLabelsCallback): void;

Calls SetLabels.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLabelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetlabelsrequest)`   
SetLabelsRequest message or plain object  
`callback` |  `[SetLabelsCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setLabels(request)
    
    
    public setLabels(request: google.container.v1.ISetLabelsRequest): Promise<google.container.v1.Operation>;

Calls SetLabels.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetLabelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetlabelsrequest)`   
SetLabelsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### setLegacyAbac(request, callback)
    
    
    public setLegacyAbac(request: google.container.v1.ISetLegacyAbacRequest, callback: google.container.v1.ClusterManager.SetLegacyAbacCallback): void;

Calls SetLegacyAbac.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLegacyAbacRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetlegacyabacrequest)`   
SetLegacyAbacRequest message or plain object  
`callback` |  `[SetLegacyAbacCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setLegacyAbac(request)
    
    
    public setLegacyAbac(request: google.container.v1.ISetLegacyAbacRequest): Promise<google.container.v1.Operation>;

Calls SetLegacyAbac.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetLegacyAbacRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetlegacyabacrequest)`   
SetLegacyAbacRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### setLocations(request, callback)
    
    
    public setLocations(request: google.container.v1.ISetLocationsRequest, callback: google.container.v1.ClusterManager.SetLocationsCallback): void;

Calls SetLocations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetlocationsrequest)`   
SetLocationsRequest message or plain object  
`callback` |  `[SetLocationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setLocations(request)
    
    
    public setLocations(request: google.container.v1.ISetLocationsRequest): Promise<google.container.v1.Operation>;

Calls SetLocations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetLocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetlocationsrequest)`   
SetLocationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### setLoggingService(request, callback)
    
    
    public setLoggingService(request: google.container.v1.ISetLoggingServiceRequest, callback: google.container.v1.ClusterManager.SetLoggingServiceCallback): void;

Calls SetLoggingService.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLoggingServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetloggingservicerequest)`   
SetLoggingServiceRequest message or plain object  
`callback` |  `[SetLoggingServiceCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setLoggingService(request)
    
    
    public setLoggingService(request: google.container.v1.ISetLoggingServiceRequest): Promise<google.container.v1.Operation>;

Calls SetLoggingService.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetLoggingServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetloggingservicerequest)`   
SetLoggingServiceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### setMaintenancePolicy(request, callback)
    
    
    public setMaintenancePolicy(request: google.container.v1.ISetMaintenancePolicyRequest, callback: google.container.v1.ClusterManager.SetMaintenancePolicyCallback): void;

Calls SetMaintenancePolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetMaintenancePolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetmaintenancepolicyrequest)`   
SetMaintenancePolicyRequest message or plain object  
`callback` |  `[SetMaintenancePolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setMaintenancePolicy(request)
    
    
    public setMaintenancePolicy(request: google.container.v1.ISetMaintenancePolicyRequest): Promise<google.container.v1.Operation>;

Calls SetMaintenancePolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetMaintenancePolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetmaintenancepolicyrequest)`   
SetMaintenancePolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### setMasterAuth(request, callback)
    
    
    public setMasterAuth(request: google.container.v1.ISetMasterAuthRequest, callback: google.container.v1.ClusterManager.SetMasterAuthCallback): void;

Calls SetMasterAuth.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetMasterAuthRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetmasterauthrequest)`   
SetMasterAuthRequest message or plain object  
`callback` |  `[SetMasterAuthCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setMasterAuth(request)
    
    
    public setMasterAuth(request: google.container.v1.ISetMasterAuthRequest): Promise<google.container.v1.Operation>;

Calls SetMasterAuth.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetMasterAuthRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetmasterauthrequest)`   
SetMasterAuthRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### setMonitoringService(request, callback)
    
    
    public setMonitoringService(request: google.container.v1.ISetMonitoringServiceRequest, callback: google.container.v1.ClusterManager.SetMonitoringServiceCallback): void;

Calls SetMonitoringService.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetMonitoringServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetmonitoringservicerequest)`   
SetMonitoringServiceRequest message or plain object  
`callback` |  `[SetMonitoringServiceCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setMonitoringService(request)
    
    
    public setMonitoringService(request: google.container.v1.ISetMonitoringServiceRequest): Promise<google.container.v1.Operation>;

Calls SetMonitoringService.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetMonitoringServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetmonitoringservicerequest)`   
SetMonitoringServiceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### setNetworkPolicy(request, callback)
    
    
    public setNetworkPolicy(request: google.container.v1.ISetNetworkPolicyRequest, callback: google.container.v1.ClusterManager.SetNetworkPolicyCallback): void;

Calls SetNetworkPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetNetworkPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetnetworkpolicyrequest)`   
SetNetworkPolicyRequest message or plain object  
`callback` |  `[SetNetworkPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setNetworkPolicy(request)
    
    
    public setNetworkPolicy(request: google.container.v1.ISetNetworkPolicyRequest): Promise<google.container.v1.Operation>;

Calls SetNetworkPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetNetworkPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetnetworkpolicyrequest)`   
SetNetworkPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### setNodePoolAutoscaling(request, callback)
    
    
    public setNodePoolAutoscaling(request: google.container.v1.ISetNodePoolAutoscalingRequest, callback: google.container.v1.ClusterManager.SetNodePoolAutoscalingCallback): void;

Calls SetNodePoolAutoscaling.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetNodePoolAutoscalingRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetnodepoolautoscalingrequest)`   
SetNodePoolAutoscalingRequest message or plain object  
`callback` |  `[SetNodePoolAutoscalingCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setNodePoolAutoscaling(request)
    
    
    public setNodePoolAutoscaling(request: google.container.v1.ISetNodePoolAutoscalingRequest): Promise<google.container.v1.Operation>;

Calls SetNodePoolAutoscaling.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetNodePoolAutoscalingRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetnodepoolautoscalingrequest)`   
SetNodePoolAutoscalingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### setNodePoolManagement(request, callback)
    
    
    public setNodePoolManagement(request: google.container.v1.ISetNodePoolManagementRequest, callback: google.container.v1.ClusterManager.SetNodePoolManagementCallback): void;

Calls SetNodePoolManagement.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetNodePoolManagementRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetnodepoolmanagementrequest)`   
SetNodePoolManagementRequest message or plain object  
`callback` |  `[SetNodePoolManagementCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setNodePoolManagement(request)
    
    
    public setNodePoolManagement(request: google.container.v1.ISetNodePoolManagementRequest): Promise<google.container.v1.Operation>;

Calls SetNodePoolManagement.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetNodePoolManagementRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetnodepoolmanagementrequest)`   
SetNodePoolManagementRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### setNodePoolSize(request, callback)
    
    
    public setNodePoolSize(request: google.container.v1.ISetNodePoolSizeRequest, callback: google.container.v1.ClusterManager.SetNodePoolSizeCallback): void;

Calls SetNodePoolSize.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetNodePoolSizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetnodepoolsizerequest)`   
SetNodePoolSizeRequest message or plain object  
`callback` |  `[SetNodePoolSizeCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setNodePoolSize(request)
    
    
    public setNodePoolSize(request: google.container.v1.ISetNodePoolSizeRequest): Promise<google.container.v1.Operation>;

Calls SetNodePoolSize.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetNodePoolSizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.isetnodepoolsizerequest)`   
SetNodePoolSizeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### startIPRotation(request, callback)
    
    
    public startIPRotation(request: google.container.v1.IStartIPRotationRequest, callback: google.container.v1.ClusterManager.StartIPRotationCallback): void;

Calls StartIPRotation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStartIPRotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.istartiprotationrequest)`   
StartIPRotationRequest message or plain object  
`callback` |  `[StartIPRotationCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### startIPRotation(request)
    
    
    public startIPRotation(request: google.container.v1.IStartIPRotationRequest): Promise<google.container.v1.Operation>;

Calls StartIPRotation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IStartIPRotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.istartiprotationrequest)`   
StartIPRotationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### updateCluster(request, callback)
    
    
    public updateCluster(request: google.container.v1.IUpdateClusterRequest, callback: google.container.v1.ClusterManager.UpdateClusterCallback): void;

Calls UpdateCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.iupdateclusterrequest)`   
UpdateClusterRequest message or plain object  
`callback` |  `[UpdateClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCluster(request)
    
    
    public updateCluster(request: google.container.v1.IUpdateClusterRequest): Promise<google.container.v1.Operation>;

Calls UpdateCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.iupdateclusterrequest)`   
UpdateClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### updateMaster(request, callback)
    
    
    public updateMaster(request: google.container.v1.IUpdateMasterRequest, callback: google.container.v1.ClusterManager.UpdateMasterCallback): void;

Calls UpdateMaster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMasterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.iupdatemasterrequest)`   
UpdateMasterRequest message or plain object  
`callback` |  `[UpdateMasterCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMaster(request)
    
    
    public updateMaster(request: google.container.v1.IUpdateMasterRequest): Promise<google.container.v1.Operation>;

Calls UpdateMaster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMasterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.iupdatemasterrequest)`   
UpdateMasterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
### updateNodePool(request, callback)
    
    
    public updateNodePool(request: google.container.v1.IUpdateNodePoolRequest, callback: google.container.v1.ClusterManager.UpdateNodePoolCallback): void;

Calls UpdateNodePool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.iupdatenodepoolrequest)`   
UpdateNodePoolRequest message or plain object  
`callback` |  `[UpdateNodePoolCallback](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateNodePool(request)
    
    
    public updateNodePool(request: google.container.v1.IUpdateNodePoolRequest): Promise<google.container.v1.Operation>;

Calls UpdateNodePool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.iupdatenodepoolrequest)`   
UpdateNodePoolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.container.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.operation-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
