---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1.BinauthzManagementServiceV1Beta1Client
title: Binary Authorization v1beta1 API - Class BinauthzManagementServiceV1Beta1.BinauthzManagementServiceV1Beta1Client (2.0.0-beta10) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:48.579794+00:00
---

# Binary Authorization v1beta1 API - Class BinauthzManagementServiceV1Beta1.BinauthzManagementServiceV1Beta1Client (2.0.0-beta10)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1.BinauthzManagementServiceV1Beta1Client

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Binary Authorization v1beta1 API - Class BinauthzManagementServiceV1Beta1.BinauthzManagementServiceV1Beta1Client (2.0.0-beta10) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0-beta10 (latest)  2.0.0-beta09  1.0.0-beta05 
    
    
    public class BinauthzManagementServiceV1Beta1.BinauthzManagementServiceV1Beta1Client : ClientBase<BinauthzManagementServiceV1Beta1.BinauthzManagementServiceV1Beta1Client>

Reference documentation and code samples for the Binary Authorization v1beta1 API class BinauthzManagementServiceV1Beta1.BinauthzManagementServiceV1Beta1Client.

Client for BinauthzManagementServiceV1Beta1

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[BinauthzManagementServiceV1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1)[BinauthzManagementServiceV1Beta1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1.BinauthzManagementServiceV1Beta1Client) > BinauthzManagementServiceV1Beta1.BinauthzManagementServiceV1Beta1Client

## Inherited Members

[ClientBase<BinauthzManagementServiceV1Beta1.BinauthzManagementServiceV1Beta1Client>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BinaryAuthorization.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1)

## Assembly

Google.Cloud.BinaryAuthorization.V1Beta1.dll

## Constructors 

### BinauthzManagementServiceV1Beta1Client()
    
    
    protected BinauthzManagementServiceV1Beta1Client()

Protected parameterless constructor to allow creation of test doubles.

### BinauthzManagementServiceV1Beta1Client(CallInvoker)
    
    
    public BinauthzManagementServiceV1Beta1Client(CallInvoker callInvoker)

Creates a new client for BinauthzManagementServiceV1Beta1 that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### BinauthzManagementServiceV1Beta1Client(ChannelBase)
    
    
    public BinauthzManagementServiceV1Beta1Client(ChannelBase channel)

Creates a new client for BinauthzManagementServiceV1Beta1

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### BinauthzManagementServiceV1Beta1Client(ClientBaseConfiguration)
    
    
    protected BinauthzManagementServiceV1Beta1Client(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### CreateAttestor(CreateAttestorRequest, CallOptions)
    
    
    public virtual Attestor CreateAttestor(CreateAttestorRequest request, CallOptions options)

Creates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor], and returns a copy of the new [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed, ALREADY_EXISTS if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] already exists.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.CreateAttestorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | The response received from the server.  
  
### CreateAttestor(CreateAttestorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Attestor CreateAttestor(CreateAttestorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor], and returns a copy of the new [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed, ALREADY_EXISTS if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] already exists.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.CreateAttestorRequest)`  
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
`[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | The response received from the server.  
  
### CreateAttestorAsync(CreateAttestorRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Attestor> CreateAttestorAsync(CreateAttestorRequest request, CallOptions options)

Creates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor], and returns a copy of the new [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed, ALREADY_EXISTS if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] already exists.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.CreateAttestorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | The call object.  
  
### CreateAttestorAsync(CreateAttestorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Attestor> CreateAttestorAsync(CreateAttestorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor], and returns a copy of the new [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed, ALREADY_EXISTS if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] already exists.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.CreateAttestorRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | The call object.  
  
### CreateIAMPolicyClient()
    
    
    public virtual IAMPolicy.IAMPolicyClient CreateIAMPolicyClient()

Creates a new instance of [IAMPolicy.IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.IAMPolicyClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[IAMPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.html)[IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.IAMPolicyClient.html)` | A new [IAMPolicy.IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.IAMPolicyClient.html) for the same target as this client.  
  
### DeleteAttestor(DeleteAttestorRequest, CallOptions)
    
    
    public virtual Empty DeleteAttestor(DeleteAttestorRequest request, CallOptions options)

Deletes an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.DeleteAttestorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteAttestor(DeleteAttestorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteAttestor(DeleteAttestorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.DeleteAttestorRequest)`  
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
  
### DeleteAttestorAsync(DeleteAttestorRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteAttestorAsync(DeleteAttestorRequest request, CallOptions options)

Deletes an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.DeleteAttestorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteAttestorAsync(DeleteAttestorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteAttestorAsync(DeleteAttestorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.DeleteAttestorRequest)`  
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
  
### GetAttestor(GetAttestorRequest, CallOptions)
    
    
    public virtual Attestor GetAttestor(GetAttestorRequest request, CallOptions options)

Gets an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.GetAttestorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | The response received from the server.  
  
### GetAttestor(GetAttestorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Attestor GetAttestor(GetAttestorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.GetAttestorRequest)`  
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
`[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | The response received from the server.  
  
### GetAttestorAsync(GetAttestorRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Attestor> GetAttestorAsync(GetAttestorRequest request, CallOptions options)

Gets an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.GetAttestorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | The call object.  
  
### GetAttestorAsync(GetAttestorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Attestor> GetAttestorAsync(GetAttestorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.GetAttestorRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | The call object.  
  
### GetPolicy(GetPolicyRequest, CallOptions)
    
    
    public virtual Policy GetPolicy(GetPolicyRequest request, CallOptions options)

A [policy][google.cloud.binaryauthorization.v1beta1.Policy] specifies the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] that must attest to a container image, before the project is allowed to deploy that image. There is at most one policy per project. All image admission requests are permitted if a project has no policy.

Gets the [policy][google.cloud.binaryauthorization.v1beta1.Policy] for this project. Returns a default [policy][google.cloud.binaryauthorization.v1beta1.Policy] if the project does not have one.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.GetPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | The response received from the server.  
  
### GetPolicy(GetPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Policy GetPolicy(GetPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

A [policy][google.cloud.binaryauthorization.v1beta1.Policy] specifies the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] that must attest to a container image, before the project is allowed to deploy that image. There is at most one policy per project. All image admission requests are permitted if a project has no policy.

Gets the [policy][google.cloud.binaryauthorization.v1beta1.Policy] for this project. Returns a default [policy][google.cloud.binaryauthorization.v1beta1.Policy] if the project does not have one.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.GetPolicyRequest)`  
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
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | The response received from the server.  
  
### GetPolicyAsync(GetPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Policy> GetPolicyAsync(GetPolicyRequest request, CallOptions options)

A [policy][google.cloud.binaryauthorization.v1beta1.Policy] specifies the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] that must attest to a container image, before the project is allowed to deploy that image. There is at most one policy per project. All image admission requests are permitted if a project has no policy.

Gets the [policy][google.cloud.binaryauthorization.v1beta1.Policy] for this project. Returns a default [policy][google.cloud.binaryauthorization.v1beta1.Policy] if the project does not have one.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.GetPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | The call object.  
  
### GetPolicyAsync(GetPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Policy> GetPolicyAsync(GetPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

A [policy][google.cloud.binaryauthorization.v1beta1.Policy] specifies the [attestors][google.cloud.binaryauthorization.v1beta1.Attestor] that must attest to a container image, before the project is allowed to deploy that image. There is at most one policy per project. All image admission requests are permitted if a project has no policy.

Gets the [policy][google.cloud.binaryauthorization.v1beta1.Policy] for this project. Returns a default [policy][google.cloud.binaryauthorization.v1beta1.Policy] if the project does not have one.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.GetPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | The call object.  
  
### ListAttestors(ListAttestorsRequest, CallOptions)
    
    
    public virtual ListAttestorsResponse ListAttestors(ListAttestorsRequest request, CallOptions options)

Lists [attestors][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns INVALID_ARGUMENT if the project does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAttestorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ListAttestorsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAttestorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ListAttestorsResponse)` | The response received from the server.  
  
### ListAttestors(ListAttestorsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListAttestorsResponse ListAttestors(ListAttestorsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists [attestors][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns INVALID_ARGUMENT if the project does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAttestorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ListAttestorsRequest)`  
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
`[ListAttestorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ListAttestorsResponse)` | The response received from the server.  
  
### ListAttestorsAsync(ListAttestorsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListAttestorsResponse> ListAttestorsAsync(ListAttestorsRequest request, CallOptions options)

Lists [attestors][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns INVALID_ARGUMENT if the project does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAttestorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ListAttestorsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAttestorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ListAttestorsResponse)` | The call object.  
  
### ListAttestorsAsync(ListAttestorsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListAttestorsResponse> ListAttestorsAsync(ListAttestorsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists [attestors][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns INVALID_ARGUMENT if the project does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAttestorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ListAttestorsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAttestorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ListAttestorsResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override BinauthzManagementServiceV1Beta1.BinauthzManagementServiceV1Beta1Client NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BinauthzManagementServiceV1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1)[BinauthzManagementServiceV1Beta1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1.BinauthzManagementServiceV1Beta1Client)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1.BinauthzManagementServiceV1Beta1Client>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### UpdateAttestor(UpdateAttestorRequest, CallOptions)
    
    
    public virtual Attestor UpdateAttestor(UpdateAttestorRequest request, CallOptions options)

Updates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UpdateAttestorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | The response received from the server.  
  
### UpdateAttestor(UpdateAttestorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Attestor UpdateAttestor(UpdateAttestorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UpdateAttestorRequest)`  
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
`[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | The response received from the server.  
  
### UpdateAttestorAsync(UpdateAttestorRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Attestor> UpdateAttestorAsync(UpdateAttestorRequest request, CallOptions options)

Updates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UpdateAttestorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | The call object.  
  
### UpdateAttestorAsync(UpdateAttestorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Attestor> UpdateAttestorAsync(UpdateAttestorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates an [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]. Returns NOT_FOUND if the [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UpdateAttestorRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)` | The call object.  
  
### UpdatePolicy(UpdatePolicyRequest, CallOptions)
    
    
    public virtual Policy UpdatePolicy(UpdatePolicyRequest request, CallOptions options)

Creates or updates a project's [policy][google.cloud.binaryauthorization.v1beta1.Policy], and returns a copy of the new [policy][google.cloud.binaryauthorization.v1beta1.Policy]. A policy is always updated as a whole, to avoid race conditions with concurrent policy enforcement (or management!) requests. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UpdatePolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | The response received from the server.  
  
### UpdatePolicy(UpdatePolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Policy UpdatePolicy(UpdatePolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates or updates a project's [policy][google.cloud.binaryauthorization.v1beta1.Policy], and returns a copy of the new [policy][google.cloud.binaryauthorization.v1beta1.Policy]. A policy is always updated as a whole, to avoid race conditions with concurrent policy enforcement (or management!) requests. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UpdatePolicyRequest)`  
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
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | The response received from the server.  
  
### UpdatePolicyAsync(UpdatePolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Policy> UpdatePolicyAsync(UpdatePolicyRequest request, CallOptions options)

Creates or updates a project's [policy][google.cloud.binaryauthorization.v1beta1.Policy], and returns a copy of the new [policy][google.cloud.binaryauthorization.v1beta1.Policy]. A policy is always updated as a whole, to avoid race conditions with concurrent policy enforcement (or management!) requests. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UpdatePolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | The call object.  
  
### UpdatePolicyAsync(UpdatePolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Policy> UpdatePolicyAsync(UpdatePolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates or updates a project's [policy][google.cloud.binaryauthorization.v1beta1.Policy], and returns a copy of the new [policy][google.cloud.binaryauthorization.v1beta1.Policy]. A policy is always updated as a whole, to avoid race conditions with concurrent policy enforcement (or management!) requests. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UpdatePolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
