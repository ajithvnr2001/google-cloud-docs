---
url: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datapointsservice-class
title: Class protos.google.devicesandservices.health.v4.DataPointsService (0.8.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:12.948671+00:00
---

# Class protos.google.devicesandservices.health.v4.DataPointsService (0.8.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datapointsservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.devicesandservices.health.v4.DataPointsService (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a DataPointsService

## Inheritance

$protobuf.rpc.Service > protos.google.devicesandservices.health.v4.DataPointsService

## Package

[@google-cloud/health](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DataPointsService service.

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

### batchDeleteDataPoints(request, callback)
    
    
    public batchDeleteDataPoints(request: google.devicesandservices.health.v4.IBatchDeleteDataPointsRequest, callback: google.devicesandservices.health.v4.DataPointsService.BatchDeleteDataPointsCallback): void;

Calls BatchDeleteDataPoints.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteDataPointsRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ibatchdeletedatapointsrequest)`   
BatchDeleteDataPointsRequest message or plain object  
`callback` |  `[BatchDeleteDataPointsCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchDeleteDataPoints(request)
    
    
    public batchDeleteDataPoints(request: google.devicesandservices.health.v4.IBatchDeleteDataPointsRequest): Promise<google.longrunning.Operation>;

Calls BatchDeleteDataPoints.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteDataPointsRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ibatchdeletedatapointsrequest)`   
BatchDeleteDataPointsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.longrunning.operation)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DataPointsService;

Creates new DataPointsService service using the specified rpc implementation.

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
`[DataPointsService](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datapointsservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createDataPoint(request, callback)
    
    
    public createDataPoint(request: google.devicesandservices.health.v4.ICreateDataPointRequest, callback: google.devicesandservices.health.v4.DataPointsService.CreateDataPointCallback): void;

Calls CreateDataPoint.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataPointRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.icreatedatapointrequest)`   
CreateDataPointRequest message or plain object  
`callback` |  `[CreateDataPointCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataPoint(request)
    
    
    public createDataPoint(request: google.devicesandservices.health.v4.ICreateDataPointRequest): Promise<google.longrunning.Operation>;

Calls CreateDataPoint.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataPointRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.icreatedatapointrequest)`   
CreateDataPointRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.longrunning.operation)>` | Promise  
  
### dailyRollUpDataPoints(request, callback)
    
    
    public dailyRollUpDataPoints(request: google.devicesandservices.health.v4.IDailyRollUpDataPointsRequest, callback: google.devicesandservices.health.v4.DataPointsService.DailyRollUpDataPointsCallback): void;

Calls DailyRollUpDataPoints.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDailyRollUpDataPointsRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.idailyrollupdatapointsrequest)`   
DailyRollUpDataPointsRequest message or plain object  
`callback` |  `[DailyRollUpDataPointsCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and DailyRollUpDataPointsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### dailyRollUpDataPoints(request)
    
    
    public dailyRollUpDataPoints(request: google.devicesandservices.health.v4.IDailyRollUpDataPointsRequest): Promise<google.devicesandservices.health.v4.DailyRollUpDataPointsResponse>;

Calls DailyRollUpDataPoints.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDailyRollUpDataPointsRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.idailyrollupdatapointsrequest)`   
DailyRollUpDataPointsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.devicesandservices.health.v4.DailyRollUpDataPointsResponse](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailyrollupdatapointsresponse)>` | Promise  
  
### exportExerciseTcx(request, callback)
    
    
    public exportExerciseTcx(request: google.devicesandservices.health.v4.IExportExerciseTcxRequest, callback: google.devicesandservices.health.v4.DataPointsService.ExportExerciseTcxCallback): void;

Calls ExportExerciseTcx.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportExerciseTcxRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.iexportexercisetcxrequest)`   
ExportExerciseTcxRequest message or plain object  
`callback` |  `[ExportExerciseTcxCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and ExportExerciseTcxResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportExerciseTcx(request)
    
    
    public exportExerciseTcx(request: google.devicesandservices.health.v4.IExportExerciseTcxRequest): Promise<google.devicesandservices.health.v4.ExportExerciseTcxResponse>;

Calls ExportExerciseTcx.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportExerciseTcxRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.iexportexercisetcxrequest)`   
ExportExerciseTcxRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.devicesandservices.health.v4.ExportExerciseTcxResponse](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.exportexercisetcxresponse)>` | Promise  
  
### getDataPoint(request, callback)
    
    
    public getDataPoint(request: google.devicesandservices.health.v4.IGetDataPointRequest, callback: google.devicesandservices.health.v4.DataPointsService.GetDataPointCallback): void;

Calls GetDataPoint.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataPointRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.igetdatapointrequest)`   
GetDataPointRequest message or plain object  
`callback` |  `[GetDataPointCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and DataPoint  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataPoint(request)
    
    
    public getDataPoint(request: google.devicesandservices.health.v4.IGetDataPointRequest): Promise<google.devicesandservices.health.v4.DataPoint>;

Calls GetDataPoint.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataPointRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.igetdatapointrequest)`   
GetDataPointRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.devicesandservices.health.v4.DataPoint](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datapoint)>` | Promise  
  
### listDataPoints(request, callback)
    
    
    public listDataPoints(request: google.devicesandservices.health.v4.IListDataPointsRequest, callback: google.devicesandservices.health.v4.DataPointsService.ListDataPointsCallback): void;

Calls ListDataPoints.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataPointsRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ilistdatapointsrequest)`   
ListDataPointsRequest message or plain object  
`callback` |  `[ListDataPointsCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDataPointsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataPoints(request)
    
    
    public listDataPoints(request: google.devicesandservices.health.v4.IListDataPointsRequest): Promise<google.devicesandservices.health.v4.ListDataPointsResponse>;

Calls ListDataPoints.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDataPointsRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ilistdatapointsrequest)`   
ListDataPointsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.devicesandservices.health.v4.ListDataPointsResponse](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.listdatapointsresponse)>` | Promise  
  
### reconcileDataPoints(request, callback)
    
    
    public reconcileDataPoints(request: google.devicesandservices.health.v4.IReconcileDataPointsRequest, callback: google.devicesandservices.health.v4.DataPointsService.ReconcileDataPointsCallback): void;

Calls ReconcileDataPoints.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReconcileDataPointsRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ireconciledatapointsrequest)`   
ReconcileDataPointsRequest message or plain object  
`callback` |  `[ReconcileDataPointsCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and ReconcileDataPointsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### reconcileDataPoints(request)
    
    
    public reconcileDataPoints(request: google.devicesandservices.health.v4.IReconcileDataPointsRequest): Promise<google.devicesandservices.health.v4.ReconcileDataPointsResponse>;

Calls ReconcileDataPoints.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IReconcileDataPointsRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ireconciledatapointsrequest)`   
ReconcileDataPointsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.devicesandservices.health.v4.ReconcileDataPointsResponse](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.reconciledatapointsresponse)>` | Promise  
  
### rollUpDataPoints(request, callback)
    
    
    public rollUpDataPoints(request: google.devicesandservices.health.v4.IRollUpDataPointsRequest, callback: google.devicesandservices.health.v4.DataPointsService.RollUpDataPointsCallback): void;

Calls RollUpDataPoints.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRollUpDataPointsRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.irollupdatapointsrequest)`   
RollUpDataPointsRequest message or plain object  
`callback` |  `[RollUpDataPointsCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and RollUpDataPointsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### rollUpDataPoints(request)
    
    
    public rollUpDataPoints(request: google.devicesandservices.health.v4.IRollUpDataPointsRequest): Promise<google.devicesandservices.health.v4.RollUpDataPointsResponse>;

Calls RollUpDataPoints.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRollUpDataPointsRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.irollupdatapointsrequest)`   
RollUpDataPointsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.devicesandservices.health.v4.RollUpDataPointsResponse](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.rollupdatapointsresponse)>` | Promise  
  
### updateDataPoint(request, callback)
    
    
    public updateDataPoint(request: google.devicesandservices.health.v4.IUpdateDataPointRequest, callback: google.devicesandservices.health.v4.DataPointsService.UpdateDataPointCallback): void;

Calls UpdateDataPoint.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataPointRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.iupdatedatapointrequest)`   
UpdateDataPointRequest message or plain object  
`callback` |  `[UpdateDataPointCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataPoint(request)
    
    
    public updateDataPoint(request: google.devicesandservices.health.v4.IUpdateDataPointRequest): Promise<google.longrunning.Operation>;

Calls UpdateDataPoint.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataPointRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.iupdatedatapointrequest)`   
UpdateDataPointRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
