---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.VertexRagDataService.VertexRagDataServiceClient
title: Vertex AI v1beta1 API - Class VertexRagDataService.VertexRagDataServiceClient (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:59.630192+00:00
---

# Vertex AI v1beta1 API - Class VertexRagDataService.VertexRagDataServiceClient (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.VertexRagDataService.VertexRagDataServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class VertexRagDataService.VertexRagDataServiceClient (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public class VertexRagDataService.VertexRagDataServiceClient : ClientBase<VertexRagDataService.VertexRagDataServiceClient>

Reference documentation and code samples for the Vertex AI v1beta1 API class VertexRagDataService.VertexRagDataServiceClient.

Client for VertexRagDataService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[VertexRagDataService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.VertexRagDataService)[VertexRagDataServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.VertexRagDataService.VertexRagDataServiceClient) > VertexRagDataService.VertexRagDataServiceClient

## Inherited Members

[ClientBase<VertexRagDataService.VertexRagDataServiceClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

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

### VertexRagDataServiceClient()
    
    
    protected VertexRagDataServiceClient()

Protected parameterless constructor to allow creation of test doubles.

### VertexRagDataServiceClient(CallInvoker)
    
    
    public VertexRagDataServiceClient(CallInvoker callInvoker)

Creates a new client for VertexRagDataService that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### VertexRagDataServiceClient(ChannelBase)
    
    
    public VertexRagDataServiceClient(ChannelBase channel)

Creates a new client for VertexRagDataService

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### VertexRagDataServiceClient(ClientBaseConfiguration)
    
    
    protected VertexRagDataServiceClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### BatchCreateRagDataSchemas(BatchCreateRagDataSchemasRequest, CallOptions)
    
    
    public virtual Operation BatchCreateRagDataSchemas(BatchCreateRagDataSchemasRequest request, CallOptions options)

Batch Create one or more RagDataSchemas

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateRagDataSchemasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateRagDataSchemasRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### BatchCreateRagDataSchemas(BatchCreateRagDataSchemasRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation BatchCreateRagDataSchemas(BatchCreateRagDataSchemasRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Batch Create one or more RagDataSchemas

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateRagDataSchemasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateRagDataSchemasRequest)`  
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
  
### BatchCreateRagDataSchemasAsync(BatchCreateRagDataSchemasRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> BatchCreateRagDataSchemasAsync(BatchCreateRagDataSchemasRequest request, CallOptions options)

Batch Create one or more RagDataSchemas

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateRagDataSchemasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateRagDataSchemasRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### BatchCreateRagDataSchemasAsync(BatchCreateRagDataSchemasRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> BatchCreateRagDataSchemasAsync(BatchCreateRagDataSchemasRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Batch Create one or more RagDataSchemas

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateRagDataSchemasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateRagDataSchemasRequest)`  
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
  
### BatchCreateRagMetadata(BatchCreateRagMetadataRequest, CallOptions)
    
    
    public virtual Operation BatchCreateRagMetadata(BatchCreateRagMetadataRequest request, CallOptions options)

Batch Create one or more RagMetadatas

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateRagMetadataRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### BatchCreateRagMetadata(BatchCreateRagMetadataRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation BatchCreateRagMetadata(BatchCreateRagMetadataRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Batch Create one or more RagMetadatas

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateRagMetadataRequest)`  
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
  
### BatchCreateRagMetadataAsync(BatchCreateRagMetadataRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> BatchCreateRagMetadataAsync(BatchCreateRagMetadataRequest request, CallOptions options)

Batch Create one or more RagMetadatas

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateRagMetadataRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### BatchCreateRagMetadataAsync(BatchCreateRagMetadataRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> BatchCreateRagMetadataAsync(BatchCreateRagMetadataRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Batch Create one or more RagMetadatas

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateRagMetadataRequest)`  
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
  
### BatchDeleteRagDataSchemas(BatchDeleteRagDataSchemasRequest, CallOptions)
    
    
    public virtual Operation BatchDeleteRagDataSchemas(BatchDeleteRagDataSchemasRequest request, CallOptions options)

Batch Deletes one or more RagDataSchemas

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteRagDataSchemasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchDeleteRagDataSchemasRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### BatchDeleteRagDataSchemas(BatchDeleteRagDataSchemasRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation BatchDeleteRagDataSchemas(BatchDeleteRagDataSchemasRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Batch Deletes one or more RagDataSchemas

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteRagDataSchemasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchDeleteRagDataSchemasRequest)`  
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
  
### BatchDeleteRagDataSchemasAsync(BatchDeleteRagDataSchemasRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> BatchDeleteRagDataSchemasAsync(BatchDeleteRagDataSchemasRequest request, CallOptions options)

Batch Deletes one or more RagDataSchemas

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteRagDataSchemasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchDeleteRagDataSchemasRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### BatchDeleteRagDataSchemasAsync(BatchDeleteRagDataSchemasRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> BatchDeleteRagDataSchemasAsync(BatchDeleteRagDataSchemasRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Batch Deletes one or more RagDataSchemas

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteRagDataSchemasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchDeleteRagDataSchemasRequest)`  
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
  
### BatchDeleteRagMetadata(BatchDeleteRagMetadataRequest, CallOptions)
    
    
    public virtual Operation BatchDeleteRagMetadata(BatchDeleteRagMetadataRequest request, CallOptions options)

Batch Deletes one or more RagMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchDeleteRagMetadataRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### BatchDeleteRagMetadata(BatchDeleteRagMetadataRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation BatchDeleteRagMetadata(BatchDeleteRagMetadataRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Batch Deletes one or more RagMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchDeleteRagMetadataRequest)`  
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
  
### BatchDeleteRagMetadataAsync(BatchDeleteRagMetadataRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> BatchDeleteRagMetadataAsync(BatchDeleteRagMetadataRequest request, CallOptions options)

Batch Deletes one or more RagMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchDeleteRagMetadataRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### BatchDeleteRagMetadataAsync(BatchDeleteRagMetadataRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> BatchDeleteRagMetadataAsync(BatchDeleteRagMetadataRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Batch Deletes one or more RagMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchDeleteRagMetadataRequest)`  
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
  
### CreateRagCorpus(CreateRagCorpusRequest, CallOptions)
    
    
    public virtual Operation CreateRagCorpus(CreateRagCorpusRequest request, CallOptions options)

Creates a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRagCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateRagCorpusRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateRagCorpus(CreateRagCorpusRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateRagCorpus(CreateRagCorpusRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRagCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateRagCorpusRequest)`  
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
  
### CreateRagCorpusAsync(CreateRagCorpusRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateRagCorpusAsync(CreateRagCorpusRequest request, CallOptions options)

Creates a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRagCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateRagCorpusRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateRagCorpusAsync(CreateRagCorpusRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateRagCorpusAsync(CreateRagCorpusRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRagCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateRagCorpusRequest)`  
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
  
### CreateRagDataSchema(CreateRagDataSchemaRequest, CallOptions)
    
    
    public virtual RagDataSchema CreateRagDataSchema(CreateRagDataSchemaRequest request, CallOptions options)

Creates a RagDataSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRagDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateRagDataSchemaRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[RagDataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchema)` | The response received from the server.  
  
### CreateRagDataSchema(CreateRagDataSchemaRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual RagDataSchema CreateRagDataSchema(CreateRagDataSchemaRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a RagDataSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRagDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateRagDataSchemaRequest)`  
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
`[RagDataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchema)` | The response received from the server.  
  
### CreateRagDataSchemaAsync(CreateRagDataSchemaRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<RagDataSchema> CreateRagDataSchemaAsync(CreateRagDataSchemaRequest request, CallOptions options)

Creates a RagDataSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRagDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateRagDataSchemaRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[RagDataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchema)` | The call object.  
  
### CreateRagDataSchemaAsync(CreateRagDataSchemaRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<RagDataSchema> CreateRagDataSchemaAsync(CreateRagDataSchemaRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a RagDataSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRagDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateRagDataSchemaRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[RagDataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchema)` | The call object.  
  
### CreateRagMetadata(CreateRagMetadataRequest, CallOptions)
    
    
    public virtual RagMetadata CreateRagMetadata(CreateRagMetadataRequest request, CallOptions options)

Creates a RagMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateRagMetadataRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[RagMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagMetadata)` | The response received from the server.  
  
### CreateRagMetadata(CreateRagMetadataRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual RagMetadata CreateRagMetadata(CreateRagMetadataRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a RagMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateRagMetadataRequest)`  
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
`[RagMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagMetadata)` | The response received from the server.  
  
### CreateRagMetadataAsync(CreateRagMetadataRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<RagMetadata> CreateRagMetadataAsync(CreateRagMetadataRequest request, CallOptions options)

Creates a RagMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateRagMetadataRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[RagMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagMetadata)` | The call object.  
  
### CreateRagMetadataAsync(CreateRagMetadataRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<RagMetadata> CreateRagMetadataAsync(CreateRagMetadataRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a RagMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateRagMetadataRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[RagMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagMetadata)` | The call object.  
  
### DeleteRagCorpus(DeleteRagCorpusRequest, CallOptions)
    
    
    public virtual Operation DeleteRagCorpus(DeleteRagCorpusRequest request, CallOptions options)

Deletes a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRagCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteRagCorpusRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteRagCorpus(DeleteRagCorpusRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteRagCorpus(DeleteRagCorpusRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRagCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteRagCorpusRequest)`  
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
  
### DeleteRagCorpusAsync(DeleteRagCorpusRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteRagCorpusAsync(DeleteRagCorpusRequest request, CallOptions options)

Deletes a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRagCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteRagCorpusRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteRagCorpusAsync(DeleteRagCorpusRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteRagCorpusAsync(DeleteRagCorpusRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRagCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteRagCorpusRequest)`  
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
  
### DeleteRagDataSchema(DeleteRagDataSchemaRequest, CallOptions)
    
    
    public virtual Empty DeleteRagDataSchema(DeleteRagDataSchemaRequest request, CallOptions options)

Deletes a RagDataSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRagDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteRagDataSchemaRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteRagDataSchema(DeleteRagDataSchemaRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteRagDataSchema(DeleteRagDataSchemaRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a RagDataSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRagDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteRagDataSchemaRequest)`  
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
  
### DeleteRagDataSchemaAsync(DeleteRagDataSchemaRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteRagDataSchemaAsync(DeleteRagDataSchemaRequest request, CallOptions options)

Deletes a RagDataSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRagDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteRagDataSchemaRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteRagDataSchemaAsync(DeleteRagDataSchemaRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteRagDataSchemaAsync(DeleteRagDataSchemaRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a RagDataSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRagDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteRagDataSchemaRequest)`  
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
  
### DeleteRagFile(DeleteRagFileRequest, CallOptions)
    
    
    public virtual Operation DeleteRagFile(DeleteRagFileRequest request, CallOptions options)

Deletes a RagFile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRagFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteRagFileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteRagFile(DeleteRagFileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteRagFile(DeleteRagFileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a RagFile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRagFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteRagFileRequest)`  
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
  
### DeleteRagFileAsync(DeleteRagFileRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteRagFileAsync(DeleteRagFileRequest request, CallOptions options)

Deletes a RagFile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRagFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteRagFileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteRagFileAsync(DeleteRagFileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteRagFileAsync(DeleteRagFileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a RagFile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRagFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteRagFileRequest)`  
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
  
### DeleteRagMetadata(DeleteRagMetadataRequest, CallOptions)
    
    
    public virtual Empty DeleteRagMetadata(DeleteRagMetadataRequest request, CallOptions options)

Deletes a RagMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteRagMetadataRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteRagMetadata(DeleteRagMetadataRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteRagMetadata(DeleteRagMetadataRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a RagMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteRagMetadataRequest)`  
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
  
### DeleteRagMetadataAsync(DeleteRagMetadataRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteRagMetadataAsync(DeleteRagMetadataRequest request, CallOptions options)

Deletes a RagMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteRagMetadataRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteRagMetadataAsync(DeleteRagMetadataRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteRagMetadataAsync(DeleteRagMetadataRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a RagMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteRagMetadataRequest)`  
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
  
### GetRagCorpus(GetRagCorpusRequest, CallOptions)
    
    
    public virtual RagCorpus GetRagCorpus(GetRagCorpusRequest request, CallOptions options)

Gets a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRagCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetRagCorpusRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[RagCorpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagCorpus)` | The response received from the server.  
  
### GetRagCorpus(GetRagCorpusRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual RagCorpus GetRagCorpus(GetRagCorpusRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRagCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetRagCorpusRequest)`  
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
`[RagCorpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagCorpus)` | The response received from the server.  
  
### GetRagCorpusAsync(GetRagCorpusRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<RagCorpus> GetRagCorpusAsync(GetRagCorpusRequest request, CallOptions options)

Gets a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRagCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetRagCorpusRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[RagCorpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagCorpus)` | The call object.  
  
### GetRagCorpusAsync(GetRagCorpusRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<RagCorpus> GetRagCorpusAsync(GetRagCorpusRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRagCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetRagCorpusRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[RagCorpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagCorpus)` | The call object.  
  
### GetRagDataSchema(GetRagDataSchemaRequest, CallOptions)
    
    
    public virtual RagDataSchema GetRagDataSchema(GetRagDataSchemaRequest request, CallOptions options)

Gets a RagDataSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRagDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetRagDataSchemaRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[RagDataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchema)` | The response received from the server.  
  
### GetRagDataSchema(GetRagDataSchemaRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual RagDataSchema GetRagDataSchema(GetRagDataSchemaRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets a RagDataSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRagDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetRagDataSchemaRequest)`  
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
`[RagDataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchema)` | The response received from the server.  
  
### GetRagDataSchemaAsync(GetRagDataSchemaRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<RagDataSchema> GetRagDataSchemaAsync(GetRagDataSchemaRequest request, CallOptions options)

Gets a RagDataSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRagDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetRagDataSchemaRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[RagDataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchema)` | The call object.  
  
### GetRagDataSchemaAsync(GetRagDataSchemaRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<RagDataSchema> GetRagDataSchemaAsync(GetRagDataSchemaRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets a RagDataSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRagDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetRagDataSchemaRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[RagDataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchema)` | The call object.  
  
### GetRagEngineConfig(GetRagEngineConfigRequest, CallOptions)
    
    
    public virtual RagEngineConfig GetRagEngineConfig(GetRagEngineConfigRequest request, CallOptions options)

Gets a RagEngineConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRagEngineConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetRagEngineConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[RagEngineConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagEngineConfig)` | The response received from the server.  
  
### GetRagEngineConfig(GetRagEngineConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual RagEngineConfig GetRagEngineConfig(GetRagEngineConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets a RagEngineConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRagEngineConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetRagEngineConfigRequest)`  
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
`[RagEngineConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagEngineConfig)` | The response received from the server.  
  
### GetRagEngineConfigAsync(GetRagEngineConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<RagEngineConfig> GetRagEngineConfigAsync(GetRagEngineConfigRequest request, CallOptions options)

Gets a RagEngineConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRagEngineConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetRagEngineConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[RagEngineConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagEngineConfig)` | The call object.  
  
### GetRagEngineConfigAsync(GetRagEngineConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<RagEngineConfig> GetRagEngineConfigAsync(GetRagEngineConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets a RagEngineConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRagEngineConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetRagEngineConfigRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[RagEngineConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagEngineConfig)` | The call object.  
  
### GetRagFile(GetRagFileRequest, CallOptions)
    
    
    public virtual RagFile GetRagFile(GetRagFileRequest request, CallOptions options)

Gets a RagFile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRagFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetRagFileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[RagFile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagFile)` | The response received from the server.  
  
### GetRagFile(GetRagFileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual RagFile GetRagFile(GetRagFileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets a RagFile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRagFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetRagFileRequest)`  
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
`[RagFile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagFile)` | The response received from the server.  
  
### GetRagFileAsync(GetRagFileRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<RagFile> GetRagFileAsync(GetRagFileRequest request, CallOptions options)

Gets a RagFile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRagFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetRagFileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[RagFile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagFile)` | The call object.  
  
### GetRagFileAsync(GetRagFileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<RagFile> GetRagFileAsync(GetRagFileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets a RagFile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRagFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetRagFileRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[RagFile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagFile)` | The call object.  
  
### GetRagMetadata(GetRagMetadataRequest, CallOptions)
    
    
    public virtual RagMetadata GetRagMetadata(GetRagMetadataRequest request, CallOptions options)

Gets a RagMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetRagMetadataRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[RagMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagMetadata)` | The response received from the server.  
  
### GetRagMetadata(GetRagMetadataRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual RagMetadata GetRagMetadata(GetRagMetadataRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets a RagMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetRagMetadataRequest)`  
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
`[RagMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagMetadata)` | The response received from the server.  
  
### GetRagMetadataAsync(GetRagMetadataRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<RagMetadata> GetRagMetadataAsync(GetRagMetadataRequest request, CallOptions options)

Gets a RagMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetRagMetadataRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[RagMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagMetadata)` | The call object.  
  
### GetRagMetadataAsync(GetRagMetadataRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<RagMetadata> GetRagMetadataAsync(GetRagMetadataRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets a RagMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetRagMetadataRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[RagMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagMetadata)` | The call object.  
  
### ImportRagFiles(ImportRagFilesRequest, CallOptions)
    
    
    public virtual Operation ImportRagFiles(ImportRagFilesRequest request, CallOptions options)

Import files from Google Cloud Storage or Google Drive into a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportRagFilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ImportRagFilesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### ImportRagFiles(ImportRagFilesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation ImportRagFiles(ImportRagFilesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Import files from Google Cloud Storage or Google Drive into a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportRagFilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ImportRagFilesRequest)`  
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
  
### ImportRagFilesAsync(ImportRagFilesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> ImportRagFilesAsync(ImportRagFilesRequest request, CallOptions options)

Import files from Google Cloud Storage or Google Drive into a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportRagFilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ImportRagFilesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### ImportRagFilesAsync(ImportRagFilesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> ImportRagFilesAsync(ImportRagFilesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Import files from Google Cloud Storage or Google Drive into a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportRagFilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ImportRagFilesRequest)`  
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
  
### ListRagCorpora(ListRagCorporaRequest, CallOptions)
    
    
    public virtual ListRagCorporaResponse ListRagCorpora(ListRagCorporaRequest request, CallOptions options)

Lists RagCorpora in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRagCorporaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagCorporaRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListRagCorporaResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagCorporaResponse)` | The response received from the server.  
  
### ListRagCorpora(ListRagCorporaRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListRagCorporaResponse ListRagCorpora(ListRagCorporaRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists RagCorpora in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRagCorporaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagCorporaRequest)`  
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
`[ListRagCorporaResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagCorporaResponse)` | The response received from the server.  
  
### ListRagCorporaAsync(ListRagCorporaRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListRagCorporaResponse> ListRagCorporaAsync(ListRagCorporaRequest request, CallOptions options)

Lists RagCorpora in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRagCorporaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagCorporaRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListRagCorporaResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagCorporaResponse)` | The call object.  
  
### ListRagCorporaAsync(ListRagCorporaRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListRagCorporaResponse> ListRagCorporaAsync(ListRagCorporaRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists RagCorpora in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRagCorporaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagCorporaRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListRagCorporaResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagCorporaResponse)` | The call object.  
  
### ListRagDataSchemas(ListRagDataSchemasRequest, CallOptions)
    
    
    public virtual ListRagDataSchemasResponse ListRagDataSchemas(ListRagDataSchemasRequest request, CallOptions options)

Lists RagDataSchemas in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRagDataSchemasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagDataSchemasRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListRagDataSchemasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagDataSchemasResponse)` | The response received from the server.  
  
### ListRagDataSchemas(ListRagDataSchemasRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListRagDataSchemasResponse ListRagDataSchemas(ListRagDataSchemasRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists RagDataSchemas in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRagDataSchemasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagDataSchemasRequest)`  
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
`[ListRagDataSchemasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagDataSchemasResponse)` | The response received from the server.  
  
### ListRagDataSchemasAsync(ListRagDataSchemasRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListRagDataSchemasResponse> ListRagDataSchemasAsync(ListRagDataSchemasRequest request, CallOptions options)

Lists RagDataSchemas in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRagDataSchemasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagDataSchemasRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListRagDataSchemasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagDataSchemasResponse)` | The call object.  
  
### ListRagDataSchemasAsync(ListRagDataSchemasRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListRagDataSchemasResponse> ListRagDataSchemasAsync(ListRagDataSchemasRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists RagDataSchemas in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRagDataSchemasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagDataSchemasRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListRagDataSchemasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagDataSchemasResponse)` | The call object.  
  
### ListRagFiles(ListRagFilesRequest, CallOptions)
    
    
    public virtual ListRagFilesResponse ListRagFiles(ListRagFilesRequest request, CallOptions options)

Lists RagFiles in a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRagFilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagFilesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListRagFilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagFilesResponse)` | The response received from the server.  
  
### ListRagFiles(ListRagFilesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListRagFilesResponse ListRagFiles(ListRagFilesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists RagFiles in a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRagFilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagFilesRequest)`  
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
`[ListRagFilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagFilesResponse)` | The response received from the server.  
  
### ListRagFilesAsync(ListRagFilesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListRagFilesResponse> ListRagFilesAsync(ListRagFilesRequest request, CallOptions options)

Lists RagFiles in a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRagFilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagFilesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListRagFilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagFilesResponse)` | The call object.  
  
### ListRagFilesAsync(ListRagFilesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListRagFilesResponse> ListRagFilesAsync(ListRagFilesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists RagFiles in a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRagFilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagFilesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListRagFilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagFilesResponse)` | The call object.  
  
### ListRagMetadata(ListRagMetadataRequest, CallOptions)
    
    
    public virtual ListRagMetadataResponse ListRagMetadata(ListRagMetadataRequest request, CallOptions options)

Lists RagMetadata in a RagFile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagMetadataRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListRagMetadataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagMetadataResponse)` | The response received from the server.  
  
### ListRagMetadata(ListRagMetadataRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListRagMetadataResponse ListRagMetadata(ListRagMetadataRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists RagMetadata in a RagFile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagMetadataRequest)`  
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
`[ListRagMetadataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagMetadataResponse)` | The response received from the server.  
  
### ListRagMetadataAsync(ListRagMetadataRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListRagMetadataResponse> ListRagMetadataAsync(ListRagMetadataRequest request, CallOptions options)

Lists RagMetadata in a RagFile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagMetadataRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListRagMetadataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagMetadataResponse)` | The call object.  
  
### ListRagMetadataAsync(ListRagMetadataRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListRagMetadataResponse> ListRagMetadataAsync(ListRagMetadataRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists RagMetadata in a RagFile.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagMetadataRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListRagMetadataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListRagMetadataResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override VertexRagDataService.VertexRagDataServiceClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VertexRagDataService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.VertexRagDataService)[VertexRagDataServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.VertexRagDataService.VertexRagDataServiceClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.AIPlatform.V1Beta1.VertexRagDataService.VertexRagDataServiceClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### UpdateRagCorpus(UpdateRagCorpusRequest, CallOptions)
    
    
    public virtual Operation UpdateRagCorpus(UpdateRagCorpusRequest request, CallOptions options)

Updates a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRagCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateRagCorpusRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateRagCorpus(UpdateRagCorpusRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateRagCorpus(UpdateRagCorpusRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRagCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateRagCorpusRequest)`  
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
  
### UpdateRagCorpusAsync(UpdateRagCorpusRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateRagCorpusAsync(UpdateRagCorpusRequest request, CallOptions options)

Updates a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRagCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateRagCorpusRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateRagCorpusAsync(UpdateRagCorpusRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateRagCorpusAsync(UpdateRagCorpusRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRagCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateRagCorpusRequest)`  
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
  
### UpdateRagEngineConfig(UpdateRagEngineConfigRequest, CallOptions)
    
    
    public virtual Operation UpdateRagEngineConfig(UpdateRagEngineConfigRequest request, CallOptions options)

Updates a RagEngineConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRagEngineConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateRagEngineConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateRagEngineConfig(UpdateRagEngineConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateRagEngineConfig(UpdateRagEngineConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a RagEngineConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRagEngineConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateRagEngineConfigRequest)`  
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
  
### UpdateRagEngineConfigAsync(UpdateRagEngineConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateRagEngineConfigAsync(UpdateRagEngineConfigRequest request, CallOptions options)

Updates a RagEngineConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRagEngineConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateRagEngineConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateRagEngineConfigAsync(UpdateRagEngineConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateRagEngineConfigAsync(UpdateRagEngineConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a RagEngineConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRagEngineConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateRagEngineConfigRequest)`  
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
  
### UpdateRagMetadata(UpdateRagMetadataRequest, CallOptions)
    
    
    public virtual RagMetadata UpdateRagMetadata(UpdateRagMetadataRequest request, CallOptions options)

Updates a RagMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateRagMetadataRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[RagMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagMetadata)` | The response received from the server.  
  
### UpdateRagMetadata(UpdateRagMetadataRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual RagMetadata UpdateRagMetadata(UpdateRagMetadataRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a RagMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateRagMetadataRequest)`  
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
`[RagMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagMetadata)` | The response received from the server.  
  
### UpdateRagMetadataAsync(UpdateRagMetadataRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<RagMetadata> UpdateRagMetadataAsync(UpdateRagMetadataRequest request, CallOptions options)

Updates a RagMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateRagMetadataRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[RagMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagMetadata)` | The call object.  
  
### UpdateRagMetadataAsync(UpdateRagMetadataRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<RagMetadata> UpdateRagMetadataAsync(UpdateRagMetadataRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a RagMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRagMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateRagMetadataRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[RagMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagMetadata)` | The call object.  
  
### UploadRagFile(UploadRagFileRequest, CallOptions)
    
    
    public virtual UploadRagFileResponse UploadRagFile(UploadRagFileRequest request, CallOptions options)

Upload a file into a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UploadRagFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UploadRagFileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[UploadRagFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UploadRagFileResponse)` | The response received from the server.  
  
### UploadRagFile(UploadRagFileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual UploadRagFileResponse UploadRagFile(UploadRagFileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Upload a file into a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UploadRagFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UploadRagFileRequest)`  
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
`[UploadRagFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UploadRagFileResponse)` | The response received from the server.  
  
### UploadRagFileAsync(UploadRagFileRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<UploadRagFileResponse> UploadRagFileAsync(UploadRagFileRequest request, CallOptions options)

Upload a file into a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UploadRagFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UploadRagFileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[UploadRagFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UploadRagFileResponse)` | The call object.  
  
### UploadRagFileAsync(UploadRagFileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<UploadRagFileResponse> UploadRagFileAsync(UploadRagFileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Upload a file into a RagCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UploadRagFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UploadRagFileRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[UploadRagFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UploadRagFileResponse)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
