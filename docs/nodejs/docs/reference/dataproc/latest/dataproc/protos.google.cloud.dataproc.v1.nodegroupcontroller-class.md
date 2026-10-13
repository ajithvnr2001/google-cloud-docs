---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.nodegroupcontroller-class
title: Class protos.google.cloud.dataproc.v1.NodeGroupController (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:03:55.794608+00:00
---

# Class protos.google.cloud.dataproc.v1.NodeGroupController (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.nodegroupcontroller-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataproc.v1.NodeGroupController (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.8.0  6.7.0  6.6.0  5.13.0  5.12.0  5.10.0  5.9.0  5.7.0  5.5.0  5.4.0  4.5.0  4.3.1  4.1.1  3.2.0  3.1.0  3.0.0  2.5.0  2.4.4 

Represents a NodeGroupController

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dataproc.v1.NodeGroupController

## Package

[@google-cloud/dataproc](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new NodeGroupController service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): NodeGroupController;

Creates new NodeGroupController service using the specified rpc implementation.

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
`[NodeGroupController](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.nodegroupcontroller-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createNodeGroup(request, callback)
    
    
    public createNodeGroup(request: google.cloud.dataproc.v1.ICreateNodeGroupRequest, callback: google.cloud.dataproc.v1.NodeGroupController.CreateNodeGroupCallback): void;

Calls CreateNodeGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.icreatenodegrouprequest)`   
CreateNodeGroupRequest message or plain object  
`callback` |  `[CreateNodeGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createNodeGroup(request)
    
    
    public createNodeGroup(request: google.cloud.dataproc.v1.ICreateNodeGroupRequest): Promise<google.longrunning.Operation>;

Calls CreateNodeGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.icreatenodegrouprequest)`   
CreateNodeGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.longrunning.operation)>` | Promise  
  
### getNodeGroup(request, callback)
    
    
    public getNodeGroup(request: google.cloud.dataproc.v1.IGetNodeGroupRequest, callback: google.cloud.dataproc.v1.NodeGroupController.GetNodeGroupCallback): void;

Calls GetNodeGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.igetnodegrouprequest)`   
GetNodeGroupRequest message or plain object  
`callback` |  `[GetNodeGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and NodeGroup  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getNodeGroup(request)
    
    
    public getNodeGroup(request: google.cloud.dataproc.v1.IGetNodeGroupRequest): Promise<google.cloud.dataproc.v1.NodeGroup>;

Calls GetNodeGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.igetnodegrouprequest)`   
GetNodeGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataproc.v1.NodeGroup](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.nodegroup-class)>` | Promise  
  
### resizeNodeGroup(request, callback)
    
    
    public resizeNodeGroup(request: google.cloud.dataproc.v1.IResizeNodeGroupRequest, callback: google.cloud.dataproc.v1.NodeGroupController.ResizeNodeGroupCallback): void;

Calls ResizeNodeGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResizeNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iresizenodegrouprequest)`   
ResizeNodeGroupRequest message or plain object  
`callback` |  `[ResizeNodeGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### resizeNodeGroup(request)
    
    
    public resizeNodeGroup(request: google.cloud.dataproc.v1.IResizeNodeGroupRequest): Promise<google.longrunning.Operation>;

Calls ResizeNodeGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IResizeNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iresizenodegrouprequest)`   
ResizeNodeGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
