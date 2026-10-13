---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartService.DashboardChartServiceClient
title: Chronicle v1 API - Class DashboardChartService.DashboardChartServiceClient (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:04.572336+00:00
---

# Chronicle v1 API - Class DashboardChartService.DashboardChartServiceClient (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartService.DashboardChartServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class DashboardChartService.DashboardChartServiceClient (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public class DashboardChartService.DashboardChartServiceClient : ClientBase<DashboardChartService.DashboardChartServiceClient>

Reference documentation and code samples for the Chronicle v1 API class DashboardChartService.DashboardChartServiceClient.

Client for DashboardChartService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[DashboardChartService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartService)[DashboardChartServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartService.DashboardChartServiceClient) > DashboardChartService.DashboardChartServiceClient

## Inherited Members

[ClientBase<DashboardChartService.DashboardChartServiceClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Constructors 

### DashboardChartServiceClient()
    
    
    protected DashboardChartServiceClient()

Protected parameterless constructor to allow creation of test doubles.

### DashboardChartServiceClient(CallInvoker)
    
    
    public DashboardChartServiceClient(CallInvoker callInvoker)

Creates a new client for DashboardChartService that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### DashboardChartServiceClient(ChannelBase)
    
    
    public DashboardChartServiceClient(ChannelBase channel)

Creates a new client for DashboardChartService

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### DashboardChartServiceClient(ClientBaseConfiguration)
    
    
    protected DashboardChartServiceClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### BatchGetDashboardCharts(BatchGetDashboardChartsRequest, CallOptions)
    
    
    public virtual BatchGetDashboardChartsResponse BatchGetDashboardCharts(BatchGetDashboardChartsRequest request, CallOptions options)

Get dashboard charts in batches.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchGetDashboardChartsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BatchGetDashboardChartsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchGetDashboardChartsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BatchGetDashboardChartsResponse)` | The response received from the server.  
  
### BatchGetDashboardCharts(BatchGetDashboardChartsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual BatchGetDashboardChartsResponse BatchGetDashboardCharts(BatchGetDashboardChartsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get dashboard charts in batches.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchGetDashboardChartsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BatchGetDashboardChartsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchGetDashboardChartsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BatchGetDashboardChartsResponse)` | The response received from the server.  
  
### BatchGetDashboardChartsAsync(BatchGetDashboardChartsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<BatchGetDashboardChartsResponse> BatchGetDashboardChartsAsync(BatchGetDashboardChartsRequest request, CallOptions options)

Get dashboard charts in batches.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchGetDashboardChartsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BatchGetDashboardChartsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BatchGetDashboardChartsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BatchGetDashboardChartsResponse)` | The call object.  
  
### BatchGetDashboardChartsAsync(BatchGetDashboardChartsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<BatchGetDashboardChartsResponse> BatchGetDashboardChartsAsync(BatchGetDashboardChartsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get dashboard charts in batches.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchGetDashboardChartsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BatchGetDashboardChartsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BatchGetDashboardChartsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BatchGetDashboardChartsResponse)` | The call object.  
  
### GetDashboardChart(GetDashboardChartRequest, CallOptions)
    
    
    public virtual DashboardChart GetDashboardChart(GetDashboardChartRequest request, CallOptions options)

Get a dashboard chart.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDashboardChartRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDashboardChartRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[DashboardChart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChart)` | The response received from the server.  
  
### GetDashboardChart(GetDashboardChartRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual DashboardChart GetDashboardChart(GetDashboardChartRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get a dashboard chart.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDashboardChartRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDashboardChartRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[DashboardChart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChart)` | The response received from the server.  
  
### GetDashboardChartAsync(GetDashboardChartRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<DashboardChart> GetDashboardChartAsync(GetDashboardChartRequest request, CallOptions options)

Get a dashboard chart.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDashboardChartRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDashboardChartRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DashboardChart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChart)` | The call object.  
  
### GetDashboardChartAsync(GetDashboardChartRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<DashboardChart> GetDashboardChartAsync(GetDashboardChartRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get a dashboard chart.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDashboardChartRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDashboardChartRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[DashboardChart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChart)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override DashboardChartService.DashboardChartServiceClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DashboardChartService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartService)[DashboardChartServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DashboardChartService.DashboardChartServiceClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Chronicle.V1.DashboardChartService.DashboardChartServiceClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
