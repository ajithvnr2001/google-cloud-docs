---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseService.CaseServiceClient
title: Google Cloud Support v2 API - Class CaseService.CaseServiceClient (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:52.857464+00:00
---

# Google Cloud Support v2 API - Class CaseService.CaseServiceClient (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseService.CaseServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Support v2 API - Class CaseService.CaseServiceClient (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public class CaseService.CaseServiceClient : ClientBase<CaseService.CaseServiceClient>

Reference documentation and code samples for the Google Cloud Support v2 API class CaseService.CaseServiceClient.

Client for CaseService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[CaseService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseService)[CaseServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseService.CaseServiceClient) > CaseService.CaseServiceClient

## Inherited Members

[ClientBase<CaseService.CaseServiceClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Support.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2)

## Assembly

Google.Cloud.Support.V2.dll

## Constructors 

### CaseServiceClient()
    
    
    protected CaseServiceClient()

Protected parameterless constructor to allow creation of test doubles.

### CaseServiceClient(CallInvoker)
    
    
    public CaseServiceClient(CallInvoker callInvoker)

Creates a new client for CaseService that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### CaseServiceClient(ChannelBase)
    
    
    public CaseServiceClient(ChannelBase channel)

Creates a new client for CaseService

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### CaseServiceClient(ClientBaseConfiguration)
    
    
    protected CaseServiceClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### CloseCase(CloseCaseRequest, CallOptions)
    
    
    public virtual Case CloseCase(CloseCaseRequest request, CallOptions options)

Close a case.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CloseCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CloseCaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The response received from the server.  
  
### CloseCase(CloseCaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Case CloseCase(CloseCaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Close a case.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CloseCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CloseCaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The response received from the server.  
  
### CloseCaseAsync(CloseCaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Case> CloseCaseAsync(CloseCaseRequest request, CallOptions options)

Close a case.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CloseCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CloseCaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The call object.  
  
### CloseCaseAsync(CloseCaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Case> CloseCaseAsync(CloseCaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Close a case.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CloseCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CloseCaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The call object.  
  
### CreateCase(CreateCaseRequest, CallOptions)
    
    
    public virtual Case CreateCase(CreateCaseRequest request, CallOptions options)

Create a new case and associate it with a parent.

It must have the following fields set: `display_name`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CreateCaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The response received from the server.  
  
### CreateCase(CreateCaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Case CreateCase(CreateCaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Create a new case and associate it with a parent.

It must have the following fields set: `display_name`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CreateCaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The response received from the server.  
  
### CreateCaseAsync(CreateCaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Case> CreateCaseAsync(CreateCaseRequest request, CallOptions options)

Create a new case and associate it with a parent.

It must have the following fields set: `display_name`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CreateCaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The call object.  
  
### CreateCaseAsync(CreateCaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Case> CreateCaseAsync(CreateCaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Create a new case and associate it with a parent.

It must have the following fields set: `display_name`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CreateCaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The call object.  
  
### EscalateCase(EscalateCaseRequest, CallOptions)
    
    
    public virtual Case EscalateCase(EscalateCaseRequest request, CallOptions options)

Escalate a case, starting the Google Cloud Support escalation management process.

This operation is only available for some support services. Go to <https://cloud.google.com/support> and look for 'Technical support escalations' in the feature list to find out which ones let you do that.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EscalateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.EscalateCaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The response received from the server.  
  
### EscalateCase(EscalateCaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Case EscalateCase(EscalateCaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Escalate a case, starting the Google Cloud Support escalation management process.

This operation is only available for some support services. Go to <https://cloud.google.com/support> and look for 'Technical support escalations' in the feature list to find out which ones let you do that.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EscalateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.EscalateCaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The response received from the server.  
  
### EscalateCaseAsync(EscalateCaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Case> EscalateCaseAsync(EscalateCaseRequest request, CallOptions options)

Escalate a case, starting the Google Cloud Support escalation management process.

This operation is only available for some support services. Go to <https://cloud.google.com/support> and look for 'Technical support escalations' in the feature list to find out which ones let you do that.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EscalateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.EscalateCaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The call object.  
  
### EscalateCaseAsync(EscalateCaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Case> EscalateCaseAsync(EscalateCaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Escalate a case, starting the Google Cloud Support escalation management process.

This operation is only available for some support services. Go to <https://cloud.google.com/support> and look for 'Technical support escalations' in the feature list to find out which ones let you do that.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EscalateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.EscalateCaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The call object.  
  
### GetCase(GetCaseRequest, CallOptions)
    
    
    public virtual Case GetCase(GetCaseRequest request, CallOptions options)

Retrieve a case.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.GetCaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The response received from the server.  
  
### GetCase(GetCaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Case GetCase(GetCaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieve a case.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.GetCaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The response received from the server.  
  
### GetCaseAsync(GetCaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Case> GetCaseAsync(GetCaseRequest request, CallOptions options)

Retrieve a case.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.GetCaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The call object.  
  
### GetCaseAsync(GetCaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Case> GetCaseAsync(GetCaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieve a case.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.GetCaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The call object.  
  
### ListCases(ListCasesRequest, CallOptions)
    
    
    public virtual ListCasesResponse ListCases(ListCasesRequest request, CallOptions options)

Retrieve all cases under a parent, but not its children.

For example, listing cases under an organization only returns the cases that are directly parented by that organization. To retrieve cases under an organization and its projects, use `cases.search`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.ListCasesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.ListCasesResponse)` | The response received from the server.  
  
### ListCases(ListCasesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListCasesResponse ListCases(ListCasesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieve all cases under a parent, but not its children.

For example, listing cases under an organization only returns the cases that are directly parented by that organization. To retrieve cases under an organization and its projects, use `cases.search`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.ListCasesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.ListCasesResponse)` | The response received from the server.  
  
### ListCasesAsync(ListCasesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListCasesResponse> ListCasesAsync(ListCasesRequest request, CallOptions options)

Retrieve all cases under a parent, but not its children.

For example, listing cases under an organization only returns the cases that are directly parented by that organization. To retrieve cases under an organization and its projects, use `cases.search`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.ListCasesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.ListCasesResponse)` | The call object.  
  
### ListCasesAsync(ListCasesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListCasesResponse> ListCasesAsync(ListCasesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieve all cases under a parent, but not its children.

For example, listing cases under an organization only returns the cases that are directly parented by that organization. To retrieve cases under an organization and its projects, use `cases.search`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.ListCasesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.ListCasesResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override CaseService.CaseServiceClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CaseService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseService)[CaseServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CaseService.CaseServiceClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Support.V2.CaseService.CaseServiceClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### SearchCaseClassifications(SearchCaseClassificationsRequest, CallOptions)
    
    
    public virtual SearchCaseClassificationsResponse SearchCaseClassifications(SearchCaseClassificationsRequest request, CallOptions options)

Retrieve valid classifications to use when creating a support case.

Classifications are hierarchical. Each classification is a string containing all levels of the hierarchy separated by `" > "`. For example, `"Technical Issue > Compute > Compute Engine"`.

Classification IDs returned by this endpoint are valid for at least six months. When a classification is deactivated, this endpoint immediately stops returning it. After six months, `case.create` requests using the classification will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchCaseClassificationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCaseClassificationsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchCaseClassificationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCaseClassificationsResponse)` | The response received from the server.  
  
### SearchCaseClassifications(SearchCaseClassificationsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual SearchCaseClassificationsResponse SearchCaseClassifications(SearchCaseClassificationsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieve valid classifications to use when creating a support case.

Classifications are hierarchical. Each classification is a string containing all levels of the hierarchy separated by `" > "`. For example, `"Technical Issue > Compute > Compute Engine"`.

Classification IDs returned by this endpoint are valid for at least six months. When a classification is deactivated, this endpoint immediately stops returning it. After six months, `case.create` requests using the classification will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchCaseClassificationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCaseClassificationsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchCaseClassificationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCaseClassificationsResponse)` | The response received from the server.  
  
### SearchCaseClassificationsAsync(SearchCaseClassificationsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<SearchCaseClassificationsResponse> SearchCaseClassificationsAsync(SearchCaseClassificationsRequest request, CallOptions options)

Retrieve valid classifications to use when creating a support case.

Classifications are hierarchical. Each classification is a string containing all levels of the hierarchy separated by `" > "`. For example, `"Technical Issue > Compute > Compute Engine"`.

Classification IDs returned by this endpoint are valid for at least six months. When a classification is deactivated, this endpoint immediately stops returning it. After six months, `case.create` requests using the classification will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchCaseClassificationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCaseClassificationsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SearchCaseClassificationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCaseClassificationsResponse)` | The call object.  
  
### SearchCaseClassificationsAsync(SearchCaseClassificationsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<SearchCaseClassificationsResponse> SearchCaseClassificationsAsync(SearchCaseClassificationsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieve valid classifications to use when creating a support case.

Classifications are hierarchical. Each classification is a string containing all levels of the hierarchy separated by `" > "`. For example, `"Technical Issue > Compute > Compute Engine"`.

Classification IDs returned by this endpoint are valid for at least six months. When a classification is deactivated, this endpoint immediately stops returning it. After six months, `case.create` requests using the classification will fail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchCaseClassificationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCaseClassificationsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SearchCaseClassificationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCaseClassificationsResponse)` | The call object.  
  
### SearchCases(SearchCasesRequest, CallOptions)
    
    
    public virtual SearchCasesResponse SearchCases(SearchCasesRequest request, CallOptions options)

Search for cases using a query.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchCasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCasesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCasesResponse)` | The response received from the server.  
  
### SearchCases(SearchCasesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual SearchCasesResponse SearchCases(SearchCasesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Search for cases using a query.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchCasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCasesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCasesResponse)` | The response received from the server.  
  
### SearchCasesAsync(SearchCasesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<SearchCasesResponse> SearchCasesAsync(SearchCasesRequest request, CallOptions options)

Search for cases using a query.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchCasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCasesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SearchCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCasesResponse)` | The call object.  
  
### SearchCasesAsync(SearchCasesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<SearchCasesResponse> SearchCasesAsync(SearchCasesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Search for cases using a query.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchCasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCasesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[SearchCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SearchCasesResponse)` | The call object.  
  
### UpdateCase(UpdateCaseRequest, CallOptions)
    
    
    public virtual Case UpdateCase(UpdateCaseRequest request, CallOptions options)

Update a case. Only some fields can be updated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.UpdateCaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The response received from the server.  
  
### UpdateCase(UpdateCaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Case UpdateCase(UpdateCaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Update a case. Only some fields can be updated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.UpdateCaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The response received from the server.  
  
### UpdateCaseAsync(UpdateCaseRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Case> UpdateCaseAsync(UpdateCaseRequest request, CallOptions options)

Update a case. Only some fields can be updated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.UpdateCaseRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The call object.  
  
### UpdateCaseAsync(UpdateCaseRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Case> UpdateCaseAsync(UpdateCaseRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Update a case. Only some fields can be updated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.UpdateCaseRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
