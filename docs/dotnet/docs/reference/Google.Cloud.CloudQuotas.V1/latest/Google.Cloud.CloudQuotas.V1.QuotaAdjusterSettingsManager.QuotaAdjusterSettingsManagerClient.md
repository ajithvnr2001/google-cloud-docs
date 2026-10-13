---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerClient
title: Cloud Quotas v1 API - Class QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerClient (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:24.385933+00:00
---

# Cloud Quotas v1 API - Class QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerClient (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Quotas v1 API - Class QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerClient (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0-beta05 
    
    
    public class QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerClient : ClientBase<QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerClient>

Reference documentation and code samples for the Cloud Quotas v1 API class QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerClient.

Client for QuotaAdjusterSettingsManager

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[QuotaAdjusterSettingsManager](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManager)[QuotaAdjusterSettingsManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerClient) > QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerClient

## Inherited Members

[ClientBase<QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudQuotas.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1)

## Assembly

Google.Cloud.CloudQuotas.V1.dll

## Constructors 

### QuotaAdjusterSettingsManagerClient()
    
    
    protected QuotaAdjusterSettingsManagerClient()

Protected parameterless constructor to allow creation of test doubles.

### QuotaAdjusterSettingsManagerClient(CallInvoker)
    
    
    public QuotaAdjusterSettingsManagerClient(CallInvoker callInvoker)

Creates a new client for QuotaAdjusterSettingsManager that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### QuotaAdjusterSettingsManagerClient(ChannelBase)
    
    
    public QuotaAdjusterSettingsManagerClient(ChannelBase channel)

Creates a new client for QuotaAdjusterSettingsManager

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### QuotaAdjusterSettingsManagerClient(ClientBaseConfiguration)
    
    
    protected QuotaAdjusterSettingsManagerClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### GetQuotaAdjusterSettings(GetQuotaAdjusterSettingsRequest, CallOptions)
    
    
    public virtual QuotaAdjusterSettings GetQuotaAdjusterSettings(GetQuotaAdjusterSettingsRequest request, CallOptions options)

Gets the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaAdjusterSettingsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | The response received from the server.  
  
### GetQuotaAdjusterSettings(GetQuotaAdjusterSettingsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual QuotaAdjusterSettings GetQuotaAdjusterSettings(GetQuotaAdjusterSettingsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaAdjusterSettingsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | The response received from the server.  
  
### GetQuotaAdjusterSettingsAsync(GetQuotaAdjusterSettingsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<QuotaAdjusterSettings> GetQuotaAdjusterSettingsAsync(GetQuotaAdjusterSettingsRequest request, CallOptions options)

Gets the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaAdjusterSettingsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | The call object.  
  
### GetQuotaAdjusterSettingsAsync(GetQuotaAdjusterSettingsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<QuotaAdjusterSettings> GetQuotaAdjusterSettingsAsync(GetQuotaAdjusterSettingsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaAdjusterSettingsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettingsManager](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManager)[QuotaAdjusterSettingsManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### UpdateQuotaAdjusterSettings(UpdateQuotaAdjusterSettingsRequest, CallOptions)
    
    
    public virtual QuotaAdjusterSettings UpdateQuotaAdjusterSettings(UpdateQuotaAdjusterSettingsRequest request, CallOptions options)

Updates the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaAdjusterSettingsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | The response received from the server.  
  
### UpdateQuotaAdjusterSettings(UpdateQuotaAdjusterSettingsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual QuotaAdjusterSettings UpdateQuotaAdjusterSettings(UpdateQuotaAdjusterSettingsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaAdjusterSettingsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | The response received from the server.  
  
### UpdateQuotaAdjusterSettingsAsync(UpdateQuotaAdjusterSettingsRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<QuotaAdjusterSettings> UpdateQuotaAdjusterSettingsAsync(UpdateQuotaAdjusterSettingsRequest request, CallOptions options)

Updates the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaAdjusterSettingsRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | The call object.  
  
### UpdateQuotaAdjusterSettingsAsync(UpdateQuotaAdjusterSettingsRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<QuotaAdjusterSettings> UpdateQuotaAdjusterSettingsAsync(UpdateQuotaAdjusterSettingsRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaAdjusterSettingsRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
