---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.featuredcontentnativedashboardservice-class
title: Class protos.google.cloud.chronicle.v1.FeaturedContentNativeDashboardService (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:34.552315+00:00
---

# Class protos.google.cloud.chronicle.v1.FeaturedContentNativeDashboardService (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.featuredcontentnativedashboardservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.chronicle.v1.FeaturedContentNativeDashboardService (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents a FeaturedContentNativeDashboardService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.chronicle.v1.FeaturedContentNativeDashboardService

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new FeaturedContentNativeDashboardService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): FeaturedContentNativeDashboardService;

Creates new FeaturedContentNativeDashboardService service using the specified rpc implementation.

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
`[FeaturedContentNativeDashboardService](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.featuredcontentnativedashboardservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### getFeaturedContentNativeDashboard(request, callback)
    
    
    public getFeaturedContentNativeDashboard(request: google.cloud.chronicle.v1.IGetFeaturedContentNativeDashboardRequest, callback: google.cloud.chronicle.v1.FeaturedContentNativeDashboardService.GetFeaturedContentNativeDashboardCallback): void;

Calls GetFeaturedContentNativeDashboard.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeaturedContentNativeDashboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetfeaturedcontentnativedashboardrequest)`   
GetFeaturedContentNativeDashboardRequest message or plain object  
`callback` |  `[GetFeaturedContentNativeDashboardCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and FeaturedContentNativeDashboard  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFeaturedContentNativeDashboard(request)
    
    
    public getFeaturedContentNativeDashboard(request: google.cloud.chronicle.v1.IGetFeaturedContentNativeDashboardRequest): Promise<google.cloud.chronicle.v1.FeaturedContentNativeDashboard>;

Calls GetFeaturedContentNativeDashboard.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetFeaturedContentNativeDashboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetfeaturedcontentnativedashboardrequest)`   
GetFeaturedContentNativeDashboardRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.FeaturedContentNativeDashboard](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.featuredcontentnativedashboard)>` | Promise  
  
### installFeaturedContentNativeDashboard(request, callback)
    
    
    public installFeaturedContentNativeDashboard(request: google.cloud.chronicle.v1.IInstallFeaturedContentNativeDashboardRequest, callback: google.cloud.chronicle.v1.FeaturedContentNativeDashboardService.InstallFeaturedContentNativeDashboardCallback): void;

Calls InstallFeaturedContentNativeDashboard.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInstallFeaturedContentNativeDashboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iinstallfeaturedcontentnativedashboardrequest)`   
InstallFeaturedContentNativeDashboardRequest message or plain object  
`callback` |  `[InstallFeaturedContentNativeDashboardCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and InstallFeaturedContentNativeDashboardResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### installFeaturedContentNativeDashboard(request)
    
    
    public installFeaturedContentNativeDashboard(request: google.cloud.chronicle.v1.IInstallFeaturedContentNativeDashboardRequest): Promise<google.cloud.chronicle.v1.InstallFeaturedContentNativeDashboardResponse>;

Calls InstallFeaturedContentNativeDashboard.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IInstallFeaturedContentNativeDashboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iinstallfeaturedcontentnativedashboardrequest)`   
InstallFeaturedContentNativeDashboardRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.InstallFeaturedContentNativeDashboardResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.installfeaturedcontentnativedashboardresponse)>` | Promise  
  
### listFeaturedContentNativeDashboards(request, callback)
    
    
    public listFeaturedContentNativeDashboards(request: google.cloud.chronicle.v1.IListFeaturedContentNativeDashboardsRequest, callback: google.cloud.chronicle.v1.FeaturedContentNativeDashboardService.ListFeaturedContentNativeDashboardsCallback): void;

Calls ListFeaturedContentNativeDashboards.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeaturedContentNativeDashboardsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistfeaturedcontentnativedashboardsrequest)`   
ListFeaturedContentNativeDashboardsRequest message or plain object  
`callback` |  `[ListFeaturedContentNativeDashboardsCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and ListFeaturedContentNativeDashboardsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFeaturedContentNativeDashboards(request)
    
    
    public listFeaturedContentNativeDashboards(request: google.cloud.chronicle.v1.IListFeaturedContentNativeDashboardsRequest): Promise<google.cloud.chronicle.v1.ListFeaturedContentNativeDashboardsResponse>;

Calls ListFeaturedContentNativeDashboards.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListFeaturedContentNativeDashboardsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistfeaturedcontentnativedashboardsrequest)`   
ListFeaturedContentNativeDashboardsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.ListFeaturedContentNativeDashboardsResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.listfeaturedcontentnativedashboardsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
