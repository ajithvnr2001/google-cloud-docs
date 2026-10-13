---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.bigquerywrite-class
title: Class protos.google.cloud.bigquery.storage.v1.BigQueryWrite (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:55:32.522418+00:00
---

# Class protos.google.cloud.bigquery.storage.v1.BigQueryWrite (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.bigquerywrite-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.bigquery.storage.v1.BigQueryWrite (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a BigQueryWrite

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.bigquery.storage.v1.BigQueryWrite

## Package

[@google-cloud/bigquery-storage-api](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new BigQueryWrite service.

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

### appendRows(request, callback)
    
    
    public appendRows(request: google.cloud.bigquery.storage.v1.IAppendRowsRequest, callback: google.cloud.bigquery.storage.v1.BigQueryWrite.AppendRowsCallback): void;

Calls AppendRows.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAppendRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.iappendrowsrequest)`   
AppendRowsRequest message or plain object  
`callback` |  `[AppendRowsCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/overview.html)`   
Node-style callback called with the error, if any, and AppendRowsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### appendRows(request)
    
    
    public appendRows(request: google.cloud.bigquery.storage.v1.IAppendRowsRequest): Promise<google.cloud.bigquery.storage.v1.AppendRowsResponse>;

Calls AppendRows.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAppendRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.iappendrowsrequest)`   
AppendRowsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.storage.v1.AppendRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.appendrowsresponse-class)>` | Promise  
  
### batchCommitWriteStreams(request, callback)
    
    
    public batchCommitWriteStreams(request: google.cloud.bigquery.storage.v1.IBatchCommitWriteStreamsRequest, callback: google.cloud.bigquery.storage.v1.BigQueryWrite.BatchCommitWriteStreamsCallback): void;

Calls BatchCommitWriteStreams.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCommitWriteStreamsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.ibatchcommitwritestreamsrequest)`   
BatchCommitWriteStreamsRequest message or plain object  
`callback` |  `[BatchCommitWriteStreamsCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchCommitWriteStreamsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCommitWriteStreams(request)
    
    
    public batchCommitWriteStreams(request: google.cloud.bigquery.storage.v1.IBatchCommitWriteStreamsRequest): Promise<google.cloud.bigquery.storage.v1.BatchCommitWriteStreamsResponse>;

Calls BatchCommitWriteStreams.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchCommitWriteStreamsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.ibatchcommitwritestreamsrequest)`   
BatchCommitWriteStreamsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.storage.v1.BatchCommitWriteStreamsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.batchcommitwritestreamsresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): BigQueryWrite;

Creates new BigQueryWrite service using the specified rpc implementation.

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
`[BigQueryWrite](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.bigquerywrite-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createWriteStream(request, callback)
    
    
    public createWriteStream(request: google.cloud.bigquery.storage.v1.ICreateWriteStreamRequest, callback: google.cloud.bigquery.storage.v1.BigQueryWrite.CreateWriteStreamCallback): void;

Calls CreateWriteStream.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWriteStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.icreatewritestreamrequest)`   
CreateWriteStreamRequest message or plain object  
`callback` |  `[CreateWriteStreamCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/overview.html)`   
Node-style callback called with the error, if any, and WriteStream  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createWriteStream(request)
    
    
    public createWriteStream(request: google.cloud.bigquery.storage.v1.ICreateWriteStreamRequest): Promise<google.cloud.bigquery.storage.v1.WriteStream>;

Calls CreateWriteStream.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateWriteStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.icreatewritestreamrequest)`   
CreateWriteStreamRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.storage.v1.WriteStream](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.writestream-class)>` | Promise  
  
### finalizeWriteStream(request, callback)
    
    
    public finalizeWriteStream(request: google.cloud.bigquery.storage.v1.IFinalizeWriteStreamRequest, callback: google.cloud.bigquery.storage.v1.BigQueryWrite.FinalizeWriteStreamCallback): void;

Calls FinalizeWriteStream.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFinalizeWriteStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.ifinalizewritestreamrequest)`   
FinalizeWriteStreamRequest message or plain object  
`callback` |  `[FinalizeWriteStreamCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/overview.html)`   
Node-style callback called with the error, if any, and FinalizeWriteStreamResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### finalizeWriteStream(request)
    
    
    public finalizeWriteStream(request: google.cloud.bigquery.storage.v1.IFinalizeWriteStreamRequest): Promise<google.cloud.bigquery.storage.v1.FinalizeWriteStreamResponse>;

Calls FinalizeWriteStream.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFinalizeWriteStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.ifinalizewritestreamrequest)`   
FinalizeWriteStreamRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.storage.v1.FinalizeWriteStreamResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.finalizewritestreamresponse)>` | Promise  
  
### flushRows(request, callback)
    
    
    public flushRows(request: google.cloud.bigquery.storage.v1.IFlushRowsRequest, callback: google.cloud.bigquery.storage.v1.BigQueryWrite.FlushRowsCallback): void;

Calls FlushRows.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFlushRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.iflushrowsrequest)`   
FlushRowsRequest message or plain object  
`callback` |  `[FlushRowsCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/overview.html)`   
Node-style callback called with the error, if any, and FlushRowsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### flushRows(request)
    
    
    public flushRows(request: google.cloud.bigquery.storage.v1.IFlushRowsRequest): Promise<google.cloud.bigquery.storage.v1.FlushRowsResponse>;

Calls FlushRows.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFlushRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.iflushrowsrequest)`   
FlushRowsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.storage.v1.FlushRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.flushrowsresponse)>` | Promise  
  
### getWriteStream(request, callback)
    
    
    public getWriteStream(request: google.cloud.bigquery.storage.v1.IGetWriteStreamRequest, callback: google.cloud.bigquery.storage.v1.BigQueryWrite.GetWriteStreamCallback): void;

Calls GetWriteStream.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWriteStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.igetwritestreamrequest)`   
GetWriteStreamRequest message or plain object  
`callback` |  `[GetWriteStreamCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/overview.html)`   
Node-style callback called with the error, if any, and WriteStream  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getWriteStream(request)
    
    
    public getWriteStream(request: google.cloud.bigquery.storage.v1.IGetWriteStreamRequest): Promise<google.cloud.bigquery.storage.v1.WriteStream>;

Calls GetWriteStream.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetWriteStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.igetwritestreamrequest)`   
GetWriteStreamRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.storage.v1.WriteStream](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.writestream-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-01 UTC."],[],[]] 
