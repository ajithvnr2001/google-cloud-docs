---
url: https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.regionalinventoryservice-class
title: Class protos.google.shopping.merchant.inventories.v1.RegionalInventoryService (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:03:13.731097+00:00
---

# Class protos.google.shopping.merchant.inventories.v1.RegionalInventoryService (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.regionalinventoryservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.inventories.v1.RegionalInventoryService (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.12.0  0.7.1  0.5.0  0.4.0 

Represents a RegionalInventoryService

## Inheritance

$protobuf.rpc.Service > protos.google.shopping.merchant.inventories.v1.RegionalInventoryService

## Package

[@google-shopping/inventories](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new RegionalInventoryService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): RegionalInventoryService;

Creates new RegionalInventoryService service using the specified rpc implementation.

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
`[RegionalInventoryService](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.regionalinventoryservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### deleteRegionalInventory(request, callback)
    
    
    public deleteRegionalInventory(request: google.shopping.merchant.inventories.v1.IDeleteRegionalInventoryRequest, callback: google.shopping.merchant.inventories.v1.RegionalInventoryService.DeleteRegionalInventoryCallback): void;

Calls DeleteRegionalInventory.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRegionalInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.ideleteregionalinventoryrequest)`   
DeleteRegionalInventoryRequest message or plain object  
`callback` |  `[DeleteRegionalInventoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteRegionalInventory(request)
    
    
    public deleteRegionalInventory(request: google.shopping.merchant.inventories.v1.IDeleteRegionalInventoryRequest): Promise<google.protobuf.Empty>;

Calls DeleteRegionalInventory.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRegionalInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.ideleteregionalinventoryrequest)`   
DeleteRegionalInventoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.protobuf.empty)>` | Promise  
  
### insertRegionalInventory(request, callback)
    
    
    public insertRegionalInventory(request: google.shopping.merchant.inventories.v1.IInsertRegionalInventoryRequest, callback: google.shopping.merchant.inventories.v1.RegionalInventoryService.InsertRegionalInventoryCallback): void;

Calls InsertRegionalInventory.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertRegionalInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.iinsertregionalinventoryrequest)`   
InsertRegionalInventoryRequest message or plain object  
`callback` |  `[InsertRegionalInventoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/overview.html)`   
Node-style callback called with the error, if any, and RegionalInventory  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insertRegionalInventory(request)
    
    
    public insertRegionalInventory(request: google.shopping.merchant.inventories.v1.IInsertRegionalInventoryRequest): Promise<google.shopping.merchant.inventories.v1.RegionalInventory>;

Calls InsertRegionalInventory.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IInsertRegionalInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.iinsertregionalinventoryrequest)`   
InsertRegionalInventoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.inventories.v1.RegionalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.regionalinventory)>` | Promise  
  
### listRegionalInventories(request, callback)
    
    
    public listRegionalInventories(request: google.shopping.merchant.inventories.v1.IListRegionalInventoriesRequest, callback: google.shopping.merchant.inventories.v1.RegionalInventoryService.ListRegionalInventoriesCallback): void;

Calls ListRegionalInventories.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRegionalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.ilistregionalinventoriesrequest)`   
ListRegionalInventoriesRequest message or plain object  
`callback` |  `[ListRegionalInventoriesCallback](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/overview.html)`   
Node-style callback called with the error, if any, and ListRegionalInventoriesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRegionalInventories(request)
    
    
    public listRegionalInventories(request: google.shopping.merchant.inventories.v1.IListRegionalInventoriesRequest): Promise<google.shopping.merchant.inventories.v1.ListRegionalInventoriesResponse>;

Calls ListRegionalInventories.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListRegionalInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.ilistregionalinventoriesrequest)`   
ListRegionalInventoriesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.inventories.v1.ListRegionalInventoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.listregionalinventoriesresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
