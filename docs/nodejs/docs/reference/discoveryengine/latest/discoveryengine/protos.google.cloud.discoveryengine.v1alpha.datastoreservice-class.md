---
url: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.datastoreservice-class
title: Class protos.google.cloud.discoveryengine.v1alpha.DataStoreService (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:29.618630+00:00
---

# Class protos.google.cloud.discoveryengine.v1alpha.DataStoreService (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.datastoreservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.discoveryengine.v1alpha.DataStoreService (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  3.3.0  3.1.0  2.9.0  2.8.0  2.6.0  2.2.0  2.0.1  1.14.0  1.10.0  1.9.0  1.7.0  1.6.0  1.4.1  1.3.1  1.2.0  1.0.0  0.6.0  0.5.0  0.3.1  0.2.0 

Represents a DataStoreService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.discoveryengine.v1alpha.DataStoreService

## Package

[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DataStoreService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DataStoreService;

Creates new DataStoreService service using the specified rpc implementation.

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
`[DataStoreService](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.datastoreservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createDataStore(request, callback)
    
    
    public createDataStore(request: google.cloud.discoveryengine.v1alpha.ICreateDataStoreRequest, callback: google.cloud.discoveryengine.v1alpha.DataStoreService.CreateDataStoreCallback): void;

Calls CreateDataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.icreatedatastorerequest)`   
CreateDataStoreRequest message or plain object  
`callback` |  `[CreateDataStoreCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataStore(request)
    
    
    public createDataStore(request: google.cloud.discoveryengine.v1alpha.ICreateDataStoreRequest): Promise<google.longrunning.Operation>;

Calls CreateDataStore.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.icreatedatastorerequest)`   
CreateDataStoreRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.operation)>` | Promise  
  
### deleteDataStore(request, callback)
    
    
    public deleteDataStore(request: google.cloud.discoveryengine.v1alpha.IDeleteDataStoreRequest, callback: google.cloud.discoveryengine.v1alpha.DataStoreService.DeleteDataStoreCallback): void;

Calls DeleteDataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ideletedatastorerequest)`   
DeleteDataStoreRequest message or plain object  
`callback` |  `[DeleteDataStoreCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataStore(request)
    
    
    public deleteDataStore(request: google.cloud.discoveryengine.v1alpha.IDeleteDataStoreRequest): Promise<google.longrunning.Operation>;

Calls DeleteDataStore.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ideletedatastorerequest)`   
DeleteDataStoreRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.operation)>` | Promise  
  
### getDataStore(request, callback)
    
    
    public getDataStore(request: google.cloud.discoveryengine.v1alpha.IGetDataStoreRequest, callback: google.cloud.discoveryengine.v1alpha.DataStoreService.GetDataStoreCallback): void;

Calls GetDataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetdatastorerequest)`   
GetDataStoreRequest message or plain object  
`callback` |  `[GetDataStoreCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and DataStore  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataStore(request)
    
    
    public getDataStore(request: google.cloud.discoveryengine.v1alpha.IGetDataStoreRequest): Promise<google.cloud.discoveryengine.v1alpha.DataStore>;

Calls GetDataStore.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetdatastorerequest)`   
GetDataStoreRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1alpha.DataStore](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.datastore-class)>` | Promise  
  
### getDocumentProcessingConfig(request, callback)
    
    
    public getDocumentProcessingConfig(request: google.cloud.discoveryengine.v1alpha.IGetDocumentProcessingConfigRequest, callback: google.cloud.discoveryengine.v1alpha.DataStoreService.GetDocumentProcessingConfigCallback): void;

Calls GetDocumentProcessingConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDocumentProcessingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetdocumentprocessingconfigrequest)`   
GetDocumentProcessingConfigRequest message or plain object  
`callback` |  `[GetDocumentProcessingConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and DocumentProcessingConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDocumentProcessingConfig(request)
    
    
    public getDocumentProcessingConfig(request: google.cloud.discoveryengine.v1alpha.IGetDocumentProcessingConfigRequest): Promise<google.cloud.discoveryengine.v1alpha.DocumentProcessingConfig>;

Calls GetDocumentProcessingConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDocumentProcessingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetdocumentprocessingconfigrequest)`   
GetDocumentProcessingConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1alpha.DocumentProcessingConfig](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.documentprocessingconfig-class)>` | Promise  
  
### listDataStores(request, callback)
    
    
    public listDataStores(request: google.cloud.discoveryengine.v1alpha.IListDataStoresRequest, callback: google.cloud.discoveryengine.v1alpha.DataStoreService.ListDataStoresCallback): void;

Calls ListDataStores.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataStoresRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistdatastoresrequest)`   
ListDataStoresRequest message or plain object  
`callback` |  `[ListDataStoresCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDataStoresResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataStores(request)
    
    
    public listDataStores(request: google.cloud.discoveryengine.v1alpha.IListDataStoresRequest): Promise<google.cloud.discoveryengine.v1alpha.ListDataStoresResponse>;

Calls ListDataStores.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDataStoresRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilistdatastoresrequest)`   
ListDataStoresRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1alpha.ListDataStoresResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.listdatastoresresponse)>` | Promise  
  
### updateDataStore(request, callback)
    
    
    public updateDataStore(request: google.cloud.discoveryengine.v1alpha.IUpdateDataStoreRequest, callback: google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateDataStoreCallback): void;

Calls UpdateDataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iupdatedatastorerequest)`   
UpdateDataStoreRequest message or plain object  
`callback` |  `[UpdateDataStoreCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and DataStore  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataStore(request)
    
    
    public updateDataStore(request: google.cloud.discoveryengine.v1alpha.IUpdateDataStoreRequest): Promise<google.cloud.discoveryengine.v1alpha.DataStore>;

Calls UpdateDataStore.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iupdatedatastorerequest)`   
UpdateDataStoreRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1alpha.DataStore](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.datastore-class)>` | Promise  
  
### updateDocumentProcessingConfig(request, callback)
    
    
    public updateDocumentProcessingConfig(request: google.cloud.discoveryengine.v1alpha.IUpdateDocumentProcessingConfigRequest, callback: google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateDocumentProcessingConfigCallback): void;

Calls UpdateDocumentProcessingConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDocumentProcessingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iupdatedocumentprocessingconfigrequest)`   
UpdateDocumentProcessingConfigRequest message or plain object  
`callback` |  `[UpdateDocumentProcessingConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and DocumentProcessingConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDocumentProcessingConfig(request)
    
    
    public updateDocumentProcessingConfig(request: google.cloud.discoveryengine.v1alpha.IUpdateDocumentProcessingConfigRequest): Promise<google.cloud.discoveryengine.v1alpha.DocumentProcessingConfig>;

Calls UpdateDocumentProcessingConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDocumentProcessingConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iupdatedocumentprocessingconfigrequest)`   
UpdateDocumentProcessingConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1alpha.DocumentProcessingConfig](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.documentprocessingconfig-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
