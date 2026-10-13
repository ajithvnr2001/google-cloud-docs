---
url: https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.executions-class
title: Class protos.google.cloud.workflows.executions.v1.Executions (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:31:12.522104+00:00
---

# Class protos.google.cloud.workflows.executions.v1.Executions (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.executions-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.workflows.executions.v1.Executions (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  4.3.0  3.1.1  2.3.2  2.2.0  1.4.0  1.3.1  1.2.6 

Represents an Executions

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.workflows.executions.v1.Executions

## Package

[@google-cloud/workflows](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Executions service.

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

### cancelExecution(request, callback)
    
    
    public cancelExecution(request: google.cloud.workflows.executions.v1.ICancelExecutionRequest, callback: google.cloud.workflows.executions.v1.Executions.CancelExecutionCallback): void;

Calls CancelExecution.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelExecutionRequest](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.icancelexecutionrequest)`   
CancelExecutionRequest message or plain object  
`callback` |  `[CancelExecutionCallback](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/overview.html)`   
Node-style callback called with the error, if any, and Execution  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelExecution(request)
    
    
    public cancelExecution(request: google.cloud.workflows.executions.v1.ICancelExecutionRequest): Promise<google.cloud.workflows.executions.v1.Execution>;

Calls CancelExecution.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICancelExecutionRequest](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.icancelexecutionrequest)`   
CancelExecutionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.workflows.executions.v1.Execution](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.execution-class)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Executions;

Creates new Executions service using the specified rpc implementation.

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
`[Executions](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.executions-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createExecution(request, callback)
    
    
    public createExecution(request: google.cloud.workflows.executions.v1.ICreateExecutionRequest, callback: google.cloud.workflows.executions.v1.Executions.CreateExecutionCallback): void;

Calls CreateExecution.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateExecutionRequest](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.icreateexecutionrequest)`   
CreateExecutionRequest message or plain object  
`callback` |  `[CreateExecutionCallback](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/overview.html)`   
Node-style callback called with the error, if any, and Execution  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createExecution(request)
    
    
    public createExecution(request: google.cloud.workflows.executions.v1.ICreateExecutionRequest): Promise<google.cloud.workflows.executions.v1.Execution>;

Calls CreateExecution.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateExecutionRequest](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.icreateexecutionrequest)`   
CreateExecutionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.workflows.executions.v1.Execution](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.execution-class)>` | Promise  
  
### getExecution(request, callback)
    
    
    public getExecution(request: google.cloud.workflows.executions.v1.IGetExecutionRequest, callback: google.cloud.workflows.executions.v1.Executions.GetExecutionCallback): void;

Calls GetExecution.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetExecutionRequest](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.igetexecutionrequest)`   
GetExecutionRequest message or plain object  
`callback` |  `[GetExecutionCallback](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/overview.html)`   
Node-style callback called with the error, if any, and Execution  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getExecution(request)
    
    
    public getExecution(request: google.cloud.workflows.executions.v1.IGetExecutionRequest): Promise<google.cloud.workflows.executions.v1.Execution>;

Calls GetExecution.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetExecutionRequest](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.igetexecutionrequest)`   
GetExecutionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.workflows.executions.v1.Execution](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.execution-class)>` | Promise  
  
### listExecutions(request, callback)
    
    
    public listExecutions(request: google.cloud.workflows.executions.v1.IListExecutionsRequest, callback: google.cloud.workflows.executions.v1.Executions.ListExecutionsCallback): void;

Calls ListExecutions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListExecutionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.ilistexecutionsrequest)`   
ListExecutionsRequest message or plain object  
`callback` |  `[ListExecutionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/overview.html)`   
Node-style callback called with the error, if any, and ListExecutionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listExecutions(request)
    
    
    public listExecutions(request: google.cloud.workflows.executions.v1.IListExecutionsRequest): Promise<google.cloud.workflows.executions.v1.ListExecutionsResponse>;

Calls ListExecutions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListExecutionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.ilistexecutionsrequest)`   
ListExecutionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.workflows.executions.v1.ListExecutionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/workflows/latest/workflows/protos.google.cloud.workflows.executions.v1.listexecutionsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
