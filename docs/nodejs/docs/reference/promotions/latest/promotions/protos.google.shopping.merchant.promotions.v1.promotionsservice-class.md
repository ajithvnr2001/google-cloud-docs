---
url: https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.promotionsservice-class
title: Class protos.google.shopping.merchant.promotions.v1.PromotionsService (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:48:49.824697+00:00
---

# Class protos.google.shopping.merchant.promotions.v1.PromotionsService (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.promotionsservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.promotions.v1.PromotionsService (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.6.0  0.2.1  0.1.0 

Represents a PromotionsService

## Inheritance

$protobuf.rpc.Service > protos.google.shopping.merchant.promotions.v1.PromotionsService

## Package

[@google-shopping/promotions](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new PromotionsService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): PromotionsService;

Creates new PromotionsService service using the specified rpc implementation.

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
`[PromotionsService](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.promotionsservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### getPromotion(request, callback)
    
    
    public getPromotion(request: google.shopping.merchant.promotions.v1.IGetPromotionRequest, callback: google.shopping.merchant.promotions.v1.PromotionsService.GetPromotionCallback): void;

Calls GetPromotion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPromotionRequest](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.igetpromotionrequest)`   
GetPromotionRequest message or plain object  
`callback` |  `[GetPromotionCallback](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/overview.html)`   
Node-style callback called with the error, if any, and Promotion  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPromotion(request)
    
    
    public getPromotion(request: google.shopping.merchant.promotions.v1.IGetPromotionRequest): Promise<google.shopping.merchant.promotions.v1.Promotion>;

Calls GetPromotion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPromotionRequest](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.igetpromotionrequest)`   
GetPromotionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.promotions.v1.Promotion](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.promotion)>` | Promise  
  
### insertPromotion(request, callback)
    
    
    public insertPromotion(request: google.shopping.merchant.promotions.v1.IInsertPromotionRequest, callback: google.shopping.merchant.promotions.v1.PromotionsService.InsertPromotionCallback): void;

Calls InsertPromotion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertPromotionRequest](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.iinsertpromotionrequest)`   
InsertPromotionRequest message or plain object  
`callback` |  `[InsertPromotionCallback](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/overview.html)`   
Node-style callback called with the error, if any, and Promotion  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insertPromotion(request)
    
    
    public insertPromotion(request: google.shopping.merchant.promotions.v1.IInsertPromotionRequest): Promise<google.shopping.merchant.promotions.v1.Promotion>;

Calls InsertPromotion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IInsertPromotionRequest](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.iinsertpromotionrequest)`   
InsertPromotionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.promotions.v1.Promotion](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.promotion)>` | Promise  
  
### listPromotions(request, callback)
    
    
    public listPromotions(request: google.shopping.merchant.promotions.v1.IListPromotionsRequest, callback: google.shopping.merchant.promotions.v1.PromotionsService.ListPromotionsCallback): void;

Calls ListPromotions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPromotionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.ilistpromotionsrequest)`   
ListPromotionsRequest message or plain object  
`callback` |  `[ListPromotionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPromotionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPromotions(request)
    
    
    public listPromotions(request: google.shopping.merchant.promotions.v1.IListPromotionsRequest): Promise<google.shopping.merchant.promotions.v1.ListPromotionsResponse>;

Calls ListPromotions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPromotionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.ilistpromotionsrequest)`   
ListPromotionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.promotions.v1.ListPromotionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/promotions/latest/promotions/protos.google.shopping.merchant.promotions.v1.listpromotionsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
