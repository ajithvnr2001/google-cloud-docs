---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.catalogservice-class
title: Class protos.google.cloud.dataplex.v1.CatalogService (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:33:25.817613+00:00
---

# Class protos.google.cloud.dataplex.v1.CatalogService (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.catalogservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataplex.v1.CatalogService (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.4.0  5.3.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.5.1  3.2.0  3.1.0  2.4.0  2.3.2  2.2.2  2.1.1  1.2.0  1.1.0  1.0.0 

Represents a CatalogService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dataplex.v1.CatalogService

## Package

[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new CatalogService service.

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

### cancelMetadataJob(request, callback)
    
    
    public cancelMetadataJob(request: google.cloud.dataplex.v1.ICancelMetadataJobRequest, callback: google.cloud.dataplex.v1.CatalogService.CancelMetadataJobCallback): void;

Calls CancelMetadataJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelMetadataJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icancelmetadatajobrequest)`   
CancelMetadataJobRequest message or plain object  
`callback` |  `[CancelMetadataJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelMetadataJob(request)
    
    
    public cancelMetadataJob(request: google.cloud.dataplex.v1.ICancelMetadataJobRequest): Promise<google.protobuf.Empty>;

Calls CancelMetadataJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICancelMetadataJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icancelmetadatajobrequest)`   
CancelMetadataJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.protobuf.empty)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): CatalogService;

Creates new CatalogService service using the specified rpc implementation.

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
`[CatalogService](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.catalogservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAspectType(request, callback)
    
    
    public createAspectType(request: google.cloud.dataplex.v1.ICreateAspectTypeRequest, callback: google.cloud.dataplex.v1.CatalogService.CreateAspectTypeCallback): void;

Calls CreateAspectType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAspectTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreateaspecttyperequest)`   
CreateAspectTypeRequest message or plain object  
`callback` |  `[CreateAspectTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAspectType(request)
    
    
    public createAspectType(request: google.cloud.dataplex.v1.ICreateAspectTypeRequest): Promise<google.longrunning.Operation>;

Calls CreateAspectType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAspectTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreateaspecttyperequest)`   
CreateAspectTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### createEntry(request, callback)
    
    
    public createEntry(request: google.cloud.dataplex.v1.ICreateEntryRequest, callback: google.cloud.dataplex.v1.CatalogService.CreateEntryCallback): void;

Calls CreateEntry.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreateentryrequest)`   
CreateEntryRequest message or plain object  
`callback` |  `[CreateEntryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Entry  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEntry(request)
    
    
    public createEntry(request: google.cloud.dataplex.v1.ICreateEntryRequest): Promise<google.cloud.dataplex.v1.Entry>;

Calls CreateEntry.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreateentryrequest)`   
CreateEntryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.Entry](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.entry)>` | Promise  
  
### createEntryGroup(request, callback)
    
    
    public createEntryGroup(request: google.cloud.dataplex.v1.ICreateEntryGroupRequest, callback: google.cloud.dataplex.v1.CatalogService.CreateEntryGroupCallback): void;

Calls CreateEntryGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEntryGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreateentrygrouprequest)`   
CreateEntryGroupRequest message or plain object  
`callback` |  `[CreateEntryGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEntryGroup(request)
    
    
    public createEntryGroup(request: google.cloud.dataplex.v1.ICreateEntryGroupRequest): Promise<google.longrunning.Operation>;

Calls CreateEntryGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateEntryGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreateentrygrouprequest)`   
CreateEntryGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### createEntryLink(request, callback)
    
    
    public createEntryLink(request: google.cloud.dataplex.v1.ICreateEntryLinkRequest, callback: google.cloud.dataplex.v1.CatalogService.CreateEntryLinkCallback): void;

Calls CreateEntryLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEntryLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreateentrylinkrequest)`   
CreateEntryLinkRequest message or plain object  
`callback` |  `[CreateEntryLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and EntryLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEntryLink(request)
    
    
    public createEntryLink(request: google.cloud.dataplex.v1.ICreateEntryLinkRequest): Promise<google.cloud.dataplex.v1.EntryLink>;

Calls CreateEntryLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateEntryLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreateentrylinkrequest)`   
CreateEntryLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.EntryLink](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.entrylink-class)>` | Promise  
  
### createEntryType(request, callback)
    
    
    public createEntryType(request: google.cloud.dataplex.v1.ICreateEntryTypeRequest, callback: google.cloud.dataplex.v1.CatalogService.CreateEntryTypeCallback): void;

Calls CreateEntryType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEntryTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreateentrytyperequest)`   
CreateEntryTypeRequest message or plain object  
`callback` |  `[CreateEntryTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEntryType(request)
    
    
    public createEntryType(request: google.cloud.dataplex.v1.ICreateEntryTypeRequest): Promise<google.longrunning.Operation>;

Calls CreateEntryType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateEntryTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreateentrytyperequest)`   
CreateEntryTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### createMetadataFeed(request, callback)
    
    
    public createMetadataFeed(request: google.cloud.dataplex.v1.ICreateMetadataFeedRequest, callback: google.cloud.dataplex.v1.CatalogService.CreateMetadataFeedCallback): void;

Calls CreateMetadataFeed.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMetadataFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatemetadatafeedrequest)`   
CreateMetadataFeedRequest message or plain object  
`callback` |  `[CreateMetadataFeedCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMetadataFeed(request)
    
    
    public createMetadataFeed(request: google.cloud.dataplex.v1.ICreateMetadataFeedRequest): Promise<google.longrunning.Operation>;

Calls CreateMetadataFeed.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateMetadataFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatemetadatafeedrequest)`   
CreateMetadataFeedRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### createMetadataJob(request, callback)
    
    
    public createMetadataJob(request: google.cloud.dataplex.v1.ICreateMetadataJobRequest, callback: google.cloud.dataplex.v1.CatalogService.CreateMetadataJobCallback): void;

Calls CreateMetadataJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMetadataJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatemetadatajobrequest)`   
CreateMetadataJobRequest message or plain object  
`callback` |  `[CreateMetadataJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMetadataJob(request)
    
    
    public createMetadataJob(request: google.cloud.dataplex.v1.ICreateMetadataJobRequest): Promise<google.longrunning.Operation>;

Calls CreateMetadataJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateMetadataJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreatemetadatajobrequest)`   
CreateMetadataJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### deleteAspectType(request, callback)
    
    
    public deleteAspectType(request: google.cloud.dataplex.v1.IDeleteAspectTypeRequest, callback: google.cloud.dataplex.v1.CatalogService.DeleteAspectTypeCallback): void;

Calls DeleteAspectType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAspectTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideleteaspecttyperequest)`   
DeleteAspectTypeRequest message or plain object  
`callback` |  `[DeleteAspectTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAspectType(request)
    
    
    public deleteAspectType(request: google.cloud.dataplex.v1.IDeleteAspectTypeRequest): Promise<google.longrunning.Operation>;

Calls DeleteAspectType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAspectTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideleteaspecttyperequest)`   
DeleteAspectTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### deleteEntry(request, callback)
    
    
    public deleteEntry(request: google.cloud.dataplex.v1.IDeleteEntryRequest, callback: google.cloud.dataplex.v1.CatalogService.DeleteEntryCallback): void;

Calls DeleteEntry.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideleteentryrequest)`   
DeleteEntryRequest message or plain object  
`callback` |  `[DeleteEntryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Entry  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEntry(request)
    
    
    public deleteEntry(request: google.cloud.dataplex.v1.IDeleteEntryRequest): Promise<google.cloud.dataplex.v1.Entry>;

Calls DeleteEntry.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideleteentryrequest)`   
DeleteEntryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.Entry](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.entry)>` | Promise  
  
### deleteEntryGroup(request, callback)
    
    
    public deleteEntryGroup(request: google.cloud.dataplex.v1.IDeleteEntryGroupRequest, callback: google.cloud.dataplex.v1.CatalogService.DeleteEntryGroupCallback): void;

Calls DeleteEntryGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEntryGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideleteentrygrouprequest)`   
DeleteEntryGroupRequest message or plain object  
`callback` |  `[DeleteEntryGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEntryGroup(request)
    
    
    public deleteEntryGroup(request: google.cloud.dataplex.v1.IDeleteEntryGroupRequest): Promise<google.longrunning.Operation>;

Calls DeleteEntryGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEntryGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideleteentrygrouprequest)`   
DeleteEntryGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### deleteEntryLink(request, callback)
    
    
    public deleteEntryLink(request: google.cloud.dataplex.v1.IDeleteEntryLinkRequest, callback: google.cloud.dataplex.v1.CatalogService.DeleteEntryLinkCallback): void;

Calls DeleteEntryLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEntryLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideleteentrylinkrequest)`   
DeleteEntryLinkRequest message or plain object  
`callback` |  `[DeleteEntryLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and EntryLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEntryLink(request)
    
    
    public deleteEntryLink(request: google.cloud.dataplex.v1.IDeleteEntryLinkRequest): Promise<google.cloud.dataplex.v1.EntryLink>;

Calls DeleteEntryLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEntryLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideleteentrylinkrequest)`   
DeleteEntryLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.EntryLink](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.entrylink-class)>` | Promise  
  
### deleteEntryType(request, callback)
    
    
    public deleteEntryType(request: google.cloud.dataplex.v1.IDeleteEntryTypeRequest, callback: google.cloud.dataplex.v1.CatalogService.DeleteEntryTypeCallback): void;

Calls DeleteEntryType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEntryTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideleteentrytyperequest)`   
DeleteEntryTypeRequest message or plain object  
`callback` |  `[DeleteEntryTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEntryType(request)
    
    
    public deleteEntryType(request: google.cloud.dataplex.v1.IDeleteEntryTypeRequest): Promise<google.longrunning.Operation>;

Calls DeleteEntryType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEntryTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideleteentrytyperequest)`   
DeleteEntryTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### deleteMetadataFeed(request, callback)
    
    
    public deleteMetadataFeed(request: google.cloud.dataplex.v1.IDeleteMetadataFeedRequest, callback: google.cloud.dataplex.v1.CatalogService.DeleteMetadataFeedCallback): void;

Calls DeleteMetadataFeed.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMetadataFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideletemetadatafeedrequest)`   
DeleteMetadataFeedRequest message or plain object  
`callback` |  `[DeleteMetadataFeedCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMetadataFeed(request)
    
    
    public deleteMetadataFeed(request: google.cloud.dataplex.v1.IDeleteMetadataFeedRequest): Promise<google.longrunning.Operation>;

Calls DeleteMetadataFeed.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMetadataFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideletemetadatafeedrequest)`   
DeleteMetadataFeedRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### getAspectType(request, callback)
    
    
    public getAspectType(request: google.cloud.dataplex.v1.IGetAspectTypeRequest, callback: google.cloud.dataplex.v1.CatalogService.GetAspectTypeCallback): void;

Calls GetAspectType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAspectTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetaspecttyperequest)`   
GetAspectTypeRequest message or plain object  
`callback` |  `[GetAspectTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and AspectType  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAspectType(request)
    
    
    public getAspectType(request: google.cloud.dataplex.v1.IGetAspectTypeRequest): Promise<google.cloud.dataplex.v1.AspectType>;

Calls GetAspectType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAspectTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetaspecttyperequest)`   
GetAspectTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.AspectType](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.aspecttype-class)>` | Promise  
  
### getEntry(request, callback)
    
    
    public getEntry(request: google.cloud.dataplex.v1.IGetEntryRequest, callback: google.cloud.dataplex.v1.CatalogService.GetEntryCallback): void;

Calls GetEntry.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetentryrequest)`   
GetEntryRequest message or plain object  
`callback` |  `[GetEntryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Entry  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEntry(request)
    
    
    public getEntry(request: google.cloud.dataplex.v1.IGetEntryRequest): Promise<google.cloud.dataplex.v1.Entry>;

Calls GetEntry.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetentryrequest)`   
GetEntryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.Entry](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.entry)>` | Promise  
  
### getEntryGroup(request, callback)
    
    
    public getEntryGroup(request: google.cloud.dataplex.v1.IGetEntryGroupRequest, callback: google.cloud.dataplex.v1.CatalogService.GetEntryGroupCallback): void;

Calls GetEntryGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEntryGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetentrygrouprequest)`   
GetEntryGroupRequest message or plain object  
`callback` |  `[GetEntryGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and EntryGroup  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEntryGroup(request)
    
    
    public getEntryGroup(request: google.cloud.dataplex.v1.IGetEntryGroupRequest): Promise<google.cloud.dataplex.v1.EntryGroup>;

Calls GetEntryGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEntryGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetentrygrouprequest)`   
GetEntryGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.EntryGroup](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.entrygroup)>` | Promise  
  
### getEntryLink(request, callback)
    
    
    public getEntryLink(request: google.cloud.dataplex.v1.IGetEntryLinkRequest, callback: google.cloud.dataplex.v1.CatalogService.GetEntryLinkCallback): void;

Calls GetEntryLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEntryLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetentrylinkrequest)`   
GetEntryLinkRequest message or plain object  
`callback` |  `[GetEntryLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and EntryLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEntryLink(request)
    
    
    public getEntryLink(request: google.cloud.dataplex.v1.IGetEntryLinkRequest): Promise<google.cloud.dataplex.v1.EntryLink>;

Calls GetEntryLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEntryLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetentrylinkrequest)`   
GetEntryLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.EntryLink](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.entrylink-class)>` | Promise  
  
### getEntryType(request, callback)
    
    
    public getEntryType(request: google.cloud.dataplex.v1.IGetEntryTypeRequest, callback: google.cloud.dataplex.v1.CatalogService.GetEntryTypeCallback): void;

Calls GetEntryType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEntryTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetentrytyperequest)`   
GetEntryTypeRequest message or plain object  
`callback` |  `[GetEntryTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and EntryType  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEntryType(request)
    
    
    public getEntryType(request: google.cloud.dataplex.v1.IGetEntryTypeRequest): Promise<google.cloud.dataplex.v1.EntryType>;

Calls GetEntryType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEntryTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetentrytyperequest)`   
GetEntryTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.EntryType](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.entrytype-class)>` | Promise  
  
### getMetadataFeed(request, callback)
    
    
    public getMetadataFeed(request: google.cloud.dataplex.v1.IGetMetadataFeedRequest, callback: google.cloud.dataplex.v1.CatalogService.GetMetadataFeedCallback): void;

Calls GetMetadataFeed.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMetadataFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetmetadatafeedrequest)`   
GetMetadataFeedRequest message or plain object  
`callback` |  `[GetMetadataFeedCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and MetadataFeed  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMetadataFeed(request)
    
    
    public getMetadataFeed(request: google.cloud.dataplex.v1.IGetMetadataFeedRequest): Promise<google.cloud.dataplex.v1.MetadataFeed>;

Calls GetMetadataFeed.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetMetadataFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetmetadatafeedrequest)`   
GetMetadataFeedRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.MetadataFeed](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.metadatafeed-class)>` | Promise  
  
### getMetadataJob(request, callback)
    
    
    public getMetadataJob(request: google.cloud.dataplex.v1.IGetMetadataJobRequest, callback: google.cloud.dataplex.v1.CatalogService.GetMetadataJobCallback): void;

Calls GetMetadataJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMetadataJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetmetadatajobrequest)`   
GetMetadataJobRequest message or plain object  
`callback` |  `[GetMetadataJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and MetadataJob  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMetadataJob(request)
    
    
    public getMetadataJob(request: google.cloud.dataplex.v1.IGetMetadataJobRequest): Promise<google.cloud.dataplex.v1.MetadataJob>;

Calls GetMetadataJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetMetadataJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetmetadatajobrequest)`   
GetMetadataJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.MetadataJob](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.metadatajob-class)>` | Promise  
  
### listAspectTypes(request, callback)
    
    
    public listAspectTypes(request: google.cloud.dataplex.v1.IListAspectTypesRequest, callback: google.cloud.dataplex.v1.CatalogService.ListAspectTypesCallback): void;

Calls ListAspectTypes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAspectTypesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistaspecttypesrequest)`   
ListAspectTypesRequest message or plain object  
`callback` |  `[ListAspectTypesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAspectTypesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAspectTypes(request)
    
    
    public listAspectTypes(request: google.cloud.dataplex.v1.IListAspectTypesRequest): Promise<google.cloud.dataplex.v1.ListAspectTypesResponse>;

Calls ListAspectTypes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAspectTypesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistaspecttypesrequest)`   
ListAspectTypesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListAspectTypesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listaspecttypesresponse)>` | Promise  
  
### listEntries(request, callback)
    
    
    public listEntries(request: google.cloud.dataplex.v1.IListEntriesRequest, callback: google.cloud.dataplex.v1.CatalogService.ListEntriesCallback): void;

Calls ListEntries.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEntriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistentriesrequest)`   
ListEntriesRequest message or plain object  
`callback` |  `[ListEntriesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListEntriesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEntries(request)
    
    
    public listEntries(request: google.cloud.dataplex.v1.IListEntriesRequest): Promise<google.cloud.dataplex.v1.ListEntriesResponse>;

Calls ListEntries.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListEntriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistentriesrequest)`   
ListEntriesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListEntriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listentriesresponse)>` | Promise  
  
### listEntryGroups(request, callback)
    
    
    public listEntryGroups(request: google.cloud.dataplex.v1.IListEntryGroupsRequest, callback: google.cloud.dataplex.v1.CatalogService.ListEntryGroupsCallback): void;

Calls ListEntryGroups.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEntryGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistentrygroupsrequest)`   
ListEntryGroupsRequest message or plain object  
`callback` |  `[ListEntryGroupsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListEntryGroupsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEntryGroups(request)
    
    
    public listEntryGroups(request: google.cloud.dataplex.v1.IListEntryGroupsRequest): Promise<google.cloud.dataplex.v1.ListEntryGroupsResponse>;

Calls ListEntryGroups.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListEntryGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistentrygroupsrequest)`   
ListEntryGroupsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListEntryGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listentrygroupsresponse)>` | Promise  
  
### listEntryTypes(request, callback)
    
    
    public listEntryTypes(request: google.cloud.dataplex.v1.IListEntryTypesRequest, callback: google.cloud.dataplex.v1.CatalogService.ListEntryTypesCallback): void;

Calls ListEntryTypes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEntryTypesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistentrytypesrequest)`   
ListEntryTypesRequest message or plain object  
`callback` |  `[ListEntryTypesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListEntryTypesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEntryTypes(request)
    
    
    public listEntryTypes(request: google.cloud.dataplex.v1.IListEntryTypesRequest): Promise<google.cloud.dataplex.v1.ListEntryTypesResponse>;

Calls ListEntryTypes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListEntryTypesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistentrytypesrequest)`   
ListEntryTypesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListEntryTypesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listentrytypesresponse)>` | Promise  
  
### listMetadataFeeds(request, callback)
    
    
    public listMetadataFeeds(request: google.cloud.dataplex.v1.IListMetadataFeedsRequest, callback: google.cloud.dataplex.v1.CatalogService.ListMetadataFeedsCallback): void;

Calls ListMetadataFeeds.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMetadataFeedsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistmetadatafeedsrequest)`   
ListMetadataFeedsRequest message or plain object  
`callback` |  `[ListMetadataFeedsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMetadataFeedsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMetadataFeeds(request)
    
    
    public listMetadataFeeds(request: google.cloud.dataplex.v1.IListMetadataFeedsRequest): Promise<google.cloud.dataplex.v1.ListMetadataFeedsResponse>;

Calls ListMetadataFeeds.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMetadataFeedsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistmetadatafeedsrequest)`   
ListMetadataFeedsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListMetadataFeedsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listmetadatafeedsresponse)>` | Promise  
  
### listMetadataJobs(request, callback)
    
    
    public listMetadataJobs(request: google.cloud.dataplex.v1.IListMetadataJobsRequest, callback: google.cloud.dataplex.v1.CatalogService.ListMetadataJobsCallback): void;

Calls ListMetadataJobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMetadataJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistmetadatajobsrequest)`   
ListMetadataJobsRequest message or plain object  
`callback` |  `[ListMetadataJobsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMetadataJobsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMetadataJobs(request)
    
    
    public listMetadataJobs(request: google.cloud.dataplex.v1.IListMetadataJobsRequest): Promise<google.cloud.dataplex.v1.ListMetadataJobsResponse>;

Calls ListMetadataJobs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMetadataJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistmetadatajobsrequest)`   
ListMetadataJobsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListMetadataJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listmetadatajobsresponse)>` | Promise  
  
### lookupContext(request, callback)
    
    
    public lookupContext(request: google.cloud.dataplex.v1.ILookupContextRequest, callback: google.cloud.dataplex.v1.CatalogService.LookupContextCallback): void;

Calls LookupContext.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupContextRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilookupcontextrequest)`   
LookupContextRequest message or plain object  
`callback` |  `[LookupContextCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and LookupContextResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### lookupContext(request)
    
    
    public lookupContext(request: google.cloud.dataplex.v1.ILookupContextRequest): Promise<google.cloud.dataplex.v1.LookupContextResponse>;

Calls LookupContext.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ILookupContextRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilookupcontextrequest)`   
LookupContextRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.LookupContextResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.lookupcontextresponse)>` | Promise  
  
### lookupEntry(request, callback)
    
    
    public lookupEntry(request: google.cloud.dataplex.v1.ILookupEntryRequest, callback: google.cloud.dataplex.v1.CatalogService.LookupEntryCallback): void;

Calls LookupEntry.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilookupentryrequest)`   
LookupEntryRequest message or plain object  
`callback` |  `[LookupEntryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Entry  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### lookupEntry(request)
    
    
    public lookupEntry(request: google.cloud.dataplex.v1.ILookupEntryRequest): Promise<google.cloud.dataplex.v1.Entry>;

Calls LookupEntry.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ILookupEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilookupentryrequest)`   
LookupEntryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.Entry](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.entry)>` | Promise  
  
### lookupEntryLinks(request, callback)
    
    
    public lookupEntryLinks(request: google.cloud.dataplex.v1.ILookupEntryLinksRequest, callback: google.cloud.dataplex.v1.CatalogService.LookupEntryLinksCallback): void;

Calls LookupEntryLinks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupEntryLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilookupentrylinksrequest)`   
LookupEntryLinksRequest message or plain object  
`callback` |  `[LookupEntryLinksCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and LookupEntryLinksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### lookupEntryLinks(request)
    
    
    public lookupEntryLinks(request: google.cloud.dataplex.v1.ILookupEntryLinksRequest): Promise<google.cloud.dataplex.v1.LookupEntryLinksResponse>;

Calls LookupEntryLinks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ILookupEntryLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilookupentrylinksrequest)`   
LookupEntryLinksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.LookupEntryLinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.lookupentrylinksresponse)>` | Promise  
  
### modifyEntry(request, callback)
    
    
    public modifyEntry(request: google.cloud.dataplex.v1.IModifyEntryRequest, callback: google.cloud.dataplex.v1.CatalogService.ModifyEntryCallback): void;

Calls ModifyEntry.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IModifyEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.imodifyentryrequest)`   
ModifyEntryRequest message or plain object  
`callback` |  `[ModifyEntryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Entry  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### modifyEntry(request)
    
    
    public modifyEntry(request: google.cloud.dataplex.v1.IModifyEntryRequest): Promise<google.cloud.dataplex.v1.Entry>;

Calls ModifyEntry.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IModifyEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.imodifyentryrequest)`   
ModifyEntryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.Entry](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.entry)>` | Promise  
  
### searchEntries(request, callback)
    
    
    public searchEntries(request: google.cloud.dataplex.v1.ISearchEntriesRequest, callback: google.cloud.dataplex.v1.CatalogService.SearchEntriesCallback): void;

Calls SearchEntries.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchEntriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.isearchentriesrequest)`   
SearchEntriesRequest message or plain object  
`callback` |  `[SearchEntriesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchEntriesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchEntries(request)
    
    
    public searchEntries(request: google.cloud.dataplex.v1.ISearchEntriesRequest): Promise<google.cloud.dataplex.v1.SearchEntriesResponse>;

Calls SearchEntries.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchEntriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.isearchentriesrequest)`   
SearchEntriesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.SearchEntriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.searchentriesresponse)>` | Promise  
  
### updateAspectType(request, callback)
    
    
    public updateAspectType(request: google.cloud.dataplex.v1.IUpdateAspectTypeRequest, callback: google.cloud.dataplex.v1.CatalogService.UpdateAspectTypeCallback): void;

Calls UpdateAspectType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAspectTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdateaspecttyperequest)`   
UpdateAspectTypeRequest message or plain object  
`callback` |  `[UpdateAspectTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAspectType(request)
    
    
    public updateAspectType(request: google.cloud.dataplex.v1.IUpdateAspectTypeRequest): Promise<google.longrunning.Operation>;

Calls UpdateAspectType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAspectTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdateaspecttyperequest)`   
UpdateAspectTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### updateEntry(request, callback)
    
    
    public updateEntry(request: google.cloud.dataplex.v1.IUpdateEntryRequest, callback: google.cloud.dataplex.v1.CatalogService.UpdateEntryCallback): void;

Calls UpdateEntry.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdateentryrequest)`   
UpdateEntryRequest message or plain object  
`callback` |  `[UpdateEntryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Entry  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEntry(request)
    
    
    public updateEntry(request: google.cloud.dataplex.v1.IUpdateEntryRequest): Promise<google.cloud.dataplex.v1.Entry>;

Calls UpdateEntry.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdateentryrequest)`   
UpdateEntryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.Entry](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.entry)>` | Promise  
  
### updateEntryGroup(request, callback)
    
    
    public updateEntryGroup(request: google.cloud.dataplex.v1.IUpdateEntryGroupRequest, callback: google.cloud.dataplex.v1.CatalogService.UpdateEntryGroupCallback): void;

Calls UpdateEntryGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEntryGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdateentrygrouprequest)`   
UpdateEntryGroupRequest message or plain object  
`callback` |  `[UpdateEntryGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEntryGroup(request)
    
    
    public updateEntryGroup(request: google.cloud.dataplex.v1.IUpdateEntryGroupRequest): Promise<google.longrunning.Operation>;

Calls UpdateEntryGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEntryGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdateentrygrouprequest)`   
UpdateEntryGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### updateEntryLink(request, callback)
    
    
    public updateEntryLink(request: google.cloud.dataplex.v1.IUpdateEntryLinkRequest, callback: google.cloud.dataplex.v1.CatalogService.UpdateEntryLinkCallback): void;

Calls UpdateEntryLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEntryLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdateentrylinkrequest)`   
UpdateEntryLinkRequest message or plain object  
`callback` |  `[UpdateEntryLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and EntryLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEntryLink(request)
    
    
    public updateEntryLink(request: google.cloud.dataplex.v1.IUpdateEntryLinkRequest): Promise<google.cloud.dataplex.v1.EntryLink>;

Calls UpdateEntryLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEntryLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdateentrylinkrequest)`   
UpdateEntryLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.EntryLink](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.entrylink-class)>` | Promise  
  
### updateEntryType(request, callback)
    
    
    public updateEntryType(request: google.cloud.dataplex.v1.IUpdateEntryTypeRequest, callback: google.cloud.dataplex.v1.CatalogService.UpdateEntryTypeCallback): void;

Calls UpdateEntryType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEntryTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdateentrytyperequest)`   
UpdateEntryTypeRequest message or plain object  
`callback` |  `[UpdateEntryTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEntryType(request)
    
    
    public updateEntryType(request: google.cloud.dataplex.v1.IUpdateEntryTypeRequest): Promise<google.longrunning.Operation>;

Calls UpdateEntryType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEntryTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdateentrytyperequest)`   
UpdateEntryTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### updateMetadataFeed(request, callback)
    
    
    public updateMetadataFeed(request: google.cloud.dataplex.v1.IUpdateMetadataFeedRequest, callback: google.cloud.dataplex.v1.CatalogService.UpdateMetadataFeedCallback): void;

Calls UpdateMetadataFeed.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMetadataFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdatemetadatafeedrequest)`   
UpdateMetadataFeedRequest message or plain object  
`callback` |  `[UpdateMetadataFeedCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMetadataFeed(request)
    
    
    public updateMetadataFeed(request: google.cloud.dataplex.v1.IUpdateMetadataFeedRequest): Promise<google.longrunning.Operation>;

Calls UpdateMetadataFeed.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMetadataFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdatemetadatafeedrequest)`   
UpdateMetadataFeedRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
