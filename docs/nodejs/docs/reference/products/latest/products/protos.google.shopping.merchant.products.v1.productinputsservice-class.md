---
url: https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productinputsservice-class
title: Class protos.google.shopping.merchant.products.v1.ProductInputsService (0.11.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:21.432415+00:00
---

# Class protos.google.shopping.merchant.products.v1.ProductInputsService (0.11.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productinputsservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.products.v1.ProductInputsService (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.1.1 

Represents a ProductInputsService

## Inheritance

$protobuf.rpc.Service > protos.google.shopping.merchant.products.v1.ProductInputsService

## Package

[@google-shopping/products](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ProductInputsService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ProductInputsService;

Creates new ProductInputsService service using the specified rpc implementation.

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
`[ProductInputsService](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productinputsservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### deleteProductInput(request, callback)
    
    
    public deleteProductInput(request: google.shopping.merchant.products.v1.IDeleteProductInputRequest, callback: google.shopping.merchant.products.v1.ProductInputsService.DeleteProductInputCallback): void;

Calls DeleteProductInput.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.ideleteproductinputrequest)`   
DeleteProductInputRequest message or plain object  
`callback` |  `[DeleteProductInputCallback](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteProductInput(request)
    
    
    public deleteProductInput(request: google.shopping.merchant.products.v1.IDeleteProductInputRequest): Promise<google.protobuf.Empty>;

Calls DeleteProductInput.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.ideleteproductinputrequest)`   
DeleteProductInputRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.protobuf.empty)>` | Promise  
  
### insertProductInput(request, callback)
    
    
    public insertProductInput(request: google.shopping.merchant.products.v1.IInsertProductInputRequest, callback: google.shopping.merchant.products.v1.ProductInputsService.InsertProductInputCallback): void;

Calls InsertProductInput.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.iinsertproductinputrequest)`   
InsertProductInputRequest message or plain object  
`callback` |  `[InsertProductInputCallback](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/overview.html)`   
Node-style callback called with the error, if any, and ProductInput  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insertProductInput(request)
    
    
    public insertProductInput(request: google.shopping.merchant.products.v1.IInsertProductInputRequest): Promise<google.shopping.merchant.products.v1.ProductInput>;

Calls InsertProductInput.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IInsertProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.iinsertproductinputrequest)`   
InsertProductInputRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.products.v1.ProductInput](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productinput)>` | Promise  
  
### updateProductInput(request, callback)
    
    
    public updateProductInput(request: google.shopping.merchant.products.v1.IUpdateProductInputRequest, callback: google.shopping.merchant.products.v1.ProductInputsService.UpdateProductInputCallback): void;

Calls UpdateProductInput.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.iupdateproductinputrequest)`   
UpdateProductInputRequest message or plain object  
`callback` |  `[UpdateProductInputCallback](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/overview.html)`   
Node-style callback called with the error, if any, and ProductInput  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateProductInput(request)
    
    
    public updateProductInput(request: google.shopping.merchant.products.v1.IUpdateProductInputRequest): Promise<google.shopping.merchant.products.v1.ProductInput>;

Calls UpdateProductInput.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateProductInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.iupdateproductinputrequest)`   
UpdateProductInputRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.products.v1.ProductInput](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productinput)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
