---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypes.AcceleratorTypesClient
title: Compute Engine v1 API - Class AcceleratorTypes.AcceleratorTypesClient (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:24:45.676610+00:00
---

# Compute Engine v1 API - Class AcceleratorTypes.AcceleratorTypesClient (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypes.AcceleratorTypesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class AcceleratorTypes.AcceleratorTypesClient (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public class AcceleratorTypes.AcceleratorTypesClient : ClientBase<AcceleratorTypes.AcceleratorTypesClient>

Reference documentation and code samples for the Compute Engine v1 API class AcceleratorTypes.AcceleratorTypesClient.

Client for AcceleratorTypes

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[AcceleratorTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypes)[AcceleratorTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypes.AcceleratorTypesClient) > AcceleratorTypes.AcceleratorTypesClient

## Inherited Members

[ClientBase<AcceleratorTypes.AcceleratorTypesClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

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

### AcceleratorTypesClient()
    
    
    protected AcceleratorTypesClient()

Protected parameterless constructor to allow creation of test doubles.

### AcceleratorTypesClient(CallInvoker)
    
    
    public AcceleratorTypesClient(CallInvoker callInvoker)

Creates a new client for AcceleratorTypes that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### AcceleratorTypesClient(ChannelBase)
    
    
    public AcceleratorTypesClient(ChannelBase channel)

Creates a new client for AcceleratorTypes

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### AcceleratorTypesClient(ClientBaseConfiguration)
    
    
    protected AcceleratorTypesClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### AggregatedList(AggregatedListAcceleratorTypesRequest, CallOptions)
    
    
    public virtual AcceleratorTypeAggregatedList AggregatedList(AggregatedListAcceleratorTypesRequest request, CallOptions options)

Retrieves an aggregated list of accelerator types.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregatedListAcceleratorTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AggregatedListAcceleratorTypesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AcceleratorTypeAggregatedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypeAggregatedList)` | The response received from the server.  
  
### AggregatedList(AggregatedListAcceleratorTypesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AcceleratorTypeAggregatedList AggregatedList(AggregatedListAcceleratorTypesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieves an aggregated list of accelerator types.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregatedListAcceleratorTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AggregatedListAcceleratorTypesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AcceleratorTypeAggregatedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypeAggregatedList)` | The response received from the server.  
  
### AggregatedListAsync(AggregatedListAcceleratorTypesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<AcceleratorTypeAggregatedList> AggregatedListAsync(AggregatedListAcceleratorTypesRequest request, CallOptions options)

Retrieves an aggregated list of accelerator types.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregatedListAcceleratorTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AggregatedListAcceleratorTypesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AcceleratorTypeAggregatedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypeAggregatedList)` | The call object.  
  
### AggregatedListAsync(AggregatedListAcceleratorTypesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<AcceleratorTypeAggregatedList> AggregatedListAsync(AggregatedListAcceleratorTypesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieves an aggregated list of accelerator types.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregatedListAcceleratorTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AggregatedListAcceleratorTypesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AcceleratorTypeAggregatedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypeAggregatedList)` | The call object.  
  
### Get(GetAcceleratorTypeRequest, CallOptions)
    
    
    public virtual AcceleratorType Get(GetAcceleratorTypeRequest request, CallOptions options)

Returns the specified accelerator type.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAcceleratorTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetAcceleratorTypeRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType)` | The response received from the server.  
  
### Get(GetAcceleratorTypeRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AcceleratorType Get(GetAcceleratorTypeRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the specified accelerator type.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAcceleratorTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetAcceleratorTypeRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType)` | The response received from the server.  
  
### GetAsync(GetAcceleratorTypeRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<AcceleratorType> GetAsync(GetAcceleratorTypeRequest request, CallOptions options)

Returns the specified accelerator type.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAcceleratorTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetAcceleratorTypeRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType)` | The call object.  
  
### GetAsync(GetAcceleratorTypeRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<AcceleratorType> GetAsync(GetAcceleratorTypeRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the specified accelerator type.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAcceleratorTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetAcceleratorTypeRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AcceleratorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorType)` | The call object.  
  
### List(ListAcceleratorTypesRequest, CallOptions)
    
    
    public virtual AcceleratorTypeList List(ListAcceleratorTypesRequest request, CallOptions options)

Retrieves a list of accelerator types that are available to the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAcceleratorTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListAcceleratorTypesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AcceleratorTypeList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypeList)` | The response received from the server.  
  
### List(ListAcceleratorTypesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AcceleratorTypeList List(ListAcceleratorTypesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieves a list of accelerator types that are available to the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAcceleratorTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListAcceleratorTypesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AcceleratorTypeList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypeList)` | The response received from the server.  
  
### ListAsync(ListAcceleratorTypesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<AcceleratorTypeList> ListAsync(ListAcceleratorTypesRequest request, CallOptions options)

Retrieves a list of accelerator types that are available to the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAcceleratorTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListAcceleratorTypesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AcceleratorTypeList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypeList)` | The call object.  
  
### ListAsync(ListAcceleratorTypesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<AcceleratorTypeList> ListAsync(ListAcceleratorTypesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieves a list of accelerator types that are available to the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAcceleratorTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListAcceleratorTypesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AcceleratorTypeList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypeList)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override AcceleratorTypes.AcceleratorTypesClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AcceleratorTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypes)[AcceleratorTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypes.AcceleratorTypesClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Compute.V1.AcceleratorTypes.AcceleratorTypesClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
