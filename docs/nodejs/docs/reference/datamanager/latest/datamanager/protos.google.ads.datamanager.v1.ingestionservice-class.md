---
url: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ingestionservice-class
title: Class protos.google.ads.datamanager.v1.IngestionService (1.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:33:30.443944+00:00
---

# Class protos.google.ads.datamanager.v1.IngestionService (1.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ingestionservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.datamanager.v1.IngestionService (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.5.0  0.4.0  0.3.0  0.1.0 

Represents an IngestionService

## Inheritance

$protobuf.rpc.Service > protos.google.ads.datamanager.v1.IngestionService

## Package

[@google-ads/datamanager](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new IngestionService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): IngestionService;

Creates new IngestionService service using the specified rpc implementation.

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
`[IngestionService](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ingestionservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### ingestAdEvents(request, callback)
    
    
    public ingestAdEvents(request: google.ads.datamanager.v1.IIngestAdEventsRequest, callback: google.ads.datamanager.v1.IngestionService.IngestAdEventsCallback): void;

Calls IngestAdEvents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IIngestAdEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iingestadeventsrequest)`   
IngestAdEventsRequest message or plain object  
`callback` |  `[IngestAdEventsCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and IngestAdEventsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### ingestAdEvents(request)
    
    
    public ingestAdEvents(request: google.ads.datamanager.v1.IIngestAdEventsRequest): Promise<google.ads.datamanager.v1.IngestAdEventsResponse>;

Calls IngestAdEvents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IIngestAdEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iingestadeventsrequest)`   
IngestAdEventsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.IngestAdEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ingestadeventsresponse)>` | Promise  
  
### ingestAudienceMembers(request, callback)
    
    
    public ingestAudienceMembers(request: google.ads.datamanager.v1.IIngestAudienceMembersRequest, callback: google.ads.datamanager.v1.IngestionService.IngestAudienceMembersCallback): void;

Calls IngestAudienceMembers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IIngestAudienceMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iingestaudiencemembersrequest)`   
IngestAudienceMembersRequest message or plain object  
`callback` |  `[IngestAudienceMembersCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and IngestAudienceMembersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### ingestAudienceMembers(request)
    
    
    public ingestAudienceMembers(request: google.ads.datamanager.v1.IIngestAudienceMembersRequest): Promise<google.ads.datamanager.v1.IngestAudienceMembersResponse>;

Calls IngestAudienceMembers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IIngestAudienceMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iingestaudiencemembersrequest)`   
IngestAudienceMembersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.IngestAudienceMembersResponse](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ingestaudiencemembersresponse)>` | Promise  
  
### ingestEvents(request, callback)
    
    
    public ingestEvents(request: google.ads.datamanager.v1.IIngestEventsRequest, callback: google.ads.datamanager.v1.IngestionService.IngestEventsCallback): void;

Calls IngestEvents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IIngestEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iingesteventsrequest)`   
IngestEventsRequest message or plain object  
`callback` |  `[IngestEventsCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and IngestEventsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### ingestEvents(request)
    
    
    public ingestEvents(request: google.ads.datamanager.v1.IIngestEventsRequest): Promise<google.ads.datamanager.v1.IngestEventsResponse>;

Calls IngestEvents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IIngestEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iingesteventsrequest)`   
IngestEventsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.IngestEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ingesteventsresponse)>` | Promise  
  
### removeAllAudienceMembers(request, callback)
    
    
    public removeAllAudienceMembers(request: google.ads.datamanager.v1.IRemoveAllAudienceMembersRequest, callback: google.ads.datamanager.v1.IngestionService.RemoveAllAudienceMembersCallback): void;

Calls RemoveAllAudienceMembers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveAllAudienceMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iremoveallaudiencemembersrequest)`   
RemoveAllAudienceMembersRequest message or plain object  
`callback` |  `[RemoveAllAudienceMembersCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and RemoveAllAudienceMembersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeAllAudienceMembers(request)
    
    
    public removeAllAudienceMembers(request: google.ads.datamanager.v1.IRemoveAllAudienceMembersRequest): Promise<google.ads.datamanager.v1.RemoveAllAudienceMembersResponse>;

Calls RemoveAllAudienceMembers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRemoveAllAudienceMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iremoveallaudiencemembersrequest)`   
RemoveAllAudienceMembersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.RemoveAllAudienceMembersResponse](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.removeallaudiencemembersresponse)>` | Promise  
  
### removeAudienceMembers(request, callback)
    
    
    public removeAudienceMembers(request: google.ads.datamanager.v1.IRemoveAudienceMembersRequest, callback: google.ads.datamanager.v1.IngestionService.RemoveAudienceMembersCallback): void;

Calls RemoveAudienceMembers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveAudienceMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iremoveaudiencemembersrequest)`   
RemoveAudienceMembersRequest message or plain object  
`callback` |  `[RemoveAudienceMembersCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and RemoveAudienceMembersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeAudienceMembers(request)
    
    
    public removeAudienceMembers(request: google.ads.datamanager.v1.IRemoveAudienceMembersRequest): Promise<google.ads.datamanager.v1.RemoveAudienceMembersResponse>;

Calls RemoveAudienceMembers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRemoveAudienceMembersRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iremoveaudiencemembersrequest)`   
RemoveAudienceMembersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.RemoveAudienceMembersResponse](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.removeaudiencemembersresponse)>` | Promise  
  
### retrieveRequestStatus(request, callback)
    
    
    public retrieveRequestStatus(request: google.ads.datamanager.v1.IRetrieveRequestStatusRequest, callback: google.ads.datamanager.v1.IngestionService.RetrieveRequestStatusCallback): void;

Calls RetrieveRequestStatus.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRetrieveRequestStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iretrieverequeststatusrequest)`   
RetrieveRequestStatusRequest message or plain object  
`callback` |  `[RetrieveRequestStatusCallback](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)`   
Node-style callback called with the error, if any, and RetrieveRequestStatusResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### retrieveRequestStatus(request)
    
    
    public retrieveRequestStatus(request: google.ads.datamanager.v1.IRetrieveRequestStatusRequest): Promise<google.ads.datamanager.v1.RetrieveRequestStatusResponse>;

Calls RetrieveRequestStatus.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRetrieveRequestStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iretrieverequeststatusrequest)`   
RetrieveRequestStatusRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.datamanager.v1.RetrieveRequestStatusResponse](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.retrieverequeststatusresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
