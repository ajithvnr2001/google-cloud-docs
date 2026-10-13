---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionBackendBuckets.RegionBackendBucketsClient
title: Compute Engine v1 API - Class RegionBackendBuckets.RegionBackendBucketsClient (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:03.522847+00:00
---

# Compute Engine v1 API - Class RegionBackendBuckets.RegionBackendBucketsClient (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionBackendBuckets.RegionBackendBucketsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class RegionBackendBuckets.RegionBackendBucketsClient (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public class RegionBackendBuckets.RegionBackendBucketsClient : ClientBase<RegionBackendBuckets.RegionBackendBucketsClient>

Reference documentation and code samples for the Compute Engine v1 API class RegionBackendBuckets.RegionBackendBucketsClient.

Client for RegionBackendBuckets

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[RegionBackendBuckets](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionBackendBuckets)[RegionBackendBucketsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionBackendBuckets.RegionBackendBucketsClient) > RegionBackendBuckets.RegionBackendBucketsClient

## Inherited Members

[ClientBase<RegionBackendBuckets.RegionBackendBucketsClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### RegionBackendBucketsClient()
    
    
    protected RegionBackendBucketsClient()

Protected parameterless constructor to allow creation of test doubles.

### RegionBackendBucketsClient(CallInvoker)
    
    
    public RegionBackendBucketsClient(CallInvoker callInvoker)

Creates a new client for RegionBackendBuckets that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### RegionBackendBucketsClient(ChannelBase)
    
    
    public RegionBackendBucketsClient(ChannelBase channel)

Creates a new client for RegionBackendBuckets

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### RegionBackendBucketsClient(ClientBaseConfiguration)
    
    
    protected RegionBackendBucketsClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### CreateOperationsClientForRegionOperations()
    
    
    public virtual Operations.OperationsClient CreateOperationsClientForRegionOperations()

Creates a new instance of [Operations.OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html) using the same call invoker as this client, delegating to RegionOperations.

**Returns**  
---  
**Type** | **Description**  
`[Operations](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.html)[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html)` | A new Operations client for the same target as this client.  
  
### Delete(DeleteRegionBackendBucketRequest, CallOptions)
    
    
    public virtual Operation Delete(DeleteRegionBackendBucketRequest request, CallOptions options)

Deletes the specified regional BackendBucket resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteRegionBackendBucketRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### Delete(DeleteRegionBackendBucketRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation Delete(DeleteRegionBackendBucketRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified regional BackendBucket resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteRegionBackendBucketRequest)`  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### DeleteAsync(DeleteRegionBackendBucketRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteAsync(DeleteRegionBackendBucketRequest request, CallOptions options)

Deletes the specified regional BackendBucket resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteRegionBackendBucketRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### DeleteAsync(DeleteRegionBackendBucketRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteAsync(DeleteRegionBackendBucketRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified regional BackendBucket resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteRegionBackendBucketRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### Get(GetRegionBackendBucketRequest, CallOptions)
    
    
    public virtual BackendBucket Get(GetRegionBackendBucketRequest request, CallOptions options)

Returns the specified regional BackendBucket resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetRegionBackendBucketRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[BackendBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendBucket)` | The response received from the server.  
  
### Get(GetRegionBackendBucketRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual BackendBucket Get(GetRegionBackendBucketRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the specified regional BackendBucket resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetRegionBackendBucketRequest)`  
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
`[BackendBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendBucket)` | The response received from the server.  
  
### GetAsync(GetRegionBackendBucketRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<BackendBucket> GetAsync(GetRegionBackendBucketRequest request, CallOptions options)

Returns the specified regional BackendBucket resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetRegionBackendBucketRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BackendBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendBucket)` | The call object.  
  
### GetAsync(GetRegionBackendBucketRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<BackendBucket> GetAsync(GetRegionBackendBucketRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the specified regional BackendBucket resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetRegionBackendBucketRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BackendBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendBucket)` | The call object.  
  
### GetIamPolicy(GetIamPolicyRegionBackendBucketRequest, CallOptions)
    
    
    public virtual Policy GetIamPolicy(GetIamPolicyRegionBackendBucketRequest request, CallOptions options)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetIamPolicyRegionBackendBucketRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The response received from the server.  
  
### GetIamPolicy(GetIamPolicyRegionBackendBucketRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Policy GetIamPolicy(GetIamPolicyRegionBackendBucketRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetIamPolicyRegionBackendBucketRequest)`  
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
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The response received from the server.  
  
### GetIamPolicyAsync(GetIamPolicyRegionBackendBucketRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Policy> GetIamPolicyAsync(GetIamPolicyRegionBackendBucketRequest request, CallOptions options)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetIamPolicyRegionBackendBucketRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The call object.  
  
### GetIamPolicyAsync(GetIamPolicyRegionBackendBucketRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Policy> GetIamPolicyAsync(GetIamPolicyRegionBackendBucketRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetIamPolicyRegionBackendBucketRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The call object.  
  
### Insert(InsertRegionBackendBucketRequest, CallOptions)
    
    
    public virtual Operation Insert(InsertRegionBackendBucketRequest request, CallOptions options)

Creates a RegionBackendBucket in the specified project in the given scope using the parameters that are included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertRegionBackendBucketRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### Insert(InsertRegionBackendBucketRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation Insert(InsertRegionBackendBucketRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a RegionBackendBucket in the specified project in the given scope using the parameters that are included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertRegionBackendBucketRequest)`  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### InsertAsync(InsertRegionBackendBucketRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> InsertAsync(InsertRegionBackendBucketRequest request, CallOptions options)

Creates a RegionBackendBucket in the specified project in the given scope using the parameters that are included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertRegionBackendBucketRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### InsertAsync(InsertRegionBackendBucketRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> InsertAsync(InsertRegionBackendBucketRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a RegionBackendBucket in the specified project in the given scope using the parameters that are included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertRegionBackendBucketRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### List(ListRegionBackendBucketsRequest, CallOptions)
    
    
    public virtual BackendBucketList List(ListRegionBackendBucketsRequest request, CallOptions options)

Retrieves the list of BackendBucket resources available to the specified project in the given region.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRegionBackendBucketsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListRegionBackendBucketsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[BackendBucketList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendBucketList)` | The response received from the server.  
  
### List(ListRegionBackendBucketsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual BackendBucketList List(ListRegionBackendBucketsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieves the list of BackendBucket resources available to the specified project in the given region.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRegionBackendBucketsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListRegionBackendBucketsRequest)`  
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
`[BackendBucketList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendBucketList)` | The response received from the server.  
  
### ListAsync(ListRegionBackendBucketsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<BackendBucketList> ListAsync(ListRegionBackendBucketsRequest request, CallOptions options)

Retrieves the list of BackendBucket resources available to the specified project in the given region.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRegionBackendBucketsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListRegionBackendBucketsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BackendBucketList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendBucketList)` | The call object.  
  
### ListAsync(ListRegionBackendBucketsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<BackendBucketList> ListAsync(ListRegionBackendBucketsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieves the list of BackendBucket resources available to the specified project in the given region.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRegionBackendBucketsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListRegionBackendBucketsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BackendBucketList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendBucketList)` | The call object.  
  
### ListUsable(ListUsableRegionBackendBucketsRequest, CallOptions)
    
    
    public virtual BackendBucketListUsable ListUsable(ListUsableRegionBackendBucketsRequest request, CallOptions options)

Retrieves a list of all usable backend buckets in the specified project in the given region.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUsableRegionBackendBucketsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListUsableRegionBackendBucketsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[BackendBucketListUsable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendBucketListUsable)` | The response received from the server.  
  
### ListUsable(ListUsableRegionBackendBucketsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual BackendBucketListUsable ListUsable(ListUsableRegionBackendBucketsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieves a list of all usable backend buckets in the specified project in the given region.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUsableRegionBackendBucketsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListUsableRegionBackendBucketsRequest)`  
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
`[BackendBucketListUsable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendBucketListUsable)` | The response received from the server.  
  
### ListUsableAsync(ListUsableRegionBackendBucketsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<BackendBucketListUsable> ListUsableAsync(ListUsableRegionBackendBucketsRequest request, CallOptions options)

Retrieves a list of all usable backend buckets in the specified project in the given region.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUsableRegionBackendBucketsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListUsableRegionBackendBucketsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BackendBucketListUsable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendBucketListUsable)` | The call object.  
  
### ListUsableAsync(ListUsableRegionBackendBucketsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<BackendBucketListUsable> ListUsableAsync(ListUsableRegionBackendBucketsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieves a list of all usable backend buckets in the specified project in the given region.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUsableRegionBackendBucketsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListUsableRegionBackendBucketsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BackendBucketListUsable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendBucketListUsable)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override RegionBackendBuckets.RegionBackendBucketsClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionBackendBuckets](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionBackendBuckets)[RegionBackendBucketsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionBackendBuckets.RegionBackendBucketsClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Compute.V1.RegionBackendBuckets.RegionBackendBucketsClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### Patch(PatchRegionBackendBucketRequest, CallOptions)
    
    
    public virtual Operation Patch(PatchRegionBackendBucketRequest request, CallOptions options)

Updates the specified BackendBucket resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchRegionBackendBucketRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### Patch(PatchRegionBackendBucketRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation Patch(PatchRegionBackendBucketRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the specified BackendBucket resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchRegionBackendBucketRequest)`  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### PatchAsync(PatchRegionBackendBucketRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> PatchAsync(PatchRegionBackendBucketRequest request, CallOptions options)

Updates the specified BackendBucket resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchRegionBackendBucketRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### PatchAsync(PatchRegionBackendBucketRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> PatchAsync(PatchRegionBackendBucketRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the specified BackendBucket resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchRegionBackendBucketRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### SetIamPolicy(SetIamPolicyRegionBackendBucketRequest, CallOptions)
    
    
    public virtual Policy SetIamPolicy(SetIamPolicyRegionBackendBucketRequest request, CallOptions options)

Sets the access control policy on the specified resource. Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SetIamPolicyRegionBackendBucketRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The response received from the server.  
  
### SetIamPolicy(SetIamPolicyRegionBackendBucketRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Policy SetIamPolicy(SetIamPolicyRegionBackendBucketRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Sets the access control policy on the specified resource. Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SetIamPolicyRegionBackendBucketRequest)`  
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
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The response received from the server.  
  
### SetIamPolicyAsync(SetIamPolicyRegionBackendBucketRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Policy> SetIamPolicyAsync(SetIamPolicyRegionBackendBucketRequest request, CallOptions options)

Sets the access control policy on the specified resource. Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SetIamPolicyRegionBackendBucketRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The call object.  
  
### SetIamPolicyAsync(SetIamPolicyRegionBackendBucketRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Policy> SetIamPolicyAsync(SetIamPolicyRegionBackendBucketRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Sets the access control policy on the specified resource. Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SetIamPolicyRegionBackendBucketRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The call object.  
  
### TestIamPermissions(TestIamPermissionsRegionBackendBucketRequest, CallOptions)
    
    
    public virtual TestPermissionsResponse TestIamPermissions(TestIamPermissionsRegionBackendBucketRequest request, CallOptions options)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestIamPermissionsRegionBackendBucketRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | The response received from the server.  
  
### TestIamPermissions(TestIamPermissionsRegionBackendBucketRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual TestPermissionsResponse TestIamPermissions(TestIamPermissionsRegionBackendBucketRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestIamPermissionsRegionBackendBucketRequest)`  
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
`[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | The response received from the server.  
  
### TestIamPermissionsAsync(TestIamPermissionsRegionBackendBucketRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<TestPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsRegionBackendBucketRequest request, CallOptions options)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestIamPermissionsRegionBackendBucketRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | The call object.  
  
### TestIamPermissionsAsync(TestIamPermissionsRegionBackendBucketRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<TestPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsRegionBackendBucketRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRegionBackendBucketRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestIamPermissionsRegionBackendBucketRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
