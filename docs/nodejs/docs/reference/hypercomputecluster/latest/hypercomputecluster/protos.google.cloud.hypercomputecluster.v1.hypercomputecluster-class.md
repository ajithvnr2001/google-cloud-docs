---
url: https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.hypercomputecluster-class
title: Class protos.google.cloud.hypercomputecluster.v1.HypercomputeCluster (0.5.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:58.297644+00:00
---

# Class protos.google.cloud.hypercomputecluster.v1.HypercomputeCluster (0.5.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.hypercomputecluster-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.hypercomputecluster.v1.HypercomputeCluster (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.2.0  0.1.0 

Represents a HypercomputeCluster

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.hypercomputecluster.v1.HypercomputeCluster

## Package

[@google-cloud/hypercomputecluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new HypercomputeCluster service.

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

### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): HypercomputeCluster;

Creates new HypercomputeCluster service using the specified rpc implementation.

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
`[HypercomputeCluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.hypercomputecluster-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createCluster(request, callback)
    
    
    public createCluster(request: google.cloud.hypercomputecluster.v1.ICreateClusterRequest, callback: google.cloud.hypercomputecluster.v1.HypercomputeCluster.CreateClusterCallback): void;

Calls CreateCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.icreateclusterrequest)`   
CreateClusterRequest message or plain object  
`callback` |  `[CreateClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCluster(request)
    
    
    public createCluster(request: google.cloud.hypercomputecluster.v1.ICreateClusterRequest): Promise<google.longrunning.Operation>;

Calls CreateCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.icreateclusterrequest)`   
CreateClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.operation)>` | Promise  
  
### deleteCluster(request, callback)
    
    
    public deleteCluster(request: google.cloud.hypercomputecluster.v1.IDeleteClusterRequest, callback: google.cloud.hypercomputecluster.v1.HypercomputeCluster.DeleteClusterCallback): void;

Calls DeleteCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.ideleteclusterrequest)`   
DeleteClusterRequest message or plain object  
`callback` |  `[DeleteClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCluster(request)
    
    
    public deleteCluster(request: google.cloud.hypercomputecluster.v1.IDeleteClusterRequest): Promise<google.longrunning.Operation>;

Calls DeleteCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.ideleteclusterrequest)`   
DeleteClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.operation)>` | Promise  
  
### getCluster(request, callback)
    
    
    public getCluster(request: google.cloud.hypercomputecluster.v1.IGetClusterRequest, callback: google.cloud.hypercomputecluster.v1.HypercomputeCluster.GetClusterCallback): void;

Calls GetCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.igetclusterrequest)`   
GetClusterRequest message or plain object  
`callback` |  `[GetClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)`   
Node-style callback called with the error, if any, and Cluster  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCluster(request)
    
    
    public getCluster(request: google.cloud.hypercomputecluster.v1.IGetClusterRequest): Promise<google.cloud.hypercomputecluster.v1.Cluster>;

Calls GetCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.igetclusterrequest)`   
GetClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.hypercomputecluster.v1.Cluster](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.cluster)>` | Promise  
  
### listClusters(request, callback)
    
    
    public listClusters(request: google.cloud.hypercomputecluster.v1.IListClustersRequest, callback: google.cloud.hypercomputecluster.v1.HypercomputeCluster.ListClustersCallback): void;

Calls ListClusters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.ilistclustersrequest)`   
ListClustersRequest message or plain object  
`callback` |  `[ListClustersCallback](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)`   
Node-style callback called with the error, if any, and ListClustersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listClusters(request)
    
    
    public listClusters(request: google.cloud.hypercomputecluster.v1.IListClustersRequest): Promise<google.cloud.hypercomputecluster.v1.ListClustersResponse>;

Calls ListClusters.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.ilistclustersrequest)`   
ListClustersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.hypercomputecluster.v1.ListClustersResponse](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.listclustersresponse)>` | Promise  
  
### updateCluster(request, callback)
    
    
    public updateCluster(request: google.cloud.hypercomputecluster.v1.IUpdateClusterRequest, callback: google.cloud.hypercomputecluster.v1.HypercomputeCluster.UpdateClusterCallback): void;

Calls UpdateCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.iupdateclusterrequest)`   
UpdateClusterRequest message or plain object  
`callback` |  `[UpdateClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCluster(request)
    
    
    public updateCluster(request: google.cloud.hypercomputecluster.v1.IUpdateClusterRequest): Promise<google.longrunning.Operation>;

Calls UpdateCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.cloud.hypercomputecluster.v1.iupdateclusterrequest)`   
UpdateClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/hypercomputecluster/latest/hypercomputecluster/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
