---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.CloudShellService.CloudShellServiceClient
title: Cloud Shell v1 API - Class CloudShellService.CloudShellServiceClient (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:28.524801+00:00
---

# Cloud Shell v1 API - Class CloudShellService.CloudShellServiceClient (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.CloudShellService.CloudShellServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Shell v1 API - Class CloudShellService.CloudShellServiceClient (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.CloudShellService.CloudShellServiceClient)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/2.5.0/Google.Cloud.Shell.V1.CloudShellService.CloudShellServiceClient)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/2.4.0/Google.Cloud.Shell.V1.CloudShellService.CloudShellServiceClient)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/2.3.0/Google.Cloud.Shell.V1.CloudShellService.CloudShellServiceClient)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/2.2.0/Google.Cloud.Shell.V1.CloudShellService.CloudShellServiceClient)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/2.1.0/Google.Cloud.Shell.V1.CloudShellService.CloudShellServiceClient)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/2.0.0/Google.Cloud.Shell.V1.CloudShellService.CloudShellServiceClient)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/1.1.0/Google.Cloud.Shell.V1.CloudShellService.CloudShellServiceClient)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/1.0.0/Google.Cloud.Shell.V1.CloudShellService.CloudShellServiceClient)


    
    
    public class CloudShellService.CloudShellServiceClient : ClientBase<CloudShellService.CloudShellServiceClient>

Reference documentation and code samples for the Cloud Shell v1 API class CloudShellService.CloudShellServiceClient.

Client for CloudShellService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[CloudShellService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.CloudShellService)[CloudShellServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.CloudShellService.CloudShellServiceClient) > CloudShellService.CloudShellServiceClient

## Inherited Members

[ClientBase<CloudShellService.CloudShellServiceClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Shell.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1)

## Assembly

Google.Cloud.Shell.V1.dll

## Constructors 

### CloudShellServiceClient()
    
    
    protected CloudShellServiceClient()

Protected parameterless constructor to allow creation of test doubles.

### CloudShellServiceClient(CallInvoker)
    
    
    public CloudShellServiceClient(CallInvoker callInvoker)

Creates a new client for CloudShellService that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### CloudShellServiceClient(ChannelBase)
    
    
    public CloudShellServiceClient(ChannelBase channel)

Creates a new client for CloudShellService

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### CloudShellServiceClient(ClientBaseConfiguration)
    
    
    protected CloudShellServiceClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### AddPublicKey(AddPublicKeyRequest, CallOptions)
    
    
    public virtual Operation AddPublicKey(AddPublicKeyRequest request, CallOptions options)

Adds a public SSH key to an environment, allowing clients with the corresponding private key to connect to that environment via SSH. If a key with the same content already exists, this will error with ALREADY_EXISTS.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddPublicKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.AddPublicKeyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### AddPublicKey(AddPublicKeyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation AddPublicKey(AddPublicKeyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Adds a public SSH key to an environment, allowing clients with the corresponding private key to connect to that environment via SSH. If a key with the same content already exists, this will error with ALREADY_EXISTS.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddPublicKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.AddPublicKeyRequest)`  
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
  
### AddPublicKeyAsync(AddPublicKeyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> AddPublicKeyAsync(AddPublicKeyRequest request, CallOptions options)

Adds a public SSH key to an environment, allowing clients with the corresponding private key to connect to that environment via SSH. If a key with the same content already exists, this will error with ALREADY_EXISTS.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddPublicKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.AddPublicKeyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### AddPublicKeyAsync(AddPublicKeyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> AddPublicKeyAsync(AddPublicKeyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Adds a public SSH key to an environment, allowing clients with the corresponding private key to connect to that environment via SSH. If a key with the same content already exists, this will error with ALREADY_EXISTS.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddPublicKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.AddPublicKeyRequest)`  
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
  
### AuthorizeEnvironment(AuthorizeEnvironmentRequest, CallOptions)
    
    
    public virtual Operation AuthorizeEnvironment(AuthorizeEnvironmentRequest request, CallOptions options)

Sends OAuth credentials to a running environment on behalf of a user. When this completes, the environment will be authorized to run various Google Cloud command line tools without requiring the user to manually authenticate.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AuthorizeEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.AuthorizeEnvironmentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### AuthorizeEnvironment(AuthorizeEnvironmentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation AuthorizeEnvironment(AuthorizeEnvironmentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Sends OAuth credentials to a running environment on behalf of a user. When this completes, the environment will be authorized to run various Google Cloud command line tools without requiring the user to manually authenticate.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AuthorizeEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.AuthorizeEnvironmentRequest)`  
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
  
### AuthorizeEnvironmentAsync(AuthorizeEnvironmentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> AuthorizeEnvironmentAsync(AuthorizeEnvironmentRequest request, CallOptions options)

Sends OAuth credentials to a running environment on behalf of a user. When this completes, the environment will be authorized to run various Google Cloud command line tools without requiring the user to manually authenticate.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AuthorizeEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.AuthorizeEnvironmentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### AuthorizeEnvironmentAsync(AuthorizeEnvironmentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> AuthorizeEnvironmentAsync(AuthorizeEnvironmentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Sends OAuth credentials to a running environment on behalf of a user. When this completes, the environment will be authorized to run various Google Cloud command line tools without requiring the user to manually authenticate.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AuthorizeEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.AuthorizeEnvironmentRequest)`  
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
  
### CreateOperationsClient()
    
    
    public virtual Operations.OperationsClient CreateOperationsClient()

Creates a new instance of [Operations.OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[Operations](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.html)[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html)` | A new Operations client for the same target as this client.  
  
### GetEnvironment(GetEnvironmentRequest, CallOptions)
    
    
    public virtual Environment GetEnvironment(GetEnvironmentRequest request, CallOptions options)

Gets an environment. Returns NOT_FOUND if the environment does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.GetEnvironmentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.Environment)` | The response received from the server.  
  
### GetEnvironment(GetEnvironmentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Environment GetEnvironment(GetEnvironmentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets an environment. Returns NOT_FOUND if the environment does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.GetEnvironmentRequest)`  
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
`[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.Environment)` | The response received from the server.  
  
### GetEnvironmentAsync(GetEnvironmentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Environment> GetEnvironmentAsync(GetEnvironmentRequest request, CallOptions options)

Gets an environment. Returns NOT_FOUND if the environment does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.GetEnvironmentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.Environment)` | The call object.  
  
### GetEnvironmentAsync(GetEnvironmentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Environment> GetEnvironmentAsync(GetEnvironmentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets an environment. Returns NOT_FOUND if the environment does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.GetEnvironmentRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.Environment)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override CloudShellService.CloudShellServiceClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudShellService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.CloudShellService)[CloudShellServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.CloudShellService.CloudShellServiceClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Shell.V1.CloudShellService.CloudShellServiceClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### RemovePublicKey(RemovePublicKeyRequest, CallOptions)
    
    
    public virtual Operation RemovePublicKey(RemovePublicKeyRequest request, CallOptions options)

Removes a public SSH key from an environment. Clients will no longer be able to connect to the environment using the corresponding private key. If a key with the same content is not present, this will error with NOT_FOUND.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemovePublicKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.RemovePublicKeyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### RemovePublicKey(RemovePublicKeyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation RemovePublicKey(RemovePublicKeyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Removes a public SSH key from an environment. Clients will no longer be able to connect to the environment using the corresponding private key. If a key with the same content is not present, this will error with NOT_FOUND.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemovePublicKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.RemovePublicKeyRequest)`  
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
  
### RemovePublicKeyAsync(RemovePublicKeyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> RemovePublicKeyAsync(RemovePublicKeyRequest request, CallOptions options)

Removes a public SSH key from an environment. Clients will no longer be able to connect to the environment using the corresponding private key. If a key with the same content is not present, this will error with NOT_FOUND.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemovePublicKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.RemovePublicKeyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### RemovePublicKeyAsync(RemovePublicKeyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> RemovePublicKeyAsync(RemovePublicKeyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Removes a public SSH key from an environment. Clients will no longer be able to connect to the environment using the corresponding private key. If a key with the same content is not present, this will error with NOT_FOUND.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemovePublicKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.RemovePublicKeyRequest)`  
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
  
### StartEnvironment(StartEnvironmentRequest, CallOptions)
    
    
    public virtual Operation StartEnvironment(StartEnvironmentRequest request, CallOptions options)

Starts an existing environment, allowing clients to connect to it. The returned operation will contain an instance of StartEnvironmentMetadata in its metadata field. Users can wait for the environment to start by polling this operation via GetOperation. Once the environment has finished starting and is ready to accept connections, the operation will contain a StartEnvironmentResponse in its response field.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.StartEnvironmentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### StartEnvironment(StartEnvironmentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation StartEnvironment(StartEnvironmentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Starts an existing environment, allowing clients to connect to it. The returned operation will contain an instance of StartEnvironmentMetadata in its metadata field. Users can wait for the environment to start by polling this operation via GetOperation. Once the environment has finished starting and is ready to accept connections, the operation will contain a StartEnvironmentResponse in its response field.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.StartEnvironmentRequest)`  
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
  
### StartEnvironmentAsync(StartEnvironmentRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> StartEnvironmentAsync(StartEnvironmentRequest request, CallOptions options)

Starts an existing environment, allowing clients to connect to it. The returned operation will contain an instance of StartEnvironmentMetadata in its metadata field. Users can wait for the environment to start by polling this operation via GetOperation. Once the environment has finished starting and is ready to accept connections, the operation will contain a StartEnvironmentResponse in its response field.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.StartEnvironmentRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### StartEnvironmentAsync(StartEnvironmentRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> StartEnvironmentAsync(StartEnvironmentRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Starts an existing environment, allowing clients to connect to it. The returned operation will contain an instance of StartEnvironmentMetadata in its metadata field. Users can wait for the environment to start by polling this operation via GetOperation. Once the environment has finished starting and is ready to accept connections, the operation will contain a StartEnvironmentResponse in its response field.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.StartEnvironmentRequest)`  
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

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
