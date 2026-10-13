---
url: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.metadataservice-class
title: Class protos.google.cloud.aiplatform.v1.MetadataService (7.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:01.855508+00:00
---

# Class protos.google.cloud.aiplatform.v1.MetadataService (7.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.metadataservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.aiplatform.v1.MetadataService (7.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.4.1 (latest)  7.3.0  6.10.0  6.9.0  6.8.1  6.6.0  6.4.0  6.3.0  6.2.0  6.1.0  6.0.0  5.14.0  5.13.0  3.15.0  3.13.0  3.11.0  3.10.1  3.9.0  3.7.0  3.6.0  3.4.0  3.3.0  3.0.0  2.12.0  2.11.0  2.10.0  2.7.0  2.6.1  2.5.0  2.3.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.11.0  1.7.2 

Represents a MetadataService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.aiplatform.v1.MetadataService

## Package

[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new MetadataService service.

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

### addContextArtifactsAndExecutions(request, callback)
    
    
    public addContextArtifactsAndExecutions(request: google.cloud.aiplatform.v1.IAddContextArtifactsAndExecutionsRequest, callback: google.cloud.aiplatform.v1.MetadataService.AddContextArtifactsAndExecutionsCallback): void;

Calls AddContextArtifactsAndExecutions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddContextArtifactsAndExecutionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iaddcontextartifactsandexecutionsrequest)`   
AddContextArtifactsAndExecutionsRequest message or plain object  
`callback` |  `[AddContextArtifactsAndExecutionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and AddContextArtifactsAndExecutionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addContextArtifactsAndExecutions(request)
    
    
    public addContextArtifactsAndExecutions(request: google.cloud.aiplatform.v1.IAddContextArtifactsAndExecutionsRequest): Promise<google.cloud.aiplatform.v1.AddContextArtifactsAndExecutionsResponse>;

Calls AddContextArtifactsAndExecutions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAddContextArtifactsAndExecutionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iaddcontextartifactsandexecutionsrequest)`   
AddContextArtifactsAndExecutionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.AddContextArtifactsAndExecutionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.addcontextartifactsandexecutionsresponse)>` | Promise  
  
### addContextChildren(request, callback)
    
    
    public addContextChildren(request: google.cloud.aiplatform.v1.IAddContextChildrenRequest, callback: google.cloud.aiplatform.v1.MetadataService.AddContextChildrenCallback): void;

Calls AddContextChildren.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddContextChildrenRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iaddcontextchildrenrequest)`   
AddContextChildrenRequest message or plain object  
`callback` |  `[AddContextChildrenCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and AddContextChildrenResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addContextChildren(request)
    
    
    public addContextChildren(request: google.cloud.aiplatform.v1.IAddContextChildrenRequest): Promise<google.cloud.aiplatform.v1.AddContextChildrenResponse>;

Calls AddContextChildren.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAddContextChildrenRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iaddcontextchildrenrequest)`   
AddContextChildrenRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.AddContextChildrenResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.addcontextchildrenresponse)>` | Promise  
  
### addExecutionEvents(request, callback)
    
    
    public addExecutionEvents(request: google.cloud.aiplatform.v1.IAddExecutionEventsRequest, callback: google.cloud.aiplatform.v1.MetadataService.AddExecutionEventsCallback): void;

Calls AddExecutionEvents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddExecutionEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iaddexecutioneventsrequest)`   
AddExecutionEventsRequest message or plain object  
`callback` |  `[AddExecutionEventsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and AddExecutionEventsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addExecutionEvents(request)
    
    
    public addExecutionEvents(request: google.cloud.aiplatform.v1.IAddExecutionEventsRequest): Promise<google.cloud.aiplatform.v1.AddExecutionEventsResponse>;

Calls AddExecutionEvents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAddExecutionEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iaddexecutioneventsrequest)`   
AddExecutionEventsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.AddExecutionEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.addexecutioneventsresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): MetadataService;

Creates new MetadataService service using the specified rpc implementation.

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
`[MetadataService](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.metadataservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createArtifact(request, callback)
    
    
    public createArtifact(request: google.cloud.aiplatform.v1.ICreateArtifactRequest, callback: google.cloud.aiplatform.v1.MetadataService.CreateArtifactCallback): void;

Calls CreateArtifact.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateArtifactRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.icreateartifactrequest)`   
CreateArtifactRequest message or plain object  
`callback` |  `[CreateArtifactCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Artifact  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createArtifact(request)
    
    
    public createArtifact(request: google.cloud.aiplatform.v1.ICreateArtifactRequest): Promise<google.cloud.aiplatform.v1.Artifact>;

Calls CreateArtifact.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateArtifactRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.icreateartifactrequest)`   
CreateArtifactRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.Artifact](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.artifact-class)>` | Promise  
  
### createContext(request, callback)
    
    
    public createContext(request: google.cloud.aiplatform.v1.ICreateContextRequest, callback: google.cloud.aiplatform.v1.MetadataService.CreateContextCallback): void;

Calls CreateContext.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateContextRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.icreatecontextrequest)`   
CreateContextRequest message or plain object  
`callback` |  `[CreateContextCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Context  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createContext(request)
    
    
    public createContext(request: google.cloud.aiplatform.v1.ICreateContextRequest): Promise<google.cloud.aiplatform.v1.Context>;

Calls CreateContext.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateContextRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.icreatecontextrequest)`   
CreateContextRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.Context](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.context)>` | Promise  
  
### createExecution(request, callback)
    
    
    public createExecution(request: google.cloud.aiplatform.v1.ICreateExecutionRequest, callback: google.cloud.aiplatform.v1.MetadataService.CreateExecutionCallback): void;

Calls CreateExecution.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateExecutionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.icreateexecutionrequest)`   
CreateExecutionRequest message or plain object  
`callback` |  `[CreateExecutionCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Execution  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createExecution(request)
    
    
    public createExecution(request: google.cloud.aiplatform.v1.ICreateExecutionRequest): Promise<google.cloud.aiplatform.v1.Execution>;

Calls CreateExecution.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateExecutionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.icreateexecutionrequest)`   
CreateExecutionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.Execution](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.execution-class)>` | Promise  
  
### createMetadataSchema(request, callback)
    
    
    public createMetadataSchema(request: google.cloud.aiplatform.v1.ICreateMetadataSchemaRequest, callback: google.cloud.aiplatform.v1.MetadataService.CreateMetadataSchemaCallback): void;

Calls CreateMetadataSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMetadataSchemaRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.icreatemetadataschemarequest)`   
CreateMetadataSchemaRequest message or plain object  
`callback` |  `[CreateMetadataSchemaCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and MetadataSchema  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMetadataSchema(request)
    
    
    public createMetadataSchema(request: google.cloud.aiplatform.v1.ICreateMetadataSchemaRequest): Promise<google.cloud.aiplatform.v1.MetadataSchema>;

Calls CreateMetadataSchema.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateMetadataSchemaRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.icreatemetadataschemarequest)`   
CreateMetadataSchemaRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.MetadataSchema](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.metadataschema-class)>` | Promise  
  
### createMetadataStore(request, callback)
    
    
    public createMetadataStore(request: google.cloud.aiplatform.v1.ICreateMetadataStoreRequest, callback: google.cloud.aiplatform.v1.MetadataService.CreateMetadataStoreCallback): void;

Calls CreateMetadataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMetadataStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.icreatemetadatastorerequest)`   
CreateMetadataStoreRequest message or plain object  
`callback` |  `[CreateMetadataStoreCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMetadataStore(request)
    
    
    public createMetadataStore(request: google.cloud.aiplatform.v1.ICreateMetadataStoreRequest): Promise<google.longrunning.Operation>;

Calls CreateMetadataStore.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateMetadataStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.icreatemetadatastorerequest)`   
CreateMetadataStoreRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### deleteArtifact(request, callback)
    
    
    public deleteArtifact(request: google.cloud.aiplatform.v1.IDeleteArtifactRequest, callback: google.cloud.aiplatform.v1.MetadataService.DeleteArtifactCallback): void;

Calls DeleteArtifact.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteArtifactRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideleteartifactrequest)`   
DeleteArtifactRequest message or plain object  
`callback` |  `[DeleteArtifactCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteArtifact(request)
    
    
    public deleteArtifact(request: google.cloud.aiplatform.v1.IDeleteArtifactRequest): Promise<google.longrunning.Operation>;

Calls DeleteArtifact.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteArtifactRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideleteartifactrequest)`   
DeleteArtifactRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### deleteContext(request, callback)
    
    
    public deleteContext(request: google.cloud.aiplatform.v1.IDeleteContextRequest, callback: google.cloud.aiplatform.v1.MetadataService.DeleteContextCallback): void;

Calls DeleteContext.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteContextRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideletecontextrequest)`   
DeleteContextRequest message or plain object  
`callback` |  `[DeleteContextCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteContext(request)
    
    
    public deleteContext(request: google.cloud.aiplatform.v1.IDeleteContextRequest): Promise<google.longrunning.Operation>;

Calls DeleteContext.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteContextRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideletecontextrequest)`   
DeleteContextRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### deleteExecution(request, callback)
    
    
    public deleteExecution(request: google.cloud.aiplatform.v1.IDeleteExecutionRequest, callback: google.cloud.aiplatform.v1.MetadataService.DeleteExecutionCallback): void;

Calls DeleteExecution.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteExecutionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideleteexecutionrequest)`   
DeleteExecutionRequest message or plain object  
`callback` |  `[DeleteExecutionCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteExecution(request)
    
    
    public deleteExecution(request: google.cloud.aiplatform.v1.IDeleteExecutionRequest): Promise<google.longrunning.Operation>;

Calls DeleteExecution.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteExecutionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideleteexecutionrequest)`   
DeleteExecutionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### deleteMetadataStore(request, callback)
    
    
    public deleteMetadataStore(request: google.cloud.aiplatform.v1.IDeleteMetadataStoreRequest, callback: google.cloud.aiplatform.v1.MetadataService.DeleteMetadataStoreCallback): void;

Calls DeleteMetadataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMetadataStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideletemetadatastorerequest)`   
DeleteMetadataStoreRequest message or plain object  
`callback` |  `[DeleteMetadataStoreCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMetadataStore(request)
    
    
    public deleteMetadataStore(request: google.cloud.aiplatform.v1.IDeleteMetadataStoreRequest): Promise<google.longrunning.Operation>;

Calls DeleteMetadataStore.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMetadataStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideletemetadatastorerequest)`   
DeleteMetadataStoreRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### getArtifact(request, callback)
    
    
    public getArtifact(request: google.cloud.aiplatform.v1.IGetArtifactRequest, callback: google.cloud.aiplatform.v1.MetadataService.GetArtifactCallback): void;

Calls GetArtifact.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetArtifactRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.igetartifactrequest)`   
GetArtifactRequest message or plain object  
`callback` |  `[GetArtifactCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Artifact  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getArtifact(request)
    
    
    public getArtifact(request: google.cloud.aiplatform.v1.IGetArtifactRequest): Promise<google.cloud.aiplatform.v1.Artifact>;

Calls GetArtifact.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetArtifactRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.igetartifactrequest)`   
GetArtifactRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.Artifact](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.artifact-class)>` | Promise  
  
### getContext(request, callback)
    
    
    public getContext(request: google.cloud.aiplatform.v1.IGetContextRequest, callback: google.cloud.aiplatform.v1.MetadataService.GetContextCallback): void;

Calls GetContext.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetContextRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.igetcontextrequest)`   
GetContextRequest message or plain object  
`callback` |  `[GetContextCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Context  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getContext(request)
    
    
    public getContext(request: google.cloud.aiplatform.v1.IGetContextRequest): Promise<google.cloud.aiplatform.v1.Context>;

Calls GetContext.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetContextRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.igetcontextrequest)`   
GetContextRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.Context](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.context)>` | Promise  
  
### getExecution(request, callback)
    
    
    public getExecution(request: google.cloud.aiplatform.v1.IGetExecutionRequest, callback: google.cloud.aiplatform.v1.MetadataService.GetExecutionCallback): void;

Calls GetExecution.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetExecutionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.igetexecutionrequest)`   
GetExecutionRequest message or plain object  
`callback` |  `[GetExecutionCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Execution  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getExecution(request)
    
    
    public getExecution(request: google.cloud.aiplatform.v1.IGetExecutionRequest): Promise<google.cloud.aiplatform.v1.Execution>;

Calls GetExecution.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetExecutionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.igetexecutionrequest)`   
GetExecutionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.Execution](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.execution-class)>` | Promise  
  
### getMetadataSchema(request, callback)
    
    
    public getMetadataSchema(request: google.cloud.aiplatform.v1.IGetMetadataSchemaRequest, callback: google.cloud.aiplatform.v1.MetadataService.GetMetadataSchemaCallback): void;

Calls GetMetadataSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMetadataSchemaRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.igetmetadataschemarequest)`   
GetMetadataSchemaRequest message or plain object  
`callback` |  `[GetMetadataSchemaCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and MetadataSchema  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMetadataSchema(request)
    
    
    public getMetadataSchema(request: google.cloud.aiplatform.v1.IGetMetadataSchemaRequest): Promise<google.cloud.aiplatform.v1.MetadataSchema>;

Calls GetMetadataSchema.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetMetadataSchemaRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.igetmetadataschemarequest)`   
GetMetadataSchemaRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.MetadataSchema](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.metadataschema-class)>` | Promise  
  
### getMetadataStore(request, callback)
    
    
    public getMetadataStore(request: google.cloud.aiplatform.v1.IGetMetadataStoreRequest, callback: google.cloud.aiplatform.v1.MetadataService.GetMetadataStoreCallback): void;

Calls GetMetadataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMetadataStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.igetmetadatastorerequest)`   
GetMetadataStoreRequest message or plain object  
`callback` |  `[GetMetadataStoreCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and MetadataStore  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMetadataStore(request)
    
    
    public getMetadataStore(request: google.cloud.aiplatform.v1.IGetMetadataStoreRequest): Promise<google.cloud.aiplatform.v1.MetadataStore>;

Calls GetMetadataStore.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetMetadataStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.igetmetadatastorerequest)`   
GetMetadataStoreRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.MetadataStore](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.metadatastore-class)>` | Promise  
  
### listArtifacts(request, callback)
    
    
    public listArtifacts(request: google.cloud.aiplatform.v1.IListArtifactsRequest, callback: google.cloud.aiplatform.v1.MetadataService.ListArtifactsCallback): void;

Calls ListArtifacts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListArtifactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ilistartifactsrequest)`   
ListArtifactsRequest message or plain object  
`callback` |  `[ListArtifactsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListArtifactsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listArtifacts(request)
    
    
    public listArtifacts(request: google.cloud.aiplatform.v1.IListArtifactsRequest): Promise<google.cloud.aiplatform.v1.ListArtifactsResponse>;

Calls ListArtifacts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListArtifactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ilistartifactsrequest)`   
ListArtifactsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.ListArtifactsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.listartifactsresponse)>` | Promise  
  
### listContexts(request, callback)
    
    
    public listContexts(request: google.cloud.aiplatform.v1.IListContextsRequest, callback: google.cloud.aiplatform.v1.MetadataService.ListContextsCallback): void;

Calls ListContexts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListContextsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ilistcontextsrequest)`   
ListContextsRequest message or plain object  
`callback` |  `[ListContextsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListContextsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listContexts(request)
    
    
    public listContexts(request: google.cloud.aiplatform.v1.IListContextsRequest): Promise<google.cloud.aiplatform.v1.ListContextsResponse>;

Calls ListContexts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListContextsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ilistcontextsrequest)`   
ListContextsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.ListContextsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.listcontextsresponse)>` | Promise  
  
### listExecutions(request, callback)
    
    
    public listExecutions(request: google.cloud.aiplatform.v1.IListExecutionsRequest, callback: google.cloud.aiplatform.v1.MetadataService.ListExecutionsCallback): void;

Calls ListExecutions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListExecutionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ilistexecutionsrequest)`   
ListExecutionsRequest message or plain object  
`callback` |  `[ListExecutionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListExecutionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listExecutions(request)
    
    
    public listExecutions(request: google.cloud.aiplatform.v1.IListExecutionsRequest): Promise<google.cloud.aiplatform.v1.ListExecutionsResponse>;

Calls ListExecutions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListExecutionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ilistexecutionsrequest)`   
ListExecutionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.ListExecutionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.listexecutionsresponse)>` | Promise  
  
### listMetadataSchemas(request, callback)
    
    
    public listMetadataSchemas(request: google.cloud.aiplatform.v1.IListMetadataSchemasRequest, callback: google.cloud.aiplatform.v1.MetadataService.ListMetadataSchemasCallback): void;

Calls ListMetadataSchemas.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMetadataSchemasRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ilistmetadataschemasrequest)`   
ListMetadataSchemasRequest message or plain object  
`callback` |  `[ListMetadataSchemasCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMetadataSchemasResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMetadataSchemas(request)
    
    
    public listMetadataSchemas(request: google.cloud.aiplatform.v1.IListMetadataSchemasRequest): Promise<google.cloud.aiplatform.v1.ListMetadataSchemasResponse>;

Calls ListMetadataSchemas.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMetadataSchemasRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ilistmetadataschemasrequest)`   
ListMetadataSchemasRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.ListMetadataSchemasResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.listmetadataschemasresponse)>` | Promise  
  
### listMetadataStores(request, callback)
    
    
    public listMetadataStores(request: google.cloud.aiplatform.v1.IListMetadataStoresRequest, callback: google.cloud.aiplatform.v1.MetadataService.ListMetadataStoresCallback): void;

Calls ListMetadataStores.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMetadataStoresRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ilistmetadatastoresrequest)`   
ListMetadataStoresRequest message or plain object  
`callback` |  `[ListMetadataStoresCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMetadataStoresResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMetadataStores(request)
    
    
    public listMetadataStores(request: google.cloud.aiplatform.v1.IListMetadataStoresRequest): Promise<google.cloud.aiplatform.v1.ListMetadataStoresResponse>;

Calls ListMetadataStores.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMetadataStoresRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ilistmetadatastoresrequest)`   
ListMetadataStoresRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.ListMetadataStoresResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.listmetadatastoresresponse)>` | Promise  
  
### purgeArtifacts(request, callback)
    
    
    public purgeArtifacts(request: google.cloud.aiplatform.v1.IPurgeArtifactsRequest, callback: google.cloud.aiplatform.v1.MetadataService.PurgeArtifactsCallback): void;

Calls PurgeArtifacts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPurgeArtifactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ipurgeartifactsrequest)`   
PurgeArtifactsRequest message or plain object  
`callback` |  `[PurgeArtifactsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### purgeArtifacts(request)
    
    
    public purgeArtifacts(request: google.cloud.aiplatform.v1.IPurgeArtifactsRequest): Promise<google.longrunning.Operation>;

Calls PurgeArtifacts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPurgeArtifactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ipurgeartifactsrequest)`   
PurgeArtifactsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### purgeContexts(request, callback)
    
    
    public purgeContexts(request: google.cloud.aiplatform.v1.IPurgeContextsRequest, callback: google.cloud.aiplatform.v1.MetadataService.PurgeContextsCallback): void;

Calls PurgeContexts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPurgeContextsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ipurgecontextsrequest)`   
PurgeContextsRequest message or plain object  
`callback` |  `[PurgeContextsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### purgeContexts(request)
    
    
    public purgeContexts(request: google.cloud.aiplatform.v1.IPurgeContextsRequest): Promise<google.longrunning.Operation>;

Calls PurgeContexts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPurgeContextsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ipurgecontextsrequest)`   
PurgeContextsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### purgeExecutions(request, callback)
    
    
    public purgeExecutions(request: google.cloud.aiplatform.v1.IPurgeExecutionsRequest, callback: google.cloud.aiplatform.v1.MetadataService.PurgeExecutionsCallback): void;

Calls PurgeExecutions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPurgeExecutionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ipurgeexecutionsrequest)`   
PurgeExecutionsRequest message or plain object  
`callback` |  `[PurgeExecutionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### purgeExecutions(request)
    
    
    public purgeExecutions(request: google.cloud.aiplatform.v1.IPurgeExecutionsRequest): Promise<google.longrunning.Operation>;

Calls PurgeExecutions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPurgeExecutionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ipurgeexecutionsrequest)`   
PurgeExecutionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### queryArtifactLineageSubgraph(request, callback)
    
    
    public queryArtifactLineageSubgraph(request: google.cloud.aiplatform.v1.IQueryArtifactLineageSubgraphRequest, callback: google.cloud.aiplatform.v1.MetadataService.QueryArtifactLineageSubgraphCallback): void;

Calls QueryArtifactLineageSubgraph.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryArtifactLineageSubgraphRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iqueryartifactlineagesubgraphrequest)`   
QueryArtifactLineageSubgraphRequest message or plain object  
`callback` |  `[QueryArtifactLineageSubgraphCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and LineageSubgraph  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryArtifactLineageSubgraph(request)
    
    
    public queryArtifactLineageSubgraph(request: google.cloud.aiplatform.v1.IQueryArtifactLineageSubgraphRequest): Promise<google.cloud.aiplatform.v1.LineageSubgraph>;

Calls QueryArtifactLineageSubgraph.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IQueryArtifactLineageSubgraphRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iqueryartifactlineagesubgraphrequest)`   
QueryArtifactLineageSubgraphRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.LineageSubgraph](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.lineagesubgraph)>` | Promise  
  
### queryContextLineageSubgraph(request, callback)
    
    
    public queryContextLineageSubgraph(request: google.cloud.aiplatform.v1.IQueryContextLineageSubgraphRequest, callback: google.cloud.aiplatform.v1.MetadataService.QueryContextLineageSubgraphCallback): void;

Calls QueryContextLineageSubgraph.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryContextLineageSubgraphRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iquerycontextlineagesubgraphrequest)`   
QueryContextLineageSubgraphRequest message or plain object  
`callback` |  `[QueryContextLineageSubgraphCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and LineageSubgraph  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryContextLineageSubgraph(request)
    
    
    public queryContextLineageSubgraph(request: google.cloud.aiplatform.v1.IQueryContextLineageSubgraphRequest): Promise<google.cloud.aiplatform.v1.LineageSubgraph>;

Calls QueryContextLineageSubgraph.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IQueryContextLineageSubgraphRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iquerycontextlineagesubgraphrequest)`   
QueryContextLineageSubgraphRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.LineageSubgraph](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.lineagesubgraph)>` | Promise  
  
### queryExecutionInputsAndOutputs(request, callback)
    
    
    public queryExecutionInputsAndOutputs(request: google.cloud.aiplatform.v1.IQueryExecutionInputsAndOutputsRequest, callback: google.cloud.aiplatform.v1.MetadataService.QueryExecutionInputsAndOutputsCallback): void;

Calls QueryExecutionInputsAndOutputs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryExecutionInputsAndOutputsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iqueryexecutioninputsandoutputsrequest)`   
QueryExecutionInputsAndOutputsRequest message or plain object  
`callback` |  `[QueryExecutionInputsAndOutputsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and LineageSubgraph  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryExecutionInputsAndOutputs(request)
    
    
    public queryExecutionInputsAndOutputs(request: google.cloud.aiplatform.v1.IQueryExecutionInputsAndOutputsRequest): Promise<google.cloud.aiplatform.v1.LineageSubgraph>;

Calls QueryExecutionInputsAndOutputs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IQueryExecutionInputsAndOutputsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iqueryexecutioninputsandoutputsrequest)`   
QueryExecutionInputsAndOutputsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.LineageSubgraph](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.lineagesubgraph)>` | Promise  
  
### removeContextChildren(request, callback)
    
    
    public removeContextChildren(request: google.cloud.aiplatform.v1.IRemoveContextChildrenRequest, callback: google.cloud.aiplatform.v1.MetadataService.RemoveContextChildrenCallback): void;

Calls RemoveContextChildren.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveContextChildrenRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iremovecontextchildrenrequest)`   
RemoveContextChildrenRequest message or plain object  
`callback` |  `[RemoveContextChildrenCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and RemoveContextChildrenResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeContextChildren(request)
    
    
    public removeContextChildren(request: google.cloud.aiplatform.v1.IRemoveContextChildrenRequest): Promise<google.cloud.aiplatform.v1.RemoveContextChildrenResponse>;

Calls RemoveContextChildren.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRemoveContextChildrenRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iremovecontextchildrenrequest)`   
RemoveContextChildrenRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.RemoveContextChildrenResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.removecontextchildrenresponse)>` | Promise  
  
### updateArtifact(request, callback)
    
    
    public updateArtifact(request: google.cloud.aiplatform.v1.IUpdateArtifactRequest, callback: google.cloud.aiplatform.v1.MetadataService.UpdateArtifactCallback): void;

Calls UpdateArtifact.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateArtifactRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iupdateartifactrequest)`   
UpdateArtifactRequest message or plain object  
`callback` |  `[UpdateArtifactCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Artifact  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateArtifact(request)
    
    
    public updateArtifact(request: google.cloud.aiplatform.v1.IUpdateArtifactRequest): Promise<google.cloud.aiplatform.v1.Artifact>;

Calls UpdateArtifact.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateArtifactRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iupdateartifactrequest)`   
UpdateArtifactRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.Artifact](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.artifact-class)>` | Promise  
  
### updateContext(request, callback)
    
    
    public updateContext(request: google.cloud.aiplatform.v1.IUpdateContextRequest, callback: google.cloud.aiplatform.v1.MetadataService.UpdateContextCallback): void;

Calls UpdateContext.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateContextRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iupdatecontextrequest)`   
UpdateContextRequest message or plain object  
`callback` |  `[UpdateContextCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Context  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateContext(request)
    
    
    public updateContext(request: google.cloud.aiplatform.v1.IUpdateContextRequest): Promise<google.cloud.aiplatform.v1.Context>;

Calls UpdateContext.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateContextRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iupdatecontextrequest)`   
UpdateContextRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.Context](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.context)>` | Promise  
  
### updateExecution(request, callback)
    
    
    public updateExecution(request: google.cloud.aiplatform.v1.IUpdateExecutionRequest, callback: google.cloud.aiplatform.v1.MetadataService.UpdateExecutionCallback): void;

Calls UpdateExecution.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateExecutionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iupdateexecutionrequest)`   
UpdateExecutionRequest message or plain object  
`callback` |  `[UpdateExecutionCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Execution  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateExecution(request)
    
    
    public updateExecution(request: google.cloud.aiplatform.v1.IUpdateExecutionRequest): Promise<google.cloud.aiplatform.v1.Execution>;

Calls UpdateExecution.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateExecutionRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iupdateexecutionrequest)`   
UpdateExecutionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.Execution](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.execution-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
