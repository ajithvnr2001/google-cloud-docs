---
url: https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.localinventoryservice-class
title: Class protos.google.shopping.merchant.inventories.v1.LocalInventoryService (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:03:13.029713+00:00
---

# Class protos.google.shopping.merchant.inventories.v1.LocalInventoryService (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.localinventoryservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.inventories.v1.LocalInventoryService (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.12.0  0.7.1  0.5.0  0.4.0 

Represents a LocalInventoryService

## Inheritance

$protobuf.rpc.Service > protos.google.shopping.merchant.inventories.v1.LocalInventoryService

## Package

[@google-shopping/inventories](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new LocalInventoryService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): LocalInventoryService;

Creates new LocalInventoryService service using the specified rpc implementation.

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
`[LocalInventoryService](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.localinventoryservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### deleteLocalInventory(request, callback)
    
    
    public deleteLocalInventory(request: google.shopping.merchant.inventories.v1.IDeleteLocalInventoryRequest, callback: google.shopping.merchant.inventories.v1.LocalInventoryService.DeleteLocalInventoryCallback): void;

Calls DeleteLocalInventory.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteLocalInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.ideletelocalinventoryrequest)`   
DeleteLocalInventoryRequest message or plain object  
`callback` |  `[DeleteLocalInventoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteLocalInventory(request)
    
    
    public deleteLocalInventory(request: google.shopping.merchant.inventories.v1.IDeleteLocalInventoryRequest): Promise<google.protobuf.Empty>;

Calls DeleteLocalInventory.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteLocalInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.ideletelocalinventoryrequest)`   
DeleteLocalInventoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.protobuf.empty)>` | Promise  
  
### insertLocalInventory(request, callback)
    
    
    public insertLocalInventory(request: google.shopping.merchant.inventories.v1.IInsertLocalInventoryRequest, callback: google.shopping.merchant.inventories.v1.LocalInventoryService.InsertLocalInventoryCallback): void;

Calls InsertLocalInventory.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertLocalInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.iinsertlocalinventoryrequest)`   
InsertLocalInventoryRequest message or plain object  
`callback` |  `[InsertLocalInventoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/overview.html)`   
Node-style callback called with the error, if any, and LocalInventory  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insertLocalInventory(request)
    
    
    public insertLocalInventory(request: google.shopping.merchant.inventories.v1.IInsertLocalInventoryRequest): Promise<google.shopping.merchant.inventories.v1.LocalInventory>;

Calls InsertLocalInventory.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IInsertLocalInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.iinsertlocalinventoryrequest)`   
InsertLocalInventoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.inventories.v1.LocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.localinventory)>` | Promise  
  
### listLocalInventories(request, callback)
    
    
    public listLocalInventories(request: google.shopping.merchant.inventories.v1.IListLocalInventoriesRequest, callback: google.shopping.merchant.inventories.v1.LocalInventoryService.ListLocalInventoriesCallback): void;

Calls ListLocalInventories.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListLocalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.ilistlocalinventoriesrequest)`   
ListLocalInventoriesRequest message or plain object  
`callback` |  `[ListLocalInventoriesCallback](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/overview.html)`   
Node-style callback called with the error, if any, and ListLocalInventoriesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listLocalInventories(request)
    
    
    public listLocalInventories(request: google.shopping.merchant.inventories.v1.IListLocalInventoriesRequest): Promise<google.shopping.merchant.inventories.v1.ListLocalInventoriesResponse>;

Calls ListLocalInventories.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListLocalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.ilistlocalinventoriesrequest)`   
ListLocalInventoriesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.inventories.v1.ListLocalInventoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.listlocalinventoriesresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
