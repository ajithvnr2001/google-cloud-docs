---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryService.FeatureRegistryServiceClient
title: Vertex AI v1beta1 API - Class FeatureRegistryService.FeatureRegistryServiceClient (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:14:32.632765+00:00
---

# Vertex AI v1beta1 API - Class FeatureRegistryService.FeatureRegistryServiceClient (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryService.FeatureRegistryServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class FeatureRegistryService.FeatureRegistryServiceClient (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public class FeatureRegistryService.FeatureRegistryServiceClient : ClientBase<FeatureRegistryService.FeatureRegistryServiceClient>

Reference documentation and code samples for the Vertex AI v1beta1 API class FeatureRegistryService.FeatureRegistryServiceClient.

Client for FeatureRegistryService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[FeatureRegistryService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryService)[FeatureRegistryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryService.FeatureRegistryServiceClient) > FeatureRegistryService.FeatureRegistryServiceClient

## Inherited Members

[ClientBase<FeatureRegistryService.FeatureRegistryServiceClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

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

### FeatureRegistryServiceClient()
    
    
    protected FeatureRegistryServiceClient()

Protected parameterless constructor to allow creation of test doubles.

### FeatureRegistryServiceClient(CallInvoker)
    
    
    public FeatureRegistryServiceClient(CallInvoker callInvoker)

Creates a new client for FeatureRegistryService that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### FeatureRegistryServiceClient(ChannelBase)
    
    
    public FeatureRegistryServiceClient(ChannelBase channel)

Creates a new client for FeatureRegistryService

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### FeatureRegistryServiceClient(ClientBaseConfiguration)
    
    
    protected FeatureRegistryServiceClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### BatchCreateFeatures(BatchCreateFeaturesRequest, CallOptions)
    
    
    public virtual Operation BatchCreateFeatures(BatchCreateFeaturesRequest request, CallOptions options)

Creates a batch of Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateFeaturesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### BatchCreateFeatures(BatchCreateFeaturesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation BatchCreateFeatures(BatchCreateFeaturesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a batch of Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateFeaturesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesRequest)`  
The request to send to the server.  
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
  
### BatchCreateFeaturesAsync(BatchCreateFeaturesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> BatchCreateFeaturesAsync(BatchCreateFeaturesRequest request, CallOptions options)

Creates a batch of Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateFeaturesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### BatchCreateFeaturesAsync(BatchCreateFeaturesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> BatchCreateFeaturesAsync(BatchCreateFeaturesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a batch of Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateFeaturesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesRequest)`  
The request to send to the server.  
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
  
### CreateFeature(CreateFeatureRequest, CallOptions)
    
    
    public virtual Operation CreateFeature(CreateFeatureRequest request, CallOptions options)

Creates a new Feature in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateFeature(CreateFeatureRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateFeature(CreateFeatureRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Feature in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureRequest)`  
The request to send to the server.  
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
  
### CreateFeatureAsync(CreateFeatureRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateFeatureAsync(CreateFeatureRequest request, CallOptions options)

Creates a new Feature in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateFeatureAsync(CreateFeatureRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateFeatureAsync(CreateFeatureRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Feature in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureRequest)`  
The request to send to the server.  
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
  
### CreateFeatureGroup(CreateFeatureGroupRequest, CallOptions)
    
    
    public virtual Operation CreateFeatureGroup(CreateFeatureGroupRequest request, CallOptions options)

Creates a new FeatureGroup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureGroupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateFeatureGroup(CreateFeatureGroupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateFeatureGroup(CreateFeatureGroupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new FeatureGroup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureGroupRequest)`  
The request to send to the server.  
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
  
### CreateFeatureGroupAsync(CreateFeatureGroupRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateFeatureGroupAsync(CreateFeatureGroupRequest request, CallOptions options)

Creates a new FeatureGroup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureGroupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateFeatureGroupAsync(CreateFeatureGroupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateFeatureGroupAsync(CreateFeatureGroupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new FeatureGroup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureGroupRequest)`  
The request to send to the server.  
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
  
### CreateFeatureMonitor(CreateFeatureMonitorRequest, CallOptions)
    
    
    public virtual Operation CreateFeatureMonitor(CreateFeatureMonitorRequest request, CallOptions options)

Creates a new FeatureMonitor in a given project, location and FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### CreateFeatureMonitor(CreateFeatureMonitorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CreateFeatureMonitor(CreateFeatureMonitorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new FeatureMonitor in a given project, location and FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorRequest)`  
The request to send to the server.  
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
  
### CreateFeatureMonitorAsync(CreateFeatureMonitorRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CreateFeatureMonitorAsync(CreateFeatureMonitorRequest request, CallOptions options)

Creates a new FeatureMonitor in a given project, location and FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### CreateFeatureMonitorAsync(CreateFeatureMonitorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CreateFeatureMonitorAsync(CreateFeatureMonitorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new FeatureMonitor in a given project, location and FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorRequest)`  
The request to send to the server.  
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
  
### CreateFeatureMonitorJob(CreateFeatureMonitorJobRequest, CallOptions)
    
    
    public virtual FeatureMonitorJob CreateFeatureMonitorJob(CreateFeatureMonitorJobRequest request, CallOptions options)

Creates a new feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureMonitorJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorJobRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | The response received from the server.  
  
### CreateFeatureMonitorJob(CreateFeatureMonitorJobRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FeatureMonitorJob CreateFeatureMonitorJob(CreateFeatureMonitorJobRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureMonitorJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorJobRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | The response received from the server.  
  
### CreateFeatureMonitorJobAsync(CreateFeatureMonitorJobRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FeatureMonitorJob> CreateFeatureMonitorJobAsync(CreateFeatureMonitorJobRequest request, CallOptions options)

Creates a new feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureMonitorJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorJobRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | The call object.  
  
### CreateFeatureMonitorJobAsync(CreateFeatureMonitorJobRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FeatureMonitorJob> CreateFeatureMonitorJobAsync(CreateFeatureMonitorJobRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureMonitorJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorJobRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | The call object.  
  
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
  
### DeleteFeature(DeleteFeatureRequest, CallOptions)
    
    
    public virtual Operation DeleteFeature(DeleteFeatureRequest request, CallOptions options)

Deletes a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteFeature(DeleteFeatureRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteFeature(DeleteFeatureRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureRequest)`  
The request to send to the server.  
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
  
### DeleteFeatureAsync(DeleteFeatureRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteFeatureAsync(DeleteFeatureRequest request, CallOptions options)

Deletes a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteFeatureAsync(DeleteFeatureRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteFeatureAsync(DeleteFeatureRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureRequest)`  
The request to send to the server.  
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
  
### DeleteFeatureGroup(DeleteFeatureGroupRequest, CallOptions)
    
    
    public virtual Operation DeleteFeatureGroup(DeleteFeatureGroupRequest request, CallOptions options)

Deletes a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureGroupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteFeatureGroup(DeleteFeatureGroupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteFeatureGroup(DeleteFeatureGroupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureGroupRequest)`  
The request to send to the server.  
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
  
### DeleteFeatureGroupAsync(DeleteFeatureGroupRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteFeatureGroupAsync(DeleteFeatureGroupRequest request, CallOptions options)

Deletes a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureGroupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteFeatureGroupAsync(DeleteFeatureGroupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteFeatureGroupAsync(DeleteFeatureGroupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureGroupRequest)`  
The request to send to the server.  
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
  
### DeleteFeatureMonitor(DeleteFeatureMonitorRequest, CallOptions)
    
    
    public virtual Operation DeleteFeatureMonitor(DeleteFeatureMonitorRequest request, CallOptions options)

Deletes a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureMonitorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteFeatureMonitor(DeleteFeatureMonitorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteFeatureMonitor(DeleteFeatureMonitorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureMonitorRequest)`  
The request to send to the server.  
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
  
### DeleteFeatureMonitorAsync(DeleteFeatureMonitorRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteFeatureMonitorAsync(DeleteFeatureMonitorRequest request, CallOptions options)

Deletes a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureMonitorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteFeatureMonitorAsync(DeleteFeatureMonitorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteFeatureMonitorAsync(DeleteFeatureMonitorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureMonitorRequest)`  
The request to send to the server.  
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
  
### GetFeature(GetFeatureRequest, CallOptions)
    
    
    public virtual Feature GetFeature(GetFeatureRequest request, CallOptions options)

Gets details of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | The response received from the server.  
  
### GetFeature(GetFeatureRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Feature GetFeature(GetFeatureRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | The response received from the server.  
  
### GetFeatureAsync(GetFeatureRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Feature> GetFeatureAsync(GetFeatureRequest request, CallOptions options)

Gets details of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | The call object.  
  
### GetFeatureAsync(GetFeatureRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Feature> GetFeatureAsync(GetFeatureRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | The call object.  
  
### GetFeatureGroup(GetFeatureGroupRequest, CallOptions)
    
    
    public virtual FeatureGroup GetFeatureGroup(GetFeatureGroupRequest request, CallOptions options)

Gets details of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureGroupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)` | The response received from the server.  
  
### GetFeatureGroup(GetFeatureGroupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FeatureGroup GetFeatureGroup(GetFeatureGroupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureGroupRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)` | The response received from the server.  
  
### GetFeatureGroupAsync(GetFeatureGroupRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FeatureGroup> GetFeatureGroupAsync(GetFeatureGroupRequest request, CallOptions options)

Gets details of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureGroupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)` | The call object.  
  
### GetFeatureGroupAsync(GetFeatureGroupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FeatureGroup> GetFeatureGroupAsync(GetFeatureGroupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureGroupRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)` | The call object.  
  
### GetFeatureMonitor(GetFeatureMonitorRequest, CallOptions)
    
    
    public virtual FeatureMonitor GetFeatureMonitor(GetFeatureMonitorRequest request, CallOptions options)

Gets details of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureMonitorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)` | The response received from the server.  
  
### GetFeatureMonitor(GetFeatureMonitorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FeatureMonitor GetFeatureMonitor(GetFeatureMonitorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureMonitorRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)` | The response received from the server.  
  
### GetFeatureMonitorAsync(GetFeatureMonitorRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FeatureMonitor> GetFeatureMonitorAsync(GetFeatureMonitorRequest request, CallOptions options)

Gets details of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureMonitorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)` | The call object.  
  
### GetFeatureMonitorAsync(GetFeatureMonitorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FeatureMonitor> GetFeatureMonitorAsync(GetFeatureMonitorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureMonitorRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)` | The call object.  
  
### GetFeatureMonitorJob(GetFeatureMonitorJobRequest, CallOptions)
    
    
    public virtual FeatureMonitorJob GetFeatureMonitorJob(GetFeatureMonitorJobRequest request, CallOptions options)

Get a feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureMonitorJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureMonitorJobRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | The response received from the server.  
  
### GetFeatureMonitorJob(GetFeatureMonitorJobRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FeatureMonitorJob GetFeatureMonitorJob(GetFeatureMonitorJobRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get a feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureMonitorJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureMonitorJobRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | The response received from the server.  
  
### GetFeatureMonitorJobAsync(GetFeatureMonitorJobRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FeatureMonitorJob> GetFeatureMonitorJobAsync(GetFeatureMonitorJobRequest request, CallOptions options)

Get a feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureMonitorJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureMonitorJobRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | The call object.  
  
### GetFeatureMonitorJobAsync(GetFeatureMonitorJobRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FeatureMonitorJob> GetFeatureMonitorJobAsync(GetFeatureMonitorJobRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get a feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureMonitorJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureMonitorJobRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | The call object.  
  
### ListFeatureGroups(ListFeatureGroupsRequest, CallOptions)
    
    
    public virtual ListFeatureGroupsResponse ListFeatureGroups(ListFeatureGroupsRequest request, CallOptions options)

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureGroupsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListFeatureGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureGroupsResponse)` | The response received from the server.  
  
### ListFeatureGroups(ListFeatureGroupsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListFeatureGroupsResponse ListFeatureGroups(ListFeatureGroupsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureGroupsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListFeatureGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureGroupsResponse)` | The response received from the server.  
  
### ListFeatureGroupsAsync(ListFeatureGroupsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListFeatureGroupsResponse> ListFeatureGroupsAsync(ListFeatureGroupsRequest request, CallOptions options)

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureGroupsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListFeatureGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureGroupsResponse)` | The call object.  
  
### ListFeatureGroupsAsync(ListFeatureGroupsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListFeatureGroupsResponse> ListFeatureGroupsAsync(ListFeatureGroupsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureGroupsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListFeatureGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureGroupsResponse)` | The call object.  
  
### ListFeatureMonitorJobs(ListFeatureMonitorJobsRequest, CallOptions)
    
    
    public virtual ListFeatureMonitorJobsResponse ListFeatureMonitorJobs(ListFeatureMonitorJobsRequest request, CallOptions options)

List feature monitor jobs.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureMonitorJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorJobsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListFeatureMonitorJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorJobsResponse)` | The response received from the server.  
  
### ListFeatureMonitorJobs(ListFeatureMonitorJobsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListFeatureMonitorJobsResponse ListFeatureMonitorJobs(ListFeatureMonitorJobsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List feature monitor jobs.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureMonitorJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorJobsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListFeatureMonitorJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorJobsResponse)` | The response received from the server.  
  
### ListFeatureMonitorJobsAsync(ListFeatureMonitorJobsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListFeatureMonitorJobsResponse> ListFeatureMonitorJobsAsync(ListFeatureMonitorJobsRequest request, CallOptions options)

List feature monitor jobs.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureMonitorJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorJobsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListFeatureMonitorJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorJobsResponse)` | The call object.  
  
### ListFeatureMonitorJobsAsync(ListFeatureMonitorJobsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListFeatureMonitorJobsResponse> ListFeatureMonitorJobsAsync(ListFeatureMonitorJobsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

List feature monitor jobs.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureMonitorJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorJobsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListFeatureMonitorJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorJobsResponse)` | The call object.  
  
### ListFeatureMonitors(ListFeatureMonitorsRequest, CallOptions)
    
    
    public virtual ListFeatureMonitorsResponse ListFeatureMonitors(ListFeatureMonitorsRequest request, CallOptions options)

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureMonitorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListFeatureMonitorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorsResponse)` | The response received from the server.  
  
### ListFeatureMonitors(ListFeatureMonitorsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListFeatureMonitorsResponse ListFeatureMonitors(ListFeatureMonitorsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureMonitorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListFeatureMonitorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorsResponse)` | The response received from the server.  
  
### ListFeatureMonitorsAsync(ListFeatureMonitorsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListFeatureMonitorsResponse> ListFeatureMonitorsAsync(ListFeatureMonitorsRequest request, CallOptions options)

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureMonitorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListFeatureMonitorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorsResponse)` | The call object.  
  
### ListFeatureMonitorsAsync(ListFeatureMonitorsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListFeatureMonitorsResponse> ListFeatureMonitorsAsync(ListFeatureMonitorsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureMonitorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListFeatureMonitorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorsResponse)` | The call object.  
  
### ListFeatures(ListFeaturesRequest, CallOptions)
    
    
    public virtual ListFeaturesResponse ListFeatures(ListFeaturesRequest request, CallOptions options)

Lists Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeaturesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturesResponse)` | The response received from the server.  
  
### ListFeatures(ListFeaturesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListFeaturesResponse ListFeatures(ListFeaturesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeaturesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturesResponse)` | The response received from the server.  
  
### ListFeaturesAsync(ListFeaturesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListFeaturesResponse> ListFeaturesAsync(ListFeaturesRequest request, CallOptions options)

Lists Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeaturesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturesResponse)` | The call object.  
  
### ListFeaturesAsync(ListFeaturesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListFeaturesResponse> ListFeaturesAsync(ListFeaturesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeaturesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturesResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override FeatureRegistryService.FeatureRegistryServiceClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FeatureRegistryService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryService)[FeatureRegistryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryService.FeatureRegistryServiceClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryService.FeatureRegistryServiceClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### UpdateFeature(UpdateFeatureRequest, CallOptions)
    
    
    public virtual Operation UpdateFeature(UpdateFeatureRequest request, CallOptions options)

Updates the parameters of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateFeature(UpdateFeatureRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateFeature(UpdateFeatureRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureRequest)`  
The request to send to the server.  
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
  
### UpdateFeatureAsync(UpdateFeatureRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateFeatureAsync(UpdateFeatureRequest request, CallOptions options)

Updates the parameters of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateFeatureAsync(UpdateFeatureRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateFeatureAsync(UpdateFeatureRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureRequest)`  
The request to send to the server.  
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
  
### UpdateFeatureGroup(UpdateFeatureGroupRequest, CallOptions)
    
    
    public virtual Operation UpdateFeatureGroup(UpdateFeatureGroupRequest request, CallOptions options)

Updates the parameters of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureGroupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateFeatureGroup(UpdateFeatureGroupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateFeatureGroup(UpdateFeatureGroupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureGroupRequest)`  
The request to send to the server.  
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
  
### UpdateFeatureGroupAsync(UpdateFeatureGroupRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateFeatureGroupAsync(UpdateFeatureGroupRequest request, CallOptions options)

Updates the parameters of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureGroupRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateFeatureGroupAsync(UpdateFeatureGroupRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateFeatureGroupAsync(UpdateFeatureGroupRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureGroupRequest)`  
The request to send to the server.  
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
  
### UpdateFeatureMonitor(UpdateFeatureMonitorRequest, CallOptions)
    
    
    public virtual Operation UpdateFeatureMonitor(UpdateFeatureMonitorRequest request, CallOptions options)

Updates the parameters of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureMonitorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### UpdateFeatureMonitor(UpdateFeatureMonitorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation UpdateFeatureMonitor(UpdateFeatureMonitorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureMonitorRequest)`  
The request to send to the server.  
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
  
### UpdateFeatureMonitorAsync(UpdateFeatureMonitorRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateFeatureMonitorAsync(UpdateFeatureMonitorRequest request, CallOptions options)

Updates the parameters of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureMonitorRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### UpdateFeatureMonitorAsync(UpdateFeatureMonitorRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> UpdateFeatureMonitorAsync(UpdateFeatureMonitorRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureMonitorRequest)`  
The request to send to the server.  
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

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
