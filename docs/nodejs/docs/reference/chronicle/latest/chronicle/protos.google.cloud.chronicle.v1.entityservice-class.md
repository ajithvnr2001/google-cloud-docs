---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.entityservice-class
title: Class protos.google.cloud.chronicle.v1.EntityService (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:32.246816+00:00
---

# Class protos.google.cloud.chronicle.v1.EntityService (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.entityservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.chronicle.v1.EntityService (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents an EntityService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.chronicle.v1.EntityService

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new EntityService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): EntityService;

Creates new EntityService service using the specified rpc implementation.

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
`[EntityService](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.entityservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createWatchlist(request, callback)
    
    
    public createWatchlist(request: google.cloud.chronicle.v1.ICreateWatchlistRequest, callback: google.cloud.chronicle.v1.EntityService.CreateWatchlistCallback): void;

Calls CreateWatchlist.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWatchlistRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.icreatewatchlistrequest)`   
CreateWatchlistRequest message or plain object  
`callback` |  `[CreateWatchlistCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and Watchlist  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createWatchlist(request)
    
    
    public createWatchlist(request: google.cloud.chronicle.v1.ICreateWatchlistRequest): Promise<google.cloud.chronicle.v1.Watchlist>;

Calls CreateWatchlist.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateWatchlistRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.icreatewatchlistrequest)`   
CreateWatchlistRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.Watchlist](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.watchlist-class)>` | Promise  
  
### deleteWatchlist(request, callback)
    
    
    public deleteWatchlist(request: google.cloud.chronicle.v1.IDeleteWatchlistRequest, callback: google.cloud.chronicle.v1.EntityService.DeleteWatchlistCallback): void;

Calls DeleteWatchlist.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWatchlistRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ideletewatchlistrequest)`   
DeleteWatchlistRequest message or plain object  
`callback` |  `[DeleteWatchlistCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteWatchlist(request)
    
    
    public deleteWatchlist(request: google.cloud.chronicle.v1.IDeleteWatchlistRequest): Promise<google.protobuf.Empty>;

Calls DeleteWatchlist.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWatchlistRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ideletewatchlistrequest)`   
DeleteWatchlistRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.protobuf.empty)>` | Promise  
  
### getWatchlist(request, callback)
    
    
    public getWatchlist(request: google.cloud.chronicle.v1.IGetWatchlistRequest, callback: google.cloud.chronicle.v1.EntityService.GetWatchlistCallback): void;

Calls GetWatchlist.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWatchlistRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetwatchlistrequest)`   
GetWatchlistRequest message or plain object  
`callback` |  `[GetWatchlistCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and Watchlist  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getWatchlist(request)
    
    
    public getWatchlist(request: google.cloud.chronicle.v1.IGetWatchlistRequest): Promise<google.cloud.chronicle.v1.Watchlist>;

Calls GetWatchlist.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetWatchlistRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetwatchlistrequest)`   
GetWatchlistRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.Watchlist](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.watchlist-class)>` | Promise  
  
### listWatchlists(request, callback)
    
    
    public listWatchlists(request: google.cloud.chronicle.v1.IListWatchlistsRequest, callback: google.cloud.chronicle.v1.EntityService.ListWatchlistsCallback): void;

Calls ListWatchlists.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWatchlistsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistwatchlistsrequest)`   
ListWatchlistsRequest message or plain object  
`callback` |  `[ListWatchlistsCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and ListWatchlistsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listWatchlists(request)
    
    
    public listWatchlists(request: google.cloud.chronicle.v1.IListWatchlistsRequest): Promise<google.cloud.chronicle.v1.ListWatchlistsResponse>;

Calls ListWatchlists.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListWatchlistsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistwatchlistsrequest)`   
ListWatchlistsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.ListWatchlistsResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.listwatchlistsresponse)>` | Promise  
  
### updateWatchlist(request, callback)
    
    
    public updateWatchlist(request: google.cloud.chronicle.v1.IUpdateWatchlistRequest, callback: google.cloud.chronicle.v1.EntityService.UpdateWatchlistCallback): void;

Calls UpdateWatchlist.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateWatchlistRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iupdatewatchlistrequest)`   
UpdateWatchlistRequest message or plain object  
`callback` |  `[UpdateWatchlistCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and Watchlist  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateWatchlist(request)
    
    
    public updateWatchlist(request: google.cloud.chronicle.v1.IUpdateWatchlistRequest): Promise<google.cloud.chronicle.v1.Watchlist>;

Calls UpdateWatchlist.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateWatchlistRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iupdatewatchlistrequest)`   
UpdateWatchlistRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.Watchlist](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.watchlist-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
