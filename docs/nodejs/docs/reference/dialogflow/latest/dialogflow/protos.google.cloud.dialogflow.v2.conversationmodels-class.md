---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversationmodels-class
title: Class protos.google.cloud.dialogflow.v2.ConversationModels (8.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:59:38.229871+00:00
---

# Class protos.google.cloud.dialogflow.v2.ConversationModels (8.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversationmodels-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.v2.ConversationModels (8.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

8.2.0 (latest)  8.1.1  7.9.0  7.8.0  7.7.0  7.5.0  7.4.0  7.1.0  7.0.1  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.8.0  6.6.0  6.4.0  6.3.1  6.2.0  6.0.0  5.7.1  5.6.0  5.5.1  5.3.0  5.2.1  4.7.0  4.6.0  4.5.0  4.4.0  4.3.1  4.2.0  4.1.4  3.5.0  3.3.0 

Represents a ConversationModels

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dialogflow.v2.ConversationModels

## Package

[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ConversationModels service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ConversationModels;

Creates new ConversationModels service using the specified rpc implementation.

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
`[ConversationModels](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversationmodels-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createConversationModel(request, callback)
    
    
    public createConversationModel(request: google.cloud.dialogflow.v2.ICreateConversationModelRequest, callback: google.cloud.dialogflow.v2.ConversationModels.CreateConversationModelCallback): void;

Calls CreateConversationModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversationModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.icreateconversationmodelrequest)`   
CreateConversationModelRequest message or plain object  
`callback` |  `[CreateConversationModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConversationModel(request)
    
    
    public createConversationModel(request: google.cloud.dialogflow.v2.ICreateConversationModelRequest): Promise<google.longrunning.Operation>;

Calls CreateConversationModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversationModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.icreateconversationmodelrequest)`   
CreateConversationModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.longrunning.operation)>` | Promise  
  
### createConversationModelEvaluation(request, callback)
    
    
    public createConversationModelEvaluation(request: google.cloud.dialogflow.v2.ICreateConversationModelEvaluationRequest, callback: google.cloud.dialogflow.v2.ConversationModels.CreateConversationModelEvaluationCallback): void;

Calls CreateConversationModelEvaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversationModelEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.icreateconversationmodelevaluationrequest)`   
CreateConversationModelEvaluationRequest message or plain object  
`callback` |  `[CreateConversationModelEvaluationCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConversationModelEvaluation(request)
    
    
    public createConversationModelEvaluation(request: google.cloud.dialogflow.v2.ICreateConversationModelEvaluationRequest): Promise<google.longrunning.Operation>;

Calls CreateConversationModelEvaluation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversationModelEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.icreateconversationmodelevaluationrequest)`   
CreateConversationModelEvaluationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.longrunning.operation)>` | Promise  
  
### deleteConversationModel(request, callback)
    
    
    public deleteConversationModel(request: google.cloud.dialogflow.v2.IDeleteConversationModelRequest, callback: google.cloud.dialogflow.v2.ConversationModels.DeleteConversationModelCallback): void;

Calls DeleteConversationModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversationModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ideleteconversationmodelrequest)`   
DeleteConversationModelRequest message or plain object  
`callback` |  `[DeleteConversationModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConversationModel(request)
    
    
    public deleteConversationModel(request: google.cloud.dialogflow.v2.IDeleteConversationModelRequest): Promise<google.longrunning.Operation>;

Calls DeleteConversationModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversationModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ideleteconversationmodelrequest)`   
DeleteConversationModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.longrunning.operation)>` | Promise  
  
### deployConversationModel(request, callback)
    
    
    public deployConversationModel(request: google.cloud.dialogflow.v2.IDeployConversationModelRequest, callback: google.cloud.dialogflow.v2.ConversationModels.DeployConversationModelCallback): void;

Calls DeployConversationModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeployConversationModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ideployconversationmodelrequest)`   
DeployConversationModelRequest message or plain object  
`callback` |  `[DeployConversationModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deployConversationModel(request)
    
    
    public deployConversationModel(request: google.cloud.dialogflow.v2.IDeployConversationModelRequest): Promise<google.longrunning.Operation>;

Calls DeployConversationModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeployConversationModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ideployconversationmodelrequest)`   
DeployConversationModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.longrunning.operation)>` | Promise  
  
### getConversationModel(request, callback)
    
    
    public getConversationModel(request: google.cloud.dialogflow.v2.IGetConversationModelRequest, callback: google.cloud.dialogflow.v2.ConversationModels.GetConversationModelCallback): void;

Calls GetConversationModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetconversationmodelrequest)`   
GetConversationModelRequest message or plain object  
`callback` |  `[GetConversationModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and ConversationModel  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConversationModel(request)
    
    
    public getConversationModel(request: google.cloud.dialogflow.v2.IGetConversationModelRequest): Promise<google.cloud.dialogflow.v2.ConversationModel>;

Calls GetConversationModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetconversationmodelrequest)`   
GetConversationModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.ConversationModel](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversationmodel-class)>` | Promise  
  
### getConversationModelEvaluation(request, callback)
    
    
    public getConversationModelEvaluation(request: google.cloud.dialogflow.v2.IGetConversationModelEvaluationRequest, callback: google.cloud.dialogflow.v2.ConversationModels.GetConversationModelEvaluationCallback): void;

Calls GetConversationModelEvaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationModelEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetconversationmodelevaluationrequest)`   
GetConversationModelEvaluationRequest message or plain object  
`callback` |  `[GetConversationModelEvaluationCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and ConversationModelEvaluation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConversationModelEvaluation(request)
    
    
    public getConversationModelEvaluation(request: google.cloud.dialogflow.v2.IGetConversationModelEvaluationRequest): Promise<google.cloud.dialogflow.v2.ConversationModelEvaluation>;

Calls GetConversationModelEvaluation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationModelEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetconversationmodelevaluationrequest)`   
GetConversationModelEvaluationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.ConversationModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.conversationmodelevaluation)>` | Promise  
  
### listConversationModelEvaluations(request, callback)
    
    
    public listConversationModelEvaluations(request: google.cloud.dialogflow.v2.IListConversationModelEvaluationsRequest, callback: google.cloud.dialogflow.v2.ConversationModels.ListConversationModelEvaluationsCallback): void;

Calls ListConversationModelEvaluations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversationModelEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistconversationmodelevaluationsrequest)`   
ListConversationModelEvaluationsRequest message or plain object  
`callback` |  `[ListConversationModelEvaluationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and ListConversationModelEvaluationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConversationModelEvaluations(request)
    
    
    public listConversationModelEvaluations(request: google.cloud.dialogflow.v2.IListConversationModelEvaluationsRequest): Promise<google.cloud.dialogflow.v2.ListConversationModelEvaluationsResponse>;

Calls ListConversationModelEvaluations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListConversationModelEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistconversationmodelevaluationsrequest)`   
ListConversationModelEvaluationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.ListConversationModelEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.listconversationmodelevaluationsresponse)>` | Promise  
  
### listConversationModels(request, callback)
    
    
    public listConversationModels(request: google.cloud.dialogflow.v2.IListConversationModelsRequest, callback: google.cloud.dialogflow.v2.ConversationModels.ListConversationModelsCallback): void;

Calls ListConversationModels.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversationModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistconversationmodelsrequest)`   
ListConversationModelsRequest message or plain object  
`callback` |  `[ListConversationModelsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and ListConversationModelsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConversationModels(request)
    
    
    public listConversationModels(request: google.cloud.dialogflow.v2.IListConversationModelsRequest): Promise<google.cloud.dialogflow.v2.ListConversationModelsResponse>;

Calls ListConversationModels.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListConversationModelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistconversationmodelsrequest)`   
ListConversationModelsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.ListConversationModelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.listconversationmodelsresponse)>` | Promise  
  
### undeployConversationModel(request, callback)
    
    
    public undeployConversationModel(request: google.cloud.dialogflow.v2.IUndeployConversationModelRequest, callback: google.cloud.dialogflow.v2.ConversationModels.UndeployConversationModelCallback): void;

Calls UndeployConversationModel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeployConversationModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iundeployconversationmodelrequest)`   
UndeployConversationModelRequest message or plain object  
`callback` |  `[UndeployConversationModelCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### undeployConversationModel(request)
    
    
    public undeployConversationModel(request: google.cloud.dialogflow.v2.IUndeployConversationModelRequest): Promise<google.longrunning.Operation>;

Calls UndeployConversationModel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUndeployConversationModelRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iundeployconversationmodelrequest)`   
UndeployConversationModelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
