---
url: https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.datastore-class
title: Class protos.google.datastore.v1.Datastore (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:47:49.240894+00:00
---

# Class protos.google.datastore.v1.Datastore (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.datastore-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.datastore.v1.Datastore (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a Datastore

## Inheritance

$protobuf.rpc.Service > protos.google.datastore.v1.Datastore

## Package

[@google-cloud/datastore-api](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Datastore service.

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

### allocateIds(request, callback)
    
    
    public allocateIds(request: google.datastore.v1.IAllocateIdsRequest, callback: google.datastore.v1.Datastore.AllocateIdsCallback): void;

Calls AllocateIds.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAllocateIdsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.iallocateidsrequest)`   
AllocateIdsRequest message or plain object  
`callback` |  `[AllocateIdsCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and AllocateIdsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### allocateIds(request)
    
    
    public allocateIds(request: google.datastore.v1.IAllocateIdsRequest): Promise<google.datastore.v1.AllocateIdsResponse>;

Calls AllocateIds.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAllocateIdsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.iallocateidsrequest)`   
AllocateIdsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.datastore.v1.AllocateIdsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.allocateidsresponse)>` | Promise  
  
### beginTransaction(request, callback)
    
    
    public beginTransaction(request: google.datastore.v1.IBeginTransactionRequest, callback: google.datastore.v1.Datastore.BeginTransactionCallback): void;

Calls BeginTransaction.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBeginTransactionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.ibegintransactionrequest)`   
BeginTransactionRequest message or plain object  
`callback` |  `[BeginTransactionCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and BeginTransactionResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### beginTransaction(request)
    
    
    public beginTransaction(request: google.datastore.v1.IBeginTransactionRequest): Promise<google.datastore.v1.BeginTransactionResponse>;

Calls BeginTransaction.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBeginTransactionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.ibegintransactionrequest)`   
BeginTransactionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.datastore.v1.BeginTransactionResponse](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.begintransactionresponse)>` | Promise  
  
### commit(request, callback)
    
    
    public commit(request: google.datastore.v1.ICommitRequest, callback: google.datastore.v1.Datastore.CommitCallback): void;

Calls Commit.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICommitRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.icommitrequest)`   
CommitRequest message or plain object  
`callback` |  `[CommitCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and CommitResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### commit(request)
    
    
    public commit(request: google.datastore.v1.ICommitRequest): Promise<google.datastore.v1.CommitResponse>;

Calls Commit.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICommitRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.icommitrequest)`   
CommitRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.datastore.v1.CommitResponse](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.commitresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Datastore;

Creates new Datastore service using the specified rpc implementation.

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
`[Datastore](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.datastore-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### lookup(request, callback)
    
    
    public lookup(request: google.datastore.v1.ILookupRequest, callback: google.datastore.v1.Datastore.LookupCallback): void;

Calls Lookup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.ilookuprequest)`   
LookupRequest message or plain object  
`callback` |  `[LookupCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and LookupResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### lookup(request)
    
    
    public lookup(request: google.datastore.v1.ILookupRequest): Promise<google.datastore.v1.LookupResponse>;

Calls Lookup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ILookupRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.ilookuprequest)`   
LookupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.datastore.v1.LookupResponse](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.lookupresponse)>` | Promise  
  
### reserveIds(request, callback)
    
    
    public reserveIds(request: google.datastore.v1.IReserveIdsRequest, callback: google.datastore.v1.Datastore.ReserveIdsCallback): void;

Calls ReserveIds.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReserveIdsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.ireserveidsrequest)`   
ReserveIdsRequest message or plain object  
`callback` |  `[ReserveIdsCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and ReserveIdsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### reserveIds(request)
    
    
    public reserveIds(request: google.datastore.v1.IReserveIdsRequest): Promise<google.datastore.v1.ReserveIdsResponse>;

Calls ReserveIds.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IReserveIdsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.ireserveidsrequest)`   
ReserveIdsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.datastore.v1.ReserveIdsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.reserveidsresponse)>` | Promise  
  
### rollback(request, callback)
    
    
    public rollback(request: google.datastore.v1.IRollbackRequest, callback: google.datastore.v1.Datastore.RollbackCallback): void;

Calls Rollback.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRollbackRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.irollbackrequest)`   
RollbackRequest message or plain object  
`callback` |  `[RollbackCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and RollbackResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### rollback(request)
    
    
    public rollback(request: google.datastore.v1.IRollbackRequest): Promise<google.datastore.v1.RollbackResponse>;

Calls Rollback.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRollbackRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.irollbackrequest)`   
RollbackRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.datastore.v1.RollbackResponse](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.rollbackresponse)>` | Promise  
  
### runAggregationQuery(request, callback)
    
    
    public runAggregationQuery(request: google.datastore.v1.IRunAggregationQueryRequest, callback: google.datastore.v1.Datastore.RunAggregationQueryCallback): void;

Calls RunAggregationQuery.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunAggregationQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.irunaggregationqueryrequest)`   
RunAggregationQueryRequest message or plain object  
`callback` |  `[RunAggregationQueryCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and RunAggregationQueryResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### runAggregationQuery(request)
    
    
    public runAggregationQuery(request: google.datastore.v1.IRunAggregationQueryRequest): Promise<google.datastore.v1.RunAggregationQueryResponse>;

Calls RunAggregationQuery.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRunAggregationQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.irunaggregationqueryrequest)`   
RunAggregationQueryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.datastore.v1.RunAggregationQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.runaggregationqueryresponse)>` | Promise  
  
### runQuery(request, callback)
    
    
    public runQuery(request: google.datastore.v1.IRunQueryRequest, callback: google.datastore.v1.Datastore.RunQueryCallback): void;

Calls RunQuery.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.irunqueryrequest)`   
RunQueryRequest message or plain object  
`callback` |  `[RunQueryCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and RunQueryResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### runQuery(request)
    
    
    public runQuery(request: google.datastore.v1.IRunQueryRequest): Promise<google.datastore.v1.RunQueryResponse>;

Calls RunQuery.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRunQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.irunqueryrequest)`   
RunQueryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.datastore.v1.RunQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.runqueryresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-01 UTC."],[],[]] 
