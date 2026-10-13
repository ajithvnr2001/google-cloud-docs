---
url: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adbreakservice-class
title: Class protos.google.ads.admanager.v1.AdBreakService (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:18:34.949081+00:00
---

# Class protos.google.ads.admanager.v1.AdBreakService (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adbreakservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.admanager.v1.AdBreakService (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.12.0  0.11.0  0.7.0  0.6.0  0.1.0 

Represents an AdBreakService

## Inheritance

$protobuf.rpc.Service > protos.google.ads.admanager.v1.AdBreakService

## Package

[@google-ads/admanager](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AdBreakService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AdBreakService;

Creates new AdBreakService service using the specified rpc implementation.

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
`[AdBreakService](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adbreakservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAdBreak(request, callback)
    
    
    public createAdBreak(request: google.ads.admanager.v1.ICreateAdBreakRequest, callback: google.ads.admanager.v1.AdBreakService.CreateAdBreakCallback): void;

Calls CreateAdBreak.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAdBreakRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.icreateadbreakrequest)`   
CreateAdBreakRequest message or plain object  
`callback` |  `[CreateAdBreakCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and AdBreak  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAdBreak(request)
    
    
    public createAdBreak(request: google.ads.admanager.v1.ICreateAdBreakRequest): Promise<google.ads.admanager.v1.AdBreak>;

Calls CreateAdBreak.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAdBreakRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.icreateadbreakrequest)`   
CreateAdBreakRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.AdBreak](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adbreak)>` | Promise  
  
### deleteAdBreak(request, callback)
    
    
    public deleteAdBreak(request: google.ads.admanager.v1.IDeleteAdBreakRequest, callback: google.ads.admanager.v1.AdBreakService.DeleteAdBreakCallback): void;

Calls DeleteAdBreak.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAdBreakRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ideleteadbreakrequest)`   
DeleteAdBreakRequest message or plain object  
`callback` |  `[DeleteAdBreakCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAdBreak(request)
    
    
    public deleteAdBreak(request: google.ads.admanager.v1.IDeleteAdBreakRequest): Promise<google.protobuf.Empty>;

Calls DeleteAdBreak.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAdBreakRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ideleteadbreakrequest)`   
DeleteAdBreakRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.protobuf.empty)>` | Promise  
  
### getAdBreak(request, callback)
    
    
    public getAdBreak(request: google.ads.admanager.v1.IGetAdBreakRequest, callback: google.ads.admanager.v1.AdBreakService.GetAdBreakCallback): void;

Calls GetAdBreak.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAdBreakRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.igetadbreakrequest)`   
GetAdBreakRequest message or plain object  
`callback` |  `[GetAdBreakCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and AdBreak  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAdBreak(request)
    
    
    public getAdBreak(request: google.ads.admanager.v1.IGetAdBreakRequest): Promise<google.ads.admanager.v1.AdBreak>;

Calls GetAdBreak.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAdBreakRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.igetadbreakrequest)`   
GetAdBreakRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.AdBreak](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adbreak)>` | Promise  
  
### listAdBreaks(request, callback)
    
    
    public listAdBreaks(request: google.ads.admanager.v1.IListAdBreaksRequest, callback: google.ads.admanager.v1.AdBreakService.ListAdBreaksCallback): void;

Calls ListAdBreaks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAdBreaksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistadbreaksrequest)`   
ListAdBreaksRequest message or plain object  
`callback` |  `[ListAdBreaksCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAdBreaksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAdBreaks(request)
    
    
    public listAdBreaks(request: google.ads.admanager.v1.IListAdBreaksRequest): Promise<google.ads.admanager.v1.ListAdBreaksResponse>;

Calls ListAdBreaks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAdBreaksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistadbreaksrequest)`   
ListAdBreaksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.ListAdBreaksResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.listadbreaksresponse)>` | Promise  
  
### updateAdBreak(request, callback)
    
    
    public updateAdBreak(request: google.ads.admanager.v1.IUpdateAdBreakRequest, callback: google.ads.admanager.v1.AdBreakService.UpdateAdBreakCallback): void;

Calls UpdateAdBreak.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAdBreakRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iupdateadbreakrequest)`   
UpdateAdBreakRequest message or plain object  
`callback` |  `[UpdateAdBreakCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and AdBreak  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAdBreak(request)
    
    
    public updateAdBreak(request: google.ads.admanager.v1.IUpdateAdBreakRequest): Promise<google.ads.admanager.v1.AdBreak>;

Calls UpdateAdBreak.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAdBreakRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iupdateadbreakrequest)`   
UpdateAdBreakRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.AdBreak](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adbreak)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
