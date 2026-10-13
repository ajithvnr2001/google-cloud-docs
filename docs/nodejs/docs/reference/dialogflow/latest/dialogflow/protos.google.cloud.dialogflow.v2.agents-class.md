---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.agents-class
title: Class protos.google.cloud.dialogflow.v2.Agents (8.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:59:09.388341+00:00
---

# Class protos.google.cloud.dialogflow.v2.Agents (8.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.agents-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.v2.Agents (8.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

8.2.0 (latest)  8.1.1  7.9.0  7.8.0  7.7.0  7.5.0  7.4.0  7.1.0  7.0.1  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.8.0  6.6.0  6.4.0  6.3.1  6.2.0  6.0.0  5.7.1  5.6.0  5.5.1  5.3.0  5.2.1  4.7.0  4.6.0  4.5.0  4.4.0  4.3.1  4.2.0  4.1.4  3.5.0  3.3.0 

Represents an Agents

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dialogflow.v2.Agents

## Package

[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Agents service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Agents;

Creates new Agents service using the specified rpc implementation.

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
`[Agents](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.agents-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### deleteAgent(request, callback)
    
    
    public deleteAgent(request: google.cloud.dialogflow.v2.IDeleteAgentRequest, callback: google.cloud.dialogflow.v2.Agents.DeleteAgentCallback): void;

Calls DeleteAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ideleteagentrequest)`   
DeleteAgentRequest message or plain object  
`callback` |  `[DeleteAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAgent(request)
    
    
    public deleteAgent(request: google.cloud.dialogflow.v2.IDeleteAgentRequest): Promise<google.protobuf.Empty>;

Calls DeleteAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ideleteagentrequest)`   
DeleteAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.protobuf.empty)>` | Promise  
  
### exportAgent(request, callback)
    
    
    public exportAgent(request: google.cloud.dialogflow.v2.IExportAgentRequest, callback: google.cloud.dialogflow.v2.Agents.ExportAgentCallback): void;

Calls ExportAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iexportagentrequest)`   
ExportAgentRequest message or plain object  
`callback` |  `[ExportAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportAgent(request)
    
    
    public exportAgent(request: google.cloud.dialogflow.v2.IExportAgentRequest): Promise<google.longrunning.Operation>;

Calls ExportAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iexportagentrequest)`   
ExportAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.longrunning.operation)>` | Promise  
  
### getAgent(request, callback)
    
    
    public getAgent(request: google.cloud.dialogflow.v2.IGetAgentRequest, callback: google.cloud.dialogflow.v2.Agents.GetAgentCallback): void;

Calls GetAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetagentrequest)`   
GetAgentRequest message or plain object  
`callback` |  `[GetAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Agent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAgent(request)
    
    
    public getAgent(request: google.cloud.dialogflow.v2.IGetAgentRequest): Promise<google.cloud.dialogflow.v2.Agent>;

Calls GetAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetagentrequest)`   
GetAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.Agent](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.agent-class)>` | Promise  
  
### getValidationResult(request, callback)
    
    
    public getValidationResult(request: google.cloud.dialogflow.v2.IGetValidationResultRequest, callback: google.cloud.dialogflow.v2.Agents.GetValidationResultCallback): void;

Calls GetValidationResult.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetValidationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetvalidationresultrequest)`   
GetValidationResultRequest message or plain object  
`callback` |  `[GetValidationResultCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and ValidationResult  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getValidationResult(request)
    
    
    public getValidationResult(request: google.cloud.dialogflow.v2.IGetValidationResultRequest): Promise<google.cloud.dialogflow.v2.ValidationResult>;

Calls GetValidationResult.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetValidationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetvalidationresultrequest)`   
GetValidationResultRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.ValidationResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.validationresult)>` | Promise  
  
### importAgent(request, callback)
    
    
    public importAgent(request: google.cloud.dialogflow.v2.IImportAgentRequest, callback: google.cloud.dialogflow.v2.Agents.ImportAgentCallback): void;

Calls ImportAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iimportagentrequest)`   
ImportAgentRequest message or plain object  
`callback` |  `[ImportAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importAgent(request)
    
    
    public importAgent(request: google.cloud.dialogflow.v2.IImportAgentRequest): Promise<google.longrunning.Operation>;

Calls ImportAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iimportagentrequest)`   
ImportAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.longrunning.operation)>` | Promise  
  
### restoreAgent(request, callback)
    
    
    public restoreAgent(request: google.cloud.dialogflow.v2.IRestoreAgentRequest, callback: google.cloud.dialogflow.v2.Agents.RestoreAgentCallback): void;

Calls RestoreAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRestoreAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.irestoreagentrequest)`   
RestoreAgentRequest message or plain object  
`callback` |  `[RestoreAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### restoreAgent(request)
    
    
    public restoreAgent(request: google.cloud.dialogflow.v2.IRestoreAgentRequest): Promise<google.longrunning.Operation>;

Calls RestoreAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRestoreAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.irestoreagentrequest)`   
RestoreAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.longrunning.operation)>` | Promise  
  
### searchAgents(request, callback)
    
    
    public searchAgents(request: google.cloud.dialogflow.v2.ISearchAgentsRequest, callback: google.cloud.dialogflow.v2.Agents.SearchAgentsCallback): void;

Calls SearchAgents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.isearchagentsrequest)`   
SearchAgentsRequest message or plain object  
`callback` |  `[SearchAgentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchAgentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchAgents(request)
    
    
    public searchAgents(request: google.cloud.dialogflow.v2.ISearchAgentsRequest): Promise<google.cloud.dialogflow.v2.SearchAgentsResponse>;

Calls SearchAgents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.isearchagentsrequest)`   
SearchAgentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.SearchAgentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.searchagentsresponse)>` | Promise  
  
### setAgent(request, callback)
    
    
    public setAgent(request: google.cloud.dialogflow.v2.ISetAgentRequest, callback: google.cloud.dialogflow.v2.Agents.SetAgentCallback): void;

Calls SetAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.isetagentrequest)`   
SetAgentRequest message or plain object  
`callback` |  `[SetAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Agent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setAgent(request)
    
    
    public setAgent(request: google.cloud.dialogflow.v2.ISetAgentRequest): Promise<google.cloud.dialogflow.v2.Agent>;

Calls SetAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.isetagentrequest)`   
SetAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.Agent](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.agent-class)>` | Promise  
  
### trainAgent(request, callback)
    
    
    public trainAgent(request: google.cloud.dialogflow.v2.ITrainAgentRequest, callback: google.cloud.dialogflow.v2.Agents.TrainAgentCallback): void;

Calls TrainAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITrainAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.itrainagentrequest)`   
TrainAgentRequest message or plain object  
`callback` |  `[TrainAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### trainAgent(request)
    
    
    public trainAgent(request: google.cloud.dialogflow.v2.ITrainAgentRequest): Promise<google.longrunning.Operation>;

Calls TrainAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ITrainAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.itrainagentrequest)`   
TrainAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
