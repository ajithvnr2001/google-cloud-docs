---
url: https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.eventarc-class
title: Class protos.google.cloud.eventarc.v1.Eventarc (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:59:49.542918+00:00
---

# Class protos.google.cloud.eventarc.v1.Eventarc (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.eventarc-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.eventarc.v1.Eventarc (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.3.0  4.1.0  4.0.1  3.2.0  2.3.2  2.2.0  2.1.1  1.2.0  1.1.2  1.0.3 

Represents an Eventarc

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.eventarc.v1.Eventarc

## Package

[@google-cloud/eventarc](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Eventarc service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Eventarc;

Creates new Eventarc service using the specified rpc implementation.

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
`[Eventarc](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.eventarc-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createChannel(request, callback)
    
    
    public createChannel(request: google.cloud.eventarc.v1.ICreateChannelRequest, callback: google.cloud.eventarc.v1.Eventarc.CreateChannelCallback): void;

Calls CreateChannel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateChannelRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.icreatechannelrequest)`   
CreateChannelRequest message or plain object  
`callback` |  `[CreateChannelCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createChannel(request)
    
    
    public createChannel(request: google.cloud.eventarc.v1.ICreateChannelRequest): Promise<google.longrunning.Operation>;

Calls CreateChannel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateChannelRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.icreatechannelrequest)`   
CreateChannelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.longrunning.operation)>` | Promise  
  
### createChannelConnection(request, callback)
    
    
    public createChannelConnection(request: google.cloud.eventarc.v1.ICreateChannelConnectionRequest, callback: google.cloud.eventarc.v1.Eventarc.CreateChannelConnectionCallback): void;

Calls CreateChannelConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateChannelConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.icreatechannelconnectionrequest)`   
CreateChannelConnectionRequest message or plain object  
`callback` |  `[CreateChannelConnectionCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createChannelConnection(request)
    
    
    public createChannelConnection(request: google.cloud.eventarc.v1.ICreateChannelConnectionRequest): Promise<google.longrunning.Operation>;

Calls CreateChannelConnection.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateChannelConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.icreatechannelconnectionrequest)`   
CreateChannelConnectionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.longrunning.operation)>` | Promise  
  
### createEnrollment(request, callback)
    
    
    public createEnrollment(request: google.cloud.eventarc.v1.ICreateEnrollmentRequest, callback: google.cloud.eventarc.v1.Eventarc.CreateEnrollmentCallback): void;

Calls CreateEnrollment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEnrollmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.icreateenrollmentrequest)`   
CreateEnrollmentRequest message or plain object  
`callback` |  `[CreateEnrollmentCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEnrollment(request)
    
    
    public createEnrollment(request: google.cloud.eventarc.v1.ICreateEnrollmentRequest): Promise<google.longrunning.Operation>;

Calls CreateEnrollment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateEnrollmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.icreateenrollmentrequest)`   
CreateEnrollmentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.longrunning.operation)>` | Promise  
  
### createGoogleApiSource(request, callback)
    
    
    public createGoogleApiSource(request: google.cloud.eventarc.v1.ICreateGoogleApiSourceRequest, callback: google.cloud.eventarc.v1.Eventarc.CreateGoogleApiSourceCallback): void;

Calls CreateGoogleApiSource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateGoogleApiSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.icreategoogleapisourcerequest)`   
CreateGoogleApiSourceRequest message or plain object  
`callback` |  `[CreateGoogleApiSourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createGoogleApiSource(request)
    
    
    public createGoogleApiSource(request: google.cloud.eventarc.v1.ICreateGoogleApiSourceRequest): Promise<google.longrunning.Operation>;

Calls CreateGoogleApiSource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateGoogleApiSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.icreategoogleapisourcerequest)`   
CreateGoogleApiSourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.longrunning.operation)>` | Promise  
  
### createMessageBus(request, callback)
    
    
    public createMessageBus(request: google.cloud.eventarc.v1.ICreateMessageBusRequest, callback: google.cloud.eventarc.v1.Eventarc.CreateMessageBusCallback): void;

Calls CreateMessageBus.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMessageBusRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.icreatemessagebusrequest)`   
CreateMessageBusRequest message or plain object  
`callback` |  `[CreateMessageBusCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMessageBus(request)
    
    
    public createMessageBus(request: google.cloud.eventarc.v1.ICreateMessageBusRequest): Promise<google.longrunning.Operation>;

Calls CreateMessageBus.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateMessageBusRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.icreatemessagebusrequest)`   
CreateMessageBusRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.longrunning.operation)>` | Promise  
  
### createPipeline(request, callback)
    
    
    public createPipeline(request: google.cloud.eventarc.v1.ICreatePipelineRequest, callback: google.cloud.eventarc.v1.Eventarc.CreatePipelineCallback): void;

Calls CreatePipeline.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePipelineRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.icreatepipelinerequest)`   
CreatePipelineRequest message or plain object  
`callback` |  `[CreatePipelineCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPipeline(request)
    
    
    public createPipeline(request: google.cloud.eventarc.v1.ICreatePipelineRequest): Promise<google.longrunning.Operation>;

Calls CreatePipeline.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreatePipelineRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.icreatepipelinerequest)`   
CreatePipelineRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.longrunning.operation)>` | Promise  
  
### createTrigger(request, callback)
    
    
    public createTrigger(request: google.cloud.eventarc.v1.ICreateTriggerRequest, callback: google.cloud.eventarc.v1.Eventarc.CreateTriggerCallback): void;

Calls CreateTrigger.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTriggerRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.icreatetriggerrequest)`   
CreateTriggerRequest message or plain object  
`callback` |  `[CreateTriggerCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTrigger(request)
    
    
    public createTrigger(request: google.cloud.eventarc.v1.ICreateTriggerRequest): Promise<google.longrunning.Operation>;

Calls CreateTrigger.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateTriggerRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.icreatetriggerrequest)`   
CreateTriggerRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.longrunning.operation)>` | Promise  
  
### deleteChannel(request, callback)
    
    
    public deleteChannel(request: google.cloud.eventarc.v1.IDeleteChannelRequest, callback: google.cloud.eventarc.v1.Eventarc.DeleteChannelCallback): void;

Calls DeleteChannel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteChannelRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ideletechannelrequest)`   
DeleteChannelRequest message or plain object  
`callback` |  `[DeleteChannelCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteChannel(request)
    
    
    public deleteChannel(request: google.cloud.eventarc.v1.IDeleteChannelRequest): Promise<google.longrunning.Operation>;

Calls DeleteChannel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteChannelRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ideletechannelrequest)`   
DeleteChannelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.longrunning.operation)>` | Promise  
  
### deleteChannelConnection(request, callback)
    
    
    public deleteChannelConnection(request: google.cloud.eventarc.v1.IDeleteChannelConnectionRequest, callback: google.cloud.eventarc.v1.Eventarc.DeleteChannelConnectionCallback): void;

Calls DeleteChannelConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteChannelConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ideletechannelconnectionrequest)`   
DeleteChannelConnectionRequest message or plain object  
`callback` |  `[DeleteChannelConnectionCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteChannelConnection(request)
    
    
    public deleteChannelConnection(request: google.cloud.eventarc.v1.IDeleteChannelConnectionRequest): Promise<google.longrunning.Operation>;

Calls DeleteChannelConnection.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteChannelConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ideletechannelconnectionrequest)`   
DeleteChannelConnectionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.longrunning.operation)>` | Promise  
  
### deleteEnrollment(request, callback)
    
    
    public deleteEnrollment(request: google.cloud.eventarc.v1.IDeleteEnrollmentRequest, callback: google.cloud.eventarc.v1.Eventarc.DeleteEnrollmentCallback): void;

Calls DeleteEnrollment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEnrollmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ideleteenrollmentrequest)`   
DeleteEnrollmentRequest message or plain object  
`callback` |  `[DeleteEnrollmentCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEnrollment(request)
    
    
    public deleteEnrollment(request: google.cloud.eventarc.v1.IDeleteEnrollmentRequest): Promise<google.longrunning.Operation>;

Calls DeleteEnrollment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEnrollmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ideleteenrollmentrequest)`   
DeleteEnrollmentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.longrunning.operation)>` | Promise  
  
### deleteGoogleApiSource(request, callback)
    
    
    public deleteGoogleApiSource(request: google.cloud.eventarc.v1.IDeleteGoogleApiSourceRequest, callback: google.cloud.eventarc.v1.Eventarc.DeleteGoogleApiSourceCallback): void;

Calls DeleteGoogleApiSource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGoogleApiSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ideletegoogleapisourcerequest)`   
DeleteGoogleApiSourceRequest message or plain object  
`callback` |  `[DeleteGoogleApiSourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteGoogleApiSource(request)
    
    
    public deleteGoogleApiSource(request: google.cloud.eventarc.v1.IDeleteGoogleApiSourceRequest): Promise<google.longrunning.Operation>;

Calls DeleteGoogleApiSource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGoogleApiSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ideletegoogleapisourcerequest)`   
DeleteGoogleApiSourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.longrunning.operation)>` | Promise  
  
### deleteMessageBus(request, callback)
    
    
    public deleteMessageBus(request: google.cloud.eventarc.v1.IDeleteMessageBusRequest, callback: google.cloud.eventarc.v1.Eventarc.DeleteMessageBusCallback): void;

Calls DeleteMessageBus.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMessageBusRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ideletemessagebusrequest)`   
DeleteMessageBusRequest message or plain object  
`callback` |  `[DeleteMessageBusCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMessageBus(request)
    
    
    public deleteMessageBus(request: google.cloud.eventarc.v1.IDeleteMessageBusRequest): Promise<google.longrunning.Operation>;

Calls DeleteMessageBus.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMessageBusRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ideletemessagebusrequest)`   
DeleteMessageBusRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.longrunning.operation)>` | Promise  
  
### deletePipeline(request, callback)
    
    
    public deletePipeline(request: google.cloud.eventarc.v1.IDeletePipelineRequest, callback: google.cloud.eventarc.v1.Eventarc.DeletePipelineCallback): void;

Calls DeletePipeline.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePipelineRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ideletepipelinerequest)`   
DeletePipelineRequest message or plain object  
`callback` |  `[DeletePipelineCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePipeline(request)
    
    
    public deletePipeline(request: google.cloud.eventarc.v1.IDeletePipelineRequest): Promise<google.longrunning.Operation>;

Calls DeletePipeline.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeletePipelineRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ideletepipelinerequest)`   
DeletePipelineRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.longrunning.operation)>` | Promise  
  
### deleteTrigger(request, callback)
    
    
    public deleteTrigger(request: google.cloud.eventarc.v1.IDeleteTriggerRequest, callback: google.cloud.eventarc.v1.Eventarc.DeleteTriggerCallback): void;

Calls DeleteTrigger.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTriggerRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ideletetriggerrequest)`   
DeleteTriggerRequest message or plain object  
`callback` |  `[DeleteTriggerCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTrigger(request)
    
    
    public deleteTrigger(request: google.cloud.eventarc.v1.IDeleteTriggerRequest): Promise<google.longrunning.Operation>;

Calls DeleteTrigger.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTriggerRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ideletetriggerrequest)`   
DeleteTriggerRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.longrunning.operation)>` | Promise  
  
### getChannel(request, callback)
    
    
    public getChannel(request: google.cloud.eventarc.v1.IGetChannelRequest, callback: google.cloud.eventarc.v1.Eventarc.GetChannelCallback): void;

Calls GetChannel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetChannelRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetchannelrequest)`   
GetChannelRequest message or plain object  
`callback` |  `[GetChannelCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Channel  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getChannel(request)
    
    
    public getChannel(request: google.cloud.eventarc.v1.IGetChannelRequest): Promise<google.cloud.eventarc.v1.Channel>;

Calls GetChannel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetChannelRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetchannelrequest)`   
GetChannelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.eventarc.v1.Channel](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.channel-class)>` | Promise  
  
### getChannelConnection(request, callback)
    
    
    public getChannelConnection(request: google.cloud.eventarc.v1.IGetChannelConnectionRequest, callback: google.cloud.eventarc.v1.Eventarc.GetChannelConnectionCallback): void;

Calls GetChannelConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetChannelConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetchannelconnectionrequest)`   
GetChannelConnectionRequest message or plain object  
`callback` |  `[GetChannelConnectionCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and ChannelConnection  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getChannelConnection(request)
    
    
    public getChannelConnection(request: google.cloud.eventarc.v1.IGetChannelConnectionRequest): Promise<google.cloud.eventarc.v1.ChannelConnection>;

Calls GetChannelConnection.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetChannelConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetchannelconnectionrequest)`   
GetChannelConnectionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.eventarc.v1.ChannelConnection](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.channelconnection)>` | Promise  
  
### getEnrollment(request, callback)
    
    
    public getEnrollment(request: google.cloud.eventarc.v1.IGetEnrollmentRequest, callback: google.cloud.eventarc.v1.Eventarc.GetEnrollmentCallback): void;

Calls GetEnrollment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEnrollmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetenrollmentrequest)`   
GetEnrollmentRequest message or plain object  
`callback` |  `[GetEnrollmentCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Enrollment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEnrollment(request)
    
    
    public getEnrollment(request: google.cloud.eventarc.v1.IGetEnrollmentRequest): Promise<google.cloud.eventarc.v1.Enrollment>;

Calls GetEnrollment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEnrollmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetenrollmentrequest)`   
GetEnrollmentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.eventarc.v1.Enrollment](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.enrollment)>` | Promise  
  
### getGoogleApiSource(request, callback)
    
    
    public getGoogleApiSource(request: google.cloud.eventarc.v1.IGetGoogleApiSourceRequest, callback: google.cloud.eventarc.v1.Eventarc.GetGoogleApiSourceCallback): void;

Calls GetGoogleApiSource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetGoogleApiSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetgoogleapisourcerequest)`   
GetGoogleApiSourceRequest message or plain object  
`callback` |  `[GetGoogleApiSourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and GoogleApiSource  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getGoogleApiSource(request)
    
    
    public getGoogleApiSource(request: google.cloud.eventarc.v1.IGetGoogleApiSourceRequest): Promise<google.cloud.eventarc.v1.GoogleApiSource>;

Calls GetGoogleApiSource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetGoogleApiSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetgoogleapisourcerequest)`   
GetGoogleApiSourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.eventarc.v1.GoogleApiSource](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.googleapisource-class)>` | Promise  
  
### getGoogleChannelConfig(request, callback)
    
    
    public getGoogleChannelConfig(request: google.cloud.eventarc.v1.IGetGoogleChannelConfigRequest, callback: google.cloud.eventarc.v1.Eventarc.GetGoogleChannelConfigCallback): void;

Calls GetGoogleChannelConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetGoogleChannelConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetgooglechannelconfigrequest)`   
GetGoogleChannelConfigRequest message or plain object  
`callback` |  `[GetGoogleChannelConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and GoogleChannelConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getGoogleChannelConfig(request)
    
    
    public getGoogleChannelConfig(request: google.cloud.eventarc.v1.IGetGoogleChannelConfigRequest): Promise<google.cloud.eventarc.v1.GoogleChannelConfig>;

Calls GetGoogleChannelConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetGoogleChannelConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetgooglechannelconfigrequest)`   
GetGoogleChannelConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.eventarc.v1.GoogleChannelConfig](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.googlechannelconfig)>` | Promise  
  
### getMessageBus(request, callback)
    
    
    public getMessageBus(request: google.cloud.eventarc.v1.IGetMessageBusRequest, callback: google.cloud.eventarc.v1.Eventarc.GetMessageBusCallback): void;

Calls GetMessageBus.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMessageBusRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetmessagebusrequest)`   
GetMessageBusRequest message or plain object  
`callback` |  `[GetMessageBusCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and MessageBus  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMessageBus(request)
    
    
    public getMessageBus(request: google.cloud.eventarc.v1.IGetMessageBusRequest): Promise<google.cloud.eventarc.v1.MessageBus>;

Calls GetMessageBus.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetMessageBusRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetmessagebusrequest)`   
GetMessageBusRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.eventarc.v1.MessageBus](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.messagebus)>` | Promise  
  
### getPipeline(request, callback)
    
    
    public getPipeline(request: google.cloud.eventarc.v1.IGetPipelineRequest, callback: google.cloud.eventarc.v1.Eventarc.GetPipelineCallback): void;

Calls GetPipeline.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPipelineRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetpipelinerequest)`   
GetPipelineRequest message or plain object  
`callback` |  `[GetPipelineCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Pipeline  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPipeline(request)
    
    
    public getPipeline(request: google.cloud.eventarc.v1.IGetPipelineRequest): Promise<google.cloud.eventarc.v1.Pipeline>;

Calls GetPipeline.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPipelineRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetpipelinerequest)`   
GetPipelineRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.eventarc.v1.Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.pipeline-class)>` | Promise  
  
### getProvider(request, callback)
    
    
    public getProvider(request: google.cloud.eventarc.v1.IGetProviderRequest, callback: google.cloud.eventarc.v1.Eventarc.GetProviderCallback): void;

Calls GetProvider.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetproviderrequest)`   
GetProviderRequest message or plain object  
`callback` |  `[GetProviderCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Provider  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProvider(request)
    
    
    public getProvider(request: google.cloud.eventarc.v1.IGetProviderRequest): Promise<google.cloud.eventarc.v1.Provider>;

Calls GetProvider.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetProviderRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetproviderrequest)`   
GetProviderRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.eventarc.v1.Provider](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.provider)>` | Promise  
  
### getTrigger(request, callback)
    
    
    public getTrigger(request: google.cloud.eventarc.v1.IGetTriggerRequest, callback: google.cloud.eventarc.v1.Eventarc.GetTriggerCallback): void;

Calls GetTrigger.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTriggerRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igettriggerrequest)`   
GetTriggerRequest message or plain object  
`callback` |  `[GetTriggerCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Trigger  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTrigger(request)
    
    
    public getTrigger(request: google.cloud.eventarc.v1.IGetTriggerRequest): Promise<google.cloud.eventarc.v1.Trigger>;

Calls GetTrigger.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetTriggerRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igettriggerrequest)`   
GetTriggerRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.eventarc.v1.Trigger](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.trigger-class)>` | Promise  
  
### listChannelConnections(request, callback)
    
    
    public listChannelConnections(request: google.cloud.eventarc.v1.IListChannelConnectionsRequest, callback: google.cloud.eventarc.v1.Eventarc.ListChannelConnectionsCallback): void;

Calls ListChannelConnections.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListChannelConnectionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistchannelconnectionsrequest)`   
ListChannelConnectionsRequest message or plain object  
`callback` |  `[ListChannelConnectionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and ListChannelConnectionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listChannelConnections(request)
    
    
    public listChannelConnections(request: google.cloud.eventarc.v1.IListChannelConnectionsRequest): Promise<google.cloud.eventarc.v1.ListChannelConnectionsResponse>;

Calls ListChannelConnections.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListChannelConnectionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistchannelconnectionsrequest)`   
ListChannelConnectionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.eventarc.v1.ListChannelConnectionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.listchannelconnectionsresponse)>` | Promise  
  
### listChannels(request, callback)
    
    
    public listChannels(request: google.cloud.eventarc.v1.IListChannelsRequest, callback: google.cloud.eventarc.v1.Eventarc.ListChannelsCallback): void;

Calls ListChannels.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListChannelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistchannelsrequest)`   
ListChannelsRequest message or plain object  
`callback` |  `[ListChannelsCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and ListChannelsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listChannels(request)
    
    
    public listChannels(request: google.cloud.eventarc.v1.IListChannelsRequest): Promise<google.cloud.eventarc.v1.ListChannelsResponse>;

Calls ListChannels.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListChannelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistchannelsrequest)`   
ListChannelsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.eventarc.v1.ListChannelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.listchannelsresponse)>` | Promise  
  
### listEnrollments(request, callback)
    
    
    public listEnrollments(request: google.cloud.eventarc.v1.IListEnrollmentsRequest, callback: google.cloud.eventarc.v1.Eventarc.ListEnrollmentsCallback): void;

Calls ListEnrollments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEnrollmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistenrollmentsrequest)`   
ListEnrollmentsRequest message or plain object  
`callback` |  `[ListEnrollmentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and ListEnrollmentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEnrollments(request)
    
    
    public listEnrollments(request: google.cloud.eventarc.v1.IListEnrollmentsRequest): Promise<google.cloud.eventarc.v1.ListEnrollmentsResponse>;

Calls ListEnrollments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListEnrollmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistenrollmentsrequest)`   
ListEnrollmentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.eventarc.v1.ListEnrollmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.listenrollmentsresponse)>` | Promise  
  
### listGoogleApiSources(request, callback)
    
    
    public listGoogleApiSources(request: google.cloud.eventarc.v1.IListGoogleApiSourcesRequest, callback: google.cloud.eventarc.v1.Eventarc.ListGoogleApiSourcesCallback): void;

Calls ListGoogleApiSources.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGoogleApiSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistgoogleapisourcesrequest)`   
ListGoogleApiSourcesRequest message or plain object  
`callback` |  `[ListGoogleApiSourcesCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and ListGoogleApiSourcesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listGoogleApiSources(request)
    
    
    public listGoogleApiSources(request: google.cloud.eventarc.v1.IListGoogleApiSourcesRequest): Promise<google.cloud.eventarc.v1.ListGoogleApiSourcesResponse>;

Calls ListGoogleApiSources.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListGoogleApiSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistgoogleapisourcesrequest)`   
ListGoogleApiSourcesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.eventarc.v1.ListGoogleApiSourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.listgoogleapisourcesresponse)>` | Promise  
  
### listMessageBusEnrollments(request, callback)
    
    
    public listMessageBusEnrollments(request: google.cloud.eventarc.v1.IListMessageBusEnrollmentsRequest, callback: google.cloud.eventarc.v1.Eventarc.ListMessageBusEnrollmentsCallback): void;

Calls ListMessageBusEnrollments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMessageBusEnrollmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistmessagebusenrollmentsrequest)`   
ListMessageBusEnrollmentsRequest message or plain object  
`callback` |  `[ListMessageBusEnrollmentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMessageBusEnrollmentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMessageBusEnrollments(request)
    
    
    public listMessageBusEnrollments(request: google.cloud.eventarc.v1.IListMessageBusEnrollmentsRequest): Promise<google.cloud.eventarc.v1.ListMessageBusEnrollmentsResponse>;

Calls ListMessageBusEnrollments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMessageBusEnrollmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistmessagebusenrollmentsrequest)`   
ListMessageBusEnrollmentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.eventarc.v1.ListMessageBusEnrollmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.listmessagebusenrollmentsresponse)>` | Promise  
  
### listMessageBuses(request, callback)
    
    
    public listMessageBuses(request: google.cloud.eventarc.v1.IListMessageBusesRequest, callback: google.cloud.eventarc.v1.Eventarc.ListMessageBusesCallback): void;

Calls ListMessageBuses.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMessageBusesRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistmessagebusesrequest)`   
ListMessageBusesRequest message or plain object  
`callback` |  `[ListMessageBusesCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMessageBusesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMessageBuses(request)
    
    
    public listMessageBuses(request: google.cloud.eventarc.v1.IListMessageBusesRequest): Promise<google.cloud.eventarc.v1.ListMessageBusesResponse>;

Calls ListMessageBuses.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMessageBusesRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistmessagebusesrequest)`   
ListMessageBusesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.eventarc.v1.ListMessageBusesResponse](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.listmessagebusesresponse)>` | Promise  
  
### listPipelines(request, callback)
    
    
    public listPipelines(request: google.cloud.eventarc.v1.IListPipelinesRequest, callback: google.cloud.eventarc.v1.Eventarc.ListPipelinesCallback): void;

Calls ListPipelines.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPipelinesRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistpipelinesrequest)`   
ListPipelinesRequest message or plain object  
`callback` |  `[ListPipelinesCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPipelinesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPipelines(request)
    
    
    public listPipelines(request: google.cloud.eventarc.v1.IListPipelinesRequest): Promise<google.cloud.eventarc.v1.ListPipelinesResponse>;

Calls ListPipelines.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPipelinesRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistpipelinesrequest)`   
ListPipelinesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.eventarc.v1.ListPipelinesResponse](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.listpipelinesresponse)>` | Promise  
  
### listProviders(request, callback)
    
    
    public listProviders(request: google.cloud.eventarc.v1.IListProvidersRequest, callback: google.cloud.eventarc.v1.Eventarc.ListProvidersCallback): void;

Calls ListProviders.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProvidersRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistprovidersrequest)`   
ListProvidersRequest message or plain object  
`callback` |  `[ListProvidersCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and ListProvidersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProviders(request)
    
    
    public listProviders(request: google.cloud.eventarc.v1.IListProvidersRequest): Promise<google.cloud.eventarc.v1.ListProvidersResponse>;

Calls ListProviders.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListProvidersRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistprovidersrequest)`   
ListProvidersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.eventarc.v1.ListProvidersResponse](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.listprovidersresponse)>` | Promise  
  
### listTriggers(request, callback)
    
    
    public listTriggers(request: google.cloud.eventarc.v1.IListTriggersRequest, callback: google.cloud.eventarc.v1.Eventarc.ListTriggersCallback): void;

Calls ListTriggers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTriggersRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilisttriggersrequest)`   
ListTriggersRequest message or plain object  
`callback` |  `[ListTriggersCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and ListTriggersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTriggers(request)
    
    
    public listTriggers(request: google.cloud.eventarc.v1.IListTriggersRequest): Promise<google.cloud.eventarc.v1.ListTriggersResponse>;

Calls ListTriggers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListTriggersRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilisttriggersrequest)`   
ListTriggersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.eventarc.v1.ListTriggersResponse](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.listtriggersresponse)>` | Promise  
  
### updateChannel(request, callback)
    
    
    public updateChannel(request: google.cloud.eventarc.v1.IUpdateChannelRequest, callback: google.cloud.eventarc.v1.Eventarc.UpdateChannelCallback): void;

Calls UpdateChannel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateChannelRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.iupdatechannelrequest)`   
UpdateChannelRequest message or plain object  
`callback` |  `[UpdateChannelCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateChannel(request)
    
    
    public updateChannel(request: google.cloud.eventarc.v1.IUpdateChannelRequest): Promise<google.longrunning.Operation>;

Calls UpdateChannel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateChannelRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.iupdatechannelrequest)`   
UpdateChannelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.longrunning.operation)>` | Promise  
  
### updateEnrollment(request, callback)
    
    
    public updateEnrollment(request: google.cloud.eventarc.v1.IUpdateEnrollmentRequest, callback: google.cloud.eventarc.v1.Eventarc.UpdateEnrollmentCallback): void;

Calls UpdateEnrollment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEnrollmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.iupdateenrollmentrequest)`   
UpdateEnrollmentRequest message or plain object  
`callback` |  `[UpdateEnrollmentCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEnrollment(request)
    
    
    public updateEnrollment(request: google.cloud.eventarc.v1.IUpdateEnrollmentRequest): Promise<google.longrunning.Operation>;

Calls UpdateEnrollment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEnrollmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.iupdateenrollmentrequest)`   
UpdateEnrollmentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.longrunning.operation)>` | Promise  
  
### updateGoogleApiSource(request, callback)
    
    
    public updateGoogleApiSource(request: google.cloud.eventarc.v1.IUpdateGoogleApiSourceRequest, callback: google.cloud.eventarc.v1.Eventarc.UpdateGoogleApiSourceCallback): void;

Calls UpdateGoogleApiSource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGoogleApiSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.iupdategoogleapisourcerequest)`   
UpdateGoogleApiSourceRequest message or plain object  
`callback` |  `[UpdateGoogleApiSourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateGoogleApiSource(request)
    
    
    public updateGoogleApiSource(request: google.cloud.eventarc.v1.IUpdateGoogleApiSourceRequest): Promise<google.longrunning.Operation>;

Calls UpdateGoogleApiSource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGoogleApiSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.iupdategoogleapisourcerequest)`   
UpdateGoogleApiSourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.longrunning.operation)>` | Promise  
  
### updateGoogleChannelConfig(request, callback)
    
    
    public updateGoogleChannelConfig(request: google.cloud.eventarc.v1.IUpdateGoogleChannelConfigRequest, callback: google.cloud.eventarc.v1.Eventarc.UpdateGoogleChannelConfigCallback): void;

Calls UpdateGoogleChannelConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGoogleChannelConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.iupdategooglechannelconfigrequest)`   
UpdateGoogleChannelConfigRequest message or plain object  
`callback` |  `[UpdateGoogleChannelConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and GoogleChannelConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateGoogleChannelConfig(request)
    
    
    public updateGoogleChannelConfig(request: google.cloud.eventarc.v1.IUpdateGoogleChannelConfigRequest): Promise<google.cloud.eventarc.v1.GoogleChannelConfig>;

Calls UpdateGoogleChannelConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGoogleChannelConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.iupdategooglechannelconfigrequest)`   
UpdateGoogleChannelConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.eventarc.v1.GoogleChannelConfig](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.googlechannelconfig)>` | Promise  
  
### updateMessageBus(request, callback)
    
    
    public updateMessageBus(request: google.cloud.eventarc.v1.IUpdateMessageBusRequest, callback: google.cloud.eventarc.v1.Eventarc.UpdateMessageBusCallback): void;

Calls UpdateMessageBus.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMessageBusRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.iupdatemessagebusrequest)`   
UpdateMessageBusRequest message or plain object  
`callback` |  `[UpdateMessageBusCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMessageBus(request)
    
    
    public updateMessageBus(request: google.cloud.eventarc.v1.IUpdateMessageBusRequest): Promise<google.longrunning.Operation>;

Calls UpdateMessageBus.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMessageBusRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.iupdatemessagebusrequest)`   
UpdateMessageBusRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.longrunning.operation)>` | Promise  
  
### updatePipeline(request, callback)
    
    
    public updatePipeline(request: google.cloud.eventarc.v1.IUpdatePipelineRequest, callback: google.cloud.eventarc.v1.Eventarc.UpdatePipelineCallback): void;

Calls UpdatePipeline.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePipelineRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.iupdatepipelinerequest)`   
UpdatePipelineRequest message or plain object  
`callback` |  `[UpdatePipelineCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updatePipeline(request)
    
    
    public updatePipeline(request: google.cloud.eventarc.v1.IUpdatePipelineRequest): Promise<google.longrunning.Operation>;

Calls UpdatePipeline.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePipelineRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.iupdatepipelinerequest)`   
UpdatePipelineRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.longrunning.operation)>` | Promise  
  
### updateTrigger(request, callback)
    
    
    public updateTrigger(request: google.cloud.eventarc.v1.IUpdateTriggerRequest, callback: google.cloud.eventarc.v1.Eventarc.UpdateTriggerCallback): void;

Calls UpdateTrigger.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTriggerRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.iupdatetriggerrequest)`   
UpdateTriggerRequest message or plain object  
`callback` |  `[UpdateTriggerCallback](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTrigger(request)
    
    
    public updateTrigger(request: google.cloud.eventarc.v1.IUpdateTriggerRequest): Promise<google.longrunning.Operation>;

Calls UpdateTrigger.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTriggerRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.iupdatetriggerrequest)`   
UpdateTriggerRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
