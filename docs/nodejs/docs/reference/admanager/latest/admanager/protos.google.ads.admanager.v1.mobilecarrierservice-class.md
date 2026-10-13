---
url: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.mobilecarrierservice-class
title: Class protos.google.ads.admanager.v1.MobileCarrierService (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:18.223004+00:00
---

# Class protos.google.ads.admanager.v1.MobileCarrierService (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.mobilecarrierservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.admanager.v1.MobileCarrierService (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.12.0  0.11.0  0.7.0  0.6.0  0.1.0 

Represents a MobileCarrierService

## Inheritance

$protobuf.rpc.Service > protos.google.ads.admanager.v1.MobileCarrierService

## Package

[@google-ads/admanager](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new MobileCarrierService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): MobileCarrierService;

Creates new MobileCarrierService service using the specified rpc implementation.

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
`[MobileCarrierService](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.mobilecarrierservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### getMobileCarrier(request, callback)
    
    
    public getMobileCarrier(request: google.ads.admanager.v1.IGetMobileCarrierRequest, callback: google.ads.admanager.v1.MobileCarrierService.GetMobileCarrierCallback): void;

Calls GetMobileCarrier.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMobileCarrierRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.igetmobilecarrierrequest)`   
GetMobileCarrierRequest message or plain object  
`callback` |  `[GetMobileCarrierCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and MobileCarrier  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMobileCarrier(request)
    
    
    public getMobileCarrier(request: google.ads.admanager.v1.IGetMobileCarrierRequest): Promise<google.ads.admanager.v1.MobileCarrier>;

Calls GetMobileCarrier.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetMobileCarrierRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.igetmobilecarrierrequest)`   
GetMobileCarrierRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.MobileCarrier](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.mobilecarrier)>` | Promise  
  
### listMobileCarriers(request, callback)
    
    
    public listMobileCarriers(request: google.ads.admanager.v1.IListMobileCarriersRequest, callback: google.ads.admanager.v1.MobileCarrierService.ListMobileCarriersCallback): void;

Calls ListMobileCarriers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMobileCarriersRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistmobilecarriersrequest)`   
ListMobileCarriersRequest message or plain object  
`callback` |  `[ListMobileCarriersCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMobileCarriersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMobileCarriers(request)
    
    
    public listMobileCarriers(request: google.ads.admanager.v1.IListMobileCarriersRequest): Promise<google.ads.admanager.v1.ListMobileCarriersResponse>;

Calls ListMobileCarriers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMobileCarriersRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistmobilecarriersrequest)`   
ListMobileCarriersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.ListMobileCarriersResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.listmobilecarriersresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
