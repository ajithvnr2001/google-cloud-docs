---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataplexservice-class
title: Class protos.google.cloud.dataplex.v1.DataplexService (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:33:42.908656+00:00
---

# Class protos.google.cloud.dataplex.v1.DataplexService (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataplexservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataplex.v1.DataplexService (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.4.0  5.3.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.5.1  3.2.0  3.1.0  2.4.0  2.3.2  2.2.2  2.1.1  1.2.0  1.1.0  1.0.0 

Represents a DataplexService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dataplex.v1.DataplexService

## Package

[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DataplexService service.

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

### cancelJob(request, callback)
    
    
    public cancelJob(request: google.cloud.dataplex.v1.ICancelJobRequest, callback: google.cloud.dataplex.v1.DataplexService.CancelJobCallback): void;

Calls CancelJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icanceljobrequest)`   
CancelJobRequest message or plain object  
`callback` |  `[CancelJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelJob(request)
    
    
    public cancelJob(request: google.cloud.dataplex.v1.ICancelJobRequest): Promise<google.protobuf.Empty>;

Calls CancelJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICancelJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icanceljobrequest)`   
CancelJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.protobuf.empty)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DataplexService;

Creates new DataplexService service using the specified rpc implementation.

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
`[DataplexService](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.dataplexservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAsset(request, callback)
    
    
    public createAsset(request: google.cloud.dataplex.v1.ICreateAssetRequest, callback: google.cloud.dataplex.v1.DataplexService.CreateAssetCallback): void;

Calls CreateAsset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreateassetrequest)`   
CreateAssetRequest message or plain object  
`callback` |  `[CreateAssetCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAsset(request)
    
    
    public createAsset(request: google.cloud.dataplex.v1.ICreateAssetRequest): Promise<google.longrunning.Operation>;

Calls CreateAsset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreateassetrequest)`   
CreateAssetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### createLake(request, callback)
    
    
    public createLake(request: google.cloud.dataplex.v1.ICreateLakeRequest, callback: google.cloud.dataplex.v1.DataplexService.CreateLakeCallback): void;

Calls CreateLake.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateLakeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatelakerequest)`   
CreateLakeRequest message or plain object  
`callback` |  `[CreateLakeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createLake(request)
    
    
    public createLake(request: google.cloud.dataplex.v1.ICreateLakeRequest): Promise<google.longrunning.Operation>;

Calls CreateLake.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateLakeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatelakerequest)`   
CreateLakeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### createTask(request, callback)
    
    
    public createTask(request: google.cloud.dataplex.v1.ICreateTaskRequest, callback: google.cloud.dataplex.v1.DataplexService.CreateTaskCallback): void;

Calls CreateTask.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatetaskrequest)`   
CreateTaskRequest message or plain object  
`callback` |  `[CreateTaskCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTask(request)
    
    
    public createTask(request: google.cloud.dataplex.v1.ICreateTaskRequest): Promise<google.longrunning.Operation>;

Calls CreateTask.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatetaskrequest)`   
CreateTaskRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### createZone(request, callback)
    
    
    public createZone(request: google.cloud.dataplex.v1.ICreateZoneRequest, callback: google.cloud.dataplex.v1.DataplexService.CreateZoneCallback): void;

Calls CreateZone.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatezonerequest)`   
CreateZoneRequest message or plain object  
`callback` |  `[CreateZoneCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createZone(request)
    
    
    public createZone(request: google.cloud.dataplex.v1.ICreateZoneRequest): Promise<google.longrunning.Operation>;

Calls CreateZone.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatezonerequest)`   
CreateZoneRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### deleteAsset(request, callback)
    
    
    public deleteAsset(request: google.cloud.dataplex.v1.IDeleteAssetRequest, callback: google.cloud.dataplex.v1.DataplexService.DeleteAssetCallback): void;

Calls DeleteAsset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideleteassetrequest)`   
DeleteAssetRequest message or plain object  
`callback` |  `[DeleteAssetCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAsset(request)
    
    
    public deleteAsset(request: google.cloud.dataplex.v1.IDeleteAssetRequest): Promise<google.longrunning.Operation>;

Calls DeleteAsset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideleteassetrequest)`   
DeleteAssetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### deleteLake(request, callback)
    
    
    public deleteLake(request: google.cloud.dataplex.v1.IDeleteLakeRequest, callback: google.cloud.dataplex.v1.DataplexService.DeleteLakeCallback): void;

Calls DeleteLake.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteLakeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideletelakerequest)`   
DeleteLakeRequest message or plain object  
`callback` |  `[DeleteLakeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteLake(request)
    
    
    public deleteLake(request: google.cloud.dataplex.v1.IDeleteLakeRequest): Promise<google.longrunning.Operation>;

Calls DeleteLake.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteLakeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideletelakerequest)`   
DeleteLakeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### deleteTask(request, callback)
    
    
    public deleteTask(request: google.cloud.dataplex.v1.IDeleteTaskRequest, callback: google.cloud.dataplex.v1.DataplexService.DeleteTaskCallback): void;

Calls DeleteTask.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideletetaskrequest)`   
DeleteTaskRequest message or plain object  
`callback` |  `[DeleteTaskCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTask(request)
    
    
    public deleteTask(request: google.cloud.dataplex.v1.IDeleteTaskRequest): Promise<google.longrunning.Operation>;

Calls DeleteTask.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideletetaskrequest)`   
DeleteTaskRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### deleteZone(request, callback)
    
    
    public deleteZone(request: google.cloud.dataplex.v1.IDeleteZoneRequest, callback: google.cloud.dataplex.v1.DataplexService.DeleteZoneCallback): void;

Calls DeleteZone.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideletezonerequest)`   
DeleteZoneRequest message or plain object  
`callback` |  `[DeleteZoneCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteZone(request)
    
    
    public deleteZone(request: google.cloud.dataplex.v1.IDeleteZoneRequest): Promise<google.longrunning.Operation>;

Calls DeleteZone.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideletezonerequest)`   
DeleteZoneRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### getAsset(request, callback)
    
    
    public getAsset(request: google.cloud.dataplex.v1.IGetAssetRequest, callback: google.cloud.dataplex.v1.DataplexService.GetAssetCallback): void;

Calls GetAsset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetassetrequest)`   
GetAssetRequest message or plain object  
`callback` |  `[GetAssetCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Asset  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAsset(request)
    
    
    public getAsset(request: google.cloud.dataplex.v1.IGetAssetRequest): Promise<google.cloud.dataplex.v1.Asset>;

Calls GetAsset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetassetrequest)`   
GetAssetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.Asset](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.asset-class)>` | Promise  
  
### getJob(request, callback)
    
    
    public getJob(request: google.cloud.dataplex.v1.IGetJobRequest, callback: google.cloud.dataplex.v1.DataplexService.GetJobCallback): void;

Calls GetJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetjobrequest)`   
GetJobRequest message or plain object  
`callback` |  `[GetJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Job  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getJob(request)
    
    
    public getJob(request: google.cloud.dataplex.v1.IGetJobRequest): Promise<google.cloud.dataplex.v1.Job>;

Calls GetJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetjobrequest)`   
GetJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.Job](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.job-class)>` | Promise  
  
### getLake(request, callback)
    
    
    public getLake(request: google.cloud.dataplex.v1.IGetLakeRequest, callback: google.cloud.dataplex.v1.DataplexService.GetLakeCallback): void;

Calls GetLake.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetLakeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetlakerequest)`   
GetLakeRequest message or plain object  
`callback` |  `[GetLakeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Lake  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getLake(request)
    
    
    public getLake(request: google.cloud.dataplex.v1.IGetLakeRequest): Promise<google.cloud.dataplex.v1.Lake>;

Calls GetLake.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetLakeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetlakerequest)`   
GetLakeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.Lake](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.lake-class)>` | Promise  
  
### getTask(request, callback)
    
    
    public getTask(request: google.cloud.dataplex.v1.IGetTaskRequest, callback: google.cloud.dataplex.v1.DataplexService.GetTaskCallback): void;

Calls GetTask.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igettaskrequest)`   
GetTaskRequest message or plain object  
`callback` |  `[GetTaskCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Task  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTask(request)
    
    
    public getTask(request: google.cloud.dataplex.v1.IGetTaskRequest): Promise<google.cloud.dataplex.v1.Task>;

Calls GetTask.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igettaskrequest)`   
GetTaskRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.Task](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.task-class)>` | Promise  
  
### getZone(request, callback)
    
    
    public getZone(request: google.cloud.dataplex.v1.IGetZoneRequest, callback: google.cloud.dataplex.v1.DataplexService.GetZoneCallback): void;

Calls GetZone.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetzonerequest)`   
GetZoneRequest message or plain object  
`callback` |  `[GetZoneCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Zone  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getZone(request)
    
    
    public getZone(request: google.cloud.dataplex.v1.IGetZoneRequest): Promise<google.cloud.dataplex.v1.Zone>;

Calls GetZone.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetzonerequest)`   
GetZoneRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.Zone](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.zone-class)>` | Promise  
  
### listAssetActions(request, callback)
    
    
    public listAssetActions(request: google.cloud.dataplex.v1.IListAssetActionsRequest, callback: google.cloud.dataplex.v1.DataplexService.ListAssetActionsCallback): void;

Calls ListAssetActions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAssetActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistassetactionsrequest)`   
ListAssetActionsRequest message or plain object  
`callback` |  `[ListAssetActionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListActionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAssetActions(request)
    
    
    public listAssetActions(request: google.cloud.dataplex.v1.IListAssetActionsRequest): Promise<google.cloud.dataplex.v1.ListActionsResponse>;

Calls ListAssetActions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAssetActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistassetactionsrequest)`   
ListAssetActionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListActionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listactionsresponse)>` | Promise  
  
### listAssets(request, callback)
    
    
    public listAssets(request: google.cloud.dataplex.v1.IListAssetsRequest, callback: google.cloud.dataplex.v1.DataplexService.ListAssetsCallback): void;

Calls ListAssets.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAssetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistassetsrequest)`   
ListAssetsRequest message or plain object  
`callback` |  `[ListAssetsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAssetsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAssets(request)
    
    
    public listAssets(request: google.cloud.dataplex.v1.IListAssetsRequest): Promise<google.cloud.dataplex.v1.ListAssetsResponse>;

Calls ListAssets.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAssetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistassetsrequest)`   
ListAssetsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListAssetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listassetsresponse)>` | Promise  
  
### listJobs(request, callback)
    
    
    public listJobs(request: google.cloud.dataplex.v1.IListJobsRequest, callback: google.cloud.dataplex.v1.DataplexService.ListJobsCallback): void;

Calls ListJobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistjobsrequest)`   
ListJobsRequest message or plain object  
`callback` |  `[ListJobsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListJobsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listJobs(request)
    
    
    public listJobs(request: google.cloud.dataplex.v1.IListJobsRequest): Promise<google.cloud.dataplex.v1.ListJobsResponse>;

Calls ListJobs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistjobsrequest)`   
ListJobsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listjobsresponse)>` | Promise  
  
### listLakeActions(request, callback)
    
    
    public listLakeActions(request: google.cloud.dataplex.v1.IListLakeActionsRequest, callback: google.cloud.dataplex.v1.DataplexService.ListLakeActionsCallback): void;

Calls ListLakeActions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListLakeActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistlakeactionsrequest)`   
ListLakeActionsRequest message or plain object  
`callback` |  `[ListLakeActionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListActionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listLakeActions(request)
    
    
    public listLakeActions(request: google.cloud.dataplex.v1.IListLakeActionsRequest): Promise<google.cloud.dataplex.v1.ListActionsResponse>;

Calls ListLakeActions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListLakeActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistlakeactionsrequest)`   
ListLakeActionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListActionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listactionsresponse)>` | Promise  
  
### listLakes(request, callback)
    
    
    public listLakes(request: google.cloud.dataplex.v1.IListLakesRequest, callback: google.cloud.dataplex.v1.DataplexService.ListLakesCallback): void;

Calls ListLakes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListLakesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistlakesrequest)`   
ListLakesRequest message or plain object  
`callback` |  `[ListLakesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListLakesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listLakes(request)
    
    
    public listLakes(request: google.cloud.dataplex.v1.IListLakesRequest): Promise<google.cloud.dataplex.v1.ListLakesResponse>;

Calls ListLakes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListLakesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistlakesrequest)`   
ListLakesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListLakesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listlakesresponse)>` | Promise  
  
### listTasks(request, callback)
    
    
    public listTasks(request: google.cloud.dataplex.v1.IListTasksRequest, callback: google.cloud.dataplex.v1.DataplexService.ListTasksCallback): void;

Calls ListTasks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilisttasksrequest)`   
ListTasksRequest message or plain object  
`callback` |  `[ListTasksCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListTasksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTasks(request)
    
    
    public listTasks(request: google.cloud.dataplex.v1.IListTasksRequest): Promise<google.cloud.dataplex.v1.ListTasksResponse>;

Calls ListTasks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListTasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilisttasksrequest)`   
ListTasksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListTasksResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listtasksresponse)>` | Promise  
  
### listZoneActions(request, callback)
    
    
    public listZoneActions(request: google.cloud.dataplex.v1.IListZoneActionsRequest, callback: google.cloud.dataplex.v1.DataplexService.ListZoneActionsCallback): void;

Calls ListZoneActions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListZoneActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistzoneactionsrequest)`   
ListZoneActionsRequest message or plain object  
`callback` |  `[ListZoneActionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListActionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listZoneActions(request)
    
    
    public listZoneActions(request: google.cloud.dataplex.v1.IListZoneActionsRequest): Promise<google.cloud.dataplex.v1.ListActionsResponse>;

Calls ListZoneActions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListZoneActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistzoneactionsrequest)`   
ListZoneActionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListActionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listactionsresponse)>` | Promise  
  
### listZones(request, callback)
    
    
    public listZones(request: google.cloud.dataplex.v1.IListZonesRequest, callback: google.cloud.dataplex.v1.DataplexService.ListZonesCallback): void;

Calls ListZones.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListZonesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistzonesrequest)`   
ListZonesRequest message or plain object  
`callback` |  `[ListZonesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListZonesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listZones(request)
    
    
    public listZones(request: google.cloud.dataplex.v1.IListZonesRequest): Promise<google.cloud.dataplex.v1.ListZonesResponse>;

Calls ListZones.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListZonesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistzonesrequest)`   
ListZonesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListZonesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listzonesresponse)>` | Promise  
  
### runTask(request, callback)
    
    
    public runTask(request: google.cloud.dataplex.v1.IRunTaskRequest, callback: google.cloud.dataplex.v1.DataplexService.RunTaskCallback): void;

Calls RunTask.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iruntaskrequest)`   
RunTaskRequest message or plain object  
`callback` |  `[RunTaskCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and RunTaskResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### runTask(request)
    
    
    public runTask(request: google.cloud.dataplex.v1.IRunTaskRequest): Promise<google.cloud.dataplex.v1.RunTaskResponse>;

Calls RunTask.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRunTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iruntaskrequest)`   
RunTaskRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.RunTaskResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.runtaskresponse)>` | Promise  
  
### updateAsset(request, callback)
    
    
    public updateAsset(request: google.cloud.dataplex.v1.IUpdateAssetRequest, callback: google.cloud.dataplex.v1.DataplexService.UpdateAssetCallback): void;

Calls UpdateAsset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdateassetrequest)`   
UpdateAssetRequest message or plain object  
`callback` |  `[UpdateAssetCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAsset(request)
    
    
    public updateAsset(request: google.cloud.dataplex.v1.IUpdateAssetRequest): Promise<google.longrunning.Operation>;

Calls UpdateAsset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdateassetrequest)`   
UpdateAssetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### updateLake(request, callback)
    
    
    public updateLake(request: google.cloud.dataplex.v1.IUpdateLakeRequest, callback: google.cloud.dataplex.v1.DataplexService.UpdateLakeCallback): void;

Calls UpdateLake.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateLakeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdatelakerequest)`   
UpdateLakeRequest message or plain object  
`callback` |  `[UpdateLakeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateLake(request)
    
    
    public updateLake(request: google.cloud.dataplex.v1.IUpdateLakeRequest): Promise<google.longrunning.Operation>;

Calls UpdateLake.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateLakeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdatelakerequest)`   
UpdateLakeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### updateTask(request, callback)
    
    
    public updateTask(request: google.cloud.dataplex.v1.IUpdateTaskRequest, callback: google.cloud.dataplex.v1.DataplexService.UpdateTaskCallback): void;

Calls UpdateTask.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdatetaskrequest)`   
UpdateTaskRequest message or plain object  
`callback` |  `[UpdateTaskCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTask(request)
    
    
    public updateTask(request: google.cloud.dataplex.v1.IUpdateTaskRequest): Promise<google.longrunning.Operation>;

Calls UpdateTask.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdatetaskrequest)`   
UpdateTaskRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### updateZone(request, callback)
    
    
    public updateZone(request: google.cloud.dataplex.v1.IUpdateZoneRequest, callback: google.cloud.dataplex.v1.DataplexService.UpdateZoneCallback): void;

Calls UpdateZone.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdatezonerequest)`   
UpdateZoneRequest message or plain object  
`callback` |  `[UpdateZoneCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateZone(request)
    
    
    public updateZone(request: google.cloud.dataplex.v1.IUpdateZoneRequest): Promise<google.longrunning.Operation>;

Calls UpdateZone.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateZoneRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdatezonerequest)`   
UpdateZoneRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
