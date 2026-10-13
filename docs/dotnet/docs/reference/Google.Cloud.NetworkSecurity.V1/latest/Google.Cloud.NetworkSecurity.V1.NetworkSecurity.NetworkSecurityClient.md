---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.NetworkSecurity.NetworkSecurityClient
title: Network Security v1 API - Class NetworkSecurity.NetworkSecurityClient (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:29.943657+00:00
---

# Network Security v1 API - Class NetworkSecurity.NetworkSecurityClient (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.NetworkSecurity.NetworkSecurityClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Security v1 API - Class NetworkSecurity.NetworkSecurityClient (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class NetworkSecurity.NetworkSecurityClient : ClientBase<NetworkSecurity.NetworkSecurityClient>

Reference documentation and code samples for the Network Security v1 API class NetworkSecurity.NetworkSecurityClient.

Client for NetworkSecurity

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[NetworkSecurity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.NetworkSecurity)[NetworkSecurityClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.NetworkSecurity.NetworkSecurityClient) > NetworkSecurity.NetworkSecurityClient

## Inherited Members

[ClientBase<NetworkSecurity.NetworkSecurityClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkSecurity.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1)

## Assembly

Google.Cloud.NetworkSecurity.V1.dll

## Constructors 

### NetworkSecurityClient()
    
    
    protected NetworkSecurityClient()

Protected parameterless constructor to allow creation of test doubles.

### NetworkSecurityClient(CallInvoker)
    
    
    public NetworkSecurityClient(CallInvoker callInvoker)

Creates a new client for NetworkSecurity that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### NetworkSecurityClient(ChannelBase)
    
    
    public NetworkSecurityClient(ChannelBase channel)

Creates a new client for NetworkSecurity

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### NetworkSecurityClient(ClientBaseConfiguration)
    
    
    protected NetworkSecurityClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### CreateAuthorizationPolicy(CreateAuthorizationPolicyRequest, CallOptions)
    
    
    public virtual Operation CreateAuthorizationPolicy(CreateAuthorizationPolicyRequest request, CallOptions options)

Creates a new AuthorizationPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAuthorizationPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateAuthorizationPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateAuthorizationPolicy(CreateAuthorizationPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateAuthorizationPolicy(CreateAuthorizationPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new AuthorizationPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAuthorizationPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateAuthorizationPolicyRequest)`  
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
  
### CreateAuthorizationPolicyAsync(CreateAuthorizationPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateAuthorizationPolicyAsync(CreateAuthorizationPolicyRequest request, CallOptions options)

Creates a new AuthorizationPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAuthorizationPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateAuthorizationPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateAuthorizationPolicyAsync(CreateAuthorizationPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateAuthorizationPolicyAsync(CreateAuthorizationPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new AuthorizationPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAuthorizationPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateAuthorizationPolicyRequest)`  
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
  
### CreateAuthzPolicy(CreateAuthzPolicyRequest, CallOptions)
    
    
    public virtual Operation CreateAuthzPolicy(CreateAuthzPolicyRequest request, CallOptions options)

Creates a new AuthzPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAuthzPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateAuthzPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateAuthzPolicy(CreateAuthzPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateAuthzPolicy(CreateAuthzPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new AuthzPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAuthzPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateAuthzPolicyRequest)`  
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
  
### CreateAuthzPolicyAsync(CreateAuthzPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateAuthzPolicyAsync(CreateAuthzPolicyRequest request, CallOptions options)

Creates a new AuthzPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAuthzPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateAuthzPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateAuthzPolicyAsync(CreateAuthzPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateAuthzPolicyAsync(CreateAuthzPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new AuthzPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAuthzPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateAuthzPolicyRequest)`  
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
  
### CreateBackendAuthenticationConfig(CreateBackendAuthenticationConfigRequest, CallOptions)
    
    
    public virtual Operation CreateBackendAuthenticationConfig(CreateBackendAuthenticationConfigRequest request, CallOptions options)

Creates a new BackendAuthenticationConfig in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBackendAuthenticationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateBackendAuthenticationConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateBackendAuthenticationConfig(CreateBackendAuthenticationConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateBackendAuthenticationConfig(CreateBackendAuthenticationConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new BackendAuthenticationConfig in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBackendAuthenticationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateBackendAuthenticationConfigRequest)`  
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
  
### CreateBackendAuthenticationConfigAsync(CreateBackendAuthenticationConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateBackendAuthenticationConfigAsync(CreateBackendAuthenticationConfigRequest request, CallOptions options)

Creates a new BackendAuthenticationConfig in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBackendAuthenticationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateBackendAuthenticationConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateBackendAuthenticationConfigAsync(CreateBackendAuthenticationConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateBackendAuthenticationConfigAsync(CreateBackendAuthenticationConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new BackendAuthenticationConfig in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBackendAuthenticationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateBackendAuthenticationConfigRequest)`  
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
  
### CreateClientTlsPolicy(CreateClientTlsPolicyRequest, CallOptions)
    
    
    public virtual Operation CreateClientTlsPolicy(CreateClientTlsPolicyRequest request, CallOptions options)

Creates a new ClientTlsPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateClientTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateClientTlsPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateClientTlsPolicy(CreateClientTlsPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateClientTlsPolicy(CreateClientTlsPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new ClientTlsPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateClientTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateClientTlsPolicyRequest)`  
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
  
### CreateClientTlsPolicyAsync(CreateClientTlsPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateClientTlsPolicyAsync(CreateClientTlsPolicyRequest request, CallOptions options)

Creates a new ClientTlsPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateClientTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateClientTlsPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateClientTlsPolicyAsync(CreateClientTlsPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateClientTlsPolicyAsync(CreateClientTlsPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new ClientTlsPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateClientTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateClientTlsPolicyRequest)`  
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
  
### CreateGatewaySecurityPolicy(CreateGatewaySecurityPolicyRequest, CallOptions)
    
    
    public virtual Operation CreateGatewaySecurityPolicy(CreateGatewaySecurityPolicyRequest request, CallOptions options)

Creates a new GatewaySecurityPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGatewaySecurityPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateGatewaySecurityPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateGatewaySecurityPolicy(CreateGatewaySecurityPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateGatewaySecurityPolicy(CreateGatewaySecurityPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new GatewaySecurityPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGatewaySecurityPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateGatewaySecurityPolicyRequest)`  
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
  
### CreateGatewaySecurityPolicyAsync(CreateGatewaySecurityPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateGatewaySecurityPolicyAsync(CreateGatewaySecurityPolicyRequest request, CallOptions options)

Creates a new GatewaySecurityPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGatewaySecurityPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateGatewaySecurityPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateGatewaySecurityPolicyAsync(CreateGatewaySecurityPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateGatewaySecurityPolicyAsync(CreateGatewaySecurityPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new GatewaySecurityPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGatewaySecurityPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateGatewaySecurityPolicyRequest)`  
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
  
### CreateGatewaySecurityPolicyRule(CreateGatewaySecurityPolicyRuleRequest, CallOptions)
    
    
    public virtual Operation CreateGatewaySecurityPolicyRule(CreateGatewaySecurityPolicyRuleRequest request, CallOptions options)

Creates a new GatewaySecurityPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateGatewaySecurityPolicyRuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateGatewaySecurityPolicyRule(CreateGatewaySecurityPolicyRuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateGatewaySecurityPolicyRule(CreateGatewaySecurityPolicyRuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new GatewaySecurityPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateGatewaySecurityPolicyRuleRequest)`  
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
  
### CreateGatewaySecurityPolicyRuleAsync(CreateGatewaySecurityPolicyRuleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateGatewaySecurityPolicyRuleAsync(CreateGatewaySecurityPolicyRuleRequest request, CallOptions options)

Creates a new GatewaySecurityPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateGatewaySecurityPolicyRuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateGatewaySecurityPolicyRuleAsync(CreateGatewaySecurityPolicyRuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateGatewaySecurityPolicyRuleAsync(CreateGatewaySecurityPolicyRuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new GatewaySecurityPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateGatewaySecurityPolicyRuleRequest)`  
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
  
### CreateServerTlsPolicy(CreateServerTlsPolicyRequest, CallOptions)
    
    
    public virtual Operation CreateServerTlsPolicy(CreateServerTlsPolicyRequest request, CallOptions options)

Creates a new ServerTlsPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServerTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateServerTlsPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateServerTlsPolicy(CreateServerTlsPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateServerTlsPolicy(CreateServerTlsPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new ServerTlsPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServerTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateServerTlsPolicyRequest)`  
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
  
### CreateServerTlsPolicyAsync(CreateServerTlsPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateServerTlsPolicyAsync(CreateServerTlsPolicyRequest request, CallOptions options)

Creates a new ServerTlsPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServerTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateServerTlsPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateServerTlsPolicyAsync(CreateServerTlsPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateServerTlsPolicyAsync(CreateServerTlsPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new ServerTlsPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServerTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateServerTlsPolicyRequest)`  
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
  
### CreateTlsInspectionPolicy(CreateTlsInspectionPolicyRequest, CallOptions)
    
    
    public virtual Operation CreateTlsInspectionPolicy(CreateTlsInspectionPolicyRequest request, CallOptions options)

Creates a new TlsInspectionPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTlsInspectionPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateTlsInspectionPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateTlsInspectionPolicy(CreateTlsInspectionPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateTlsInspectionPolicy(CreateTlsInspectionPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new TlsInspectionPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTlsInspectionPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateTlsInspectionPolicyRequest)`  
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
  
### CreateTlsInspectionPolicyAsync(CreateTlsInspectionPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateTlsInspectionPolicyAsync(CreateTlsInspectionPolicyRequest request, CallOptions options)

Creates a new TlsInspectionPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTlsInspectionPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateTlsInspectionPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateTlsInspectionPolicyAsync(CreateTlsInspectionPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateTlsInspectionPolicyAsync(CreateTlsInspectionPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new TlsInspectionPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTlsInspectionPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateTlsInspectionPolicyRequest)`  
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
  
### CreateUrlList(CreateUrlListRequest, CallOptions)
    
    
    public virtual Operation CreateUrlList(CreateUrlListRequest request, CallOptions options)

Creates a new UrlList in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUrlListRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateUrlListRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateUrlList(CreateUrlListRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateUrlList(CreateUrlListRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new UrlList in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUrlListRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateUrlListRequest)`  
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
  
### CreateUrlListAsync(CreateUrlListRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateUrlListAsync(CreateUrlListRequest request, CallOptions options)

Creates a new UrlList in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUrlListRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateUrlListRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateUrlListAsync(CreateUrlListRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateUrlListAsync(CreateUrlListRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new UrlList in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUrlListRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateUrlListRequest)`  
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
  
### DeleteAuthorizationPolicy(DeleteAuthorizationPolicyRequest, CallOptions)
    
    
    public virtual Operation DeleteAuthorizationPolicy(DeleteAuthorizationPolicyRequest request, CallOptions options)

Deletes a single AuthorizationPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthorizationPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteAuthorizationPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteAuthorizationPolicy(DeleteAuthorizationPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteAuthorizationPolicy(DeleteAuthorizationPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single AuthorizationPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthorizationPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteAuthorizationPolicyRequest)`  
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
  
### DeleteAuthorizationPolicyAsync(DeleteAuthorizationPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteAuthorizationPolicyAsync(DeleteAuthorizationPolicyRequest request, CallOptions options)

Deletes a single AuthorizationPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthorizationPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteAuthorizationPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteAuthorizationPolicyAsync(DeleteAuthorizationPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteAuthorizationPolicyAsync(DeleteAuthorizationPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single AuthorizationPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthorizationPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteAuthorizationPolicyRequest)`  
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
  
### DeleteAuthzPolicy(DeleteAuthzPolicyRequest, CallOptions)
    
    
    public virtual Operation DeleteAuthzPolicy(DeleteAuthzPolicyRequest request, CallOptions options)

Deletes a single AuthzPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthzPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteAuthzPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteAuthzPolicy(DeleteAuthzPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteAuthzPolicy(DeleteAuthzPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single AuthzPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthzPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteAuthzPolicyRequest)`  
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
  
### DeleteAuthzPolicyAsync(DeleteAuthzPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteAuthzPolicyAsync(DeleteAuthzPolicyRequest request, CallOptions options)

Deletes a single AuthzPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthzPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteAuthzPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteAuthzPolicyAsync(DeleteAuthzPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteAuthzPolicyAsync(DeleteAuthzPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single AuthzPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthzPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteAuthzPolicyRequest)`  
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
  
### DeleteBackendAuthenticationConfig(DeleteBackendAuthenticationConfigRequest, CallOptions)
    
    
    public virtual Operation DeleteBackendAuthenticationConfig(DeleteBackendAuthenticationConfigRequest request, CallOptions options)

Deletes a single BackendAuthenticationConfig to BackendAuthenticationConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackendAuthenticationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteBackendAuthenticationConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteBackendAuthenticationConfig(DeleteBackendAuthenticationConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteBackendAuthenticationConfig(DeleteBackendAuthenticationConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single BackendAuthenticationConfig to BackendAuthenticationConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackendAuthenticationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteBackendAuthenticationConfigRequest)`  
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
  
### DeleteBackendAuthenticationConfigAsync(DeleteBackendAuthenticationConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteBackendAuthenticationConfigAsync(DeleteBackendAuthenticationConfigRequest request, CallOptions options)

Deletes a single BackendAuthenticationConfig to BackendAuthenticationConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackendAuthenticationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteBackendAuthenticationConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteBackendAuthenticationConfigAsync(DeleteBackendAuthenticationConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteBackendAuthenticationConfigAsync(DeleteBackendAuthenticationConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single BackendAuthenticationConfig to BackendAuthenticationConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackendAuthenticationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteBackendAuthenticationConfigRequest)`  
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
  
### DeleteClientTlsPolicy(DeleteClientTlsPolicyRequest, CallOptions)
    
    
    public virtual Operation DeleteClientTlsPolicy(DeleteClientTlsPolicyRequest request, CallOptions options)

Deletes a single ClientTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteClientTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteClientTlsPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteClientTlsPolicy(DeleteClientTlsPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteClientTlsPolicy(DeleteClientTlsPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single ClientTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteClientTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteClientTlsPolicyRequest)`  
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
  
### DeleteClientTlsPolicyAsync(DeleteClientTlsPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteClientTlsPolicyAsync(DeleteClientTlsPolicyRequest request, CallOptions options)

Deletes a single ClientTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteClientTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteClientTlsPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteClientTlsPolicyAsync(DeleteClientTlsPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteClientTlsPolicyAsync(DeleteClientTlsPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single ClientTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteClientTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteClientTlsPolicyRequest)`  
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
  
### DeleteGatewaySecurityPolicy(DeleteGatewaySecurityPolicyRequest, CallOptions)
    
    
    public virtual Operation DeleteGatewaySecurityPolicy(DeleteGatewaySecurityPolicyRequest request, CallOptions options)

Deletes a single GatewaySecurityPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGatewaySecurityPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteGatewaySecurityPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteGatewaySecurityPolicy(DeleteGatewaySecurityPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteGatewaySecurityPolicy(DeleteGatewaySecurityPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single GatewaySecurityPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGatewaySecurityPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteGatewaySecurityPolicyRequest)`  
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
  
### DeleteGatewaySecurityPolicyAsync(DeleteGatewaySecurityPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteGatewaySecurityPolicyAsync(DeleteGatewaySecurityPolicyRequest request, CallOptions options)

Deletes a single GatewaySecurityPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGatewaySecurityPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteGatewaySecurityPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteGatewaySecurityPolicyAsync(DeleteGatewaySecurityPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteGatewaySecurityPolicyAsync(DeleteGatewaySecurityPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single GatewaySecurityPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGatewaySecurityPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteGatewaySecurityPolicyRequest)`  
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
  
### DeleteGatewaySecurityPolicyRule(DeleteGatewaySecurityPolicyRuleRequest, CallOptions)
    
    
    public virtual Operation DeleteGatewaySecurityPolicyRule(DeleteGatewaySecurityPolicyRuleRequest request, CallOptions options)

Deletes a single GatewaySecurityPolicyRule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteGatewaySecurityPolicyRuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteGatewaySecurityPolicyRule(DeleteGatewaySecurityPolicyRuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteGatewaySecurityPolicyRule(DeleteGatewaySecurityPolicyRuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single GatewaySecurityPolicyRule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteGatewaySecurityPolicyRuleRequest)`  
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
  
### DeleteGatewaySecurityPolicyRuleAsync(DeleteGatewaySecurityPolicyRuleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteGatewaySecurityPolicyRuleAsync(DeleteGatewaySecurityPolicyRuleRequest request, CallOptions options)

Deletes a single GatewaySecurityPolicyRule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteGatewaySecurityPolicyRuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteGatewaySecurityPolicyRuleAsync(DeleteGatewaySecurityPolicyRuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteGatewaySecurityPolicyRuleAsync(DeleteGatewaySecurityPolicyRuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single GatewaySecurityPolicyRule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteGatewaySecurityPolicyRuleRequest)`  
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
  
### DeleteServerTlsPolicy(DeleteServerTlsPolicyRequest, CallOptions)
    
    
    public virtual Operation DeleteServerTlsPolicy(DeleteServerTlsPolicyRequest request, CallOptions options)

Deletes a single ServerTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServerTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteServerTlsPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteServerTlsPolicy(DeleteServerTlsPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteServerTlsPolicy(DeleteServerTlsPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single ServerTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServerTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteServerTlsPolicyRequest)`  
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
  
### DeleteServerTlsPolicyAsync(DeleteServerTlsPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteServerTlsPolicyAsync(DeleteServerTlsPolicyRequest request, CallOptions options)

Deletes a single ServerTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServerTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteServerTlsPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteServerTlsPolicyAsync(DeleteServerTlsPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteServerTlsPolicyAsync(DeleteServerTlsPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single ServerTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServerTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteServerTlsPolicyRequest)`  
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
  
### DeleteTlsInspectionPolicy(DeleteTlsInspectionPolicyRequest, CallOptions)
    
    
    public virtual Operation DeleteTlsInspectionPolicy(DeleteTlsInspectionPolicyRequest request, CallOptions options)

Deletes a single TlsInspectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTlsInspectionPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteTlsInspectionPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteTlsInspectionPolicy(DeleteTlsInspectionPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteTlsInspectionPolicy(DeleteTlsInspectionPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single TlsInspectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTlsInspectionPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteTlsInspectionPolicyRequest)`  
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
  
### DeleteTlsInspectionPolicyAsync(DeleteTlsInspectionPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteTlsInspectionPolicyAsync(DeleteTlsInspectionPolicyRequest request, CallOptions options)

Deletes a single TlsInspectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTlsInspectionPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteTlsInspectionPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteTlsInspectionPolicyAsync(DeleteTlsInspectionPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteTlsInspectionPolicyAsync(DeleteTlsInspectionPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single TlsInspectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTlsInspectionPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteTlsInspectionPolicyRequest)`  
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
  
### DeleteUrlList(DeleteUrlListRequest, CallOptions)
    
    
    public virtual Operation DeleteUrlList(DeleteUrlListRequest request, CallOptions options)

Deletes a single UrlList.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUrlListRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteUrlListRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteUrlList(DeleteUrlListRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteUrlList(DeleteUrlListRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single UrlList.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUrlListRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteUrlListRequest)`  
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
  
### DeleteUrlListAsync(DeleteUrlListRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteUrlListAsync(DeleteUrlListRequest request, CallOptions options)

Deletes a single UrlList.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUrlListRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteUrlListRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteUrlListAsync(DeleteUrlListRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteUrlListAsync(DeleteUrlListRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single UrlList.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUrlListRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.DeleteUrlListRequest)`  
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
  
### GetAuthorizationPolicy(GetAuthorizationPolicyRequest, CallOptions)
    
    
    public virtual AuthorizationPolicy GetAuthorizationPolicy(GetAuthorizationPolicyRequest request, CallOptions options)

Gets details of a single AuthorizationPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAuthorizationPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetAuthorizationPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AuthorizationPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.AuthorizationPolicy)` | The response received from the server.  
  
### GetAuthorizationPolicy(GetAuthorizationPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AuthorizationPolicy GetAuthorizationPolicy(GetAuthorizationPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single AuthorizationPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAuthorizationPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetAuthorizationPolicyRequest)`  
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
`[AuthorizationPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.AuthorizationPolicy)` | The response received from the server.  
  
### GetAuthorizationPolicyAsync(GetAuthorizationPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<AuthorizationPolicy> GetAuthorizationPolicyAsync(GetAuthorizationPolicyRequest request, CallOptions options)

Gets details of a single AuthorizationPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAuthorizationPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetAuthorizationPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AuthorizationPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.AuthorizationPolicy)` | The call object.  
  
### GetAuthorizationPolicyAsync(GetAuthorizationPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<AuthorizationPolicy> GetAuthorizationPolicyAsync(GetAuthorizationPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single AuthorizationPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAuthorizationPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetAuthorizationPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AuthorizationPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.AuthorizationPolicy)` | The call object.  
  
### GetAuthzPolicy(GetAuthzPolicyRequest, CallOptions)
    
    
    public virtual AuthzPolicy GetAuthzPolicy(GetAuthzPolicyRequest request, CallOptions options)

Gets details of a single AuthzPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAuthzPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetAuthzPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AuthzPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.AuthzPolicy)` | The response received from the server.  
  
### GetAuthzPolicy(GetAuthzPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AuthzPolicy GetAuthzPolicy(GetAuthzPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single AuthzPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAuthzPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetAuthzPolicyRequest)`  
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
`[AuthzPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.AuthzPolicy)` | The response received from the server.  
  
### GetAuthzPolicyAsync(GetAuthzPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<AuthzPolicy> GetAuthzPolicyAsync(GetAuthzPolicyRequest request, CallOptions options)

Gets details of a single AuthzPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAuthzPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetAuthzPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AuthzPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.AuthzPolicy)` | The call object.  
  
### GetAuthzPolicyAsync(GetAuthzPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<AuthzPolicy> GetAuthzPolicyAsync(GetAuthzPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single AuthzPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAuthzPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetAuthzPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AuthzPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.AuthzPolicy)` | The call object.  
  
### GetBackendAuthenticationConfig(GetBackendAuthenticationConfigRequest, CallOptions)
    
    
    public virtual BackendAuthenticationConfig GetBackendAuthenticationConfig(GetBackendAuthenticationConfigRequest request, CallOptions options)

Gets details of a single BackendAuthenticationConfig to BackendAuthenticationConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackendAuthenticationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetBackendAuthenticationConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[BackendAuthenticationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.BackendAuthenticationConfig)` | The response received from the server.  
  
### GetBackendAuthenticationConfig(GetBackendAuthenticationConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual BackendAuthenticationConfig GetBackendAuthenticationConfig(GetBackendAuthenticationConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single BackendAuthenticationConfig to BackendAuthenticationConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackendAuthenticationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetBackendAuthenticationConfigRequest)`  
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
`[BackendAuthenticationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.BackendAuthenticationConfig)` | The response received from the server.  
  
### GetBackendAuthenticationConfigAsync(GetBackendAuthenticationConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<BackendAuthenticationConfig> GetBackendAuthenticationConfigAsync(GetBackendAuthenticationConfigRequest request, CallOptions options)

Gets details of a single BackendAuthenticationConfig to BackendAuthenticationConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackendAuthenticationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetBackendAuthenticationConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BackendAuthenticationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.BackendAuthenticationConfig)` | The call object.  
  
### GetBackendAuthenticationConfigAsync(GetBackendAuthenticationConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<BackendAuthenticationConfig> GetBackendAuthenticationConfigAsync(GetBackendAuthenticationConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single BackendAuthenticationConfig to BackendAuthenticationConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackendAuthenticationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetBackendAuthenticationConfigRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BackendAuthenticationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.BackendAuthenticationConfig)` | The call object.  
  
### GetClientTlsPolicy(GetClientTlsPolicyRequest, CallOptions)
    
    
    public virtual ClientTlsPolicy GetClientTlsPolicy(GetClientTlsPolicyRequest request, CallOptions options)

Gets details of a single ClientTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClientTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetClientTlsPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ClientTlsPolicy)` | The response received from the server.  
  
### GetClientTlsPolicy(GetClientTlsPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ClientTlsPolicy GetClientTlsPolicy(GetClientTlsPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single ClientTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClientTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetClientTlsPolicyRequest)`  
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
`[ClientTlsPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ClientTlsPolicy)` | The response received from the server.  
  
### GetClientTlsPolicyAsync(GetClientTlsPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ClientTlsPolicy> GetClientTlsPolicyAsync(GetClientTlsPolicyRequest request, CallOptions options)

Gets details of a single ClientTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClientTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetClientTlsPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ClientTlsPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ClientTlsPolicy)` | The call object.  
  
### GetClientTlsPolicyAsync(GetClientTlsPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ClientTlsPolicy> GetClientTlsPolicyAsync(GetClientTlsPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single ClientTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClientTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetClientTlsPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ClientTlsPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ClientTlsPolicy)` | The call object.  
  
### GetGatewaySecurityPolicy(GetGatewaySecurityPolicyRequest, CallOptions)
    
    
    public virtual GatewaySecurityPolicy GetGatewaySecurityPolicy(GetGatewaySecurityPolicyRequest request, CallOptions options)

Gets details of a single GatewaySecurityPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGatewaySecurityPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetGatewaySecurityPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[GatewaySecurityPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GatewaySecurityPolicy)` | The response received from the server.  
  
### GetGatewaySecurityPolicy(GetGatewaySecurityPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual GatewaySecurityPolicy GetGatewaySecurityPolicy(GetGatewaySecurityPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single GatewaySecurityPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGatewaySecurityPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetGatewaySecurityPolicyRequest)`  
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
`[GatewaySecurityPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GatewaySecurityPolicy)` | The response received from the server.  
  
### GetGatewaySecurityPolicyAsync(GetGatewaySecurityPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<GatewaySecurityPolicy> GetGatewaySecurityPolicyAsync(GetGatewaySecurityPolicyRequest request, CallOptions options)

Gets details of a single GatewaySecurityPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGatewaySecurityPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetGatewaySecurityPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[GatewaySecurityPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GatewaySecurityPolicy)` | The call object.  
  
### GetGatewaySecurityPolicyAsync(GetGatewaySecurityPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<GatewaySecurityPolicy> GetGatewaySecurityPolicyAsync(GetGatewaySecurityPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single GatewaySecurityPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGatewaySecurityPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetGatewaySecurityPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[GatewaySecurityPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GatewaySecurityPolicy)` | The call object.  
  
### GetGatewaySecurityPolicyRule(GetGatewaySecurityPolicyRuleRequest, CallOptions)
    
    
    public virtual GatewaySecurityPolicyRule GetGatewaySecurityPolicyRule(GetGatewaySecurityPolicyRuleRequest request, CallOptions options)

Gets details of a single GatewaySecurityPolicyRule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetGatewaySecurityPolicyRuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[GatewaySecurityPolicyRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GatewaySecurityPolicyRule)` | The response received from the server.  
  
### GetGatewaySecurityPolicyRule(GetGatewaySecurityPolicyRuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual GatewaySecurityPolicyRule GetGatewaySecurityPolicyRule(GetGatewaySecurityPolicyRuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single GatewaySecurityPolicyRule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetGatewaySecurityPolicyRuleRequest)`  
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
`[GatewaySecurityPolicyRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GatewaySecurityPolicyRule)` | The response received from the server.  
  
### GetGatewaySecurityPolicyRuleAsync(GetGatewaySecurityPolicyRuleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<GatewaySecurityPolicyRule> GetGatewaySecurityPolicyRuleAsync(GetGatewaySecurityPolicyRuleRequest request, CallOptions options)

Gets details of a single GatewaySecurityPolicyRule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetGatewaySecurityPolicyRuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[GatewaySecurityPolicyRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GatewaySecurityPolicyRule)` | The call object.  
  
### GetGatewaySecurityPolicyRuleAsync(GetGatewaySecurityPolicyRuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<GatewaySecurityPolicyRule> GetGatewaySecurityPolicyRuleAsync(GetGatewaySecurityPolicyRuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single GatewaySecurityPolicyRule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetGatewaySecurityPolicyRuleRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[GatewaySecurityPolicyRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GatewaySecurityPolicyRule)` | The call object.  
  
### GetServerTlsPolicy(GetServerTlsPolicyRequest, CallOptions)
    
    
    public virtual ServerTlsPolicy GetServerTlsPolicy(GetServerTlsPolicyRequest request, CallOptions options)

Gets details of a single ServerTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServerTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetServerTlsPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ServerTlsPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ServerTlsPolicy)` | The response received from the server.  
  
### GetServerTlsPolicy(GetServerTlsPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ServerTlsPolicy GetServerTlsPolicy(GetServerTlsPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single ServerTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServerTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetServerTlsPolicyRequest)`  
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
`[ServerTlsPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ServerTlsPolicy)` | The response received from the server.  
  
### GetServerTlsPolicyAsync(GetServerTlsPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ServerTlsPolicy> GetServerTlsPolicyAsync(GetServerTlsPolicyRequest request, CallOptions options)

Gets details of a single ServerTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServerTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetServerTlsPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ServerTlsPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ServerTlsPolicy)` | The call object.  
  
### GetServerTlsPolicyAsync(GetServerTlsPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ServerTlsPolicy> GetServerTlsPolicyAsync(GetServerTlsPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single ServerTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServerTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetServerTlsPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ServerTlsPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ServerTlsPolicy)` | The call object.  
  
### GetTlsInspectionPolicy(GetTlsInspectionPolicyRequest, CallOptions)
    
    
    public virtual TlsInspectionPolicy GetTlsInspectionPolicy(GetTlsInspectionPolicyRequest request, CallOptions options)

Gets details of a single TlsInspectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTlsInspectionPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetTlsInspectionPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[TlsInspectionPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.TlsInspectionPolicy)` | The response received from the server.  
  
### GetTlsInspectionPolicy(GetTlsInspectionPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual TlsInspectionPolicy GetTlsInspectionPolicy(GetTlsInspectionPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single TlsInspectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTlsInspectionPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetTlsInspectionPolicyRequest)`  
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
`[TlsInspectionPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.TlsInspectionPolicy)` | The response received from the server.  
  
### GetTlsInspectionPolicyAsync(GetTlsInspectionPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<TlsInspectionPolicy> GetTlsInspectionPolicyAsync(GetTlsInspectionPolicyRequest request, CallOptions options)

Gets details of a single TlsInspectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTlsInspectionPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetTlsInspectionPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[TlsInspectionPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.TlsInspectionPolicy)` | The call object.  
  
### GetTlsInspectionPolicyAsync(GetTlsInspectionPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<TlsInspectionPolicy> GetTlsInspectionPolicyAsync(GetTlsInspectionPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single TlsInspectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTlsInspectionPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetTlsInspectionPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[TlsInspectionPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.TlsInspectionPolicy)` | The call object.  
  
### GetUrlList(GetUrlListRequest, CallOptions)
    
    
    public virtual UrlList GetUrlList(GetUrlListRequest request, CallOptions options)

Gets details of a single UrlList.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUrlListRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetUrlListRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[UrlList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UrlList)` | The response received from the server.  
  
### GetUrlList(GetUrlListRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual UrlList GetUrlList(GetUrlListRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single UrlList.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUrlListRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetUrlListRequest)`  
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
`[UrlList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UrlList)` | The response received from the server.  
  
### GetUrlListAsync(GetUrlListRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<UrlList> GetUrlListAsync(GetUrlListRequest request, CallOptions options)

Gets details of a single UrlList.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUrlListRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetUrlListRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[UrlList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UrlList)` | The call object.  
  
### GetUrlListAsync(GetUrlListRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<UrlList> GetUrlListAsync(GetUrlListRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single UrlList.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUrlListRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.GetUrlListRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[UrlList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UrlList)` | The call object.  
  
### ListAuthorizationPolicies(ListAuthorizationPoliciesRequest, CallOptions)
    
    
    public virtual ListAuthorizationPoliciesResponse ListAuthorizationPolicies(ListAuthorizationPoliciesRequest request, CallOptions options)

Lists AuthorizationPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAuthorizationPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListAuthorizationPoliciesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAuthorizationPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListAuthorizationPoliciesResponse)` | The response received from the server.  
  
### ListAuthorizationPolicies(ListAuthorizationPoliciesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListAuthorizationPoliciesResponse ListAuthorizationPolicies(ListAuthorizationPoliciesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists AuthorizationPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAuthorizationPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListAuthorizationPoliciesRequest)`  
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
`[ListAuthorizationPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListAuthorizationPoliciesResponse)` | The response received from the server.  
  
### ListAuthorizationPoliciesAsync(ListAuthorizationPoliciesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListAuthorizationPoliciesResponse> ListAuthorizationPoliciesAsync(ListAuthorizationPoliciesRequest request, CallOptions options)

Lists AuthorizationPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAuthorizationPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListAuthorizationPoliciesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAuthorizationPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListAuthorizationPoliciesResponse)` | The call object.  
  
### ListAuthorizationPoliciesAsync(ListAuthorizationPoliciesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListAuthorizationPoliciesResponse> ListAuthorizationPoliciesAsync(ListAuthorizationPoliciesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists AuthorizationPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAuthorizationPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListAuthorizationPoliciesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAuthorizationPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListAuthorizationPoliciesResponse)` | The call object.  
  
### ListAuthzPolicies(ListAuthzPoliciesRequest, CallOptions)
    
    
    public virtual ListAuthzPoliciesResponse ListAuthzPolicies(ListAuthzPoliciesRequest request, CallOptions options)

Lists AuthzPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAuthzPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListAuthzPoliciesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAuthzPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListAuthzPoliciesResponse)` | The response received from the server.  
  
### ListAuthzPolicies(ListAuthzPoliciesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListAuthzPoliciesResponse ListAuthzPolicies(ListAuthzPoliciesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists AuthzPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAuthzPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListAuthzPoliciesRequest)`  
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
`[ListAuthzPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListAuthzPoliciesResponse)` | The response received from the server.  
  
### ListAuthzPoliciesAsync(ListAuthzPoliciesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListAuthzPoliciesResponse> ListAuthzPoliciesAsync(ListAuthzPoliciesRequest request, CallOptions options)

Lists AuthzPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAuthzPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListAuthzPoliciesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAuthzPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListAuthzPoliciesResponse)` | The call object.  
  
### ListAuthzPoliciesAsync(ListAuthzPoliciesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListAuthzPoliciesResponse> ListAuthzPoliciesAsync(ListAuthzPoliciesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists AuthzPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAuthzPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListAuthzPoliciesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAuthzPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListAuthzPoliciesResponse)` | The call object.  
  
### ListBackendAuthenticationConfigs(ListBackendAuthenticationConfigsRequest, CallOptions)
    
    
    public virtual ListBackendAuthenticationConfigsResponse ListBackendAuthenticationConfigs(ListBackendAuthenticationConfigsRequest request, CallOptions options)

Lists BackendAuthenticationConfigs in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackendAuthenticationConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListBackendAuthenticationConfigsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListBackendAuthenticationConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListBackendAuthenticationConfigsResponse)` | The response received from the server.  
  
### ListBackendAuthenticationConfigs(ListBackendAuthenticationConfigsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListBackendAuthenticationConfigsResponse ListBackendAuthenticationConfigs(ListBackendAuthenticationConfigsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists BackendAuthenticationConfigs in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackendAuthenticationConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListBackendAuthenticationConfigsRequest)`  
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
`[ListBackendAuthenticationConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListBackendAuthenticationConfigsResponse)` | The response received from the server.  
  
### ListBackendAuthenticationConfigsAsync(ListBackendAuthenticationConfigsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListBackendAuthenticationConfigsResponse> ListBackendAuthenticationConfigsAsync(ListBackendAuthenticationConfigsRequest request, CallOptions options)

Lists BackendAuthenticationConfigs in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackendAuthenticationConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListBackendAuthenticationConfigsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListBackendAuthenticationConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListBackendAuthenticationConfigsResponse)` | The call object.  
  
### ListBackendAuthenticationConfigsAsync(ListBackendAuthenticationConfigsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListBackendAuthenticationConfigsResponse> ListBackendAuthenticationConfigsAsync(ListBackendAuthenticationConfigsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists BackendAuthenticationConfigs in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackendAuthenticationConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListBackendAuthenticationConfigsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListBackendAuthenticationConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListBackendAuthenticationConfigsResponse)` | The call object.  
  
### ListClientTlsPolicies(ListClientTlsPoliciesRequest, CallOptions)
    
    
    public virtual ListClientTlsPoliciesResponse ListClientTlsPolicies(ListClientTlsPoliciesRequest request, CallOptions options)

Lists ClientTlsPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListClientTlsPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListClientTlsPoliciesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListClientTlsPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListClientTlsPoliciesResponse)` | The response received from the server.  
  
### ListClientTlsPolicies(ListClientTlsPoliciesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListClientTlsPoliciesResponse ListClientTlsPolicies(ListClientTlsPoliciesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists ClientTlsPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListClientTlsPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListClientTlsPoliciesRequest)`  
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
`[ListClientTlsPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListClientTlsPoliciesResponse)` | The response received from the server.  
  
### ListClientTlsPoliciesAsync(ListClientTlsPoliciesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListClientTlsPoliciesResponse> ListClientTlsPoliciesAsync(ListClientTlsPoliciesRequest request, CallOptions options)

Lists ClientTlsPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListClientTlsPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListClientTlsPoliciesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListClientTlsPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListClientTlsPoliciesResponse)` | The call object.  
  
### ListClientTlsPoliciesAsync(ListClientTlsPoliciesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListClientTlsPoliciesResponse> ListClientTlsPoliciesAsync(ListClientTlsPoliciesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists ClientTlsPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListClientTlsPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListClientTlsPoliciesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListClientTlsPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListClientTlsPoliciesResponse)` | The call object.  
  
### ListGatewaySecurityPolicies(ListGatewaySecurityPoliciesRequest, CallOptions)
    
    
    public virtual ListGatewaySecurityPoliciesResponse ListGatewaySecurityPolicies(ListGatewaySecurityPoliciesRequest request, CallOptions options)

Lists GatewaySecurityPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGatewaySecurityPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListGatewaySecurityPoliciesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListGatewaySecurityPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListGatewaySecurityPoliciesResponse)` | The response received from the server.  
  
### ListGatewaySecurityPolicies(ListGatewaySecurityPoliciesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListGatewaySecurityPoliciesResponse ListGatewaySecurityPolicies(ListGatewaySecurityPoliciesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists GatewaySecurityPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGatewaySecurityPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListGatewaySecurityPoliciesRequest)`  
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
`[ListGatewaySecurityPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListGatewaySecurityPoliciesResponse)` | The response received from the server.  
  
### ListGatewaySecurityPoliciesAsync(ListGatewaySecurityPoliciesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListGatewaySecurityPoliciesResponse> ListGatewaySecurityPoliciesAsync(ListGatewaySecurityPoliciesRequest request, CallOptions options)

Lists GatewaySecurityPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGatewaySecurityPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListGatewaySecurityPoliciesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGatewaySecurityPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListGatewaySecurityPoliciesResponse)` | The call object.  
  
### ListGatewaySecurityPoliciesAsync(ListGatewaySecurityPoliciesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListGatewaySecurityPoliciesResponse> ListGatewaySecurityPoliciesAsync(ListGatewaySecurityPoliciesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists GatewaySecurityPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGatewaySecurityPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListGatewaySecurityPoliciesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGatewaySecurityPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListGatewaySecurityPoliciesResponse)` | The call object.  
  
### ListGatewaySecurityPolicyRules(ListGatewaySecurityPolicyRulesRequest, CallOptions)
    
    
    public virtual ListGatewaySecurityPolicyRulesResponse ListGatewaySecurityPolicyRules(ListGatewaySecurityPolicyRulesRequest request, CallOptions options)

Lists GatewaySecurityPolicyRules in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGatewaySecurityPolicyRulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListGatewaySecurityPolicyRulesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListGatewaySecurityPolicyRulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListGatewaySecurityPolicyRulesResponse)` | The response received from the server.  
  
### ListGatewaySecurityPolicyRules(ListGatewaySecurityPolicyRulesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListGatewaySecurityPolicyRulesResponse ListGatewaySecurityPolicyRules(ListGatewaySecurityPolicyRulesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists GatewaySecurityPolicyRules in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGatewaySecurityPolicyRulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListGatewaySecurityPolicyRulesRequest)`  
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
`[ListGatewaySecurityPolicyRulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListGatewaySecurityPolicyRulesResponse)` | The response received from the server.  
  
### ListGatewaySecurityPolicyRulesAsync(ListGatewaySecurityPolicyRulesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListGatewaySecurityPolicyRulesResponse> ListGatewaySecurityPolicyRulesAsync(ListGatewaySecurityPolicyRulesRequest request, CallOptions options)

Lists GatewaySecurityPolicyRules in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGatewaySecurityPolicyRulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListGatewaySecurityPolicyRulesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGatewaySecurityPolicyRulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListGatewaySecurityPolicyRulesResponse)` | The call object.  
  
### ListGatewaySecurityPolicyRulesAsync(ListGatewaySecurityPolicyRulesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListGatewaySecurityPolicyRulesResponse> ListGatewaySecurityPolicyRulesAsync(ListGatewaySecurityPolicyRulesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists GatewaySecurityPolicyRules in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGatewaySecurityPolicyRulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListGatewaySecurityPolicyRulesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListGatewaySecurityPolicyRulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListGatewaySecurityPolicyRulesResponse)` | The call object.  
  
### ListServerTlsPolicies(ListServerTlsPoliciesRequest, CallOptions)
    
    
    public virtual ListServerTlsPoliciesResponse ListServerTlsPolicies(ListServerTlsPoliciesRequest request, CallOptions options)

Lists ServerTlsPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServerTlsPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListServerTlsPoliciesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListServerTlsPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListServerTlsPoliciesResponse)` | The response received from the server.  
  
### ListServerTlsPolicies(ListServerTlsPoliciesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListServerTlsPoliciesResponse ListServerTlsPolicies(ListServerTlsPoliciesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists ServerTlsPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServerTlsPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListServerTlsPoliciesRequest)`  
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
`[ListServerTlsPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListServerTlsPoliciesResponse)` | The response received from the server.  
  
### ListServerTlsPoliciesAsync(ListServerTlsPoliciesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListServerTlsPoliciesResponse> ListServerTlsPoliciesAsync(ListServerTlsPoliciesRequest request, CallOptions options)

Lists ServerTlsPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServerTlsPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListServerTlsPoliciesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListServerTlsPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListServerTlsPoliciesResponse)` | The call object.  
  
### ListServerTlsPoliciesAsync(ListServerTlsPoliciesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListServerTlsPoliciesResponse> ListServerTlsPoliciesAsync(ListServerTlsPoliciesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists ServerTlsPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServerTlsPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListServerTlsPoliciesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListServerTlsPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListServerTlsPoliciesResponse)` | The call object.  
  
### ListTlsInspectionPolicies(ListTlsInspectionPoliciesRequest, CallOptions)
    
    
    public virtual ListTlsInspectionPoliciesResponse ListTlsInspectionPolicies(ListTlsInspectionPoliciesRequest request, CallOptions options)

Lists TlsInspectionPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTlsInspectionPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListTlsInspectionPoliciesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListTlsInspectionPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListTlsInspectionPoliciesResponse)` | The response received from the server.  
  
### ListTlsInspectionPolicies(ListTlsInspectionPoliciesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListTlsInspectionPoliciesResponse ListTlsInspectionPolicies(ListTlsInspectionPoliciesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists TlsInspectionPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTlsInspectionPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListTlsInspectionPoliciesRequest)`  
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
`[ListTlsInspectionPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListTlsInspectionPoliciesResponse)` | The response received from the server.  
  
### ListTlsInspectionPoliciesAsync(ListTlsInspectionPoliciesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListTlsInspectionPoliciesResponse> ListTlsInspectionPoliciesAsync(ListTlsInspectionPoliciesRequest request, CallOptions options)

Lists TlsInspectionPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTlsInspectionPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListTlsInspectionPoliciesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListTlsInspectionPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListTlsInspectionPoliciesResponse)` | The call object.  
  
### ListTlsInspectionPoliciesAsync(ListTlsInspectionPoliciesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListTlsInspectionPoliciesResponse> ListTlsInspectionPoliciesAsync(ListTlsInspectionPoliciesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists TlsInspectionPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTlsInspectionPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListTlsInspectionPoliciesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListTlsInspectionPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListTlsInspectionPoliciesResponse)` | The call object.  
  
### ListUrlLists(ListUrlListsRequest, CallOptions)
    
    
    public virtual ListUrlListsResponse ListUrlLists(ListUrlListsRequest request, CallOptions options)

Lists UrlLists in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUrlListsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListUrlListsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListUrlListsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListUrlListsResponse)` | The response received from the server.  
  
### ListUrlLists(ListUrlListsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListUrlListsResponse ListUrlLists(ListUrlListsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists UrlLists in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUrlListsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListUrlListsRequest)`  
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
`[ListUrlListsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListUrlListsResponse)` | The response received from the server.  
  
### ListUrlListsAsync(ListUrlListsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListUrlListsResponse> ListUrlListsAsync(ListUrlListsRequest request, CallOptions options)

Lists UrlLists in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUrlListsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListUrlListsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListUrlListsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListUrlListsResponse)` | The call object.  
  
### ListUrlListsAsync(ListUrlListsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListUrlListsResponse> ListUrlListsAsync(ListUrlListsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists UrlLists in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUrlListsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListUrlListsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListUrlListsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.ListUrlListsResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override NetworkSecurity.NetworkSecurityClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.NetworkSecurity)[NetworkSecurityClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.NetworkSecurity.NetworkSecurityClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.NetworkSecurity.V1.NetworkSecurity.NetworkSecurityClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### UpdateAuthorizationPolicy(UpdateAuthorizationPolicyRequest, CallOptions)
    
    
    public virtual Operation UpdateAuthorizationPolicy(UpdateAuthorizationPolicyRequest request, CallOptions options)

Updates the parameters of a single AuthorizationPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAuthorizationPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateAuthorizationPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateAuthorizationPolicy(UpdateAuthorizationPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateAuthorizationPolicy(UpdateAuthorizationPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single AuthorizationPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAuthorizationPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateAuthorizationPolicyRequest)`  
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
  
### UpdateAuthorizationPolicyAsync(UpdateAuthorizationPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateAuthorizationPolicyAsync(UpdateAuthorizationPolicyRequest request, CallOptions options)

Updates the parameters of a single AuthorizationPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAuthorizationPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateAuthorizationPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateAuthorizationPolicyAsync(UpdateAuthorizationPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateAuthorizationPolicyAsync(UpdateAuthorizationPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single AuthorizationPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAuthorizationPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateAuthorizationPolicyRequest)`  
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
  
### UpdateAuthzPolicy(UpdateAuthzPolicyRequest, CallOptions)
    
    
    public virtual Operation UpdateAuthzPolicy(UpdateAuthzPolicyRequest request, CallOptions options)

Updates the parameters of a single AuthzPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAuthzPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateAuthzPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateAuthzPolicy(UpdateAuthzPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateAuthzPolicy(UpdateAuthzPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single AuthzPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAuthzPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateAuthzPolicyRequest)`  
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
  
### UpdateAuthzPolicyAsync(UpdateAuthzPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateAuthzPolicyAsync(UpdateAuthzPolicyRequest request, CallOptions options)

Updates the parameters of a single AuthzPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAuthzPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateAuthzPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateAuthzPolicyAsync(UpdateAuthzPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateAuthzPolicyAsync(UpdateAuthzPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single AuthzPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAuthzPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateAuthzPolicyRequest)`  
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
  
### UpdateBackendAuthenticationConfig(UpdateBackendAuthenticationConfigRequest, CallOptions)
    
    
    public virtual Operation UpdateBackendAuthenticationConfig(UpdateBackendAuthenticationConfigRequest request, CallOptions options)

Updates the parameters of a single BackendAuthenticationConfig to BackendAuthenticationConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBackendAuthenticationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateBackendAuthenticationConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateBackendAuthenticationConfig(UpdateBackendAuthenticationConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateBackendAuthenticationConfig(UpdateBackendAuthenticationConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single BackendAuthenticationConfig to BackendAuthenticationConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBackendAuthenticationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateBackendAuthenticationConfigRequest)`  
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
  
### UpdateBackendAuthenticationConfigAsync(UpdateBackendAuthenticationConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateBackendAuthenticationConfigAsync(UpdateBackendAuthenticationConfigRequest request, CallOptions options)

Updates the parameters of a single BackendAuthenticationConfig to BackendAuthenticationConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBackendAuthenticationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateBackendAuthenticationConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateBackendAuthenticationConfigAsync(UpdateBackendAuthenticationConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateBackendAuthenticationConfigAsync(UpdateBackendAuthenticationConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single BackendAuthenticationConfig to BackendAuthenticationConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBackendAuthenticationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateBackendAuthenticationConfigRequest)`  
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
  
### UpdateClientTlsPolicy(UpdateClientTlsPolicyRequest, CallOptions)
    
    
    public virtual Operation UpdateClientTlsPolicy(UpdateClientTlsPolicyRequest request, CallOptions options)

Updates the parameters of a single ClientTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateClientTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateClientTlsPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateClientTlsPolicy(UpdateClientTlsPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateClientTlsPolicy(UpdateClientTlsPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single ClientTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateClientTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateClientTlsPolicyRequest)`  
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
  
### UpdateClientTlsPolicyAsync(UpdateClientTlsPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateClientTlsPolicyAsync(UpdateClientTlsPolicyRequest request, CallOptions options)

Updates the parameters of a single ClientTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateClientTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateClientTlsPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateClientTlsPolicyAsync(UpdateClientTlsPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateClientTlsPolicyAsync(UpdateClientTlsPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single ClientTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateClientTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateClientTlsPolicyRequest)`  
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
  
### UpdateGatewaySecurityPolicy(UpdateGatewaySecurityPolicyRequest, CallOptions)
    
    
    public virtual Operation UpdateGatewaySecurityPolicy(UpdateGatewaySecurityPolicyRequest request, CallOptions options)

Updates the parameters of a single GatewaySecurityPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGatewaySecurityPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateGatewaySecurityPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateGatewaySecurityPolicy(UpdateGatewaySecurityPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateGatewaySecurityPolicy(UpdateGatewaySecurityPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single GatewaySecurityPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGatewaySecurityPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateGatewaySecurityPolicyRequest)`  
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
  
### UpdateGatewaySecurityPolicyAsync(UpdateGatewaySecurityPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateGatewaySecurityPolicyAsync(UpdateGatewaySecurityPolicyRequest request, CallOptions options)

Updates the parameters of a single GatewaySecurityPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGatewaySecurityPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateGatewaySecurityPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateGatewaySecurityPolicyAsync(UpdateGatewaySecurityPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateGatewaySecurityPolicyAsync(UpdateGatewaySecurityPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single GatewaySecurityPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGatewaySecurityPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateGatewaySecurityPolicyRequest)`  
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
  
### UpdateGatewaySecurityPolicyRule(UpdateGatewaySecurityPolicyRuleRequest, CallOptions)
    
    
    public virtual Operation UpdateGatewaySecurityPolicyRule(UpdateGatewaySecurityPolicyRuleRequest request, CallOptions options)

Updates the parameters of a single GatewaySecurityPolicyRule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateGatewaySecurityPolicyRuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateGatewaySecurityPolicyRule(UpdateGatewaySecurityPolicyRuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateGatewaySecurityPolicyRule(UpdateGatewaySecurityPolicyRuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single GatewaySecurityPolicyRule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateGatewaySecurityPolicyRuleRequest)`  
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
  
### UpdateGatewaySecurityPolicyRuleAsync(UpdateGatewaySecurityPolicyRuleRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateGatewaySecurityPolicyRuleAsync(UpdateGatewaySecurityPolicyRuleRequest request, CallOptions options)

Updates the parameters of a single GatewaySecurityPolicyRule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateGatewaySecurityPolicyRuleRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateGatewaySecurityPolicyRuleAsync(UpdateGatewaySecurityPolicyRuleRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateGatewaySecurityPolicyRuleAsync(UpdateGatewaySecurityPolicyRuleRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single GatewaySecurityPolicyRule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateGatewaySecurityPolicyRuleRequest)`  
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
  
### UpdateServerTlsPolicy(UpdateServerTlsPolicyRequest, CallOptions)
    
    
    public virtual Operation UpdateServerTlsPolicy(UpdateServerTlsPolicyRequest request, CallOptions options)

Updates the parameters of a single ServerTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServerTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateServerTlsPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateServerTlsPolicy(UpdateServerTlsPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateServerTlsPolicy(UpdateServerTlsPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single ServerTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServerTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateServerTlsPolicyRequest)`  
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
  
### UpdateServerTlsPolicyAsync(UpdateServerTlsPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateServerTlsPolicyAsync(UpdateServerTlsPolicyRequest request, CallOptions options)

Updates the parameters of a single ServerTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServerTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateServerTlsPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateServerTlsPolicyAsync(UpdateServerTlsPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateServerTlsPolicyAsync(UpdateServerTlsPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single ServerTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServerTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateServerTlsPolicyRequest)`  
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
  
### UpdateTlsInspectionPolicy(UpdateTlsInspectionPolicyRequest, CallOptions)
    
    
    public virtual Operation UpdateTlsInspectionPolicy(UpdateTlsInspectionPolicyRequest request, CallOptions options)

Updates the parameters of a single TlsInspectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTlsInspectionPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateTlsInspectionPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateTlsInspectionPolicy(UpdateTlsInspectionPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateTlsInspectionPolicy(UpdateTlsInspectionPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single TlsInspectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTlsInspectionPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateTlsInspectionPolicyRequest)`  
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
  
### UpdateTlsInspectionPolicyAsync(UpdateTlsInspectionPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateTlsInspectionPolicyAsync(UpdateTlsInspectionPolicyRequest request, CallOptions options)

Updates the parameters of a single TlsInspectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTlsInspectionPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateTlsInspectionPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateTlsInspectionPolicyAsync(UpdateTlsInspectionPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateTlsInspectionPolicyAsync(UpdateTlsInspectionPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single TlsInspectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTlsInspectionPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateTlsInspectionPolicyRequest)`  
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
  
### UpdateUrlList(UpdateUrlListRequest, CallOptions)
    
    
    public virtual Operation UpdateUrlList(UpdateUrlListRequest request, CallOptions options)

Updates the parameters of a single UrlList.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUrlListRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateUrlListRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateUrlList(UpdateUrlListRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateUrlList(UpdateUrlListRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single UrlList.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUrlListRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateUrlListRequest)`  
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
  
### UpdateUrlListAsync(UpdateUrlListRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateUrlListAsync(UpdateUrlListRequest request, CallOptions options)

Updates the parameters of a single UrlList.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUrlListRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateUrlListRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateUrlListAsync(UpdateUrlListRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateUrlListAsync(UpdateUrlListRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single UrlList.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateUrlListRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.UpdateUrlListRequest)`  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-01 UTC."],[],[]] 
