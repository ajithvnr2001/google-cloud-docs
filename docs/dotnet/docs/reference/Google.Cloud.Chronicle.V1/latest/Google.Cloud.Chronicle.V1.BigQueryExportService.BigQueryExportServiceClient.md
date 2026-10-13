---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportService.BigQueryExportServiceClient
title: Chronicle v1 API - Class BigQueryExportService.BigQueryExportServiceClient (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:41.865684+00:00
---

# Chronicle v1 API - Class BigQueryExportService.BigQueryExportServiceClient (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportService.BigQueryExportServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class BigQueryExportService.BigQueryExportServiceClient (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public class BigQueryExportService.BigQueryExportServiceClient : ClientBase<BigQueryExportService.BigQueryExportServiceClient>

Reference documentation and code samples for the Chronicle v1 API class BigQueryExportService.BigQueryExportServiceClient.

Client for BigQueryExportService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[BigQueryExportService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportService)[BigQueryExportServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportService.BigQueryExportServiceClient) > BigQueryExportService.BigQueryExportServiceClient

## Inherited Members

[ClientBase<BigQueryExportService.BigQueryExportServiceClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

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

### BigQueryExportServiceClient()
    
    
    protected BigQueryExportServiceClient()

Protected parameterless constructor to allow creation of test doubles.

### BigQueryExportServiceClient(CallInvoker)
    
    
    public BigQueryExportServiceClient(CallInvoker callInvoker)

Creates a new client for BigQueryExportService that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### BigQueryExportServiceClient(ChannelBase)
    
    
    public BigQueryExportServiceClient(ChannelBase channel)

Creates a new client for BigQueryExportService

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### BigQueryExportServiceClient(ClientBaseConfiguration)
    
    
    protected BigQueryExportServiceClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### GetBigQueryExport(GetBigQueryExportRequest, CallOptions)
    
    
    public virtual BigQueryExport GetBigQueryExport(GetBigQueryExportRequest request, CallOptions options)

Get the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetBigQueryExportRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The response received from the server.  
  
### GetBigQueryExport(GetBigQueryExportRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual BigQueryExport GetBigQueryExport(GetBigQueryExportRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetBigQueryExportRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The response received from the server.  
  
### GetBigQueryExportAsync(GetBigQueryExportRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<BigQueryExport> GetBigQueryExportAsync(GetBigQueryExportRequest request, CallOptions options)

Get the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetBigQueryExportRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The call object.  
  
### GetBigQueryExportAsync(GetBigQueryExportRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<BigQueryExport> GetBigQueryExportAsync(GetBigQueryExportRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Get the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetBigQueryExportRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override BigQueryExportService.BigQueryExportServiceClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExportService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportService)[BigQueryExportServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExportService.BigQueryExportServiceClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Chronicle.V1.BigQueryExportService.BigQueryExportServiceClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### ProvisionBigQueryExport(ProvisionBigQueryExportRequest, CallOptions)
    
    
    public virtual BigQueryExport ProvisionBigQueryExport(ProvisionBigQueryExportRequest request, CallOptions options)

Provision the BigQuery export for a Chronicle instance. This will create {{gcp_name}} resources like {{storage_name}} buckets, BigQuery datasets and set default export settings for each data source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ProvisionBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ProvisionBigQueryExportRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The response received from the server.  
  
### ProvisionBigQueryExport(ProvisionBigQueryExportRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual BigQueryExport ProvisionBigQueryExport(ProvisionBigQueryExportRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Provision the BigQuery export for a Chronicle instance. This will create {{gcp_name}} resources like {{storage_name}} buckets, BigQuery datasets and set default export settings for each data source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ProvisionBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ProvisionBigQueryExportRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The response received from the server.  
  
### ProvisionBigQueryExportAsync(ProvisionBigQueryExportRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<BigQueryExport> ProvisionBigQueryExportAsync(ProvisionBigQueryExportRequest request, CallOptions options)

Provision the BigQuery export for a Chronicle instance. This will create {{gcp_name}} resources like {{storage_name}} buckets, BigQuery datasets and set default export settings for each data source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ProvisionBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ProvisionBigQueryExportRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The call object.  
  
### ProvisionBigQueryExportAsync(ProvisionBigQueryExportRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<BigQueryExport> ProvisionBigQueryExportAsync(ProvisionBigQueryExportRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Provision the BigQuery export for a Chronicle instance. This will create {{gcp_name}} resources like {{storage_name}} buckets, BigQuery datasets and set default export settings for each data source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ProvisionBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ProvisionBigQueryExportRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The call object.  
  
### UpdateBigQueryExport(UpdateBigQueryExportRequest, CallOptions)
    
    
    public virtual BigQueryExport UpdateBigQueryExport(UpdateBigQueryExportRequest request, CallOptions options)

Update the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateBigQueryExportRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The response received from the server.  
  
### UpdateBigQueryExport(UpdateBigQueryExportRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual BigQueryExport UpdateBigQueryExport(UpdateBigQueryExportRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Update the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateBigQueryExportRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The response received from the server.  
  
### UpdateBigQueryExportAsync(UpdateBigQueryExportRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<BigQueryExport> UpdateBigQueryExportAsync(UpdateBigQueryExportRequest request, CallOptions options)

Update the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateBigQueryExportRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The call object.  
  
### UpdateBigQueryExportAsync(UpdateBigQueryExportRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<BigQueryExport> UpdateBigQueryExportAsync(UpdateBigQueryExportRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Update the BigQuery export configuration for a Chronicle instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.UpdateBigQueryExportRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[BigQueryExport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BigQueryExport)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
