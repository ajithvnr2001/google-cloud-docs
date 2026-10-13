---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.LiveVideoAnalytics.LiveVideoAnalyticsClient
title: Vision AI v1 API - Class LiveVideoAnalytics.LiveVideoAnalyticsClient (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:06.736106+00:00
---

# Vision AI v1 API - Class LiveVideoAnalytics.LiveVideoAnalyticsClient (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.LiveVideoAnalytics.LiveVideoAnalyticsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vision AI v1 API - Class LiveVideoAnalytics.LiveVideoAnalyticsClient (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public class LiveVideoAnalytics.LiveVideoAnalyticsClient : ClientBase<LiveVideoAnalytics.LiveVideoAnalyticsClient>

Reference documentation and code samples for the Vision AI v1 API class LiveVideoAnalytics.LiveVideoAnalyticsClient.

Client for LiveVideoAnalytics

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[LiveVideoAnalytics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.LiveVideoAnalytics)[LiveVideoAnalyticsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.LiveVideoAnalytics.LiveVideoAnalyticsClient) > LiveVideoAnalytics.LiveVideoAnalyticsClient

## Inherited Members

[ClientBase<LiveVideoAnalytics.LiveVideoAnalyticsClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.VisionAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1)

## Assembly

Google.Cloud.VisionAI.V1.dll

## Constructors 

### LiveVideoAnalyticsClient()
    
    
    protected LiveVideoAnalyticsClient()

Protected parameterless constructor to allow creation of test doubles.

### LiveVideoAnalyticsClient(CallInvoker)
    
    
    public LiveVideoAnalyticsClient(CallInvoker callInvoker)

Creates a new client for LiveVideoAnalytics that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### LiveVideoAnalyticsClient(ChannelBase)
    
    
    public LiveVideoAnalyticsClient(ChannelBase channel)

Creates a new client for LiveVideoAnalytics

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### LiveVideoAnalyticsClient(ClientBaseConfiguration)
    
    
    protected LiveVideoAnalyticsClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### BatchRunProcess(BatchRunProcessRequest, CallOptions)
    
    
    public virtual Operation BatchRunProcess(BatchRunProcessRequest request, CallOptions options)

Run all of the processes to "completion". Max time for each process is the LRO time limit.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchRunProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.BatchRunProcessRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### BatchRunProcess(BatchRunProcessRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation BatchRunProcess(BatchRunProcessRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Run all of the processes to "completion". Max time for each process is the LRO time limit.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchRunProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.BatchRunProcessRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### BatchRunProcessAsync(BatchRunProcessRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> BatchRunProcessAsync(BatchRunProcessRequest request, CallOptions options)

Run all of the processes to "completion". Max time for each process is the LRO time limit.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchRunProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.BatchRunProcessRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### BatchRunProcessAsync(BatchRunProcessRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> BatchRunProcessAsync(BatchRunProcessRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Run all of the processes to "completion". Max time for each process is the LRO time limit.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchRunProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.BatchRunProcessRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateAnalysis(CreateAnalysisRequest, CallOptions)
    
    
    public virtual Operation CreateAnalysis(CreateAnalysisRequest request, CallOptions options)

Creates a new Analysis in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAnalysisRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateAnalysisRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateAnalysis(CreateAnalysisRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateAnalysis(CreateAnalysisRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Analysis in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAnalysisRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateAnalysisRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateAnalysisAsync(CreateAnalysisRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateAnalysisAsync(CreateAnalysisRequest request, CallOptions options)

Creates a new Analysis in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAnalysisRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateAnalysisRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateAnalysisAsync(CreateAnalysisRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateAnalysisAsync(CreateAnalysisRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Analysis in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAnalysisRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateAnalysisRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateIAMPolicyClient()
    
    
    public virtual IAMPolicy.IAMPolicyClient CreateIAMPolicyClient()

Creates a new instance of [IAMPolicy.IAMPolicyClient](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.IAMPolicyClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[IAMPolicy](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.html)[IAMPolicyClient](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.IAMPolicyClient.html)` | A new [IAMPolicy.IAMPolicyClient](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.IAMPolicyClient.html) for the same target as this client.  
  
### CreateLocationsClient()
    
    
    public virtual Locations.LocationsClient CreateLocationsClient()

Creates a new instance of [Locations.LocationsClient](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[Locations](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.html)[LocationsClient](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html)` | A new [Locations.LocationsClient](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html) for the same target as this client.  
  
### CreateOperationsClient()
    
    
    public virtual Operations.OperationsClient CreateOperationsClient()

Creates a new instance of [Operations.OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[Operations](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.html)[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html)` | A new Operations client for the same target as this client.  
  
### CreateOperator(CreateOperatorRequest, CallOptions)
    
    
    public virtual Operation CreateOperator(CreateOperatorRequest request, CallOptions options)

Creates a new Operator in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateOperatorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateOperatorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateOperator(CreateOperatorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateOperator(CreateOperatorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Operator in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateOperatorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateOperatorRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateOperatorAsync(CreateOperatorRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateOperatorAsync(CreateOperatorRequest request, CallOptions options)

Creates a new Operator in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateOperatorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateOperatorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateOperatorAsync(CreateOperatorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateOperatorAsync(CreateOperatorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Operator in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateOperatorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateOperatorRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateProcess(CreateProcessRequest, CallOptions)
    
    
    public virtual Operation CreateProcess(CreateProcessRequest request, CallOptions options)

Creates a new Process in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateProcessRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateProcess(CreateProcessRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateProcess(CreateProcessRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Process in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateProcessRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateProcessAsync(CreateProcessRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateProcessAsync(CreateProcessRequest request, CallOptions options)

Creates a new Process in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateProcessRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateProcessAsync(CreateProcessRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateProcessAsync(CreateProcessRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Process in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateProcessRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteAnalysis(DeleteAnalysisRequest, CallOptions)
    
    
    public virtual Operation DeleteAnalysis(DeleteAnalysisRequest request, CallOptions options)

Deletes a single Analysis.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAnalysisRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAnalysisRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteAnalysis(DeleteAnalysisRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteAnalysis(DeleteAnalysisRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Analysis.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAnalysisRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAnalysisRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteAnalysisAsync(DeleteAnalysisRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteAnalysisAsync(DeleteAnalysisRequest request, CallOptions options)

Deletes a single Analysis.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAnalysisRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAnalysisRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteAnalysisAsync(DeleteAnalysisRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteAnalysisAsync(DeleteAnalysisRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Analysis.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAnalysisRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAnalysisRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteOperator(DeleteOperatorRequest, CallOptions)
    
    
    public virtual Operation DeleteOperator(DeleteOperatorRequest request, CallOptions options)

Deletes a single Operator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteOperatorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteOperatorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteOperator(DeleteOperatorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteOperator(DeleteOperatorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Operator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteOperatorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteOperatorRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteOperatorAsync(DeleteOperatorRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteOperatorAsync(DeleteOperatorRequest request, CallOptions options)

Deletes a single Operator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteOperatorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteOperatorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteOperatorAsync(DeleteOperatorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteOperatorAsync(DeleteOperatorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Operator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteOperatorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteOperatorRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteProcess(DeleteProcessRequest, CallOptions)
    
    
    public virtual Operation DeleteProcess(DeleteProcessRequest request, CallOptions options)

Deletes a single Process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteProcessRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteProcess(DeleteProcessRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteProcess(DeleteProcessRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteProcessRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteProcessAsync(DeleteProcessRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteProcessAsync(DeleteProcessRequest request, CallOptions options)

Deletes a single Process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteProcessRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteProcessAsync(DeleteProcessRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteProcessAsync(DeleteProcessRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteProcessRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### GetAnalysis(GetAnalysisRequest, CallOptions)
    
    
    public virtual Analysis GetAnalysis(GetAnalysisRequest request, CallOptions options)

Gets details of a single Analysis.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAnalysisRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetAnalysisRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Analysis](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Analysis)` | The response received from the server.  
  
### GetAnalysis(GetAnalysisRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Analysis GetAnalysis(GetAnalysisRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Analysis.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAnalysisRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetAnalysisRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Analysis](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Analysis)` | The response received from the server.  
  
### GetAnalysisAsync(GetAnalysisRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Analysis> GetAnalysisAsync(GetAnalysisRequest request, CallOptions options)

Gets details of a single Analysis.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAnalysisRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetAnalysisRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Analysis](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Analysis)` | The call object.  
  
### GetAnalysisAsync(GetAnalysisRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Analysis> GetAnalysisAsync(GetAnalysisRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Analysis.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAnalysisRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetAnalysisRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Analysis](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Analysis)` | The call object.  
  
### GetOperator(GetOperatorRequest, CallOptions)
    
    
    public virtual Operator GetOperator(GetOperatorRequest request, CallOptions options)

Gets details of a single Operator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOperatorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetOperatorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Operator)` | The response received from the server.  
  
### GetOperator(GetOperatorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operator GetOperator(GetOperatorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Operator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOperatorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetOperatorRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Operator)` | The response received from the server.  
  
### GetOperatorAsync(GetOperatorRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operator> GetOperatorAsync(GetOperatorRequest request, CallOptions options)

Gets details of a single Operator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOperatorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetOperatorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Operator)` | The call object.  
  
### GetOperatorAsync(GetOperatorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operator> GetOperatorAsync(GetOperatorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Operator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOperatorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetOperatorRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Operator)` | The call object.  
  
### GetProcess(GetProcessRequest, CallOptions)
    
    
    public virtual Process GetProcess(GetProcessRequest request, CallOptions options)

Gets details of a single Process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetProcessRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Process)` | The response received from the server.  
  
### GetProcess(GetProcessRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Process GetProcess(GetProcessRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetProcessRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Process)` | The response received from the server.  
  
### GetProcessAsync(GetProcessRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Process> GetProcessAsync(GetProcessRequest request, CallOptions options)

Gets details of a single Process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetProcessRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Process)` | The call object.  
  
### GetProcessAsync(GetProcessRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Process> GetProcessAsync(GetProcessRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetProcessRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Process](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Process)` | The call object.  
  
### ListAnalyses(ListAnalysesRequest, CallOptions)
    
    
    public virtual ListAnalysesResponse ListAnalyses(ListAnalysesRequest request, CallOptions options)

Lists Analyses in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAnalysesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAnalysesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAnalysesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAnalysesResponse)` | The response received from the server.  
  
### ListAnalyses(ListAnalysesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListAnalysesResponse ListAnalyses(ListAnalysesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Analyses in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAnalysesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAnalysesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListAnalysesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAnalysesResponse)` | The response received from the server.  
  
### ListAnalysesAsync(ListAnalysesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListAnalysesResponse> ListAnalysesAsync(ListAnalysesRequest request, CallOptions options)

Lists Analyses in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAnalysesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAnalysesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAnalysesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAnalysesResponse)` | The call object.  
  
### ListAnalysesAsync(ListAnalysesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListAnalysesResponse> ListAnalysesAsync(ListAnalysesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Analyses in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAnalysesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAnalysesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListAnalysesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAnalysesResponse)` | The call object.  
  
### ListOperators(ListOperatorsRequest, CallOptions)
    
    
    public virtual ListOperatorsResponse ListOperators(ListOperatorsRequest request, CallOptions options)

Lists Operators in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOperatorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListOperatorsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListOperatorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListOperatorsResponse)` | The response received from the server.  
  
### ListOperators(ListOperatorsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListOperatorsResponse ListOperators(ListOperatorsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Operators in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOperatorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListOperatorsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListOperatorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListOperatorsResponse)` | The response received from the server.  
  
### ListOperatorsAsync(ListOperatorsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListOperatorsResponse> ListOperatorsAsync(ListOperatorsRequest request, CallOptions options)

Lists Operators in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOperatorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListOperatorsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListOperatorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListOperatorsResponse)` | The call object.  
  
### ListOperatorsAsync(ListOperatorsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListOperatorsResponse> ListOperatorsAsync(ListOperatorsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Operators in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOperatorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListOperatorsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListOperatorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListOperatorsResponse)` | The call object.  
  
### ListProcesses(ListProcessesRequest, CallOptions)
    
    
    public virtual ListProcessesResponse ListProcesses(ListProcessesRequest request, CallOptions options)

Lists Processes in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProcessesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListProcessesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListProcessesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListProcessesResponse)` | The response received from the server.  
  
### ListProcesses(ListProcessesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListProcessesResponse ListProcesses(ListProcessesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Processes in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProcessesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListProcessesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListProcessesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListProcessesResponse)` | The response received from the server.  
  
### ListProcessesAsync(ListProcessesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListProcessesResponse> ListProcessesAsync(ListProcessesRequest request, CallOptions options)

Lists Processes in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProcessesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListProcessesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListProcessesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListProcessesResponse)` | The call object.  
  
### ListProcessesAsync(ListProcessesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListProcessesResponse> ListProcessesAsync(ListProcessesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Processes in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProcessesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListProcessesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListProcessesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListProcessesResponse)` | The call object.  
  
### ListPublicOperators(ListPublicOperatorsRequest, CallOptions)
    
    
    public virtual ListPublicOperatorsResponse ListPublicOperators(ListPublicOperatorsRequest request, CallOptions options)

ListPublicOperators returns all the operators in public registry.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPublicOperatorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListPublicOperatorsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListPublicOperatorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListPublicOperatorsResponse)` | The response received from the server.  
  
### ListPublicOperators(ListPublicOperatorsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListPublicOperatorsResponse ListPublicOperators(ListPublicOperatorsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

ListPublicOperators returns all the operators in public registry.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPublicOperatorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListPublicOperatorsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListPublicOperatorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListPublicOperatorsResponse)` | The response received from the server.  
  
### ListPublicOperatorsAsync(ListPublicOperatorsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListPublicOperatorsResponse> ListPublicOperatorsAsync(ListPublicOperatorsRequest request, CallOptions options)

ListPublicOperators returns all the operators in public registry.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPublicOperatorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListPublicOperatorsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListPublicOperatorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListPublicOperatorsResponse)` | The call object.  
  
### ListPublicOperatorsAsync(ListPublicOperatorsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListPublicOperatorsResponse> ListPublicOperatorsAsync(ListPublicOperatorsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

ListPublicOperators returns all the operators in public registry.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPublicOperatorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListPublicOperatorsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListPublicOperatorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListPublicOperatorsResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override LiveVideoAnalytics.LiveVideoAnalyticsClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LiveVideoAnalytics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.LiveVideoAnalytics)[LiveVideoAnalyticsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.LiveVideoAnalytics.LiveVideoAnalyticsClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.VisionAI.V1.LiveVideoAnalytics.LiveVideoAnalyticsClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### ResolveOperatorInfo(ResolveOperatorInfoRequest, CallOptions)
    
    
    public virtual ResolveOperatorInfoResponse ResolveOperatorInfo(ResolveOperatorInfoRequest request, CallOptions options)

ResolveOperatorInfo returns the operator information based on the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResolveOperatorInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ResolveOperatorInfoRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ResolveOperatorInfoResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ResolveOperatorInfoResponse)` | The response received from the server.  
  
### ResolveOperatorInfo(ResolveOperatorInfoRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ResolveOperatorInfoResponse ResolveOperatorInfo(ResolveOperatorInfoRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

ResolveOperatorInfo returns the operator information based on the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResolveOperatorInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ResolveOperatorInfoRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ResolveOperatorInfoResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ResolveOperatorInfoResponse)` | The response received from the server.  
  
### ResolveOperatorInfoAsync(ResolveOperatorInfoRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ResolveOperatorInfoResponse> ResolveOperatorInfoAsync(ResolveOperatorInfoRequest request, CallOptions options)

ResolveOperatorInfo returns the operator information based on the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResolveOperatorInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ResolveOperatorInfoRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ResolveOperatorInfoResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ResolveOperatorInfoResponse)` | The call object.  
  
### ResolveOperatorInfoAsync(ResolveOperatorInfoRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ResolveOperatorInfoResponse> ResolveOperatorInfoAsync(ResolveOperatorInfoRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

ResolveOperatorInfo returns the operator information based on the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResolveOperatorInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ResolveOperatorInfoRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ResolveOperatorInfoResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ResolveOperatorInfoResponse)` | The call object.  
  
### UpdateAnalysis(UpdateAnalysisRequest, CallOptions)
    
    
    public virtual Operation UpdateAnalysis(UpdateAnalysisRequest request, CallOptions options)

Updates the parameters of a single Analysis.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAnalysisRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateAnalysisRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateAnalysis(UpdateAnalysisRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateAnalysis(UpdateAnalysisRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single Analysis.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAnalysisRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateAnalysisRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateAnalysisAsync(UpdateAnalysisRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateAnalysisAsync(UpdateAnalysisRequest request, CallOptions options)

Updates the parameters of a single Analysis.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAnalysisRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateAnalysisRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateAnalysisAsync(UpdateAnalysisRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateAnalysisAsync(UpdateAnalysisRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single Analysis.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAnalysisRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateAnalysisRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateOperator(UpdateOperatorRequest, CallOptions)
    
    
    public virtual Operation UpdateOperator(UpdateOperatorRequest request, CallOptions options)

Updates the parameters of a single Operator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateOperatorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateOperatorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateOperator(UpdateOperatorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateOperator(UpdateOperatorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single Operator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateOperatorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateOperatorRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateOperatorAsync(UpdateOperatorRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateOperatorAsync(UpdateOperatorRequest request, CallOptions options)

Updates the parameters of a single Operator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateOperatorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateOperatorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateOperatorAsync(UpdateOperatorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateOperatorAsync(UpdateOperatorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single Operator.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateOperatorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateOperatorRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateProcess(UpdateProcessRequest, CallOptions)
    
    
    public virtual Operation UpdateProcess(UpdateProcessRequest request, CallOptions options)

Updates the parameters of a single Process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateProcessRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateProcess(UpdateProcessRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateProcess(UpdateProcessRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single Process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateProcessRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateProcessAsync(UpdateProcessRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateProcessAsync(UpdateProcessRequest request, CallOptions options)

Updates the parameters of a single Process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateProcessRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateProcessAsync(UpdateProcessRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateProcessAsync(UpdateProcessRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single Process.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProcessRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateProcessRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
