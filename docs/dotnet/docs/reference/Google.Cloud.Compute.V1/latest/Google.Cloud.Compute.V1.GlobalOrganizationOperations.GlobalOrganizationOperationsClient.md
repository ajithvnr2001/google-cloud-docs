---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalOrganizationOperations.GlobalOrganizationOperationsClient
title: Compute Engine v1 API - Class GlobalOrganizationOperations.GlobalOrganizationOperationsClient (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:13:41.338145+00:00
---

# Compute Engine v1 API - Class GlobalOrganizationOperations.GlobalOrganizationOperationsClient (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalOrganizationOperations.GlobalOrganizationOperationsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class GlobalOrganizationOperations.GlobalOrganizationOperationsClient (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public class GlobalOrganizationOperations.GlobalOrganizationOperationsClient : ClientBase<GlobalOrganizationOperations.GlobalOrganizationOperationsClient>

Reference documentation and code samples for the Compute Engine v1 API class GlobalOrganizationOperations.GlobalOrganizationOperationsClient.

Client for GlobalOrganizationOperations

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[GlobalOrganizationOperations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalOrganizationOperations)[GlobalOrganizationOperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalOrganizationOperations.GlobalOrganizationOperationsClient) > GlobalOrganizationOperations.GlobalOrganizationOperationsClient

## Inherited Members

[ClientBase<GlobalOrganizationOperations.GlobalOrganizationOperationsClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

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

### GlobalOrganizationOperationsClient()
    
    
    protected GlobalOrganizationOperationsClient()

Protected parameterless constructor to allow creation of test doubles.

### GlobalOrganizationOperationsClient(CallInvoker)
    
    
    public GlobalOrganizationOperationsClient(CallInvoker callInvoker)

Creates a new client for GlobalOrganizationOperations that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### GlobalOrganizationOperationsClient(ChannelBase)
    
    
    public GlobalOrganizationOperationsClient(ChannelBase channel)

Creates a new client for GlobalOrganizationOperations

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### GlobalOrganizationOperationsClient(ClientBaseConfiguration)
    
    
    protected GlobalOrganizationOperationsClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### Delete(DeleteGlobalOrganizationOperationRequest, CallOptions)
    
    
    public virtual DeleteGlobalOrganizationOperationResponse Delete(DeleteGlobalOrganizationOperationRequest request, CallOptions options)

Deletes the specified Operations resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGlobalOrganizationOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteGlobalOrganizationOperationRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DeleteGlobalOrganizationOperationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteGlobalOrganizationOperationResponse)` | The response received from the server.  
  
### Delete(DeleteGlobalOrganizationOperationRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DeleteGlobalOrganizationOperationResponse Delete(DeleteGlobalOrganizationOperationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified Operations resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGlobalOrganizationOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteGlobalOrganizationOperationRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[DeleteGlobalOrganizationOperationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteGlobalOrganizationOperationResponse)` | The response received from the server.  
  
### DeleteAsync(DeleteGlobalOrganizationOperationRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DeleteGlobalOrganizationOperationResponse> DeleteAsync(DeleteGlobalOrganizationOperationRequest request, CallOptions options)

Deletes the specified Operations resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGlobalOrganizationOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteGlobalOrganizationOperationRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DeleteGlobalOrganizationOperationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteGlobalOrganizationOperationResponse)` | The call object.  
  
### DeleteAsync(DeleteGlobalOrganizationOperationRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DeleteGlobalOrganizationOperationResponse> DeleteAsync(DeleteGlobalOrganizationOperationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified Operations resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGlobalOrganizationOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteGlobalOrganizationOperationRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DeleteGlobalOrganizationOperationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteGlobalOrganizationOperationResponse)` | The call object.  
  
### Get(GetGlobalOrganizationOperationRequest, CallOptions)
    
    
    public virtual Operation Get(GetGlobalOrganizationOperationRequest request, CallOptions options)

Retrieves the specified Operations resource. Gets a list of operations by making a `list()` request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGlobalOrganizationOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetGlobalOrganizationOperationRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### Get(GetGlobalOrganizationOperationRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation Get(GetGlobalOrganizationOperationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieves the specified Operations resource. Gets a list of operations by making a `list()` request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGlobalOrganizationOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetGlobalOrganizationOperationRequest)`  
The request to send to the server.  
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
  
### GetAsync(GetGlobalOrganizationOperationRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> GetAsync(GetGlobalOrganizationOperationRequest request, CallOptions options)

Retrieves the specified Operations resource. Gets a list of operations by making a `list()` request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGlobalOrganizationOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetGlobalOrganizationOperationRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### GetAsync(GetGlobalOrganizationOperationRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> GetAsync(GetGlobalOrganizationOperationRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieves the specified Operations resource. Gets a list of operations by making a `list()` request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGlobalOrganizationOperationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetGlobalOrganizationOperationRequest)`  
The request to send to the server.  
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
  
### List(ListGlobalOrganizationOperationsRequest, CallOptions)
    
    
    public virtual OperationList List(ListGlobalOrganizationOperationsRequest request, CallOptions options)

Retrieves a list of Operation resources contained within the specified organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGlobalOrganizationOperationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListGlobalOrganizationOperationsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.OperationList)` | The response received from the server.  
  
### List(ListGlobalOrganizationOperationsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual OperationList List(ListGlobalOrganizationOperationsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieves a list of Operation resources contained within the specified organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGlobalOrganizationOperationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListGlobalOrganizationOperationsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.OperationList)` | The response received from the server.  
  
### ListAsync(ListGlobalOrganizationOperationsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<OperationList> ListAsync(ListGlobalOrganizationOperationsRequest request, CallOptions options)

Retrieves a list of Operation resources contained within the specified organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGlobalOrganizationOperationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListGlobalOrganizationOperationsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[OperationList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.OperationList)` | The call object.  
  
### ListAsync(ListGlobalOrganizationOperationsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<OperationList> ListAsync(ListGlobalOrganizationOperationsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieves a list of Operation resources contained within the specified organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGlobalOrganizationOperationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListGlobalOrganizationOperationsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[OperationList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.OperationList)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override GlobalOrganizationOperations.GlobalOrganizationOperationsClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GlobalOrganizationOperations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalOrganizationOperations)[GlobalOrganizationOperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalOrganizationOperations.GlobalOrganizationOperationsClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Compute.V1.GlobalOrganizationOperations.GlobalOrganizationOperationsClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
