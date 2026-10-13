---
url: https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpstoreservice-class
title: Class protos.google.shopping.merchant.lfp.v1beta.LfpStoreService (0.11.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:23.782971+00:00
---

# Class protos.google.shopping.merchant.lfp.v1beta.LfpStoreService (0.11.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpstoreservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.lfp.v1beta.LfpStoreService (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.10.0  0.4.1  0.2.0  0.1.0 

Represents a LfpStoreService

## Inheritance

$protobuf.rpc.Service > protos.google.shopping.merchant.lfp.v1beta.LfpStoreService

## Package

[@google-shopping/lfp](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new LfpStoreService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): LfpStoreService;

Creates new LfpStoreService service using the specified rpc implementation.

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
`[LfpStoreService](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpstoreservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### deleteLfpStore(request, callback)
    
    
    public deleteLfpStore(request: google.shopping.merchant.lfp.v1beta.IDeleteLfpStoreRequest, callback: google.shopping.merchant.lfp.v1beta.LfpStoreService.DeleteLfpStoreCallback): void;

Calls DeleteLfpStore.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteLfpStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.ideletelfpstorerequest)`   
DeleteLfpStoreRequest message or plain object  
`callback` |  `[DeleteLfpStoreCallback](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteLfpStore(request)
    
    
    public deleteLfpStore(request: google.shopping.merchant.lfp.v1beta.IDeleteLfpStoreRequest): Promise<google.protobuf.Empty>;

Calls DeleteLfpStore.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteLfpStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.ideletelfpstorerequest)`   
DeleteLfpStoreRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.protobuf.empty)>` | Promise  
  
### getLfpStore(request, callback)
    
    
    public getLfpStore(request: google.shopping.merchant.lfp.v1beta.IGetLfpStoreRequest, callback: google.shopping.merchant.lfp.v1beta.LfpStoreService.GetLfpStoreCallback): void;

Calls GetLfpStore.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetLfpStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.igetlfpstorerequest)`   
GetLfpStoreRequest message or plain object  
`callback` |  `[GetLfpStoreCallback](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/overview.html)`   
Node-style callback called with the error, if any, and LfpStore  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getLfpStore(request)
    
    
    public getLfpStore(request: google.shopping.merchant.lfp.v1beta.IGetLfpStoreRequest): Promise<google.shopping.merchant.lfp.v1beta.LfpStore>;

Calls GetLfpStore.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetLfpStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.igetlfpstorerequest)`   
GetLfpStoreRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.lfp.v1beta.LfpStore](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpstore-class)>` | Promise  
  
### insertLfpStore(request, callback)
    
    
    public insertLfpStore(request: google.shopping.merchant.lfp.v1beta.IInsertLfpStoreRequest, callback: google.shopping.merchant.lfp.v1beta.LfpStoreService.InsertLfpStoreCallback): void;

Calls InsertLfpStore.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertLfpStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.iinsertlfpstorerequest)`   
InsertLfpStoreRequest message or plain object  
`callback` |  `[InsertLfpStoreCallback](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/overview.html)`   
Node-style callback called with the error, if any, and LfpStore  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insertLfpStore(request)
    
    
    public insertLfpStore(request: google.shopping.merchant.lfp.v1beta.IInsertLfpStoreRequest): Promise<google.shopping.merchant.lfp.v1beta.LfpStore>;

Calls InsertLfpStore.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IInsertLfpStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.iinsertlfpstorerequest)`   
InsertLfpStoreRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.lfp.v1beta.LfpStore](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpstore-class)>` | Promise  
  
### listLfpStores(request, callback)
    
    
    public listLfpStores(request: google.shopping.merchant.lfp.v1beta.IListLfpStoresRequest, callback: google.shopping.merchant.lfp.v1beta.LfpStoreService.ListLfpStoresCallback): void;

Calls ListLfpStores.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListLfpStoresRequest](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.ilistlfpstoresrequest)`   
ListLfpStoresRequest message or plain object  
`callback` |  `[ListLfpStoresCallback](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/overview.html)`   
Node-style callback called with the error, if any, and ListLfpStoresResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listLfpStores(request)
    
    
    public listLfpStores(request: google.shopping.merchant.lfp.v1beta.IListLfpStoresRequest): Promise<google.shopping.merchant.lfp.v1beta.ListLfpStoresResponse>;

Calls ListLfpStores.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListLfpStoresRequest](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.ilistlfpstoresrequest)`   
ListLfpStoresRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.lfp.v1beta.ListLfpStoresResponse](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.listlfpstoresresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
