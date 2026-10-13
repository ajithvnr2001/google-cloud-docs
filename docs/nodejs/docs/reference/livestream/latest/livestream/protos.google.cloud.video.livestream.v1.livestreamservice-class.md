---
url: https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.livestreamservice-class
title: Class protos.google.cloud.video.livestream.v1.LivestreamService (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:04:23.244025+00:00
---

# Class protos.google.cloud.video.livestream.v1.LivestreamService (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.livestreamservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.video.livestream.v1.LivestreamService (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  1.0.2  0.5.1  0.4.1  0.3.4  0.1.0 

Represents a LivestreamService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.video.livestream.v1.LivestreamService

## Package

[@google-cloud/livestream](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new LivestreamService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): LivestreamService;

Creates new LivestreamService service using the specified rpc implementation.

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
`[LivestreamService](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.livestreamservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAsset(request, callback)
    
    
    public createAsset(request: google.cloud.video.livestream.v1.ICreateAssetRequest, callback: google.cloud.video.livestream.v1.LivestreamService.CreateAssetCallback): void;

Calls CreateAsset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.icreateassetrequest)`   
CreateAssetRequest message or plain object  
`callback` |  `[CreateAssetCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAsset(request)
    
    
    public createAsset(request: google.cloud.video.livestream.v1.ICreateAssetRequest): Promise<google.longrunning.Operation>;

Calls CreateAsset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.icreateassetrequest)`   
CreateAssetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.longrunning.operation)>` | Promise  
  
### createChannel(request, callback)
    
    
    public createChannel(request: google.cloud.video.livestream.v1.ICreateChannelRequest, callback: google.cloud.video.livestream.v1.LivestreamService.CreateChannelCallback): void;

Calls CreateChannel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateChannelRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.icreatechannelrequest)`   
CreateChannelRequest message or plain object  
`callback` |  `[CreateChannelCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createChannel(request)
    
    
    public createChannel(request: google.cloud.video.livestream.v1.ICreateChannelRequest): Promise<google.longrunning.Operation>;

Calls CreateChannel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateChannelRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.icreatechannelrequest)`   
CreateChannelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.longrunning.operation)>` | Promise  
  
### createClip(request, callback)
    
    
    public createClip(request: google.cloud.video.livestream.v1.ICreateClipRequest, callback: google.cloud.video.livestream.v1.LivestreamService.CreateClipCallback): void;

Calls CreateClip.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateClipRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.icreatecliprequest)`   
CreateClipRequest message or plain object  
`callback` |  `[CreateClipCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createClip(request)
    
    
    public createClip(request: google.cloud.video.livestream.v1.ICreateClipRequest): Promise<google.longrunning.Operation>;

Calls CreateClip.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateClipRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.icreatecliprequest)`   
CreateClipRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.longrunning.operation)>` | Promise  
  
### createDvrSession(request, callback)
    
    
    public createDvrSession(request: google.cloud.video.livestream.v1.ICreateDvrSessionRequest, callback: google.cloud.video.livestream.v1.LivestreamService.CreateDvrSessionCallback): void;

Calls CreateDvrSession.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDvrSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.icreatedvrsessionrequest)`   
CreateDvrSessionRequest message or plain object  
`callback` |  `[CreateDvrSessionCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDvrSession(request)
    
    
    public createDvrSession(request: google.cloud.video.livestream.v1.ICreateDvrSessionRequest): Promise<google.longrunning.Operation>;

Calls CreateDvrSession.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDvrSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.icreatedvrsessionrequest)`   
CreateDvrSessionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.longrunning.operation)>` | Promise  
  
### createEvent(request, callback)
    
    
    public createEvent(request: google.cloud.video.livestream.v1.ICreateEventRequest, callback: google.cloud.video.livestream.v1.LivestreamService.CreateEventCallback): void;

Calls CreateEvent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.icreateeventrequest)`   
CreateEventRequest message or plain object  
`callback` |  `[CreateEventCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Event  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEvent(request)
    
    
    public createEvent(request: google.cloud.video.livestream.v1.ICreateEventRequest): Promise<google.cloud.video.livestream.v1.Event>;

Calls CreateEvent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.icreateeventrequest)`   
CreateEventRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.video.livestream.v1.Event](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.event-class)>` | Promise  
  
### createInput(request, callback)
    
    
    public createInput(request: google.cloud.video.livestream.v1.ICreateInputRequest, callback: google.cloud.video.livestream.v1.LivestreamService.CreateInputCallback): void;

Calls CreateInput.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.icreateinputrequest)`   
CreateInputRequest message or plain object  
`callback` |  `[CreateInputCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createInput(request)
    
    
    public createInput(request: google.cloud.video.livestream.v1.ICreateInputRequest): Promise<google.longrunning.Operation>;

Calls CreateInput.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.icreateinputrequest)`   
CreateInputRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.longrunning.operation)>` | Promise  
  
### deleteAsset(request, callback)
    
    
    public deleteAsset(request: google.cloud.video.livestream.v1.IDeleteAssetRequest, callback: google.cloud.video.livestream.v1.LivestreamService.DeleteAssetCallback): void;

Calls DeleteAsset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ideleteassetrequest)`   
DeleteAssetRequest message or plain object  
`callback` |  `[DeleteAssetCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAsset(request)
    
    
    public deleteAsset(request: google.cloud.video.livestream.v1.IDeleteAssetRequest): Promise<google.longrunning.Operation>;

Calls DeleteAsset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ideleteassetrequest)`   
DeleteAssetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.longrunning.operation)>` | Promise  
  
### deleteChannel(request, callback)
    
    
    public deleteChannel(request: google.cloud.video.livestream.v1.IDeleteChannelRequest, callback: google.cloud.video.livestream.v1.LivestreamService.DeleteChannelCallback): void;

Calls DeleteChannel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteChannelRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ideletechannelrequest)`   
DeleteChannelRequest message or plain object  
`callback` |  `[DeleteChannelCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteChannel(request)
    
    
    public deleteChannel(request: google.cloud.video.livestream.v1.IDeleteChannelRequest): Promise<google.longrunning.Operation>;

Calls DeleteChannel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteChannelRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ideletechannelrequest)`   
DeleteChannelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.longrunning.operation)>` | Promise  
  
### deleteClip(request, callback)
    
    
    public deleteClip(request: google.cloud.video.livestream.v1.IDeleteClipRequest, callback: google.cloud.video.livestream.v1.LivestreamService.DeleteClipCallback): void;

Calls DeleteClip.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClipRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ideletecliprequest)`   
DeleteClipRequest message or plain object  
`callback` |  `[DeleteClipCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteClip(request)
    
    
    public deleteClip(request: google.cloud.video.livestream.v1.IDeleteClipRequest): Promise<google.longrunning.Operation>;

Calls DeleteClip.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClipRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ideletecliprequest)`   
DeleteClipRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.longrunning.operation)>` | Promise  
  
### deleteDvrSession(request, callback)
    
    
    public deleteDvrSession(request: google.cloud.video.livestream.v1.IDeleteDvrSessionRequest, callback: google.cloud.video.livestream.v1.LivestreamService.DeleteDvrSessionCallback): void;

Calls DeleteDvrSession.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDvrSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ideletedvrsessionrequest)`   
DeleteDvrSessionRequest message or plain object  
`callback` |  `[DeleteDvrSessionCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDvrSession(request)
    
    
    public deleteDvrSession(request: google.cloud.video.livestream.v1.IDeleteDvrSessionRequest): Promise<google.longrunning.Operation>;

Calls DeleteDvrSession.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDvrSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ideletedvrsessionrequest)`   
DeleteDvrSessionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.longrunning.operation)>` | Promise  
  
### deleteEvent(request, callback)
    
    
    public deleteEvent(request: google.cloud.video.livestream.v1.IDeleteEventRequest, callback: google.cloud.video.livestream.v1.LivestreamService.DeleteEventCallback): void;

Calls DeleteEvent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ideleteeventrequest)`   
DeleteEventRequest message or plain object  
`callback` |  `[DeleteEventCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEvent(request)
    
    
    public deleteEvent(request: google.cloud.video.livestream.v1.IDeleteEventRequest): Promise<google.protobuf.Empty>;

Calls DeleteEvent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ideleteeventrequest)`   
DeleteEventRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.protobuf.empty)>` | Promise  
  
### deleteInput(request, callback)
    
    
    public deleteInput(request: google.cloud.video.livestream.v1.IDeleteInputRequest, callback: google.cloud.video.livestream.v1.LivestreamService.DeleteInputCallback): void;

Calls DeleteInput.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ideleteinputrequest)`   
DeleteInputRequest message or plain object  
`callback` |  `[DeleteInputCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteInput(request)
    
    
    public deleteInput(request: google.cloud.video.livestream.v1.IDeleteInputRequest): Promise<google.longrunning.Operation>;

Calls DeleteInput.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ideleteinputrequest)`   
DeleteInputRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.longrunning.operation)>` | Promise  
  
### getAsset(request, callback)
    
    
    public getAsset(request: google.cloud.video.livestream.v1.IGetAssetRequest, callback: google.cloud.video.livestream.v1.LivestreamService.GetAssetCallback): void;

Calls GetAsset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.igetassetrequest)`   
GetAssetRequest message or plain object  
`callback` |  `[GetAssetCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Asset  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAsset(request)
    
    
    public getAsset(request: google.cloud.video.livestream.v1.IGetAssetRequest): Promise<google.cloud.video.livestream.v1.Asset>;

Calls GetAsset.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAssetRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.igetassetrequest)`   
GetAssetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.video.livestream.v1.Asset](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.asset-class)>` | Promise  
  
### getChannel(request, callback)
    
    
    public getChannel(request: google.cloud.video.livestream.v1.IGetChannelRequest, callback: google.cloud.video.livestream.v1.LivestreamService.GetChannelCallback): void;

Calls GetChannel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetChannelRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.igetchannelrequest)`   
GetChannelRequest message or plain object  
`callback` |  `[GetChannelCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Channel  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getChannel(request)
    
    
    public getChannel(request: google.cloud.video.livestream.v1.IGetChannelRequest): Promise<google.cloud.video.livestream.v1.Channel>;

Calls GetChannel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetChannelRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.igetchannelrequest)`   
GetChannelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.video.livestream.v1.Channel](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.channel-class)>` | Promise  
  
### getClip(request, callback)
    
    
    public getClip(request: google.cloud.video.livestream.v1.IGetClipRequest, callback: google.cloud.video.livestream.v1.LivestreamService.GetClipCallback): void;

Calls GetClip.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetClipRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.igetcliprequest)`   
GetClipRequest message or plain object  
`callback` |  `[GetClipCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Clip  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getClip(request)
    
    
    public getClip(request: google.cloud.video.livestream.v1.IGetClipRequest): Promise<google.cloud.video.livestream.v1.Clip>;

Calls GetClip.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetClipRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.igetcliprequest)`   
GetClipRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.video.livestream.v1.Clip](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.clip-class)>` | Promise  
  
### getDvrSession(request, callback)
    
    
    public getDvrSession(request: google.cloud.video.livestream.v1.IGetDvrSessionRequest, callback: google.cloud.video.livestream.v1.LivestreamService.GetDvrSessionCallback): void;

Calls GetDvrSession.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDvrSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.igetdvrsessionrequest)`   
GetDvrSessionRequest message or plain object  
`callback` |  `[GetDvrSessionCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and DvrSession  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDvrSession(request)
    
    
    public getDvrSession(request: google.cloud.video.livestream.v1.IGetDvrSessionRequest): Promise<google.cloud.video.livestream.v1.DvrSession>;

Calls GetDvrSession.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDvrSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.igetdvrsessionrequest)`   
GetDvrSessionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.video.livestream.v1.DvrSession](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.dvrsession-class)>` | Promise  
  
### getEvent(request, callback)
    
    
    public getEvent(request: google.cloud.video.livestream.v1.IGetEventRequest, callback: google.cloud.video.livestream.v1.LivestreamService.GetEventCallback): void;

Calls GetEvent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.igeteventrequest)`   
GetEventRequest message or plain object  
`callback` |  `[GetEventCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Event  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEvent(request)
    
    
    public getEvent(request: google.cloud.video.livestream.v1.IGetEventRequest): Promise<google.cloud.video.livestream.v1.Event>;

Calls GetEvent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.igeteventrequest)`   
GetEventRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.video.livestream.v1.Event](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.event-class)>` | Promise  
  
### getInput(request, callback)
    
    
    public getInput(request: google.cloud.video.livestream.v1.IGetInputRequest, callback: google.cloud.video.livestream.v1.LivestreamService.GetInputCallback): void;

Calls GetInput.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.igetinputrequest)`   
GetInputRequest message or plain object  
`callback` |  `[GetInputCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Input  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getInput(request)
    
    
    public getInput(request: google.cloud.video.livestream.v1.IGetInputRequest): Promise<google.cloud.video.livestream.v1.Input>;

Calls GetInput.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.igetinputrequest)`   
GetInputRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.video.livestream.v1.Input](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.input-class)>` | Promise  
  
### getPool(request, callback)
    
    
    public getPool(request: google.cloud.video.livestream.v1.IGetPoolRequest, callback: google.cloud.video.livestream.v1.LivestreamService.GetPoolCallback): void;

Calls GetPool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.igetpoolrequest)`   
GetPoolRequest message or plain object  
`callback` |  `[GetPoolCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Pool  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPool(request)
    
    
    public getPool(request: google.cloud.video.livestream.v1.IGetPoolRequest): Promise<google.cloud.video.livestream.v1.Pool>;

Calls GetPool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.igetpoolrequest)`   
GetPoolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.video.livestream.v1.Pool](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.pool-class)>` | Promise  
  
### listAssets(request, callback)
    
    
    public listAssets(request: google.cloud.video.livestream.v1.IListAssetsRequest, callback: google.cloud.video.livestream.v1.LivestreamService.ListAssetsCallback): void;

Calls ListAssets.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAssetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ilistassetsrequest)`   
ListAssetsRequest message or plain object  
`callback` |  `[ListAssetsCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAssetsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAssets(request)
    
    
    public listAssets(request: google.cloud.video.livestream.v1.IListAssetsRequest): Promise<google.cloud.video.livestream.v1.ListAssetsResponse>;

Calls ListAssets.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAssetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ilistassetsrequest)`   
ListAssetsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.video.livestream.v1.ListAssetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.listassetsresponse)>` | Promise  
  
### listChannels(request, callback)
    
    
    public listChannels(request: google.cloud.video.livestream.v1.IListChannelsRequest, callback: google.cloud.video.livestream.v1.LivestreamService.ListChannelsCallback): void;

Calls ListChannels.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListChannelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ilistchannelsrequest)`   
ListChannelsRequest message or plain object  
`callback` |  `[ListChannelsCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and ListChannelsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listChannels(request)
    
    
    public listChannels(request: google.cloud.video.livestream.v1.IListChannelsRequest): Promise<google.cloud.video.livestream.v1.ListChannelsResponse>;

Calls ListChannels.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListChannelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ilistchannelsrequest)`   
ListChannelsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.video.livestream.v1.ListChannelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.listchannelsresponse)>` | Promise  
  
### listClips(request, callback)
    
    
    public listClips(request: google.cloud.video.livestream.v1.IListClipsRequest, callback: google.cloud.video.livestream.v1.LivestreamService.ListClipsCallback): void;

Calls ListClips.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClipsRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ilistclipsrequest)`   
ListClipsRequest message or plain object  
`callback` |  `[ListClipsCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and ListClipsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listClips(request)
    
    
    public listClips(request: google.cloud.video.livestream.v1.IListClipsRequest): Promise<google.cloud.video.livestream.v1.ListClipsResponse>;

Calls ListClips.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListClipsRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ilistclipsrequest)`   
ListClipsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.video.livestream.v1.ListClipsResponse](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.listclipsresponse)>` | Promise  
  
### listDvrSessions(request, callback)
    
    
    public listDvrSessions(request: google.cloud.video.livestream.v1.IListDvrSessionsRequest, callback: google.cloud.video.livestream.v1.LivestreamService.ListDvrSessionsCallback): void;

Calls ListDvrSessions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDvrSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ilistdvrsessionsrequest)`   
ListDvrSessionsRequest message or plain object  
`callback` |  `[ListDvrSessionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDvrSessionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDvrSessions(request)
    
    
    public listDvrSessions(request: google.cloud.video.livestream.v1.IListDvrSessionsRequest): Promise<google.cloud.video.livestream.v1.ListDvrSessionsResponse>;

Calls ListDvrSessions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDvrSessionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ilistdvrsessionsrequest)`   
ListDvrSessionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.video.livestream.v1.ListDvrSessionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.listdvrsessionsresponse)>` | Promise  
  
### listEvents(request, callback)
    
    
    public listEvents(request: google.cloud.video.livestream.v1.IListEventsRequest, callback: google.cloud.video.livestream.v1.LivestreamService.ListEventsCallback): void;

Calls ListEvents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ilisteventsrequest)`   
ListEventsRequest message or plain object  
`callback` |  `[ListEventsCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and ListEventsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvents(request)
    
    
    public listEvents(request: google.cloud.video.livestream.v1.IListEventsRequest): Promise<google.cloud.video.livestream.v1.ListEventsResponse>;

Calls ListEvents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ilisteventsrequest)`   
ListEventsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.video.livestream.v1.ListEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.listeventsresponse)>` | Promise  
  
### listInputs(request, callback)
    
    
    public listInputs(request: google.cloud.video.livestream.v1.IListInputsRequest, callback: google.cloud.video.livestream.v1.LivestreamService.ListInputsCallback): void;

Calls ListInputs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInputsRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ilistinputsrequest)`   
ListInputsRequest message or plain object  
`callback` |  `[ListInputsCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and ListInputsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listInputs(request)
    
    
    public listInputs(request: google.cloud.video.livestream.v1.IListInputsRequest): Promise<google.cloud.video.livestream.v1.ListInputsResponse>;

Calls ListInputs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListInputsRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ilistinputsrequest)`   
ListInputsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.video.livestream.v1.ListInputsResponse](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.listinputsresponse)>` | Promise  
  
### previewInput(request, callback)
    
    
    public previewInput(request: google.cloud.video.livestream.v1.IPreviewInputRequest, callback: google.cloud.video.livestream.v1.LivestreamService.PreviewInputCallback): void;

Calls PreviewInput.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPreviewInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ipreviewinputrequest)`   
PreviewInputRequest message or plain object  
`callback` |  `[PreviewInputCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and PreviewInputResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### previewInput(request)
    
    
    public previewInput(request: google.cloud.video.livestream.v1.IPreviewInputRequest): Promise<google.cloud.video.livestream.v1.PreviewInputResponse>;

Calls PreviewInput.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPreviewInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ipreviewinputrequest)`   
PreviewInputRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.video.livestream.v1.PreviewInputResponse](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.previewinputresponse)>` | Promise  
  
### startChannel(request, callback)
    
    
    public startChannel(request: google.cloud.video.livestream.v1.IStartChannelRequest, callback: google.cloud.video.livestream.v1.LivestreamService.StartChannelCallback): void;

Calls StartChannel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStartChannelRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.istartchannelrequest)`   
StartChannelRequest message or plain object  
`callback` |  `[StartChannelCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### startChannel(request)
    
    
    public startChannel(request: google.cloud.video.livestream.v1.IStartChannelRequest): Promise<google.longrunning.Operation>;

Calls StartChannel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IStartChannelRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.istartchannelrequest)`   
StartChannelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.longrunning.operation)>` | Promise  
  
### startDistribution(request, callback)
    
    
    public startDistribution(request: google.cloud.video.livestream.v1.IStartDistributionRequest, callback: google.cloud.video.livestream.v1.LivestreamService.StartDistributionCallback): void;

Calls StartDistribution.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStartDistributionRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.istartdistributionrequest)`   
StartDistributionRequest message or plain object  
`callback` |  `[StartDistributionCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### startDistribution(request)
    
    
    public startDistribution(request: google.cloud.video.livestream.v1.IStartDistributionRequest): Promise<google.longrunning.Operation>;

Calls StartDistribution.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IStartDistributionRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.istartdistributionrequest)`   
StartDistributionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.longrunning.operation)>` | Promise  
  
### stopChannel(request, callback)
    
    
    public stopChannel(request: google.cloud.video.livestream.v1.IStopChannelRequest, callback: google.cloud.video.livestream.v1.LivestreamService.StopChannelCallback): void;

Calls StopChannel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStopChannelRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.istopchannelrequest)`   
StopChannelRequest message or plain object  
`callback` |  `[StopChannelCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### stopChannel(request)
    
    
    public stopChannel(request: google.cloud.video.livestream.v1.IStopChannelRequest): Promise<google.longrunning.Operation>;

Calls StopChannel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IStopChannelRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.istopchannelrequest)`   
StopChannelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.longrunning.operation)>` | Promise  
  
### stopDistribution(request, callback)
    
    
    public stopDistribution(request: google.cloud.video.livestream.v1.IStopDistributionRequest, callback: google.cloud.video.livestream.v1.LivestreamService.StopDistributionCallback): void;

Calls StopDistribution.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStopDistributionRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.istopdistributionrequest)`   
StopDistributionRequest message or plain object  
`callback` |  `[StopDistributionCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### stopDistribution(request)
    
    
    public stopDistribution(request: google.cloud.video.livestream.v1.IStopDistributionRequest): Promise<google.longrunning.Operation>;

Calls StopDistribution.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IStopDistributionRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.istopdistributionrequest)`   
StopDistributionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.longrunning.operation)>` | Promise  
  
### updateChannel(request, callback)
    
    
    public updateChannel(request: google.cloud.video.livestream.v1.IUpdateChannelRequest, callback: google.cloud.video.livestream.v1.LivestreamService.UpdateChannelCallback): void;

Calls UpdateChannel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateChannelRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.iupdatechannelrequest)`   
UpdateChannelRequest message or plain object  
`callback` |  `[UpdateChannelCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateChannel(request)
    
    
    public updateChannel(request: google.cloud.video.livestream.v1.IUpdateChannelRequest): Promise<google.longrunning.Operation>;

Calls UpdateChannel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateChannelRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.iupdatechannelrequest)`   
UpdateChannelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.longrunning.operation)>` | Promise  
  
### updateDvrSession(request, callback)
    
    
    public updateDvrSession(request: google.cloud.video.livestream.v1.IUpdateDvrSessionRequest, callback: google.cloud.video.livestream.v1.LivestreamService.UpdateDvrSessionCallback): void;

Calls UpdateDvrSession.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDvrSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.iupdatedvrsessionrequest)`   
UpdateDvrSessionRequest message or plain object  
`callback` |  `[UpdateDvrSessionCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDvrSession(request)
    
    
    public updateDvrSession(request: google.cloud.video.livestream.v1.IUpdateDvrSessionRequest): Promise<google.longrunning.Operation>;

Calls UpdateDvrSession.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDvrSessionRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.iupdatedvrsessionrequest)`   
UpdateDvrSessionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.longrunning.operation)>` | Promise  
  
### updateInput(request, callback)
    
    
    public updateInput(request: google.cloud.video.livestream.v1.IUpdateInputRequest, callback: google.cloud.video.livestream.v1.LivestreamService.UpdateInputCallback): void;

Calls UpdateInput.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.iupdateinputrequest)`   
UpdateInputRequest message or plain object  
`callback` |  `[UpdateInputCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateInput(request)
    
    
    public updateInput(request: google.cloud.video.livestream.v1.IUpdateInputRequest): Promise<google.longrunning.Operation>;

Calls UpdateInput.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateInputRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.iupdateinputrequest)`   
UpdateInputRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.longrunning.operation)>` | Promise  
  
### updatePool(request, callback)
    
    
    public updatePool(request: google.cloud.video.livestream.v1.IUpdatePoolRequest, callback: google.cloud.video.livestream.v1.LivestreamService.UpdatePoolCallback): void;

Calls UpdatePool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.iupdatepoolrequest)`   
UpdatePoolRequest message or plain object  
`callback` |  `[UpdatePoolCallback](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updatePool(request)
    
    
    public updatePool(request: google.cloud.video.livestream.v1.IUpdatePoolRequest): Promise<google.longrunning.Operation>;

Calls UpdatePool.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.iupdatepoolrequest)`   
UpdatePoolRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
