---
url: https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpinventoryservice-class
title: Class protos.google.shopping.merchant.lfp.v1beta.LfpInventoryService (0.11.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:23.069798+00:00
---

# Class protos.google.shopping.merchant.lfp.v1beta.LfpInventoryService (0.11.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpinventoryservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.lfp.v1beta.LfpInventoryService (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.10.0  0.4.1  0.2.0  0.1.0 

Represents a LfpInventoryService

## Inheritance

$protobuf.rpc.Service > protos.google.shopping.merchant.lfp.v1beta.LfpInventoryService

## Package

[@google-shopping/lfp](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new LfpInventoryService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): LfpInventoryService;

Creates new LfpInventoryService service using the specified rpc implementation.

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
`[LfpInventoryService](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpinventoryservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### insertLfpInventory(request, callback)
    
    
    public insertLfpInventory(request: google.shopping.merchant.lfp.v1beta.IInsertLfpInventoryRequest, callback: google.shopping.merchant.lfp.v1beta.LfpInventoryService.InsertLfpInventoryCallback): void;

Calls InsertLfpInventory.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertLfpInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.iinsertlfpinventoryrequest)`   
InsertLfpInventoryRequest message or plain object  
`callback` |  `[InsertLfpInventoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/overview.html)`   
Node-style callback called with the error, if any, and LfpInventory  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insertLfpInventory(request)
    
    
    public insertLfpInventory(request: google.shopping.merchant.lfp.v1beta.IInsertLfpInventoryRequest): Promise<google.shopping.merchant.lfp.v1beta.LfpInventory>;

Calls InsertLfpInventory.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IInsertLfpInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.iinsertlfpinventoryrequest)`   
InsertLfpInventoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.lfp.v1beta.LfpInventory](https://docs.cloud.google.com/nodejs/docs/reference/lfp/latest/lfp/protos.google.shopping.merchant.lfp.v1beta.lfpinventory)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
