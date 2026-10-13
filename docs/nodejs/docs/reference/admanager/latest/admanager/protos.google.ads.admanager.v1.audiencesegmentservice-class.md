---
url: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.audiencesegmentservice-class
title: Class protos.google.ads.admanager.v1.AudienceSegmentService (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:18:51.479615+00:00
---

# Class protos.google.ads.admanager.v1.AudienceSegmentService (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.audiencesegmentservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.admanager.v1.AudienceSegmentService (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.12.0  0.11.0  0.7.0  0.6.0  0.1.0 

Represents an AudienceSegmentService

## Inheritance

$protobuf.rpc.Service > protos.google.ads.admanager.v1.AudienceSegmentService

## Package

[@google-ads/admanager](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AudienceSegmentService service.

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

### batchActivateAudienceSegments(request, callback)
    
    
    public batchActivateAudienceSegments(request: google.ads.admanager.v1.IBatchActivateAudienceSegmentsRequest, callback: google.ads.admanager.v1.AudienceSegmentService.BatchActivateAudienceSegmentsCallback): void;

Calls BatchActivateAudienceSegments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchActivateAudienceSegmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchactivateaudiencesegmentsrequest)`   
BatchActivateAudienceSegmentsRequest message or plain object  
`callback` |  `[BatchActivateAudienceSegmentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchActivateAudienceSegmentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchActivateAudienceSegments(request)
    
    
    public batchActivateAudienceSegments(request: google.ads.admanager.v1.IBatchActivateAudienceSegmentsRequest): Promise<google.ads.admanager.v1.BatchActivateAudienceSegmentsResponse>;

Calls BatchActivateAudienceSegments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchActivateAudienceSegmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchactivateaudiencesegmentsrequest)`   
BatchActivateAudienceSegmentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchActivateAudienceSegmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchactivateaudiencesegmentsresponse)>` | Promise  
  
### batchApproveAudienceSegments(request, callback)
    
    
    public batchApproveAudienceSegments(request: google.ads.admanager.v1.IBatchApproveAudienceSegmentsRequest, callback: google.ads.admanager.v1.AudienceSegmentService.BatchApproveAudienceSegmentsCallback): void;

Calls BatchApproveAudienceSegments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchApproveAudienceSegmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchapproveaudiencesegmentsrequest)`   
BatchApproveAudienceSegmentsRequest message or plain object  
`callback` |  `[BatchApproveAudienceSegmentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchApproveAudienceSegmentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchApproveAudienceSegments(request)
    
    
    public batchApproveAudienceSegments(request: google.ads.admanager.v1.IBatchApproveAudienceSegmentsRequest): Promise<google.ads.admanager.v1.BatchApproveAudienceSegmentsResponse>;

Calls BatchApproveAudienceSegments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchApproveAudienceSegmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchapproveaudiencesegmentsrequest)`   
BatchApproveAudienceSegmentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchApproveAudienceSegmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchapproveaudiencesegmentsresponse)>` | Promise  
  
### batchCreateAudienceSegments(request, callback)
    
    
    public batchCreateAudienceSegments(request: google.ads.admanager.v1.IBatchCreateAudienceSegmentsRequest, callback: google.ads.admanager.v1.AudienceSegmentService.BatchCreateAudienceSegmentsCallback): void;

Calls BatchCreateAudienceSegments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateAudienceSegmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchcreateaudiencesegmentsrequest)`   
BatchCreateAudienceSegmentsRequest message or plain object  
`callback` |  `[BatchCreateAudienceSegmentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchCreateAudienceSegmentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateAudienceSegments(request)
    
    
    public batchCreateAudienceSegments(request: google.ads.admanager.v1.IBatchCreateAudienceSegmentsRequest): Promise<google.ads.admanager.v1.BatchCreateAudienceSegmentsResponse>;

Calls BatchCreateAudienceSegments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateAudienceSegmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchcreateaudiencesegmentsrequest)`   
BatchCreateAudienceSegmentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchCreateAudienceSegmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchcreateaudiencesegmentsresponse)>` | Promise  
  
### batchDeactivateAudienceSegments(request, callback)
    
    
    public batchDeactivateAudienceSegments(request: google.ads.admanager.v1.IBatchDeactivateAudienceSegmentsRequest, callback: google.ads.admanager.v1.AudienceSegmentService.BatchDeactivateAudienceSegmentsCallback): void;

Calls BatchDeactivateAudienceSegments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeactivateAudienceSegmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchdeactivateaudiencesegmentsrequest)`   
BatchDeactivateAudienceSegmentsRequest message or plain object  
`callback` |  `[BatchDeactivateAudienceSegmentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchDeactivateAudienceSegmentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchDeactivateAudienceSegments(request)
    
    
    public batchDeactivateAudienceSegments(request: google.ads.admanager.v1.IBatchDeactivateAudienceSegmentsRequest): Promise<google.ads.admanager.v1.BatchDeactivateAudienceSegmentsResponse>;

Calls BatchDeactivateAudienceSegments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeactivateAudienceSegmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchdeactivateaudiencesegmentsrequest)`   
BatchDeactivateAudienceSegmentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchDeactivateAudienceSegmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchdeactivateaudiencesegmentsresponse)>` | Promise  
  
### batchPopulateAudienceSegments(request, callback)
    
    
    public batchPopulateAudienceSegments(request: google.ads.admanager.v1.IBatchPopulateAudienceSegmentsRequest, callback: google.ads.admanager.v1.AudienceSegmentService.BatchPopulateAudienceSegmentsCallback): void;

Calls BatchPopulateAudienceSegments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchPopulateAudienceSegmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchpopulateaudiencesegmentsrequest)`   
BatchPopulateAudienceSegmentsRequest message or plain object  
`callback` |  `[BatchPopulateAudienceSegmentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchPopulateAudienceSegmentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchPopulateAudienceSegments(request)
    
    
    public batchPopulateAudienceSegments(request: google.ads.admanager.v1.IBatchPopulateAudienceSegmentsRequest): Promise<google.ads.admanager.v1.BatchPopulateAudienceSegmentsResponse>;

Calls BatchPopulateAudienceSegments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchPopulateAudienceSegmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchpopulateaudiencesegmentsrequest)`   
BatchPopulateAudienceSegmentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchPopulateAudienceSegmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchpopulateaudiencesegmentsresponse)>` | Promise  
  
### batchRejectAudienceSegments(request, callback)
    
    
    public batchRejectAudienceSegments(request: google.ads.admanager.v1.IBatchRejectAudienceSegmentsRequest, callback: google.ads.admanager.v1.AudienceSegmentService.BatchRejectAudienceSegmentsCallback): void;

Calls BatchRejectAudienceSegments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchRejectAudienceSegmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchrejectaudiencesegmentsrequest)`   
BatchRejectAudienceSegmentsRequest message or plain object  
`callback` |  `[BatchRejectAudienceSegmentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchRejectAudienceSegmentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchRejectAudienceSegments(request)
    
    
    public batchRejectAudienceSegments(request: google.ads.admanager.v1.IBatchRejectAudienceSegmentsRequest): Promise<google.ads.admanager.v1.BatchRejectAudienceSegmentsResponse>;

Calls BatchRejectAudienceSegments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchRejectAudienceSegmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchrejectaudiencesegmentsrequest)`   
BatchRejectAudienceSegmentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchRejectAudienceSegmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchrejectaudiencesegmentsresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AudienceSegmentService;

Creates new AudienceSegmentService service using the specified rpc implementation.

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
`[AudienceSegmentService](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.audiencesegmentservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAudienceSegment(request, callback)
    
    
    public createAudienceSegment(request: google.ads.admanager.v1.ICreateAudienceSegmentRequest, callback: google.ads.admanager.v1.AudienceSegmentService.CreateAudienceSegmentCallback): void;

Calls CreateAudienceSegment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAudienceSegmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.icreateaudiencesegmentrequest)`   
CreateAudienceSegmentRequest message or plain object  
`callback` |  `[CreateAudienceSegmentCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and AudienceSegment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAudienceSegment(request)
    
    
    public createAudienceSegment(request: google.ads.admanager.v1.ICreateAudienceSegmentRequest): Promise<google.ads.admanager.v1.AudienceSegment>;

Calls CreateAudienceSegment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAudienceSegmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.icreateaudiencesegmentrequest)`   
CreateAudienceSegmentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.AudienceSegment](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.audiencesegment-class)>` | Promise  
  
### getAudienceSegment(request, callback)
    
    
    public getAudienceSegment(request: google.ads.admanager.v1.IGetAudienceSegmentRequest, callback: google.ads.admanager.v1.AudienceSegmentService.GetAudienceSegmentCallback): void;

Calls GetAudienceSegment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAudienceSegmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.igetaudiencesegmentrequest)`   
GetAudienceSegmentRequest message or plain object  
`callback` |  `[GetAudienceSegmentCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and AudienceSegment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAudienceSegment(request)
    
    
    public getAudienceSegment(request: google.ads.admanager.v1.IGetAudienceSegmentRequest): Promise<google.ads.admanager.v1.AudienceSegment>;

Calls GetAudienceSegment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAudienceSegmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.igetaudiencesegmentrequest)`   
GetAudienceSegmentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.AudienceSegment](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.audiencesegment-class)>` | Promise  
  
### listAudienceSegments(request, callback)
    
    
    public listAudienceSegments(request: google.ads.admanager.v1.IListAudienceSegmentsRequest, callback: google.ads.admanager.v1.AudienceSegmentService.ListAudienceSegmentsCallback): void;

Calls ListAudienceSegments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAudienceSegmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistaudiencesegmentsrequest)`   
ListAudienceSegmentsRequest message or plain object  
`callback` |  `[ListAudienceSegmentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAudienceSegmentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAudienceSegments(request)
    
    
    public listAudienceSegments(request: google.ads.admanager.v1.IListAudienceSegmentsRequest): Promise<google.ads.admanager.v1.ListAudienceSegmentsResponse>;

Calls ListAudienceSegments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAudienceSegmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistaudiencesegmentsrequest)`   
ListAudienceSegmentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.ListAudienceSegmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.listaudiencesegmentsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
