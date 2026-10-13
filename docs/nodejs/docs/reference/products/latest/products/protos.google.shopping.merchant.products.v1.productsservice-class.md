---
url: https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productsservice-class
title: Class protos.google.shopping.merchant.products.v1.ProductsService (0.11.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:22.649191+00:00
---

# Class protos.google.shopping.merchant.products.v1.ProductsService (0.11.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productsservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.products.v1.ProductsService (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.1.1 

Represents a ProductsService

## Inheritance

$protobuf.rpc.Service > protos.google.shopping.merchant.products.v1.ProductsService

## Package

[@google-shopping/products](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ProductsService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ProductsService;

Creates new ProductsService service using the specified rpc implementation.

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
`[ProductsService](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productsservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### getProduct(request, callback)
    
    
    public getProduct(request: google.shopping.merchant.products.v1.IGetProductRequest, callback: google.shopping.merchant.products.v1.ProductsService.GetProductCallback): void;

Calls GetProduct.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.igetproductrequest)`   
GetProductRequest message or plain object  
`callback` |  `[GetProductCallback](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/overview.html)`   
Node-style callback called with the error, if any, and Product  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProduct(request)
    
    
    public getProduct(request: google.shopping.merchant.products.v1.IGetProductRequest): Promise<google.shopping.merchant.products.v1.Product>;

Calls GetProduct.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetProductRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.igetproductrequest)`   
GetProductRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.products.v1.Product](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.product)>` | Promise  
  
### listProducts(request, callback)
    
    
    public listProducts(request: google.shopping.merchant.products.v1.IListProductsRequest, callback: google.shopping.merchant.products.v1.ProductsService.ListProductsCallback): void;

Calls ListProducts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.ilistproductsrequest)`   
ListProductsRequest message or plain object  
`callback` |  `[ListProductsCallback](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/overview.html)`   
Node-style callback called with the error, if any, and ListProductsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProducts(request)
    
    
    public listProducts(request: google.shopping.merchant.products.v1.IListProductsRequest): Promise<google.shopping.merchant.products.v1.ListProductsResponse>;

Calls ListProducts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListProductsRequest](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.ilistproductsrequest)`   
ListProductsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.products.v1.ListProductsResponse](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.listproductsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
