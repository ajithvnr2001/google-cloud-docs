---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardqueryservice-class
title: Class protos.google.cloud.chronicle.v1.DashboardQueryService (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:16.512461+00:00
---

# Class protos.google.cloud.chronicle.v1.DashboardQueryService (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardqueryservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.chronicle.v1.DashboardQueryService (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents a DashboardQueryService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.chronicle.v1.DashboardQueryService

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DashboardQueryService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DashboardQueryService;

Creates new DashboardQueryService service using the specified rpc implementation.

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
`[DashboardQueryService](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardqueryservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### executeDashboardQuery(request, callback)
    
    
    public executeDashboardQuery(request: google.cloud.chronicle.v1.IExecuteDashboardQueryRequest, callback: google.cloud.chronicle.v1.DashboardQueryService.ExecuteDashboardQueryCallback): void;

Calls ExecuteDashboardQuery.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExecuteDashboardQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iexecutedashboardqueryrequest)`   
ExecuteDashboardQueryRequest message or plain object  
`callback` |  `[ExecuteDashboardQueryCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and ExecuteDashboardQueryResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### executeDashboardQuery(request)
    
    
    public executeDashboardQuery(request: google.cloud.chronicle.v1.IExecuteDashboardQueryRequest): Promise<google.cloud.chronicle.v1.ExecuteDashboardQueryResponse>;

Calls ExecuteDashboardQuery.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExecuteDashboardQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iexecutedashboardqueryrequest)`   
ExecuteDashboardQueryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.ExecuteDashboardQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.executedashboardqueryresponse-class)>` | Promise  
  
### getDashboardQuery(request, callback)
    
    
    public getDashboardQuery(request: google.cloud.chronicle.v1.IGetDashboardQueryRequest, callback: google.cloud.chronicle.v1.DashboardQueryService.GetDashboardQueryCallback): void;

Calls GetDashboardQuery.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDashboardQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetdashboardqueryrequest)`   
GetDashboardQueryRequest message or plain object  
`callback` |  `[GetDashboardQueryCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and DashboardQuery  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDashboardQuery(request)
    
    
    public getDashboardQuery(request: google.cloud.chronicle.v1.IGetDashboardQueryRequest): Promise<google.cloud.chronicle.v1.DashboardQuery>;

Calls GetDashboardQuery.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDashboardQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetdashboardqueryrequest)`   
GetDashboardQueryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.DashboardQuery](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardquery-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
