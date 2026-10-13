---
url: https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.metricsservicev2-class
title: Class protos.google.logging.v2.MetricsServiceV2 (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:28:06.515484+00:00
---

# Class protos.google.logging.v2.MetricsServiceV2 (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.metricsservicev2-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.logging.v2.MetricsServiceV2 (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a MetricsServiceV2

## Inheritance

$protobuf.rpc.Service > protos.google.logging.v2.MetricsServiceV2

## Package

[@google-cloud/logging-api](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new MetricsServiceV2 service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): MetricsServiceV2;

Creates new MetricsServiceV2 service using the specified rpc implementation.

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
`[MetricsServiceV2](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.metricsservicev2-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createLogMetric(request, callback)
    
    
    public createLogMetric(request: google.logging.v2.ICreateLogMetricRequest, callback: google.logging.v2.MetricsServiceV2.CreateLogMetricCallback): void;

Calls CreateLogMetric.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateLogMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.icreatelogmetricrequest)`   
CreateLogMetricRequest message or plain object  
`callback` |  `[CreateLogMetricCallback](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/overview.html)`   
Node-style callback called with the error, if any, and LogMetric  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createLogMetric(request)
    
    
    public createLogMetric(request: google.logging.v2.ICreateLogMetricRequest): Promise<google.logging.v2.LogMetric>;

Calls CreateLogMetric.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateLogMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.icreatelogmetricrequest)`   
CreateLogMetricRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.logging.v2.LogMetric](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.logmetric-class)>` | Promise  
  
### deleteLogMetric(request, callback)
    
    
    public deleteLogMetric(request: google.logging.v2.IDeleteLogMetricRequest, callback: google.logging.v2.MetricsServiceV2.DeleteLogMetricCallback): void;

Calls DeleteLogMetric.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteLogMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.ideletelogmetricrequest)`   
DeleteLogMetricRequest message or plain object  
`callback` |  `[DeleteLogMetricCallback](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteLogMetric(request)
    
    
    public deleteLogMetric(request: google.logging.v2.IDeleteLogMetricRequest): Promise<google.protobuf.Empty>;

Calls DeleteLogMetric.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteLogMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.ideletelogmetricrequest)`   
DeleteLogMetricRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.protobuf.empty)>` | Promise  
  
### getLogMetric(request, callback)
    
    
    public getLogMetric(request: google.logging.v2.IGetLogMetricRequest, callback: google.logging.v2.MetricsServiceV2.GetLogMetricCallback): void;

Calls GetLogMetric.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetLogMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.igetlogmetricrequest)`   
GetLogMetricRequest message or plain object  
`callback` |  `[GetLogMetricCallback](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/overview.html)`   
Node-style callback called with the error, if any, and LogMetric  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getLogMetric(request)
    
    
    public getLogMetric(request: google.logging.v2.IGetLogMetricRequest): Promise<google.logging.v2.LogMetric>;

Calls GetLogMetric.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetLogMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.igetlogmetricrequest)`   
GetLogMetricRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.logging.v2.LogMetric](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.logmetric-class)>` | Promise  
  
### listLogMetrics(request, callback)
    
    
    public listLogMetrics(request: google.logging.v2.IListLogMetricsRequest, callback: google.logging.v2.MetricsServiceV2.ListLogMetricsCallback): void;

Calls ListLogMetrics.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListLogMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.ilistlogmetricsrequest)`   
ListLogMetricsRequest message or plain object  
`callback` |  `[ListLogMetricsCallback](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/overview.html)`   
Node-style callback called with the error, if any, and ListLogMetricsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listLogMetrics(request)
    
    
    public listLogMetrics(request: google.logging.v2.IListLogMetricsRequest): Promise<google.logging.v2.ListLogMetricsResponse>;

Calls ListLogMetrics.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListLogMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.ilistlogmetricsrequest)`   
ListLogMetricsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.logging.v2.ListLogMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.listlogmetricsresponse)>` | Promise  
  
### updateLogMetric(request, callback)
    
    
    public updateLogMetric(request: google.logging.v2.IUpdateLogMetricRequest, callback: google.logging.v2.MetricsServiceV2.UpdateLogMetricCallback): void;

Calls UpdateLogMetric.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateLogMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.iupdatelogmetricrequest)`   
UpdateLogMetricRequest message or plain object  
`callback` |  `[UpdateLogMetricCallback](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/overview.html)`   
Node-style callback called with the error, if any, and LogMetric  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateLogMetric(request)
    
    
    public updateLogMetric(request: google.logging.v2.IUpdateLogMetricRequest): Promise<google.logging.v2.LogMetric>;

Calls UpdateLogMetric.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateLogMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.iupdatelogmetricrequest)`   
UpdateLogMetricRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.logging.v2.LogMetric](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.logmetric-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
