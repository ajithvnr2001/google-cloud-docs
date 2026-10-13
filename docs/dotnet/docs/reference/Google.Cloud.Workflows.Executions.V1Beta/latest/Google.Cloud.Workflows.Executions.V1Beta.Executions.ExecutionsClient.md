---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.Executions.ExecutionsClient
title: Workflow Executions v1beta API - Class Executions.ExecutionsClient (2.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:29.750743+00:00
---

# Workflow Executions v1beta API - Class Executions.ExecutionsClient (2.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.Executions.ExecutionsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Workflow Executions v1beta API - Class Executions.ExecutionsClient (2.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.Executions.ExecutionsClient)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/2.0.0-beta05/Google.Cloud.Workflows.Executions.V1Beta.Executions.ExecutionsClient)
  * [ 1.0.0-beta03 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/1.0.0-beta03/Google.Cloud.Workflows.Executions.V1Beta.Executions.ExecutionsClient)


    
    
    public class Executions.ExecutionsClient : ClientBase<Executions.ExecutionsClient>

Reference documentation and code samples for the Workflow Executions v1beta API class Executions.ExecutionsClient.

Client for Executions

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[Executions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.Executions)[ExecutionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.Executions.ExecutionsClient) > Executions.ExecutionsClient

## Inherited Members

[ClientBase<Executions.ExecutionsClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Workflows.Executions.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta)

## Assembly

Google.Cloud.Workflows.Executions.V1Beta.dll

## Constructors 

### ExecutionsClient()
    
    
    protected ExecutionsClient()

Protected parameterless constructor to allow creation of test doubles.

### ExecutionsClient(CallInvoker)
    
    
    public ExecutionsClient(CallInvoker callInvoker)

Creates a new client for Executions that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### ExecutionsClient(ChannelBase)
    
    
    public ExecutionsClient(ChannelBase channel)

Creates a new client for Executions

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### ExecutionsClient(ClientBaseConfiguration)
    
    
    protected ExecutionsClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### CancelExecution(CancelExecutionRequest, CallOptions)
    
    
    public virtual Execution CancelExecution(CancelExecutionRequest request, CallOptions options)

Cancels an execution of the given name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelExecutionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.CancelExecutionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.Execution)` | The response received from the server.  
  
### CancelExecution(CancelExecutionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Execution CancelExecution(CancelExecutionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Cancels an execution of the given name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelExecutionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.CancelExecutionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.Execution)` | The response received from the server.  
  
### CancelExecutionAsync(CancelExecutionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Execution> CancelExecutionAsync(CancelExecutionRequest request, CallOptions options)

Cancels an execution of the given name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelExecutionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.CancelExecutionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Execution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.Execution)` | The call object.  
  
### CancelExecutionAsync(CancelExecutionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Execution> CancelExecutionAsync(CancelExecutionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Cancels an execution of the given name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelExecutionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.CancelExecutionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Execution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.Execution)` | The call object.  
  
### CreateExecution(CreateExecutionRequest, CallOptions)
    
    
    public virtual Execution CreateExecution(CreateExecutionRequest request, CallOptions options)

Creates a new execution using the latest revision of the given workflow.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExecutionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.CreateExecutionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.Execution)` | The response received from the server.  
  
### CreateExecution(CreateExecutionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Execution CreateExecution(CreateExecutionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new execution using the latest revision of the given workflow.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExecutionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.CreateExecutionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.Execution)` | The response received from the server.  
  
### CreateExecutionAsync(CreateExecutionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Execution> CreateExecutionAsync(CreateExecutionRequest request, CallOptions options)

Creates a new execution using the latest revision of the given workflow.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExecutionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.CreateExecutionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Execution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.Execution)` | The call object.  
  
### CreateExecutionAsync(CreateExecutionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Execution> CreateExecutionAsync(CreateExecutionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new execution using the latest revision of the given workflow.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExecutionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.CreateExecutionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Execution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.Execution)` | The call object.  
  
### GetExecution(GetExecutionRequest, CallOptions)
    
    
    public virtual Execution GetExecution(GetExecutionRequest request, CallOptions options)

Returns an execution of the given name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExecutionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.GetExecutionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.Execution)` | The response received from the server.  
  
### GetExecution(GetExecutionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Execution GetExecution(GetExecutionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns an execution of the given name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExecutionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.GetExecutionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.Execution)` | The response received from the server.  
  
### GetExecutionAsync(GetExecutionRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Execution> GetExecutionAsync(GetExecutionRequest request, CallOptions options)

Returns an execution of the given name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExecutionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.GetExecutionRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Execution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.Execution)` | The call object.  
  
### GetExecutionAsync(GetExecutionRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Execution> GetExecutionAsync(GetExecutionRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns an execution of the given name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExecutionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.GetExecutionRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Execution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.Execution)` | The call object.  
  
### ListExecutions(ListExecutionsRequest, CallOptions)
    
    
    public virtual ListExecutionsResponse ListExecutions(ListExecutionsRequest request, CallOptions options)

Returns a list of executions which belong to the workflow with the given name. The method returns executions of all workflow revisions. Returned executions are ordered by their start time (newest first).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExecutionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.ListExecutionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListExecutionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.ListExecutionsResponse)` | The response received from the server.  
  
### ListExecutions(ListExecutionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListExecutionsResponse ListExecutions(ListExecutionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a list of executions which belong to the workflow with the given name. The method returns executions of all workflow revisions. Returned executions are ordered by their start time (newest first).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExecutionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.ListExecutionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListExecutionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.ListExecutionsResponse)` | The response received from the server.  
  
### ListExecutionsAsync(ListExecutionsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListExecutionsResponse> ListExecutionsAsync(ListExecutionsRequest request, CallOptions options)

Returns a list of executions which belong to the workflow with the given name. The method returns executions of all workflow revisions. Returned executions are ordered by their start time (newest first).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExecutionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.ListExecutionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListExecutionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.ListExecutionsResponse)` | The call object.  
  
### ListExecutionsAsync(ListExecutionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListExecutionsResponse> ListExecutionsAsync(ListExecutionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns a list of executions which belong to the workflow with the given name. The method returns executions of all workflow revisions. Returned executions are ordered by their start time (newest first).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExecutionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.ListExecutionsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListExecutionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.ListExecutionsResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override Executions.ExecutionsClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Executions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.Executions)[ExecutionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Executions.V1Beta/latest/Google.Cloud.Workflows.Executions.V1Beta.Executions.ExecutionsClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Workflows.Executions.V1Beta.Executions.ExecutionsClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
