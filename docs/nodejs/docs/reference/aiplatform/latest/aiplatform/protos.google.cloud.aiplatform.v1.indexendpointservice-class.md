---
url: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.indexendpointservice-class
title: Class protos.google.cloud.aiplatform.v1.IndexEndpointService (7.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:32.296718+00:00
---

# Class protos.google.cloud.aiplatform.v1.IndexEndpointService (7.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.indexendpointservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.aiplatform.v1.IndexEndpointService (7.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.4.1 (latest)  7.3.0  6.10.0  6.9.0  6.8.1  6.6.0  6.4.0  6.3.0  6.2.0  6.1.0  6.0.0  5.14.0  5.13.0  3.15.0  3.13.0  3.11.0  3.10.1  3.9.0  3.7.0  3.6.0  3.4.0  3.3.0  3.0.0  2.12.0  2.11.0  2.10.0  2.7.0  2.6.1  2.5.0  2.3.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.11.0  1.7.2 

Represents an IndexEndpointService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.aiplatform.v1.IndexEndpointService

## Package

[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new IndexEndpointService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): IndexEndpointService;

Creates new IndexEndpointService service using the specified rpc implementation.

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
`[IndexEndpointService](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.indexendpointservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createIndexEndpoint(request, callback)
    
    
    public createIndexEndpoint(request: google.cloud.aiplatform.v1.ICreateIndexEndpointRequest, callback: google.cloud.aiplatform.v1.IndexEndpointService.CreateIndexEndpointCallback): void;

Calls CreateIndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateIndexEndpointRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.icreateindexendpointrequest)`   
CreateIndexEndpointRequest message or plain object  
`callback` |  `[CreateIndexEndpointCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createIndexEndpoint(request)
    
    
    public createIndexEndpoint(request: google.cloud.aiplatform.v1.ICreateIndexEndpointRequest): Promise<google.longrunning.Operation>;

Calls CreateIndexEndpoint.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateIndexEndpointRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.icreateindexendpointrequest)`   
CreateIndexEndpointRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### deleteIndexEndpoint(request, callback)
    
    
    public deleteIndexEndpoint(request: google.cloud.aiplatform.v1.IDeleteIndexEndpointRequest, callback: google.cloud.aiplatform.v1.IndexEndpointService.DeleteIndexEndpointCallback): void;

Calls DeleteIndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteIndexEndpointRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideleteindexendpointrequest)`   
DeleteIndexEndpointRequest message or plain object  
`callback` |  `[DeleteIndexEndpointCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteIndexEndpoint(request)
    
    
    public deleteIndexEndpoint(request: google.cloud.aiplatform.v1.IDeleteIndexEndpointRequest): Promise<google.longrunning.Operation>;

Calls DeleteIndexEndpoint.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteIndexEndpointRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideleteindexendpointrequest)`   
DeleteIndexEndpointRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### deployIndex(request, callback)
    
    
    public deployIndex(request: google.cloud.aiplatform.v1.IDeployIndexRequest, callback: google.cloud.aiplatform.v1.IndexEndpointService.DeployIndexCallback): void;

Calls DeployIndex.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeployIndexRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideployindexrequest)`   
DeployIndexRequest message or plain object  
`callback` |  `[DeployIndexCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deployIndex(request)
    
    
    public deployIndex(request: google.cloud.aiplatform.v1.IDeployIndexRequest): Promise<google.longrunning.Operation>;

Calls DeployIndex.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeployIndexRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideployindexrequest)`   
DeployIndexRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### getIndexEndpoint(request, callback)
    
    
    public getIndexEndpoint(request: google.cloud.aiplatform.v1.IGetIndexEndpointRequest, callback: google.cloud.aiplatform.v1.IndexEndpointService.GetIndexEndpointCallback): void;

Calls GetIndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIndexEndpointRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.igetindexendpointrequest)`   
GetIndexEndpointRequest message or plain object  
`callback` |  `[GetIndexEndpointCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and IndexEndpoint  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIndexEndpoint(request)
    
    
    public getIndexEndpoint(request: google.cloud.aiplatform.v1.IGetIndexEndpointRequest): Promise<google.cloud.aiplatform.v1.IndexEndpoint>;

Calls GetIndexEndpoint.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetIndexEndpointRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.igetindexendpointrequest)`   
GetIndexEndpointRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.IndexEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.indexendpoint)>` | Promise  
  
### listIndexEndpoints(request, callback)
    
    
    public listIndexEndpoints(request: google.cloud.aiplatform.v1.IListIndexEndpointsRequest, callback: google.cloud.aiplatform.v1.IndexEndpointService.ListIndexEndpointsCallback): void;

Calls ListIndexEndpoints.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListIndexEndpointsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ilistindexendpointsrequest)`   
ListIndexEndpointsRequest message or plain object  
`callback` |  `[ListIndexEndpointsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListIndexEndpointsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listIndexEndpoints(request)
    
    
    public listIndexEndpoints(request: google.cloud.aiplatform.v1.IListIndexEndpointsRequest): Promise<google.cloud.aiplatform.v1.ListIndexEndpointsResponse>;

Calls ListIndexEndpoints.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListIndexEndpointsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ilistindexendpointsrequest)`   
ListIndexEndpointsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.ListIndexEndpointsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.listindexendpointsresponse)>` | Promise  
  
### mutateDeployedIndex(request, callback)
    
    
    public mutateDeployedIndex(request: google.cloud.aiplatform.v1.IMutateDeployedIndexRequest, callback: google.cloud.aiplatform.v1.IndexEndpointService.MutateDeployedIndexCallback): void;

Calls MutateDeployedIndex.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMutateDeployedIndexRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.imutatedeployedindexrequest)`   
MutateDeployedIndexRequest message or plain object  
`callback` |  `[MutateDeployedIndexCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### mutateDeployedIndex(request)
    
    
    public mutateDeployedIndex(request: google.cloud.aiplatform.v1.IMutateDeployedIndexRequest): Promise<google.longrunning.Operation>;

Calls MutateDeployedIndex.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IMutateDeployedIndexRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.imutatedeployedindexrequest)`   
MutateDeployedIndexRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### undeployIndex(request, callback)
    
    
    public undeployIndex(request: google.cloud.aiplatform.v1.IUndeployIndexRequest, callback: google.cloud.aiplatform.v1.IndexEndpointService.UndeployIndexCallback): void;

Calls UndeployIndex.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeployIndexRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iundeployindexrequest)`   
UndeployIndexRequest message or plain object  
`callback` |  `[UndeployIndexCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### undeployIndex(request)
    
    
    public undeployIndex(request: google.cloud.aiplatform.v1.IUndeployIndexRequest): Promise<google.longrunning.Operation>;

Calls UndeployIndex.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUndeployIndexRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iundeployindexrequest)`   
UndeployIndexRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### updateIndexEndpoint(request, callback)
    
    
    public updateIndexEndpoint(request: google.cloud.aiplatform.v1.IUpdateIndexEndpointRequest, callback: google.cloud.aiplatform.v1.IndexEndpointService.UpdateIndexEndpointCallback): void;

Calls UpdateIndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateIndexEndpointRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iupdateindexendpointrequest)`   
UpdateIndexEndpointRequest message or plain object  
`callback` |  `[UpdateIndexEndpointCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and IndexEndpoint  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateIndexEndpoint(request)
    
    
    public updateIndexEndpoint(request: google.cloud.aiplatform.v1.IUpdateIndexEndpointRequest): Promise<google.cloud.aiplatform.v1.IndexEndpoint>;

Calls UpdateIndexEndpoint.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateIndexEndpointRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iupdateindexendpointrequest)`   
UpdateIndexEndpointRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.IndexEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.indexendpoint)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
