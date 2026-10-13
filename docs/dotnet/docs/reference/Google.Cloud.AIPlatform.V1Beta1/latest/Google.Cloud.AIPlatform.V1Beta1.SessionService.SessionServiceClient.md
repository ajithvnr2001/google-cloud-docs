---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SessionService.SessionServiceClient
title: Vertex AI v1beta1 API - Class SessionService.SessionServiceClient (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:25.606713+00:00
---

# Vertex AI v1beta1 API - Class SessionService.SessionServiceClient (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SessionService.SessionServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class SessionService.SessionServiceClient (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public class SessionService.SessionServiceClient : ClientBase<SessionService.SessionServiceClient>

Reference documentation and code samples for the Vertex AI v1beta1 API class SessionService.SessionServiceClient.

Client for SessionService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[SessionService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SessionService)[SessionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SessionService.SessionServiceClient) > SessionService.SessionServiceClient

## Inherited Members

[ClientBase<SessionService.SessionServiceClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### SessionServiceClient()
    
    
    protected SessionServiceClient()

Protected parameterless constructor to allow creation of test doubles.

### SessionServiceClient(CallInvoker)
    
    
    public SessionServiceClient(CallInvoker callInvoker)

Creates a new client for SessionService that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### SessionServiceClient(ChannelBase)
    
    
    public SessionServiceClient(ChannelBase channel)

Creates a new client for SessionService

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### SessionServiceClient(ClientBaseConfiguration)
    
    
    protected SessionServiceClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### AppendEvent(AppendEventRequest, CallOptions)
    
    
    public virtual AppendEventResponse AppendEvent(AppendEventRequest request, CallOptions options)

Appends an event to a given session.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AppendEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AppendEventRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AppendEventResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AppendEventResponse)` | The response received from the server.  
  
### AppendEvent(AppendEventRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AppendEventResponse AppendEvent(AppendEventRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Appends an event to a given session.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AppendEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AppendEventRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AppendEventResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AppendEventResponse)` | The response received from the server.  
  
### AppendEventAsync(AppendEventRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<AppendEventResponse> AppendEventAsync(AppendEventRequest request, CallOptions options)

Appends an event to a given session.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AppendEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AppendEventRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AppendEventResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AppendEventResponse)` | The call object.  
  
### AppendEventAsync(AppendEventRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<AppendEventResponse> AppendEventAsync(AppendEventRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Appends an event to a given session.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AppendEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AppendEventRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AppendEventResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AppendEventResponse)` | The call object.  
  
### CreateIAMPolicyClient()
    
    
    public virtual IAMPolicy.IAMPolicyClient CreateIAMPolicyClient()

Creates a new instance of [IAMPolicy.IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.IAMPolicyClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[IAMPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.html)[IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.IAMPolicyClient.html)` | A new [IAMPolicy.IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.IAMPolicyClient.html) for the same target as this client.  
  
### CreateLocationsClient()
    
    
    public virtual Locations.LocationsClient CreateLocationsClient()

Creates a new instance of [Locations.LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[Locations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.html)[LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html)` | A new [Locations.LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html) for the same target as this client.  
  
### CreateOperationsClient()
    
    
    public virtual Operations.OperationsClient CreateOperationsClient()

Creates a new instance of [Operations.OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[Operations](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.html)[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html)` | A new Operations client for the same target as this client.  
  
### CreateSession(CreateSessionRequest, CallOptions)
    
    
    public virtual Operation CreateSession(CreateSessionRequest request, CallOptions options)

Creates a new [Session][google.cloud.aiplatform.v1beta1.Session].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateSessionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateSession(CreateSessionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateSession(CreateSessionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new [Session][google.cloud.aiplatform.v1beta1.Session].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateSessionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateSessionAsync(CreateSessionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateSessionAsync(CreateSessionRequest request, CallOptions options)

Creates a new [Session][google.cloud.aiplatform.v1beta1.Session].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateSessionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateSessionAsync(CreateSessionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateSessionAsync(CreateSessionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new [Session][google.cloud.aiplatform.v1beta1.Session].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateSessionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteSession(DeleteSessionRequest, CallOptions)
    
    
    public virtual Operation DeleteSession(DeleteSessionRequest request, CallOptions options)

Deletes details of the specific [Session][google.cloud.aiplatform.v1beta1.Session].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteSessionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteSession(DeleteSessionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteSession(DeleteSessionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes details of the specific [Session][google.cloud.aiplatform.v1beta1.Session].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteSessionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteSessionAsync(DeleteSessionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteSessionAsync(DeleteSessionRequest request, CallOptions options)

Deletes details of the specific [Session][google.cloud.aiplatform.v1beta1.Session].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteSessionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteSessionAsync(DeleteSessionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteSessionAsync(DeleteSessionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes details of the specific [Session][google.cloud.aiplatform.v1beta1.Session].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteSessionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### GetSession(GetSessionRequest, CallOptions)
    
    
    public virtual Session GetSession(GetSessionRequest request, CallOptions options)

Gets details of the specific [Session][google.cloud.aiplatform.v1beta1.Session].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetSessionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Session)` | The response received from the server.  
  
### GetSession(GetSessionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Session GetSession(GetSessionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of the specific [Session][google.cloud.aiplatform.v1beta1.Session].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetSessionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Session)` | The response received from the server.  
  
### GetSessionAsync(GetSessionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Session> GetSessionAsync(GetSessionRequest request, CallOptions options)

Gets details of the specific [Session][google.cloud.aiplatform.v1beta1.Session].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetSessionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Session](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Session)` | The call object.  
  
### GetSessionAsync(GetSessionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Session> GetSessionAsync(GetSessionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of the specific [Session][google.cloud.aiplatform.v1beta1.Session].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetSessionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Session](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Session)` | The call object.  
  
### ListEvents(ListEventsRequest, CallOptions)
    
    
    public virtual ListEventsResponse ListEvents(ListEventsRequest request, CallOptions options)

Lists [Events][google.cloud.aiplatform.v1beta1.Event] in a given session.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEventsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListEventsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListEventsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListEventsResponse)` | The response received from the server.  
  
### ListEvents(ListEventsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListEventsResponse ListEvents(ListEventsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists [Events][google.cloud.aiplatform.v1beta1.Event] in a given session.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEventsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListEventsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListEventsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListEventsResponse)` | The response received from the server.  
  
### ListEventsAsync(ListEventsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListEventsResponse> ListEventsAsync(ListEventsRequest request, CallOptions options)

Lists [Events][google.cloud.aiplatform.v1beta1.Event] in a given session.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEventsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListEventsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListEventsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListEventsResponse)` | The call object.  
  
### ListEventsAsync(ListEventsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListEventsResponse> ListEventsAsync(ListEventsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists [Events][google.cloud.aiplatform.v1beta1.Event] in a given session.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEventsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListEventsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListEventsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListEventsResponse)` | The call object.  
  
### ListSessions(ListSessionsRequest, CallOptions)
    
    
    public virtual ListSessionsResponse ListSessions(ListSessionsRequest request, CallOptions options)

Lists [Sessions][google.cloud.aiplatform.v1beta1.Session] in a given reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSessionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListSessionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListSessionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListSessionsResponse)` | The response received from the server.  
  
### ListSessions(ListSessionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListSessionsResponse ListSessions(ListSessionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists [Sessions][google.cloud.aiplatform.v1beta1.Session] in a given reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSessionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListSessionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListSessionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListSessionsResponse)` | The response received from the server.  
  
### ListSessionsAsync(ListSessionsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListSessionsResponse> ListSessionsAsync(ListSessionsRequest request, CallOptions options)

Lists [Sessions][google.cloud.aiplatform.v1beta1.Session] in a given reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSessionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListSessionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListSessionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListSessionsResponse)` | The call object.  
  
### ListSessionsAsync(ListSessionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListSessionsResponse> ListSessionsAsync(ListSessionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists [Sessions][google.cloud.aiplatform.v1beta1.Session] in a given reasoning engine.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSessionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListSessionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListSessionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListSessionsResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override SessionService.SessionServiceClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SessionService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SessionService)[SessionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SessionService.SessionServiceClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.AIPlatform.V1Beta1.SessionService.SessionServiceClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### UpdateSession(UpdateSessionRequest, CallOptions)
    
    
    public virtual Session UpdateSession(UpdateSessionRequest request, CallOptions options)

Updates the specific [Session][google.cloud.aiplatform.v1beta1.Session].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateSessionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Session)` | The response received from the server.  
  
### UpdateSession(UpdateSessionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Session UpdateSession(UpdateSessionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the specific [Session][google.cloud.aiplatform.v1beta1.Session].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateSessionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Session)` | The response received from the server.  
  
### UpdateSessionAsync(UpdateSessionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Session> UpdateSessionAsync(UpdateSessionRequest request, CallOptions options)

Updates the specific [Session][google.cloud.aiplatform.v1beta1.Session].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateSessionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Session](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Session)` | The call object.  
  
### UpdateSessionAsync(UpdateSessionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Session> UpdateSessionAsync(UpdateSessionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the specific [Session][google.cloud.aiplatform.v1beta1.Session].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateSessionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Session](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Session)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
