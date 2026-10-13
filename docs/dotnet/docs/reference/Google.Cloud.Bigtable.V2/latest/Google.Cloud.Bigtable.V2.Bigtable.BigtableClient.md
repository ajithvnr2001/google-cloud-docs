---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Bigtable.BigtableClient
title: Google Bigtable v2 API - Class Bigtable.BigtableClient (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:40.100786+00:00
---

# Google Bigtable v2 API - Class Bigtable.BigtableClient (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Bigtable.BigtableClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class Bigtable.BigtableClient (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public class Bigtable.BigtableClient : ClientBase<Bigtable.BigtableClient>

Reference documentation and code samples for the Google Bigtable v2 API class Bigtable.BigtableClient.

Client for Bigtable

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[Bigtable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Bigtable)[BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Bigtable.BigtableClient) > Bigtable.BigtableClient

## Inherited Members

[ClientBase<Bigtable.BigtableClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Constructors 

### BigtableClient()
    
    
    protected BigtableClient()

Protected parameterless constructor to allow creation of test doubles.

### BigtableClient(CallInvoker)
    
    
    public BigtableClient(CallInvoker callInvoker)

Creates a new client for Bigtable that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### BigtableClient(ChannelBase)
    
    
    public BigtableClient(ChannelBase channel)

Creates a new client for Bigtable

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### BigtableClient(ClientBaseConfiguration)
    
    
    protected BigtableClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### CheckAndMutateRow(CheckAndMutateRowRequest, CallOptions)
    
    
    public virtual CheckAndMutateRowResponse CheckAndMutateRow(CheckAndMutateRowRequest request, CallOptions options)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckAndMutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | The response received from the server.  
  
### CheckAndMutateRow(CheckAndMutateRowRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual CheckAndMutateRowResponse CheckAndMutateRow(CheckAndMutateRowRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckAndMutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | The response received from the server.  
  
### CheckAndMutateRowAsync(CheckAndMutateRowRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<CheckAndMutateRowResponse> CheckAndMutateRowAsync(CheckAndMutateRowRequest request, CallOptions options)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckAndMutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | The call object.  
  
### CheckAndMutateRowAsync(CheckAndMutateRowRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<CheckAndMutateRowResponse> CheckAndMutateRowAsync(CheckAndMutateRowRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckAndMutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | The call object.  
  
### ExecuteQuery(ExecuteQueryRequest, CallOptions)
    
    
    public virtual AsyncServerStreamingCall<ExecuteQueryResponse> ExecuteQuery(ExecuteQueryRequest request, CallOptions options)

Executes a SQL query against a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecuteQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ExecuteQueryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncServerStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncServerStreamingCall-1.html)[ExecuteQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ExecuteQueryResponse)` | The call object.  
  
### ExecuteQuery(ExecuteQueryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncServerStreamingCall<ExecuteQueryResponse> ExecuteQuery(ExecuteQueryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Executes a SQL query against a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecuteQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ExecuteQueryRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncServerStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncServerStreamingCall-1.html)[ExecuteQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ExecuteQueryResponse)` | The call object.  
  
### GenerateInitialChangeStreamPartitions(GenerateInitialChangeStreamPartitionsRequest, CallOptions)
    
    
    public virtual AsyncServerStreamingCall<GenerateInitialChangeStreamPartitionsResponse> GenerateInitialChangeStreamPartitions(GenerateInitialChangeStreamPartitionsRequest request, CallOptions options)

Returns the current list of partitions that make up the table's change stream. The union of partitions will cover the entire keyspace. Partitions can be read with `ReadChangeStream`. NOTE: This API is only intended to be used by Apache Beam BigtableIO.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateInitialChangeStreamPartitionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GenerateInitialChangeStreamPartitionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncServerStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncServerStreamingCall-1.html)[GenerateInitialChangeStreamPartitionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GenerateInitialChangeStreamPartitionsResponse)` | The call object.  
  
### GenerateInitialChangeStreamPartitions(GenerateInitialChangeStreamPartitionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncServerStreamingCall<GenerateInitialChangeStreamPartitionsResponse> GenerateInitialChangeStreamPartitions(GenerateInitialChangeStreamPartitionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the current list of partitions that make up the table's change stream. The union of partitions will cover the entire keyspace. Partitions can be read with `ReadChangeStream`. NOTE: This API is only intended to be used by Apache Beam BigtableIO.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateInitialChangeStreamPartitionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GenerateInitialChangeStreamPartitionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncServerStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncServerStreamingCall-1.html)[GenerateInitialChangeStreamPartitionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GenerateInitialChangeStreamPartitionsResponse)` | The call object.  
  
### GetClientConfiguration(GetClientConfigurationRequest, CallOptions)
    
    
    public virtual ClientConfiguration GetClientConfiguration(GetClientConfigurationRequest request, CallOptions options)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClientConfigurationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GetClientConfigurationRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ClientConfiguration)` | The response received from the server.  
  
### GetClientConfiguration(GetClientConfigurationRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ClientConfiguration GetClientConfiguration(GetClientConfigurationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClientConfigurationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GetClientConfigurationRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ClientConfiguration)` | The response received from the server.  
  
### GetClientConfigurationAsync(GetClientConfigurationRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ClientConfiguration> GetClientConfigurationAsync(GetClientConfigurationRequest request, CallOptions options)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClientConfigurationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GetClientConfigurationRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ClientConfiguration)` | The call object.  
  
### GetClientConfigurationAsync(GetClientConfigurationRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ClientConfiguration> GetClientConfigurationAsync(GetClientConfigurationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClientConfigurationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GetClientConfigurationRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ClientConfiguration)` | The call object.  
  
### MutateRow(MutateRowRequest, CallOptions)
    
    
    public virtual MutateRowResponse MutateRow(MutateRowRequest request, CallOptions options)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | The response received from the server.  
  
### MutateRow(MutateRowRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual MutateRowResponse MutateRow(MutateRowRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | The response received from the server.  
  
### MutateRowAsync(MutateRowRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<MutateRowResponse> MutateRowAsync(MutateRowRequest request, CallOptions options)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | The call object.  
  
### MutateRowAsync(MutateRowRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<MutateRowResponse> MutateRowAsync(MutateRowRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | The call object.  
  
### MutateRows(MutateRowsRequest, CallOptions)
    
    
    public virtual AsyncServerStreamingCall<MutateRowsResponse> MutateRows(MutateRowsRequest request, CallOptions options)

Mutates multiple rows in a batch. Each individual row is mutated atomically as in MutateRow, but the entire batch is not executed atomically.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MutateRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncServerStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncServerStreamingCall-1.html)[MutateRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsResponse)` | The call object.  
  
### MutateRows(MutateRowsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncServerStreamingCall<MutateRowsResponse> MutateRows(MutateRowsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Mutates multiple rows in a batch. Each individual row is mutated atomically as in MutateRow, but the entire batch is not executed atomically.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MutateRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncServerStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncServerStreamingCall-1.html)[MutateRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override Bigtable.BigtableClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Bigtable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Bigtable)[BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Bigtable.BigtableClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Bigtable.V2.Bigtable.BigtableClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### OpenAuthorizedView(CallOptions)
    
    
    public virtual AsyncDuplexStreamingCall<SessionRequest, SessionResponse> OpenAuthorizedView(CallOptions options)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameter**  
---  
**Name** | **Description**  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncDuplexStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncDuplexStreamingCall-2.html)[SessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionRequest)[SessionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionResponse)` | The call object.  
  
### OpenAuthorizedView(Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncDuplexStreamingCall<SessionRequest, SessionResponse> OpenAuthorizedView(Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncDuplexStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncDuplexStreamingCall-2.html)[SessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionRequest)[SessionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionResponse)` | The call object.  
  
### OpenMaterializedView(CallOptions)
    
    
    public virtual AsyncDuplexStreamingCall<SessionRequest, SessionResponse> OpenMaterializedView(CallOptions options)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameter**  
---  
**Name** | **Description**  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncDuplexStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncDuplexStreamingCall-2.html)[SessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionRequest)[SessionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionResponse)` | The call object.  
  
### OpenMaterializedView(Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncDuplexStreamingCall<SessionRequest, SessionResponse> OpenMaterializedView(Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncDuplexStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncDuplexStreamingCall-2.html)[SessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionRequest)[SessionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionResponse)` | The call object.  
  
### OpenTable(CallOptions)
    
    
    public virtual AsyncDuplexStreamingCall<SessionRequest, SessionResponse> OpenTable(CallOptions options)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameter**  
---  
**Name** | **Description**  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncDuplexStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncDuplexStreamingCall-2.html)[SessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionRequest)[SessionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionResponse)` | The call object.  
  
### OpenTable(Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncDuplexStreamingCall<SessionRequest, SessionResponse> OpenTable(Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncDuplexStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncDuplexStreamingCall-2.html)[SessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionRequest)[SessionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionResponse)` | The call object.  
  
### PingAndWarm(PingAndWarmRequest, CallOptions)
    
    
    public virtual PingAndWarmResponse PingAndWarm(PingAndWarmRequest request, CallOptions options)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PingAndWarmRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | The response received from the server.  
  
### PingAndWarm(PingAndWarmRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual PingAndWarmResponse PingAndWarm(PingAndWarmRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PingAndWarmRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | The response received from the server.  
  
### PingAndWarmAsync(PingAndWarmRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<PingAndWarmResponse> PingAndWarmAsync(PingAndWarmRequest request, CallOptions options)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PingAndWarmRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | The call object.  
  
### PingAndWarmAsync(PingAndWarmRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<PingAndWarmResponse> PingAndWarmAsync(PingAndWarmRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PingAndWarmRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | The call object.  
  
### PrepareQuery(PrepareQueryRequest, CallOptions)
    
    
    public virtual PrepareQueryResponse PrepareQuery(PrepareQueryRequest request, CallOptions options)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PrepareQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | The response received from the server.  
  
### PrepareQuery(PrepareQueryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual PrepareQueryResponse PrepareQuery(PrepareQueryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PrepareQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | The response received from the server.  
  
### PrepareQueryAsync(PrepareQueryRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<PrepareQueryResponse> PrepareQueryAsync(PrepareQueryRequest request, CallOptions options)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PrepareQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | The call object.  
  
### PrepareQueryAsync(PrepareQueryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<PrepareQueryResponse> PrepareQueryAsync(PrepareQueryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PrepareQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | The call object.  
  
### ReadChangeStream(ReadChangeStreamRequest, CallOptions)
    
    
    public virtual AsyncServerStreamingCall<ReadChangeStreamResponse> ReadChangeStream(ReadChangeStreamRequest request, CallOptions options)

Reads changes from a table's change stream. Changes will reflect both user-initiated mutations and mutations that are caused by garbage collection. NOTE: This API is only intended to be used by Apache Beam BigtableIO.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadChangeStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncServerStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncServerStreamingCall-1.html)[ReadChangeStreamResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse)` | The call object.  
  
### ReadChangeStream(ReadChangeStreamRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncServerStreamingCall<ReadChangeStreamResponse> ReadChangeStream(ReadChangeStreamRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Reads changes from a table's change stream. Changes will reflect both user-initiated mutations and mutations that are caused by garbage collection. NOTE: This API is only intended to be used by Apache Beam BigtableIO.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadChangeStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncServerStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncServerStreamingCall-1.html)[ReadChangeStreamResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse)` | The call object.  
  
### ReadModifyWriteRow(ReadModifyWriteRowRequest, CallOptions)
    
    
    public virtual ReadModifyWriteRowResponse ReadModifyWriteRow(ReadModifyWriteRowRequest request, CallOptions options)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadModifyWriteRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | The response received from the server.  
  
### ReadModifyWriteRow(ReadModifyWriteRowRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ReadModifyWriteRowResponse ReadModifyWriteRow(ReadModifyWriteRowRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadModifyWriteRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | The response received from the server.  
  
### ReadModifyWriteRowAsync(ReadModifyWriteRowRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ReadModifyWriteRowResponse> ReadModifyWriteRowAsync(ReadModifyWriteRowRequest request, CallOptions options)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadModifyWriteRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | The call object.  
  
### ReadModifyWriteRowAsync(ReadModifyWriteRowRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ReadModifyWriteRowResponse> ReadModifyWriteRowAsync(ReadModifyWriteRowRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadModifyWriteRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | The call object.  
  
### ReadRows(ReadRowsRequest, CallOptions)
    
    
    public virtual AsyncServerStreamingCall<ReadRowsResponse> ReadRows(ReadRowsRequest request, CallOptions options)

Streams back the contents of all requested rows in key order, optionally applying the same Reader filter to each. Depending on their size, rows and cells may be broken up across multiple responses, but atomicity of each row will still be preserved. See the ReadRowsResponse documentation for details.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncServerStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncServerStreamingCall-1.html)[ReadRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse)` | The call object.  
  
### ReadRows(ReadRowsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncServerStreamingCall<ReadRowsResponse> ReadRows(ReadRowsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Streams back the contents of all requested rows in key order, optionally applying the same Reader filter to each. Depending on their size, rows and cells may be broken up across multiple responses, but atomicity of each row will still be preserved. See the ReadRowsResponse documentation for details.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncServerStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncServerStreamingCall-1.html)[ReadRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse)` | The call object.  
  
### SampleRowKeys(SampleRowKeysRequest, CallOptions)
    
    
    public virtual AsyncServerStreamingCall<SampleRowKeysResponse> SampleRowKeys(SampleRowKeysRequest request, CallOptions options)

Returns a sample of row keys in the table. The returned row keys will delimit contiguous sections of the table of approximately equal size, which can be used to break up the data for distributed tasks like mapreduces.

If a `row_range` is provided in the request, the returned samples will be restricted to the specified range.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SampleRowKeysRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SampleRowKeysRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncServerStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncServerStreamingCall-1.html)[SampleRowKeysResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SampleRowKeysResponse)` | The call object.  
  
### SampleRowKeys(SampleRowKeysRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncServerStreamingCall<SampleRowKeysResponse> SampleRowKeys(SampleRowKeysRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a sample of row keys in the table. The returned row keys will delimit contiguous sections of the table of approximately equal size, which can be used to break up the data for distributed tasks like mapreduces.

If a `row_range` is provided in the request, the returned samples will be restricted to the specified range.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SampleRowKeysRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SampleRowKeysRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncServerStreamingCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncServerStreamingCall-1.html)[SampleRowKeysResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SampleRowKeysResponse)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
