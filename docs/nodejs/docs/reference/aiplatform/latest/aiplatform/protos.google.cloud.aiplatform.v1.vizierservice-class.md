---
url: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.vizierservice-class
title: Class protos.google.cloud.aiplatform.v1.VizierService (7.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:41:30.884933+00:00
---

# Class protos.google.cloud.aiplatform.v1.VizierService (7.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.vizierservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.aiplatform.v1.VizierService (7.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.4.1 (latest)  7.3.0  6.10.0  6.9.0  6.8.1  6.6.0  6.4.0  6.3.0  6.2.0  6.1.0  6.0.0  5.14.0  5.13.0  3.15.0  3.13.0  3.11.0  3.10.1  3.9.0  3.7.0  3.6.0  3.4.0  3.3.0  3.0.0  2.12.0  2.11.0  2.10.0  2.7.0  2.6.1  2.5.0  2.3.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.11.0  1.7.2 

Represents a VizierService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.aiplatform.v1.VizierService

## Package

[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new VizierService service.

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

### addTrialMeasurement(request, callback)
    
    
    public addTrialMeasurement(request: google.cloud.aiplatform.v1.IAddTrialMeasurementRequest, callback: google.cloud.aiplatform.v1.VizierService.AddTrialMeasurementCallback): void;

Calls AddTrialMeasurement.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddTrialMeasurementRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iaddtrialmeasurementrequest)`   
AddTrialMeasurementRequest message or plain object  
`callback` |  `[AddTrialMeasurementCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Trial  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addTrialMeasurement(request)
    
    
    public addTrialMeasurement(request: google.cloud.aiplatform.v1.IAddTrialMeasurementRequest): Promise<google.cloud.aiplatform.v1.Trial>;

Calls AddTrialMeasurement.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAddTrialMeasurementRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iaddtrialmeasurementrequest)`   
AddTrialMeasurementRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.Trial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.trial-class)>` | Promise  
  
### checkTrialEarlyStoppingState(request, callback)
    
    
    public checkTrialEarlyStoppingState(request: google.cloud.aiplatform.v1.ICheckTrialEarlyStoppingStateRequest, callback: google.cloud.aiplatform.v1.VizierService.CheckTrialEarlyStoppingStateCallback): void;

Calls CheckTrialEarlyStoppingState.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICheckTrialEarlyStoppingStateRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ichecktrialearlystoppingstaterequest)`   
CheckTrialEarlyStoppingStateRequest message or plain object  
`callback` |  `[CheckTrialEarlyStoppingStateCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### checkTrialEarlyStoppingState(request)
    
    
    public checkTrialEarlyStoppingState(request: google.cloud.aiplatform.v1.ICheckTrialEarlyStoppingStateRequest): Promise<google.longrunning.Operation>;

Calls CheckTrialEarlyStoppingState.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICheckTrialEarlyStoppingStateRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ichecktrialearlystoppingstaterequest)`   
CheckTrialEarlyStoppingStateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
### completeTrial(request, callback)
    
    
    public completeTrial(request: google.cloud.aiplatform.v1.ICompleteTrialRequest, callback: google.cloud.aiplatform.v1.VizierService.CompleteTrialCallback): void;

Calls CompleteTrial.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICompleteTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.icompletetrialrequest)`   
CompleteTrialRequest message or plain object  
`callback` |  `[CompleteTrialCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Trial  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### completeTrial(request)
    
    
    public completeTrial(request: google.cloud.aiplatform.v1.ICompleteTrialRequest): Promise<google.cloud.aiplatform.v1.Trial>;

Calls CompleteTrial.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICompleteTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.icompletetrialrequest)`   
CompleteTrialRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.Trial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.trial-class)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): VizierService;

Creates new VizierService service using the specified rpc implementation.

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
`[VizierService](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.vizierservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createStudy(request, callback)
    
    
    public createStudy(request: google.cloud.aiplatform.v1.ICreateStudyRequest, callback: google.cloud.aiplatform.v1.VizierService.CreateStudyCallback): void;

Calls CreateStudy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.icreatestudyrequest)`   
CreateStudyRequest message or plain object  
`callback` |  `[CreateStudyCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Study  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createStudy(request)
    
    
    public createStudy(request: google.cloud.aiplatform.v1.ICreateStudyRequest): Promise<google.cloud.aiplatform.v1.Study>;

Calls CreateStudy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.icreatestudyrequest)`   
CreateStudyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.Study](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.study-class)>` | Promise  
  
### createTrial(request, callback)
    
    
    public createTrial(request: google.cloud.aiplatform.v1.ICreateTrialRequest, callback: google.cloud.aiplatform.v1.VizierService.CreateTrialCallback): void;

Calls CreateTrial.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.icreatetrialrequest)`   
CreateTrialRequest message or plain object  
`callback` |  `[CreateTrialCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Trial  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTrial(request)
    
    
    public createTrial(request: google.cloud.aiplatform.v1.ICreateTrialRequest): Promise<google.cloud.aiplatform.v1.Trial>;

Calls CreateTrial.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.icreatetrialrequest)`   
CreateTrialRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.Trial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.trial-class)>` | Promise  
  
### deleteStudy(request, callback)
    
    
    public deleteStudy(request: google.cloud.aiplatform.v1.IDeleteStudyRequest, callback: google.cloud.aiplatform.v1.VizierService.DeleteStudyCallback): void;

Calls DeleteStudy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideletestudyrequest)`   
DeleteStudyRequest message or plain object  
`callback` |  `[DeleteStudyCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteStudy(request)
    
    
    public deleteStudy(request: google.cloud.aiplatform.v1.IDeleteStudyRequest): Promise<google.protobuf.Empty>;

Calls DeleteStudy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideletestudyrequest)`   
DeleteStudyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.empty)>` | Promise  
  
### deleteTrial(request, callback)
    
    
    public deleteTrial(request: google.cloud.aiplatform.v1.IDeleteTrialRequest, callback: google.cloud.aiplatform.v1.VizierService.DeleteTrialCallback): void;

Calls DeleteTrial.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideletetrialrequest)`   
DeleteTrialRequest message or plain object  
`callback` |  `[DeleteTrialCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTrial(request)
    
    
    public deleteTrial(request: google.cloud.aiplatform.v1.IDeleteTrialRequest): Promise<google.protobuf.Empty>;

Calls DeleteTrial.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ideletetrialrequest)`   
DeleteTrialRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.empty)>` | Promise  
  
### getStudy(request, callback)
    
    
    public getStudy(request: google.cloud.aiplatform.v1.IGetStudyRequest, callback: google.cloud.aiplatform.v1.VizierService.GetStudyCallback): void;

Calls GetStudy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.igetstudyrequest)`   
GetStudyRequest message or plain object  
`callback` |  `[GetStudyCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Study  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getStudy(request)
    
    
    public getStudy(request: google.cloud.aiplatform.v1.IGetStudyRequest): Promise<google.cloud.aiplatform.v1.Study>;

Calls GetStudy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.igetstudyrequest)`   
GetStudyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.Study](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.study-class)>` | Promise  
  
### getTrial(request, callback)
    
    
    public getTrial(request: google.cloud.aiplatform.v1.IGetTrialRequest, callback: google.cloud.aiplatform.v1.VizierService.GetTrialCallback): void;

Calls GetTrial.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.igettrialrequest)`   
GetTrialRequest message or plain object  
`callback` |  `[GetTrialCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Trial  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTrial(request)
    
    
    public getTrial(request: google.cloud.aiplatform.v1.IGetTrialRequest): Promise<google.cloud.aiplatform.v1.Trial>;

Calls GetTrial.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.igettrialrequest)`   
GetTrialRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.Trial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.trial-class)>` | Promise  
  
### listOptimalTrials(request, callback)
    
    
    public listOptimalTrials(request: google.cloud.aiplatform.v1.IListOptimalTrialsRequest, callback: google.cloud.aiplatform.v1.VizierService.ListOptimalTrialsCallback): void;

Calls ListOptimalTrials.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOptimalTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ilistoptimaltrialsrequest)`   
ListOptimalTrialsRequest message or plain object  
`callback` |  `[ListOptimalTrialsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListOptimalTrialsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listOptimalTrials(request)
    
    
    public listOptimalTrials(request: google.cloud.aiplatform.v1.IListOptimalTrialsRequest): Promise<google.cloud.aiplatform.v1.ListOptimalTrialsResponse>;

Calls ListOptimalTrials.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListOptimalTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ilistoptimaltrialsrequest)`   
ListOptimalTrialsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.ListOptimalTrialsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.listoptimaltrialsresponse)>` | Promise  
  
### listStudies(request, callback)
    
    
    public listStudies(request: google.cloud.aiplatform.v1.IListStudiesRequest, callback: google.cloud.aiplatform.v1.VizierService.ListStudiesCallback): void;

Calls ListStudies.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListStudiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iliststudiesrequest)`   
ListStudiesRequest message or plain object  
`callback` |  `[ListStudiesCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListStudiesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listStudies(request)
    
    
    public listStudies(request: google.cloud.aiplatform.v1.IListStudiesRequest): Promise<google.cloud.aiplatform.v1.ListStudiesResponse>;

Calls ListStudies.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListStudiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.iliststudiesrequest)`   
ListStudiesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.ListStudiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.liststudiesresponse)>` | Promise  
  
### listTrials(request, callback)
    
    
    public listTrials(request: google.cloud.aiplatform.v1.IListTrialsRequest, callback: google.cloud.aiplatform.v1.VizierService.ListTrialsCallback): void;

Calls ListTrials.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ilisttrialsrequest)`   
ListTrialsRequest message or plain object  
`callback` |  `[ListTrialsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and ListTrialsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTrials(request)
    
    
    public listTrials(request: google.cloud.aiplatform.v1.IListTrialsRequest): Promise<google.cloud.aiplatform.v1.ListTrialsResponse>;

Calls ListTrials.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ilisttrialsrequest)`   
ListTrialsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.ListTrialsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.listtrialsresponse)>` | Promise  
  
### lookupStudy(request, callback)
    
    
    public lookupStudy(request: google.cloud.aiplatform.v1.ILookupStudyRequest, callback: google.cloud.aiplatform.v1.VizierService.LookupStudyCallback): void;

Calls LookupStudy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ilookupstudyrequest)`   
LookupStudyRequest message or plain object  
`callback` |  `[LookupStudyCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Study  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### lookupStudy(request)
    
    
    public lookupStudy(request: google.cloud.aiplatform.v1.ILookupStudyRequest): Promise<google.cloud.aiplatform.v1.Study>;

Calls LookupStudy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ILookupStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.ilookupstudyrequest)`   
LookupStudyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.Study](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.study-class)>` | Promise  
  
### stopTrial(request, callback)
    
    
    public stopTrial(request: google.cloud.aiplatform.v1.IStopTrialRequest, callback: google.cloud.aiplatform.v1.VizierService.StopTrialCallback): void;

Calls StopTrial.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStopTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.istoptrialrequest)`   
StopTrialRequest message or plain object  
`callback` |  `[StopTrialCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Trial  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### stopTrial(request)
    
    
    public stopTrial(request: google.cloud.aiplatform.v1.IStopTrialRequest): Promise<google.cloud.aiplatform.v1.Trial>;

Calls StopTrial.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IStopTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.istoptrialrequest)`   
StopTrialRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.aiplatform.v1.Trial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.trial-class)>` | Promise  
  
### suggestTrials(request, callback)
    
    
    public suggestTrials(request: google.cloud.aiplatform.v1.ISuggestTrialsRequest, callback: google.cloud.aiplatform.v1.VizierService.SuggestTrialsCallback): void;

Calls SuggestTrials.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISuggestTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.isuggesttrialsrequest)`   
SuggestTrialsRequest message or plain object  
`callback` |  `[SuggestTrialsCallback](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### suggestTrials(request)
    
    
    public suggestTrials(request: google.cloud.aiplatform.v1.ISuggestTrialsRequest): Promise<google.longrunning.Operation>;

Calls SuggestTrials.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISuggestTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1.isuggesttrialsrequest)`   
SuggestTrialsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
