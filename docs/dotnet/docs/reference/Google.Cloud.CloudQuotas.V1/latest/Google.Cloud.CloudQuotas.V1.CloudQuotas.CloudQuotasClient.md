---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotas.CloudQuotasClient
title: Cloud Quotas v1 API - Class CloudQuotas.CloudQuotasClient (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:20.777881+00:00
---

# Cloud Quotas v1 API - Class CloudQuotas.CloudQuotasClient (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotas.CloudQuotasClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Quotas v1 API - Class CloudQuotas.CloudQuotasClient (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0-beta05 
    
    
    public class CloudQuotas.CloudQuotasClient : ClientBase<CloudQuotas.CloudQuotasClient>

Reference documentation and code samples for the Cloud Quotas v1 API class CloudQuotas.CloudQuotasClient.

Client for CloudQuotas

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[CloudQuotas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotas)[CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotas.CloudQuotasClient) > CloudQuotas.CloudQuotasClient

## Inherited Members

[ClientBase<CloudQuotas.CloudQuotasClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

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

### CloudQuotasClient()
    
    
    protected CloudQuotasClient()

Protected parameterless constructor to allow creation of test doubles.

### CloudQuotasClient(CallInvoker)
    
    
    public CloudQuotasClient(CallInvoker callInvoker)

Creates a new client for CloudQuotas that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### CloudQuotasClient(ChannelBase)
    
    
    public CloudQuotasClient(ChannelBase channel)

Creates a new client for CloudQuotas

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### CloudQuotasClient(ClientBaseConfiguration)
    
    
    protected CloudQuotasClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### CreateQuotaPreference(CreateQuotaPreferenceRequest, CallOptions)
    
    
    public virtual QuotaPreference CreateQuotaPreference(CreateQuotaPreferenceRequest request, CallOptions options)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CreateQuotaPreferenceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The response received from the server.  
  
### CreateQuotaPreference(CreateQuotaPreferenceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual QuotaPreference CreateQuotaPreference(CreateQuotaPreferenceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CreateQuotaPreferenceRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The response received from the server.  
  
### CreateQuotaPreferenceAsync(CreateQuotaPreferenceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<QuotaPreference> CreateQuotaPreferenceAsync(CreateQuotaPreferenceRequest request, CallOptions options)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CreateQuotaPreferenceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The call object.  
  
### CreateQuotaPreferenceAsync(CreateQuotaPreferenceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<QuotaPreference> CreateQuotaPreferenceAsync(CreateQuotaPreferenceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CreateQuotaPreferenceRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The call object.  
  
### GetQuotaInfo(GetQuotaInfoRequest, CallOptions)
    
    
    public virtual QuotaInfo GetQuotaInfo(GetQuotaInfoRequest request, CallOptions options)

Retrieve the QuotaInfo of a quota for a project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaInfoRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)` | The response received from the server.  
  
### GetQuotaInfo(GetQuotaInfoRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual QuotaInfo GetQuotaInfo(GetQuotaInfoRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieve the QuotaInfo of a quota for a project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaInfoRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)` | The response received from the server.  
  
### GetQuotaInfoAsync(GetQuotaInfoRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<QuotaInfo> GetQuotaInfoAsync(GetQuotaInfoRequest request, CallOptions options)

Retrieve the QuotaInfo of a quota for a project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaInfoRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)` | The call object.  
  
### GetQuotaInfoAsync(GetQuotaInfoRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<QuotaInfo> GetQuotaInfoAsync(GetQuotaInfoRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieve the QuotaInfo of a quota for a project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaInfoRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)` | The call object.  
  
### GetQuotaPreference(GetQuotaPreferenceRequest, CallOptions)
    
    
    public virtual QuotaPreference GetQuotaPreference(GetQuotaPreferenceRequest request, CallOptions options)

Gets details of a single QuotaPreference.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaPreferenceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The response received from the server.  
  
### GetQuotaPreference(GetQuotaPreferenceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual QuotaPreference GetQuotaPreference(GetQuotaPreferenceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single QuotaPreference.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaPreferenceRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The response received from the server.  
  
### GetQuotaPreferenceAsync(GetQuotaPreferenceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<QuotaPreference> GetQuotaPreferenceAsync(GetQuotaPreferenceRequest request, CallOptions options)

Gets details of a single QuotaPreference.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaPreferenceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The call object.  
  
### GetQuotaPreferenceAsync(GetQuotaPreferenceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<QuotaPreference> GetQuotaPreferenceAsync(GetQuotaPreferenceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets details of a single QuotaPreference.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaPreferenceRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The call object.  
  
### ListQuotaInfos(ListQuotaInfosRequest, CallOptions)
    
    
    public virtual ListQuotaInfosResponse ListQuotaInfos(ListQuotaInfosRequest request, CallOptions options)

Lists QuotaInfos of all quotas for a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQuotaInfosRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListQuotaInfosResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse)` | The response received from the server.  
  
### ListQuotaInfos(ListQuotaInfosRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListQuotaInfosResponse ListQuotaInfos(ListQuotaInfosRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists QuotaInfos of all quotas for a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQuotaInfosRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListQuotaInfosResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse)` | The response received from the server.  
  
### ListQuotaInfosAsync(ListQuotaInfosRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListQuotaInfosResponse> ListQuotaInfosAsync(ListQuotaInfosRequest request, CallOptions options)

Lists QuotaInfos of all quotas for a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQuotaInfosRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListQuotaInfosResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse)` | The call object.  
  
### ListQuotaInfosAsync(ListQuotaInfosRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListQuotaInfosResponse> ListQuotaInfosAsync(ListQuotaInfosRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists QuotaInfos of all quotas for a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQuotaInfosRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListQuotaInfosResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse)` | The call object.  
  
### ListQuotaPreferences(ListQuotaPreferencesRequest, CallOptions)
    
    
    public virtual ListQuotaPreferencesResponse ListQuotaPreferences(ListQuotaPreferencesRequest request, CallOptions options)

Lists QuotaPreferences in a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQuotaPreferencesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListQuotaPreferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse)` | The response received from the server.  
  
### ListQuotaPreferences(ListQuotaPreferencesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ListQuotaPreferencesResponse ListQuotaPreferences(ListQuotaPreferencesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists QuotaPreferences in a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQuotaPreferencesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ListQuotaPreferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse)` | The response received from the server.  
  
### ListQuotaPreferencesAsync(ListQuotaPreferencesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ListQuotaPreferencesResponse> ListQuotaPreferencesAsync(ListQuotaPreferencesRequest request, CallOptions options)

Lists QuotaPreferences in a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQuotaPreferencesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListQuotaPreferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse)` | The call object.  
  
### ListQuotaPreferencesAsync(ListQuotaPreferencesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ListQuotaPreferencesResponse> ListQuotaPreferencesAsync(ListQuotaPreferencesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists QuotaPreferences in a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQuotaPreferencesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ListQuotaPreferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override CloudQuotas.CloudQuotasClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudQuotas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotas)[CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotas.CloudQuotasClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.CloudQuotas.V1.CloudQuotas.CloudQuotasClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### UpdateQuotaPreference(UpdateQuotaPreferenceRequest, CallOptions)
    
    
    public virtual QuotaPreference UpdateQuotaPreference(UpdateQuotaPreferenceRequest request, CallOptions options)

Updates the parameters of a single QuotaPreference. It can updates the config in any states, not just the ones pending approval.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaPreferenceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The response received from the server.  
  
### UpdateQuotaPreference(UpdateQuotaPreferenceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual QuotaPreference UpdateQuotaPreference(UpdateQuotaPreferenceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single QuotaPreference. It can updates the config in any states, not just the ones pending approval.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaPreferenceRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The response received from the server.  
  
### UpdateQuotaPreferenceAsync(UpdateQuotaPreferenceRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<QuotaPreference> UpdateQuotaPreferenceAsync(UpdateQuotaPreferenceRequest request, CallOptions options)

Updates the parameters of a single QuotaPreference. It can updates the config in any states, not just the ones pending approval.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaPreferenceRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The call object.  
  
### UpdateQuotaPreferenceAsync(UpdateQuotaPreferenceRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<QuotaPreference> UpdateQuotaPreferenceAsync(UpdateQuotaPreferenceRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the parameters of a single QuotaPreference. It can updates the config in any states, not just the ones pending approval.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaPreferenceRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
