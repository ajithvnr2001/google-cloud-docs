---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.clustercontroller-class
title: Class protos.google.cloud.dataproc.v1.ClusterController (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:03:37.698932+00:00
---

# Class protos.google.cloud.dataproc.v1.ClusterController (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.clustercontroller-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataproc.v1.ClusterController (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.8.0  6.7.0  6.6.0  5.13.0  5.12.0  5.10.0  5.9.0  5.7.0  5.5.0  5.4.0  4.5.0  4.3.1  4.1.1  3.2.0  3.1.0  3.0.0  2.5.0  2.4.4 

Represents a ClusterController

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dataproc.v1.ClusterController

## Package

[@google-cloud/dataproc](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ClusterController service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ClusterController;

Creates new ClusterController service using the specified rpc implementation.

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
`[ClusterController](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.clustercontroller-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createCluster(request, callback)
    
    
    public createCluster(request: google.cloud.dataproc.v1.ICreateClusterRequest, callback: google.cloud.dataproc.v1.ClusterController.CreateClusterCallback): void;

Calls CreateCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.icreateclusterrequest)`   
CreateClusterRequest message or plain object  
`callback` |  `[CreateClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCluster(request)
    
    
    public createCluster(request: google.cloud.dataproc.v1.ICreateClusterRequest): Promise<google.longrunning.Operation>;

Calls CreateCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.icreateclusterrequest)`   
CreateClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.longrunning.operation)>` | Promise  
  
### deleteCluster(request, callback)
    
    
    public deleteCluster(request: google.cloud.dataproc.v1.IDeleteClusterRequest, callback: google.cloud.dataproc.v1.ClusterController.DeleteClusterCallback): void;

Calls DeleteCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ideleteclusterrequest)`   
DeleteClusterRequest message or plain object  
`callback` |  `[DeleteClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCluster(request)
    
    
    public deleteCluster(request: google.cloud.dataproc.v1.IDeleteClusterRequest): Promise<google.longrunning.Operation>;

Calls DeleteCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ideleteclusterrequest)`   
DeleteClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.longrunning.operation)>` | Promise  
  
### diagnoseCluster(request, callback)
    
    
    public diagnoseCluster(request: google.cloud.dataproc.v1.IDiagnoseClusterRequest, callback: google.cloud.dataproc.v1.ClusterController.DiagnoseClusterCallback): void;

Calls DiagnoseCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDiagnoseClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.idiagnoseclusterrequest)`   
DiagnoseClusterRequest message or plain object  
`callback` |  `[DiagnoseClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### diagnoseCluster(request)
    
    
    public diagnoseCluster(request: google.cloud.dataproc.v1.IDiagnoseClusterRequest): Promise<google.longrunning.Operation>;

Calls DiagnoseCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDiagnoseClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.idiagnoseclusterrequest)`   
DiagnoseClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.longrunning.operation)>` | Promise  
  
### getCluster(request, callback)
    
    
    public getCluster(request: google.cloud.dataproc.v1.IGetClusterRequest, callback: google.cloud.dataproc.v1.ClusterController.GetClusterCallback): void;

Calls GetCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.igetclusterrequest)`   
GetClusterRequest message or plain object  
`callback` |  `[GetClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Cluster  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCluster(request)
    
    
    public getCluster(request: google.cloud.dataproc.v1.IGetClusterRequest): Promise<google.cloud.dataproc.v1.Cluster>;

Calls GetCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.igetclusterrequest)`   
GetClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataproc.v1.Cluster](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.cluster)>` | Promise  
  
### listClusters(request, callback)
    
    
    public listClusters(request: google.cloud.dataproc.v1.IListClustersRequest, callback: google.cloud.dataproc.v1.ClusterController.ListClustersCallback): void;

Calls ListClusters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ilistclustersrequest)`   
ListClustersRequest message or plain object  
`callback` |  `[ListClustersCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and ListClustersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listClusters(request)
    
    
    public listClusters(request: google.cloud.dataproc.v1.IListClustersRequest): Promise<google.cloud.dataproc.v1.ListClustersResponse>;

Calls ListClusters.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ilistclustersrequest)`   
ListClustersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataproc.v1.ListClustersResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.listclustersresponse)>` | Promise  
  
### startCluster(request, callback)
    
    
    public startCluster(request: google.cloud.dataproc.v1.IStartClusterRequest, callback: google.cloud.dataproc.v1.ClusterController.StartClusterCallback): void;

Calls StartCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStartClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.istartclusterrequest)`   
StartClusterRequest message or plain object  
`callback` |  `[StartClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### startCluster(request)
    
    
    public startCluster(request: google.cloud.dataproc.v1.IStartClusterRequest): Promise<google.longrunning.Operation>;

Calls StartCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IStartClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.istartclusterrequest)`   
StartClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.longrunning.operation)>` | Promise  
  
### stopCluster(request, callback)
    
    
    public stopCluster(request: google.cloud.dataproc.v1.IStopClusterRequest, callback: google.cloud.dataproc.v1.ClusterController.StopClusterCallback): void;

Calls StopCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStopClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.istopclusterrequest)`   
StopClusterRequest message or plain object  
`callback` |  `[StopClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### stopCluster(request)
    
    
    public stopCluster(request: google.cloud.dataproc.v1.IStopClusterRequest): Promise<google.longrunning.Operation>;

Calls StopCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IStopClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.istopclusterrequest)`   
StopClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.longrunning.operation)>` | Promise  
  
### updateCluster(request, callback)
    
    
    public updateCluster(request: google.cloud.dataproc.v1.IUpdateClusterRequest, callback: google.cloud.dataproc.v1.ClusterController.UpdateClusterCallback): void;

Calls UpdateCluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iupdateclusterrequest)`   
UpdateClusterRequest message or plain object  
`callback` |  `[UpdateClusterCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCluster(request)
    
    
    public updateCluster(request: google.cloud.dataproc.v1.IUpdateClusterRequest): Promise<google.longrunning.Operation>;

Calls UpdateCluster.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iupdateclusterrequest)`   
UpdateClusterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
