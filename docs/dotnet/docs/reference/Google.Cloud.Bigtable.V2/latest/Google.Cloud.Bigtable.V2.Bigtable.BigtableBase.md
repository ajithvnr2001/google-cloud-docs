---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Bigtable.BigtableBase
title: Google Bigtable v2 API - Class Bigtable.BigtableBase (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:38.689889+00:00
---

# Google Bigtable v2 API - Class Bigtable.BigtableBase (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Bigtable.BigtableBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class Bigtable.BigtableBase (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    [BindServiceMethod(typeof(Bigtable), "BindService")]
    public abstract class Bigtable.BigtableBase

Reference documentation and code samples for the Google Bigtable v2 API class Bigtable.BigtableBase.

Base class for server-side implementations of Bigtable

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Bigtable.BigtableBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Methods 

### CheckAndMutateRow(CheckAndMutateRowRequest, ServerCallContext)
    
    
    public virtual Task<CheckAndMutateRowResponse> CheckAndMutateRow(CheckAndMutateRowRequest request, ServerCallContext context)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckAndMutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | The response to send back to the client (wrapped by a task).  
  
### ExecuteQuery(ExecuteQueryRequest, IServerStreamWriter<ExecuteQueryResponse>, ServerCallContext)
    
    
    public virtual Task ExecuteQuery(ExecuteQueryRequest request, IServerStreamWriter<ExecuteQueryResponse> responseStream, ServerCallContext context)

Executes a SQL query against a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecuteQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ExecuteQueryRequest)`  
The request received from the client.  
`responseStream` | `[IServerStreamWriter](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IServerStreamWriter-1.html)[ExecuteQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ExecuteQueryResponse)`  
Used for sending responses back to the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task indicating completion of the handler.  
  
### GenerateInitialChangeStreamPartitions(GenerateInitialChangeStreamPartitionsRequest, IServerStreamWriter<GenerateInitialChangeStreamPartitionsResponse>, ServerCallContext)
    
    
    public virtual Task GenerateInitialChangeStreamPartitions(GenerateInitialChangeStreamPartitionsRequest request, IServerStreamWriter<GenerateInitialChangeStreamPartitionsResponse> responseStream, ServerCallContext context)

Returns the current list of partitions that make up the table's change stream. The union of partitions will cover the entire keyspace. Partitions can be read with `ReadChangeStream`. NOTE: This API is only intended to be used by Apache Beam BigtableIO.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateInitialChangeStreamPartitionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GenerateInitialChangeStreamPartitionsRequest)`  
The request received from the client.  
`responseStream` | `[IServerStreamWriter](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IServerStreamWriter-1.html)[GenerateInitialChangeStreamPartitionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GenerateInitialChangeStreamPartitionsResponse)`  
Used for sending responses back to the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task indicating completion of the handler.  
  
### GetClientConfiguration(GetClientConfigurationRequest, ServerCallContext)
    
    
    public virtual Task<ClientConfiguration> GetClientConfiguration(GetClientConfigurationRequest request, ServerCallContext context)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClientConfigurationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GetClientConfigurationRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ClientConfiguration)` | The response to send back to the client (wrapped by a task).  
  
### MutateRow(MutateRowRequest, ServerCallContext)
    
    
    public virtual Task<MutateRowResponse> MutateRow(MutateRowRequest request, ServerCallContext context)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | The response to send back to the client (wrapped by a task).  
  
### MutateRows(MutateRowsRequest, IServerStreamWriter<MutateRowsResponse>, ServerCallContext)
    
    
    public virtual Task MutateRows(MutateRowsRequest request, IServerStreamWriter<MutateRowsResponse> responseStream, ServerCallContext context)

Mutates multiple rows in a batch. Each individual row is mutated atomically as in MutateRow, but the entire batch is not executed atomically.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MutateRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest)`  
The request received from the client.  
`responseStream` | `[IServerStreamWriter](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IServerStreamWriter-1.html)[MutateRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsResponse)`  
Used for sending responses back to the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task indicating completion of the handler.  
  
### OpenAuthorizedView(IAsyncStreamReader<SessionRequest>, IServerStreamWriter<SessionResponse>, ServerCallContext)
    
    
    public virtual Task OpenAuthorizedView(IAsyncStreamReader<SessionRequest> requestStream, IServerStreamWriter<SessionResponse> responseStream, ServerCallContext context)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`requestStream` | `[IAsyncStreamReader](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IAsyncStreamReader-1.html)[SessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionRequest)`  
Used for reading requests from the client.  
`responseStream` | `[IServerStreamWriter](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IServerStreamWriter-1.html)[SessionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionResponse)`  
Used for sending responses back to the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task indicating completion of the handler.  
  
### OpenMaterializedView(IAsyncStreamReader<SessionRequest>, IServerStreamWriter<SessionResponse>, ServerCallContext)
    
    
    public virtual Task OpenMaterializedView(IAsyncStreamReader<SessionRequest> requestStream, IServerStreamWriter<SessionResponse> responseStream, ServerCallContext context)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`requestStream` | `[IAsyncStreamReader](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IAsyncStreamReader-1.html)[SessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionRequest)`  
Used for reading requests from the client.  
`responseStream` | `[IServerStreamWriter](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IServerStreamWriter-1.html)[SessionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionResponse)`  
Used for sending responses back to the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task indicating completion of the handler.  
  
### OpenTable(IAsyncStreamReader<SessionRequest>, IServerStreamWriter<SessionResponse>, ServerCallContext)
    
    
    public virtual Task OpenTable(IAsyncStreamReader<SessionRequest> requestStream, IServerStreamWriter<SessionResponse> responseStream, ServerCallContext context)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`requestStream` | `[IAsyncStreamReader](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IAsyncStreamReader-1.html)[SessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionRequest)`  
Used for reading requests from the client.  
`responseStream` | `[IServerStreamWriter](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IServerStreamWriter-1.html)[SessionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionResponse)`  
Used for sending responses back to the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task indicating completion of the handler.  
  
### PingAndWarm(PingAndWarmRequest, ServerCallContext)
    
    
    public virtual Task<PingAndWarmResponse> PingAndWarm(PingAndWarmRequest request, ServerCallContext context)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PingAndWarmRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | The response to send back to the client (wrapped by a task).  
  
### PrepareQuery(PrepareQueryRequest, ServerCallContext)
    
    
    public virtual Task<PrepareQueryResponse> PrepareQuery(PrepareQueryRequest request, ServerCallContext context)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PrepareQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | The response to send back to the client (wrapped by a task).  
  
### ReadChangeStream(ReadChangeStreamRequest, IServerStreamWriter<ReadChangeStreamResponse>, ServerCallContext)
    
    
    public virtual Task ReadChangeStream(ReadChangeStreamRequest request, IServerStreamWriter<ReadChangeStreamResponse> responseStream, ServerCallContext context)

Reads changes from a table's change stream. Changes will reflect both user-initiated mutations and mutations that are caused by garbage collection. NOTE: This API is only intended to be used by Apache Beam BigtableIO.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadChangeStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamRequest)`  
The request received from the client.  
`responseStream` | `[IServerStreamWriter](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IServerStreamWriter-1.html)[ReadChangeStreamResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse)`  
Used for sending responses back to the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task indicating completion of the handler.  
  
### ReadModifyWriteRow(ReadModifyWriteRowRequest, ServerCallContext)
    
    
    public virtual Task<ReadModifyWriteRowResponse> ReadModifyWriteRow(ReadModifyWriteRowRequest request, ServerCallContext context)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadModifyWriteRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | The response to send back to the client (wrapped by a task).  
  
### ReadRows(ReadRowsRequest, IServerStreamWriter<ReadRowsResponse>, ServerCallContext)
    
    
    public virtual Task ReadRows(ReadRowsRequest request, IServerStreamWriter<ReadRowsResponse> responseStream, ServerCallContext context)

Streams back the contents of all requested rows in key order, optionally applying the same Reader filter to each. Depending on their size, rows and cells may be broken up across multiple responses, but atomicity of each row will still be preserved. See the ReadRowsResponse documentation for details.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsRequest)`  
The request received from the client.  
`responseStream` | `[IServerStreamWriter](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IServerStreamWriter-1.html)[ReadRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse)`  
Used for sending responses back to the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task indicating completion of the handler.  
  
### SampleRowKeys(SampleRowKeysRequest, IServerStreamWriter<SampleRowKeysResponse>, ServerCallContext)
    
    
    public virtual Task SampleRowKeys(SampleRowKeysRequest request, IServerStreamWriter<SampleRowKeysResponse> responseStream, ServerCallContext context)

Returns a sample of row keys in the table. The returned row keys will delimit contiguous sections of the table of approximately equal size, which can be used to break up the data for distributed tasks like mapreduces.

If a `row_range` is provided in the request, the returned samples will be restricted to the specified range.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SampleRowKeysRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SampleRowKeysRequest)`  
The request received from the client.  
`responseStream` | `[IServerStreamWriter](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.IServerStreamWriter-1.html)[SampleRowKeysResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SampleRowKeysResponse)`  
Used for sending responses back to the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task indicating completion of the handler.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
