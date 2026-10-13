---
url: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.marketingdatainsightsservice-class
title: Class protos.google.ads.datamanager.v1.MarketingDataInsightsService (1.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:33:32.521936+00:00
---

# Class protos.google.ads.datamanager.v1.MarketingDataInsightsService (1.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.marketingdatainsightsservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.datamanager.v1.MarketingDataInsightsService (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.5.0  0.4.0  0.3.0  0.1.0 

Represents a MarketingDataInsightsService

## Inheritance

$protobuf.rpc.Service > protos.google.ads.datamanager.v1.MarketingDataInsightsService

## Package

[@google-ads/datamanager](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new MarketingDataInsightsService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): MarketingDataInsightsService;

Creates new MarketingDataInsightsService service using the specified rpc implementation.

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
`[MarketingDataInsightsService](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.marketingdatainsightsservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### retrieveInsights(request, callback)
    
    
    public retrieveInsights(request: google.ads.datamanager.v1.IRetrieveInsightsRequest, callback: google.ads.datamanager.v1.MarketingDataInsightsService.RetrieveInsightsCallback): void;

Calls RetrieveInsights.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRetrieveInsightsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iretrieveinsightsrequest)`   
RetrieveInsightsRequest message or plain object  
`callback` |  `[RetrieveInsightsCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and RetrieveInsightsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### retrieveInsights(request)
    
    
    public retrieveInsights(request: google.ads.datamanager.v1.IRetrieveInsightsRequest): Promise<google.ads.datamanager.v1.RetrieveInsightsResponse>;

Calls RetrieveInsights.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRetrieveInsightsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iretrieveinsightsrequest)`   
RetrieveInsightsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.RetrieveInsightsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.retrieveinsightsresponse-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
