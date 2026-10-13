---
url: https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/ordertracking/protos.google.shopping.merchant.ordertracking.v1.ordertrackingsignalsservice-class
title: Class protos.google.shopping.merchant.ordertracking.v1.OrderTrackingSignalsService (0.5.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:10.010818+00:00
---

# Class protos.google.shopping.merchant.ordertracking.v1.OrderTrackingSignalsService (0.5.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/ordertracking/protos.google.shopping.merchant.ordertracking.v1.ordertrackingsignalsservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.ordertracking.v1.OrderTrackingSignalsService (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.4.0 

Represents an OrderTrackingSignalsService

## Inheritance

$protobuf.rpc.Service > protos.google.shopping.merchant.ordertracking.v1.OrderTrackingSignalsService

## Package

[@google-shopping/ordertracking](https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new OrderTrackingSignalsService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): OrderTrackingSignalsService;

Creates new OrderTrackingSignalsService service using the specified rpc implementation.

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
`[OrderTrackingSignalsService](https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/ordertracking/protos.google.shopping.merchant.ordertracking.v1.ordertrackingsignalsservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createOrderTrackingSignal(request, callback)
    
    
    public createOrderTrackingSignal(request: google.shopping.merchant.ordertracking.v1.ICreateOrderTrackingSignalRequest, callback: google.shopping.merchant.ordertracking.v1.OrderTrackingSignalsService.CreateOrderTrackingSignalCallback): void;

Calls CreateOrderTrackingSignal.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateOrderTrackingSignalRequest](https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/ordertracking/protos.google.shopping.merchant.ordertracking.v1.icreateordertrackingsignalrequest)`   
CreateOrderTrackingSignalRequest message or plain object  
`callback` |  `[CreateOrderTrackingSignalCallback](https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/overview.html)`   
Node-style callback called with the error, if any, and OrderTrackingSignal  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createOrderTrackingSignal(request)
    
    
    public createOrderTrackingSignal(request: google.shopping.merchant.ordertracking.v1.ICreateOrderTrackingSignalRequest): Promise<google.shopping.merchant.ordertracking.v1.OrderTrackingSignal>;

Calls CreateOrderTrackingSignal.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateOrderTrackingSignalRequest](https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/ordertracking/protos.google.shopping.merchant.ordertracking.v1.icreateordertrackingsignalrequest)`   
CreateOrderTrackingSignalRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.ordertracking.v1.OrderTrackingSignal](https://docs.cloud.google.com/nodejs/docs/reference/ordertracking/latest/ordertracking/protos.google.shopping.merchant.ordertracking.v1.ordertrackingsignal-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
