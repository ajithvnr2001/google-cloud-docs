---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchartservice-class
title: Class protos.google.cloud.chronicle.v1.DashboardChartService (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:15.217073+00:00
---

# Class protos.google.cloud.chronicle.v1.DashboardChartService (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchartservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.chronicle.v1.DashboardChartService (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents a DashboardChartService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.chronicle.v1.DashboardChartService

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DashboardChartService service.

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

### batchGetDashboardCharts(request, callback)
    
    
    public batchGetDashboardCharts(request: google.cloud.chronicle.v1.IBatchGetDashboardChartsRequest, callback: google.cloud.chronicle.v1.DashboardChartService.BatchGetDashboardChartsCallback): void;

Calls BatchGetDashboardCharts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchGetDashboardChartsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ibatchgetdashboardchartsrequest)`   
BatchGetDashboardChartsRequest message or plain object  
`callback` |  `[BatchGetDashboardChartsCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchGetDashboardChartsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchGetDashboardCharts(request)
    
    
    public batchGetDashboardCharts(request: google.cloud.chronicle.v1.IBatchGetDashboardChartsRequest): Promise<google.cloud.chronicle.v1.BatchGetDashboardChartsResponse>;

Calls BatchGetDashboardCharts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchGetDashboardChartsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ibatchgetdashboardchartsrequest)`   
BatchGetDashboardChartsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.BatchGetDashboardChartsResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.batchgetdashboardchartsresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DashboardChartService;

Creates new DashboardChartService service using the specified rpc implementation.

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
`[DashboardChartService](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchartservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### getDashboardChart(request, callback)
    
    
    public getDashboardChart(request: google.cloud.chronicle.v1.IGetDashboardChartRequest, callback: google.cloud.chronicle.v1.DashboardChartService.GetDashboardChartCallback): void;

Calls GetDashboardChart.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDashboardChartRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetdashboardchartrequest)`   
GetDashboardChartRequest message or plain object  
`callback` |  `[GetDashboardChartCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and DashboardChart  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDashboardChart(request)
    
    
    public getDashboardChart(request: google.cloud.chronicle.v1.IGetDashboardChartRequest): Promise<google.cloud.chronicle.v1.DashboardChart>;

Calls GetDashboardChart.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDashboardChartRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetdashboardchartrequest)`   
GetDashboardChartRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.DashboardChart](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dashboardchart-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
