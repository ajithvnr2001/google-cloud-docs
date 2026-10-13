---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.SnapshotsV1Beta3.SnapshotsV1Beta3Client
title: Dataflow v1beta3 API - Class SnapshotsV1Beta3.SnapshotsV1Beta3Client (2.0.0-beta10) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:29.218511+00:00
---

# Dataflow v1beta3 API - Class SnapshotsV1Beta3.SnapshotsV1Beta3Client (2.0.0-beta10)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.SnapshotsV1Beta3.SnapshotsV1Beta3Client

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataflow v1beta3 API - Class SnapshotsV1Beta3.SnapshotsV1Beta3Client (2.0.0-beta10) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0-beta10 (latest)  2.0.0-beta09  1.0.0-beta03 
    
    
    public class SnapshotsV1Beta3.SnapshotsV1Beta3Client : ClientBase<SnapshotsV1Beta3.SnapshotsV1Beta3Client>

Reference documentation and code samples for the Dataflow v1beta3 API class SnapshotsV1Beta3.SnapshotsV1Beta3Client.

Client for SnapshotsV1Beta3

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[SnapshotsV1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.SnapshotsV1Beta3)[SnapshotsV1Beta3Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.SnapshotsV1Beta3.SnapshotsV1Beta3Client) > SnapshotsV1Beta3.SnapshotsV1Beta3Client

## Inherited Members

[ClientBase<SnapshotsV1Beta3.SnapshotsV1Beta3Client>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataflow.V1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3)

## Assembly

Google.Cloud.Dataflow.V1Beta3.dll

## Constructors 

### SnapshotsV1Beta3Client()
    
    
    protected SnapshotsV1Beta3Client()

Protected parameterless constructor to allow creation of test doubles.

### SnapshotsV1Beta3Client(CallInvoker)
    
    
    public SnapshotsV1Beta3Client(CallInvoker callInvoker)

Creates a new client for SnapshotsV1Beta3 that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### SnapshotsV1Beta3Client(ChannelBase)
    
    
    public SnapshotsV1Beta3Client(ChannelBase channel)

Creates a new client for SnapshotsV1Beta3

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### SnapshotsV1Beta3Client(ClientBaseConfiguration)
    
    
    protected SnapshotsV1Beta3Client(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### DeleteSnapshot(DeleteSnapshotRequest, CallOptions)
    
    
    public virtual DeleteSnapshotResponse DeleteSnapshot(DeleteSnapshotRequest request, CallOptions options)

Deletes a snapshot.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.DeleteSnapshotRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DeleteSnapshotResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.DeleteSnapshotResponse)` | The response received from the server.  
  
### DeleteSnapshot(DeleteSnapshotRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DeleteSnapshotResponse DeleteSnapshot(DeleteSnapshotRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a snapshot.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.DeleteSnapshotRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[DeleteSnapshotResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.DeleteSnapshotResponse)` | The response received from the server.  
  
### DeleteSnapshotAsync(DeleteSnapshotRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DeleteSnapshotResponse> DeleteSnapshotAsync(DeleteSnapshotRequest request, CallOptions options)

Deletes a snapshot.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.DeleteSnapshotRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DeleteSnapshotResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.DeleteSnapshotResponse)` | The call object.  
  
### DeleteSnapshotAsync(DeleteSnapshotRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DeleteSnapshotResponse> DeleteSnapshotAsync(DeleteSnapshotRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a snapshot.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.DeleteSnapshotRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DeleteSnapshotResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.DeleteSnapshotResponse)` | The call object.  
  
### GetSnapshot(GetSnapshotRequest, CallOptions)
    
    
    public virtual Snapshot GetSnapshot(GetSnapshotRequest request, CallOptions options)

Gets information about a snapshot.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetSnapshotRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Snapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.Snapshot)` | The response received from the server.  
  
### GetSnapshot(GetSnapshotRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Snapshot GetSnapshot(GetSnapshotRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets information about a snapshot.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetSnapshotRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Snapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.Snapshot)` | The response received from the server.  
  
### GetSnapshotAsync(GetSnapshotRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Snapshot> GetSnapshotAsync(GetSnapshotRequest request, CallOptions options)

Gets information about a snapshot.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetSnapshotRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Snapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.Snapshot)` | The call object.  
  
### GetSnapshotAsync(GetSnapshotRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Snapshot> GetSnapshotAsync(GetSnapshotRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets information about a snapshot.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetSnapshotRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Snapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.Snapshot)` | The call object.  
  
### ListSnapshots(ListSnapshotsRequest, CallOptions)
    
    
    public virtual ListSnapshotsResponse ListSnapshots(ListSnapshotsRequest request, CallOptions options)

Lists snapshots.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSnapshotsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.ListSnapshotsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListSnapshotsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.ListSnapshotsResponse)` | The response received from the server.  
  
### ListSnapshots(ListSnapshotsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListSnapshotsResponse ListSnapshots(ListSnapshotsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists snapshots.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSnapshotsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.ListSnapshotsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListSnapshotsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.ListSnapshotsResponse)` | The response received from the server.  
  
### ListSnapshotsAsync(ListSnapshotsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListSnapshotsResponse> ListSnapshotsAsync(ListSnapshotsRequest request, CallOptions options)

Lists snapshots.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSnapshotsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.ListSnapshotsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListSnapshotsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.ListSnapshotsResponse)` | The call object.  
  
### ListSnapshotsAsync(ListSnapshotsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListSnapshotsResponse> ListSnapshotsAsync(ListSnapshotsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists snapshots.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSnapshotsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.ListSnapshotsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListSnapshotsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.ListSnapshotsResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override SnapshotsV1Beta3.SnapshotsV1Beta3Client NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SnapshotsV1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.SnapshotsV1Beta3)[SnapshotsV1Beta3Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.SnapshotsV1Beta3.SnapshotsV1Beta3Client)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Dataflow.V1Beta3.SnapshotsV1Beta3.SnapshotsV1Beta3Client>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
