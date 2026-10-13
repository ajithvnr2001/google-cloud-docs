---
url: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.modelservice-class
title: Class protos.google.cloud.retail.v2beta.ModelService (5.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:12:47.482781+00:00
---

# Class protos.google.cloud.retail.v2beta.ModelService (5.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.modelservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.retail.v2beta.ModelService (5.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.4.0 (latest)  5.3.1  5.0.1  4.4.0  4.3.0  3.6.0  3.5.0  3.1.0  2.4.1  2.3.1  2.1.1  2.0.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.2  1.1.6 

Represents a ModelService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.retail.v2beta.ModelService

## Package

[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ModelService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ModelService;

Creates new ModelService service using the specified rpc implementation.

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
`[ModelService](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.modelservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createModel(request, callback)
    
    
    public createModel(request: google.cloud.retail.v2beta.ICreateModelRequest, callback: google.cloud.retail.v2beta.ModelService.CreateModelCallback): void;

Calls CreateModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.icreatemodelrequest)`   
CreateModelRequest message or plain object  
`callback` |  `[CreateModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createModel(request)
    
    
    public createModel(request: google.cloud.retail.v2beta.ICreateModelRequest): Promise<google.longrunning.Operation>;

Calls CreateModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.icreatemodelrequest)`   
CreateModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)>` | Promise  
  
### deleteModel(request, callback)
    
    
    public deleteModel(request: google.cloud.retail.v2beta.IDeleteModelRequest, callback: google.cloud.retail.v2beta.ModelService.DeleteModelCallback): void;

Calls DeleteModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ideletemodelrequest)`   
DeleteModelRequest message or plain object  
`callback` |  `[DeleteModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteModel(request)
    
    
    public deleteModel(request: google.cloud.retail.v2beta.IDeleteModelRequest): Promise<google.protobuf.Empty>;

Calls DeleteModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ideletemodelrequest)`   
DeleteModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.empty)>` | Promise  
  
### getModel(request, callback)
    
    
    public getModel(request: google.cloud.retail.v2beta.IGetModelRequest, callback: google.cloud.retail.v2beta.ModelService.GetModelCallback): void;

Calls GetModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.igetmodelrequest)`   
GetModelRequest message or plain object  
`callback` |  `[GetModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Model  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getModel(request)
    
    
    public getModel(request: google.cloud.retail.v2beta.IGetModelRequest): Promise<google.cloud.retail.v2beta.Model>;

Calls GetModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.igetmodelrequest)`   
GetModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.retail.v2beta.Model](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.model-class)>` | Promise  
  
### listModels(request, callback)
    
    
    public listModels(request: google.cloud.retail.v2beta.IListModelsRequest, callback: google.cloud.retail.v2beta.ModelService.ListModelsCallback): void;

Calls ListModels.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ilistmodelsrequest)`   
ListModelsRequest message or plain object  
`callback` |  `[ListModelsCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and ListModelsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listModels(request)
    
    
    public listModels(request: google.cloud.retail.v2beta.IListModelsRequest): Promise<google.cloud.retail.v2beta.ListModelsResponse>;

Calls ListModels.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ilistmodelsrequest)`   
ListModelsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.retail.v2beta.ListModelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.listmodelsresponse)>` | Promise  
  
### pauseModel(request, callback)
    
    
    public pauseModel(request: google.cloud.retail.v2beta.IPauseModelRequest, callback: google.cloud.retail.v2beta.ModelService.PauseModelCallback): void;

Calls PauseModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPauseModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ipausemodelrequest)`   
PauseModelRequest message or plain object  
`callback` |  `[PauseModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Model  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### pauseModel(request)
    
    
    public pauseModel(request: google.cloud.retail.v2beta.IPauseModelRequest): Promise<google.cloud.retail.v2beta.Model>;

Calls PauseModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPauseModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ipausemodelrequest)`   
PauseModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.retail.v2beta.Model](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.model-class)>` | Promise  
  
### resumeModel(request, callback)
    
    
    public resumeModel(request: google.cloud.retail.v2beta.IResumeModelRequest, callback: google.cloud.retail.v2beta.ModelService.ResumeModelCallback): void;

Calls ResumeModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResumeModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iresumemodelrequest)`   
ResumeModelRequest message or plain object  
`callback` |  `[ResumeModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Model  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### resumeModel(request)
    
    
    public resumeModel(request: google.cloud.retail.v2beta.IResumeModelRequest): Promise<google.cloud.retail.v2beta.Model>;

Calls ResumeModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IResumeModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iresumemodelrequest)`   
ResumeModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.retail.v2beta.Model](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.model-class)>` | Promise  
  
### tuneModel(request, callback)
    
    
    public tuneModel(request: google.cloud.retail.v2beta.ITuneModelRequest, callback: google.cloud.retail.v2beta.ModelService.TuneModelCallback): void;

Calls TuneModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITuneModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.itunemodelrequest)`   
TuneModelRequest message or plain object  
`callback` |  `[TuneModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### tuneModel(request)
    
    
    public tuneModel(request: google.cloud.retail.v2beta.ITuneModelRequest): Promise<google.longrunning.Operation>;

Calls TuneModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ITuneModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.itunemodelrequest)`   
TuneModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)>` | Promise  
  
### updateModel(request, callback)
    
    
    public updateModel(request: google.cloud.retail.v2beta.IUpdateModelRequest, callback: google.cloud.retail.v2beta.ModelService.UpdateModelCallback): void;

Calls UpdateModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iupdatemodelrequest)`   
UpdateModelRequest message or plain object  
`callback` |  `[UpdateModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Model  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateModel(request)
    
    
    public updateModel(request: google.cloud.retail.v2beta.IUpdateModelRequest): Promise<google.cloud.retail.v2beta.Model>;

Calls UpdateModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iupdatemodelrequest)`   
UpdateModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.retail.v2beta.Model](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.model-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
