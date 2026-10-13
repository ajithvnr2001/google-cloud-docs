---
url: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta2.modelservice-class
title: Class protos.google.ai.generativelanguage.v1beta2.ModelService (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:16.882832+00:00
---

# Class protos.google.ai.generativelanguage.v1beta2.ModelService (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta2.modelservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ai.generativelanguage.v1beta2.ModelService (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  4.1.0  3.7.0  3.6.0  2.9.0  2.8.0  2.7.0  2.6.0  2.4.0  2.3.0 

Represents a ModelService

## Inheritance

$protobuf.rpc.Service > protos.google.ai.generativelanguage.v1beta2.ModelService

## Package

[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)

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
`[ModelService](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta2.modelservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### getModel(request, callback)
    
    
    public getModel(request: google.ai.generativelanguage.v1beta2.IGetModelRequest, callback: google.ai.generativelanguage.v1beta2.ModelService.GetModelCallback): void;

Calls GetModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta2.igetmodelrequest)`   
GetModelRequest message or plain object  
`callback` |  `[GetModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and Model  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getModel(request)
    
    
    public getModel(request: google.ai.generativelanguage.v1beta2.IGetModelRequest): Promise<google.ai.generativelanguage.v1beta2.Model>;

Calls GetModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta2.igetmodelrequest)`   
GetModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1beta2.Model](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta2.model)>` | Promise  
  
### listModels(request, callback)
    
    
    public listModels(request: google.ai.generativelanguage.v1beta2.IListModelsRequest, callback: google.ai.generativelanguage.v1beta2.ModelService.ListModelsCallback): void;

Calls ListModels.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta2.ilistmodelsrequest)`   
ListModelsRequest message or plain object  
`callback` |  `[ListModelsCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and ListModelsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listModels(request)
    
    
    public listModels(request: google.ai.generativelanguage.v1beta2.IListModelsRequest): Promise<google.ai.generativelanguage.v1beta2.ListModelsResponse>;

Calls ListModels.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta2.ilistmodelsrequest)`   
ListModelsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1beta2.ListModelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta2.listmodelsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
