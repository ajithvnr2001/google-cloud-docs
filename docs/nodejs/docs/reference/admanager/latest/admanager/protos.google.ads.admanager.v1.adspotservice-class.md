---
url: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adspotservice-class
title: Class protos.google.ads.admanager.v1.AdSpotService (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:18:44.103658+00:00
---

# Class protos.google.ads.admanager.v1.AdSpotService (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adspotservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.admanager.v1.AdSpotService (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.12.0  0.11.0  0.7.0  0.6.0  0.1.0 

Represents an AdSpotService

## Inheritance

$protobuf.rpc.Service > protos.google.ads.admanager.v1.AdSpotService

## Package

[@google-ads/admanager](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AdSpotService service.

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

### batchCreateAdSpots(request, callback)
    
    
    public batchCreateAdSpots(request: google.ads.admanager.v1.IBatchCreateAdSpotsRequest, callback: google.ads.admanager.v1.AdSpotService.BatchCreateAdSpotsCallback): void;

Calls BatchCreateAdSpots.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateAdSpotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchcreateadspotsrequest)`   
BatchCreateAdSpotsRequest message or plain object  
`callback` |  `[BatchCreateAdSpotsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchCreateAdSpotsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateAdSpots(request)
    
    
    public batchCreateAdSpots(request: google.ads.admanager.v1.IBatchCreateAdSpotsRequest): Promise<google.ads.admanager.v1.BatchCreateAdSpotsResponse>;

Calls BatchCreateAdSpots.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateAdSpotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchcreateadspotsrequest)`   
BatchCreateAdSpotsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchCreateAdSpotsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchcreateadspotsresponse)>` | Promise  
  
### batchUpdateAdSpots(request, callback)
    
    
    public batchUpdateAdSpots(request: google.ads.admanager.v1.IBatchUpdateAdSpotsRequest, callback: google.ads.admanager.v1.AdSpotService.BatchUpdateAdSpotsCallback): void;

Calls BatchUpdateAdSpots.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateAdSpotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchupdateadspotsrequest)`   
BatchUpdateAdSpotsRequest message or plain object  
`callback` |  `[BatchUpdateAdSpotsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchUpdateAdSpotsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchUpdateAdSpots(request)
    
    
    public batchUpdateAdSpots(request: google.ads.admanager.v1.IBatchUpdateAdSpotsRequest): Promise<google.ads.admanager.v1.BatchUpdateAdSpotsResponse>;

Calls BatchUpdateAdSpots.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateAdSpotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchupdateadspotsrequest)`   
BatchUpdateAdSpotsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchUpdateAdSpotsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchupdateadspotsresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AdSpotService;

Creates new AdSpotService service using the specified rpc implementation.

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
`[AdSpotService](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adspotservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAdSpot(request, callback)
    
    
    public createAdSpot(request: google.ads.admanager.v1.ICreateAdSpotRequest, callback: google.ads.admanager.v1.AdSpotService.CreateAdSpotCallback): void;

Calls CreateAdSpot.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAdSpotRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.icreateadspotrequest)`   
CreateAdSpotRequest message or plain object  
`callback` |  `[CreateAdSpotCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and AdSpot  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAdSpot(request)
    
    
    public createAdSpot(request: google.ads.admanager.v1.ICreateAdSpotRequest): Promise<google.ads.admanager.v1.AdSpot>;

Calls CreateAdSpot.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAdSpotRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.icreateadspotrequest)`   
CreateAdSpotRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.AdSpot](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adspot)>` | Promise  
  
### getAdSpot(request, callback)
    
    
    public getAdSpot(request: google.ads.admanager.v1.IGetAdSpotRequest, callback: google.ads.admanager.v1.AdSpotService.GetAdSpotCallback): void;

Calls GetAdSpot.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAdSpotRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.igetadspotrequest)`   
GetAdSpotRequest message or plain object  
`callback` |  `[GetAdSpotCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and AdSpot  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAdSpot(request)
    
    
    public getAdSpot(request: google.ads.admanager.v1.IGetAdSpotRequest): Promise<google.ads.admanager.v1.AdSpot>;

Calls GetAdSpot.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAdSpotRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.igetadspotrequest)`   
GetAdSpotRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.AdSpot](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adspot)>` | Promise  
  
### listAdSpots(request, callback)
    
    
    public listAdSpots(request: google.ads.admanager.v1.IListAdSpotsRequest, callback: google.ads.admanager.v1.AdSpotService.ListAdSpotsCallback): void;

Calls ListAdSpots.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAdSpotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistadspotsrequest)`   
ListAdSpotsRequest message or plain object  
`callback` |  `[ListAdSpotsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAdSpotsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAdSpots(request)
    
    
    public listAdSpots(request: google.ads.admanager.v1.IListAdSpotsRequest): Promise<google.ads.admanager.v1.ListAdSpotsResponse>;

Calls ListAdSpots.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAdSpotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistadspotsrequest)`   
ListAdSpotsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.ListAdSpotsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.listadspotsresponse)>` | Promise  
  
### updateAdSpot(request, callback)
    
    
    public updateAdSpot(request: google.ads.admanager.v1.IUpdateAdSpotRequest, callback: google.ads.admanager.v1.AdSpotService.UpdateAdSpotCallback): void;

Calls UpdateAdSpot.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAdSpotRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iupdateadspotrequest)`   
UpdateAdSpotRequest message or plain object  
`callback` |  `[UpdateAdSpotCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and AdSpot  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAdSpot(request)
    
    
    public updateAdSpot(request: google.ads.admanager.v1.IUpdateAdSpotRequest): Promise<google.ads.admanager.v1.AdSpot>;

Calls UpdateAdSpot.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAdSpotRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iupdateadspotrequest)`   
UpdateAdSpotRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.AdSpot](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adspot)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
