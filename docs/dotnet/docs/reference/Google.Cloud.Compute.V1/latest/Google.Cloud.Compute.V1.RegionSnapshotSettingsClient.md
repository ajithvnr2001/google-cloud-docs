---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettingsClient
title: Compute Engine v1 API - Class RegionSnapshotSettingsClient (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:47.174388+00:00
---

# Compute Engine v1 API - Class RegionSnapshotSettingsClient (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettingsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class RegionSnapshotSettingsClient (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public abstract class RegionSnapshotSettingsClient

Reference documentation and code samples for the Compute Engine v1 API class RegionSnapshotSettingsClient.

RegionSnapshotSettings client wrapper, for convenient use. This client implements API version 2026-09-01.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RegionSnapshotSettingsClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[RegionSnapshotSettingsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettingsClientImpl)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Remarks

The RegionSnapshotSettings API.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the RegionSnapshotSettings service, which is a host of "compute.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default RegionSnapshotSettings scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default RegionSnapshotSettings scopes are:

  * <https://www.googleapis.com/auth/compute>
  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual RegionSnapshotSettings.RegionSnapshotSettingsClient GrpcClient { get; }

The underlying gRPC RegionSnapshotSettings client

**Property Value**  
---  
**Type** | **Description**  
`[RegionSnapshotSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettings)[RegionSnapshotSettingsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettings.RegionSnapshotSettingsClient)` |   
  
### PatchOperationsClient
    
    
    public virtual OperationsClient PatchOperationsClient { get; }

The long-running operations client for `Patch`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### Create()
    
    
    public static RegionSnapshotSettingsClient Create()

Synchronously creates a [RegionSnapshotSettingsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettingsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [RegionSnapshotSettingsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettingsClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[RegionSnapshotSettingsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettingsClient)` | The created [RegionSnapshotSettingsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettingsClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<RegionSnapshotSettingsClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [RegionSnapshotSettingsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettingsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [RegionSnapshotSettingsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettingsClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RegionSnapshotSettingsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettingsClient)` | The task representing the created [RegionSnapshotSettingsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettingsClient).  
  
### Get(GetRegionSnapshotSettingRequest, CallSettings)
    
    
    public virtual SnapshotSettings Get(GetRegionSnapshotSettingRequest request, CallSettings callSettings = null)

Get region snapshot settings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRegionSnapshotSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetRegionSnapshotSettingRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SnapshotSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SnapshotSettings)` | The RPC response.  
**Example**
    
    
    // Create client
    RegionSnapshotSettingsClient regionSnapshotSettingsClient = RegionSnapshotSettingsClient.Create();
    // Initialize request argument(s)
    GetRegionSnapshotSettingRequest request = new GetRegionSnapshotSettingRequest
    {
        Region = "",
        Project = "",
    };
    // Make the request
    SnapshotSettings response = regionSnapshotSettingsClient.Get(request);
    

### Get(string, string, CallSettings)
    
    
    public virtual SnapshotSettings Get(string project, string region, CallSettings callSettings = null)

Get region snapshot settings.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SnapshotSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SnapshotSettings)` | The RPC response.  
**Example**
    
    
    // Create client
    RegionSnapshotSettingsClient regionSnapshotSettingsClient = RegionSnapshotSettingsClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    // Make the request
    SnapshotSettings response = regionSnapshotSettingsClient.Get(project, region);
    

### GetAsync(GetRegionSnapshotSettingRequest, CallSettings)
    
    
    public virtual Task<SnapshotSettings> GetAsync(GetRegionSnapshotSettingRequest request, CallSettings callSettings = null)

Get region snapshot settings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRegionSnapshotSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetRegionSnapshotSettingRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SnapshotSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SnapshotSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    RegionSnapshotSettingsClient regionSnapshotSettingsClient = await RegionSnapshotSettingsClient.CreateAsync();
    // Initialize request argument(s)
    GetRegionSnapshotSettingRequest request = new GetRegionSnapshotSettingRequest
    {
        Region = "",
        Project = "",
    };
    // Make the request
    SnapshotSettings response = await regionSnapshotSettingsClient.GetAsync(request);
    

### GetAsync(GetRegionSnapshotSettingRequest, CancellationToken)
    
    
    public virtual Task<SnapshotSettings> GetAsync(GetRegionSnapshotSettingRequest request, CancellationToken cancellationToken)

Get region snapshot settings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRegionSnapshotSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetRegionSnapshotSettingRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SnapshotSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SnapshotSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    RegionSnapshotSettingsClient regionSnapshotSettingsClient = await RegionSnapshotSettingsClient.CreateAsync();
    // Initialize request argument(s)
    GetRegionSnapshotSettingRequest request = new GetRegionSnapshotSettingRequest
    {
        Region = "",
        Project = "",
    };
    // Make the request
    SnapshotSettings response = await regionSnapshotSettingsClient.GetAsync(request);
    

### GetAsync(string, string, CallSettings)
    
    
    public virtual Task<SnapshotSettings> GetAsync(string project, string region, CallSettings callSettings = null)

Get region snapshot settings.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SnapshotSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SnapshotSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    RegionSnapshotSettingsClient regionSnapshotSettingsClient = await RegionSnapshotSettingsClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    // Make the request
    SnapshotSettings response = await regionSnapshotSettingsClient.GetAsync(project, region);
    

### GetAsync(string, string, CancellationToken)
    
    
    public virtual Task<SnapshotSettings> GetAsync(string project, string region, CancellationToken cancellationToken)

Get region snapshot settings.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SnapshotSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SnapshotSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    RegionSnapshotSettingsClient regionSnapshotSettingsClient = await RegionSnapshotSettingsClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    // Make the request
    SnapshotSettings response = await regionSnapshotSettingsClient.GetAsync(project, region);
    

### Patch(PatchRegionSnapshotSettingRequest, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Patch(PatchRegionSnapshotSettingRequest request, CallSettings callSettings = null)

Patch region snapshot settings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchRegionSnapshotSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchRegionSnapshotSettingRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    RegionSnapshotSettingsClient regionSnapshotSettingsClient = RegionSnapshotSettingsClient.Create();
    // Initialize request argument(s)
    PatchRegionSnapshotSettingRequest request = new PatchRegionSnapshotSettingRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        SnapshotSettingsResource = new SnapshotSettings(),
        UpdateMask = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = regionSnapshotSettingsClient.Patch(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = regionSnapshotSettingsClient.PollOncePatch(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### Patch(string, string, SnapshotSettings, CallSettings)
    
    
    public virtual Operation<Operation, Operation> Patch(string project, string region, SnapshotSettings snapshotSettingsResource, CallSettings callSettings = null)

Patch region snapshot settings.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`snapshotSettingsResource` | `[SnapshotSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SnapshotSettings)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The RPC response.  
**Example**
    
    
    // Create client
    RegionSnapshotSettingsClient regionSnapshotSettingsClient = RegionSnapshotSettingsClient.Create();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    SnapshotSettings snapshotSettingsResource = new SnapshotSettings();
    // Make the request
    lro::Operation<Operation, Operation> response = regionSnapshotSettingsClient.Patch(project, region, snapshotSettingsResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = regionSnapshotSettingsClient.PollOncePatch(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### PatchAsync(PatchRegionSnapshotSettingRequest, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> PatchAsync(PatchRegionSnapshotSettingRequest request, CallSettings callSettings = null)

Patch region snapshot settings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchRegionSnapshotSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchRegionSnapshotSettingRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    RegionSnapshotSettingsClient regionSnapshotSettingsClient = await RegionSnapshotSettingsClient.CreateAsync();
    // Initialize request argument(s)
    PatchRegionSnapshotSettingRequest request = new PatchRegionSnapshotSettingRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        SnapshotSettingsResource = new SnapshotSettings(),
        UpdateMask = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await regionSnapshotSettingsClient.PatchAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await regionSnapshotSettingsClient.PollOncePatchAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### PatchAsync(PatchRegionSnapshotSettingRequest, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> PatchAsync(PatchRegionSnapshotSettingRequest request, CancellationToken cancellationToken)

Patch region snapshot settings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchRegionSnapshotSettingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchRegionSnapshotSettingRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    RegionSnapshotSettingsClient regionSnapshotSettingsClient = await RegionSnapshotSettingsClient.CreateAsync();
    // Initialize request argument(s)
    PatchRegionSnapshotSettingRequest request = new PatchRegionSnapshotSettingRequest
    {
        RequestId = "",
        Region = "",
        Project = "",
        SnapshotSettingsResource = new SnapshotSettings(),
        UpdateMask = "",
    };
    // Make the request
    lro::Operation<Operation, Operation> response = await regionSnapshotSettingsClient.PatchAsync(request);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await regionSnapshotSettingsClient.PollOncePatchAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### PatchAsync(string, string, SnapshotSettings, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> PatchAsync(string project, string region, SnapshotSettings snapshotSettingsResource, CallSettings callSettings = null)

Patch region snapshot settings.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`snapshotSettingsResource` | `[SnapshotSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SnapshotSettings)`  
The body resource for this request  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    RegionSnapshotSettingsClient regionSnapshotSettingsClient = await RegionSnapshotSettingsClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    SnapshotSettings snapshotSettingsResource = new SnapshotSettings();
    // Make the request
    lro::Operation<Operation, Operation> response = await regionSnapshotSettingsClient.PatchAsync(project, region, snapshotSettingsResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await regionSnapshotSettingsClient.PollOncePatchAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### PatchAsync(string, string, SnapshotSettings, CancellationToken)
    
    
    public virtual Task<Operation<Operation, Operation>> PatchAsync(string project, string region, SnapshotSettings snapshotSettingsResource, CancellationToken cancellationToken)

Patch region snapshot settings.

**Parameters**  
---  
**Name** | **Description**  
`project` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Project ID for this request.  
`region` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Name of the region for this request.  
`snapshotSettingsResource` | `[SnapshotSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SnapshotSettings)`  
The body resource for this request  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    RegionSnapshotSettingsClient regionSnapshotSettingsClient = await RegionSnapshotSettingsClient.CreateAsync();
    // Initialize request argument(s)
    string project = "";
    string region = "";
    SnapshotSettings snapshotSettingsResource = new SnapshotSettings();
    // Make the request
    lro::Operation<Operation, Operation> response = await regionSnapshotSettingsClient.PatchAsync(project, region, snapshotSettingsResource);
    
    // Poll until the returned long-running operation is complete
    lro::Operation<Operation, Operation> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Operation result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    lro::Operation<Operation, Operation> retrievedResponse = await regionSnapshotSettingsClient.PollOncePatchAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Operation retrievedResult = retrievedResponse.Result;
    }
    

### PollOncePatch(string, CallSettings)
    
    
    public virtual Operation<Operation, Operation> PollOncePatch(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `Patch`.

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The result of polling the operation.  
  
### PollOncePatchAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Operation, Operation>> PollOncePatchAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `Patch` .

**Parameters**  
---  
**Name** | **Description**  
`operationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of a previously invoked operation. Must not be `null` or empty.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | A task representing the result of polling the operation.  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettingsClient#Google_Cloud_Compute_V1_RegionSnapshotSettingsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettingsClient#Google_Cloud_Compute_V1_RegionSnapshotSettingsClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettingsClient#Google_Cloud_Compute_V1_RegionSnapshotSettingsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettingsClient#Google_Cloud_Compute_V1_RegionSnapshotSettingsClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
