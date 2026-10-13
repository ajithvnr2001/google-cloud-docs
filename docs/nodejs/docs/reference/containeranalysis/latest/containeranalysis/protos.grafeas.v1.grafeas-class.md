---
url: https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.grafeas-class
title: Class protos.grafeas.v1.Grafeas (7.0.2) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:07.374834+00:00
---

# Class protos.grafeas.v1.Grafeas (7.0.2)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.grafeas-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.grafeas.v1.Grafeas (7.0.2) Stay organized with collections  Save and categorize content based on your preferences. 

7.0.2 (latest)  7.0.1  6.8.0  6.7.0  6.5.0  5.6.0  5.0.1  4.7.0  4.4.2  4.3.0  3.4.0  3.3.0  3.2.0  3.1.8 

Represents a Grafeas

## Inheritance

$protobuf.rpc.Service > protos.grafeas.v1.Grafeas

## Package

[@google-cloud/containeranalysis](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Grafeas service.

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

### batchCreateNotes(request, callback)
    
    
    public batchCreateNotes(request: grafeas.v1.IBatchCreateNotesRequest, callback: grafeas.v1.Grafeas.BatchCreateNotesCallback): void;

Calls BatchCreateNotes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateNotesRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.ibatchcreatenotesrequest)`   
BatchCreateNotesRequest message or plain object  
`callback` |  `[BatchCreateNotesCallback](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchCreateNotesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateNotes(request)
    
    
    public batchCreateNotes(request: grafeas.v1.IBatchCreateNotesRequest): Promise<grafeas.v1.BatchCreateNotesResponse>;

Calls BatchCreateNotes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateNotesRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.ibatchcreatenotesrequest)`   
BatchCreateNotesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[grafeas.v1.BatchCreateNotesResponse](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.batchcreatenotesresponse)>` | Promise  
  
### batchCreateOccurrences(request, callback)
    
    
    public batchCreateOccurrences(request: grafeas.v1.IBatchCreateOccurrencesRequest, callback: grafeas.v1.Grafeas.BatchCreateOccurrencesCallback): void;

Calls BatchCreateOccurrences.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateOccurrencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.ibatchcreateoccurrencesrequest)`   
BatchCreateOccurrencesRequest message or plain object  
`callback` |  `[BatchCreateOccurrencesCallback](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchCreateOccurrencesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateOccurrences(request)
    
    
    public batchCreateOccurrences(request: grafeas.v1.IBatchCreateOccurrencesRequest): Promise<grafeas.v1.BatchCreateOccurrencesResponse>;

Calls BatchCreateOccurrences.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateOccurrencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.ibatchcreateoccurrencesrequest)`   
BatchCreateOccurrencesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[grafeas.v1.BatchCreateOccurrencesResponse](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.batchcreateoccurrencesresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Grafeas;

Creates new Grafeas service using the specified rpc implementation.

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
`[Grafeas](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.grafeas-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createNote(request, callback)
    
    
    public createNote(request: grafeas.v1.ICreateNoteRequest, callback: grafeas.v1.Grafeas.CreateNoteCallback): void;

Calls CreateNote.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateNoteRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.icreatenoterequest)`   
CreateNoteRequest message or plain object  
`callback` |  `[CreateNoteCallback](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)`   
Node-style callback called with the error, if any, and Note  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createNote(request)
    
    
    public createNote(request: grafeas.v1.ICreateNoteRequest): Promise<grafeas.v1.Note>;

Calls CreateNote.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateNoteRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.icreatenoterequest)`   
CreateNoteRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[grafeas.v1.Note](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.note)>` | Promise  
  
### createOccurrence(request, callback)
    
    
    public createOccurrence(request: grafeas.v1.ICreateOccurrenceRequest, callback: grafeas.v1.Grafeas.CreateOccurrenceCallback): void;

Calls CreateOccurrence.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.icreateoccurrencerequest)`   
CreateOccurrenceRequest message or plain object  
`callback` |  `[CreateOccurrenceCallback](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)`   
Node-style callback called with the error, if any, and Occurrence  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createOccurrence(request)
    
    
    public createOccurrence(request: grafeas.v1.ICreateOccurrenceRequest): Promise<grafeas.v1.Occurrence>;

Calls CreateOccurrence.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.icreateoccurrencerequest)`   
CreateOccurrenceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[grafeas.v1.Occurrence](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.occurrence)>` | Promise  
  
### deleteNote(request, callback)
    
    
    public deleteNote(request: grafeas.v1.IDeleteNoteRequest, callback: grafeas.v1.Grafeas.DeleteNoteCallback): void;

Calls DeleteNote.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteNoteRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.ideletenoterequest)`   
DeleteNoteRequest message or plain object  
`callback` |  `[DeleteNoteCallback](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteNote(request)
    
    
    public deleteNote(request: grafeas.v1.IDeleteNoteRequest): Promise<google.protobuf.Empty>;

Calls DeleteNote.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteNoteRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.ideletenoterequest)`   
DeleteNoteRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.google.protobuf.empty)>` | Promise  
  
### deleteOccurrence(request, callback)
    
    
    public deleteOccurrence(request: grafeas.v1.IDeleteOccurrenceRequest, callback: grafeas.v1.Grafeas.DeleteOccurrenceCallback): void;

Calls DeleteOccurrence.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.ideleteoccurrencerequest)`   
DeleteOccurrenceRequest message or plain object  
`callback` |  `[DeleteOccurrenceCallback](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteOccurrence(request)
    
    
    public deleteOccurrence(request: grafeas.v1.IDeleteOccurrenceRequest): Promise<google.protobuf.Empty>;

Calls DeleteOccurrence.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.ideleteoccurrencerequest)`   
DeleteOccurrenceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.google.protobuf.empty)>` | Promise  
  
### getNote(request, callback)
    
    
    public getNote(request: grafeas.v1.IGetNoteRequest, callback: grafeas.v1.Grafeas.GetNoteCallback): void;

Calls GetNote.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetNoteRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.igetnoterequest)`   
GetNoteRequest message or plain object  
`callback` |  `[GetNoteCallback](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)`   
Node-style callback called with the error, if any, and Note  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getNote(request)
    
    
    public getNote(request: grafeas.v1.IGetNoteRequest): Promise<grafeas.v1.Note>;

Calls GetNote.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetNoteRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.igetnoterequest)`   
GetNoteRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[grafeas.v1.Note](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.note)>` | Promise  
  
### getOccurrence(request, callback)
    
    
    public getOccurrence(request: grafeas.v1.IGetOccurrenceRequest, callback: grafeas.v1.Grafeas.GetOccurrenceCallback): void;

Calls GetOccurrence.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.igetoccurrencerequest)`   
GetOccurrenceRequest message or plain object  
`callback` |  `[GetOccurrenceCallback](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)`   
Node-style callback called with the error, if any, and Occurrence  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getOccurrence(request)
    
    
    public getOccurrence(request: grafeas.v1.IGetOccurrenceRequest): Promise<grafeas.v1.Occurrence>;

Calls GetOccurrence.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.igetoccurrencerequest)`   
GetOccurrenceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[grafeas.v1.Occurrence](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.occurrence)>` | Promise  
  
### getOccurrenceNote(request, callback)
    
    
    public getOccurrenceNote(request: grafeas.v1.IGetOccurrenceNoteRequest, callback: grafeas.v1.Grafeas.GetOccurrenceNoteCallback): void;

Calls GetOccurrenceNote.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetOccurrenceNoteRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.igetoccurrencenoterequest)`   
GetOccurrenceNoteRequest message or plain object  
`callback` |  `[GetOccurrenceNoteCallback](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)`   
Node-style callback called with the error, if any, and Note  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getOccurrenceNote(request)
    
    
    public getOccurrenceNote(request: grafeas.v1.IGetOccurrenceNoteRequest): Promise<grafeas.v1.Note>;

Calls GetOccurrenceNote.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetOccurrenceNoteRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.igetoccurrencenoterequest)`   
GetOccurrenceNoteRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[grafeas.v1.Note](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.note)>` | Promise  
  
### listNoteOccurrences(request, callback)
    
    
    public listNoteOccurrences(request: grafeas.v1.IListNoteOccurrencesRequest, callback: grafeas.v1.Grafeas.ListNoteOccurrencesCallback): void;

Calls ListNoteOccurrences.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListNoteOccurrencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.ilistnoteoccurrencesrequest)`   
ListNoteOccurrencesRequest message or plain object  
`callback` |  `[ListNoteOccurrencesCallback](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)`   
Node-style callback called with the error, if any, and ListNoteOccurrencesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listNoteOccurrences(request)
    
    
    public listNoteOccurrences(request: grafeas.v1.IListNoteOccurrencesRequest): Promise<grafeas.v1.ListNoteOccurrencesResponse>;

Calls ListNoteOccurrences.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListNoteOccurrencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.ilistnoteoccurrencesrequest)`   
ListNoteOccurrencesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[grafeas.v1.ListNoteOccurrencesResponse](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.listnoteoccurrencesresponse)>` | Promise  
  
### listNotes(request, callback)
    
    
    public listNotes(request: grafeas.v1.IListNotesRequest, callback: grafeas.v1.Grafeas.ListNotesCallback): void;

Calls ListNotes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListNotesRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.ilistnotesrequest)`   
ListNotesRequest message or plain object  
`callback` |  `[ListNotesCallback](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)`   
Node-style callback called with the error, if any, and ListNotesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listNotes(request)
    
    
    public listNotes(request: grafeas.v1.IListNotesRequest): Promise<grafeas.v1.ListNotesResponse>;

Calls ListNotes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListNotesRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.ilistnotesrequest)`   
ListNotesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[grafeas.v1.ListNotesResponse](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.listnotesresponse)>` | Promise  
  
### listOccurrences(request, callback)
    
    
    public listOccurrences(request: grafeas.v1.IListOccurrencesRequest, callback: grafeas.v1.Grafeas.ListOccurrencesCallback): void;

Calls ListOccurrences.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOccurrencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.ilistoccurrencesrequest)`   
ListOccurrencesRequest message or plain object  
`callback` |  `[ListOccurrencesCallback](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)`   
Node-style callback called with the error, if any, and ListOccurrencesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listOccurrences(request)
    
    
    public listOccurrences(request: grafeas.v1.IListOccurrencesRequest): Promise<grafeas.v1.ListOccurrencesResponse>;

Calls ListOccurrences.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListOccurrencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.ilistoccurrencesrequest)`   
ListOccurrencesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[grafeas.v1.ListOccurrencesResponse](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.listoccurrencesresponse)>` | Promise  
  
### updateNote(request, callback)
    
    
    public updateNote(request: grafeas.v1.IUpdateNoteRequest, callback: grafeas.v1.Grafeas.UpdateNoteCallback): void;

Calls UpdateNote.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateNoteRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.iupdatenoterequest)`   
UpdateNoteRequest message or plain object  
`callback` |  `[UpdateNoteCallback](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)`   
Node-style callback called with the error, if any, and Note  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateNote(request)
    
    
    public updateNote(request: grafeas.v1.IUpdateNoteRequest): Promise<grafeas.v1.Note>;

Calls UpdateNote.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateNoteRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.iupdatenoterequest)`   
UpdateNoteRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[grafeas.v1.Note](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.note)>` | Promise  
  
### updateOccurrence(request, callback)
    
    
    public updateOccurrence(request: grafeas.v1.IUpdateOccurrenceRequest, callback: grafeas.v1.Grafeas.UpdateOccurrenceCallback): void;

Calls UpdateOccurrence.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.iupdateoccurrencerequest)`   
UpdateOccurrenceRequest message or plain object  
`callback` |  `[UpdateOccurrenceCallback](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)`   
Node-style callback called with the error, if any, and Occurrence  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateOccurrence(request)
    
    
    public updateOccurrence(request: grafeas.v1.IUpdateOccurrenceRequest): Promise<grafeas.v1.Occurrence>;

Calls UpdateOccurrence.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.iupdateoccurrencerequest)`   
UpdateOccurrenceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[grafeas.v1.Occurrence](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/protos.grafeas.v1.occurrence)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
