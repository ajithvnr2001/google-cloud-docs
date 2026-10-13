---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Dataform.DataformClient
title: Dataform v1beta1 API - Class Dataform.DataformClient (1.0.0-beta15) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:16:07.059251+00:00
---

# Dataform v1beta1 API - Class Dataform.DataformClient (1.0.0-beta15)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Dataform.DataformClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataform v1beta1 API - Class Dataform.DataformClient (1.0.0-beta15) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta15 (latest)  1.0.0-beta14 
    
    
    public class Dataform.DataformClient : ClientBase<Dataform.DataformClient>

Reference documentation and code samples for the Dataform v1beta1 API class Dataform.DataformClient.

Client for Dataform

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[Dataform](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Dataform)[DataformClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Dataform.DataformClient) > Dataform.DataformClient

## Inherited Members

[ClientBase<Dataform.DataformClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1)

## Assembly

Google.Cloud.Dataform.V1Beta1.dll

## Constructors 

### DataformClient()
    
    
    protected DataformClient()

Protected parameterless constructor to allow creation of test doubles.

### DataformClient(CallInvoker)
    
    
    public DataformClient(CallInvoker callInvoker)

Creates a new client for Dataform that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### DataformClient(ChannelBase)
    
    
    public DataformClient(ChannelBase channel)

Creates a new client for Dataform

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### DataformClient(ClientBaseConfiguration)
    
    
    protected DataformClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### CancelWorkflowInvocation(CancelWorkflowInvocationRequest, CallOptions)
    
    
    public virtual CancelWorkflowInvocationResponse CancelWorkflowInvocation(CancelWorkflowInvocationRequest request, CallOptions options)

Requests cancellation of a running WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelWorkflowInvocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CancelWorkflowInvocationRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[CancelWorkflowInvocationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CancelWorkflowInvocationResponse)` | The response received from the server.  
  
### CancelWorkflowInvocation(CancelWorkflowInvocationRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual CancelWorkflowInvocationResponse CancelWorkflowInvocation(CancelWorkflowInvocationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Requests cancellation of a running WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelWorkflowInvocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CancelWorkflowInvocationRequest)`  
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
`[CancelWorkflowInvocationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CancelWorkflowInvocationResponse)` | The response received from the server.  
  
### CancelWorkflowInvocationAsync(CancelWorkflowInvocationRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<CancelWorkflowInvocationResponse> CancelWorkflowInvocationAsync(CancelWorkflowInvocationRequest request, CallOptions options)

Requests cancellation of a running WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelWorkflowInvocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CancelWorkflowInvocationRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CancelWorkflowInvocationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CancelWorkflowInvocationResponse)` | The call object.  
  
### CancelWorkflowInvocationAsync(CancelWorkflowInvocationRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<CancelWorkflowInvocationResponse> CancelWorkflowInvocationAsync(CancelWorkflowInvocationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Requests cancellation of a running WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelWorkflowInvocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CancelWorkflowInvocationRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CancelWorkflowInvocationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CancelWorkflowInvocationResponse)` | The call object.  
  
### CheckoutWorkspaceBranch(CheckoutWorkspaceBranchRequest, CallOptions)
    
    
    public virtual Empty CheckoutWorkspaceBranch(CheckoutWorkspaceBranchRequest request, CallOptions options)

Checkout a branch in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckoutWorkspaceBranchRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CheckoutWorkspaceBranchRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### CheckoutWorkspaceBranch(CheckoutWorkspaceBranchRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty CheckoutWorkspaceBranch(CheckoutWorkspaceBranchRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Checkout a branch in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckoutWorkspaceBranchRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CheckoutWorkspaceBranchRequest)`  
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
  
### CheckoutWorkspaceBranchAsync(CheckoutWorkspaceBranchRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> CheckoutWorkspaceBranchAsync(CheckoutWorkspaceBranchRequest request, CallOptions options)

Checkout a branch in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckoutWorkspaceBranchRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CheckoutWorkspaceBranchRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### CheckoutWorkspaceBranchAsync(CheckoutWorkspaceBranchRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> CheckoutWorkspaceBranchAsync(CheckoutWorkspaceBranchRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Checkout a branch in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckoutWorkspaceBranchRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CheckoutWorkspaceBranchRequest)`  
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
  
### CommitRepositoryChanges(CommitRepositoryChangesRequest, CallOptions)
    
    
    public virtual CommitRepositoryChangesResponse CommitRepositoryChanges(CommitRepositoryChangesRequest request, CallOptions options)

Applies a Git commit to a Repository. The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CommitRepositoryChangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitRepositoryChangesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[CommitRepositoryChangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitRepositoryChangesResponse)` | The response received from the server.  
  
### CommitRepositoryChanges(CommitRepositoryChangesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual CommitRepositoryChangesResponse CommitRepositoryChanges(CommitRepositoryChangesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Applies a Git commit to a Repository. The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CommitRepositoryChangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitRepositoryChangesRequest)`  
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
`[CommitRepositoryChangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitRepositoryChangesResponse)` | The response received from the server.  
  
### CommitRepositoryChangesAsync(CommitRepositoryChangesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<CommitRepositoryChangesResponse> CommitRepositoryChangesAsync(CommitRepositoryChangesRequest request, CallOptions options)

Applies a Git commit to a Repository. The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CommitRepositoryChangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitRepositoryChangesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CommitRepositoryChangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitRepositoryChangesResponse)` | The call object.  
  
### CommitRepositoryChangesAsync(CommitRepositoryChangesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<CommitRepositoryChangesResponse> CommitRepositoryChangesAsync(CommitRepositoryChangesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Applies a Git commit to a Repository. The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CommitRepositoryChangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitRepositoryChangesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CommitRepositoryChangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitRepositoryChangesResponse)` | The call object.  
  
### CommitWorkspaceChanges(CommitWorkspaceChangesRequest, CallOptions)
    
    
    public virtual CommitWorkspaceChangesResponse CommitWorkspaceChanges(CommitWorkspaceChangesRequest request, CallOptions options)

Applies a Git commit for uncommitted files in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CommitWorkspaceChangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitWorkspaceChangesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[CommitWorkspaceChangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitWorkspaceChangesResponse)` | The response received from the server.  
  
### CommitWorkspaceChanges(CommitWorkspaceChangesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual CommitWorkspaceChangesResponse CommitWorkspaceChanges(CommitWorkspaceChangesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Applies a Git commit for uncommitted files in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CommitWorkspaceChangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitWorkspaceChangesRequest)`  
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
`[CommitWorkspaceChangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitWorkspaceChangesResponse)` | The response received from the server.  
  
### CommitWorkspaceChangesAsync(CommitWorkspaceChangesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<CommitWorkspaceChangesResponse> CommitWorkspaceChangesAsync(CommitWorkspaceChangesRequest request, CallOptions options)

Applies a Git commit for uncommitted files in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CommitWorkspaceChangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitWorkspaceChangesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CommitWorkspaceChangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitWorkspaceChangesResponse)` | The call object.  
  
### CommitWorkspaceChangesAsync(CommitWorkspaceChangesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<CommitWorkspaceChangesResponse> CommitWorkspaceChangesAsync(CommitWorkspaceChangesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Applies a Git commit for uncommitted files in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CommitWorkspaceChangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitWorkspaceChangesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CommitWorkspaceChangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CommitWorkspaceChangesResponse)` | The call object.  
  
### ComputeRepositoryAccessTokenStatus(ComputeRepositoryAccessTokenStatusRequest, CallOptions)
    
    
    public virtual ComputeRepositoryAccessTokenStatusResponse ComputeRepositoryAccessTokenStatus(ComputeRepositoryAccessTokenStatusRequest request, CallOptions options)

Computes a Repository's Git access token status.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ComputeRepositoryAccessTokenStatusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ComputeRepositoryAccessTokenStatusRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ComputeRepositoryAccessTokenStatusResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ComputeRepositoryAccessTokenStatusResponse)` | The response received from the server.  
  
### ComputeRepositoryAccessTokenStatus(ComputeRepositoryAccessTokenStatusRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ComputeRepositoryAccessTokenStatusResponse ComputeRepositoryAccessTokenStatus(ComputeRepositoryAccessTokenStatusRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Computes a Repository's Git access token status.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ComputeRepositoryAccessTokenStatusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ComputeRepositoryAccessTokenStatusRequest)`  
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
`[ComputeRepositoryAccessTokenStatusResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ComputeRepositoryAccessTokenStatusResponse)` | The response received from the server.  
  
### ComputeRepositoryAccessTokenStatusAsync(ComputeRepositoryAccessTokenStatusRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ComputeRepositoryAccessTokenStatusResponse> ComputeRepositoryAccessTokenStatusAsync(ComputeRepositoryAccessTokenStatusRequest request, CallOptions options)

Computes a Repository's Git access token status.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ComputeRepositoryAccessTokenStatusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ComputeRepositoryAccessTokenStatusRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ComputeRepositoryAccessTokenStatusResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ComputeRepositoryAccessTokenStatusResponse)` | The call object.  
  
### ComputeRepositoryAccessTokenStatusAsync(ComputeRepositoryAccessTokenStatusRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ComputeRepositoryAccessTokenStatusResponse> ComputeRepositoryAccessTokenStatusAsync(ComputeRepositoryAccessTokenStatusRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Computes a Repository's Git access token status.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ComputeRepositoryAccessTokenStatusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ComputeRepositoryAccessTokenStatusRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ComputeRepositoryAccessTokenStatusResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ComputeRepositoryAccessTokenStatusResponse)` | The call object.  
  
### CreateCompilationResult(CreateCompilationResultRequest, CallOptions)
    
    
    public virtual CompilationResult CreateCompilationResult(CreateCompilationResultRequest request, CallOptions options)

Creates a new CompilationResult in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCompilationResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateCompilationResultRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[CompilationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResult)` | The response received from the server.  
  
### CreateCompilationResult(CreateCompilationResultRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual CompilationResult CreateCompilationResult(CreateCompilationResultRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new CompilationResult in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCompilationResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateCompilationResultRequest)`  
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
`[CompilationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResult)` | The response received from the server.  
  
### CreateCompilationResultAsync(CreateCompilationResultRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<CompilationResult> CreateCompilationResultAsync(CreateCompilationResultRequest request, CallOptions options)

Creates a new CompilationResult in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCompilationResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateCompilationResultRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CompilationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResult)` | The call object.  
  
### CreateCompilationResultAsync(CreateCompilationResultRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<CompilationResult> CreateCompilationResultAsync(CreateCompilationResultRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new CompilationResult in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCompilationResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateCompilationResultRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CompilationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResult)` | The call object.  
  
### CreateFolder(CreateFolderRequest, CallOptions)
    
    
    public virtual Folder CreateFolder(CreateFolderRequest request, CallOptions options)

Creates a new Folder in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateFolderRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Folder)` | The response received from the server.  
  
### CreateFolder(CreateFolderRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Folder CreateFolder(CreateFolderRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Folder in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateFolderRequest)`  
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
`[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Folder)` | The response received from the server.  
  
### CreateFolderAsync(CreateFolderRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Folder> CreateFolderAsync(CreateFolderRequest request, CallOptions options)

Creates a new Folder in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateFolderRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Folder)` | The call object.  
  
### CreateFolderAsync(CreateFolderRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Folder> CreateFolderAsync(CreateFolderRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Folder in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateFolderRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Folder)` | The call object.  
  
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
  
### CreateReleaseConfig(CreateReleaseConfigRequest, CallOptions)
    
    
    public virtual ReleaseConfig CreateReleaseConfig(CreateReleaseConfigRequest request, CallOptions options)

Creates a new ReleaseConfig in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReleaseConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateReleaseConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig)` | The response received from the server.  
  
### CreateReleaseConfig(CreateReleaseConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ReleaseConfig CreateReleaseConfig(CreateReleaseConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new ReleaseConfig in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReleaseConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateReleaseConfigRequest)`  
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
`[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig)` | The response received from the server.  
  
### CreateReleaseConfigAsync(CreateReleaseConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ReleaseConfig> CreateReleaseConfigAsync(CreateReleaseConfigRequest request, CallOptions options)

Creates a new ReleaseConfig in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReleaseConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateReleaseConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig)` | The call object.  
  
### CreateReleaseConfigAsync(CreateReleaseConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ReleaseConfig> CreateReleaseConfigAsync(CreateReleaseConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new ReleaseConfig in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReleaseConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateReleaseConfigRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig)` | The call object.  
  
### CreateRepository(CreateRepositoryRequest, CallOptions)
    
    
    public virtual Repository CreateRepository(CreateRepositoryRequest request, CallOptions options)

Creates a new Repository in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateRepositoryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Repository)` | The response received from the server.  
  
### CreateRepository(CreateRepositoryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Repository CreateRepository(CreateRepositoryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Repository in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateRepositoryRequest)`  
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
`[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Repository)` | The response received from the server.  
  
### CreateRepositoryAsync(CreateRepositoryRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Repository> CreateRepositoryAsync(CreateRepositoryRequest request, CallOptions options)

Creates a new Repository in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateRepositoryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Repository)` | The call object.  
  
### CreateRepositoryAsync(CreateRepositoryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Repository> CreateRepositoryAsync(CreateRepositoryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Repository in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateRepositoryRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Repository)` | The call object.  
  
### CreateTeamFolder(CreateTeamFolderRequest, CallOptions)
    
    
    public virtual TeamFolder CreateTeamFolder(CreateTeamFolderRequest request, CallOptions options)

Creates a new TeamFolder in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTeamFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateTeamFolderRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[TeamFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.TeamFolder)` | The response received from the server.  
  
### CreateTeamFolder(CreateTeamFolderRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual TeamFolder CreateTeamFolder(CreateTeamFolderRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new TeamFolder in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTeamFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateTeamFolderRequest)`  
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
`[TeamFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.TeamFolder)` | The response received from the server.  
  
### CreateTeamFolderAsync(CreateTeamFolderRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<TeamFolder> CreateTeamFolderAsync(CreateTeamFolderRequest request, CallOptions options)

Creates a new TeamFolder in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTeamFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateTeamFolderRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[TeamFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.TeamFolder)` | The call object.  
  
### CreateTeamFolderAsync(CreateTeamFolderRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<TeamFolder> CreateTeamFolderAsync(CreateTeamFolderRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new TeamFolder in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTeamFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateTeamFolderRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[TeamFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.TeamFolder)` | The call object.  
  
### CreateWorkflowConfig(CreateWorkflowConfigRequest, CallOptions)
    
    
    public virtual WorkflowConfig CreateWorkflowConfig(CreateWorkflowConfigRequest request, CallOptions options)

Creates a new WorkflowConfig in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkflowConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateWorkflowConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfig)` | The response received from the server.  
  
### CreateWorkflowConfig(CreateWorkflowConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual WorkflowConfig CreateWorkflowConfig(CreateWorkflowConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new WorkflowConfig in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkflowConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateWorkflowConfigRequest)`  
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
`[WorkflowConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfig)` | The response received from the server.  
  
### CreateWorkflowConfigAsync(CreateWorkflowConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<WorkflowConfig> CreateWorkflowConfigAsync(CreateWorkflowConfigRequest request, CallOptions options)

Creates a new WorkflowConfig in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkflowConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateWorkflowConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[WorkflowConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfig)` | The call object.  
  
### CreateWorkflowConfigAsync(CreateWorkflowConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<WorkflowConfig> CreateWorkflowConfigAsync(CreateWorkflowConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new WorkflowConfig in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkflowConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateWorkflowConfigRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[WorkflowConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfig)` | The call object.  
  
### CreateWorkflowInvocation(CreateWorkflowInvocationRequest, CallOptions)
    
    
    public virtual WorkflowInvocation CreateWorkflowInvocation(CreateWorkflowInvocationRequest request, CallOptions options)

Creates a new WorkflowInvocation in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkflowInvocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateWorkflowInvocationRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowInvocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowInvocation)` | The response received from the server.  
  
### CreateWorkflowInvocation(CreateWorkflowInvocationRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual WorkflowInvocation CreateWorkflowInvocation(CreateWorkflowInvocationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new WorkflowInvocation in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkflowInvocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateWorkflowInvocationRequest)`  
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
`[WorkflowInvocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowInvocation)` | The response received from the server.  
  
### CreateWorkflowInvocationAsync(CreateWorkflowInvocationRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<WorkflowInvocation> CreateWorkflowInvocationAsync(CreateWorkflowInvocationRequest request, CallOptions options)

Creates a new WorkflowInvocation in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkflowInvocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateWorkflowInvocationRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[WorkflowInvocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowInvocation)` | The call object.  
  
### CreateWorkflowInvocationAsync(CreateWorkflowInvocationRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<WorkflowInvocation> CreateWorkflowInvocationAsync(CreateWorkflowInvocationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new WorkflowInvocation in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkflowInvocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateWorkflowInvocationRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[WorkflowInvocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowInvocation)` | The call object.  
  
### CreateWorkspace(CreateWorkspaceRequest, CallOptions)
    
    
    public virtual Workspace CreateWorkspace(CreateWorkspaceRequest request, CallOptions options)

Creates a new Workspace in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkspaceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateWorkspaceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Workspace](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Workspace)` | The response received from the server.  
  
### CreateWorkspace(CreateWorkspaceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Workspace CreateWorkspace(CreateWorkspaceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Workspace in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkspaceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateWorkspaceRequest)`  
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
`[Workspace](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Workspace)` | The response received from the server.  
  
### CreateWorkspaceAsync(CreateWorkspaceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Workspace> CreateWorkspaceAsync(CreateWorkspaceRequest request, CallOptions options)

Creates a new Workspace in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkspaceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateWorkspaceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Workspace](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Workspace)` | The call object.  
  
### CreateWorkspaceAsync(CreateWorkspaceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Workspace> CreateWorkspaceAsync(CreateWorkspaceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new Workspace in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkspaceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CreateWorkspaceRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Workspace](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Workspace)` | The call object.  
  
### DeleteBranch(DeleteBranchRequest, CallOptions)
    
    
    public virtual DeleteBranchResponse DeleteBranch(DeleteBranchRequest request, CallOptions options)

Deletes a branch in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBranchRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteBranchRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DeleteBranchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteBranchResponse)` | The response received from the server.  
  
### DeleteBranch(DeleteBranchRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DeleteBranchResponse DeleteBranch(DeleteBranchRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a branch in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBranchRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteBranchRequest)`  
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
`[DeleteBranchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteBranchResponse)` | The response received from the server.  
  
### DeleteBranchAsync(DeleteBranchRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DeleteBranchResponse> DeleteBranchAsync(DeleteBranchRequest request, CallOptions options)

Deletes a branch in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBranchRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteBranchRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DeleteBranchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteBranchResponse)` | The call object.  
  
### DeleteBranchAsync(DeleteBranchRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DeleteBranchResponse> DeleteBranchAsync(DeleteBranchRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a branch in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBranchRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteBranchRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DeleteBranchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteBranchResponse)` | The call object.  
  
### DeleteFolder(DeleteFolderRequest, CallOptions)
    
    
    public virtual Empty DeleteFolder(DeleteFolderRequest request, CallOptions options)

Deletes a single Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteFolderRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteFolder(DeleteFolderRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteFolder(DeleteFolderRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteFolderRequest)`  
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
  
### DeleteFolderAsync(DeleteFolderRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteFolderAsync(DeleteFolderRequest request, CallOptions options)

Deletes a single Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteFolderRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteFolderAsync(DeleteFolderRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteFolderAsync(DeleteFolderRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteFolderRequest)`  
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
  
### DeleteFolderTree(DeleteFolderTreeRequest, CallOptions)
    
    
    public virtual Operation DeleteFolderTree(DeleteFolderTreeRequest request, CallOptions options)

Deletes a Folder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFolderTreeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteFolderTreeRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteFolderTree(DeleteFolderTreeRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteFolderTree(DeleteFolderTreeRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a Folder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFolderTreeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteFolderTreeRequest)`  
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
  
### DeleteFolderTreeAsync(DeleteFolderTreeRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteFolderTreeAsync(DeleteFolderTreeRequest request, CallOptions options)

Deletes a Folder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFolderTreeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteFolderTreeRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteFolderTreeAsync(DeleteFolderTreeRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteFolderTreeAsync(DeleteFolderTreeRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a Folder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFolderTreeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteFolderTreeRequest)`  
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
  
### DeleteReleaseConfig(DeleteReleaseConfigRequest, CallOptions)
    
    
    public virtual Empty DeleteReleaseConfig(DeleteReleaseConfigRequest request, CallOptions options)

Deletes a single ReleaseConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReleaseConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteReleaseConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteReleaseConfig(DeleteReleaseConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteReleaseConfig(DeleteReleaseConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single ReleaseConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReleaseConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteReleaseConfigRequest)`  
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
  
### DeleteReleaseConfigAsync(DeleteReleaseConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteReleaseConfigAsync(DeleteReleaseConfigRequest request, CallOptions options)

Deletes a single ReleaseConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReleaseConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteReleaseConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteReleaseConfigAsync(DeleteReleaseConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteReleaseConfigAsync(DeleteReleaseConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single ReleaseConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReleaseConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteReleaseConfigRequest)`  
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
  
### DeleteRepository(DeleteRepositoryRequest, CallOptions)
    
    
    public virtual Empty DeleteRepository(DeleteRepositoryRequest request, CallOptions options)

Deletes a single Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteRepositoryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteRepository(DeleteRepositoryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteRepository(DeleteRepositoryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteRepositoryRequest)`  
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
  
### DeleteRepositoryAsync(DeleteRepositoryRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteRepositoryAsync(DeleteRepositoryRequest request, CallOptions options)

Deletes a single Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteRepositoryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteRepositoryAsync(DeleteRepositoryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteRepositoryAsync(DeleteRepositoryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteRepositoryRequest)`  
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
  
### DeleteRepositoryLongRunning(DeleteRepositoryLongRunningRequest, CallOptions)
    
    
    public virtual Operation DeleteRepositoryLongRunning(DeleteRepositoryLongRunningRequest request, CallOptions options)

Deletes a single repository asynchronously.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRepositoryLongRunningRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteRepositoryLongRunningRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteRepositoryLongRunning(DeleteRepositoryLongRunningRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteRepositoryLongRunning(DeleteRepositoryLongRunningRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single repository asynchronously.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRepositoryLongRunningRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteRepositoryLongRunningRequest)`  
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
  
### DeleteRepositoryLongRunningAsync(DeleteRepositoryLongRunningRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteRepositoryLongRunningAsync(DeleteRepositoryLongRunningRequest request, CallOptions options)

Deletes a single repository asynchronously.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRepositoryLongRunningRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteRepositoryLongRunningRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteRepositoryLongRunningAsync(DeleteRepositoryLongRunningRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteRepositoryLongRunningAsync(DeleteRepositoryLongRunningRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single repository asynchronously.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRepositoryLongRunningRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteRepositoryLongRunningRequest)`  
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
  
### DeleteTeamFolder(DeleteTeamFolderRequest, CallOptions)
    
    
    public virtual Empty DeleteTeamFolder(DeleteTeamFolderRequest request, CallOptions options)

Deletes a single TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTeamFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteTeamFolderRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteTeamFolder(DeleteTeamFolderRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteTeamFolder(DeleteTeamFolderRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTeamFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteTeamFolderRequest)`  
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
  
### DeleteTeamFolderAsync(DeleteTeamFolderRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteTeamFolderAsync(DeleteTeamFolderRequest request, CallOptions options)

Deletes a single TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTeamFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteTeamFolderRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteTeamFolderAsync(DeleteTeamFolderRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteTeamFolderAsync(DeleteTeamFolderRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTeamFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteTeamFolderRequest)`  
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
  
### DeleteTeamFolderTree(DeleteTeamFolderTreeRequest, CallOptions)
    
    
    public virtual Operation DeleteTeamFolderTree(DeleteTeamFolderTreeRequest request, CallOptions options)

Deletes a TeamFolder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTeamFolderTreeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteTeamFolderTreeRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### DeleteTeamFolderTree(DeleteTeamFolderTreeRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation DeleteTeamFolderTree(DeleteTeamFolderTreeRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a TeamFolder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTeamFolderTreeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteTeamFolderTreeRequest)`  
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
  
### DeleteTeamFolderTreeAsync(DeleteTeamFolderTreeRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteTeamFolderTreeAsync(DeleteTeamFolderTreeRequest request, CallOptions options)

Deletes a TeamFolder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTeamFolderTreeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteTeamFolderTreeRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### DeleteTeamFolderTreeAsync(DeleteTeamFolderTreeRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteTeamFolderTreeAsync(DeleteTeamFolderTreeRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a TeamFolder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTeamFolderTreeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteTeamFolderTreeRequest)`  
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
  
### DeleteWorkflowConfig(DeleteWorkflowConfigRequest, CallOptions)
    
    
    public virtual Empty DeleteWorkflowConfig(DeleteWorkflowConfigRequest request, CallOptions options)

Deletes a single WorkflowConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkflowConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteWorkflowConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteWorkflowConfig(DeleteWorkflowConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteWorkflowConfig(DeleteWorkflowConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single WorkflowConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkflowConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteWorkflowConfigRequest)`  
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
  
### DeleteWorkflowConfigAsync(DeleteWorkflowConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteWorkflowConfigAsync(DeleteWorkflowConfigRequest request, CallOptions options)

Deletes a single WorkflowConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkflowConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteWorkflowConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteWorkflowConfigAsync(DeleteWorkflowConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteWorkflowConfigAsync(DeleteWorkflowConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single WorkflowConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkflowConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteWorkflowConfigRequest)`  
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
  
### DeleteWorkflowInvocation(DeleteWorkflowInvocationRequest, CallOptions)
    
    
    public virtual Empty DeleteWorkflowInvocation(DeleteWorkflowInvocationRequest request, CallOptions options)

Deletes a single WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkflowInvocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteWorkflowInvocationRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteWorkflowInvocation(DeleteWorkflowInvocationRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteWorkflowInvocation(DeleteWorkflowInvocationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkflowInvocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteWorkflowInvocationRequest)`  
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
  
### DeleteWorkflowInvocationAsync(DeleteWorkflowInvocationRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteWorkflowInvocationAsync(DeleteWorkflowInvocationRequest request, CallOptions options)

Deletes a single WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkflowInvocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteWorkflowInvocationRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteWorkflowInvocationAsync(DeleteWorkflowInvocationRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteWorkflowInvocationAsync(DeleteWorkflowInvocationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkflowInvocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteWorkflowInvocationRequest)`  
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
  
### DeleteWorkspace(DeleteWorkspaceRequest, CallOptions)
    
    
    public virtual Empty DeleteWorkspace(DeleteWorkspaceRequest request, CallOptions options)

Deletes a single Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkspaceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteWorkspaceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The response received from the server.  
  
### DeleteWorkspace(DeleteWorkspaceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Empty DeleteWorkspace(DeleteWorkspaceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkspaceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteWorkspaceRequest)`  
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
  
### DeleteWorkspaceAsync(DeleteWorkspaceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteWorkspaceAsync(DeleteWorkspaceRequest request, CallOptions options)

Deletes a single Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkspaceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteWorkspaceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)` | The call object.  
  
### DeleteWorkspaceAsync(DeleteWorkspaceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Empty> DeleteWorkspaceAsync(DeleteWorkspaceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a single Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkspaceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.DeleteWorkspaceRequest)`  
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
  
### FetchCurrentWorkspaceBranch(FetchCurrentWorkspaceBranchRequest, CallOptions)
    
    
    public virtual FetchCurrentWorkspaceBranchResponse FetchCurrentWorkspaceBranch(FetchCurrentWorkspaceBranchRequest request, CallOptions options)

Fetches the current branch of a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchCurrentWorkspaceBranchRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchCurrentWorkspaceBranchRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FetchCurrentWorkspaceBranchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchCurrentWorkspaceBranchResponse)` | The response received from the server.  
  
### FetchCurrentWorkspaceBranch(FetchCurrentWorkspaceBranchRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FetchCurrentWorkspaceBranchResponse FetchCurrentWorkspaceBranch(FetchCurrentWorkspaceBranchRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches the current branch of a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchCurrentWorkspaceBranchRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchCurrentWorkspaceBranchRequest)`  
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
`[FetchCurrentWorkspaceBranchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchCurrentWorkspaceBranchResponse)` | The response received from the server.  
  
### FetchCurrentWorkspaceBranchAsync(FetchCurrentWorkspaceBranchRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FetchCurrentWorkspaceBranchResponse> FetchCurrentWorkspaceBranchAsync(FetchCurrentWorkspaceBranchRequest request, CallOptions options)

Fetches the current branch of a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchCurrentWorkspaceBranchRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchCurrentWorkspaceBranchRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FetchCurrentWorkspaceBranchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchCurrentWorkspaceBranchResponse)` | The call object.  
  
### FetchCurrentWorkspaceBranchAsync(FetchCurrentWorkspaceBranchRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FetchCurrentWorkspaceBranchResponse> FetchCurrentWorkspaceBranchAsync(FetchCurrentWorkspaceBranchRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches the current branch of a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchCurrentWorkspaceBranchRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchCurrentWorkspaceBranchRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FetchCurrentWorkspaceBranchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchCurrentWorkspaceBranchResponse)` | The call object.  
  
### FetchFileDiff(FetchFileDiffRequest, CallOptions)
    
    
    public virtual FetchFileDiffResponse FetchFileDiff(FetchFileDiffRequest request, CallOptions options)

Fetches Git diff for an uncommitted file in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchFileDiffRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchFileDiffRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FetchFileDiffResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchFileDiffResponse)` | The response received from the server.  
  
### FetchFileDiff(FetchFileDiffRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FetchFileDiffResponse FetchFileDiff(FetchFileDiffRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches Git diff for an uncommitted file in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchFileDiffRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchFileDiffRequest)`  
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
`[FetchFileDiffResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchFileDiffResponse)` | The response received from the server.  
  
### FetchFileDiffAsync(FetchFileDiffRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FetchFileDiffResponse> FetchFileDiffAsync(FetchFileDiffRequest request, CallOptions options)

Fetches Git diff for an uncommitted file in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchFileDiffRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchFileDiffRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FetchFileDiffResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchFileDiffResponse)` | The call object.  
  
### FetchFileDiffAsync(FetchFileDiffRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FetchFileDiffResponse> FetchFileDiffAsync(FetchFileDiffRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches Git diff for an uncommitted file in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchFileDiffRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchFileDiffRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FetchFileDiffResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchFileDiffResponse)` | The call object.  
  
### FetchFileGitStatuses(FetchFileGitStatusesRequest, CallOptions)
    
    
    public virtual FetchFileGitStatusesResponse FetchFileGitStatuses(FetchFileGitStatusesRequest request, CallOptions options)

Fetches Git statuses for the files in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchFileGitStatusesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchFileGitStatusesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FetchFileGitStatusesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchFileGitStatusesResponse)` | The response received from the server.  
  
### FetchFileGitStatuses(FetchFileGitStatusesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FetchFileGitStatusesResponse FetchFileGitStatuses(FetchFileGitStatusesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches Git statuses for the files in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchFileGitStatusesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchFileGitStatusesRequest)`  
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
`[FetchFileGitStatusesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchFileGitStatusesResponse)` | The response received from the server.  
  
### FetchFileGitStatusesAsync(FetchFileGitStatusesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FetchFileGitStatusesResponse> FetchFileGitStatusesAsync(FetchFileGitStatusesRequest request, CallOptions options)

Fetches Git statuses for the files in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchFileGitStatusesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchFileGitStatusesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FetchFileGitStatusesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchFileGitStatusesResponse)` | The call object.  
  
### FetchFileGitStatusesAsync(FetchFileGitStatusesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FetchFileGitStatusesResponse> FetchFileGitStatusesAsync(FetchFileGitStatusesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches Git statuses for the files in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchFileGitStatusesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchFileGitStatusesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FetchFileGitStatusesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchFileGitStatusesResponse)` | The call object.  
  
### FetchGitAheadBehind(FetchGitAheadBehindRequest, CallOptions)
    
    
    public virtual FetchGitAheadBehindResponse FetchGitAheadBehind(FetchGitAheadBehindRequest request, CallOptions options)

Fetches Git ahead/behind against a remote branch.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchGitAheadBehindRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchGitAheadBehindRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FetchGitAheadBehindResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchGitAheadBehindResponse)` | The response received from the server.  
  
### FetchGitAheadBehind(FetchGitAheadBehindRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FetchGitAheadBehindResponse FetchGitAheadBehind(FetchGitAheadBehindRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches Git ahead/behind against a remote branch.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchGitAheadBehindRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchGitAheadBehindRequest)`  
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
`[FetchGitAheadBehindResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchGitAheadBehindResponse)` | The response received from the server.  
  
### FetchGitAheadBehindAsync(FetchGitAheadBehindRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FetchGitAheadBehindResponse> FetchGitAheadBehindAsync(FetchGitAheadBehindRequest request, CallOptions options)

Fetches Git ahead/behind against a remote branch.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchGitAheadBehindRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchGitAheadBehindRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FetchGitAheadBehindResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchGitAheadBehindResponse)` | The call object.  
  
### FetchGitAheadBehindAsync(FetchGitAheadBehindRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FetchGitAheadBehindResponse> FetchGitAheadBehindAsync(FetchGitAheadBehindRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches Git ahead/behind against a remote branch.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchGitAheadBehindRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchGitAheadBehindRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FetchGitAheadBehindResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchGitAheadBehindResponse)` | The call object.  
  
### FetchRemoteBranches(FetchRemoteBranchesRequest, CallOptions)
    
    
    public virtual FetchRemoteBranchesResponse FetchRemoteBranches(FetchRemoteBranchesRequest request, CallOptions options)

Fetches a Repository's remote branches.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchRemoteBranchesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchRemoteBranchesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FetchRemoteBranchesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchRemoteBranchesResponse)` | The response received from the server.  
  
### FetchRemoteBranches(FetchRemoteBranchesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FetchRemoteBranchesResponse FetchRemoteBranches(FetchRemoteBranchesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches a Repository's remote branches.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchRemoteBranchesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchRemoteBranchesRequest)`  
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
`[FetchRemoteBranchesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchRemoteBranchesResponse)` | The response received from the server.  
  
### FetchRemoteBranchesAsync(FetchRemoteBranchesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FetchRemoteBranchesResponse> FetchRemoteBranchesAsync(FetchRemoteBranchesRequest request, CallOptions options)

Fetches a Repository's remote branches.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchRemoteBranchesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchRemoteBranchesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FetchRemoteBranchesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchRemoteBranchesResponse)` | The call object.  
  
### FetchRemoteBranchesAsync(FetchRemoteBranchesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FetchRemoteBranchesResponse> FetchRemoteBranchesAsync(FetchRemoteBranchesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches a Repository's remote branches.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchRemoteBranchesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchRemoteBranchesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FetchRemoteBranchesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchRemoteBranchesResponse)` | The call object.  
  
### FetchRepositoryHistory(FetchRepositoryHistoryRequest, CallOptions)
    
    
    public virtual FetchRepositoryHistoryResponse FetchRepositoryHistory(FetchRepositoryHistoryRequest request, CallOptions options)

Fetches a Repository's history of commits. The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchRepositoryHistoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchRepositoryHistoryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FetchRepositoryHistoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchRepositoryHistoryResponse)` | The response received from the server.  
  
### FetchRepositoryHistory(FetchRepositoryHistoryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FetchRepositoryHistoryResponse FetchRepositoryHistory(FetchRepositoryHistoryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches a Repository's history of commits. The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchRepositoryHistoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchRepositoryHistoryRequest)`  
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
`[FetchRepositoryHistoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchRepositoryHistoryResponse)` | The response received from the server.  
  
### FetchRepositoryHistoryAsync(FetchRepositoryHistoryRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FetchRepositoryHistoryResponse> FetchRepositoryHistoryAsync(FetchRepositoryHistoryRequest request, CallOptions options)

Fetches a Repository's history of commits. The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchRepositoryHistoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchRepositoryHistoryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FetchRepositoryHistoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchRepositoryHistoryResponse)` | The call object.  
  
### FetchRepositoryHistoryAsync(FetchRepositoryHistoryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FetchRepositoryHistoryResponse> FetchRepositoryHistoryAsync(FetchRepositoryHistoryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches a Repository's history of commits. The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchRepositoryHistoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchRepositoryHistoryRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FetchRepositoryHistoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchRepositoryHistoryResponse)` | The call object.  
  
### FetchWorkspaceBranches(FetchWorkspaceBranchesRequest, CallOptions)
    
    
    public virtual FetchWorkspaceBranchesResponse FetchWorkspaceBranches(FetchWorkspaceBranchesRequest request, CallOptions options)

Fetches branches in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchWorkspaceBranchesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchWorkspaceBranchesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FetchWorkspaceBranchesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchWorkspaceBranchesResponse)` | The response received from the server.  
  
### FetchWorkspaceBranches(FetchWorkspaceBranchesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FetchWorkspaceBranchesResponse FetchWorkspaceBranches(FetchWorkspaceBranchesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches branches in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchWorkspaceBranchesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchWorkspaceBranchesRequest)`  
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
`[FetchWorkspaceBranchesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchWorkspaceBranchesResponse)` | The response received from the server.  
  
### FetchWorkspaceBranchesAsync(FetchWorkspaceBranchesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FetchWorkspaceBranchesResponse> FetchWorkspaceBranchesAsync(FetchWorkspaceBranchesRequest request, CallOptions options)

Fetches branches in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchWorkspaceBranchesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchWorkspaceBranchesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FetchWorkspaceBranchesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchWorkspaceBranchesResponse)` | The call object.  
  
### FetchWorkspaceBranchesAsync(FetchWorkspaceBranchesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FetchWorkspaceBranchesResponse> FetchWorkspaceBranchesAsync(FetchWorkspaceBranchesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches branches in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchWorkspaceBranchesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchWorkspaceBranchesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FetchWorkspaceBranchesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.FetchWorkspaceBranchesResponse)` | The call object.  
  
### GetCompilationResult(GetCompilationResultRequest, CallOptions)
    
    
    public virtual CompilationResult GetCompilationResult(GetCompilationResultRequest request, CallOptions options)

Fetches a single CompilationResult.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCompilationResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetCompilationResultRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[CompilationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResult)` | The response received from the server.  
  
### GetCompilationResult(GetCompilationResultRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual CompilationResult GetCompilationResult(GetCompilationResultRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches a single CompilationResult.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCompilationResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetCompilationResultRequest)`  
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
`[CompilationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResult)` | The response received from the server.  
  
### GetCompilationResultAsync(GetCompilationResultRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<CompilationResult> GetCompilationResultAsync(GetCompilationResultRequest request, CallOptions options)

Fetches a single CompilationResult.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCompilationResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetCompilationResultRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CompilationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResult)` | The call object.  
  
### GetCompilationResultAsync(GetCompilationResultRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<CompilationResult> GetCompilationResultAsync(GetCompilationResultRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches a single CompilationResult.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCompilationResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetCompilationResultRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CompilationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.CompilationResult)` | The call object.  
  
### GetConfig(GetConfigRequest, CallOptions)
    
    
    public virtual Config GetConfig(GetConfigRequest request, CallOptions options)

Get default config for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Config](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Config)` | The response received from the server.  
  
### GetConfig(GetConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Config GetConfig(GetConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get default config for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetConfigRequest)`  
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
`[Config](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Config)` | The response received from the server.  
  
### GetConfigAsync(GetConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Config> GetConfigAsync(GetConfigRequest request, CallOptions options)

Get default config for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Config](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Config)` | The call object.  
  
### GetConfigAsync(GetConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Config> GetConfigAsync(GetConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get default config for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetConfigRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Config](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Config)` | The call object.  
  
### GetFolder(GetFolderRequest, CallOptions)
    
    
    public virtual Folder GetFolder(GetFolderRequest request, CallOptions options)

Fetches a single Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetFolderRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Folder)` | The response received from the server.  
  
### GetFolder(GetFolderRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Folder GetFolder(GetFolderRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches a single Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetFolderRequest)`  
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
`[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Folder)` | The response received from the server.  
  
### GetFolderAsync(GetFolderRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Folder> GetFolderAsync(GetFolderRequest request, CallOptions options)

Fetches a single Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetFolderRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Folder)` | The call object.  
  
### GetFolderAsync(GetFolderRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Folder> GetFolderAsync(GetFolderRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches a single Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetFolderRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Folder)` | The call object.  
  
### GetIamPolicy(GetIamPolicyRequest, CallOptions)
    
    
    public virtual Policy GetIamPolicy(GetIamPolicyRequest request, CallOptions options)

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The response received from the server.  
  
### GetIamPolicy(GetIamPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Policy GetIamPolicy(GetIamPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)`  
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
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The response received from the server.  
  
### GetIamPolicyAsync(GetIamPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Policy> GetIamPolicyAsync(GetIamPolicyRequest request, CallOptions options)

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The call object.  
  
### GetIamPolicyAsync(GetIamPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Policy> GetIamPolicyAsync(GetIamPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The call object.  
  
### GetReleaseConfig(GetReleaseConfigRequest, CallOptions)
    
    
    public virtual ReleaseConfig GetReleaseConfig(GetReleaseConfigRequest request, CallOptions options)

Fetches a single ReleaseConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReleaseConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetReleaseConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig)` | The response received from the server.  
  
### GetReleaseConfig(GetReleaseConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ReleaseConfig GetReleaseConfig(GetReleaseConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches a single ReleaseConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReleaseConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetReleaseConfigRequest)`  
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
`[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig)` | The response received from the server.  
  
### GetReleaseConfigAsync(GetReleaseConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ReleaseConfig> GetReleaseConfigAsync(GetReleaseConfigRequest request, CallOptions options)

Fetches a single ReleaseConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReleaseConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetReleaseConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig)` | The call object.  
  
### GetReleaseConfigAsync(GetReleaseConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ReleaseConfig> GetReleaseConfigAsync(GetReleaseConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches a single ReleaseConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReleaseConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetReleaseConfigRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig)` | The call object.  
  
### GetRepository(GetRepositoryRequest, CallOptions)
    
    
    public virtual Repository GetRepository(GetRepositoryRequest request, CallOptions options)

Fetches a single Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetRepositoryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Repository)` | The response received from the server.  
  
### GetRepository(GetRepositoryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Repository GetRepository(GetRepositoryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches a single Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetRepositoryRequest)`  
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
`[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Repository)` | The response received from the server.  
  
### GetRepositoryAsync(GetRepositoryRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Repository> GetRepositoryAsync(GetRepositoryRequest request, CallOptions options)

Fetches a single Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetRepositoryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Repository)` | The call object.  
  
### GetRepositoryAsync(GetRepositoryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Repository> GetRepositoryAsync(GetRepositoryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches a single Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetRepositoryRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Repository)` | The call object.  
  
### GetTeamFolder(GetTeamFolderRequest, CallOptions)
    
    
    public virtual TeamFolder GetTeamFolder(GetTeamFolderRequest request, CallOptions options)

Fetches a single TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTeamFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetTeamFolderRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[TeamFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.TeamFolder)` | The response received from the server.  
  
### GetTeamFolder(GetTeamFolderRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual TeamFolder GetTeamFolder(GetTeamFolderRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches a single TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTeamFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetTeamFolderRequest)`  
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
`[TeamFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.TeamFolder)` | The response received from the server.  
  
### GetTeamFolderAsync(GetTeamFolderRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<TeamFolder> GetTeamFolderAsync(GetTeamFolderRequest request, CallOptions options)

Fetches a single TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTeamFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetTeamFolderRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[TeamFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.TeamFolder)` | The call object.  
  
### GetTeamFolderAsync(GetTeamFolderRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<TeamFolder> GetTeamFolderAsync(GetTeamFolderRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches a single TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTeamFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetTeamFolderRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[TeamFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.TeamFolder)` | The call object.  
  
### GetWorkflowConfig(GetWorkflowConfigRequest, CallOptions)
    
    
    public virtual WorkflowConfig GetWorkflowConfig(GetWorkflowConfigRequest request, CallOptions options)

Fetches a single WorkflowConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkflowConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetWorkflowConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfig)` | The response received from the server.  
  
### GetWorkflowConfig(GetWorkflowConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual WorkflowConfig GetWorkflowConfig(GetWorkflowConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches a single WorkflowConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkflowConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetWorkflowConfigRequest)`  
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
`[WorkflowConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfig)` | The response received from the server.  
  
### GetWorkflowConfigAsync(GetWorkflowConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<WorkflowConfig> GetWorkflowConfigAsync(GetWorkflowConfigRequest request, CallOptions options)

Fetches a single WorkflowConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkflowConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetWorkflowConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[WorkflowConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfig)` | The call object.  
  
### GetWorkflowConfigAsync(GetWorkflowConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<WorkflowConfig> GetWorkflowConfigAsync(GetWorkflowConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches a single WorkflowConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkflowConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetWorkflowConfigRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[WorkflowConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfig)` | The call object.  
  
### GetWorkflowInvocation(GetWorkflowInvocationRequest, CallOptions)
    
    
    public virtual WorkflowInvocation GetWorkflowInvocation(GetWorkflowInvocationRequest request, CallOptions options)

Fetches a single WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkflowInvocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetWorkflowInvocationRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowInvocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowInvocation)` | The response received from the server.  
  
### GetWorkflowInvocation(GetWorkflowInvocationRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual WorkflowInvocation GetWorkflowInvocation(GetWorkflowInvocationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches a single WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkflowInvocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetWorkflowInvocationRequest)`  
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
`[WorkflowInvocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowInvocation)` | The response received from the server.  
  
### GetWorkflowInvocationAsync(GetWorkflowInvocationRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<WorkflowInvocation> GetWorkflowInvocationAsync(GetWorkflowInvocationRequest request, CallOptions options)

Fetches a single WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkflowInvocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetWorkflowInvocationRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[WorkflowInvocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowInvocation)` | The call object.  
  
### GetWorkflowInvocationAsync(GetWorkflowInvocationRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<WorkflowInvocation> GetWorkflowInvocationAsync(GetWorkflowInvocationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches a single WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkflowInvocationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetWorkflowInvocationRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[WorkflowInvocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowInvocation)` | The call object.  
  
### GetWorkspace(GetWorkspaceRequest, CallOptions)
    
    
    public virtual Workspace GetWorkspace(GetWorkspaceRequest request, CallOptions options)

Fetches a single Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkspaceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetWorkspaceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Workspace](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Workspace)` | The response received from the server.  
  
### GetWorkspace(GetWorkspaceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Workspace GetWorkspace(GetWorkspaceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches a single Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkspaceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetWorkspaceRequest)`  
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
`[Workspace](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Workspace)` | The response received from the server.  
  
### GetWorkspaceAsync(GetWorkspaceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Workspace> GetWorkspaceAsync(GetWorkspaceRequest request, CallOptions options)

Fetches a single Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkspaceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetWorkspaceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Workspace](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Workspace)` | The call object.  
  
### GetWorkspaceAsync(GetWorkspaceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Workspace> GetWorkspaceAsync(GetWorkspaceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Fetches a single Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkspaceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.GetWorkspaceRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Workspace](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Workspace)` | The call object.  
  
### InstallNpmPackages(InstallNpmPackagesRequest, CallOptions)
    
    
    public virtual InstallNpmPackagesResponse InstallNpmPackages(InstallNpmPackagesRequest request, CallOptions options)

Installs dependency NPM packages (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InstallNpmPackagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.InstallNpmPackagesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[InstallNpmPackagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.InstallNpmPackagesResponse)` | The response received from the server.  
  
### InstallNpmPackages(InstallNpmPackagesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual InstallNpmPackagesResponse InstallNpmPackages(InstallNpmPackagesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Installs dependency NPM packages (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InstallNpmPackagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.InstallNpmPackagesRequest)`  
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
`[InstallNpmPackagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.InstallNpmPackagesResponse)` | The response received from the server.  
  
### InstallNpmPackagesAsync(InstallNpmPackagesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<InstallNpmPackagesResponse> InstallNpmPackagesAsync(InstallNpmPackagesRequest request, CallOptions options)

Installs dependency NPM packages (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InstallNpmPackagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.InstallNpmPackagesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[InstallNpmPackagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.InstallNpmPackagesResponse)` | The call object.  
  
### InstallNpmPackagesAsync(InstallNpmPackagesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<InstallNpmPackagesResponse> InstallNpmPackagesAsync(InstallNpmPackagesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Installs dependency NPM packages (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InstallNpmPackagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.InstallNpmPackagesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[InstallNpmPackagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.InstallNpmPackagesResponse)` | The call object.  
  
### ListCompilationResults(ListCompilationResultsRequest, CallOptions)
    
    
    public virtual ListCompilationResultsResponse ListCompilationResults(ListCompilationResultsRequest request, CallOptions options)

Lists CompilationResults in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCompilationResultsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListCompilationResultsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListCompilationResultsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListCompilationResultsResponse)` | The response received from the server.  
  
### ListCompilationResults(ListCompilationResultsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListCompilationResultsResponse ListCompilationResults(ListCompilationResultsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists CompilationResults in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCompilationResultsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListCompilationResultsRequest)`  
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
`[ListCompilationResultsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListCompilationResultsResponse)` | The response received from the server.  
  
### ListCompilationResultsAsync(ListCompilationResultsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListCompilationResultsResponse> ListCompilationResultsAsync(ListCompilationResultsRequest request, CallOptions options)

Lists CompilationResults in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCompilationResultsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListCompilationResultsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListCompilationResultsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListCompilationResultsResponse)` | The call object.  
  
### ListCompilationResultsAsync(ListCompilationResultsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListCompilationResultsResponse> ListCompilationResultsAsync(ListCompilationResultsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists CompilationResults in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCompilationResultsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListCompilationResultsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListCompilationResultsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListCompilationResultsResponse)` | The call object.  
  
### ListReleaseConfigs(ListReleaseConfigsRequest, CallOptions)
    
    
    public virtual ListReleaseConfigsResponse ListReleaseConfigs(ListReleaseConfigsRequest request, CallOptions options)

Lists ReleaseConfigs in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReleaseConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListReleaseConfigsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListReleaseConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListReleaseConfigsResponse)` | The response received from the server.  
  
### ListReleaseConfigs(ListReleaseConfigsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListReleaseConfigsResponse ListReleaseConfigs(ListReleaseConfigsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists ReleaseConfigs in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReleaseConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListReleaseConfigsRequest)`  
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
`[ListReleaseConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListReleaseConfigsResponse)` | The response received from the server.  
  
### ListReleaseConfigsAsync(ListReleaseConfigsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListReleaseConfigsResponse> ListReleaseConfigsAsync(ListReleaseConfigsRequest request, CallOptions options)

Lists ReleaseConfigs in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReleaseConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListReleaseConfigsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListReleaseConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListReleaseConfigsResponse)` | The call object.  
  
### ListReleaseConfigsAsync(ListReleaseConfigsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListReleaseConfigsResponse> ListReleaseConfigsAsync(ListReleaseConfigsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists ReleaseConfigs in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReleaseConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListReleaseConfigsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListReleaseConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListReleaseConfigsResponse)` | The call object.  
  
### ListRepositories(ListRepositoriesRequest, CallOptions)
    
    
    public virtual ListRepositoriesResponse ListRepositories(ListRepositoriesRequest request, CallOptions options)

Lists Repositories in a given project and location.

**Note:** _This method can return repositories not shown in the[Dataform UI](https://console.cloud.google.com/bigquery/dataform)_.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRepositoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListRepositoriesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListRepositoriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListRepositoriesResponse)` | The response received from the server.  
  
### ListRepositories(ListRepositoriesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListRepositoriesResponse ListRepositories(ListRepositoriesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Repositories in a given project and location.

**Note:** _This method can return repositories not shown in the[Dataform UI](https://console.cloud.google.com/bigquery/dataform)_.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRepositoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListRepositoriesRequest)`  
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
`[ListRepositoriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListRepositoriesResponse)` | The response received from the server.  
  
### ListRepositoriesAsync(ListRepositoriesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListRepositoriesResponse> ListRepositoriesAsync(ListRepositoriesRequest request, CallOptions options)

Lists Repositories in a given project and location.

**Note:** _This method can return repositories not shown in the[Dataform UI](https://console.cloud.google.com/bigquery/dataform)_.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRepositoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListRepositoriesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListRepositoriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListRepositoriesResponse)` | The call object.  
  
### ListRepositoriesAsync(ListRepositoriesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListRepositoriesResponse> ListRepositoriesAsync(ListRepositoriesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Repositories in a given project and location.

**Note:** _This method can return repositories not shown in the[Dataform UI](https://console.cloud.google.com/bigquery/dataform)_.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRepositoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListRepositoriesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListRepositoriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListRepositoriesResponse)` | The call object.  
  
### ListWorkflowConfigs(ListWorkflowConfigsRequest, CallOptions)
    
    
    public virtual ListWorkflowConfigsResponse ListWorkflowConfigs(ListWorkflowConfigsRequest request, CallOptions options)

Lists WorkflowConfigs in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkflowConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkflowConfigsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListWorkflowConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkflowConfigsResponse)` | The response received from the server.  
  
### ListWorkflowConfigs(ListWorkflowConfigsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListWorkflowConfigsResponse ListWorkflowConfigs(ListWorkflowConfigsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists WorkflowConfigs in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkflowConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkflowConfigsRequest)`  
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
`[ListWorkflowConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkflowConfigsResponse)` | The response received from the server.  
  
### ListWorkflowConfigsAsync(ListWorkflowConfigsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListWorkflowConfigsResponse> ListWorkflowConfigsAsync(ListWorkflowConfigsRequest request, CallOptions options)

Lists WorkflowConfigs in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkflowConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkflowConfigsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListWorkflowConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkflowConfigsResponse)` | The call object.  
  
### ListWorkflowConfigsAsync(ListWorkflowConfigsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListWorkflowConfigsResponse> ListWorkflowConfigsAsync(ListWorkflowConfigsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists WorkflowConfigs in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkflowConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkflowConfigsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListWorkflowConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkflowConfigsResponse)` | The call object.  
  
### ListWorkflowInvocations(ListWorkflowInvocationsRequest, CallOptions)
    
    
    public virtual ListWorkflowInvocationsResponse ListWorkflowInvocations(ListWorkflowInvocationsRequest request, CallOptions options)

Lists WorkflowInvocations in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkflowInvocationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkflowInvocationsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListWorkflowInvocationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkflowInvocationsResponse)` | The response received from the server.  
  
### ListWorkflowInvocations(ListWorkflowInvocationsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListWorkflowInvocationsResponse ListWorkflowInvocations(ListWorkflowInvocationsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists WorkflowInvocations in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkflowInvocationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkflowInvocationsRequest)`  
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
`[ListWorkflowInvocationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkflowInvocationsResponse)` | The response received from the server.  
  
### ListWorkflowInvocationsAsync(ListWorkflowInvocationsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListWorkflowInvocationsResponse> ListWorkflowInvocationsAsync(ListWorkflowInvocationsRequest request, CallOptions options)

Lists WorkflowInvocations in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkflowInvocationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkflowInvocationsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListWorkflowInvocationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkflowInvocationsResponse)` | The call object.  
  
### ListWorkflowInvocationsAsync(ListWorkflowInvocationsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListWorkflowInvocationsResponse> ListWorkflowInvocationsAsync(ListWorkflowInvocationsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists WorkflowInvocations in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkflowInvocationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkflowInvocationsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListWorkflowInvocationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkflowInvocationsResponse)` | The call object.  
  
### ListWorkspaces(ListWorkspacesRequest, CallOptions)
    
    
    public virtual ListWorkspacesResponse ListWorkspaces(ListWorkspacesRequest request, CallOptions options)

Lists Workspaces in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkspacesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkspacesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListWorkspacesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkspacesResponse)` | The response received from the server.  
  
### ListWorkspaces(ListWorkspacesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListWorkspacesResponse ListWorkspaces(ListWorkspacesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Workspaces in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkspacesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkspacesRequest)`  
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
`[ListWorkspacesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkspacesResponse)` | The response received from the server.  
  
### ListWorkspacesAsync(ListWorkspacesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListWorkspacesResponse> ListWorkspacesAsync(ListWorkspacesRequest request, CallOptions options)

Lists Workspaces in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkspacesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkspacesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListWorkspacesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkspacesResponse)` | The call object.  
  
### ListWorkspacesAsync(ListWorkspacesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListWorkspacesResponse> ListWorkspacesAsync(ListWorkspacesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists Workspaces in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkspacesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkspacesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListWorkspacesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListWorkspacesResponse)` | The call object.  
  
### MakeDirectory(MakeDirectoryRequest, CallOptions)
    
    
    public virtual MakeDirectoryResponse MakeDirectory(MakeDirectoryRequest request, CallOptions options)

Creates a directory inside a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MakeDirectoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MakeDirectoryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[MakeDirectoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MakeDirectoryResponse)` | The response received from the server.  
  
### MakeDirectory(MakeDirectoryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual MakeDirectoryResponse MakeDirectory(MakeDirectoryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a directory inside a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MakeDirectoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MakeDirectoryRequest)`  
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
`[MakeDirectoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MakeDirectoryResponse)` | The response received from the server.  
  
### MakeDirectoryAsync(MakeDirectoryRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<MakeDirectoryResponse> MakeDirectoryAsync(MakeDirectoryRequest request, CallOptions options)

Creates a directory inside a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MakeDirectoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MakeDirectoryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[MakeDirectoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MakeDirectoryResponse)` | The call object.  
  
### MakeDirectoryAsync(MakeDirectoryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<MakeDirectoryResponse> MakeDirectoryAsync(MakeDirectoryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a directory inside a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MakeDirectoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MakeDirectoryRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[MakeDirectoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MakeDirectoryResponse)` | The call object.  
  
### MoveDirectory(MoveDirectoryRequest, CallOptions)
    
    
    public virtual MoveDirectoryResponse MoveDirectory(MoveDirectoryRequest request, CallOptions options)

Moves a directory (inside a Workspace), and all of its contents, to a new location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveDirectoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveDirectoryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[MoveDirectoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveDirectoryResponse)` | The response received from the server.  
  
### MoveDirectory(MoveDirectoryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual MoveDirectoryResponse MoveDirectory(MoveDirectoryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Moves a directory (inside a Workspace), and all of its contents, to a new location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveDirectoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveDirectoryRequest)`  
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
`[MoveDirectoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveDirectoryResponse)` | The response received from the server.  
  
### MoveDirectoryAsync(MoveDirectoryRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<MoveDirectoryResponse> MoveDirectoryAsync(MoveDirectoryRequest request, CallOptions options)

Moves a directory (inside a Workspace), and all of its contents, to a new location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveDirectoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveDirectoryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[MoveDirectoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveDirectoryResponse)` | The call object.  
  
### MoveDirectoryAsync(MoveDirectoryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<MoveDirectoryResponse> MoveDirectoryAsync(MoveDirectoryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Moves a directory (inside a Workspace), and all of its contents, to a new location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveDirectoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveDirectoryRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[MoveDirectoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveDirectoryResponse)` | The call object.  
  
### MoveFile(MoveFileRequest, CallOptions)
    
    
    public virtual MoveFileResponse MoveFile(MoveFileRequest request, CallOptions options)

Moves a file (inside a Workspace) to a new location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveFileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[MoveFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveFileResponse)` | The response received from the server.  
  
### MoveFile(MoveFileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual MoveFileResponse MoveFile(MoveFileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Moves a file (inside a Workspace) to a new location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveFileRequest)`  
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
`[MoveFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveFileResponse)` | The response received from the server.  
  
### MoveFileAsync(MoveFileRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<MoveFileResponse> MoveFileAsync(MoveFileRequest request, CallOptions options)

Moves a file (inside a Workspace) to a new location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveFileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[MoveFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveFileResponse)` | The call object.  
  
### MoveFileAsync(MoveFileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<MoveFileResponse> MoveFileAsync(MoveFileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Moves a file (inside a Workspace) to a new location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveFileRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[MoveFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveFileResponse)` | The call object.  
  
### MoveFolder(MoveFolderRequest, CallOptions)
    
    
    public virtual Operation MoveFolder(MoveFolderRequest request, CallOptions options)

Moves a Folder to a new Folder, TeamFolder, or the root location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveFolderRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### MoveFolder(MoveFolderRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation MoveFolder(MoveFolderRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Moves a Folder to a new Folder, TeamFolder, or the root location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveFolderRequest)`  
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
  
### MoveFolderAsync(MoveFolderRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> MoveFolderAsync(MoveFolderRequest request, CallOptions options)

Moves a Folder to a new Folder, TeamFolder, or the root location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveFolderRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### MoveFolderAsync(MoveFolderRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> MoveFolderAsync(MoveFolderRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Moves a Folder to a new Folder, TeamFolder, or the root location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveFolderRequest)`  
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
  
### MoveRepository(MoveRepositoryRequest, CallOptions)
    
    
    public virtual Operation MoveRepository(MoveRepositoryRequest request, CallOptions options)

Moves a Repository to a new location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveRepositoryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response received from the server.  
  
### MoveRepository(MoveRepositoryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation MoveRepository(MoveRepositoryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Moves a Repository to a new location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveRepositoryRequest)`  
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
  
### MoveRepositoryAsync(MoveRepositoryRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> MoveRepositoryAsync(MoveRepositoryRequest request, CallOptions options)

Moves a Repository to a new location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveRepositoryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The call object.  
  
### MoveRepositoryAsync(MoveRepositoryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> MoveRepositoryAsync(MoveRepositoryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Moves a Repository to a new location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.MoveRepositoryRequest)`  
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
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override Dataform.DataformClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Dataform](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Dataform)[DataformClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Dataform.DataformClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Dataform.V1Beta1.Dataform.DataformClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### PullGitCommits(PullGitCommitsRequest, CallOptions)
    
    
    public virtual PullGitCommitsResponse PullGitCommits(PullGitCommitsRequest request, CallOptions options)

Pulls Git commits from the Repository's remote into a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PullGitCommitsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.PullGitCommitsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[PullGitCommitsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.PullGitCommitsResponse)` | The response received from the server.  
  
### PullGitCommits(PullGitCommitsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual PullGitCommitsResponse PullGitCommits(PullGitCommitsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Pulls Git commits from the Repository's remote into a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PullGitCommitsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.PullGitCommitsRequest)`  
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
`[PullGitCommitsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.PullGitCommitsResponse)` | The response received from the server.  
  
### PullGitCommitsAsync(PullGitCommitsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<PullGitCommitsResponse> PullGitCommitsAsync(PullGitCommitsRequest request, CallOptions options)

Pulls Git commits from the Repository's remote into a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PullGitCommitsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.PullGitCommitsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[PullGitCommitsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.PullGitCommitsResponse)` | The call object.  
  
### PullGitCommitsAsync(PullGitCommitsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<PullGitCommitsResponse> PullGitCommitsAsync(PullGitCommitsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Pulls Git commits from the Repository's remote into a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PullGitCommitsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.PullGitCommitsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[PullGitCommitsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.PullGitCommitsResponse)` | The call object.  
  
### PushGitCommits(PushGitCommitsRequest, CallOptions)
    
    
    public virtual PushGitCommitsResponse PushGitCommits(PushGitCommitsRequest request, CallOptions options)

Pushes Git commits from a Workspace to the Repository's remote.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PushGitCommitsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.PushGitCommitsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[PushGitCommitsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.PushGitCommitsResponse)` | The response received from the server.  
  
### PushGitCommits(PushGitCommitsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual PushGitCommitsResponse PushGitCommits(PushGitCommitsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Pushes Git commits from a Workspace to the Repository's remote.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PushGitCommitsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.PushGitCommitsRequest)`  
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
`[PushGitCommitsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.PushGitCommitsResponse)` | The response received from the server.  
  
### PushGitCommitsAsync(PushGitCommitsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<PushGitCommitsResponse> PushGitCommitsAsync(PushGitCommitsRequest request, CallOptions options)

Pushes Git commits from a Workspace to the Repository's remote.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PushGitCommitsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.PushGitCommitsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[PushGitCommitsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.PushGitCommitsResponse)` | The call object.  
  
### PushGitCommitsAsync(PushGitCommitsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<PushGitCommitsResponse> PushGitCommitsAsync(PushGitCommitsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Pushes Git commits from a Workspace to the Repository's remote.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PushGitCommitsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.PushGitCommitsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[PushGitCommitsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.PushGitCommitsResponse)` | The call object.  
  
### QueryCompilationResultActions(QueryCompilationResultActionsRequest, CallOptions)
    
    
    public virtual QueryCompilationResultActionsResponse QueryCompilationResultActions(QueryCompilationResultActionsRequest request, CallOptions options)

Returns CompilationResultActions in a given CompilationResult.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryCompilationResultActionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryCompilationResultActionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryCompilationResultActionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryCompilationResultActionsResponse)` | The response received from the server.  
  
### QueryCompilationResultActions(QueryCompilationResultActionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual QueryCompilationResultActionsResponse QueryCompilationResultActions(QueryCompilationResultActionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns CompilationResultActions in a given CompilationResult.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryCompilationResultActionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryCompilationResultActionsRequest)`  
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
`[QueryCompilationResultActionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryCompilationResultActionsResponse)` | The response received from the server.  
  
### QueryCompilationResultActionsAsync(QueryCompilationResultActionsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<QueryCompilationResultActionsResponse> QueryCompilationResultActionsAsync(QueryCompilationResultActionsRequest request, CallOptions options)

Returns CompilationResultActions in a given CompilationResult.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryCompilationResultActionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryCompilationResultActionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryCompilationResultActionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryCompilationResultActionsResponse)` | The call object.  
  
### QueryCompilationResultActionsAsync(QueryCompilationResultActionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<QueryCompilationResultActionsResponse> QueryCompilationResultActionsAsync(QueryCompilationResultActionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns CompilationResultActions in a given CompilationResult.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryCompilationResultActionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryCompilationResultActionsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryCompilationResultActionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryCompilationResultActionsResponse)` | The call object.  
  
### QueryDirectoryContents(QueryDirectoryContentsRequest, CallOptions)
    
    
    public virtual QueryDirectoryContentsResponse QueryDirectoryContents(QueryDirectoryContentsRequest request, CallOptions options)

Returns the contents of a given Workspace directory.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryDirectoryContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryDirectoryContentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryDirectoryContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryDirectoryContentsResponse)` | The response received from the server.  
  
### QueryDirectoryContents(QueryDirectoryContentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual QueryDirectoryContentsResponse QueryDirectoryContents(QueryDirectoryContentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the contents of a given Workspace directory.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryDirectoryContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryDirectoryContentsRequest)`  
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
`[QueryDirectoryContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryDirectoryContentsResponse)` | The response received from the server.  
  
### QueryDirectoryContentsAsync(QueryDirectoryContentsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<QueryDirectoryContentsResponse> QueryDirectoryContentsAsync(QueryDirectoryContentsRequest request, CallOptions options)

Returns the contents of a given Workspace directory.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryDirectoryContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryDirectoryContentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryDirectoryContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryDirectoryContentsResponse)` | The call object.  
  
### QueryDirectoryContentsAsync(QueryDirectoryContentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<QueryDirectoryContentsResponse> QueryDirectoryContentsAsync(QueryDirectoryContentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the contents of a given Workspace directory.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryDirectoryContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryDirectoryContentsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryDirectoryContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryDirectoryContentsResponse)` | The call object.  
  
### QueryFolderContents(QueryFolderContentsRequest, CallOptions)
    
    
    public virtual QueryFolderContentsResponse QueryFolderContents(QueryFolderContentsRequest request, CallOptions options)

Returns the contents of a given Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryFolderContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryFolderContentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryFolderContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryFolderContentsResponse)` | The response received from the server.  
  
### QueryFolderContents(QueryFolderContentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual QueryFolderContentsResponse QueryFolderContents(QueryFolderContentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the contents of a given Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryFolderContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryFolderContentsRequest)`  
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
`[QueryFolderContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryFolderContentsResponse)` | The response received from the server.  
  
### QueryFolderContentsAsync(QueryFolderContentsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<QueryFolderContentsResponse> QueryFolderContentsAsync(QueryFolderContentsRequest request, CallOptions options)

Returns the contents of a given Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryFolderContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryFolderContentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryFolderContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryFolderContentsResponse)` | The call object.  
  
### QueryFolderContentsAsync(QueryFolderContentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<QueryFolderContentsResponse> QueryFolderContentsAsync(QueryFolderContentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the contents of a given Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryFolderContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryFolderContentsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryFolderContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryFolderContentsResponse)` | The call object.  
  
### QueryRepositoryDirectoryContents(QueryRepositoryDirectoryContentsRequest, CallOptions)
    
    
    public virtual QueryRepositoryDirectoryContentsResponse QueryRepositoryDirectoryContents(QueryRepositoryDirectoryContentsRequest request, CallOptions options)

Returns the contents of a given Repository directory. The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryRepositoryDirectoryContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryRepositoryDirectoryContentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryRepositoryDirectoryContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryRepositoryDirectoryContentsResponse)` | The response received from the server.  
  
### QueryRepositoryDirectoryContents(QueryRepositoryDirectoryContentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual QueryRepositoryDirectoryContentsResponse QueryRepositoryDirectoryContents(QueryRepositoryDirectoryContentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the contents of a given Repository directory. The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryRepositoryDirectoryContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryRepositoryDirectoryContentsRequest)`  
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
`[QueryRepositoryDirectoryContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryRepositoryDirectoryContentsResponse)` | The response received from the server.  
  
### QueryRepositoryDirectoryContentsAsync(QueryRepositoryDirectoryContentsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<QueryRepositoryDirectoryContentsResponse> QueryRepositoryDirectoryContentsAsync(QueryRepositoryDirectoryContentsRequest request, CallOptions options)

Returns the contents of a given Repository directory. The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryRepositoryDirectoryContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryRepositoryDirectoryContentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryRepositoryDirectoryContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryRepositoryDirectoryContentsResponse)` | The call object.  
  
### QueryRepositoryDirectoryContentsAsync(QueryRepositoryDirectoryContentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<QueryRepositoryDirectoryContentsResponse> QueryRepositoryDirectoryContentsAsync(QueryRepositoryDirectoryContentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the contents of a given Repository directory. The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryRepositoryDirectoryContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryRepositoryDirectoryContentsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryRepositoryDirectoryContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryRepositoryDirectoryContentsResponse)` | The call object.  
  
### QueryTeamFolderContents(QueryTeamFolderContentsRequest, CallOptions)
    
    
    public virtual QueryTeamFolderContentsResponse QueryTeamFolderContents(QueryTeamFolderContentsRequest request, CallOptions options)

Returns the contents of a given TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryTeamFolderContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryTeamFolderContentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryTeamFolderContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryTeamFolderContentsResponse)` | The response received from the server.  
  
### QueryTeamFolderContents(QueryTeamFolderContentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual QueryTeamFolderContentsResponse QueryTeamFolderContents(QueryTeamFolderContentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the contents of a given TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryTeamFolderContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryTeamFolderContentsRequest)`  
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
`[QueryTeamFolderContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryTeamFolderContentsResponse)` | The response received from the server.  
  
### QueryTeamFolderContentsAsync(QueryTeamFolderContentsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<QueryTeamFolderContentsResponse> QueryTeamFolderContentsAsync(QueryTeamFolderContentsRequest request, CallOptions options)

Returns the contents of a given TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryTeamFolderContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryTeamFolderContentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryTeamFolderContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryTeamFolderContentsResponse)` | The call object.  
  
### QueryTeamFolderContentsAsync(QueryTeamFolderContentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<QueryTeamFolderContentsResponse> QueryTeamFolderContentsAsync(QueryTeamFolderContentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the contents of a given TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryTeamFolderContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryTeamFolderContentsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryTeamFolderContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryTeamFolderContentsResponse)` | The call object.  
  
### QueryUserRootContents(QueryUserRootContentsRequest, CallOptions)
    
    
    public virtual QueryUserRootContentsResponse QueryUserRootContents(QueryUserRootContentsRequest request, CallOptions options)

Returns the contents of a caller's root folder in a given location. The root folder contains all resources that are created by the user and not contained in any other folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryUserRootContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryUserRootContentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryUserRootContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryUserRootContentsResponse)` | The response received from the server.  
  
### QueryUserRootContents(QueryUserRootContentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual QueryUserRootContentsResponse QueryUserRootContents(QueryUserRootContentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the contents of a caller's root folder in a given location. The root folder contains all resources that are created by the user and not contained in any other folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryUserRootContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryUserRootContentsRequest)`  
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
`[QueryUserRootContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryUserRootContentsResponse)` | The response received from the server.  
  
### QueryUserRootContentsAsync(QueryUserRootContentsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<QueryUserRootContentsResponse> QueryUserRootContentsAsync(QueryUserRootContentsRequest request, CallOptions options)

Returns the contents of a caller's root folder in a given location. The root folder contains all resources that are created by the user and not contained in any other folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryUserRootContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryUserRootContentsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryUserRootContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryUserRootContentsResponse)` | The call object.  
  
### QueryUserRootContentsAsync(QueryUserRootContentsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<QueryUserRootContentsResponse> QueryUserRootContentsAsync(QueryUserRootContentsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the contents of a caller's root folder in a given location. The root folder contains all resources that are created by the user and not contained in any other folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryUserRootContentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryUserRootContentsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryUserRootContentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryUserRootContentsResponse)` | The call object.  
  
### QueryWorkflowInvocationActions(QueryWorkflowInvocationActionsRequest, CallOptions)
    
    
    public virtual QueryWorkflowInvocationActionsResponse QueryWorkflowInvocationActions(QueryWorkflowInvocationActionsRequest request, CallOptions options)

Returns WorkflowInvocationActions in a given WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryWorkflowInvocationActionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryWorkflowInvocationActionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryWorkflowInvocationActionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryWorkflowInvocationActionsResponse)` | The response received from the server.  
  
### QueryWorkflowInvocationActions(QueryWorkflowInvocationActionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual QueryWorkflowInvocationActionsResponse QueryWorkflowInvocationActions(QueryWorkflowInvocationActionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns WorkflowInvocationActions in a given WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryWorkflowInvocationActionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryWorkflowInvocationActionsRequest)`  
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
`[QueryWorkflowInvocationActionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryWorkflowInvocationActionsResponse)` | The response received from the server.  
  
### QueryWorkflowInvocationActionsAsync(QueryWorkflowInvocationActionsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<QueryWorkflowInvocationActionsResponse> QueryWorkflowInvocationActionsAsync(QueryWorkflowInvocationActionsRequest request, CallOptions options)

Returns WorkflowInvocationActions in a given WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryWorkflowInvocationActionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryWorkflowInvocationActionsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryWorkflowInvocationActionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryWorkflowInvocationActionsResponse)` | The call object.  
  
### QueryWorkflowInvocationActionsAsync(QueryWorkflowInvocationActionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<QueryWorkflowInvocationActionsResponse> QueryWorkflowInvocationActionsAsync(QueryWorkflowInvocationActionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns WorkflowInvocationActions in a given WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryWorkflowInvocationActionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryWorkflowInvocationActionsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QueryWorkflowInvocationActionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.QueryWorkflowInvocationActionsResponse)` | The call object.  
  
### ReadFile(ReadFileRequest, CallOptions)
    
    
    public virtual ReadFileResponse ReadFile(ReadFileRequest request, CallOptions options)

Returns the contents of a file (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReadFileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ReadFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReadFileResponse)` | The response received from the server.  
  
### ReadFile(ReadFileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ReadFileResponse ReadFile(ReadFileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the contents of a file (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReadFileRequest)`  
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
`[ReadFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReadFileResponse)` | The response received from the server.  
  
### ReadFileAsync(ReadFileRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ReadFileResponse> ReadFileAsync(ReadFileRequest request, CallOptions options)

Returns the contents of a file (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReadFileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ReadFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReadFileResponse)` | The call object.  
  
### ReadFileAsync(ReadFileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ReadFileResponse> ReadFileAsync(ReadFileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the contents of a file (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReadFileRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ReadFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReadFileResponse)` | The call object.  
  
### ReadRepositoryFile(ReadRepositoryFileRequest, CallOptions)
    
    
    public virtual ReadRepositoryFileResponse ReadRepositoryFile(ReadRepositoryFileRequest request, CallOptions options)

Returns the contents of a file (inside a Repository). The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadRepositoryFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReadRepositoryFileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ReadRepositoryFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReadRepositoryFileResponse)` | The response received from the server.  
  
### ReadRepositoryFile(ReadRepositoryFileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ReadRepositoryFileResponse ReadRepositoryFile(ReadRepositoryFileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the contents of a file (inside a Repository). The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadRepositoryFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReadRepositoryFileRequest)`  
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
`[ReadRepositoryFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReadRepositoryFileResponse)` | The response received from the server.  
  
### ReadRepositoryFileAsync(ReadRepositoryFileRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ReadRepositoryFileResponse> ReadRepositoryFileAsync(ReadRepositoryFileRequest request, CallOptions options)

Returns the contents of a file (inside a Repository). The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadRepositoryFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReadRepositoryFileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ReadRepositoryFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReadRepositoryFileResponse)` | The call object.  
  
### ReadRepositoryFileAsync(ReadRepositoryFileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ReadRepositoryFileResponse> ReadRepositoryFileAsync(ReadRepositoryFileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the contents of a file (inside a Repository). The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadRepositoryFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReadRepositoryFileRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ReadRepositoryFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReadRepositoryFileResponse)` | The call object.  
  
### RemoveDirectory(RemoveDirectoryRequest, CallOptions)
    
    
    public virtual RemoveDirectoryResponse RemoveDirectory(RemoveDirectoryRequest request, CallOptions options)

Deletes a directory (inside a Workspace) and all of its contents.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveDirectoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.RemoveDirectoryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[RemoveDirectoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.RemoveDirectoryResponse)` | The response received from the server.  
  
### RemoveDirectory(RemoveDirectoryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual RemoveDirectoryResponse RemoveDirectory(RemoveDirectoryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a directory (inside a Workspace) and all of its contents.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveDirectoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.RemoveDirectoryRequest)`  
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
`[RemoveDirectoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.RemoveDirectoryResponse)` | The response received from the server.  
  
### RemoveDirectoryAsync(RemoveDirectoryRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<RemoveDirectoryResponse> RemoveDirectoryAsync(RemoveDirectoryRequest request, CallOptions options)

Deletes a directory (inside a Workspace) and all of its contents.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveDirectoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.RemoveDirectoryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[RemoveDirectoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.RemoveDirectoryResponse)` | The call object.  
  
### RemoveDirectoryAsync(RemoveDirectoryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<RemoveDirectoryResponse> RemoveDirectoryAsync(RemoveDirectoryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a directory (inside a Workspace) and all of its contents.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveDirectoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.RemoveDirectoryRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[RemoveDirectoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.RemoveDirectoryResponse)` | The call object.  
  
### RemoveFile(RemoveFileRequest, CallOptions)
    
    
    public virtual RemoveFileResponse RemoveFile(RemoveFileRequest request, CallOptions options)

Deletes a file (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.RemoveFileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[RemoveFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.RemoveFileResponse)` | The response received from the server.  
  
### RemoveFile(RemoveFileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual RemoveFileResponse RemoveFile(RemoveFileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a file (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.RemoveFileRequest)`  
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
`[RemoveFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.RemoveFileResponse)` | The response received from the server.  
  
### RemoveFileAsync(RemoveFileRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<RemoveFileResponse> RemoveFileAsync(RemoveFileRequest request, CallOptions options)

Deletes a file (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.RemoveFileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[RemoveFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.RemoveFileResponse)` | The call object.  
  
### RemoveFileAsync(RemoveFileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<RemoveFileResponse> RemoveFileAsync(RemoveFileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a file (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.RemoveFileRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[RemoveFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.RemoveFileResponse)` | The call object.  
  
### ResetWorkspaceChanges(ResetWorkspaceChangesRequest, CallOptions)
    
    
    public virtual ResetWorkspaceChangesResponse ResetWorkspaceChanges(ResetWorkspaceChangesRequest request, CallOptions options)

Performs a Git reset for uncommitted files in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResetWorkspaceChangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ResetWorkspaceChangesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ResetWorkspaceChangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ResetWorkspaceChangesResponse)` | The response received from the server.  
  
### ResetWorkspaceChanges(ResetWorkspaceChangesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ResetWorkspaceChangesResponse ResetWorkspaceChanges(ResetWorkspaceChangesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Performs a Git reset for uncommitted files in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResetWorkspaceChangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ResetWorkspaceChangesRequest)`  
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
`[ResetWorkspaceChangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ResetWorkspaceChangesResponse)` | The response received from the server.  
  
### ResetWorkspaceChangesAsync(ResetWorkspaceChangesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ResetWorkspaceChangesResponse> ResetWorkspaceChangesAsync(ResetWorkspaceChangesRequest request, CallOptions options)

Performs a Git reset for uncommitted files in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResetWorkspaceChangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ResetWorkspaceChangesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ResetWorkspaceChangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ResetWorkspaceChangesResponse)` | The call object.  
  
### ResetWorkspaceChangesAsync(ResetWorkspaceChangesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ResetWorkspaceChangesResponse> ResetWorkspaceChangesAsync(ResetWorkspaceChangesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Performs a Git reset for uncommitted files in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResetWorkspaceChangesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ResetWorkspaceChangesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ResetWorkspaceChangesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ResetWorkspaceChangesResponse)` | The call object.  
  
### SearchFiles(SearchFilesRequest, CallOptions)
    
    
    public virtual SearchFilesResponse SearchFiles(SearchFilesRequest request, CallOptions options)

Finds the contents of a given Workspace directory by filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchFilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SearchFilesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchFilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SearchFilesResponse)` | The response received from the server.  
  
### SearchFiles(SearchFilesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual SearchFilesResponse SearchFiles(SearchFilesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Finds the contents of a given Workspace directory by filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchFilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SearchFilesRequest)`  
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
`[SearchFilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SearchFilesResponse)` | The response received from the server.  
  
### SearchFilesAsync(SearchFilesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<SearchFilesResponse> SearchFilesAsync(SearchFilesRequest request, CallOptions options)

Finds the contents of a given Workspace directory by filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchFilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SearchFilesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SearchFilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SearchFilesResponse)` | The call object.  
  
### SearchFilesAsync(SearchFilesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<SearchFilesResponse> SearchFilesAsync(SearchFilesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Finds the contents of a given Workspace directory by filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchFilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SearchFilesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SearchFilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SearchFilesResponse)` | The call object.  
  
### SearchTeamFolders(SearchTeamFoldersRequest, CallOptions)
    
    
    public virtual SearchTeamFoldersResponse SearchTeamFolders(SearchTeamFoldersRequest request, CallOptions options)

Returns all TeamFolders in a given location that the caller has access to and match the provided filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchTeamFoldersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SearchTeamFoldersRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchTeamFoldersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SearchTeamFoldersResponse)` | The response received from the server.  
  
### SearchTeamFolders(SearchTeamFoldersRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual SearchTeamFoldersResponse SearchTeamFolders(SearchTeamFoldersRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns all TeamFolders in a given location that the caller has access to and match the provided filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchTeamFoldersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SearchTeamFoldersRequest)`  
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
`[SearchTeamFoldersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SearchTeamFoldersResponse)` | The response received from the server.  
  
### SearchTeamFoldersAsync(SearchTeamFoldersRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<SearchTeamFoldersResponse> SearchTeamFoldersAsync(SearchTeamFoldersRequest request, CallOptions options)

Returns all TeamFolders in a given location that the caller has access to and match the provided filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchTeamFoldersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SearchTeamFoldersRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SearchTeamFoldersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SearchTeamFoldersResponse)` | The call object.  
  
### SearchTeamFoldersAsync(SearchTeamFoldersRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<SearchTeamFoldersResponse> SearchTeamFoldersAsync(SearchTeamFoldersRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns all TeamFolders in a given location that the caller has access to and match the provided filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchTeamFoldersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SearchTeamFoldersRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SearchTeamFoldersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SearchTeamFoldersResponse)` | The call object.  
  
### SetIamPolicy(SetIamPolicyRequest, CallOptions)
    
    
    public virtual Policy SetIamPolicy(SetIamPolicyRequest request, CallOptions options)

Sets the access control policy on the specified resource. Replaces any existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The response received from the server.  
  
### SetIamPolicy(SetIamPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Policy SetIamPolicy(SetIamPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Sets the access control policy on the specified resource. Replaces any existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)`  
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
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The response received from the server.  
  
### SetIamPolicyAsync(SetIamPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Policy> SetIamPolicyAsync(SetIamPolicyRequest request, CallOptions options)

Sets the access control policy on the specified resource. Replaces any existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The call object.  
  
### SetIamPolicyAsync(SetIamPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Policy> SetIamPolicyAsync(SetIamPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Sets the access control policy on the specified resource. Replaces any existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The call object.  
  
### SyncWorkspaceRefs(SyncWorkspaceRefsRequest, CallOptions)
    
    
    public virtual SyncWorkspaceRefsResponse SyncWorkspaceRefs(SyncWorkspaceRefsRequest request, CallOptions options)

Syncs the refs of a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SyncWorkspaceRefsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SyncWorkspaceRefsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[SyncWorkspaceRefsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SyncWorkspaceRefsResponse)` | The response received from the server.  
  
### SyncWorkspaceRefs(SyncWorkspaceRefsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual SyncWorkspaceRefsResponse SyncWorkspaceRefs(SyncWorkspaceRefsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Syncs the refs of a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SyncWorkspaceRefsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SyncWorkspaceRefsRequest)`  
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
`[SyncWorkspaceRefsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SyncWorkspaceRefsResponse)` | The response received from the server.  
  
### SyncWorkspaceRefsAsync(SyncWorkspaceRefsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<SyncWorkspaceRefsResponse> SyncWorkspaceRefsAsync(SyncWorkspaceRefsRequest request, CallOptions options)

Syncs the refs of a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SyncWorkspaceRefsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SyncWorkspaceRefsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SyncWorkspaceRefsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SyncWorkspaceRefsResponse)` | The call object.  
  
### SyncWorkspaceRefsAsync(SyncWorkspaceRefsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<SyncWorkspaceRefsResponse> SyncWorkspaceRefsAsync(SyncWorkspaceRefsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Syncs the refs of a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SyncWorkspaceRefsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SyncWorkspaceRefsRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SyncWorkspaceRefsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.SyncWorkspaceRefsResponse)` | The call object.  
  
### TestIamPermissions(TestIamPermissionsRequest, CallOptions)
    
    
    public virtual TestIamPermissionsResponse TestIamPermissions(TestIamPermissionsRequest request, CallOptions options)

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | The response received from the server.  
  
### TestIamPermissions(TestIamPermissionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual TestIamPermissionsResponse TestIamPermissions(TestIamPermissionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html)`  
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
`[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | The response received from the server.  
  
### TestIamPermissionsAsync(TestIamPermissionsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<TestIamPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsRequest request, CallOptions options)

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | The call object.  
  
### TestIamPermissionsAsync(TestIamPermissionsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<TestIamPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | The call object.  
  
### UpdateConfig(UpdateConfigRequest, CallOptions)
    
    
    public virtual Config UpdateConfig(UpdateConfigRequest request, CallOptions options)

Update default config for a given project and location.

**Note:** _This method does not fully implement[AIP/134](https://google.aip.dev/134). The wildcard entry (*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields._

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Config](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Config)` | The response received from the server.  
  
### UpdateConfig(UpdateConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Config UpdateConfig(UpdateConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Update default config for a given project and location.

**Note:** _This method does not fully implement[AIP/134](https://google.aip.dev/134). The wildcard entry (*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields._

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateConfigRequest)`  
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
`[Config](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Config)` | The response received from the server.  
  
### UpdateConfigAsync(UpdateConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Config> UpdateConfigAsync(UpdateConfigRequest request, CallOptions options)

Update default config for a given project and location.

**Note:** _This method does not fully implement[AIP/134](https://google.aip.dev/134). The wildcard entry (*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields._

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Config](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Config)` | The call object.  
  
### UpdateConfigAsync(UpdateConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Config> UpdateConfigAsync(UpdateConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Update default config for a given project and location.

**Note:** _This method does not fully implement[AIP/134](https://google.aip.dev/134). The wildcard entry (*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields._

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateConfigRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Config](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Config)` | The call object.  
  
### UpdateFolder(UpdateFolderRequest, CallOptions)
    
    
    public virtual Folder UpdateFolder(UpdateFolderRequest request, CallOptions options)

Updates a single Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateFolderRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Folder)` | The response received from the server.  
  
### UpdateFolder(UpdateFolderRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Folder UpdateFolder(UpdateFolderRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a single Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateFolderRequest)`  
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
`[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Folder)` | The response received from the server.  
  
### UpdateFolderAsync(UpdateFolderRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Folder> UpdateFolderAsync(UpdateFolderRequest request, CallOptions options)

Updates a single Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateFolderRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Folder)` | The call object.  
  
### UpdateFolderAsync(UpdateFolderRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Folder> UpdateFolderAsync(UpdateFolderRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a single Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateFolderRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Folder)` | The call object.  
  
### UpdateReleaseConfig(UpdateReleaseConfigRequest, CallOptions)
    
    
    public virtual ReleaseConfig UpdateReleaseConfig(UpdateReleaseConfigRequest request, CallOptions options)

Updates a single ReleaseConfig.

**Note:** _This method does not fully implement[AIP/134](https://google.aip.dev/134). The wildcard entry (*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields._

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateReleaseConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateReleaseConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig)` | The response received from the server.  
  
### UpdateReleaseConfig(UpdateReleaseConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ReleaseConfig UpdateReleaseConfig(UpdateReleaseConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a single ReleaseConfig.

**Note:** _This method does not fully implement[AIP/134](https://google.aip.dev/134). The wildcard entry (*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields._

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateReleaseConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateReleaseConfigRequest)`  
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
`[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig)` | The response received from the server.  
  
### UpdateReleaseConfigAsync(UpdateReleaseConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ReleaseConfig> UpdateReleaseConfigAsync(UpdateReleaseConfigRequest request, CallOptions options)

Updates a single ReleaseConfig.

**Note:** _This method does not fully implement[AIP/134](https://google.aip.dev/134). The wildcard entry (*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields._

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateReleaseConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateReleaseConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig)` | The call object.  
  
### UpdateReleaseConfigAsync(UpdateReleaseConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ReleaseConfig> UpdateReleaseConfigAsync(UpdateReleaseConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a single ReleaseConfig.

**Note:** _This method does not fully implement[AIP/134](https://google.aip.dev/134). The wildcard entry (*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields._

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateReleaseConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateReleaseConfigRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ReleaseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ReleaseConfig)` | The call object.  
  
### UpdateRepository(UpdateRepositoryRequest, CallOptions)
    
    
    public virtual Repository UpdateRepository(UpdateRepositoryRequest request, CallOptions options)

Updates a single Repository.

**Note:** _This method does not fully implement[AIP/134](https://google.aip.dev/134). The wildcard entry (*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields._

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateRepositoryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Repository)` | The response received from the server.  
  
### UpdateRepository(UpdateRepositoryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Repository UpdateRepository(UpdateRepositoryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a single Repository.

**Note:** _This method does not fully implement[AIP/134](https://google.aip.dev/134). The wildcard entry (*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields._

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateRepositoryRequest)`  
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
`[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Repository)` | The response received from the server.  
  
### UpdateRepositoryAsync(UpdateRepositoryRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Repository> UpdateRepositoryAsync(UpdateRepositoryRequest request, CallOptions options)

Updates a single Repository.

**Note:** _This method does not fully implement[AIP/134](https://google.aip.dev/134). The wildcard entry (*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields._

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateRepositoryRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Repository)` | The call object.  
  
### UpdateRepositoryAsync(UpdateRepositoryRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Repository> UpdateRepositoryAsync(UpdateRepositoryRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a single Repository.

**Note:** _This method does not fully implement[AIP/134](https://google.aip.dev/134). The wildcard entry (*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields._

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateRepositoryRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.Repository)` | The call object.  
  
### UpdateTeamFolder(UpdateTeamFolderRequest, CallOptions)
    
    
    public virtual TeamFolder UpdateTeamFolder(UpdateTeamFolderRequest request, CallOptions options)

Updates a single TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTeamFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateTeamFolderRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[TeamFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.TeamFolder)` | The response received from the server.  
  
### UpdateTeamFolder(UpdateTeamFolderRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual TeamFolder UpdateTeamFolder(UpdateTeamFolderRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a single TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTeamFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateTeamFolderRequest)`  
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
`[TeamFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.TeamFolder)` | The response received from the server.  
  
### UpdateTeamFolderAsync(UpdateTeamFolderRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<TeamFolder> UpdateTeamFolderAsync(UpdateTeamFolderRequest request, CallOptions options)

Updates a single TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTeamFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateTeamFolderRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[TeamFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.TeamFolder)` | The call object.  
  
### UpdateTeamFolderAsync(UpdateTeamFolderRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<TeamFolder> UpdateTeamFolderAsync(UpdateTeamFolderRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a single TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTeamFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateTeamFolderRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[TeamFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.TeamFolder)` | The call object.  
  
### UpdateWorkflowConfig(UpdateWorkflowConfigRequest, CallOptions)
    
    
    public virtual WorkflowConfig UpdateWorkflowConfig(UpdateWorkflowConfigRequest request, CallOptions options)

Updates a single WorkflowConfig.

**Note:** _This method does not fully implement[AIP/134](https://google.aip.dev/134). The wildcard entry (*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields._

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateWorkflowConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateWorkflowConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfig)` | The response received from the server.  
  
### UpdateWorkflowConfig(UpdateWorkflowConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual WorkflowConfig UpdateWorkflowConfig(UpdateWorkflowConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a single WorkflowConfig.

**Note:** _This method does not fully implement[AIP/134](https://google.aip.dev/134). The wildcard entry (*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields._

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateWorkflowConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateWorkflowConfigRequest)`  
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
`[WorkflowConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfig)` | The response received from the server.  
  
### UpdateWorkflowConfigAsync(UpdateWorkflowConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<WorkflowConfig> UpdateWorkflowConfigAsync(UpdateWorkflowConfigRequest request, CallOptions options)

Updates a single WorkflowConfig.

**Note:** _This method does not fully implement[AIP/134](https://google.aip.dev/134). The wildcard entry (*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields._

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateWorkflowConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateWorkflowConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[WorkflowConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfig)` | The call object.  
  
### UpdateWorkflowConfigAsync(UpdateWorkflowConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<WorkflowConfig> UpdateWorkflowConfigAsync(UpdateWorkflowConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates a single WorkflowConfig.

**Note:** _This method does not fully implement[AIP/134](https://google.aip.dev/134). The wildcard entry (*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields._

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateWorkflowConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.UpdateWorkflowConfigRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[WorkflowConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfig)` | The call object.  
  
### WriteFile(WriteFileRequest, CallOptions)
    
    
    public virtual WriteFileResponse WriteFile(WriteFileRequest request, CallOptions options)

Writes to a file (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[WriteFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WriteFileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[WriteFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WriteFileResponse)` | The response received from the server.  
  
### WriteFile(WriteFileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual WriteFileResponse WriteFile(WriteFileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Writes to a file (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[WriteFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WriteFileRequest)`  
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
`[WriteFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WriteFileResponse)` | The response received from the server.  
  
### WriteFileAsync(WriteFileRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<WriteFileResponse> WriteFileAsync(WriteFileRequest request, CallOptions options)

Writes to a file (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[WriteFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WriteFileRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[WriteFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WriteFileResponse)` | The call object.  
  
### WriteFileAsync(WriteFileRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<WriteFileResponse> WriteFileAsync(WriteFileRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Writes to a file (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[WriteFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WriteFileRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[WriteFileResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WriteFileResponse)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
