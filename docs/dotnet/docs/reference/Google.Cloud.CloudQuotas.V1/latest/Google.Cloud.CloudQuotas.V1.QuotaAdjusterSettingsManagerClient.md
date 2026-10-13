---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerClient
title: Cloud Quotas v1 API - Class QuotaAdjusterSettingsManagerClient (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:25.041455+00:00
---

# Cloud Quotas v1 API - Class QuotaAdjusterSettingsManagerClient (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Quotas v1 API - Class QuotaAdjusterSettingsManagerClient (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0-beta05 
    
    
    public abstract class QuotaAdjusterSettingsManagerClient

Reference documentation and code samples for the Cloud Quotas v1 API class QuotaAdjusterSettingsManagerClient.

QuotaAdjusterSettingsManager client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > QuotaAdjusterSettingsManagerClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[QuotaAdjusterSettingsManagerClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerClientImpl)

## Namespace

[Google.Cloud.CloudQuotas.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1)

## Assembly

Google.Cloud.CloudQuotas.V1.dll

## Remarks

The Quotas Adjuster Settings API is an infrastructure service for Google Cloud that lets service consumers view and update their quota adjuster settings.

  * Update quota adjuster settings.
  * Get the name of the configurations.



## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the QuotaAdjusterSettingsManager service, which is a host of "cloudquotas.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default QuotaAdjusterSettingsManager scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default QuotaAdjusterSettingsManager scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerClient GrpcClient { get; }

The underlying gRPC QuotaAdjusterSettingsManager client

**Property Value**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettingsManager](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManager)[QuotaAdjusterSettingsManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### Create()
    
    
    public static QuotaAdjusterSettingsManagerClient Create()

Synchronously creates a [QuotaAdjusterSettingsManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [QuotaAdjusterSettingsManagerClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettingsManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerClient)` | The created [QuotaAdjusterSettingsManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<QuotaAdjusterSettingsManagerClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [QuotaAdjusterSettingsManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [QuotaAdjusterSettingsManagerClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaAdjusterSettingsManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerClient)` | The task representing the created [QuotaAdjusterSettingsManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerClient).  
  
### GetQuotaAdjusterSettings(GetQuotaAdjusterSettingsRequest, CallSettings)
    
    
    public virtual QuotaAdjusterSettings GetQuotaAdjusterSettings(GetQuotaAdjusterSettingsRequest request, CallSettings callSettings = null)

Gets the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaAdjusterSettingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | The RPC response.  
**Example**
    
    
    // Create client
    QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient = QuotaAdjusterSettingsManagerClient.Create();
    // Initialize request argument(s)
    GetQuotaAdjusterSettingsRequest request = new GetQuotaAdjusterSettingsRequest
    {
        QuotaAdjusterSettingsName = QuotaAdjusterSettingsName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    QuotaAdjusterSettings response = quotaAdjusterSettingsManagerClient.GetQuotaAdjusterSettings(request);
    

### GetQuotaAdjusterSettings(QuotaAdjusterSettingsName, CallSettings)
    
    
    public virtual QuotaAdjusterSettings GetQuotaAdjusterSettings(QuotaAdjusterSettingsName name, CallSettings callSettings = null)

Gets the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QuotaAdjusterSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsName)`  
Required. Identifier. Name of the `quotaAdjusterSettings` configuration. Only a single setting per project is supported.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | The RPC response.  
**Example**
    
    
    // Create client
    QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient = QuotaAdjusterSettingsManagerClient.Create();
    // Initialize request argument(s)
    QuotaAdjusterSettingsName name = QuotaAdjusterSettingsName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    QuotaAdjusterSettings response = quotaAdjusterSettingsManagerClient.GetQuotaAdjusterSettings(name);
    

### GetQuotaAdjusterSettings(string, CallSettings)
    
    
    public virtual QuotaAdjusterSettings GetQuotaAdjusterSettings(string name, CallSettings callSettings = null)

Gets the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Identifier. Name of the `quotaAdjusterSettings` configuration. Only a single setting per project is supported.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | The RPC response.  
**Example**
    
    
    // Create client
    QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient = QuotaAdjusterSettingsManagerClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/quotaAdjusterSettings";
    // Make the request
    QuotaAdjusterSettings response = quotaAdjusterSettingsManagerClient.GetQuotaAdjusterSettings(name);
    

### GetQuotaAdjusterSettingsAsync(GetQuotaAdjusterSettingsRequest, CallSettings)
    
    
    public virtual Task<QuotaAdjusterSettings> GetQuotaAdjusterSettingsAsync(GetQuotaAdjusterSettingsRequest request, CallSettings callSettings = null)

Gets the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaAdjusterSettingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient = await QuotaAdjusterSettingsManagerClient.CreateAsync();
    // Initialize request argument(s)
    GetQuotaAdjusterSettingsRequest request = new GetQuotaAdjusterSettingsRequest
    {
        QuotaAdjusterSettingsName = QuotaAdjusterSettingsName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    QuotaAdjusterSettings response = await quotaAdjusterSettingsManagerClient.GetQuotaAdjusterSettingsAsync(request);
    

### GetQuotaAdjusterSettingsAsync(GetQuotaAdjusterSettingsRequest, CancellationToken)
    
    
    public virtual Task<QuotaAdjusterSettings> GetQuotaAdjusterSettingsAsync(GetQuotaAdjusterSettingsRequest request, CancellationToken cancellationToken)

Gets the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaAdjusterSettingsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient = await QuotaAdjusterSettingsManagerClient.CreateAsync();
    // Initialize request argument(s)
    GetQuotaAdjusterSettingsRequest request = new GetQuotaAdjusterSettingsRequest
    {
        QuotaAdjusterSettingsName = QuotaAdjusterSettingsName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    QuotaAdjusterSettings response = await quotaAdjusterSettingsManagerClient.GetQuotaAdjusterSettingsAsync(request);
    

### GetQuotaAdjusterSettingsAsync(QuotaAdjusterSettingsName, CallSettings)
    
    
    public virtual Task<QuotaAdjusterSettings> GetQuotaAdjusterSettingsAsync(QuotaAdjusterSettingsName name, CallSettings callSettings = null)

Gets the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QuotaAdjusterSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsName)`  
Required. Identifier. Name of the `quotaAdjusterSettings` configuration. Only a single setting per project is supported.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient = await QuotaAdjusterSettingsManagerClient.CreateAsync();
    // Initialize request argument(s)
    QuotaAdjusterSettingsName name = QuotaAdjusterSettingsName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    QuotaAdjusterSettings response = await quotaAdjusterSettingsManagerClient.GetQuotaAdjusterSettingsAsync(name);
    

### GetQuotaAdjusterSettingsAsync(QuotaAdjusterSettingsName, CancellationToken)
    
    
    public virtual Task<QuotaAdjusterSettings> GetQuotaAdjusterSettingsAsync(QuotaAdjusterSettingsName name, CancellationToken cancellationToken)

Gets the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[QuotaAdjusterSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsName)`  
Required. Identifier. Name of the `quotaAdjusterSettings` configuration. Only a single setting per project is supported.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient = await QuotaAdjusterSettingsManagerClient.CreateAsync();
    // Initialize request argument(s)
    QuotaAdjusterSettingsName name = QuotaAdjusterSettingsName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    QuotaAdjusterSettings response = await quotaAdjusterSettingsManagerClient.GetQuotaAdjusterSettingsAsync(name);
    

### GetQuotaAdjusterSettingsAsync(string, CallSettings)
    
    
    public virtual Task<QuotaAdjusterSettings> GetQuotaAdjusterSettingsAsync(string name, CallSettings callSettings = null)

Gets the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Identifier. Name of the `quotaAdjusterSettings` configuration. Only a single setting per project is supported.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient = await QuotaAdjusterSettingsManagerClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/quotaAdjusterSettings";
    // Make the request
    QuotaAdjusterSettings response = await quotaAdjusterSettingsManagerClient.GetQuotaAdjusterSettingsAsync(name);
    

### GetQuotaAdjusterSettingsAsync(string, CancellationToken)
    
    
    public virtual Task<QuotaAdjusterSettings> GetQuotaAdjusterSettingsAsync(string name, CancellationToken cancellationToken)

Gets the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Identifier. Name of the `quotaAdjusterSettings` configuration. Only a single setting per project is supported.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient = await QuotaAdjusterSettingsManagerClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/quotaAdjusterSettings";
    // Make the request
    QuotaAdjusterSettings response = await quotaAdjusterSettingsManagerClient.GetQuotaAdjusterSettingsAsync(name);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerClient#Google_Cloud_CloudQuotas_V1_QuotaAdjusterSettingsManagerClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerClient#Google_Cloud_CloudQuotas_V1_QuotaAdjusterSettingsManagerClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerClient#Google_Cloud_CloudQuotas_V1_QuotaAdjusterSettingsManagerClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerClient#Google_Cloud_CloudQuotas_V1_QuotaAdjusterSettingsManagerClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateQuotaAdjusterSettings(QuotaAdjusterSettings, FieldMask, CallSettings)
    
    
    public virtual QuotaAdjusterSettings UpdateQuotaAdjusterSettings(QuotaAdjusterSettings quotaAdjusterSettings, FieldMask updateMask, CallSettings callSettings = null)

Updates the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`quotaAdjusterSettings` | `[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)`  
Required. The QuotaAdjusterSettings to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | The RPC response.  
**Example**
    
    
    // Create client
    QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient = QuotaAdjusterSettingsManagerClient.Create();
    // Initialize request argument(s)
    QuotaAdjusterSettings quotaAdjusterSettings = new QuotaAdjusterSettings();
    FieldMask updateMask = new FieldMask();
    // Make the request
    QuotaAdjusterSettings response = quotaAdjusterSettingsManagerClient.UpdateQuotaAdjusterSettings(quotaAdjusterSettings, updateMask);
    

### UpdateQuotaAdjusterSettings(UpdateQuotaAdjusterSettingsRequest, CallSettings)
    
    
    public virtual QuotaAdjusterSettings UpdateQuotaAdjusterSettings(UpdateQuotaAdjusterSettingsRequest request, CallSettings callSettings = null)

Updates the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaAdjusterSettingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | The RPC response.  
**Example**
    
    
    // Create client
    QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient = QuotaAdjusterSettingsManagerClient.Create();
    // Initialize request argument(s)
    UpdateQuotaAdjusterSettingsRequest request = new UpdateQuotaAdjusterSettingsRequest
    {
        QuotaAdjusterSettings = new QuotaAdjusterSettings(),
        UpdateMask = new FieldMask(),
        ValidateOnly = false,
    };
    // Make the request
    QuotaAdjusterSettings response = quotaAdjusterSettingsManagerClient.UpdateQuotaAdjusterSettings(request);
    

### UpdateQuotaAdjusterSettingsAsync(QuotaAdjusterSettings, FieldMask, CallSettings)
    
    
    public virtual Task<QuotaAdjusterSettings> UpdateQuotaAdjusterSettingsAsync(QuotaAdjusterSettings quotaAdjusterSettings, FieldMask updateMask, CallSettings callSettings = null)

Updates the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`quotaAdjusterSettings` | `[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)`  
Required. The QuotaAdjusterSettings to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient = await QuotaAdjusterSettingsManagerClient.CreateAsync();
    // Initialize request argument(s)
    QuotaAdjusterSettings quotaAdjusterSettings = new QuotaAdjusterSettings();
    FieldMask updateMask = new FieldMask();
    // Make the request
    QuotaAdjusterSettings response = await quotaAdjusterSettingsManagerClient.UpdateQuotaAdjusterSettingsAsync(quotaAdjusterSettings, updateMask);
    

### UpdateQuotaAdjusterSettingsAsync(QuotaAdjusterSettings, FieldMask, CancellationToken)
    
    
    public virtual Task<QuotaAdjusterSettings> UpdateQuotaAdjusterSettingsAsync(QuotaAdjusterSettings quotaAdjusterSettings, FieldMask updateMask, CancellationToken cancellationToken)

Updates the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`quotaAdjusterSettings` | `[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)`  
Required. The QuotaAdjusterSettings to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. The list of fields to update.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient = await QuotaAdjusterSettingsManagerClient.CreateAsync();
    // Initialize request argument(s)
    QuotaAdjusterSettings quotaAdjusterSettings = new QuotaAdjusterSettings();
    FieldMask updateMask = new FieldMask();
    // Make the request
    QuotaAdjusterSettings response = await quotaAdjusterSettingsManagerClient.UpdateQuotaAdjusterSettingsAsync(quotaAdjusterSettings, updateMask);
    

### UpdateQuotaAdjusterSettingsAsync(UpdateQuotaAdjusterSettingsRequest, CallSettings)
    
    
    public virtual Task<QuotaAdjusterSettings> UpdateQuotaAdjusterSettingsAsync(UpdateQuotaAdjusterSettingsRequest request, CallSettings callSettings = null)

Updates the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaAdjusterSettingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient = await QuotaAdjusterSettingsManagerClient.CreateAsync();
    // Initialize request argument(s)
    UpdateQuotaAdjusterSettingsRequest request = new UpdateQuotaAdjusterSettingsRequest
    {
        QuotaAdjusterSettings = new QuotaAdjusterSettings(),
        UpdateMask = new FieldMask(),
        ValidateOnly = false,
    };
    // Make the request
    QuotaAdjusterSettings response = await quotaAdjusterSettingsManagerClient.UpdateQuotaAdjusterSettingsAsync(request);
    

### UpdateQuotaAdjusterSettingsAsync(UpdateQuotaAdjusterSettingsRequest, CancellationToken)
    
    
    public virtual Task<QuotaAdjusterSettings> UpdateQuotaAdjusterSettingsAsync(UpdateQuotaAdjusterSettingsRequest request, CancellationToken cancellationToken)

Updates the QuotaAdjusterSettings for the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaAdjusterSettingsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    QuotaAdjusterSettingsManagerClient quotaAdjusterSettingsManagerClient = await QuotaAdjusterSettingsManagerClient.CreateAsync();
    // Initialize request argument(s)
    UpdateQuotaAdjusterSettingsRequest request = new UpdateQuotaAdjusterSettingsRequest
    {
        QuotaAdjusterSettings = new QuotaAdjusterSettings(),
        UpdateMask = new FieldMask(),
        ValidateOnly = false,
    };
    // Make the request
    QuotaAdjusterSettings response = await quotaAdjusterSettingsManagerClient.UpdateQuotaAdjusterSettingsAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
