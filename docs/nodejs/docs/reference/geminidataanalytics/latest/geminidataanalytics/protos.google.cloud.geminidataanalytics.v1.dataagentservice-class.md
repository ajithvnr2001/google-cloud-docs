---
url: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.dataagentservice-class
title: Class protos.google.cloud.geminidataanalytics.v1.DataAgentService (0.13.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:37:37.568996+00:00
---

# Class protos.google.cloud.geminidataanalytics.v1.DataAgentService (0.13.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.dataagentservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.geminidataanalytics.v1.DataAgentService (0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.13.0  0.7.0  0.6.0  0.4.0  0.2.0 

Represents a DataAgentService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.geminidataanalytics.v1.DataAgentService

## Package

[@google-cloud/geminidataanalytics](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DataAgentService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DataAgentService;

Creates new DataAgentService service using the specified rpc implementation.

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
`[DataAgentService](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.dataagentservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createDataAgent(request, callback)
    
    
    public createDataAgent(request: google.cloud.geminidataanalytics.v1.ICreateDataAgentRequest, callback: google.cloud.geminidataanalytics.v1.DataAgentService.CreateDataAgentCallback): void;

Calls CreateDataAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.icreatedataagentrequest)`   
CreateDataAgentRequest message or plain object  
`callback` |  `[CreateDataAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataAgent(request)
    
    
    public createDataAgent(request: google.cloud.geminidataanalytics.v1.ICreateDataAgentRequest): Promise<google.longrunning.Operation>;

Calls CreateDataAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.icreatedataagentrequest)`   
CreateDataAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.operation)>` | Promise  
  
### createDataAgentSync(request, callback)
    
    
    public createDataAgentSync(request: google.cloud.geminidataanalytics.v1.ICreateDataAgentRequest, callback: google.cloud.geminidataanalytics.v1.DataAgentService.CreateDataAgentSyncCallback): void;

Calls CreateDataAgentSync.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.icreatedataagentrequest)`   
CreateDataAgentRequest message or plain object  
`callback` |  `[CreateDataAgentSyncCallback](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)`   
Node-style callback called with the error, if any, and DataAgent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataAgentSync(request)
    
    
    public createDataAgentSync(request: google.cloud.geminidataanalytics.v1.ICreateDataAgentRequest): Promise<google.cloud.geminidataanalytics.v1.DataAgent>;

Calls CreateDataAgentSync.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.icreatedataagentrequest)`   
CreateDataAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.geminidataanalytics.v1.DataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.dataagent)>` | Promise  
  
### deleteDataAgent(request, callback)
    
    
    public deleteDataAgent(request: google.cloud.geminidataanalytics.v1.IDeleteDataAgentRequest, callback: google.cloud.geminidataanalytics.v1.DataAgentService.DeleteDataAgentCallback): void;

Calls DeleteDataAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.ideletedataagentrequest)`   
DeleteDataAgentRequest message or plain object  
`callback` |  `[DeleteDataAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataAgent(request)
    
    
    public deleteDataAgent(request: google.cloud.geminidataanalytics.v1.IDeleteDataAgentRequest): Promise<google.longrunning.Operation>;

Calls DeleteDataAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.ideletedataagentrequest)`   
DeleteDataAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.operation)>` | Promise  
  
### deleteDataAgentSync(request, callback)
    
    
    public deleteDataAgentSync(request: google.cloud.geminidataanalytics.v1.IDeleteDataAgentRequest, callback: google.cloud.geminidataanalytics.v1.DataAgentService.DeleteDataAgentSyncCallback): void;

Calls DeleteDataAgentSync.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.ideletedataagentrequest)`   
DeleteDataAgentRequest message or plain object  
`callback` |  `[DeleteDataAgentSyncCallback](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataAgentSync(request)
    
    
    public deleteDataAgentSync(request: google.cloud.geminidataanalytics.v1.IDeleteDataAgentRequest): Promise<google.protobuf.Empty>;

Calls DeleteDataAgentSync.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.ideletedataagentrequest)`   
DeleteDataAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.protobuf.empty)>` | Promise  
  
### getDataAgent(request, callback)
    
    
    public getDataAgent(request: google.cloud.geminidataanalytics.v1.IGetDataAgentRequest, callback: google.cloud.geminidataanalytics.v1.DataAgentService.GetDataAgentCallback): void;

Calls GetDataAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.igetdataagentrequest)`   
GetDataAgentRequest message or plain object  
`callback` |  `[GetDataAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)`   
Node-style callback called with the error, if any, and DataAgent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataAgent(request)
    
    
    public getDataAgent(request: google.cloud.geminidataanalytics.v1.IGetDataAgentRequest): Promise<google.cloud.geminidataanalytics.v1.DataAgent>;

Calls GetDataAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.igetdataagentrequest)`   
GetDataAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.geminidataanalytics.v1.DataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.dataagent)>` | Promise  
  
### getIamPolicy(request, callback)
    
    
    public getIamPolicy(request: google.iam.v1.IGetIamPolicyRequest, callback: google.cloud.geminidataanalytics.v1.DataAgentService.GetIamPolicyCallback): void;

Calls GetIamPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.igetiampolicyrequest)`   
GetIamPolicyRequest message or plain object  
`callback` |  `[GetIamPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request)
    
    
    public getIamPolicy(request: google.iam.v1.IGetIamPolicyRequest): Promise<google.iam.v1.Policy>;

Calls GetIamPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.igetiampolicyrequest)`   
GetIamPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.policy)>` | Promise  
  
### listAccessibleDataAgents(request, callback)
    
    
    public listAccessibleDataAgents(request: google.cloud.geminidataanalytics.v1.IListAccessibleDataAgentsRequest, callback: google.cloud.geminidataanalytics.v1.DataAgentService.ListAccessibleDataAgentsCallback): void;

Calls ListAccessibleDataAgents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccessibleDataAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.ilistaccessibledataagentsrequest)`   
ListAccessibleDataAgentsRequest message or plain object  
`callback` |  `[ListAccessibleDataAgentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAccessibleDataAgentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAccessibleDataAgents(request)
    
    
    public listAccessibleDataAgents(request: google.cloud.geminidataanalytics.v1.IListAccessibleDataAgentsRequest): Promise<google.cloud.geminidataanalytics.v1.ListAccessibleDataAgentsResponse>;

Calls ListAccessibleDataAgents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAccessibleDataAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.ilistaccessibledataagentsrequest)`   
ListAccessibleDataAgentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.geminidataanalytics.v1.ListAccessibleDataAgentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.listaccessibledataagentsresponse)>` | Promise  
  
### listDataAgents(request, callback)
    
    
    public listDataAgents(request: google.cloud.geminidataanalytics.v1.IListDataAgentsRequest, callback: google.cloud.geminidataanalytics.v1.DataAgentService.ListDataAgentsCallback): void;

Calls ListDataAgents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.ilistdataagentsrequest)`   
ListDataAgentsRequest message or plain object  
`callback` |  `[ListDataAgentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDataAgentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataAgents(request)
    
    
    public listDataAgents(request: google.cloud.geminidataanalytics.v1.IListDataAgentsRequest): Promise<google.cloud.geminidataanalytics.v1.ListDataAgentsResponse>;

Calls ListDataAgents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDataAgentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.ilistdataagentsrequest)`   
ListDataAgentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.geminidataanalytics.v1.ListDataAgentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.listdataagentsresponse)>` | Promise  
  
### retrieveAgentOpsObservability(request, callback)
    
    
    public retrieveAgentOpsObservability(request: google.cloud.geminidataanalytics.v1.IRetrieveAgentOpsObservabilityRequest, callback: google.cloud.geminidataanalytics.v1.DataAgentService.RetrieveAgentOpsObservabilityCallback): void;

Calls RetrieveAgentOpsObservability.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRetrieveAgentOpsObservabilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.iretrieveagentopsobservabilityrequest)`   
RetrieveAgentOpsObservabilityRequest message or plain object  
`callback` |  `[RetrieveAgentOpsObservabilityCallback](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)`   
Node-style callback called with the error, if any, and RetrieveAgentOpsObservabilityResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### retrieveAgentOpsObservability(request)
    
    
    public retrieveAgentOpsObservability(request: google.cloud.geminidataanalytics.v1.IRetrieveAgentOpsObservabilityRequest): Promise<google.cloud.geminidataanalytics.v1.RetrieveAgentOpsObservabilityResponse>;

Calls RetrieveAgentOpsObservability.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRetrieveAgentOpsObservabilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.iretrieveagentopsobservabilityrequest)`   
RetrieveAgentOpsObservabilityRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.geminidataanalytics.v1.RetrieveAgentOpsObservabilityResponse](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.retrieveagentopsobservabilityresponse)>` | Promise  
  
### setAgentOpsObservability(request, callback)
    
    
    public setAgentOpsObservability(request: google.cloud.geminidataanalytics.v1.ISetAgentOpsObservabilityRequest, callback: google.cloud.geminidataanalytics.v1.DataAgentService.SetAgentOpsObservabilityCallback): void;

Calls SetAgentOpsObservability.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetAgentOpsObservabilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.isetagentopsobservabilityrequest)`   
SetAgentOpsObservabilityRequest message or plain object  
`callback` |  `[SetAgentOpsObservabilityCallback](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setAgentOpsObservability(request)
    
    
    public setAgentOpsObservability(request: google.cloud.geminidataanalytics.v1.ISetAgentOpsObservabilityRequest): Promise<google.longrunning.Operation>;

Calls SetAgentOpsObservability.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetAgentOpsObservabilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.isetagentopsobservabilityrequest)`   
SetAgentOpsObservabilityRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.operation)>` | Promise  
  
### setIamPolicy(request, callback)
    
    
    public setIamPolicy(request: google.iam.v1.ISetIamPolicyRequest, callback: google.cloud.geminidataanalytics.v1.DataAgentService.SetIamPolicyCallback): void;

Calls SetIamPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.isetiampolicyrequest)`   
SetIamPolicyRequest message or plain object  
`callback` |  `[SetIamPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request)
    
    
    public setIamPolicy(request: google.iam.v1.ISetIamPolicyRequest): Promise<google.iam.v1.Policy>;

Calls SetIamPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.isetiampolicyrequest)`   
SetIamPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.iam.v1.policy)>` | Promise  
  
### updateDataAgent(request, callback)
    
    
    public updateDataAgent(request: google.cloud.geminidataanalytics.v1.IUpdateDataAgentRequest, callback: google.cloud.geminidataanalytics.v1.DataAgentService.UpdateDataAgentCallback): void;

Calls UpdateDataAgent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.iupdatedataagentrequest)`   
UpdateDataAgentRequest message or plain object  
`callback` |  `[UpdateDataAgentCallback](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataAgent(request)
    
    
    public updateDataAgent(request: google.cloud.geminidataanalytics.v1.IUpdateDataAgentRequest): Promise<google.longrunning.Operation>;

Calls UpdateDataAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.iupdatedataagentrequest)`   
UpdateDataAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.longrunning.operation)>` | Promise  
  
### updateDataAgentSync(request, callback)
    
    
    public updateDataAgentSync(request: google.cloud.geminidataanalytics.v1.IUpdateDataAgentRequest, callback: google.cloud.geminidataanalytics.v1.DataAgentService.UpdateDataAgentSyncCallback): void;

Calls UpdateDataAgentSync.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.iupdatedataagentrequest)`   
UpdateDataAgentRequest message or plain object  
`callback` |  `[UpdateDataAgentSyncCallback](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/overview.html)`   
Node-style callback called with the error, if any, and DataAgent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataAgentSync(request)
    
    
    public updateDataAgentSync(request: google.cloud.geminidataanalytics.v1.IUpdateDataAgentRequest): Promise<google.cloud.geminidataanalytics.v1.DataAgent>;

Calls UpdateDataAgentSync.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataAgentRequest](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.iupdatedataagentrequest)`   
UpdateDataAgentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.geminidataanalytics.v1.DataAgent](https://docs.cloud.google.com/nodejs/docs/reference/geminidataanalytics/latest/geminidataanalytics/protos.google.cloud.geminidataanalytics.v1.dataagent)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
