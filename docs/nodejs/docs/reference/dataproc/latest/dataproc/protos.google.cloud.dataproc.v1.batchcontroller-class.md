---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.batchcontroller-class
title: Class protos.google.cloud.dataproc.v1.BatchController (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:03:36.208402+00:00
---

# Class protos.google.cloud.dataproc.v1.BatchController (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.batchcontroller-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataproc.v1.BatchController (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.8.0  6.7.0  6.6.0  5.13.0  5.12.0  5.10.0  5.9.0  5.7.0  5.5.0  5.4.0  4.5.0  4.3.1  4.1.1  3.2.0  3.1.0  3.0.0  2.5.0  2.4.4 

Represents a BatchController

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dataproc.v1.BatchController

## Package

[@google-cloud/dataproc](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new BatchController service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): BatchController;

Creates new BatchController service using the specified rpc implementation.

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
`[BatchController](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.batchcontroller-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createBatch(request, callback)
    
    
    public createBatch(request: google.cloud.dataproc.v1.ICreateBatchRequest, callback: google.cloud.dataproc.v1.BatchController.CreateBatchCallback): void;

Calls CreateBatch.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateBatchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.icreatebatchrequest)`   
CreateBatchRequest message or plain object  
`callback` |  `[CreateBatchCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createBatch(request)
    
    
    public createBatch(request: google.cloud.dataproc.v1.ICreateBatchRequest): Promise<google.longrunning.Operation>;

Calls CreateBatch.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateBatchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.icreatebatchrequest)`   
CreateBatchRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.longrunning.operation)>` | Promise  
  
### deleteBatch(request, callback)
    
    
    public deleteBatch(request: google.cloud.dataproc.v1.IDeleteBatchRequest, callback: google.cloud.dataproc.v1.BatchController.DeleteBatchCallback): void;

Calls DeleteBatch.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBatchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ideletebatchrequest)`   
DeleteBatchRequest message or plain object  
`callback` |  `[DeleteBatchCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteBatch(request)
    
    
    public deleteBatch(request: google.cloud.dataproc.v1.IDeleteBatchRequest): Promise<google.protobuf.Empty>;

Calls DeleteBatch.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBatchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ideletebatchrequest)`   
DeleteBatchRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.protobuf.empty)>` | Promise  
  
### getBatch(request, callback)
    
    
    public getBatch(request: google.cloud.dataproc.v1.IGetBatchRequest, callback: google.cloud.dataproc.v1.BatchController.GetBatchCallback): void;

Calls GetBatch.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBatchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.igetbatchrequest)`   
GetBatchRequest message or plain object  
`callback` |  `[GetBatchCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Batch  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBatch(request)
    
    
    public getBatch(request: google.cloud.dataproc.v1.IGetBatchRequest): Promise<google.cloud.dataproc.v1.Batch>;

Calls GetBatch.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetBatchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.igetbatchrequest)`   
GetBatchRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataproc.v1.Batch](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.batch-class)>` | Promise  
  
### listBatches(request, callback)
    
    
    public listBatches(request: google.cloud.dataproc.v1.IListBatchesRequest, callback: google.cloud.dataproc.v1.BatchController.ListBatchesCallback): void;

Calls ListBatches.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBatchesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ilistbatchesrequest)`   
ListBatchesRequest message or plain object  
`callback` |  `[ListBatchesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and ListBatchesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBatches(request)
    
    
    public listBatches(request: google.cloud.dataproc.v1.IListBatchesRequest): Promise<google.cloud.dataproc.v1.ListBatchesResponse>;

Calls ListBatches.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListBatchesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ilistbatchesrequest)`   
ListBatchesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataproc.v1.ListBatchesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.listbatchesresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
