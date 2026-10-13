---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.companionagents-class
title: Class protos.google.cloud.dialogflow.v2.CompanionAgents (8.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:59:28.629668+00:00
---

# Class protos.google.cloud.dialogflow.v2.CompanionAgents (8.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.companionagents-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.v2.CompanionAgents (8.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

8.2.0 (latest)  8.1.1  7.9.0  7.8.0  7.7.0  7.5.0  7.4.0  7.1.0  7.0.1  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.8.0  6.6.0  6.4.0  6.3.1  6.2.0  6.0.0  5.7.1  5.6.0  5.5.1  5.3.0  5.2.1  4.7.0  4.6.0  4.5.0  4.4.0  4.3.1  4.2.0  4.1.4  3.5.0  3.3.0 

Represents a CompanionAgents

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dialogflow.v2.CompanionAgents

## Package

[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new CompanionAgents service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): CompanionAgents;

Creates new CompanionAgents service using the specified rpc implementation.

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
`[CompanionAgents](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.companionagents-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createCompanionAgent(request, callback)
    
    
    public createCompanionAgent(request: google.cloud.dialogflow.v2.ICreateCompanionAgentRequest, callback: google.cloud.dialogflow.v2.CompanionAgents.CreateCompanionAgentCallback): void;

Calls CreateCompanionAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCompanionAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.icreatecompanionagentrequest)`   
CreateCompanionAgentRequest message or plain object  
`callback` |  `[CreateCompanionAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and CompanionAgent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCompanionAgent(request)
    
    
    public createCompanionAgent(request: google.cloud.dialogflow.v2.ICreateCompanionAgentRequest): Promise<google.cloud.dialogflow.v2.CompanionAgent>;

Calls CreateCompanionAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCompanionAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.icreatecompanionagentrequest)`   
CreateCompanionAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.CompanionAgent](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.companionagent-class)>` | Promise  
  
### deleteCompanionAgent(request, callback)
    
    
    public deleteCompanionAgent(request: google.cloud.dialogflow.v2.IDeleteCompanionAgentRequest, callback: google.cloud.dialogflow.v2.CompanionAgents.DeleteCompanionAgentCallback): void;

Calls DeleteCompanionAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCompanionAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ideletecompanionagentrequest)`   
DeleteCompanionAgentRequest message or plain object  
`callback` |  `[DeleteCompanionAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCompanionAgent(request)
    
    
    public deleteCompanionAgent(request: google.cloud.dialogflow.v2.IDeleteCompanionAgentRequest): Promise<google.protobuf.Empty>;

Calls DeleteCompanionAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCompanionAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ideletecompanionagentrequest)`   
DeleteCompanionAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.protobuf.empty)>` | Promise  
  
### getCompanionAgent(request, callback)
    
    
    public getCompanionAgent(request: google.cloud.dialogflow.v2.IGetCompanionAgentRequest, callback: google.cloud.dialogflow.v2.CompanionAgents.GetCompanionAgentCallback): void;

Calls GetCompanionAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCompanionAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetcompanionagentrequest)`   
GetCompanionAgentRequest message or plain object  
`callback` |  `[GetCompanionAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and CompanionAgent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCompanionAgent(request)
    
    
    public getCompanionAgent(request: google.cloud.dialogflow.v2.IGetCompanionAgentRequest): Promise<google.cloud.dialogflow.v2.CompanionAgent>;

Calls GetCompanionAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCompanionAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetcompanionagentrequest)`   
GetCompanionAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.CompanionAgent](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.companionagent-class)>` | Promise  
  
### listCompanionAgents(request, callback)
    
    
    public listCompanionAgents(request: google.cloud.dialogflow.v2.IListCompanionAgentsRequest, callback: google.cloud.dialogflow.v2.CompanionAgents.ListCompanionAgentsCallback): void;

Calls ListCompanionAgents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCompanionAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistcompanionagentsrequest)`   
ListCompanionAgentsRequest message or plain object  
`callback` |  `[ListCompanionAgentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCompanionAgentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCompanionAgents(request)
    
    
    public listCompanionAgents(request: google.cloud.dialogflow.v2.IListCompanionAgentsRequest): Promise<google.cloud.dialogflow.v2.ListCompanionAgentsResponse>;

Calls ListCompanionAgents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCompanionAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistcompanionagentsrequest)`   
ListCompanionAgentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.ListCompanionAgentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.listcompanionagentsresponse)>` | Promise  
  
### updateCompanionAgent(request, callback)
    
    
    public updateCompanionAgent(request: google.cloud.dialogflow.v2.IUpdateCompanionAgentRequest, callback: google.cloud.dialogflow.v2.CompanionAgents.UpdateCompanionAgentCallback): void;

Calls UpdateCompanionAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCompanionAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iupdatecompanionagentrequest)`   
UpdateCompanionAgentRequest message or plain object  
`callback` |  `[UpdateCompanionAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and CompanionAgent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCompanionAgent(request)
    
    
    public updateCompanionAgent(request: google.cloud.dialogflow.v2.IUpdateCompanionAgentRequest): Promise<google.cloud.dialogflow.v2.CompanionAgent>;

Calls UpdateCompanionAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCompanionAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iupdatecompanionagentrequest)`   
UpdateCompanionAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.CompanionAgent](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.companionagent-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
