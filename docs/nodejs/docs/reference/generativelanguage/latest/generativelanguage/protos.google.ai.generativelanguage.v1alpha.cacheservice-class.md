---
url: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.cacheservice-class
title: Class protos.google.ai.generativelanguage.v1alpha.CacheService (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:17.559494+00:00
---

# Class protos.google.ai.generativelanguage.v1alpha.CacheService (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.cacheservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ai.generativelanguage.v1alpha.CacheService (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  4.1.0  3.7.0  3.6.0  2.9.0  2.8.0  2.7.0  2.6.0  2.4.0  2.3.0 

Represents a CacheService

## Inheritance

$protobuf.rpc.Service > protos.google.ai.generativelanguage.v1alpha.CacheService

## Package

[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new CacheService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): CacheService;

Creates new CacheService service using the specified rpc implementation.

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
`[CacheService](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.cacheservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createCachedContent(request, callback)
    
    
    public createCachedContent(request: google.ai.generativelanguage.v1alpha.ICreateCachedContentRequest, callback: google.ai.generativelanguage.v1alpha.CacheService.CreateCachedContentCallback): void;

Calls CreateCachedContent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatecachedcontentrequest)`   
CreateCachedContentRequest message or plain object  
`callback` |  `[CreateCachedContentCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and CachedContent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCachedContent(request)
    
    
    public createCachedContent(request: google.ai.generativelanguage.v1alpha.ICreateCachedContentRequest): Promise<google.ai.generativelanguage.v1alpha.CachedContent>;

Calls CreateCachedContent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatecachedcontentrequest)`   
CreateCachedContentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.CachedContent](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.cachedcontent-class)>` | Promise  
  
### deleteCachedContent(request, callback)
    
    
    public deleteCachedContent(request: google.ai.generativelanguage.v1alpha.IDeleteCachedContentRequest, callback: google.ai.generativelanguage.v1alpha.CacheService.DeleteCachedContentCallback): void;

Calls DeleteCachedContent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletecachedcontentrequest)`   
DeleteCachedContentRequest message or plain object  
`callback` |  `[DeleteCachedContentCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCachedContent(request)
    
    
    public deleteCachedContent(request: google.ai.generativelanguage.v1alpha.IDeleteCachedContentRequest): Promise<google.protobuf.Empty>;

Calls DeleteCachedContent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletecachedcontentrequest)`   
DeleteCachedContentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.empty)>` | Promise  
  
### getCachedContent(request, callback)
    
    
    public getCachedContent(request: google.ai.generativelanguage.v1alpha.IGetCachedContentRequest, callback: google.ai.generativelanguage.v1alpha.CacheService.GetCachedContentCallback): void;

Calls GetCachedContent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetcachedcontentrequest)`   
GetCachedContentRequest message or plain object  
`callback` |  `[GetCachedContentCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and CachedContent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCachedContent(request)
    
    
    public getCachedContent(request: google.ai.generativelanguage.v1alpha.IGetCachedContentRequest): Promise<google.ai.generativelanguage.v1alpha.CachedContent>;

Calls GetCachedContent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetcachedcontentrequest)`   
GetCachedContentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.CachedContent](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.cachedcontent-class)>` | Promise  
  
### listCachedContents(request, callback)
    
    
    public listCachedContents(request: google.ai.generativelanguage.v1alpha.IListCachedContentsRequest, callback: google.ai.generativelanguage.v1alpha.CacheService.ListCachedContentsCallback): void;

Calls ListCachedContents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCachedContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistcachedcontentsrequest)`   
ListCachedContentsRequest message or plain object  
`callback` |  `[ListCachedContentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCachedContentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCachedContents(request)
    
    
    public listCachedContents(request: google.ai.generativelanguage.v1alpha.IListCachedContentsRequest): Promise<google.ai.generativelanguage.v1alpha.ListCachedContentsResponse>;

Calls ListCachedContents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCachedContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistcachedcontentsrequest)`   
ListCachedContentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.ListCachedContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.listcachedcontentsresponse)>` | Promise  
  
### updateCachedContent(request, callback)
    
    
    public updateCachedContent(request: google.ai.generativelanguage.v1alpha.IUpdateCachedContentRequest, callback: google.ai.generativelanguage.v1alpha.CacheService.UpdateCachedContentCallback): void;

Calls UpdateCachedContent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatecachedcontentrequest)`   
UpdateCachedContentRequest message or plain object  
`callback` |  `[UpdateCachedContentCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and CachedContent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCachedContent(request)
    
    
    public updateCachedContent(request: google.ai.generativelanguage.v1alpha.IUpdateCachedContentRequest): Promise<google.ai.generativelanguage.v1alpha.CachedContent>;

Calls UpdateCachedContent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatecachedcontentrequest)`   
UpdateCachedContentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.CachedContent](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.cachedcontent-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
