---
url: https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.rapidmigrationassessment-class
title: Class protos.google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:11.321619+00:00
---

# Class protos.google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.rapidmigrationassessment-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.1.0  2.0.1 

Represents a RapidMigrationAssessment

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment

## Package

[@google-cloud/rapidmigrationassessment](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new RapidMigrationAssessment service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): RapidMigrationAssessment;

Creates new RapidMigrationAssessment service using the specified rpc implementation.

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
`[RapidMigrationAssessment](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.rapidmigrationassessment-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAnnotation(request, callback)
    
    
    public createAnnotation(request: google.cloud.rapidmigrationassessment.v1.ICreateAnnotationRequest, callback: google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment.CreateAnnotationCallback): void;

Calls CreateAnnotation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAnnotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.icreateannotationrequest)`   
CreateAnnotationRequest message or plain object  
`callback` |  `[CreateAnnotationCallback](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAnnotation(request)
    
    
    public createAnnotation(request: google.cloud.rapidmigrationassessment.v1.ICreateAnnotationRequest): Promise<google.longrunning.Operation>;

Calls CreateAnnotation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAnnotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.icreateannotationrequest)`   
CreateAnnotationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.longrunning.operation)>` | Promise  
  
### createCollector(request, callback)
    
    
    public createCollector(request: google.cloud.rapidmigrationassessment.v1.ICreateCollectorRequest, callback: google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment.CreateCollectorCallback): void;

Calls CreateCollector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCollectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.icreatecollectorrequest)`   
CreateCollectorRequest message or plain object  
`callback` |  `[CreateCollectorCallback](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCollector(request)
    
    
    public createCollector(request: google.cloud.rapidmigrationassessment.v1.ICreateCollectorRequest): Promise<google.longrunning.Operation>;

Calls CreateCollector.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCollectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.icreatecollectorrequest)`   
CreateCollectorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.longrunning.operation)>` | Promise  
  
### deleteCollector(request, callback)
    
    
    public deleteCollector(request: google.cloud.rapidmigrationassessment.v1.IDeleteCollectorRequest, callback: google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment.DeleteCollectorCallback): void;

Calls DeleteCollector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCollectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.ideletecollectorrequest)`   
DeleteCollectorRequest message or plain object  
`callback` |  `[DeleteCollectorCallback](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCollector(request)
    
    
    public deleteCollector(request: google.cloud.rapidmigrationassessment.v1.IDeleteCollectorRequest): Promise<google.longrunning.Operation>;

Calls DeleteCollector.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCollectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.ideletecollectorrequest)`   
DeleteCollectorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.longrunning.operation)>` | Promise  
  
### getAnnotation(request, callback)
    
    
    public getAnnotation(request: google.cloud.rapidmigrationassessment.v1.IGetAnnotationRequest, callback: google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment.GetAnnotationCallback): void;

Calls GetAnnotation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.igetannotationrequest)`   
GetAnnotationRequest message or plain object  
`callback` |  `[GetAnnotationCallback](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/overview.html)`   
Node-style callback called with the error, if any, and Annotation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAnnotation(request)
    
    
    public getAnnotation(request: google.cloud.rapidmigrationassessment.v1.IGetAnnotationRequest): Promise<google.cloud.rapidmigrationassessment.v1.Annotation>;

Calls GetAnnotation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.igetannotationrequest)`   
GetAnnotationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.rapidmigrationassessment.v1.Annotation](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.annotation-class)>` | Promise  
  
### getCollector(request, callback)
    
    
    public getCollector(request: google.cloud.rapidmigrationassessment.v1.IGetCollectorRequest, callback: google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment.GetCollectorCallback): void;

Calls GetCollector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCollectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.igetcollectorrequest)`   
GetCollectorRequest message or plain object  
`callback` |  `[GetCollectorCallback](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/overview.html)`   
Node-style callback called with the error, if any, and Collector  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCollector(request)
    
    
    public getCollector(request: google.cloud.rapidmigrationassessment.v1.IGetCollectorRequest): Promise<google.cloud.rapidmigrationassessment.v1.Collector>;

Calls GetCollector.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCollectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.igetcollectorrequest)`   
GetCollectorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.rapidmigrationassessment.v1.Collector](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.collector-class)>` | Promise  
  
### listCollectors(request, callback)
    
    
    public listCollectors(request: google.cloud.rapidmigrationassessment.v1.IListCollectorsRequest, callback: google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment.ListCollectorsCallback): void;

Calls ListCollectors.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCollectorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.ilistcollectorsrequest)`   
ListCollectorsRequest message or plain object  
`callback` |  `[ListCollectorsCallback](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCollectorsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCollectors(request)
    
    
    public listCollectors(request: google.cloud.rapidmigrationassessment.v1.IListCollectorsRequest): Promise<google.cloud.rapidmigrationassessment.v1.ListCollectorsResponse>;

Calls ListCollectors.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCollectorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.ilistcollectorsrequest)`   
ListCollectorsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.rapidmigrationassessment.v1.ListCollectorsResponse](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.listcollectorsresponse)>` | Promise  
  
### pauseCollector(request, callback)
    
    
    public pauseCollector(request: google.cloud.rapidmigrationassessment.v1.IPauseCollectorRequest, callback: google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment.PauseCollectorCallback): void;

Calls PauseCollector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPauseCollectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.ipausecollectorrequest)`   
PauseCollectorRequest message or plain object  
`callback` |  `[PauseCollectorCallback](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### pauseCollector(request)
    
    
    public pauseCollector(request: google.cloud.rapidmigrationassessment.v1.IPauseCollectorRequest): Promise<google.longrunning.Operation>;

Calls PauseCollector.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPauseCollectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.ipausecollectorrequest)`   
PauseCollectorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.longrunning.operation)>` | Promise  
  
### registerCollector(request, callback)
    
    
    public registerCollector(request: google.cloud.rapidmigrationassessment.v1.IRegisterCollectorRequest, callback: google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment.RegisterCollectorCallback): void;

Calls RegisterCollector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRegisterCollectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.iregistercollectorrequest)`   
RegisterCollectorRequest message or plain object  
`callback` |  `[RegisterCollectorCallback](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### registerCollector(request)
    
    
    public registerCollector(request: google.cloud.rapidmigrationassessment.v1.IRegisterCollectorRequest): Promise<google.longrunning.Operation>;

Calls RegisterCollector.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRegisterCollectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.iregistercollectorrequest)`   
RegisterCollectorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.longrunning.operation)>` | Promise  
  
### resumeCollector(request, callback)
    
    
    public resumeCollector(request: google.cloud.rapidmigrationassessment.v1.IResumeCollectorRequest, callback: google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment.ResumeCollectorCallback): void;

Calls ResumeCollector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResumeCollectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.iresumecollectorrequest)`   
ResumeCollectorRequest message or plain object  
`callback` |  `[ResumeCollectorCallback](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### resumeCollector(request)
    
    
    public resumeCollector(request: google.cloud.rapidmigrationassessment.v1.IResumeCollectorRequest): Promise<google.longrunning.Operation>;

Calls ResumeCollector.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IResumeCollectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.iresumecollectorrequest)`   
ResumeCollectorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.longrunning.operation)>` | Promise  
  
### updateCollector(request, callback)
    
    
    public updateCollector(request: google.cloud.rapidmigrationassessment.v1.IUpdateCollectorRequest, callback: google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessment.UpdateCollectorCallback): void;

Calls UpdateCollector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCollectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.iupdatecollectorrequest)`   
UpdateCollectorRequest message or plain object  
`callback` |  `[UpdateCollectorCallback](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCollector(request)
    
    
    public updateCollector(request: google.cloud.rapidmigrationassessment.v1.IUpdateCollectorRequest): Promise<google.longrunning.Operation>;

Calls UpdateCollector.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCollectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.iupdatecollectorrequest)`   
UpdateCollectorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
