---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.agents-class
title: Class protos.google.cloud.dialogflow.cx.v3.Agents (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:52:53.436655+00:00
---

# Class protos.google.cloud.dialogflow.cx.v3.Agents (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.agents-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.cx.v3.Agents (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.6.0  5.5.0  5.1.0  5.0.1  4.10.0  4.9.0  4.8.0  4.6.0  4.3.1  4.2.0  4.0.0  3.4.2  3.2.1  3.1.2  2.15.0  2.14.0  2.13.0  2.12.1 

Represents an Agents

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dialogflow.cx.v3.Agents

## Package

[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)

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
`[Agents](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.agents-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAgent(request, callback)
    
    
    public createAgent(request: google.cloud.dialogflow.cx.v3.ICreateAgentRequest, callback: google.cloud.dialogflow.cx.v3.Agents.CreateAgentCallback): void;

Calls CreateAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.icreateagentrequest)`   
CreateAgentRequest message or plain object  
`callback` |  `[CreateAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)`   
Node-style callback called with the error, if any, and Agent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAgent(request)
    
    
    public createAgent(request: google.cloud.dialogflow.cx.v3.ICreateAgentRequest): Promise<google.cloud.dialogflow.cx.v3.Agent>;

Calls CreateAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.icreateagentrequest)`   
CreateAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.cx.v3.Agent](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.agent-class)>` | Promise  
  
### deleteAgent(request, callback)
    
    
    public deleteAgent(request: google.cloud.dialogflow.cx.v3.IDeleteAgentRequest, callback: google.cloud.dialogflow.cx.v3.Agents.DeleteAgentCallback): void;

Calls DeleteAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.ideleteagentrequest)`   
DeleteAgentRequest message or plain object  
`callback` |  `[DeleteAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAgent(request)
    
    
    public deleteAgent(request: google.cloud.dialogflow.cx.v3.IDeleteAgentRequest): Promise<google.protobuf.Empty>;

Calls DeleteAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.ideleteagentrequest)`   
DeleteAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.protobuf.empty)>` | Promise  
  
### exportAgent(request, callback)
    
    
    public exportAgent(request: google.cloud.dialogflow.cx.v3.IExportAgentRequest, callback: google.cloud.dialogflow.cx.v3.Agents.ExportAgentCallback): void;

Calls ExportAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.iexportagentrequest)`   
ExportAgentRequest message or plain object  
`callback` |  `[ExportAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportAgent(request)
    
    
    public exportAgent(request: google.cloud.dialogflow.cx.v3.IExportAgentRequest): Promise<google.longrunning.Operation>;

Calls ExportAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.iexportagentrequest)`   
ExportAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.operation)>` | Promise  
  
### getAgent(request, callback)
    
    
    public getAgent(request: google.cloud.dialogflow.cx.v3.IGetAgentRequest, callback: google.cloud.dialogflow.cx.v3.Agents.GetAgentCallback): void;

Calls GetAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.igetagentrequest)`   
GetAgentRequest message or plain object  
`callback` |  `[GetAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)`   
Node-style callback called with the error, if any, and Agent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAgent(request)
    
    
    public getAgent(request: google.cloud.dialogflow.cx.v3.IGetAgentRequest): Promise<google.cloud.dialogflow.cx.v3.Agent>;

Calls GetAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.igetagentrequest)`   
GetAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.cx.v3.Agent](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.agent-class)>` | Promise  
  
### getAgentValidationResult(request, callback)
    
    
    public getAgentValidationResult(request: google.cloud.dialogflow.cx.v3.IGetAgentValidationResultRequest, callback: google.cloud.dialogflow.cx.v3.Agents.GetAgentValidationResultCallback): void;

Calls GetAgentValidationResult.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAgentValidationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.igetagentvalidationresultrequest)`   
GetAgentValidationResultRequest message or plain object  
`callback` |  `[GetAgentValidationResultCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)`   
Node-style callback called with the error, if any, and AgentValidationResult  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAgentValidationResult(request)
    
    
    public getAgentValidationResult(request: google.cloud.dialogflow.cx.v3.IGetAgentValidationResultRequest): Promise<google.cloud.dialogflow.cx.v3.AgentValidationResult>;

Calls GetAgentValidationResult.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAgentValidationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.igetagentvalidationresultrequest)`   
GetAgentValidationResultRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.cx.v3.AgentValidationResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.agentvalidationresult)>` | Promise  
  
### getGenerativeSettings(request, callback)
    
    
    public getGenerativeSettings(request: google.cloud.dialogflow.cx.v3.IGetGenerativeSettingsRequest, callback: google.cloud.dialogflow.cx.v3.Agents.GetGenerativeSettingsCallback): void;

Calls GetGenerativeSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetGenerativeSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.igetgenerativesettingsrequest)`   
GetGenerativeSettingsRequest message or plain object  
`callback` |  `[GetGenerativeSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerativeSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getGenerativeSettings(request)
    
    
    public getGenerativeSettings(request: google.cloud.dialogflow.cx.v3.IGetGenerativeSettingsRequest): Promise<google.cloud.dialogflow.cx.v3.GenerativeSettings>;

Calls GetGenerativeSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetGenerativeSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.igetgenerativesettingsrequest)`   
GetGenerativeSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.cx.v3.GenerativeSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.generativesettings-class)>` | Promise  
  
### listAgents(request, callback)
    
    
    public listAgents(request: google.cloud.dialogflow.cx.v3.IListAgentsRequest, callback: google.cloud.dialogflow.cx.v3.Agents.ListAgentsCallback): void;

Calls ListAgents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.ilistagentsrequest)`   
ListAgentsRequest message or plain object  
`callback` |  `[ListAgentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAgentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAgents(request)
    
    
    public listAgents(request: google.cloud.dialogflow.cx.v3.IListAgentsRequest): Promise<google.cloud.dialogflow.cx.v3.ListAgentsResponse>;

Calls ListAgents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.ilistagentsrequest)`   
ListAgentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.cx.v3.ListAgentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.listagentsresponse)>` | Promise  
  
### restoreAgent(request, callback)
    
    
    public restoreAgent(request: google.cloud.dialogflow.cx.v3.IRestoreAgentRequest, callback: google.cloud.dialogflow.cx.v3.Agents.RestoreAgentCallback): void;

Calls RestoreAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRestoreAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.irestoreagentrequest)`   
RestoreAgentRequest message or plain object  
`callback` |  `[RestoreAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### restoreAgent(request)
    
    
    public restoreAgent(request: google.cloud.dialogflow.cx.v3.IRestoreAgentRequest): Promise<google.longrunning.Operation>;

Calls RestoreAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRestoreAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.irestoreagentrequest)`   
RestoreAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.longrunning.operation)>` | Promise  
  
### updateAgent(request, callback)
    
    
    public updateAgent(request: google.cloud.dialogflow.cx.v3.IUpdateAgentRequest, callback: google.cloud.dialogflow.cx.v3.Agents.UpdateAgentCallback): void;

Calls UpdateAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.iupdateagentrequest)`   
UpdateAgentRequest message or plain object  
`callback` |  `[UpdateAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)`   
Node-style callback called with the error, if any, and Agent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAgent(request)
    
    
    public updateAgent(request: google.cloud.dialogflow.cx.v3.IUpdateAgentRequest): Promise<google.cloud.dialogflow.cx.v3.Agent>;

Calls UpdateAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.iupdateagentrequest)`   
UpdateAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.cx.v3.Agent](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.agent-class)>` | Promise  
  
### updateGenerativeSettings(request, callback)
    
    
    public updateGenerativeSettings(request: google.cloud.dialogflow.cx.v3.IUpdateGenerativeSettingsRequest, callback: google.cloud.dialogflow.cx.v3.Agents.UpdateGenerativeSettingsCallback): void;

Calls UpdateGenerativeSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGenerativeSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.iupdategenerativesettingsrequest)`   
UpdateGenerativeSettingsRequest message or plain object  
`callback` |  `[UpdateGenerativeSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerativeSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateGenerativeSettings(request)
    
    
    public updateGenerativeSettings(request: google.cloud.dialogflow.cx.v3.IUpdateGenerativeSettingsRequest): Promise<google.cloud.dialogflow.cx.v3.GenerativeSettings>;

Calls UpdateGenerativeSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGenerativeSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.iupdategenerativesettingsrequest)`   
UpdateGenerativeSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.cx.v3.GenerativeSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.generativesettings-class)>` | Promise  
  
### validateAgent(request, callback)
    
    
    public validateAgent(request: google.cloud.dialogflow.cx.v3.IValidateAgentRequest, callback: google.cloud.dialogflow.cx.v3.Agents.ValidateAgentCallback): void;

Calls ValidateAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IValidateAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.ivalidateagentrequest)`   
ValidateAgentRequest message or plain object  
`callback` |  `[ValidateAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)`   
Node-style callback called with the error, if any, and AgentValidationResult  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### validateAgent(request)
    
    
    public validateAgent(request: google.cloud.dialogflow.cx.v3.IValidateAgentRequest): Promise<google.cloud.dialogflow.cx.v3.AgentValidationResult>;

Calls ValidateAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IValidateAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.ivalidateagentrequest)`   
ValidateAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.cx.v3.AgentValidationResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.agentvalidationresult)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
