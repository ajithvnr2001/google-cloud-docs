---
url: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adreviewcenteradservice-class
title: Class protos.google.ads.admanager.v1.AdReviewCenterAdService (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:18:38.962115+00:00
---

# Class protos.google.ads.admanager.v1.AdReviewCenterAdService (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adreviewcenteradservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.admanager.v1.AdReviewCenterAdService (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.12.0  0.11.0  0.7.0  0.6.0  0.1.0 

Represents an AdReviewCenterAdService

## Inheritance

$protobuf.rpc.Service > protos.google.ads.admanager.v1.AdReviewCenterAdService

## Package

[@google-ads/admanager](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AdReviewCenterAdService service.

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

### batchAllowAdReviewCenterAds(request, callback)
    
    
    public batchAllowAdReviewCenterAds(request: google.ads.admanager.v1.IBatchAllowAdReviewCenterAdsRequest, callback: google.ads.admanager.v1.AdReviewCenterAdService.BatchAllowAdReviewCenterAdsCallback): void;

Calls BatchAllowAdReviewCenterAds.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchAllowAdReviewCenterAdsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchallowadreviewcenteradsrequest)`   
BatchAllowAdReviewCenterAdsRequest message or plain object  
`callback` |  `[BatchAllowAdReviewCenterAdsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchAllowAdReviewCenterAds(request)
    
    
    public batchAllowAdReviewCenterAds(request: google.ads.admanager.v1.IBatchAllowAdReviewCenterAdsRequest): Promise<google.longrunning.Operation>;

Calls BatchAllowAdReviewCenterAds.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchAllowAdReviewCenterAdsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchallowadreviewcenteradsrequest)`   
BatchAllowAdReviewCenterAdsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.longrunning.operation)>` | Promise  
  
### batchBlockAdReviewCenterAds(request, callback)
    
    
    public batchBlockAdReviewCenterAds(request: google.ads.admanager.v1.IBatchBlockAdReviewCenterAdsRequest, callback: google.ads.admanager.v1.AdReviewCenterAdService.BatchBlockAdReviewCenterAdsCallback): void;

Calls BatchBlockAdReviewCenterAds.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchBlockAdReviewCenterAdsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchblockadreviewcenteradsrequest)`   
BatchBlockAdReviewCenterAdsRequest message or plain object  
`callback` |  `[BatchBlockAdReviewCenterAdsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchBlockAdReviewCenterAds(request)
    
    
    public batchBlockAdReviewCenterAds(request: google.ads.admanager.v1.IBatchBlockAdReviewCenterAdsRequest): Promise<google.longrunning.Operation>;

Calls BatchBlockAdReviewCenterAds.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchBlockAdReviewCenterAdsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchblockadreviewcenteradsrequest)`   
BatchBlockAdReviewCenterAdsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.longrunning.operation)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AdReviewCenterAdService;

Creates new AdReviewCenterAdService service using the specified rpc implementation.

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
`[AdReviewCenterAdService](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adreviewcenteradservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### searchAdReviewCenterAds(request, callback)
    
    
    public searchAdReviewCenterAds(request: google.ads.admanager.v1.ISearchAdReviewCenterAdsRequest, callback: google.ads.admanager.v1.AdReviewCenterAdService.SearchAdReviewCenterAdsCallback): void;

Calls SearchAdReviewCenterAds.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchAdReviewCenterAdsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.isearchadreviewcenteradsrequest)`   
SearchAdReviewCenterAdsRequest message or plain object  
`callback` |  `[SearchAdReviewCenterAdsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchAdReviewCenterAdsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchAdReviewCenterAds(request)
    
    
    public searchAdReviewCenterAds(request: google.ads.admanager.v1.ISearchAdReviewCenterAdsRequest): Promise<google.ads.admanager.v1.SearchAdReviewCenterAdsResponse>;

Calls SearchAdReviewCenterAds.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchAdReviewCenterAdsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.isearchadreviewcenteradsrequest)`   
SearchAdReviewCenterAdsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.SearchAdReviewCenterAdsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.searchadreviewcenteradsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
