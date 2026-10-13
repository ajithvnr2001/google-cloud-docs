---
url: https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.operations-class
title: Class protos.google.longrunning.Operations (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:32:46.811588+00:00
---

# Class protos.google.longrunning.Operations (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.operations-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.longrunning.Operations (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  2.3.2  2.1.4  1.5.1  1.4.7 

Represents an Operations

## Inheritance

$protobuf.rpc.Service > protos.google.longrunning.Operations

## Package

[@google-cloud/memcache](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Operations service.

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

### cancelOperation(request, callback)
    
    
    public cancelOperation(request: google.longrunning.ICancelOperationRequest, callback: google.longrunning.Operations.CancelOperationCallback): void;

Calls CancelOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.icanceloperationrequest)`   
CancelOperationRequest message or plain object  
`callback` |  `[CancelOperationCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelOperation(request)
    
    
    public cancelOperation(request: google.longrunning.ICancelOperationRequest): Promise<google.protobuf.Empty>;

Calls CancelOperation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.icanceloperationrequest)`   
CancelOperationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.protobuf.empty)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Operations;

Creates new Operations service using the specified rpc implementation.

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
`[Operations](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.operations-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### deleteOperation(request, callback)
    
    
    public deleteOperation(request: google.longrunning.IDeleteOperationRequest, callback: google.longrunning.Operations.DeleteOperationCallback): void;

Calls DeleteOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.ideleteoperationrequest)`   
DeleteOperationRequest message or plain object  
`callback` |  `[DeleteOperationCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteOperation(request)
    
    
    public deleteOperation(request: google.longrunning.IDeleteOperationRequest): Promise<google.protobuf.Empty>;

Calls DeleteOperation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.ideleteoperationrequest)`   
DeleteOperationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.protobuf.empty)>` | Promise  
  
### getOperation(request, callback)
    
    
    public getOperation(request: google.longrunning.IGetOperationRequest, callback: google.longrunning.Operations.GetOperationCallback): void;

Calls GetOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.igetoperationrequest)`   
GetOperationRequest message or plain object  
`callback` |  `[GetOperationCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getOperation(request)
    
    
    public getOperation(request: google.longrunning.IGetOperationRequest): Promise<google.longrunning.Operation>;

Calls GetOperation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.igetoperationrequest)`   
GetOperationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.operation)>` | Promise  
  
### listOperations(request, callback)
    
    
    public listOperations(request: google.longrunning.IListOperationsRequest, callback: google.longrunning.Operations.ListOperationsCallback): void;

Calls ListOperations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.ilistoperationsrequest)`   
ListOperationsRequest message or plain object  
`callback` |  `[ListOperationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and ListOperationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listOperations(request)
    
    
    public listOperations(request: google.longrunning.IListOperationsRequest): Promise<google.longrunning.ListOperationsResponse>;

Calls ListOperations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.ilistoperationsrequest)`   
ListOperationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.ListOperationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.listoperationsresponse)>` | Promise  
  
### waitOperation(request, callback)
    
    
    public waitOperation(request: google.longrunning.IWaitOperationRequest, callback: google.longrunning.Operations.WaitOperationCallback): void;

Calls WaitOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IWaitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.iwaitoperationrequest)`   
WaitOperationRequest message or plain object  
`callback` |  `[WaitOperationCallback](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### waitOperation(request)
    
    
    public waitOperation(request: google.longrunning.IWaitOperationRequest): Promise<google.longrunning.Operation>;

Calls WaitOperation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IWaitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.iwaitoperationrequest)`   
WaitOperationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/memcache/latest/memcache/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
