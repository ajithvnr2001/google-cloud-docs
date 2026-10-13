---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Datastream.DatastreamBase
title: DataStream v1 API - Class Datastream.DatastreamBase (2.12.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:41:22.545918+00:00
---

# DataStream v1 API - Class Datastream.DatastreamBase (2.12.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Datastream.DatastreamBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  DataStream v1 API - Class Datastream.DatastreamBase (2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.12.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Datastream.DatastreamBase)
  * [ 2.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.11.0/Google.Cloud.Datastream.V1.Datastream.DatastreamBase)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.10.0/Google.Cloud.Datastream.V1.Datastream.DatastreamBase)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.9.0/Google.Cloud.Datastream.V1.Datastream.DatastreamBase)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.8.0/Google.Cloud.Datastream.V1.Datastream.DatastreamBase)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.7.0/Google.Cloud.Datastream.V1.Datastream.DatastreamBase)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.6.0/Google.Cloud.Datastream.V1.Datastream.DatastreamBase)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.5.0/Google.Cloud.Datastream.V1.Datastream.DatastreamBase)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.4.0/Google.Cloud.Datastream.V1.Datastream.DatastreamBase)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.3.0/Google.Cloud.Datastream.V1.Datastream.DatastreamBase)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.2.0/Google.Cloud.Datastream.V1.Datastream.DatastreamBase)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.1.0/Google.Cloud.Datastream.V1.Datastream.DatastreamBase)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.0.0/Google.Cloud.Datastream.V1.Datastream.DatastreamBase)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/1.0.0/Google.Cloud.Datastream.V1.Datastream.DatastreamBase)


    
    
    [BindServiceMethod(typeof(Datastream), "BindService")]
    public abstract class Datastream.DatastreamBase

Reference documentation and code samples for the DataStream v1 API class Datastream.DatastreamBase.

Base class for server-side implementations of Datastream

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Datastream.DatastreamBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Datastream.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1)

## Assembly

Google.Cloud.Datastream.V1.dll

## Methods 

### CreateConnectionProfile(CreateConnectionProfileRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateConnectionProfile(CreateConnectionProfileRequest request, ServerCallContext context)

Use this method to create a connection profile in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateConnectionProfileRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### CreatePrivateConnection(CreatePrivateConnectionRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreatePrivateConnection(CreatePrivateConnectionRequest request, ServerCallContext context)

Use this method to create a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreatePrivateConnectionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### CreateRoute(CreateRouteRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateRoute(CreateRouteRequest request, ServerCallContext context)

Use this method to create a route for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateRouteRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### CreateStream(CreateStreamRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateStream(CreateStreamRequest request, ServerCallContext context)

Use this method to create a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.CreateStreamRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteConnectionProfile(DeleteConnectionProfileRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteConnectionProfile(DeleteConnectionProfileRequest request, ServerCallContext context)

Use this method to delete a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteConnectionProfileRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeletePrivateConnection(DeletePrivateConnectionRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeletePrivateConnection(DeletePrivateConnectionRequest request, ServerCallContext context)

Use this method to delete a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeletePrivateConnectionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteRoute(DeleteRouteRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteRoute(DeleteRouteRequest request, ServerCallContext context)

Use this method to delete a route.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteRouteRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteStream(DeleteStreamRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteStream(DeleteStreamRequest request, ServerCallContext context)

Use this method to delete a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DeleteStreamRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DiscoverConnectionProfile(DiscoverConnectionProfileRequest, ServerCallContext)
    
    
    public virtual Task<DiscoverConnectionProfileResponse> DiscoverConnectionProfile(DiscoverConnectionProfileRequest request, ServerCallContext context)

Use this method to discover a connection profile. The discover API call exposes the data objects and metadata belonging to the profile. Typically, a request returns children data objects of a parent data object that's optionally supplied in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DiscoverConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DiscoverConnectionProfileRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DiscoverConnectionProfileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.DiscoverConnectionProfileResponse)` | The response to send back to the client (wrapped by a task).  
  
### FetchStaticIps(FetchStaticIpsRequest, ServerCallContext)
    
    
    public virtual Task<FetchStaticIpsResponse> FetchStaticIps(FetchStaticIpsRequest request, ServerCallContext context)

The FetchStaticIps API call exposes the static IP addresses used by Datastream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchStaticIpsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.FetchStaticIpsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FetchStaticIpsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.FetchStaticIpsResponse)` | The response to send back to the client (wrapped by a task).  
  
### GetConnectionProfile(GetConnectionProfileRequest, ServerCallContext)
    
    
    public virtual Task<ConnectionProfile> GetConnectionProfile(GetConnectionProfileRequest request, ServerCallContext context)

Use this method to get details about a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetConnectionProfileRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)` | The response to send back to the client (wrapped by a task).  
  
### GetPrivateConnection(GetPrivateConnectionRequest, ServerCallContext)
    
    
    public virtual Task<PrivateConnection> GetPrivateConnection(GetPrivateConnectionRequest request, ServerCallContext context)

Use this method to get details about a private connectivity configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPrivateConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetPrivateConnectionRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrivateConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnection)` | The response to send back to the client (wrapped by a task).  
  
### GetRoute(GetRouteRequest, ServerCallContext)
    
    
    public virtual Task<Route> GetRoute(GetRouteRequest request, ServerCallContext context)

Use this method to get details about a route.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRouteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetRouteRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Route](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Route)` | The response to send back to the client (wrapped by a task).  
  
### GetStream(GetStreamRequest, ServerCallContext)
    
    
    public virtual Task<Stream> GetStream(GetStreamRequest request, ServerCallContext context)

Use this method to get details about a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Stream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.Stream)` | The response to send back to the client (wrapped by a task).  
  
### GetStreamObject(GetStreamObjectRequest, ServerCallContext)
    
    
    public virtual Task<StreamObject> GetStreamObject(GetStreamObjectRequest request, ServerCallContext context)

Use this method to get details about a stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStreamObjectRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GetStreamObjectRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | The response to send back to the client (wrapped by a task).  
  
### ListConnectionProfiles(ListConnectionProfilesRequest, ServerCallContext)
    
    
    public virtual Task<ListConnectionProfilesResponse> ListConnectionProfiles(ListConnectionProfilesRequest request, ServerCallContext context)

Use this method to list connection profiles created in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConnectionProfilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListConnectionProfilesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListConnectionProfilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListConnectionProfilesResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListPrivateConnections(ListPrivateConnectionsRequest, ServerCallContext)
    
    
    public virtual Task<ListPrivateConnectionsResponse> ListPrivateConnections(ListPrivateConnectionsRequest request, ServerCallContext context)

Use this method to list private connectivity configurations in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPrivateConnectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListPrivateConnectionsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListPrivateConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListPrivateConnectionsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListRoutes(ListRoutesRequest, ServerCallContext)
    
    
    public virtual Task<ListRoutesResponse> ListRoutes(ListRoutesRequest request, ServerCallContext context)

Use this method to list routes created for a private connectivity configuration in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRoutesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListRoutesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListRoutesResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListStreamObjects(ListStreamObjectsRequest, ServerCallContext)
    
    
    public virtual Task<ListStreamObjectsResponse> ListStreamObjects(ListStreamObjectsRequest request, ServerCallContext context)

Use this method to list the objects of a specific stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListStreamObjectsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamObjectsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListStreamObjectsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamObjectsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListStreams(ListStreamsRequest, ServerCallContext)
    
    
    public virtual Task<ListStreamsResponse> ListStreams(ListStreamsRequest request, ServerCallContext context)

Use this method to list streams in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListStreamsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListStreamsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ListStreamsResponse)` | The response to send back to the client (wrapped by a task).  
  
### LookupStreamObject(LookupStreamObjectRequest, ServerCallContext)
    
    
    public virtual Task<StreamObject> LookupStreamObject(LookupStreamObjectRequest request, ServerCallContext context)

Use this method to look up a stream object by its source object identifier.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupStreamObjectRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.LookupStreamObjectRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StreamObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StreamObject)` | The response to send back to the client (wrapped by a task).  
  
### RunStream(RunStreamRequest, ServerCallContext)
    
    
    public virtual Task<Operation> RunStream(RunStreamRequest request, ServerCallContext context)

Use this method to start, resume or recover a stream with a non default CDC strategy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.RunStreamRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### StartBackfillJob(StartBackfillJobRequest, ServerCallContext)
    
    
    public virtual Task<StartBackfillJobResponse> StartBackfillJob(StartBackfillJobRequest request, ServerCallContext context)

Use this method to start a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartBackfillJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StartBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StartBackfillJobResponse)` | The response to send back to the client (wrapped by a task).  
  
### StopBackfillJob(StopBackfillJobRequest, ServerCallContext)
    
    
    public virtual Task<StopBackfillJobResponse> StopBackfillJob(StopBackfillJobRequest request, ServerCallContext context)

Use this method to stop a backfill job for the specified stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopBackfillJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[StopBackfillJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StopBackfillJobResponse)` | The response to send back to the client (wrapped by a task).  
  
### UpdateConnectionProfile(UpdateConnectionProfileRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateConnectionProfile(UpdateConnectionProfileRequest request, ServerCallContext context)

Use this method to update the parameters of a connection profile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.UpdateConnectionProfileRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### UpdateStream(UpdateStreamRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UpdateStream(UpdateStreamRequest request, ServerCallContext context)

Use this method to update the configuration of a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.UpdateStreamRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
