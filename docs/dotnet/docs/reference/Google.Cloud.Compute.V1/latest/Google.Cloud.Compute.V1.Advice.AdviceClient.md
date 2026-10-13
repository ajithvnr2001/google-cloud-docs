---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Advice.AdviceClient
title: Compute Engine v1 API - Class Advice.AdviceClient (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:25:24.171790+00:00
---

# Compute Engine v1 API - Class Advice.AdviceClient (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Advice.AdviceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class Advice.AdviceClient (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public class Advice.AdviceClient : ClientBase<Advice.AdviceClient>

Reference documentation and code samples for the Compute Engine v1 API class Advice.AdviceClient.

Client for Advice

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[Advice](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Advice)[AdviceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Advice.AdviceClient) > Advice.AdviceClient

## Inherited Members

[ClientBase<Advice.AdviceClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

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

### AdviceClient()
    
    
    protected AdviceClient()

Protected parameterless constructor to allow creation of test doubles.

### AdviceClient(CallInvoker)
    
    
    public AdviceClient(CallInvoker callInvoker)

Creates a new client for Advice that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### AdviceClient(ChannelBase)
    
    
    public AdviceClient(ChannelBase channel)

Creates a new client for Advice

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### AdviceClient(ClientBaseConfiguration)
    
    
    protected AdviceClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### CalendarMode(CalendarModeAdviceRpcRequest, CallOptions)
    
    
    public virtual CalendarModeAdviceResponse CalendarMode(CalendarModeAdviceRpcRequest request, CallOptions options)

Advise how, where and when to create the requested amount of instances with specified accelerators, within the specified time and location limits. The method recommends creating future reservations for the requested resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CalendarModeAdviceRpcRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CalendarModeAdviceRpcRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[CalendarModeAdviceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CalendarModeAdviceResponse)` | The response received from the server.  
  
### CalendarMode(CalendarModeAdviceRpcRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual CalendarModeAdviceResponse CalendarMode(CalendarModeAdviceRpcRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Advise how, where and when to create the requested amount of instances with specified accelerators, within the specified time and location limits. The method recommends creating future reservations for the requested resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CalendarModeAdviceRpcRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CalendarModeAdviceRpcRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[CalendarModeAdviceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CalendarModeAdviceResponse)` | The response received from the server.  
  
### CalendarModeAsync(CalendarModeAdviceRpcRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<CalendarModeAdviceResponse> CalendarModeAsync(CalendarModeAdviceRpcRequest request, CallOptions options)

Advise how, where and when to create the requested amount of instances with specified accelerators, within the specified time and location limits. The method recommends creating future reservations for the requested resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CalendarModeAdviceRpcRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CalendarModeAdviceRpcRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CalendarModeAdviceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CalendarModeAdviceResponse)` | The call object.  
  
### CalendarModeAsync(CalendarModeAdviceRpcRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<CalendarModeAdviceResponse> CalendarModeAsync(CalendarModeAdviceRpcRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Advise how, where and when to create the requested amount of instances with specified accelerators, within the specified time and location limits. The method recommends creating future reservations for the requested resources.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CalendarModeAdviceRpcRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CalendarModeAdviceRpcRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CalendarModeAdviceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CalendarModeAdviceResponse)` | The call object.  
  
### Capacity(CapacityAdviceRpcRequest, CallOptions)
    
    
    public virtual CapacityAdviceResponse Capacity(CapacityAdviceRpcRequest request, CallOptions options)

Advice on making real-time decisions (such as choosing zone or machine types) during deployment to maximize your chances of obtaining capacity.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CapacityAdviceRpcRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityAdviceRpcRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[CapacityAdviceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityAdviceResponse)` | The response received from the server.  
  
### Capacity(CapacityAdviceRpcRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual CapacityAdviceResponse Capacity(CapacityAdviceRpcRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Advice on making real-time decisions (such as choosing zone or machine types) during deployment to maximize your chances of obtaining capacity.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CapacityAdviceRpcRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityAdviceRpcRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[CapacityAdviceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityAdviceResponse)` | The response received from the server.  
  
### CapacityAsync(CapacityAdviceRpcRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<CapacityAdviceResponse> CapacityAsync(CapacityAdviceRpcRequest request, CallOptions options)

Advice on making real-time decisions (such as choosing zone or machine types) during deployment to maximize your chances of obtaining capacity.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CapacityAdviceRpcRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityAdviceRpcRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CapacityAdviceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityAdviceResponse)` | The call object.  
  
### CapacityAsync(CapacityAdviceRpcRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<CapacityAdviceResponse> CapacityAsync(CapacityAdviceRpcRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Advice on making real-time decisions (such as choosing zone or machine types) during deployment to maximize your chances of obtaining capacity.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CapacityAdviceRpcRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityAdviceRpcRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CapacityAdviceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityAdviceResponse)` | The call object.  
  
### CapacityHistory(CapacityHistoryAdviceRequest, CallOptions)
    
    
    public virtual CapacityHistoryResponse CapacityHistory(CapacityHistoryAdviceRequest request, CallOptions options)

Gets the capacity history.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CapacityHistoryAdviceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityHistoryAdviceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[CapacityHistoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityHistoryResponse)` | The response received from the server.  
  
### CapacityHistory(CapacityHistoryAdviceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual CapacityHistoryResponse CapacityHistory(CapacityHistoryAdviceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the capacity history.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CapacityHistoryAdviceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityHistoryAdviceRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[CapacityHistoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityHistoryResponse)` | The response received from the server.  
  
### CapacityHistoryAsync(CapacityHistoryAdviceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<CapacityHistoryResponse> CapacityHistoryAsync(CapacityHistoryAdviceRequest request, CallOptions options)

Gets the capacity history.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CapacityHistoryAdviceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityHistoryAdviceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CapacityHistoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityHistoryResponse)` | The call object.  
  
### CapacityHistoryAsync(CapacityHistoryAdviceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<CapacityHistoryResponse> CapacityHistoryAsync(CapacityHistoryAdviceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the capacity history.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CapacityHistoryAdviceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityHistoryAdviceRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[CapacityHistoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CapacityHistoryResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override Advice.AdviceClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Advice](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Advice)[AdviceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Advice.AdviceClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Compute.V1.Advice.AdviceClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
