---
url: https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.dataobjectsearchservice-class
title: Class protos.google.cloud.vectorsearch.v1beta.DataObjectSearchService (0.13.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:46.551073+00:00
---

# Class protos.google.cloud.vectorsearch.v1beta.DataObjectSearchService (0.13.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.dataobjectsearchservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.vectorsearch.v1beta.DataObjectSearchService (0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.13.0  0.8.0  0.6.0  0.5.0  0.4.0  0.2.0  0.1.0 

Represents a DataObjectSearchService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.vectorsearch.v1beta.DataObjectSearchService

## Package

[@google-cloud/vectorsearch](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DataObjectSearchService service.

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

### aggregateDataObjects(request, callback)
    
    
    public aggregateDataObjects(request: google.cloud.vectorsearch.v1beta.IAggregateDataObjectsRequest, callback: google.cloud.vectorsearch.v1beta.DataObjectSearchService.AggregateDataObjectsCallback): void;

Calls AggregateDataObjects.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAggregateDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.iaggregatedataobjectsrequest)`   
AggregateDataObjectsRequest message or plain object  
`callback` |  `[AggregateDataObjectsCallback](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)`   
Node-style callback called with the error, if any, and AggregateDataObjectsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### aggregateDataObjects(request)
    
    
    public aggregateDataObjects(request: google.cloud.vectorsearch.v1beta.IAggregateDataObjectsRequest): Promise<google.cloud.vectorsearch.v1beta.AggregateDataObjectsResponse>;

Calls AggregateDataObjects.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAggregateDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.iaggregatedataobjectsrequest)`   
AggregateDataObjectsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vectorsearch.v1beta.AggregateDataObjectsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.aggregatedataobjectsresponse)>` | Promise  
  
### batchSearchDataObjects(request, callback)
    
    
    public batchSearchDataObjects(request: google.cloud.vectorsearch.v1beta.IBatchSearchDataObjectsRequest, callback: google.cloud.vectorsearch.v1beta.DataObjectSearchService.BatchSearchDataObjectsCallback): void;

Calls BatchSearchDataObjects.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchSearchDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchsearchdataobjectsrequest)`   
BatchSearchDataObjectsRequest message or plain object  
`callback` |  `[BatchSearchDataObjectsCallback](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchSearchDataObjectsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchSearchDataObjects(request)
    
    
    public batchSearchDataObjects(request: google.cloud.vectorsearch.v1beta.IBatchSearchDataObjectsRequest): Promise<google.cloud.vectorsearch.v1beta.BatchSearchDataObjectsResponse>;

Calls BatchSearchDataObjects.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchSearchDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchsearchdataobjectsrequest)`   
BatchSearchDataObjectsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vectorsearch.v1beta.BatchSearchDataObjectsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.batchsearchdataobjectsresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DataObjectSearchService;

Creates new DataObjectSearchService service using the specified rpc implementation.

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
`[DataObjectSearchService](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.dataobjectsearchservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### queryDataObjects(request, callback)
    
    
    public queryDataObjects(request: google.cloud.vectorsearch.v1beta.IQueryDataObjectsRequest, callback: google.cloud.vectorsearch.v1beta.DataObjectSearchService.QueryDataObjectsCallback): void;

Calls QueryDataObjects.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.iquerydataobjectsrequest)`   
QueryDataObjectsRequest message or plain object  
`callback` |  `[QueryDataObjectsCallback](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryDataObjectsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryDataObjects(request)
    
    
    public queryDataObjects(request: google.cloud.vectorsearch.v1beta.IQueryDataObjectsRequest): Promise<google.cloud.vectorsearch.v1beta.QueryDataObjectsResponse>;

Calls QueryDataObjects.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IQueryDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.iquerydataobjectsrequest)`   
QueryDataObjectsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vectorsearch.v1beta.QueryDataObjectsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.querydataobjectsresponse)>` | Promise  
  
### searchDataObjects(request, callback)
    
    
    public searchDataObjects(request: google.cloud.vectorsearch.v1beta.ISearchDataObjectsRequest, callback: google.cloud.vectorsearch.v1beta.DataObjectSearchService.SearchDataObjectsCallback): void;

Calls SearchDataObjects.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.isearchdataobjectsrequest)`   
SearchDataObjectsRequest message or plain object  
`callback` |  `[SearchDataObjectsCallback](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchDataObjectsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchDataObjects(request)
    
    
    public searchDataObjects(request: google.cloud.vectorsearch.v1beta.ISearchDataObjectsRequest): Promise<google.cloud.vectorsearch.v1beta.SearchDataObjectsResponse>;

Calls SearchDataObjects.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.isearchdataobjectsrequest)`   
SearchDataObjectsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.vectorsearch.v1beta.SearchDataObjectsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.searchdataobjectsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
