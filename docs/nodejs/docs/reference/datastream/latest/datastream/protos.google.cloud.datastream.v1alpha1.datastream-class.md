---
url: https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.datastream-class
title: Class protos.google.cloud.datastream.v1alpha1.Datastream (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:18.039544+00:00
---

# Class protos.google.cloud.datastream.v1alpha1.Datastream (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.datastream-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.datastream.v1alpha1.Datastream (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.0.1  3.4.0  3.3.0  3.1.0  2.2.2  2.1.2  1.1.0  1.0.0  0.2.0 

Represents a Datastream

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.datastream.v1alpha1.Datastream

## Package

[@google-cloud/datastream](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Datastream service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Datastream;

Creates new Datastream service using the specified rpc implementation.

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
`[Datastream](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.datastream-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createConnectionProfile(request, callback)
    
    
    public createConnectionProfile(request: google.cloud.datastream.v1alpha1.ICreateConnectionProfileRequest, callback: google.cloud.datastream.v1alpha1.Datastream.CreateConnectionProfileCallback): void;

Calls CreateConnectionProfile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConnectionProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.icreateconnectionprofilerequest)`   
CreateConnectionProfileRequest message or plain object  
`callback` |  `[CreateConnectionProfileCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConnectionProfile(request)
    
    
    public createConnectionProfile(request: google.cloud.datastream.v1alpha1.ICreateConnectionProfileRequest): Promise<google.longrunning.Operation>;

Calls CreateConnectionProfile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateConnectionProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.icreateconnectionprofilerequest)`   
CreateConnectionProfileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.longrunning.operation)>` | Promise  
  
### createPrivateConnection(request, callback)
    
    
    public createPrivateConnection(request: google.cloud.datastream.v1alpha1.ICreatePrivateConnectionRequest, callback: google.cloud.datastream.v1alpha1.Datastream.CreatePrivateConnectionCallback): void;

Calls CreatePrivateConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePrivateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.icreateprivateconnectionrequest)`   
CreatePrivateConnectionRequest message or plain object  
`callback` |  `[CreatePrivateConnectionCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPrivateConnection(request)
    
    
    public createPrivateConnection(request: google.cloud.datastream.v1alpha1.ICreatePrivateConnectionRequest): Promise<google.longrunning.Operation>;

Calls CreatePrivateConnection.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreatePrivateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.icreateprivateconnectionrequest)`   
CreatePrivateConnectionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.longrunning.operation)>` | Promise  
  
### createRoute(request, callback)
    
    
    public createRoute(request: google.cloud.datastream.v1alpha1.ICreateRouteRequest, callback: google.cloud.datastream.v1alpha1.Datastream.CreateRouteCallback): void;

Calls CreateRoute.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRouteRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.icreaterouterequest)`   
CreateRouteRequest message or plain object  
`callback` |  `[CreateRouteCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createRoute(request)
    
    
    public createRoute(request: google.cloud.datastream.v1alpha1.ICreateRouteRequest): Promise<google.longrunning.Operation>;

Calls CreateRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateRouteRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.icreaterouterequest)`   
CreateRouteRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.longrunning.operation)>` | Promise  
  
### createStream(request, callback)
    
    
    public createStream(request: google.cloud.datastream.v1alpha1.ICreateStreamRequest, callback: google.cloud.datastream.v1alpha1.Datastream.CreateStreamCallback): void;

Calls CreateStream.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.icreatestreamrequest)`   
CreateStreamRequest message or plain object  
`callback` |  `[CreateStreamCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createStream(request)
    
    
    public createStream(request: google.cloud.datastream.v1alpha1.ICreateStreamRequest): Promise<google.longrunning.Operation>;

Calls CreateStream.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.icreatestreamrequest)`   
CreateStreamRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.longrunning.operation)>` | Promise  
  
### deleteConnectionProfile(request, callback)
    
    
    public deleteConnectionProfile(request: google.cloud.datastream.v1alpha1.IDeleteConnectionProfileRequest, callback: google.cloud.datastream.v1alpha1.Datastream.DeleteConnectionProfileCallback): void;

Calls DeleteConnectionProfile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConnectionProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ideleteconnectionprofilerequest)`   
DeleteConnectionProfileRequest message or plain object  
`callback` |  `[DeleteConnectionProfileCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConnectionProfile(request)
    
    
    public deleteConnectionProfile(request: google.cloud.datastream.v1alpha1.IDeleteConnectionProfileRequest): Promise<google.longrunning.Operation>;

Calls DeleteConnectionProfile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConnectionProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ideleteconnectionprofilerequest)`   
DeleteConnectionProfileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.longrunning.operation)>` | Promise  
  
### deletePrivateConnection(request, callback)
    
    
    public deletePrivateConnection(request: google.cloud.datastream.v1alpha1.IDeletePrivateConnectionRequest, callback: google.cloud.datastream.v1alpha1.Datastream.DeletePrivateConnectionCallback): void;

Calls DeletePrivateConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePrivateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ideleteprivateconnectionrequest)`   
DeletePrivateConnectionRequest message or plain object  
`callback` |  `[DeletePrivateConnectionCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePrivateConnection(request)
    
    
    public deletePrivateConnection(request: google.cloud.datastream.v1alpha1.IDeletePrivateConnectionRequest): Promise<google.longrunning.Operation>;

Calls DeletePrivateConnection.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeletePrivateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ideleteprivateconnectionrequest)`   
DeletePrivateConnectionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.longrunning.operation)>` | Promise  
  
### deleteRoute(request, callback)
    
    
    public deleteRoute(request: google.cloud.datastream.v1alpha1.IDeleteRouteRequest, callback: google.cloud.datastream.v1alpha1.Datastream.DeleteRouteCallback): void;

Calls DeleteRoute.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRouteRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ideleterouterequest)`   
DeleteRouteRequest message or plain object  
`callback` |  `[DeleteRouteCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteRoute(request)
    
    
    public deleteRoute(request: google.cloud.datastream.v1alpha1.IDeleteRouteRequest): Promise<google.longrunning.Operation>;

Calls DeleteRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRouteRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ideleterouterequest)`   
DeleteRouteRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.longrunning.operation)>` | Promise  
  
### deleteStream(request, callback)
    
    
    public deleteStream(request: google.cloud.datastream.v1alpha1.IDeleteStreamRequest, callback: google.cloud.datastream.v1alpha1.Datastream.DeleteStreamCallback): void;

Calls DeleteStream.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ideletestreamrequest)`   
DeleteStreamRequest message or plain object  
`callback` |  `[DeleteStreamCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteStream(request)
    
    
    public deleteStream(request: google.cloud.datastream.v1alpha1.IDeleteStreamRequest): Promise<google.longrunning.Operation>;

Calls DeleteStream.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ideletestreamrequest)`   
DeleteStreamRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.longrunning.operation)>` | Promise  
  
### discoverConnectionProfile(request, callback)
    
    
    public discoverConnectionProfile(request: google.cloud.datastream.v1alpha1.IDiscoverConnectionProfileRequest, callback: google.cloud.datastream.v1alpha1.Datastream.DiscoverConnectionProfileCallback): void;

Calls DiscoverConnectionProfile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDiscoverConnectionProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.idiscoverconnectionprofilerequest)`   
DiscoverConnectionProfileRequest message or plain object  
`callback` |  `[DiscoverConnectionProfileCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and DiscoverConnectionProfileResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### discoverConnectionProfile(request)
    
    
    public discoverConnectionProfile(request: google.cloud.datastream.v1alpha1.IDiscoverConnectionProfileRequest): Promise<google.cloud.datastream.v1alpha1.DiscoverConnectionProfileResponse>;

Calls DiscoverConnectionProfile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDiscoverConnectionProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.idiscoverconnectionprofilerequest)`   
DiscoverConnectionProfileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datastream.v1alpha1.DiscoverConnectionProfileResponse](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.discoverconnectionprofileresponse)>` | Promise  
  
### fetchErrors(request, callback)
    
    
    public fetchErrors(request: google.cloud.datastream.v1alpha1.IFetchErrorsRequest, callback: google.cloud.datastream.v1alpha1.Datastream.FetchErrorsCallback): void;

Calls FetchErrors.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchErrorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ifetcherrorsrequest)`   
FetchErrorsRequest message or plain object  
`callback` |  `[FetchErrorsCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchErrors(request)
    
    
    public fetchErrors(request: google.cloud.datastream.v1alpha1.IFetchErrorsRequest): Promise<google.longrunning.Operation>;

Calls FetchErrors.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchErrorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ifetcherrorsrequest)`   
FetchErrorsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.longrunning.operation)>` | Promise  
  
### fetchStaticIps(request, callback)
    
    
    public fetchStaticIps(request: google.cloud.datastream.v1alpha1.IFetchStaticIpsRequest, callback: google.cloud.datastream.v1alpha1.Datastream.FetchStaticIpsCallback): void;

Calls FetchStaticIps.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchStaticIpsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ifetchstaticipsrequest)`   
FetchStaticIpsRequest message or plain object  
`callback` |  `[FetchStaticIpsCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and FetchStaticIpsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchStaticIps(request)
    
    
    public fetchStaticIps(request: google.cloud.datastream.v1alpha1.IFetchStaticIpsRequest): Promise<google.cloud.datastream.v1alpha1.FetchStaticIpsResponse>;

Calls FetchStaticIps.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchStaticIpsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ifetchstaticipsrequest)`   
FetchStaticIpsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datastream.v1alpha1.FetchStaticIpsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.fetchstaticipsresponse)>` | Promise  
  
### getConnectionProfile(request, callback)
    
    
    public getConnectionProfile(request: google.cloud.datastream.v1alpha1.IGetConnectionProfileRequest, callback: google.cloud.datastream.v1alpha1.Datastream.GetConnectionProfileCallback): void;

Calls GetConnectionProfile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectionProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.igetconnectionprofilerequest)`   
GetConnectionProfileRequest message or plain object  
`callback` |  `[GetConnectionProfileCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and ConnectionProfile  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConnectionProfile(request)
    
    
    public getConnectionProfile(request: google.cloud.datastream.v1alpha1.IGetConnectionProfileRequest): Promise<google.cloud.datastream.v1alpha1.ConnectionProfile>;

Calls GetConnectionProfile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectionProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.igetconnectionprofilerequest)`   
GetConnectionProfileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datastream.v1alpha1.ConnectionProfile](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.connectionprofile)>` | Promise  
  
### getPrivateConnection(request, callback)
    
    
    public getPrivateConnection(request: google.cloud.datastream.v1alpha1.IGetPrivateConnectionRequest, callback: google.cloud.datastream.v1alpha1.Datastream.GetPrivateConnectionCallback): void;

Calls GetPrivateConnection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPrivateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.igetprivateconnectionrequest)`   
GetPrivateConnectionRequest message or plain object  
`callback` |  `[GetPrivateConnectionCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and PrivateConnection  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPrivateConnection(request)
    
    
    public getPrivateConnection(request: google.cloud.datastream.v1alpha1.IGetPrivateConnectionRequest): Promise<google.cloud.datastream.v1alpha1.PrivateConnection>;

Calls GetPrivateConnection.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPrivateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.igetprivateconnectionrequest)`   
GetPrivateConnectionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datastream.v1alpha1.PrivateConnection](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.privateconnection-class)>` | Promise  
  
### getRoute(request, callback)
    
    
    public getRoute(request: google.cloud.datastream.v1alpha1.IGetRouteRequest, callback: google.cloud.datastream.v1alpha1.Datastream.GetRouteCallback): void;

Calls GetRoute.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRouteRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.igetrouterequest)`   
GetRouteRequest message or plain object  
`callback` |  `[GetRouteCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and Route  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRoute(request)
    
    
    public getRoute(request: google.cloud.datastream.v1alpha1.IGetRouteRequest): Promise<google.cloud.datastream.v1alpha1.Route>;

Calls GetRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetRouteRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.igetrouterequest)`   
GetRouteRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datastream.v1alpha1.Route](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.route)>` | Promise  
  
### getStream(request, callback)
    
    
    public getStream(request: google.cloud.datastream.v1alpha1.IGetStreamRequest, callback: google.cloud.datastream.v1alpha1.Datastream.GetStreamCallback): void;

Calls GetStream.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.igetstreamrequest)`   
GetStreamRequest message or plain object  
`callback` |  `[GetStreamCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and Stream  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getStream(request)
    
    
    public getStream(request: google.cloud.datastream.v1alpha1.IGetStreamRequest): Promise<google.cloud.datastream.v1alpha1.Stream>;

Calls GetStream.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.igetstreamrequest)`   
GetStreamRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datastream.v1alpha1.Stream](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.stream-class)>` | Promise  
  
### listConnectionProfiles(request, callback)
    
    
    public listConnectionProfiles(request: google.cloud.datastream.v1alpha1.IListConnectionProfilesRequest, callback: google.cloud.datastream.v1alpha1.Datastream.ListConnectionProfilesCallback): void;

Calls ListConnectionProfiles.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConnectionProfilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ilistconnectionprofilesrequest)`   
ListConnectionProfilesRequest message or plain object  
`callback` |  `[ListConnectionProfilesCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and ListConnectionProfilesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConnectionProfiles(request)
    
    
    public listConnectionProfiles(request: google.cloud.datastream.v1alpha1.IListConnectionProfilesRequest): Promise<google.cloud.datastream.v1alpha1.ListConnectionProfilesResponse>;

Calls ListConnectionProfiles.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListConnectionProfilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ilistconnectionprofilesrequest)`   
ListConnectionProfilesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datastream.v1alpha1.ListConnectionProfilesResponse](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.listconnectionprofilesresponse)>` | Promise  
  
### listPrivateConnections(request, callback)
    
    
    public listPrivateConnections(request: google.cloud.datastream.v1alpha1.IListPrivateConnectionsRequest, callback: google.cloud.datastream.v1alpha1.Datastream.ListPrivateConnectionsCallback): void;

Calls ListPrivateConnections.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPrivateConnectionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ilistprivateconnectionsrequest)`   
ListPrivateConnectionsRequest message or plain object  
`callback` |  `[ListPrivateConnectionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPrivateConnectionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPrivateConnections(request)
    
    
    public listPrivateConnections(request: google.cloud.datastream.v1alpha1.IListPrivateConnectionsRequest): Promise<google.cloud.datastream.v1alpha1.ListPrivateConnectionsResponse>;

Calls ListPrivateConnections.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPrivateConnectionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ilistprivateconnectionsrequest)`   
ListPrivateConnectionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datastream.v1alpha1.ListPrivateConnectionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.listprivateconnectionsresponse)>` | Promise  
  
### listRoutes(request, callback)
    
    
    public listRoutes(request: google.cloud.datastream.v1alpha1.IListRoutesRequest, callback: google.cloud.datastream.v1alpha1.Datastream.ListRoutesCallback): void;

Calls ListRoutes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRoutesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ilistroutesrequest)`   
ListRoutesRequest message or plain object  
`callback` |  `[ListRoutesCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and ListRoutesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRoutes(request)
    
    
    public listRoutes(request: google.cloud.datastream.v1alpha1.IListRoutesRequest): Promise<google.cloud.datastream.v1alpha1.ListRoutesResponse>;

Calls ListRoutes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListRoutesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.ilistroutesrequest)`   
ListRoutesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datastream.v1alpha1.ListRoutesResponse](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.listroutesresponse)>` | Promise  
  
### listStreams(request, callback)
    
    
    public listStreams(request: google.cloud.datastream.v1alpha1.IListStreamsRequest, callback: google.cloud.datastream.v1alpha1.Datastream.ListStreamsCallback): void;

Calls ListStreams.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListStreamsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.iliststreamsrequest)`   
ListStreamsRequest message or plain object  
`callback` |  `[ListStreamsCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and ListStreamsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listStreams(request)
    
    
    public listStreams(request: google.cloud.datastream.v1alpha1.IListStreamsRequest): Promise<google.cloud.datastream.v1alpha1.ListStreamsResponse>;

Calls ListStreams.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListStreamsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.iliststreamsrequest)`   
ListStreamsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datastream.v1alpha1.ListStreamsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.liststreamsresponse)>` | Promise  
  
### updateConnectionProfile(request, callback)
    
    
    public updateConnectionProfile(request: google.cloud.datastream.v1alpha1.IUpdateConnectionProfileRequest, callback: google.cloud.datastream.v1alpha1.Datastream.UpdateConnectionProfileCallback): void;

Calls UpdateConnectionProfile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConnectionProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.iupdateconnectionprofilerequest)`   
UpdateConnectionProfileRequest message or plain object  
`callback` |  `[UpdateConnectionProfileCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConnectionProfile(request)
    
    
    public updateConnectionProfile(request: google.cloud.datastream.v1alpha1.IUpdateConnectionProfileRequest): Promise<google.longrunning.Operation>;

Calls UpdateConnectionProfile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConnectionProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.iupdateconnectionprofilerequest)`   
UpdateConnectionProfileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.longrunning.operation)>` | Promise  
  
### updateStream(request, callback)
    
    
    public updateStream(request: google.cloud.datastream.v1alpha1.IUpdateStreamRequest, callback: google.cloud.datastream.v1alpha1.Datastream.UpdateStreamCallback): void;

Calls UpdateStream.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.iupdatestreamrequest)`   
UpdateStreamRequest message or plain object  
`callback` |  `[UpdateStreamCallback](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateStream(request)
    
    
    public updateStream(request: google.cloud.datastream.v1alpha1.IUpdateStreamRequest): Promise<google.longrunning.Operation>;

Calls UpdateStream.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1alpha1.iupdatestreamrequest)`   
UpdateStreamRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
