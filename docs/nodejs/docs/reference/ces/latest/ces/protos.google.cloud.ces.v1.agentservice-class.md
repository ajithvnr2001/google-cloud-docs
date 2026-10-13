---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.agentservice-class
title: Class protos.google.cloud.ces.v1.AgentService (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:05:52.099560+00:00
---

# Class protos.google.cloud.ces.v1.AgentService (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.agentservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ces.v1.AgentService (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

Represents an AgentService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.ces.v1.AgentService

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AgentService service.

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

### batchDeleteConversations(request, callback)
    
    
    public batchDeleteConversations(request: google.cloud.ces.v1.IBatchDeleteConversationsRequest, callback: google.cloud.ces.v1.AgentService.BatchDeleteConversationsCallback): void;

Calls BatchDeleteConversations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ibatchdeleteconversationsrequest)`   
BatchDeleteConversationsRequest message or plain object  
`callback` |  `[BatchDeleteConversationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchDeleteConversations(request)
    
    
    public batchDeleteConversations(request: google.cloud.ces.v1.IBatchDeleteConversationsRequest): Promise<google.longrunning.Operation>;

Calls BatchDeleteConversations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ibatchdeleteconversationsrequest)`   
BatchDeleteConversationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.operation)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AgentService;

Creates new AgentService service using the specified rpc implementation.

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
`[AgentService](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.agentservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAgent(request, callback)
    
    
    public createAgent(request: google.cloud.ces.v1.ICreateAgentRequest, callback: google.cloud.ces.v1.AgentService.CreateAgentCallback): void;

Calls CreateAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreateagentrequest)`   
CreateAgentRequest message or plain object  
`callback` |  `[CreateAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Agent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAgent(request)
    
    
    public createAgent(request: google.cloud.ces.v1.ICreateAgentRequest): Promise<google.cloud.ces.v1.Agent>;

Calls CreateAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreateagentrequest)`   
CreateAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.Agent](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.agent-class)>` | Promise  
  
### createApp(request, callback)
    
    
    public createApp(request: google.cloud.ces.v1.ICreateAppRequest, callback: google.cloud.ces.v1.AgentService.CreateAppCallback): void;

Calls CreateApp.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAppRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreateapprequest)`   
CreateAppRequest message or plain object  
`callback` |  `[CreateAppCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createApp(request)
    
    
    public createApp(request: google.cloud.ces.v1.ICreateAppRequest): Promise<google.longrunning.Operation>;

Calls CreateApp.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAppRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreateapprequest)`   
CreateAppRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.operation)>` | Promise  
  
### createAppVersion(request, callback)
    
    
    public createAppVersion(request: google.cloud.ces.v1.ICreateAppVersionRequest, callback: google.cloud.ces.v1.AgentService.CreateAppVersionCallback): void;

Calls CreateAppVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAppVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreateappversionrequest)`   
CreateAppVersionRequest message or plain object  
`callback` |  `[CreateAppVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and AppVersion  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAppVersion(request)
    
    
    public createAppVersion(request: google.cloud.ces.v1.ICreateAppVersionRequest): Promise<google.cloud.ces.v1.AppVersion>;

Calls CreateAppVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAppVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreateappversionrequest)`   
CreateAppVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.AppVersion](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.appversion)>` | Promise  
  
### createDeployment(request, callback)
    
    
    public createDeployment(request: google.cloud.ces.v1.ICreateDeploymentRequest, callback: google.cloud.ces.v1.AgentService.CreateDeploymentCallback): void;

Calls CreateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreatedeploymentrequest)`   
CreateDeploymentRequest message or plain object  
`callback` |  `[CreateDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Deployment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDeployment(request)
    
    
    public createDeployment(request: google.cloud.ces.v1.ICreateDeploymentRequest): Promise<google.cloud.ces.v1.Deployment>;

Calls CreateDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreatedeploymentrequest)`   
CreateDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.Deployment](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.deployment)>` | Promise  
  
### createExample(request, callback)
    
    
    public createExample(request: google.cloud.ces.v1.ICreateExampleRequest, callback: google.cloud.ces.v1.AgentService.CreateExampleCallback): void;

Calls CreateExample.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateExampleRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreateexamplerequest)`   
CreateExampleRequest message or plain object  
`callback` |  `[CreateExampleCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Example  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createExample(request)
    
    
    public createExample(request: google.cloud.ces.v1.ICreateExampleRequest): Promise<google.cloud.ces.v1.Example>;

Calls CreateExample.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateExampleRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreateexamplerequest)`   
CreateExampleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.Example](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.example)>` | Promise  
  
### createGuardrail(request, callback)
    
    
    public createGuardrail(request: google.cloud.ces.v1.ICreateGuardrailRequest, callback: google.cloud.ces.v1.AgentService.CreateGuardrailCallback): void;

Calls CreateGuardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateGuardrailRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreateguardrailrequest)`   
CreateGuardrailRequest message or plain object  
`callback` |  `[CreateGuardrailCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Guardrail  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createGuardrail(request)
    
    
    public createGuardrail(request: google.cloud.ces.v1.ICreateGuardrailRequest): Promise<google.cloud.ces.v1.Guardrail>;

Calls CreateGuardrail.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateGuardrailRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreateguardrailrequest)`   
CreateGuardrailRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.Guardrail](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.guardrail-class)>` | Promise  
  
### createTool(request, callback)
    
    
    public createTool(request: google.cloud.ces.v1.ICreateToolRequest, callback: google.cloud.ces.v1.AgentService.CreateToolCallback): void;

Calls CreateTool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreatetoolrequest)`   
CreateToolRequest message or plain object  
`callback` |  `[CreateToolCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Tool  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTool(request)
    
    
    public createTool(request: google.cloud.ces.v1.ICreateToolRequest): Promise<google.cloud.ces.v1.Tool>;

Calls CreateTool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreatetoolrequest)`   
CreateToolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.Tool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.tool)>` | Promise  
  
### createToolset(request, callback)
    
    
    public createToolset(request: google.cloud.ces.v1.ICreateToolsetRequest, callback: google.cloud.ces.v1.AgentService.CreateToolsetCallback): void;

Calls CreateToolset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateToolsetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreatetoolsetrequest)`   
CreateToolsetRequest message or plain object  
`callback` |  `[CreateToolsetCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Toolset  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createToolset(request)
    
    
    public createToolset(request: google.cloud.ces.v1.ICreateToolsetRequest): Promise<google.cloud.ces.v1.Toolset>;

Calls CreateToolset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateToolsetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.icreatetoolsetrequest)`   
CreateToolsetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.Toolset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.toolset)>` | Promise  
  
### deleteAgent(request, callback)
    
    
    public deleteAgent(request: google.cloud.ces.v1.IDeleteAgentRequest, callback: google.cloud.ces.v1.AgentService.DeleteAgentCallback): void;

Calls DeleteAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ideleteagentrequest)`   
DeleteAgentRequest message or plain object  
`callback` |  `[DeleteAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAgent(request)
    
    
    public deleteAgent(request: google.cloud.ces.v1.IDeleteAgentRequest): Promise<google.protobuf.Empty>;

Calls DeleteAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ideleteagentrequest)`   
DeleteAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.empty)>` | Promise  
  
### deleteApp(request, callback)
    
    
    public deleteApp(request: google.cloud.ces.v1.IDeleteAppRequest, callback: google.cloud.ces.v1.AgentService.DeleteAppCallback): void;

Calls DeleteApp.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAppRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ideleteapprequest)`   
DeleteAppRequest message or plain object  
`callback` |  `[DeleteAppCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteApp(request)
    
    
    public deleteApp(request: google.cloud.ces.v1.IDeleteAppRequest): Promise<google.longrunning.Operation>;

Calls DeleteApp.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAppRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ideleteapprequest)`   
DeleteAppRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.operation)>` | Promise  
  
### deleteAppVersion(request, callback)
    
    
    public deleteAppVersion(request: google.cloud.ces.v1.IDeleteAppVersionRequest, callback: google.cloud.ces.v1.AgentService.DeleteAppVersionCallback): void;

Calls DeleteAppVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAppVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ideleteappversionrequest)`   
DeleteAppVersionRequest message or plain object  
`callback` |  `[DeleteAppVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAppVersion(request)
    
    
    public deleteAppVersion(request: google.cloud.ces.v1.IDeleteAppVersionRequest): Promise<google.protobuf.Empty>;

Calls DeleteAppVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAppVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ideleteappversionrequest)`   
DeleteAppVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.empty)>` | Promise  
  
### deleteConversation(request, callback)
    
    
    public deleteConversation(request: google.cloud.ces.v1.IDeleteConversationRequest, callback: google.cloud.ces.v1.AgentService.DeleteConversationCallback): void;

Calls DeleteConversation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ideleteconversationrequest)`   
DeleteConversationRequest message or plain object  
`callback` |  `[DeleteConversationCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConversation(request)
    
    
    public deleteConversation(request: google.cloud.ces.v1.IDeleteConversationRequest): Promise<google.protobuf.Empty>;

Calls DeleteConversation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ideleteconversationrequest)`   
DeleteConversationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.empty)>` | Promise  
  
### deleteDeployment(request, callback)
    
    
    public deleteDeployment(request: google.cloud.ces.v1.IDeleteDeploymentRequest, callback: google.cloud.ces.v1.AgentService.DeleteDeploymentCallback): void;

Calls DeleteDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ideletedeploymentrequest)`   
DeleteDeploymentRequest message or plain object  
`callback` |  `[DeleteDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDeployment(request)
    
    
    public deleteDeployment(request: google.cloud.ces.v1.IDeleteDeploymentRequest): Promise<google.protobuf.Empty>;

Calls DeleteDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ideletedeploymentrequest)`   
DeleteDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.empty)>` | Promise  
  
### deleteExample(request, callback)
    
    
    public deleteExample(request: google.cloud.ces.v1.IDeleteExampleRequest, callback: google.cloud.ces.v1.AgentService.DeleteExampleCallback): void;

Calls DeleteExample.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteExampleRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ideleteexamplerequest)`   
DeleteExampleRequest message or plain object  
`callback` |  `[DeleteExampleCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteExample(request)
    
    
    public deleteExample(request: google.cloud.ces.v1.IDeleteExampleRequest): Promise<google.protobuf.Empty>;

Calls DeleteExample.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteExampleRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ideleteexamplerequest)`   
DeleteExampleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.empty)>` | Promise  
  
### deleteGuardrail(request, callback)
    
    
    public deleteGuardrail(request: google.cloud.ces.v1.IDeleteGuardrailRequest, callback: google.cloud.ces.v1.AgentService.DeleteGuardrailCallback): void;

Calls DeleteGuardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGuardrailRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ideleteguardrailrequest)`   
DeleteGuardrailRequest message or plain object  
`callback` |  `[DeleteGuardrailCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteGuardrail(request)
    
    
    public deleteGuardrail(request: google.cloud.ces.v1.IDeleteGuardrailRequest): Promise<google.protobuf.Empty>;

Calls DeleteGuardrail.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGuardrailRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ideleteguardrailrequest)`   
DeleteGuardrailRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.empty)>` | Promise  
  
### deleteTool(request, callback)
    
    
    public deleteTool(request: google.cloud.ces.v1.IDeleteToolRequest, callback: google.cloud.ces.v1.AgentService.DeleteToolCallback): void;

Calls DeleteTool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ideletetoolrequest)`   
DeleteToolRequest message or plain object  
`callback` |  `[DeleteToolCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTool(request)
    
    
    public deleteTool(request: google.cloud.ces.v1.IDeleteToolRequest): Promise<google.protobuf.Empty>;

Calls DeleteTool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ideletetoolrequest)`   
DeleteToolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.empty)>` | Promise  
  
### deleteToolset(request, callback)
    
    
    public deleteToolset(request: google.cloud.ces.v1.IDeleteToolsetRequest, callback: google.cloud.ces.v1.AgentService.DeleteToolsetCallback): void;

Calls DeleteToolset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteToolsetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ideletetoolsetrequest)`   
DeleteToolsetRequest message or plain object  
`callback` |  `[DeleteToolsetCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteToolset(request)
    
    
    public deleteToolset(request: google.cloud.ces.v1.IDeleteToolsetRequest): Promise<google.protobuf.Empty>;

Calls DeleteToolset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteToolsetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ideletetoolsetrequest)`   
DeleteToolsetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.protobuf.empty)>` | Promise  
  
### exportApp(request, callback)
    
    
    public exportApp(request: google.cloud.ces.v1.IExportAppRequest, callback: google.cloud.ces.v1.AgentService.ExportAppCallback): void;

Calls ExportApp.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportAppRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iexportapprequest)`   
ExportAppRequest message or plain object  
`callback` |  `[ExportAppCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportApp(request)
    
    
    public exportApp(request: google.cloud.ces.v1.IExportAppRequest): Promise<google.longrunning.Operation>;

Calls ExportApp.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportAppRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iexportapprequest)`   
ExportAppRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.operation)>` | Promise  
  
### getAgent(request, callback)
    
    
    public getAgent(request: google.cloud.ces.v1.IGetAgentRequest, callback: google.cloud.ces.v1.AgentService.GetAgentCallback): void;

Calls GetAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.igetagentrequest)`   
GetAgentRequest message or plain object  
`callback` |  `[GetAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Agent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAgent(request)
    
    
    public getAgent(request: google.cloud.ces.v1.IGetAgentRequest): Promise<google.cloud.ces.v1.Agent>;

Calls GetAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.igetagentrequest)`   
GetAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.Agent](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.agent-class)>` | Promise  
  
### getApp(request, callback)
    
    
    public getApp(request: google.cloud.ces.v1.IGetAppRequest, callback: google.cloud.ces.v1.AgentService.GetAppCallback): void;

Calls GetApp.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAppRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.igetapprequest)`   
GetAppRequest message or plain object  
`callback` |  `[GetAppCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and App  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getApp(request)
    
    
    public getApp(request: google.cloud.ces.v1.IGetAppRequest): Promise<google.cloud.ces.v1.App>;

Calls GetApp.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAppRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.igetapprequest)`   
GetAppRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.App](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.app-class)>` | Promise  
  
### getAppVersion(request, callback)
    
    
    public getAppVersion(request: google.cloud.ces.v1.IGetAppVersionRequest, callback: google.cloud.ces.v1.AgentService.GetAppVersionCallback): void;

Calls GetAppVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAppVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.igetappversionrequest)`   
GetAppVersionRequest message or plain object  
`callback` |  `[GetAppVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and AppVersion  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAppVersion(request)
    
    
    public getAppVersion(request: google.cloud.ces.v1.IGetAppVersionRequest): Promise<google.cloud.ces.v1.AppVersion>;

Calls GetAppVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAppVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.igetappversionrequest)`   
GetAppVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.AppVersion](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.appversion)>` | Promise  
  
### getChangelog(request, callback)
    
    
    public getChangelog(request: google.cloud.ces.v1.IGetChangelogRequest, callback: google.cloud.ces.v1.AgentService.GetChangelogCallback): void;

Calls GetChangelog.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetChangelogRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.igetchangelogrequest)`   
GetChangelogRequest message or plain object  
`callback` |  `[GetChangelogCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Changelog  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getChangelog(request)
    
    
    public getChangelog(request: google.cloud.ces.v1.IGetChangelogRequest): Promise<google.cloud.ces.v1.Changelog>;

Calls GetChangelog.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetChangelogRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.igetchangelogrequest)`   
GetChangelogRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.Changelog](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.changelog)>` | Promise  
  
### getConversation(request, callback)
    
    
    public getConversation(request: google.cloud.ces.v1.IGetConversationRequest, callback: google.cloud.ces.v1.AgentService.GetConversationCallback): void;

Calls GetConversation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.igetconversationrequest)`   
GetConversationRequest message or plain object  
`callback` |  `[GetConversationCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Conversation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConversation(request)
    
    
    public getConversation(request: google.cloud.ces.v1.IGetConversationRequest): Promise<google.cloud.ces.v1.Conversation>;

Calls GetConversation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConversationRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.igetconversationrequest)`   
GetConversationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.Conversation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.conversation-class)>` | Promise  
  
### getDeployment(request, callback)
    
    
    public getDeployment(request: google.cloud.ces.v1.IGetDeploymentRequest, callback: google.cloud.ces.v1.AgentService.GetDeploymentCallback): void;

Calls GetDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.igetdeploymentrequest)`   
GetDeploymentRequest message or plain object  
`callback` |  `[GetDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Deployment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDeployment(request)
    
    
    public getDeployment(request: google.cloud.ces.v1.IGetDeploymentRequest): Promise<google.cloud.ces.v1.Deployment>;

Calls GetDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.igetdeploymentrequest)`   
GetDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.Deployment](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.deployment)>` | Promise  
  
### getExample(request, callback)
    
    
    public getExample(request: google.cloud.ces.v1.IGetExampleRequest, callback: google.cloud.ces.v1.AgentService.GetExampleCallback): void;

Calls GetExample.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetExampleRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.igetexamplerequest)`   
GetExampleRequest message or plain object  
`callback` |  `[GetExampleCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Example  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getExample(request)
    
    
    public getExample(request: google.cloud.ces.v1.IGetExampleRequest): Promise<google.cloud.ces.v1.Example>;

Calls GetExample.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetExampleRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.igetexamplerequest)`   
GetExampleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.Example](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.example)>` | Promise  
  
### getGuardrail(request, callback)
    
    
    public getGuardrail(request: google.cloud.ces.v1.IGetGuardrailRequest, callback: google.cloud.ces.v1.AgentService.GetGuardrailCallback): void;

Calls GetGuardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetGuardrailRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.igetguardrailrequest)`   
GetGuardrailRequest message or plain object  
`callback` |  `[GetGuardrailCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Guardrail  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getGuardrail(request)
    
    
    public getGuardrail(request: google.cloud.ces.v1.IGetGuardrailRequest): Promise<google.cloud.ces.v1.Guardrail>;

Calls GetGuardrail.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetGuardrailRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.igetguardrailrequest)`   
GetGuardrailRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.Guardrail](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.guardrail-class)>` | Promise  
  
### getTool(request, callback)
    
    
    public getTool(request: google.cloud.ces.v1.IGetToolRequest, callback: google.cloud.ces.v1.AgentService.GetToolCallback): void;

Calls GetTool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.igettoolrequest)`   
GetToolRequest message or plain object  
`callback` |  `[GetToolCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Tool  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTool(request)
    
    
    public getTool(request: google.cloud.ces.v1.IGetToolRequest): Promise<google.cloud.ces.v1.Tool>;

Calls GetTool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.igettoolrequest)`   
GetToolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.Tool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.tool)>` | Promise  
  
### getToolset(request, callback)
    
    
    public getToolset(request: google.cloud.ces.v1.IGetToolsetRequest, callback: google.cloud.ces.v1.AgentService.GetToolsetCallback): void;

Calls GetToolset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetToolsetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.igettoolsetrequest)`   
GetToolsetRequest message or plain object  
`callback` |  `[GetToolsetCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Toolset  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getToolset(request)
    
    
    public getToolset(request: google.cloud.ces.v1.IGetToolsetRequest): Promise<google.cloud.ces.v1.Toolset>;

Calls GetToolset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetToolsetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.igettoolsetrequest)`   
GetToolsetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.Toolset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.toolset)>` | Promise  
  
### importApp(request, callback)
    
    
    public importApp(request: google.cloud.ces.v1.IImportAppRequest, callback: google.cloud.ces.v1.AgentService.ImportAppCallback): void;

Calls ImportApp.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportAppRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iimportapprequest)`   
ImportAppRequest message or plain object  
`callback` |  `[ImportAppCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importApp(request)
    
    
    public importApp(request: google.cloud.ces.v1.IImportAppRequest): Promise<google.longrunning.Operation>;

Calls ImportApp.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportAppRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iimportapprequest)`   
ImportAppRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.operation)>` | Promise  
  
### listAgents(request, callback)
    
    
    public listAgents(request: google.cloud.ces.v1.IListAgentsRequest, callback: google.cloud.ces.v1.AgentService.ListAgentsCallback): void;

Calls ListAgents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ilistagentsrequest)`   
ListAgentsRequest message or plain object  
`callback` |  `[ListAgentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAgentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAgents(request)
    
    
    public listAgents(request: google.cloud.ces.v1.IListAgentsRequest): Promise<google.cloud.ces.v1.ListAgentsResponse>;

Calls ListAgents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ilistagentsrequest)`   
ListAgentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.ListAgentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.listagentsresponse)>` | Promise  
  
### listApps(request, callback)
    
    
    public listApps(request: google.cloud.ces.v1.IListAppsRequest, callback: google.cloud.ces.v1.AgentService.ListAppsCallback): void;

Calls ListApps.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAppsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ilistappsrequest)`   
ListAppsRequest message or plain object  
`callback` |  `[ListAppsCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAppsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listApps(request)
    
    
    public listApps(request: google.cloud.ces.v1.IListAppsRequest): Promise<google.cloud.ces.v1.ListAppsResponse>;

Calls ListApps.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAppsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ilistappsrequest)`   
ListAppsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.ListAppsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.listappsresponse)>` | Promise  
  
### listAppVersions(request, callback)
    
    
    public listAppVersions(request: google.cloud.ces.v1.IListAppVersionsRequest, callback: google.cloud.ces.v1.AgentService.ListAppVersionsCallback): void;

Calls ListAppVersions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAppVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ilistappversionsrequest)`   
ListAppVersionsRequest message or plain object  
`callback` |  `[ListAppVersionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAppVersionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAppVersions(request)
    
    
    public listAppVersions(request: google.cloud.ces.v1.IListAppVersionsRequest): Promise<google.cloud.ces.v1.ListAppVersionsResponse>;

Calls ListAppVersions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAppVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ilistappversionsrequest)`   
ListAppVersionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.ListAppVersionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.listappversionsresponse)>` | Promise  
  
### listChangelogs(request, callback)
    
    
    public listChangelogs(request: google.cloud.ces.v1.IListChangelogsRequest, callback: google.cloud.ces.v1.AgentService.ListChangelogsCallback): void;

Calls ListChangelogs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListChangelogsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ilistchangelogsrequest)`   
ListChangelogsRequest message or plain object  
`callback` |  `[ListChangelogsCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and ListChangelogsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listChangelogs(request)
    
    
    public listChangelogs(request: google.cloud.ces.v1.IListChangelogsRequest): Promise<google.cloud.ces.v1.ListChangelogsResponse>;

Calls ListChangelogs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListChangelogsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ilistchangelogsrequest)`   
ListChangelogsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.ListChangelogsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.listchangelogsresponse)>` | Promise  
  
### listConversations(request, callback)
    
    
    public listConversations(request: google.cloud.ces.v1.IListConversationsRequest, callback: google.cloud.ces.v1.AgentService.ListConversationsCallback): void;

Calls ListConversations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ilistconversationsrequest)`   
ListConversationsRequest message or plain object  
`callback` |  `[ListConversationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and ListConversationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConversations(request)
    
    
    public listConversations(request: google.cloud.ces.v1.IListConversationsRequest): Promise<google.cloud.ces.v1.ListConversationsResponse>;

Calls ListConversations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListConversationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ilistconversationsrequest)`   
ListConversationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.ListConversationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.listconversationsresponse)>` | Promise  
  
### listDeployments(request, callback)
    
    
    public listDeployments(request: google.cloud.ces.v1.IListDeploymentsRequest, callback: google.cloud.ces.v1.AgentService.ListDeploymentsCallback): void;

Calls ListDeployments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDeploymentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ilistdeploymentsrequest)`   
ListDeploymentsRequest message or plain object  
`callback` |  `[ListDeploymentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDeploymentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDeployments(request)
    
    
    public listDeployments(request: google.cloud.ces.v1.IListDeploymentsRequest): Promise<google.cloud.ces.v1.ListDeploymentsResponse>;

Calls ListDeployments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDeploymentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ilistdeploymentsrequest)`   
ListDeploymentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.ListDeploymentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.listdeploymentsresponse)>` | Promise  
  
### listExamples(request, callback)
    
    
    public listExamples(request: google.cloud.ces.v1.IListExamplesRequest, callback: google.cloud.ces.v1.AgentService.ListExamplesCallback): void;

Calls ListExamples.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListExamplesRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ilistexamplesrequest)`   
ListExamplesRequest message or plain object  
`callback` |  `[ListExamplesCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and ListExamplesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listExamples(request)
    
    
    public listExamples(request: google.cloud.ces.v1.IListExamplesRequest): Promise<google.cloud.ces.v1.ListExamplesResponse>;

Calls ListExamples.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListExamplesRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ilistexamplesrequest)`   
ListExamplesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.ListExamplesResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.listexamplesresponse)>` | Promise  
  
### listGuardrails(request, callback)
    
    
    public listGuardrails(request: google.cloud.ces.v1.IListGuardrailsRequest, callback: google.cloud.ces.v1.AgentService.ListGuardrailsCallback): void;

Calls ListGuardrails.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGuardrailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ilistguardrailsrequest)`   
ListGuardrailsRequest message or plain object  
`callback` |  `[ListGuardrailsCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and ListGuardrailsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listGuardrails(request)
    
    
    public listGuardrails(request: google.cloud.ces.v1.IListGuardrailsRequest): Promise<google.cloud.ces.v1.ListGuardrailsResponse>;

Calls ListGuardrails.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListGuardrailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ilistguardrailsrequest)`   
ListGuardrailsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.ListGuardrailsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.listguardrailsresponse)>` | Promise  
  
### listTools(request, callback)
    
    
    public listTools(request: google.cloud.ces.v1.IListToolsRequest, callback: google.cloud.ces.v1.AgentService.ListToolsCallback): void;

Calls ListTools.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListToolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ilisttoolsrequest)`   
ListToolsRequest message or plain object  
`callback` |  `[ListToolsCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and ListToolsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTools(request)
    
    
    public listTools(request: google.cloud.ces.v1.IListToolsRequest): Promise<google.cloud.ces.v1.ListToolsResponse>;

Calls ListTools.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListToolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ilisttoolsrequest)`   
ListToolsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.ListToolsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.listtoolsresponse)>` | Promise  
  
### listToolsets(request, callback)
    
    
    public listToolsets(request: google.cloud.ces.v1.IListToolsetsRequest, callback: google.cloud.ces.v1.AgentService.ListToolsetsCallback): void;

Calls ListToolsets.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListToolsetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ilisttoolsetsrequest)`   
ListToolsetsRequest message or plain object  
`callback` |  `[ListToolsetsCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and ListToolsetsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listToolsets(request)
    
    
    public listToolsets(request: google.cloud.ces.v1.IListToolsetsRequest): Promise<google.cloud.ces.v1.ListToolsetsResponse>;

Calls ListToolsets.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListToolsetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ilisttoolsetsrequest)`   
ListToolsetsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.ListToolsetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.listtoolsetsresponse)>` | Promise  
  
### restoreAppVersion(request, callback)
    
    
    public restoreAppVersion(request: google.cloud.ces.v1.IRestoreAppVersionRequest, callback: google.cloud.ces.v1.AgentService.RestoreAppVersionCallback): void;

Calls RestoreAppVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRestoreAppVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.irestoreappversionrequest)`   
RestoreAppVersionRequest message or plain object  
`callback` |  `[RestoreAppVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### restoreAppVersion(request)
    
    
    public restoreAppVersion(request: google.cloud.ces.v1.IRestoreAppVersionRequest): Promise<google.longrunning.Operation>;

Calls RestoreAppVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRestoreAppVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.irestoreappversionrequest)`   
RestoreAppVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.longrunning.operation)>` | Promise  
  
### updateAgent(request, callback)
    
    
    public updateAgent(request: google.cloud.ces.v1.IUpdateAgentRequest, callback: google.cloud.ces.v1.AgentService.UpdateAgentCallback): void;

Calls UpdateAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iupdateagentrequest)`   
UpdateAgentRequest message or plain object  
`callback` |  `[UpdateAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Agent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAgent(request)
    
    
    public updateAgent(request: google.cloud.ces.v1.IUpdateAgentRequest): Promise<google.cloud.ces.v1.Agent>;

Calls UpdateAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iupdateagentrequest)`   
UpdateAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.Agent](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.agent-class)>` | Promise  
  
### updateApp(request, callback)
    
    
    public updateApp(request: google.cloud.ces.v1.IUpdateAppRequest, callback: google.cloud.ces.v1.AgentService.UpdateAppCallback): void;

Calls UpdateApp.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAppRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iupdateapprequest)`   
UpdateAppRequest message or plain object  
`callback` |  `[UpdateAppCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and App  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateApp(request)
    
    
    public updateApp(request: google.cloud.ces.v1.IUpdateAppRequest): Promise<google.cloud.ces.v1.App>;

Calls UpdateApp.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAppRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iupdateapprequest)`   
UpdateAppRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.App](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.app-class)>` | Promise  
  
### updateDeployment(request, callback)
    
    
    public updateDeployment(request: google.cloud.ces.v1.IUpdateDeploymentRequest, callback: google.cloud.ces.v1.AgentService.UpdateDeploymentCallback): void;

Calls UpdateDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iupdatedeploymentrequest)`   
UpdateDeploymentRequest message or plain object  
`callback` |  `[UpdateDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Deployment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDeployment(request)
    
    
    public updateDeployment(request: google.cloud.ces.v1.IUpdateDeploymentRequest): Promise<google.cloud.ces.v1.Deployment>;

Calls UpdateDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iupdatedeploymentrequest)`   
UpdateDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.Deployment](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.deployment)>` | Promise  
  
### updateExample(request, callback)
    
    
    public updateExample(request: google.cloud.ces.v1.IUpdateExampleRequest, callback: google.cloud.ces.v1.AgentService.UpdateExampleCallback): void;

Calls UpdateExample.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateExampleRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iupdateexamplerequest)`   
UpdateExampleRequest message or plain object  
`callback` |  `[UpdateExampleCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Example  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateExample(request)
    
    
    public updateExample(request: google.cloud.ces.v1.IUpdateExampleRequest): Promise<google.cloud.ces.v1.Example>;

Calls UpdateExample.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateExampleRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iupdateexamplerequest)`   
UpdateExampleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.Example](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.example)>` | Promise  
  
### updateGuardrail(request, callback)
    
    
    public updateGuardrail(request: google.cloud.ces.v1.IUpdateGuardrailRequest, callback: google.cloud.ces.v1.AgentService.UpdateGuardrailCallback): void;

Calls UpdateGuardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGuardrailRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iupdateguardrailrequest)`   
UpdateGuardrailRequest message or plain object  
`callback` |  `[UpdateGuardrailCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Guardrail  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateGuardrail(request)
    
    
    public updateGuardrail(request: google.cloud.ces.v1.IUpdateGuardrailRequest): Promise<google.cloud.ces.v1.Guardrail>;

Calls UpdateGuardrail.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGuardrailRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iupdateguardrailrequest)`   
UpdateGuardrailRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.Guardrail](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.guardrail-class)>` | Promise  
  
### updateTool(request, callback)
    
    
    public updateTool(request: google.cloud.ces.v1.IUpdateToolRequest, callback: google.cloud.ces.v1.AgentService.UpdateToolCallback): void;

Calls UpdateTool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iupdatetoolrequest)`   
UpdateToolRequest message or plain object  
`callback` |  `[UpdateToolCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Tool  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTool(request)
    
    
    public updateTool(request: google.cloud.ces.v1.IUpdateToolRequest): Promise<google.cloud.ces.v1.Tool>;

Calls UpdateTool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iupdatetoolrequest)`   
UpdateToolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.Tool](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.tool)>` | Promise  
  
### updateToolset(request, callback)
    
    
    public updateToolset(request: google.cloud.ces.v1.IUpdateToolsetRequest, callback: google.cloud.ces.v1.AgentService.UpdateToolsetCallback): void;

Calls UpdateToolset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateToolsetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iupdatetoolsetrequest)`   
UpdateToolsetRequest message or plain object  
`callback` |  `[UpdateToolsetCallback](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)`   
Node-style callback called with the error, if any, and Toolset  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateToolset(request)
    
    
    public updateToolset(request: google.cloud.ces.v1.IUpdateToolsetRequest): Promise<google.cloud.ces.v1.Toolset>;

Calls UpdateToolset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateToolsetRequest](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iupdatetoolsetrequest)`   
UpdateToolsetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.ces.v1.Toolset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.toolset)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
