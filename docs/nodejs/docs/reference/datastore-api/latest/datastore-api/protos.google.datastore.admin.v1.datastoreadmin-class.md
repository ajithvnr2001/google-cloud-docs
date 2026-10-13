---
url: https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.datastoreadmin-class
title: Class protos.google.datastore.admin.v1.DatastoreAdmin (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:47:44.222555+00:00
---

# Class protos.google.datastore.admin.v1.DatastoreAdmin (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.datastoreadmin-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.datastore.admin.v1.DatastoreAdmin (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a DatastoreAdmin

## Inheritance

$protobuf.rpc.Service > protos.google.datastore.admin.v1.DatastoreAdmin

## Package

[@google-cloud/datastore-api](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DatastoreAdmin service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DatastoreAdmin;

Creates new DatastoreAdmin service using the specified rpc implementation.

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
`[DatastoreAdmin](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.datastoreadmin-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createIndex(request, callback)
    
    
    public createIndex(request: google.datastore.admin.v1.ICreateIndexRequest, callback: google.datastore.admin.v1.DatastoreAdmin.CreateIndexCallback): void;

Calls CreateIndex.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateIndexRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.icreateindexrequest)`   
CreateIndexRequest message or plain object  
`callback` |  `[CreateIndexCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createIndex(request)
    
    
    public createIndex(request: google.datastore.admin.v1.ICreateIndexRequest): Promise<google.longrunning.Operation>;

Calls CreateIndex.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateIndexRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.icreateindexrequest)`   
CreateIndexRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.longrunning.operation)>` | Promise  
  
### deleteIndex(request, callback)
    
    
    public deleteIndex(request: google.datastore.admin.v1.IDeleteIndexRequest, callback: google.datastore.admin.v1.DatastoreAdmin.DeleteIndexCallback): void;

Calls DeleteIndex.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteIndexRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.ideleteindexrequest)`   
DeleteIndexRequest message or plain object  
`callback` |  `[DeleteIndexCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteIndex(request)
    
    
    public deleteIndex(request: google.datastore.admin.v1.IDeleteIndexRequest): Promise<google.longrunning.Operation>;

Calls DeleteIndex.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteIndexRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.ideleteindexrequest)`   
DeleteIndexRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.longrunning.operation)>` | Promise  
  
### exportEntities(request, callback)
    
    
    public exportEntities(request: google.datastore.admin.v1.IExportEntitiesRequest, callback: google.datastore.admin.v1.DatastoreAdmin.ExportEntitiesCallback): void;

Calls ExportEntities.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.iexportentitiesrequest)`   
ExportEntitiesRequest message or plain object  
`callback` |  `[ExportEntitiesCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportEntities(request)
    
    
    public exportEntities(request: google.datastore.admin.v1.IExportEntitiesRequest): Promise<google.longrunning.Operation>;

Calls ExportEntities.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.iexportentitiesrequest)`   
ExportEntitiesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.longrunning.operation)>` | Promise  
  
### getIndex(request, callback)
    
    
    public getIndex(request: google.datastore.admin.v1.IGetIndexRequest, callback: google.datastore.admin.v1.DatastoreAdmin.GetIndexCallback): void;

Calls GetIndex.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIndexRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.igetindexrequest)`   
GetIndexRequest message or plain object  
`callback` |  `[GetIndexCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Index  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIndex(request)
    
    
    public getIndex(request: google.datastore.admin.v1.IGetIndexRequest): Promise<google.datastore.admin.v1.Index>;

Calls GetIndex.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetIndexRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.igetindexrequest)`   
GetIndexRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.datastore.admin.v1.Index](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.index-class)>` | Promise  
  
### importEntities(request, callback)
    
    
    public importEntities(request: google.datastore.admin.v1.IImportEntitiesRequest, callback: google.datastore.admin.v1.DatastoreAdmin.ImportEntitiesCallback): void;

Calls ImportEntities.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.iimportentitiesrequest)`   
ImportEntitiesRequest message or plain object  
`callback` |  `[ImportEntitiesCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importEntities(request)
    
    
    public importEntities(request: google.datastore.admin.v1.IImportEntitiesRequest): Promise<google.longrunning.Operation>;

Calls ImportEntities.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.iimportentitiesrequest)`   
ImportEntitiesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.longrunning.operation)>` | Promise  
  
### listIndexes(request, callback)
    
    
    public listIndexes(request: google.datastore.admin.v1.IListIndexesRequest, callback: google.datastore.admin.v1.DatastoreAdmin.ListIndexesCallback): void;

Calls ListIndexes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListIndexesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.ilistindexesrequest)`   
ListIndexesRequest message or plain object  
`callback` |  `[ListIndexesCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/overview.html)`   
Node-style callback called with the error, if any, and ListIndexesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listIndexes(request)
    
    
    public listIndexes(request: google.datastore.admin.v1.IListIndexesRequest): Promise<google.datastore.admin.v1.ListIndexesResponse>;

Calls ListIndexes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListIndexesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.ilistindexesrequest)`   
ListIndexesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.datastore.admin.v1.ListIndexesResponse](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.listindexesresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-01 UTC."],[],[]] 
