---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentService.AgentServiceClient
title: Gemini Enterprise for Customer Experience v1beta API - Class AgentService.AgentServiceClient (1.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:39:46.564586+00:00
---

# Gemini Enterprise for Customer Experience v1beta API - Class AgentService.AgentServiceClient (1.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentService.AgentServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1beta API - Class AgentService.AgentServiceClient (1.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta09 (latest)  1.0.0-beta08 
    
    
    public class AgentService.AgentServiceClient : ClientBase<AgentService.AgentServiceClient>

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1beta API class AgentService.AgentServiceClient.

Client for AgentService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[AgentService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentService)[AgentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentService.AgentServiceClient) > AgentService.AgentServiceClient

## Inherited Members

[ClientBase<AgentService.AgentServiceClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Ces.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta)

## Assembly

Google.Cloud.Ces.V1Beta.dll

## Constructors 

### AgentServiceClient()
    
    
    protected AgentServiceClient()

Protected parameterless constructor to allow creation of test doubles.

### AgentServiceClient(CallInvoker)
    
    
    public AgentServiceClient(CallInvoker callInvoker)

Creates a new client for AgentService that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### AgentServiceClient(ChannelBase)
    
    
    public AgentServiceClient(ChannelBase channel)

Creates a new client for AgentService

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### AgentServiceClient(ClientBaseConfiguration)
    
    
    protected AgentServiceClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### BatchDeleteConversations(BatchDeleteConversationsRequest, CallOptions)
    
    
    public virtual Operation BatchDeleteConversations(BatchDeleteConversationsRequest request, CallOptions options)

Batch deletes the specified conversations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### BatchDeleteConversations(BatchDeleteConversationsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation BatchDeleteConversations(BatchDeleteConversationsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Batch deletes the specified conversations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsRequest)`  
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
  
### BatchDeleteConversationsAsync(BatchDeleteConversationsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> BatchDeleteConversationsAsync(BatchDeleteConversationsRequest request, CallOptions options)

Batch deletes the specified conversations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### BatchDeleteConversationsAsync(BatchDeleteConversationsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> BatchDeleteConversationsAsync(BatchDeleteConversationsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Batch deletes the specified conversations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsRequest)`  
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
  
### CreateAgent(CreateAgentRequest, CallOptions)
    
    
    public virtual Agent CreateAgent(CreateAgentRequest request, CallOptions options)

Creates a new agent in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAgentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The response received from the server.  
  
### CreateAgent(CreateAgentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Agent CreateAgent(CreateAgentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new agent in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAgentRequest)`  
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
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The response received from the server.  
  
### CreateAgentAsync(CreateAgentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Agent> CreateAgentAsync(CreateAgentRequest request, CallOptions options)

Creates a new agent in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAgentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The call object.  
  
### CreateAgentAsync(CreateAgentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Agent> CreateAgentAsync(CreateAgentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new agent in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAgentRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The call object.  
  
### CreateApp(CreateAppRequest, CallOptions)
    
    
    public virtual Operation CreateApp(CreateAppRequest request, CallOptions options)

Creates a new app in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAppRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateApp(CreateAppRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateApp(CreateAppRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new app in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAppRequest)`  
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
  
### CreateAppAsync(CreateAppRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateAppAsync(CreateAppRequest request, CallOptions options)

Creates a new app in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAppRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateAppAsync(CreateAppRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateAppAsync(CreateAppRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new app in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAppRequest)`  
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
  
### CreateAppVersion(CreateAppVersionRequest, CallOptions)
    
    
    public virtual AppVersion CreateAppVersion(CreateAppVersionRequest request, CallOptions options)

Creates a new app version in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAppVersionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | The response received from the server.  
  
### CreateAppVersion(CreateAppVersionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AppVersion CreateAppVersion(CreateAppVersionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new app version in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAppVersionRequest)`  
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
`[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | The response received from the server.  
  
### CreateAppVersionAsync(CreateAppVersionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<AppVersion> CreateAppVersionAsync(CreateAppVersionRequest request, CallOptions options)

Creates a new app version in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAppVersionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | The call object.  
  
### CreateAppVersionAsync(CreateAppVersionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<AppVersion> CreateAppVersionAsync(CreateAppVersionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new app version in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAppVersionRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | The call object.  
  
### CreateDeployment(CreateDeploymentRequest, CallOptions)
    
    
    public virtual Deployment CreateDeployment(CreateDeploymentRequest request, CallOptions options)

Creates a new deployment in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The response received from the server.  
  
### CreateDeployment(CreateDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Deployment CreateDeployment(CreateDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new deployment in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateDeploymentRequest)`  
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
`[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The response received from the server.  
  
### CreateDeploymentAsync(CreateDeploymentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Deployment> CreateDeploymentAsync(CreateDeploymentRequest request, CallOptions options)

Creates a new deployment in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The call object.  
  
### CreateDeploymentAsync(CreateDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Deployment> CreateDeploymentAsync(CreateDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new deployment in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateDeploymentRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The call object.  
  
### CreateExample(CreateExampleRequest, CallOptions)
    
    
    public virtual Example CreateExample(CreateExampleRequest request, CallOptions options)

Creates a new example in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateExampleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The response received from the server.  
  
### CreateExample(CreateExampleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Example CreateExample(CreateExampleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new example in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateExampleRequest)`  
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
`[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The response received from the server.  
  
### CreateExampleAsync(CreateExampleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Example> CreateExampleAsync(CreateExampleRequest request, CallOptions options)

Creates a new example in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateExampleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The call object.  
  
### CreateExampleAsync(CreateExampleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Example> CreateExampleAsync(CreateExampleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new example in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateExampleRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The call object.  
  
### CreateGuardrail(CreateGuardrailRequest, CallOptions)
    
    
    public virtual Guardrail CreateGuardrail(CreateGuardrailRequest request, CallOptions options)

Creates a new guardrail in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateGuardrailRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The response received from the server.  
  
### CreateGuardrail(CreateGuardrailRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Guardrail CreateGuardrail(CreateGuardrailRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new guardrail in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateGuardrailRequest)`  
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
`[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The response received from the server.  
  
### CreateGuardrailAsync(CreateGuardrailRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Guardrail> CreateGuardrailAsync(CreateGuardrailRequest request, CallOptions options)

Creates a new guardrail in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateGuardrailRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The call object.  
  
### CreateGuardrailAsync(CreateGuardrailRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Guardrail> CreateGuardrailAsync(CreateGuardrailRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new guardrail in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateGuardrailRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The call object.  
  
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
  
### CreateTool(CreateToolRequest, CallOptions)
    
    
    public virtual Tool CreateTool(CreateToolRequest request, CallOptions options)

Creates a new tool in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The response received from the server.  
  
### CreateTool(CreateToolRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Tool CreateTool(CreateToolRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new tool in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolRequest)`  
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
`[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The response received from the server.  
  
### CreateToolAsync(CreateToolRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Tool> CreateToolAsync(CreateToolRequest request, CallOptions options)

Creates a new tool in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The call object.  
  
### CreateToolAsync(CreateToolRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Tool> CreateToolAsync(CreateToolRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new tool in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The call object.  
  
### CreateToolset(CreateToolsetRequest, CallOptions)
    
    
    public virtual Toolset CreateToolset(CreateToolsetRequest request, CallOptions options)

Creates a new toolset in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolsetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The response received from the server.  
  
### CreateToolset(CreateToolsetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Toolset CreateToolset(CreateToolsetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new toolset in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolsetRequest)`  
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
`[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The response received from the server.  
  
### CreateToolsetAsync(CreateToolsetRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Toolset> CreateToolsetAsync(CreateToolsetRequest request, CallOptions options)

Creates a new toolset in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolsetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The call object.  
  
### CreateToolsetAsync(CreateToolsetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Toolset> CreateToolsetAsync(CreateToolsetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new toolset in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolsetRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The call object.  
  
### DeleteAgent(DeleteAgentRequest, CallOptions)
    
    
    public virtual Empty DeleteAgent(DeleteAgentRequest request, CallOptions options)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAgentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteAgent(DeleteAgentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteAgent(DeleteAgentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAgentRequest)`  
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
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteAgentAsync(DeleteAgentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteAgentAsync(DeleteAgentRequest request, CallOptions options)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAgentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteAgentAsync(DeleteAgentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteAgentAsync(DeleteAgentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAgentRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteApp(DeleteAppRequest, CallOptions)
    
    
    public virtual Operation DeleteApp(DeleteAppRequest request, CallOptions options)

Deletes the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAppRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteApp(DeleteAppRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteApp(DeleteAppRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAppRequest)`  
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
  
### DeleteAppAsync(DeleteAppRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteAppAsync(DeleteAppRequest request, CallOptions options)

Deletes the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAppRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteAppAsync(DeleteAppRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteAppAsync(DeleteAppRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAppRequest)`  
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
  
### DeleteAppVersion(DeleteAppVersionRequest, CallOptions)
    
    
    public virtual Empty DeleteAppVersion(DeleteAppVersionRequest request, CallOptions options)

Deletes the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAppVersionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteAppVersion(DeleteAppVersionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteAppVersion(DeleteAppVersionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAppVersionRequest)`  
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
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteAppVersionAsync(DeleteAppVersionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteAppVersionAsync(DeleteAppVersionRequest request, CallOptions options)

Deletes the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAppVersionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteAppVersionAsync(DeleteAppVersionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteAppVersionAsync(DeleteAppVersionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAppVersionRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteConversation(DeleteConversationRequest, CallOptions)
    
    
    public virtual Empty DeleteConversation(DeleteConversationRequest request, CallOptions options)

Deletes the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteConversationRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteConversation(DeleteConversationRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteConversation(DeleteConversationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteConversationRequest)`  
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
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteConversationAsync(DeleteConversationRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteConversationAsync(DeleteConversationRequest request, CallOptions options)

Deletes the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteConversationRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteConversationAsync(DeleteConversationRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteConversationAsync(DeleteConversationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteConversationRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteDeployment(DeleteDeploymentRequest, CallOptions)
    
    
    public virtual Empty DeleteDeployment(DeleteDeploymentRequest request, CallOptions options)

Deletes the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteDeployment(DeleteDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteDeployment(DeleteDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteDeploymentRequest)`  
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
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteDeploymentAsync(DeleteDeploymentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteDeploymentAsync(DeleteDeploymentRequest request, CallOptions options)

Deletes the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteDeploymentAsync(DeleteDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteDeploymentAsync(DeleteDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteDeploymentRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteExample(DeleteExampleRequest, CallOptions)
    
    
    public virtual Empty DeleteExample(DeleteExampleRequest request, CallOptions options)

Deletes the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteExampleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteExample(DeleteExampleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteExample(DeleteExampleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteExampleRequest)`  
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
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteExampleAsync(DeleteExampleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteExampleAsync(DeleteExampleRequest request, CallOptions options)

Deletes the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteExampleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteExampleAsync(DeleteExampleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteExampleAsync(DeleteExampleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteExampleRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteGuardrail(DeleteGuardrailRequest, CallOptions)
    
    
    public virtual Empty DeleteGuardrail(DeleteGuardrailRequest request, CallOptions options)

Deletes the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteGuardrailRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteGuardrail(DeleteGuardrailRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteGuardrail(DeleteGuardrailRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteGuardrailRequest)`  
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
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteGuardrailAsync(DeleteGuardrailRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteGuardrailAsync(DeleteGuardrailRequest request, CallOptions options)

Deletes the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteGuardrailRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteGuardrailAsync(DeleteGuardrailRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteGuardrailAsync(DeleteGuardrailRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteGuardrailRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteTool(DeleteToolRequest, CallOptions)
    
    
    public virtual Empty DeleteTool(DeleteToolRequest request, CallOptions options)

Deletes the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteToolRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteTool(DeleteToolRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteTool(DeleteToolRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteToolRequest)`  
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
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteToolAsync(DeleteToolRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteToolAsync(DeleteToolRequest request, CallOptions options)

Deletes the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteToolRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteToolAsync(DeleteToolRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteToolAsync(DeleteToolRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteToolRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteToolset(DeleteToolsetRequest, CallOptions)
    
    
    public virtual Empty DeleteToolset(DeleteToolsetRequest request, CallOptions options)

Deletes the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteToolsetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteToolset(DeleteToolsetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteToolset(DeleteToolsetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteToolsetRequest)`  
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
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteToolsetAsync(DeleteToolsetRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteToolsetAsync(DeleteToolsetRequest request, CallOptions options)

Deletes the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteToolsetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteToolsetAsync(DeleteToolsetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteToolsetAsync(DeleteToolsetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteToolsetRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### ExportApp(ExportAppRequest, CallOptions)
    
    
    public virtual Operation ExportApp(ExportAppRequest request, CallOptions options)

Exports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### ExportApp(ExportAppRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation ExportApp(ExportAppRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Exports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppRequest)`  
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
  
### ExportAppAsync(ExportAppRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> ExportAppAsync(ExportAppRequest request, CallOptions options)

Exports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### ExportAppAsync(ExportAppRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> ExportAppAsync(ExportAppRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Exports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppRequest)`  
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
  
### GenerateAppResource(GenerateAppResourceRequest, CallOptions)
    
    
    public virtual Operation GenerateAppResource(GenerateAppResourceRequest request, CallOptions options)

Generates specific resources (e.g. agent) in the app using LLM assistant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateAppResourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### GenerateAppResource(GenerateAppResourceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation GenerateAppResource(GenerateAppResourceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Generates specific resources (e.g. agent) in the app using LLM assistant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateAppResourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest)`  
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
  
### GenerateAppResourceAsync(GenerateAppResourceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> GenerateAppResourceAsync(GenerateAppResourceRequest request, CallOptions options)

Generates specific resources (e.g. agent) in the app using LLM assistant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateAppResourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### GenerateAppResourceAsync(GenerateAppResourceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> GenerateAppResourceAsync(GenerateAppResourceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Generates specific resources (e.g. agent) in the app using LLM assistant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateAppResourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest)`  
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
  
### GetAgent(GetAgentRequest, CallOptions)
    
    
    public virtual Agent GetAgent(GetAgentRequest request, CallOptions options)

Gets details of the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAgentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The response received from the server.  
  
### GetAgent(GetAgentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Agent GetAgent(GetAgentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAgentRequest)`  
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
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The response received from the server.  
  
### GetAgentAsync(GetAgentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Agent> GetAgentAsync(GetAgentRequest request, CallOptions options)

Gets details of the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAgentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The call object.  
  
### GetAgentAsync(GetAgentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Agent> GetAgentAsync(GetAgentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAgentRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The call object.  
  
### GetApp(GetAppRequest, CallOptions)
    
    
    public virtual App GetApp(GetAppRequest request, CallOptions options)

Gets details of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAppRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | The response received from the server.  
  
### GetApp(GetAppRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual App GetApp(GetAppRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAppRequest)`  
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
`[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | The response received from the server.  
  
### GetAppAsync(GetAppRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<App> GetAppAsync(GetAppRequest request, CallOptions options)

Gets details of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAppRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | The call object.  
  
### GetAppAsync(GetAppRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<App> GetAppAsync(GetAppRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAppRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | The call object.  
  
### GetAppVersion(GetAppVersionRequest, CallOptions)
    
    
    public virtual AppVersion GetAppVersion(GetAppVersionRequest request, CallOptions options)

Gets details of the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAppVersionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | The response received from the server.  
  
### GetAppVersion(GetAppVersionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AppVersion GetAppVersion(GetAppVersionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAppVersionRequest)`  
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
`[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | The response received from the server.  
  
### GetAppVersionAsync(GetAppVersionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<AppVersion> GetAppVersionAsync(GetAppVersionRequest request, CallOptions options)

Gets details of the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAppVersionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | The call object.  
  
### GetAppVersionAsync(GetAppVersionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<AppVersion> GetAppVersionAsync(GetAppVersionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAppVersionRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)` | The call object.  
  
### GetChangelog(GetChangelogRequest, CallOptions)
    
    
    public virtual Changelog GetChangelog(GetChangelogRequest request, CallOptions options)

Gets the specified changelog.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetChangelogRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetChangelogRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)` | The response received from the server.  
  
### GetChangelog(GetChangelogRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Changelog GetChangelog(GetChangelogRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the specified changelog.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetChangelogRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetChangelogRequest)`  
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
`[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)` | The response received from the server.  
  
### GetChangelogAsync(GetChangelogRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Changelog> GetChangelogAsync(GetChangelogRequest request, CallOptions options)

Gets the specified changelog.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetChangelogRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetChangelogRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)` | The call object.  
  
### GetChangelogAsync(GetChangelogRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Changelog> GetChangelogAsync(GetChangelogRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the specified changelog.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetChangelogRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetChangelogRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)` | The call object.  
  
### GetConversation(GetConversationRequest, CallOptions)
    
    
    public virtual Conversation GetConversation(GetConversationRequest request, CallOptions options)

Gets details of the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetConversationRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)` | The response received from the server.  
  
### GetConversation(GetConversationRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Conversation GetConversation(GetConversationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetConversationRequest)`  
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
`[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)` | The response received from the server.  
  
### GetConversationAsync(GetConversationRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Conversation> GetConversationAsync(GetConversationRequest request, CallOptions options)

Gets details of the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetConversationRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)` | The call object.  
  
### GetConversationAsync(GetConversationRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Conversation> GetConversationAsync(GetConversationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetConversationRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)` | The call object.  
  
### GetDeployment(GetDeploymentRequest, CallOptions)
    
    
    public virtual Deployment GetDeployment(GetDeploymentRequest request, CallOptions options)

Gets details of the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The response received from the server.  
  
### GetDeployment(GetDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Deployment GetDeployment(GetDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetDeploymentRequest)`  
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
`[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The response received from the server.  
  
### GetDeploymentAsync(GetDeploymentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Deployment> GetDeploymentAsync(GetDeploymentRequest request, CallOptions options)

Gets details of the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The call object.  
  
### GetDeploymentAsync(GetDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Deployment> GetDeploymentAsync(GetDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetDeploymentRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The call object.  
  
### GetExample(GetExampleRequest, CallOptions)
    
    
    public virtual Example GetExample(GetExampleRequest request, CallOptions options)

Gets details of the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetExampleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The response received from the server.  
  
### GetExample(GetExampleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Example GetExample(GetExampleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetExampleRequest)`  
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
`[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The response received from the server.  
  
### GetExampleAsync(GetExampleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Example> GetExampleAsync(GetExampleRequest request, CallOptions options)

Gets details of the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetExampleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The call object.  
  
### GetExampleAsync(GetExampleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Example> GetExampleAsync(GetExampleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetExampleRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The call object.  
  
### GetGuardrail(GetGuardrailRequest, CallOptions)
    
    
    public virtual Guardrail GetGuardrail(GetGuardrailRequest request, CallOptions options)

Gets details of the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetGuardrailRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The response received from the server.  
  
### GetGuardrail(GetGuardrailRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Guardrail GetGuardrail(GetGuardrailRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetGuardrailRequest)`  
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
`[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The response received from the server.  
  
### GetGuardrailAsync(GetGuardrailRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Guardrail> GetGuardrailAsync(GetGuardrailRequest request, CallOptions options)

Gets details of the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetGuardrailRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The call object.  
  
### GetGuardrailAsync(GetGuardrailRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Guardrail> GetGuardrailAsync(GetGuardrailRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetGuardrailRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The call object.  
  
### GetSecuritySettings(GetSecuritySettingsRequest, CallOptions)
    
    
    public virtual SecuritySettings GetSecuritySettings(GetSecuritySettingsRequest request, CallOptions options)

Retrieves the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetSecuritySettingsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | The response received from the server.  
  
### GetSecuritySettings(GetSecuritySettingsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual SecuritySettings GetSecuritySettings(GetSecuritySettingsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieves the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetSecuritySettingsRequest)`  
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
`[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | The response received from the server.  
  
### GetSecuritySettingsAsync(GetSecuritySettingsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<SecuritySettings> GetSecuritySettingsAsync(GetSecuritySettingsRequest request, CallOptions options)

Retrieves the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetSecuritySettingsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | The call object.  
  
### GetSecuritySettingsAsync(GetSecuritySettingsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<SecuritySettings> GetSecuritySettingsAsync(GetSecuritySettingsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieves the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetSecuritySettingsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | The call object.  
  
### GetTool(GetToolRequest, CallOptions)
    
    
    public virtual Tool GetTool(GetToolRequest request, CallOptions options)

Gets details of the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetToolRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The response received from the server.  
  
### GetTool(GetToolRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Tool GetTool(GetToolRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetToolRequest)`  
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
`[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The response received from the server.  
  
### GetToolAsync(GetToolRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Tool> GetToolAsync(GetToolRequest request, CallOptions options)

Gets details of the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetToolRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The call object.  
  
### GetToolAsync(GetToolRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Tool> GetToolAsync(GetToolRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetToolRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The call object.  
  
### GetToolset(GetToolsetRequest, CallOptions)
    
    
    public virtual Toolset GetToolset(GetToolsetRequest request, CallOptions options)

Gets details of the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetToolsetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The response received from the server.  
  
### GetToolset(GetToolsetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Toolset GetToolset(GetToolsetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetToolsetRequest)`  
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
`[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The response received from the server.  
  
### GetToolsetAsync(GetToolsetRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Toolset> GetToolsetAsync(GetToolsetRequest request, CallOptions options)

Gets details of the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetToolsetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The call object.  
  
### GetToolsetAsync(GetToolsetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Toolset> GetToolsetAsync(GetToolsetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetToolsetRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The call object.  
  
### ImportApp(ImportAppRequest, CallOptions)
    
    
    public virtual Operation ImportApp(ImportAppRequest request, CallOptions options)

Imports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### ImportApp(ImportAppRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation ImportApp(ImportAppRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Imports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppRequest)`  
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
  
### ImportAppAsync(ImportAppRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> ImportAppAsync(ImportAppRequest request, CallOptions options)

Imports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### ImportAppAsync(ImportAppRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> ImportAppAsync(ImportAppRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Imports the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppRequest)`  
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
  
### ListAgents(ListAgentsRequest, CallOptions)
    
    
    public virtual ListAgentsResponse ListAgents(ListAgentsRequest request, CallOptions options)

Lists agents in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAgentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAgentsResponse)` | The response received from the server.  
  
### ListAgents(ListAgentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListAgentsResponse ListAgents(ListAgentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists agents in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAgentsRequest)`  
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
`[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAgentsResponse)` | The response received from the server.  
  
### ListAgentsAsync(ListAgentsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListAgentsResponse> ListAgentsAsync(ListAgentsRequest request, CallOptions options)

Lists agents in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAgentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAgentsResponse)` | The call object.  
  
### ListAgentsAsync(ListAgentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListAgentsResponse> ListAgentsAsync(ListAgentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists agents in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAgentsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAgentsResponse)` | The call object.  
  
### ListAppVersions(ListAppVersionsRequest, CallOptions)
    
    
    public virtual ListAppVersionsResponse ListAppVersions(ListAppVersionsRequest request, CallOptions options)

Lists all app versions in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAppVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppVersionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAppVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppVersionsResponse)` | The response received from the server.  
  
### ListAppVersions(ListAppVersionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListAppVersionsResponse ListAppVersions(ListAppVersionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all app versions in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAppVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppVersionsRequest)`  
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
`[ListAppVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppVersionsResponse)` | The response received from the server.  
  
### ListAppVersionsAsync(ListAppVersionsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListAppVersionsResponse> ListAppVersionsAsync(ListAppVersionsRequest request, CallOptions options)

Lists all app versions in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAppVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppVersionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAppVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppVersionsResponse)` | The call object.  
  
### ListAppVersionsAsync(ListAppVersionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListAppVersionsResponse> ListAppVersionsAsync(ListAppVersionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all app versions in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAppVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppVersionsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAppVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppVersionsResponse)` | The call object.  
  
### ListApps(ListAppsRequest, CallOptions)
    
    
    public virtual ListAppsResponse ListApps(ListAppsRequest request, CallOptions options)

Lists apps in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAppsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAppsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppsResponse)` | The response received from the server.  
  
### ListApps(ListAppsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListAppsResponse ListApps(ListAppsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists apps in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAppsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppsRequest)`  
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
`[ListAppsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppsResponse)` | The response received from the server.  
  
### ListAppsAsync(ListAppsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListAppsResponse> ListAppsAsync(ListAppsRequest request, CallOptions options)

Lists apps in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAppsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAppsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppsResponse)` | The call object.  
  
### ListAppsAsync(ListAppsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListAppsResponse> ListAppsAsync(ListAppsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists apps in the given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAppsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAppsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppsResponse)` | The call object.  
  
### ListChangelogs(ListChangelogsRequest, CallOptions)
    
    
    public virtual ListChangelogsResponse ListChangelogs(ListChangelogsRequest request, CallOptions options)

Lists the changelogs of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListChangelogsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListChangelogsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListChangelogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListChangelogsResponse)` | The response received from the server.  
  
### ListChangelogs(ListChangelogsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListChangelogsResponse ListChangelogs(ListChangelogsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists the changelogs of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListChangelogsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListChangelogsRequest)`  
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
`[ListChangelogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListChangelogsResponse)` | The response received from the server.  
  
### ListChangelogsAsync(ListChangelogsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListChangelogsResponse> ListChangelogsAsync(ListChangelogsRequest request, CallOptions options)

Lists the changelogs of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListChangelogsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListChangelogsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListChangelogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListChangelogsResponse)` | The call object.  
  
### ListChangelogsAsync(ListChangelogsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListChangelogsResponse> ListChangelogsAsync(ListChangelogsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists the changelogs of the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListChangelogsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListChangelogsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListChangelogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListChangelogsResponse)` | The call object.  
  
### ListConversations(ListConversationsRequest, CallOptions)
    
    
    public virtual ListConversationsResponse ListConversations(ListConversationsRequest request, CallOptions options)

Lists conversations in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListConversationsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListConversationsResponse)` | The response received from the server.  
  
### ListConversations(ListConversationsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListConversationsResponse ListConversations(ListConversationsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists conversations in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListConversationsRequest)`  
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
`[ListConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListConversationsResponse)` | The response received from the server.  
  
### ListConversationsAsync(ListConversationsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListConversationsResponse> ListConversationsAsync(ListConversationsRequest request, CallOptions options)

Lists conversations in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListConversationsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListConversationsResponse)` | The call object.  
  
### ListConversationsAsync(ListConversationsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListConversationsResponse> ListConversationsAsync(ListConversationsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists conversations in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListConversationsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListConversationsResponse)` | The call object.  
  
### ListDeployments(ListDeploymentsRequest, CallOptions)
    
    
    public virtual ListDeploymentsResponse ListDeployments(ListDeploymentsRequest request, CallOptions options)

Lists deployments in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListDeploymentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListDeploymentsResponse)` | The response received from the server.  
  
### ListDeployments(ListDeploymentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListDeploymentsResponse ListDeployments(ListDeploymentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists deployments in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListDeploymentsRequest)`  
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
`[ListDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListDeploymentsResponse)` | The response received from the server.  
  
### ListDeploymentsAsync(ListDeploymentsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListDeploymentsResponse> ListDeploymentsAsync(ListDeploymentsRequest request, CallOptions options)

Lists deployments in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListDeploymentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListDeploymentsResponse)` | The call object.  
  
### ListDeploymentsAsync(ListDeploymentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListDeploymentsResponse> ListDeploymentsAsync(ListDeploymentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists deployments in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListDeploymentsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListDeploymentsResponse)` | The call object.  
  
### ListExamples(ListExamplesRequest, CallOptions)
    
    
    public virtual ListExamplesResponse ListExamples(ListExamplesRequest request, CallOptions options)

Lists examples in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExamplesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListExamplesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListExamplesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListExamplesResponse)` | The response received from the server.  
  
### ListExamples(ListExamplesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListExamplesResponse ListExamples(ListExamplesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists examples in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExamplesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListExamplesRequest)`  
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
`[ListExamplesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListExamplesResponse)` | The response received from the server.  
  
### ListExamplesAsync(ListExamplesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListExamplesResponse> ListExamplesAsync(ListExamplesRequest request, CallOptions options)

Lists examples in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExamplesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListExamplesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListExamplesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListExamplesResponse)` | The call object.  
  
### ListExamplesAsync(ListExamplesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListExamplesResponse> ListExamplesAsync(ListExamplesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists examples in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExamplesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListExamplesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListExamplesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListExamplesResponse)` | The call object.  
  
### ListGuardrails(ListGuardrailsRequest, CallOptions)
    
    
    public virtual ListGuardrailsResponse ListGuardrails(ListGuardrailsRequest request, CallOptions options)

Lists guardrails in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGuardrailsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListGuardrailsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListGuardrailsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListGuardrailsResponse)` | The response received from the server.  
  
### ListGuardrails(ListGuardrailsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListGuardrailsResponse ListGuardrails(ListGuardrailsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists guardrails in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGuardrailsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListGuardrailsRequest)`  
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
`[ListGuardrailsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListGuardrailsResponse)` | The response received from the server.  
  
### ListGuardrailsAsync(ListGuardrailsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListGuardrailsResponse> ListGuardrailsAsync(ListGuardrailsRequest request, CallOptions options)

Lists guardrails in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGuardrailsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListGuardrailsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGuardrailsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListGuardrailsResponse)` | The call object.  
  
### ListGuardrailsAsync(ListGuardrailsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListGuardrailsResponse> ListGuardrailsAsync(ListGuardrailsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists guardrails in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGuardrailsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListGuardrailsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGuardrailsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListGuardrailsResponse)` | The call object.  
  
### ListTools(ListToolsRequest, CallOptions)
    
    
    public virtual ListToolsResponse ListTools(ListToolsRequest request, CallOptions options)

Lists tools in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListToolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListToolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsResponse)` | The response received from the server.  
  
### ListTools(ListToolsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListToolsResponse ListTools(ListToolsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists tools in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListToolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsRequest)`  
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
`[ListToolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsResponse)` | The response received from the server.  
  
### ListToolsAsync(ListToolsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListToolsResponse> ListToolsAsync(ListToolsRequest request, CallOptions options)

Lists tools in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListToolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListToolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsResponse)` | The call object.  
  
### ListToolsAsync(ListToolsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListToolsResponse> ListToolsAsync(ListToolsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists tools in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListToolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListToolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsResponse)` | The call object.  
  
### ListToolsets(ListToolsetsRequest, CallOptions)
    
    
    public virtual ListToolsetsResponse ListToolsets(ListToolsetsRequest request, CallOptions options)

Lists toolsets in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListToolsetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsetsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListToolsetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsetsResponse)` | The response received from the server.  
  
### ListToolsets(ListToolsetsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListToolsetsResponse ListToolsets(ListToolsetsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists toolsets in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListToolsetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsetsRequest)`  
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
`[ListToolsetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsetsResponse)` | The response received from the server.  
  
### ListToolsetsAsync(ListToolsetsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListToolsetsResponse> ListToolsetsAsync(ListToolsetsRequest request, CallOptions options)

Lists toolsets in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListToolsetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsetsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListToolsetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsetsResponse)` | The call object.  
  
### ListToolsetsAsync(ListToolsetsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListToolsetsResponse> ListToolsetsAsync(ListToolsetsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists toolsets in the given app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListToolsetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsetsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListToolsetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsetsResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override AgentService.AgentServiceClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AgentService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentService)[AgentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentService.AgentServiceClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Ces.V1Beta.AgentService.AgentServiceClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### RestoreAppVersion(RestoreAppVersionRequest, CallOptions)
    
    
    public virtual Operation RestoreAppVersion(RestoreAppVersionRequest request, CallOptions options)

Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### RestoreAppVersion(RestoreAppVersionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation RestoreAppVersion(RestoreAppVersionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionRequest)`  
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
  
### RestoreAppVersionAsync(RestoreAppVersionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> RestoreAppVersionAsync(RestoreAppVersionRequest request, CallOptions options)

Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### RestoreAppVersionAsync(RestoreAppVersionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> RestoreAppVersionAsync(RestoreAppVersionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionRequest)`  
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
  
### UpdateAgent(UpdateAgentRequest, CallOptions)
    
    
    public virtual Agent UpdateAgent(UpdateAgentRequest request, CallOptions options)

Updates the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateAgentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The response received from the server.  
  
### UpdateAgent(UpdateAgentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Agent UpdateAgent(UpdateAgentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateAgentRequest)`  
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
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The response received from the server.  
  
### UpdateAgentAsync(UpdateAgentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Agent> UpdateAgentAsync(UpdateAgentRequest request, CallOptions options)

Updates the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateAgentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The call object.  
  
### UpdateAgentAsync(UpdateAgentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Agent> UpdateAgentAsync(UpdateAgentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateAgentRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)` | The call object.  
  
### UpdateApp(UpdateAppRequest, CallOptions)
    
    
    public virtual App UpdateApp(UpdateAppRequest request, CallOptions options)

Updates the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateAppRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | The response received from the server.  
  
### UpdateApp(UpdateAppRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual App UpdateApp(UpdateAppRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateAppRequest)`  
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
`[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | The response received from the server.  
  
### UpdateAppAsync(UpdateAppRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<App> UpdateAppAsync(UpdateAppRequest request, CallOptions options)

Updates the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateAppRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | The call object.  
  
### UpdateAppAsync(UpdateAppRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<App> UpdateAppAsync(UpdateAppRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the specified app.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateAppRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)` | The call object.  
  
### UpdateDeployment(UpdateDeploymentRequest, CallOptions)
    
    
    public virtual Deployment UpdateDeployment(UpdateDeploymentRequest request, CallOptions options)

Updates the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The response received from the server.  
  
### UpdateDeployment(UpdateDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Deployment UpdateDeployment(UpdateDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateDeploymentRequest)`  
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
`[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The response received from the server.  
  
### UpdateDeploymentAsync(UpdateDeploymentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Deployment> UpdateDeploymentAsync(UpdateDeploymentRequest request, CallOptions options)

Updates the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateDeploymentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The call object.  
  
### UpdateDeploymentAsync(UpdateDeploymentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Deployment> UpdateDeploymentAsync(UpdateDeploymentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the specified deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateDeploymentRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)` | The call object.  
  
### UpdateExample(UpdateExampleRequest, CallOptions)
    
    
    public virtual Example UpdateExample(UpdateExampleRequest request, CallOptions options)

Updates the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateExampleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The response received from the server.  
  
### UpdateExample(UpdateExampleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Example UpdateExample(UpdateExampleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateExampleRequest)`  
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
`[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The response received from the server.  
  
### UpdateExampleAsync(UpdateExampleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Example> UpdateExampleAsync(UpdateExampleRequest request, CallOptions options)

Updates the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateExampleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The call object.  
  
### UpdateExampleAsync(UpdateExampleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Example> UpdateExampleAsync(UpdateExampleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the specified example.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateExampleRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)` | The call object.  
  
### UpdateGuardrail(UpdateGuardrailRequest, CallOptions)
    
    
    public virtual Guardrail UpdateGuardrail(UpdateGuardrailRequest request, CallOptions options)

Updates the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateGuardrailRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The response received from the server.  
  
### UpdateGuardrail(UpdateGuardrailRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Guardrail UpdateGuardrail(UpdateGuardrailRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateGuardrailRequest)`  
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
`[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The response received from the server.  
  
### UpdateGuardrailAsync(UpdateGuardrailRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Guardrail> UpdateGuardrailAsync(UpdateGuardrailRequest request, CallOptions options)

Updates the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateGuardrailRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The call object.  
  
### UpdateGuardrailAsync(UpdateGuardrailRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Guardrail> UpdateGuardrailAsync(UpdateGuardrailRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the specified guardrail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateGuardrailRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)` | The call object.  
  
### UpdateSecuritySettings(UpdateSecuritySettingsRequest, CallOptions)
    
    
    public virtual SecuritySettings UpdateSecuritySettings(UpdateSecuritySettingsRequest request, CallOptions options)

Updates the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateSecuritySettingsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | The response received from the server.  
  
### UpdateSecuritySettings(UpdateSecuritySettingsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual SecuritySettings UpdateSecuritySettings(UpdateSecuritySettingsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateSecuritySettingsRequest)`  
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
`[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | The response received from the server.  
  
### UpdateSecuritySettingsAsync(UpdateSecuritySettingsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<SecuritySettings> UpdateSecuritySettingsAsync(UpdateSecuritySettingsRequest request, CallOptions options)

Updates the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateSecuritySettingsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | The call object.  
  
### UpdateSecuritySettingsAsync(UpdateSecuritySettingsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<SecuritySettings> UpdateSecuritySettingsAsync(UpdateSecuritySettingsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the security settings for the project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateSecuritySettingsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)` | The call object.  
  
### UpdateTool(UpdateToolRequest, CallOptions)
    
    
    public virtual Tool UpdateTool(UpdateToolRequest request, CallOptions options)

Updates the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateToolRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The response received from the server.  
  
### UpdateTool(UpdateToolRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Tool UpdateTool(UpdateToolRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateToolRequest)`  
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
`[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The response received from the server.  
  
### UpdateToolAsync(UpdateToolRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Tool> UpdateToolAsync(UpdateToolRequest request, CallOptions options)

Updates the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateToolRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The call object.  
  
### UpdateToolAsync(UpdateToolRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Tool> UpdateToolAsync(UpdateToolRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the specified tool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateToolRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)` | The call object.  
  
### UpdateToolset(UpdateToolsetRequest, CallOptions)
    
    
    public virtual Toolset UpdateToolset(UpdateToolsetRequest request, CallOptions options)

Updates the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateToolsetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The response received from the server.  
  
### UpdateToolset(UpdateToolsetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Toolset UpdateToolset(UpdateToolsetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateToolsetRequest)`  
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
`[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The response received from the server.  
  
### UpdateToolsetAsync(UpdateToolsetRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Toolset> UpdateToolsetAsync(UpdateToolsetRequest request, CallOptions options)

Updates the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateToolsetRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The call object.  
  
### UpdateToolsetAsync(UpdateToolsetRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Toolset> UpdateToolsetAsync(UpdateToolsetRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the specified toolset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateToolsetRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
