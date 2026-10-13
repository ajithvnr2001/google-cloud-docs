---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.bigqueryread-class
title: Class protos.google.cloud.bigquery.storage.v1.BigQueryRead (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:55:32.391484+00:00
---

# Class protos.google.cloud.bigquery.storage.v1.BigQueryRead (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.bigqueryread-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.bigquery.storage.v1.BigQueryRead (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a BigQueryRead

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.bigquery.storage.v1.BigQueryRead

## Package

[@google-cloud/bigquery-storage-api](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new BigQueryRead service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): BigQueryRead;

Creates new BigQueryRead service using the specified rpc implementation.

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
`[BigQueryRead](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.bigqueryread-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createReadSession(request, callback)
    
    
    public createReadSession(request: google.cloud.bigquery.storage.v1.ICreateReadSessionRequest, callback: google.cloud.bigquery.storage.v1.BigQueryRead.CreateReadSessionCallback): void;

Calls CreateReadSession.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateReadSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.icreatereadsessionrequest)`   
CreateReadSessionRequest message or plain object  
`callback` |  `[CreateReadSessionCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/overview.html)`   
Node-style callback called with the error, if any, and ReadSession  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createReadSession(request)
    
    
    public createReadSession(request: google.cloud.bigquery.storage.v1.ICreateReadSessionRequest): Promise<google.cloud.bigquery.storage.v1.ReadSession>;

Calls CreateReadSession.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateReadSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.icreatereadsessionrequest)`   
CreateReadSessionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.storage.v1.ReadSession](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.readsession-class)>` | Promise  
  
### readRows(request, callback)
    
    
    public readRows(request: google.cloud.bigquery.storage.v1.IReadRowsRequest, callback: google.cloud.bigquery.storage.v1.BigQueryRead.ReadRowsCallback): void;

Calls ReadRows.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReadRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.ireadrowsrequest)`   
ReadRowsRequest message or plain object  
`callback` |  `[ReadRowsCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/overview.html)`   
Node-style callback called with the error, if any, and ReadRowsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### readRows(request)
    
    
    public readRows(request: google.cloud.bigquery.storage.v1.IReadRowsRequest): Promise<google.cloud.bigquery.storage.v1.ReadRowsResponse>;

Calls ReadRows.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IReadRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.ireadrowsrequest)`   
ReadRowsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.storage.v1.ReadRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.readrowsresponse)>` | Promise  
  
### splitReadStream(request, callback)
    
    
    public splitReadStream(request: google.cloud.bigquery.storage.v1.ISplitReadStreamRequest, callback: google.cloud.bigquery.storage.v1.BigQueryRead.SplitReadStreamCallback): void;

Calls SplitReadStream.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISplitReadStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.isplitreadstreamrequest)`   
SplitReadStreamRequest message or plain object  
`callback` |  `[SplitReadStreamCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/overview.html)`   
Node-style callback called with the error, if any, and SplitReadStreamResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### splitReadStream(request)
    
    
    public splitReadStream(request: google.cloud.bigquery.storage.v1.ISplitReadStreamRequest): Promise<google.cloud.bigquery.storage.v1.SplitReadStreamResponse>;

Calls SplitReadStream.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISplitReadStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.isplitreadstreamrequest)`   
SplitReadStreamRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.storage.v1.SplitReadStreamResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.cloud.bigquery.storage.v1.splitreadstreamresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-01 UTC."],[],[]] 
