---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.contexts-class
title: Class protos.google.cloud.dialogflow.v2.Contexts (8.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:59:33.639915+00:00
---

# Class protos.google.cloud.dialogflow.v2.Contexts (8.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.contexts-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.v2.Contexts (8.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

8.2.0 (latest)  8.1.1  7.9.0  7.8.0  7.7.0  7.5.0  7.4.0  7.1.0  7.0.1  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.8.0  6.6.0  6.4.0  6.3.1  6.2.0  6.0.0  5.7.1  5.6.0  5.5.1  5.3.0  5.2.1  4.7.0  4.6.0  4.5.0  4.4.0  4.3.1  4.2.0  4.1.4  3.5.0  3.3.0 

Represents a Contexts

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dialogflow.v2.Contexts

## Package

[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Contexts service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Contexts;

Creates new Contexts service using the specified rpc implementation.

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
`[Contexts](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.contexts-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createContext(request, callback)
    
    
    public createContext(request: google.cloud.dialogflow.v2.ICreateContextRequest, callback: google.cloud.dialogflow.v2.Contexts.CreateContextCallback): void;

Calls CreateContext.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateContextRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.icreatecontextrequest)`   
CreateContextRequest message or plain object  
`callback` |  `[CreateContextCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Context  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createContext(request)
    
    
    public createContext(request: google.cloud.dialogflow.v2.ICreateContextRequest): Promise<google.cloud.dialogflow.v2.Context>;

Calls CreateContext.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateContextRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.icreatecontextrequest)`   
CreateContextRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.Context](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.context)>` | Promise  
  
### deleteAllContexts(request, callback)
    
    
    public deleteAllContexts(request: google.cloud.dialogflow.v2.IDeleteAllContextsRequest, callback: google.cloud.dialogflow.v2.Contexts.DeleteAllContextsCallback): void;

Calls DeleteAllContexts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAllContextsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ideleteallcontextsrequest)`   
DeleteAllContextsRequest message or plain object  
`callback` |  `[DeleteAllContextsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAllContexts(request)
    
    
    public deleteAllContexts(request: google.cloud.dialogflow.v2.IDeleteAllContextsRequest): Promise<google.protobuf.Empty>;

Calls DeleteAllContexts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAllContextsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ideleteallcontextsrequest)`   
DeleteAllContextsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.protobuf.empty)>` | Promise  
  
### deleteContext(request, callback)
    
    
    public deleteContext(request: google.cloud.dialogflow.v2.IDeleteContextRequest, callback: google.cloud.dialogflow.v2.Contexts.DeleteContextCallback): void;

Calls DeleteContext.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteContextRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ideletecontextrequest)`   
DeleteContextRequest message or plain object  
`callback` |  `[DeleteContextCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteContext(request)
    
    
    public deleteContext(request: google.cloud.dialogflow.v2.IDeleteContextRequest): Promise<google.protobuf.Empty>;

Calls DeleteContext.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteContextRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ideletecontextrequest)`   
DeleteContextRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.protobuf.empty)>` | Promise  
  
### getContext(request, callback)
    
    
    public getContext(request: google.cloud.dialogflow.v2.IGetContextRequest, callback: google.cloud.dialogflow.v2.Contexts.GetContextCallback): void;

Calls GetContext.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetContextRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetcontextrequest)`   
GetContextRequest message or plain object  
`callback` |  `[GetContextCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Context  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getContext(request)
    
    
    public getContext(request: google.cloud.dialogflow.v2.IGetContextRequest): Promise<google.cloud.dialogflow.v2.Context>;

Calls GetContext.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetContextRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetcontextrequest)`   
GetContextRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.Context](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.context)>` | Promise  
  
### listContexts(request, callback)
    
    
    public listContexts(request: google.cloud.dialogflow.v2.IListContextsRequest, callback: google.cloud.dialogflow.v2.Contexts.ListContextsCallback): void;

Calls ListContexts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListContextsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistcontextsrequest)`   
ListContextsRequest message or plain object  
`callback` |  `[ListContextsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and ListContextsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listContexts(request)
    
    
    public listContexts(request: google.cloud.dialogflow.v2.IListContextsRequest): Promise<google.cloud.dialogflow.v2.ListContextsResponse>;

Calls ListContexts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListContextsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistcontextsrequest)`   
ListContextsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.ListContextsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.listcontextsresponse)>` | Promise  
  
### updateContext(request, callback)
    
    
    public updateContext(request: google.cloud.dialogflow.v2.IUpdateContextRequest, callback: google.cloud.dialogflow.v2.Contexts.UpdateContextCallback): void;

Calls UpdateContext.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateContextRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iupdatecontextrequest)`   
UpdateContextRequest message or plain object  
`callback` |  `[UpdateContextCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Context  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateContext(request)
    
    
    public updateContext(request: google.cloud.dialogflow.v2.IUpdateContextRequest): Promise<google.cloud.dialogflow.v2.Context>;

Calls UpdateContext.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateContextRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iupdatecontextrequest)`   
UpdateContextRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.Context](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.context)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
