---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.WarehouseClient
title: Vision AI v1 API - Class WarehouseClient (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:44:05.079097+00:00
---

# Vision AI v1 API - Class WarehouseClient (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.WarehouseClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vision AI v1 API - Class WarehouseClient (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public abstract class WarehouseClient

Reference documentation and code samples for the Vision AI v1 API class WarehouseClient.

Warehouse client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > WarehouseClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[WarehouseClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.WarehouseClientImpl)

## Namespace

[Google.Cloud.VisionAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1)

## Assembly

Google.Cloud.VisionAI.V1.dll

## Remarks

Service that manages media content + metadata for streaming.

## Properties 

### AnalyzeAssetOperationsClient
    
    
    public virtual OperationsClient AnalyzeAssetOperationsClient { get; }

The long-running operations client for `AnalyzeAsset`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### AnalyzeCorpusOperationsClient
    
    
    public virtual OperationsClient AnalyzeCorpusOperationsClient { get; }

The long-running operations client for `AnalyzeCorpus`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateCollectionOperationsClient
    
    
    public virtual OperationsClient CreateCollectionOperationsClient { get; }

The long-running operations client for `CreateCollection`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateCorpusOperationsClient
    
    
    public virtual OperationsClient CreateCorpusOperationsClient { get; }

The long-running operations client for `CreateCorpus`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateIndexEndpointOperationsClient
    
    
    public virtual OperationsClient CreateIndexEndpointOperationsClient { get; }

The long-running operations client for `CreateIndexEndpoint`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateIndexOperationsClient
    
    
    public virtual OperationsClient CreateIndexOperationsClient { get; }

The long-running operations client for `CreateIndex`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the Warehouse service, which is a host of "warehouse-visionai.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default Warehouse scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default Warehouse scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteAssetOperationsClient
    
    
    public virtual OperationsClient DeleteAssetOperationsClient { get; }

The long-running operations client for `DeleteAsset`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteCollectionOperationsClient
    
    
    public virtual OperationsClient DeleteCollectionOperationsClient { get; }

The long-running operations client for `DeleteCollection`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteIndexEndpointOperationsClient
    
    
    public virtual OperationsClient DeleteIndexEndpointOperationsClient { get; }

The long-running operations client for `DeleteIndexEndpoint`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteIndexOperationsClient
    
    
    public virtual OperationsClient DeleteIndexOperationsClient { get; }

The long-running operations client for `DeleteIndex`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeployIndexOperationsClient
    
    
    public virtual OperationsClient DeployIndexOperationsClient { get; }

The long-running operations client for `DeployIndex`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual Warehouse.WarehouseClient GrpcClient { get; }

The underlying gRPC Warehouse client

**Property Value**  
---  
**Type** | **Description**  
`[Warehouse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Warehouse)[WarehouseClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Warehouse.WarehouseClient)` |   
  
### IAMPolicyClient
    
    
    public virtual IAMPolicyClient IAMPolicyClient { get; }

The [IAMPolicyClient](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[IAMPolicyClient](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html)` |   
  
### ImportAssetsOperationsClient
    
    
    public virtual OperationsClient ImportAssetsOperationsClient { get; }

The long-running operations client for `ImportAssets`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### IndexAssetOperationsClient
    
    
    public virtual OperationsClient IndexAssetOperationsClient { get; }

The long-running operations client for `IndexAsset`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### LocationsClient
    
    
    public virtual LocationsClient LocationsClient { get; }

The [LocationsClient](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[LocationsClient](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html)` |   
  
### RemoveIndexAssetOperationsClient
    
    
    public virtual OperationsClient RemoveIndexAssetOperationsClient { get; }

The long-running operations client for `RemoveIndexAsset`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
### UndeployIndexOperationsClient
    
    
    public virtual OperationsClient UndeployIndexOperationsClient { get; }

The long-running operations client for `UndeployIndex`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateIndexEndpointOperationsClient
    
    
    public virtual OperationsClient UpdateIndexEndpointOperationsClient { get; }

The long-running operations client for `UpdateIndexEndpoint`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateIndexOperationsClient
    
    
    public virtual OperationsClient UpdateIndexOperationsClient { get; }

The long-running operations client for `UpdateIndex`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UploadAssetOperationsClient
    
    
    public virtual OperationsClient UploadAssetOperationsClient { get; }

The long-running operations client for `UploadAsset`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### AddCollectionItem(AddCollectionItemRequest, CallSettings)
    
    
    public virtual AddCollectionItemResponse AddCollectionItem(AddCollectionItemRequest request, CallSettings callSettings = null)

Adds an item into a Collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddCollectionItemRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddCollectionItemRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AddCollectionItemResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddCollectionItemResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::AddCollectionItemRequest request = new gcvv::AddCollectionItemRequest
    {
        Item = new gcvv::CollectionItem(),
    };
    // Make the request
    gcvv::AddCollectionItemResponse response = warehouseClient.AddCollectionItem(request);
    

### AddCollectionItem(CollectionItem, CallSettings)
    
    
    public virtual AddCollectionItemResponse AddCollectionItem(CollectionItem item, CallSettings callSettings = null)

Adds an item into a Collection.

**Parameters**  
---  
**Name** | **Description**  
`item` | `[CollectionItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionItem)`  
Required. The item to be added.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AddCollectionItemResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddCollectionItemResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CollectionItem item = new gcvv::CollectionItem();
    // Make the request
    gcvv::AddCollectionItemResponse response = warehouseClient.AddCollectionItem(item);
    

### AddCollectionItemAsync(AddCollectionItemRequest, CallSettings)
    
    
    public virtual Task<AddCollectionItemResponse> AddCollectionItemAsync(AddCollectionItemRequest request, CallSettings callSettings = null)

Adds an item into a Collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddCollectionItemRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddCollectionItemRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AddCollectionItemResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddCollectionItemResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::AddCollectionItemRequest request = new gcvv::AddCollectionItemRequest
    {
        Item = new gcvv::CollectionItem(),
    };
    // Make the request
    gcvv::AddCollectionItemResponse response = await warehouseClient.AddCollectionItemAsync(request);
    

### AddCollectionItemAsync(AddCollectionItemRequest, CancellationToken)
    
    
    public virtual Task<AddCollectionItemResponse> AddCollectionItemAsync(AddCollectionItemRequest request, CancellationToken cancellationToken)

Adds an item into a Collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddCollectionItemRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddCollectionItemRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AddCollectionItemResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddCollectionItemResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::AddCollectionItemRequest request = new gcvv::AddCollectionItemRequest
    {
        Item = new gcvv::CollectionItem(),
    };
    // Make the request
    gcvv::AddCollectionItemResponse response = await warehouseClient.AddCollectionItemAsync(request);
    

### AddCollectionItemAsync(CollectionItem, CallSettings)
    
    
    public virtual Task<AddCollectionItemResponse> AddCollectionItemAsync(CollectionItem item, CallSettings callSettings = null)

Adds an item into a Collection.

**Parameters**  
---  
**Name** | **Description**  
`item` | `[CollectionItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionItem)`  
Required. The item to be added.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AddCollectionItemResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddCollectionItemResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CollectionItem item = new gcvv::CollectionItem();
    // Make the request
    gcvv::AddCollectionItemResponse response = await warehouseClient.AddCollectionItemAsync(item);
    

### AddCollectionItemAsync(CollectionItem, CancellationToken)
    
    
    public virtual Task<AddCollectionItemResponse> AddCollectionItemAsync(CollectionItem item, CancellationToken cancellationToken)

Adds an item into a Collection.

**Parameters**  
---  
**Name** | **Description**  
`item` | `[CollectionItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionItem)`  
Required. The item to be added.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AddCollectionItemResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AddCollectionItemResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CollectionItem item = new gcvv::CollectionItem();
    // Make the request
    gcvv::AddCollectionItemResponse response = await warehouseClient.AddCollectionItemAsync(item);
    

### AnalyzeAsset(AnalyzeAssetRequest, CallSettings)
    
    
    public virtual Operation<AnalyzeAssetResponse, AnalyzeAssetMetadata> AnalyzeAsset(AnalyzeAssetRequest request, CallSettings callSettings = null)

Analyze asset to power search capability.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AnalyzeAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeAssetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnalyzeAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeAssetResponse)[AnalyzeAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeAssetMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::AnalyzeAssetRequest request = new gcvv::AnalyzeAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
    };
    // Make the request
    Operation<gcvv::AnalyzeAssetResponse, gcvv::AnalyzeAssetMetadata> response = warehouseClient.AnalyzeAsset(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::AnalyzeAssetResponse, gcvv::AnalyzeAssetMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::AnalyzeAssetResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::AnalyzeAssetResponse, gcvv::AnalyzeAssetMetadata> retrievedResponse = warehouseClient.PollOnceAnalyzeAsset(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::AnalyzeAssetResponse retrievedResult = retrievedResponse.Result;
    }
    

### AnalyzeAssetAsync(AnalyzeAssetRequest, CallSettings)
    
    
    public virtual Task<Operation<AnalyzeAssetResponse, AnalyzeAssetMetadata>> AnalyzeAssetAsync(AnalyzeAssetRequest request, CallSettings callSettings = null)

Analyze asset to power search capability.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AnalyzeAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeAssetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnalyzeAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeAssetResponse)[AnalyzeAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeAssetMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::AnalyzeAssetRequest request = new gcvv::AnalyzeAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
    };
    // Make the request
    Operation<gcvv::AnalyzeAssetResponse, gcvv::AnalyzeAssetMetadata> response = await warehouseClient.AnalyzeAssetAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::AnalyzeAssetResponse, gcvv::AnalyzeAssetMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::AnalyzeAssetResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::AnalyzeAssetResponse, gcvv::AnalyzeAssetMetadata> retrievedResponse = await warehouseClient.PollOnceAnalyzeAssetAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::AnalyzeAssetResponse retrievedResult = retrievedResponse.Result;
    }
    

### AnalyzeAssetAsync(AnalyzeAssetRequest, CancellationToken)
    
    
    public virtual Task<Operation<AnalyzeAssetResponse, AnalyzeAssetMetadata>> AnalyzeAssetAsync(AnalyzeAssetRequest request, CancellationToken cancellationToken)

Analyze asset to power search capability.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AnalyzeAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeAssetRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnalyzeAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeAssetResponse)[AnalyzeAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeAssetMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::AnalyzeAssetRequest request = new gcvv::AnalyzeAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
    };
    // Make the request
    Operation<gcvv::AnalyzeAssetResponse, gcvv::AnalyzeAssetMetadata> response = await warehouseClient.AnalyzeAssetAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::AnalyzeAssetResponse, gcvv::AnalyzeAssetMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::AnalyzeAssetResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::AnalyzeAssetResponse, gcvv::AnalyzeAssetMetadata> retrievedResponse = await warehouseClient.PollOnceAnalyzeAssetAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::AnalyzeAssetResponse retrievedResult = retrievedResponse.Result;
    }
    

### AnalyzeCorpus(AnalyzeCorpusRequest, CallSettings)
    
    
    public virtual Operation<AnalyzeCorpusResponse, AnalyzeCorpusMetadata> AnalyzeCorpus(AnalyzeCorpusRequest request, CallSettings callSettings = null)

Analyzes a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AnalyzeCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeCorpusRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnalyzeCorpusResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeCorpusResponse)[AnalyzeCorpusMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeCorpusMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::AnalyzeCorpusRequest request = new gcvv::AnalyzeCorpusRequest
    {
        CorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
    };
    // Make the request
    Operation<gcvv::AnalyzeCorpusResponse, gcvv::AnalyzeCorpusMetadata> response = warehouseClient.AnalyzeCorpus(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::AnalyzeCorpusResponse, gcvv::AnalyzeCorpusMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::AnalyzeCorpusResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::AnalyzeCorpusResponse, gcvv::AnalyzeCorpusMetadata> retrievedResponse = warehouseClient.PollOnceAnalyzeCorpus(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::AnalyzeCorpusResponse retrievedResult = retrievedResponse.Result;
    }
    

### AnalyzeCorpusAsync(AnalyzeCorpusRequest, CallSettings)
    
    
    public virtual Task<Operation<AnalyzeCorpusResponse, AnalyzeCorpusMetadata>> AnalyzeCorpusAsync(AnalyzeCorpusRequest request, CallSettings callSettings = null)

Analyzes a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AnalyzeCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeCorpusRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnalyzeCorpusResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeCorpusResponse)[AnalyzeCorpusMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeCorpusMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::AnalyzeCorpusRequest request = new gcvv::AnalyzeCorpusRequest
    {
        CorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
    };
    // Make the request
    Operation<gcvv::AnalyzeCorpusResponse, gcvv::AnalyzeCorpusMetadata> response = await warehouseClient.AnalyzeCorpusAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::AnalyzeCorpusResponse, gcvv::AnalyzeCorpusMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::AnalyzeCorpusResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::AnalyzeCorpusResponse, gcvv::AnalyzeCorpusMetadata> retrievedResponse = await warehouseClient.PollOnceAnalyzeCorpusAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::AnalyzeCorpusResponse retrievedResult = retrievedResponse.Result;
    }
    

### AnalyzeCorpusAsync(AnalyzeCorpusRequest, CancellationToken)
    
    
    public virtual Task<Operation<AnalyzeCorpusResponse, AnalyzeCorpusMetadata>> AnalyzeCorpusAsync(AnalyzeCorpusRequest request, CancellationToken cancellationToken)

Analyzes a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AnalyzeCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeCorpusRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnalyzeCorpusResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeCorpusResponse)[AnalyzeCorpusMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeCorpusMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::AnalyzeCorpusRequest request = new gcvv::AnalyzeCorpusRequest
    {
        CorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
    };
    // Make the request
    Operation<gcvv::AnalyzeCorpusResponse, gcvv::AnalyzeCorpusMetadata> response = await warehouseClient.AnalyzeCorpusAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::AnalyzeCorpusResponse, gcvv::AnalyzeCorpusMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::AnalyzeCorpusResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::AnalyzeCorpusResponse, gcvv::AnalyzeCorpusMetadata> retrievedResponse = await warehouseClient.PollOnceAnalyzeCorpusAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::AnalyzeCorpusResponse retrievedResult = retrievedResponse.Result;
    }
    

### ClipAsset(ClipAssetRequest, CallSettings)
    
    
    public virtual ClipAssetResponse ClipAsset(ClipAssetRequest request, CallSettings callSettings = null)

Supported by STREAM_VIDEO corpus type. Generates clips for downloading. The api takes in a time range, and generates a clip of the first content available after start_time and before end_time, which may overflow beyond these bounds. Returned clips are truncated if the total size of the clips are larger than 100MB.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ClipAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ClipAssetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ClipAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ClipAssetResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::ClipAssetRequest request = new gcvv::ClipAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
        TemporalPartition = new gcvv::Partition.Types.TemporalPartition(),
    };
    // Make the request
    gcvv::ClipAssetResponse response = warehouseClient.ClipAsset(request);
    

### ClipAssetAsync(ClipAssetRequest, CallSettings)
    
    
    public virtual Task<ClipAssetResponse> ClipAssetAsync(ClipAssetRequest request, CallSettings callSettings = null)

Supported by STREAM_VIDEO corpus type. Generates clips for downloading. The api takes in a time range, and generates a clip of the first content available after start_time and before end_time, which may overflow beyond these bounds. Returned clips are truncated if the total size of the clips are larger than 100MB.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ClipAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ClipAssetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ClipAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ClipAssetResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::ClipAssetRequest request = new gcvv::ClipAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
        TemporalPartition = new gcvv::Partition.Types.TemporalPartition(),
    };
    // Make the request
    gcvv::ClipAssetResponse response = await warehouseClient.ClipAssetAsync(request);
    

### ClipAssetAsync(ClipAssetRequest, CancellationToken)
    
    
    public virtual Task<ClipAssetResponse> ClipAssetAsync(ClipAssetRequest request, CancellationToken cancellationToken)

Supported by STREAM_VIDEO corpus type. Generates clips for downloading. The api takes in a time range, and generates a clip of the first content available after start_time and before end_time, which may overflow beyond these bounds. Returned clips are truncated if the total size of the clips are larger than 100MB.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ClipAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ClipAssetRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ClipAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ClipAssetResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::ClipAssetRequest request = new gcvv::ClipAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
        TemporalPartition = new gcvv::Partition.Types.TemporalPartition(),
    };
    // Make the request
    gcvv::ClipAssetResponse response = await warehouseClient.ClipAssetAsync(request);
    

### Create()
    
    
    public static WarehouseClient Create()

Synchronously creates a [WarehouseClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.WarehouseClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [WarehouseClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.WarehouseClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[WarehouseClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.WarehouseClient)` | The created [WarehouseClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.WarehouseClient).  
  
### CreateAnnotation(AssetName, Annotation, string, CallSettings)
    
    
    public virtual Annotation CreateAnnotation(AssetName parent, Annotation annotation, string annotationId, CallSettings callSettings = null)

Creates annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AssetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AssetName)`  
Required. The parent resource where this annotation will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/assets/{asset_id}`  
`annotation` | `[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)`  
Required. The annotation to create.  
`annotationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the annotation, which will become the final component of the annotation's resource name if user choose to specify. Otherwise, annotation id will be generated by system. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::AssetName parent = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]");
    gcvv::Annotation annotation = new gcvv::Annotation();
    string annotationId = "";
    // Make the request
    gcvv::Annotation response = warehouseClient.CreateAnnotation(parent, annotation, annotationId);
    

### CreateAnnotation(CreateAnnotationRequest, CallSettings)
    
    
    public virtual Annotation CreateAnnotation(CreateAnnotationRequest request, CallSettings callSettings = null)

Creates annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAnnotationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateAnnotationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CreateAnnotationRequest request = new gcvv::CreateAnnotationRequest
    {
        ParentAsAssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
        Annotation = new gcvv::Annotation(),
        AnnotationId = "",
    };
    // Make the request
    gcvv::Annotation response = warehouseClient.CreateAnnotation(request);
    

### CreateAnnotation(string, Annotation, string, CallSettings)
    
    
    public virtual Annotation CreateAnnotation(string parent, Annotation annotation, string annotationId, CallSettings callSettings = null)

Creates annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this annotation will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/assets/{asset_id}`  
`annotation` | `[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)`  
Required. The annotation to create.  
`annotationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the annotation, which will become the final component of the annotation's resource name if user choose to specify. Otherwise, annotation id will be generated by system. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/assets/[ASSET]";
    gcvv::Annotation annotation = new gcvv::Annotation();
    string annotationId = "";
    // Make the request
    gcvv::Annotation response = warehouseClient.CreateAnnotation(parent, annotation, annotationId);
    

### CreateAnnotationAsync(AssetName, Annotation, string, CallSettings)
    
    
    public virtual Task<Annotation> CreateAnnotationAsync(AssetName parent, Annotation annotation, string annotationId, CallSettings callSettings = null)

Creates annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AssetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AssetName)`  
Required. The parent resource where this annotation will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/assets/{asset_id}`  
`annotation` | `[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)`  
Required. The annotation to create.  
`annotationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the annotation, which will become the final component of the annotation's resource name if user choose to specify. Otherwise, annotation id will be generated by system. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::AssetName parent = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]");
    gcvv::Annotation annotation = new gcvv::Annotation();
    string annotationId = "";
    // Make the request
    gcvv::Annotation response = await warehouseClient.CreateAnnotationAsync(parent, annotation, annotationId);
    

### CreateAnnotationAsync(AssetName, Annotation, string, CancellationToken)
    
    
    public virtual Task<Annotation> CreateAnnotationAsync(AssetName parent, Annotation annotation, string annotationId, CancellationToken cancellationToken)

Creates annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AssetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AssetName)`  
Required. The parent resource where this annotation will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/assets/{asset_id}`  
`annotation` | `[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)`  
Required. The annotation to create.  
`annotationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the annotation, which will become the final component of the annotation's resource name if user choose to specify. Otherwise, annotation id will be generated by system. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::AssetName parent = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]");
    gcvv::Annotation annotation = new gcvv::Annotation();
    string annotationId = "";
    // Make the request
    gcvv::Annotation response = await warehouseClient.CreateAnnotationAsync(parent, annotation, annotationId);
    

### CreateAnnotationAsync(CreateAnnotationRequest, CallSettings)
    
    
    public virtual Task<Annotation> CreateAnnotationAsync(CreateAnnotationRequest request, CallSettings callSettings = null)

Creates annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAnnotationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateAnnotationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CreateAnnotationRequest request = new gcvv::CreateAnnotationRequest
    {
        ParentAsAssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
        Annotation = new gcvv::Annotation(),
        AnnotationId = "",
    };
    // Make the request
    gcvv::Annotation response = await warehouseClient.CreateAnnotationAsync(request);
    

### CreateAnnotationAsync(CreateAnnotationRequest, CancellationToken)
    
    
    public virtual Task<Annotation> CreateAnnotationAsync(CreateAnnotationRequest request, CancellationToken cancellationToken)

Creates annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAnnotationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateAnnotationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CreateAnnotationRequest request = new gcvv::CreateAnnotationRequest
    {
        ParentAsAssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
        Annotation = new gcvv::Annotation(),
        AnnotationId = "",
    };
    // Make the request
    gcvv::Annotation response = await warehouseClient.CreateAnnotationAsync(request);
    

### CreateAnnotationAsync(string, Annotation, string, CallSettings)
    
    
    public virtual Task<Annotation> CreateAnnotationAsync(string parent, Annotation annotation, string annotationId, CallSettings callSettings = null)

Creates annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this annotation will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/assets/{asset_id}`  
`annotation` | `[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)`  
Required. The annotation to create.  
`annotationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the annotation, which will become the final component of the annotation's resource name if user choose to specify. Otherwise, annotation id will be generated by system. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/assets/[ASSET]";
    gcvv::Annotation annotation = new gcvv::Annotation();
    string annotationId = "";
    // Make the request
    gcvv::Annotation response = await warehouseClient.CreateAnnotationAsync(parent, annotation, annotationId);
    

### CreateAnnotationAsync(string, Annotation, string, CancellationToken)
    
    
    public virtual Task<Annotation> CreateAnnotationAsync(string parent, Annotation annotation, string annotationId, CancellationToken cancellationToken)

Creates annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this annotation will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/assets/{asset_id}`  
`annotation` | `[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)`  
Required. The annotation to create.  
`annotationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the annotation, which will become the final component of the annotation's resource name if user choose to specify. Otherwise, annotation id will be generated by system. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/assets/[ASSET]";
    gcvv::Annotation annotation = new gcvv::Annotation();
    string annotationId = "";
    // Make the request
    gcvv::Annotation response = await warehouseClient.CreateAnnotationAsync(parent, annotation, annotationId);
    

### CreateAsset(CorpusName, Asset, string, CallSettings)
    
    
    public virtual Asset CreateAsset(CorpusName parent, Asset asset, string assetId, CallSettings callSettings = null)

Creates an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent resource where this asset will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`asset` | `[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)`  
Required. The asset to create.  
`assetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the asset, which will become the final component of the asset's resource name if user choose to specify. Otherwise, asset id will be generated by system. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    gcvv::Asset asset = new gcvv::Asset();
    string assetId = "";
    // Make the request
    gcvv::Asset response = warehouseClient.CreateAsset(parent, asset, assetId);
    

### CreateAsset(CreateAssetRequest, CallSettings)
    
    
    public virtual Asset CreateAsset(CreateAssetRequest request, CallSettings callSettings = null)

Creates an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateAssetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CreateAssetRequest request = new gcvv::CreateAssetRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        Asset = new gcvv::Asset(),
        AssetId = "",
    };
    // Make the request
    gcvv::Asset response = warehouseClient.CreateAsset(request);
    

### CreateAsset(string, Asset, string, CallSettings)
    
    
    public virtual Asset CreateAsset(string parent, Asset asset, string assetId, CallSettings callSettings = null)

Creates an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this asset will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`asset` | `[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)`  
Required. The asset to create.  
`assetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the asset, which will become the final component of the asset's resource name if user choose to specify. Otherwise, asset id will be generated by system. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    gcvv::Asset asset = new gcvv::Asset();
    string assetId = "";
    // Make the request
    gcvv::Asset response = warehouseClient.CreateAsset(parent, asset, assetId);
    

### CreateAssetAsync(CorpusName, Asset, string, CallSettings)
    
    
    public virtual Task<Asset> CreateAssetAsync(CorpusName parent, Asset asset, string assetId, CallSettings callSettings = null)

Creates an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent resource where this asset will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`asset` | `[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)`  
Required. The asset to create.  
`assetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the asset, which will become the final component of the asset's resource name if user choose to specify. Otherwise, asset id will be generated by system. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    gcvv::Asset asset = new gcvv::Asset();
    string assetId = "";
    // Make the request
    gcvv::Asset response = await warehouseClient.CreateAssetAsync(parent, asset, assetId);
    

### CreateAssetAsync(CorpusName, Asset, string, CancellationToken)
    
    
    public virtual Task<Asset> CreateAssetAsync(CorpusName parent, Asset asset, string assetId, CancellationToken cancellationToken)

Creates an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent resource where this asset will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`asset` | `[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)`  
Required. The asset to create.  
`assetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the asset, which will become the final component of the asset's resource name if user choose to specify. Otherwise, asset id will be generated by system. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    gcvv::Asset asset = new gcvv::Asset();
    string assetId = "";
    // Make the request
    gcvv::Asset response = await warehouseClient.CreateAssetAsync(parent, asset, assetId);
    

### CreateAssetAsync(CreateAssetRequest, CallSettings)
    
    
    public virtual Task<Asset> CreateAssetAsync(CreateAssetRequest request, CallSettings callSettings = null)

Creates an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateAssetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CreateAssetRequest request = new gcvv::CreateAssetRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        Asset = new gcvv::Asset(),
        AssetId = "",
    };
    // Make the request
    gcvv::Asset response = await warehouseClient.CreateAssetAsync(request);
    

### CreateAssetAsync(CreateAssetRequest, CancellationToken)
    
    
    public virtual Task<Asset> CreateAssetAsync(CreateAssetRequest request, CancellationToken cancellationToken)

Creates an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateAssetRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CreateAssetRequest request = new gcvv::CreateAssetRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        Asset = new gcvv::Asset(),
        AssetId = "",
    };
    // Make the request
    gcvv::Asset response = await warehouseClient.CreateAssetAsync(request);
    

### CreateAssetAsync(string, Asset, string, CallSettings)
    
    
    public virtual Task<Asset> CreateAssetAsync(string parent, Asset asset, string assetId, CallSettings callSettings = null)

Creates an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this asset will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`asset` | `[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)`  
Required. The asset to create.  
`assetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the asset, which will become the final component of the asset's resource name if user choose to specify. Otherwise, asset id will be generated by system. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    gcvv::Asset asset = new gcvv::Asset();
    string assetId = "";
    // Make the request
    gcvv::Asset response = await warehouseClient.CreateAssetAsync(parent, asset, assetId);
    

### CreateAssetAsync(string, Asset, string, CancellationToken)
    
    
    public virtual Task<Asset> CreateAssetAsync(string parent, Asset asset, string assetId, CancellationToken cancellationToken)

Creates an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this asset will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`asset` | `[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)`  
Required. The asset to create.  
`assetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the asset, which will become the final component of the asset's resource name if user choose to specify. Otherwise, asset id will be generated by system. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    gcvv::Asset asset = new gcvv::Asset();
    string assetId = "";
    // Make the request
    gcvv::Asset response = await warehouseClient.CreateAssetAsync(parent, asset, assetId);
    

### CreateAsync(CancellationToken)
    
    
    public static Task<WarehouseClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [WarehouseClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.WarehouseClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [WarehouseClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.WarehouseClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[WarehouseClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.WarehouseClient)` | The task representing the created [WarehouseClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.WarehouseClient).  
  
### CreateCollection(CorpusName, Collection, string, CallSettings)
    
    
    public virtual Operation<Collection, CreateCollectionMetadata> CreateCollection(CorpusName parent, Collection collection, string collectionId, CallSettings callSettings = null)

Creates a collection.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent resource where this collection will be created. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`collection` | `[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)`  
Required. The collection resource to be created.  
`collectionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the collection, which will become the final component of the resource name if user choose to specify. Otherwise, collection id will be generated by system. This value should be up to 55 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)[CreateCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCollectionMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    gcvv::Collection collection = new gcvv::Collection();
    string collectionId = "";
    // Make the request
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> response = warehouseClient.CreateCollection(parent, collection, collectionId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::Collection result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> retrievedResponse = warehouseClient.PollOnceCreateCollection(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Collection retrievedResult = retrievedResponse.Result;
    }
    

### CreateCollection(CreateCollectionRequest, CallSettings)
    
    
    public virtual Operation<Collection, CreateCollectionMetadata> CreateCollection(CreateCollectionRequest request, CallSettings callSettings = null)

Creates a collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCollectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCollectionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)[CreateCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCollectionMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CreateCollectionRequest request = new gcvv::CreateCollectionRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        Collection = new gcvv::Collection(),
        CollectionId = "",
    };
    // Make the request
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> response = warehouseClient.CreateCollection(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::Collection result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> retrievedResponse = warehouseClient.PollOnceCreateCollection(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Collection retrievedResult = retrievedResponse.Result;
    }
    

### CreateCollection(string, Collection, string, CallSettings)
    
    
    public virtual Operation<Collection, CreateCollectionMetadata> CreateCollection(string parent, Collection collection, string collectionId, CallSettings callSettings = null)

Creates a collection.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this collection will be created. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`collection` | `[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)`  
Required. The collection resource to be created.  
`collectionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the collection, which will become the final component of the resource name if user choose to specify. Otherwise, collection id will be generated by system. This value should be up to 55 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)[CreateCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCollectionMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    gcvv::Collection collection = new gcvv::Collection();
    string collectionId = "";
    // Make the request
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> response = warehouseClient.CreateCollection(parent, collection, collectionId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::Collection result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> retrievedResponse = warehouseClient.PollOnceCreateCollection(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Collection retrievedResult = retrievedResponse.Result;
    }
    

### CreateCollectionAsync(CorpusName, Collection, string, CallSettings)
    
    
    public virtual Task<Operation<Collection, CreateCollectionMetadata>> CreateCollectionAsync(CorpusName parent, Collection collection, string collectionId, CallSettings callSettings = null)

Creates a collection.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent resource where this collection will be created. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`collection` | `[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)`  
Required. The collection resource to be created.  
`collectionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the collection, which will become the final component of the resource name if user choose to specify. Otherwise, collection id will be generated by system. This value should be up to 55 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)[CreateCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCollectionMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    gcvv::Collection collection = new gcvv::Collection();
    string collectionId = "";
    // Make the request
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> response = await warehouseClient.CreateCollectionAsync(parent, collection, collectionId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::Collection result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> retrievedResponse = await warehouseClient.PollOnceCreateCollectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Collection retrievedResult = retrievedResponse.Result;
    }
    

### CreateCollectionAsync(CorpusName, Collection, string, CancellationToken)
    
    
    public virtual Task<Operation<Collection, CreateCollectionMetadata>> CreateCollectionAsync(CorpusName parent, Collection collection, string collectionId, CancellationToken cancellationToken)

Creates a collection.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent resource where this collection will be created. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`collection` | `[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)`  
Required. The collection resource to be created.  
`collectionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the collection, which will become the final component of the resource name if user choose to specify. Otherwise, collection id will be generated by system. This value should be up to 55 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)[CreateCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCollectionMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    gcvv::Collection collection = new gcvv::Collection();
    string collectionId = "";
    // Make the request
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> response = await warehouseClient.CreateCollectionAsync(parent, collection, collectionId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::Collection result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> retrievedResponse = await warehouseClient.PollOnceCreateCollectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Collection retrievedResult = retrievedResponse.Result;
    }
    

### CreateCollectionAsync(CreateCollectionRequest, CallSettings)
    
    
    public virtual Task<Operation<Collection, CreateCollectionMetadata>> CreateCollectionAsync(CreateCollectionRequest request, CallSettings callSettings = null)

Creates a collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCollectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCollectionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)[CreateCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCollectionMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CreateCollectionRequest request = new gcvv::CreateCollectionRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        Collection = new gcvv::Collection(),
        CollectionId = "",
    };
    // Make the request
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> response = await warehouseClient.CreateCollectionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::Collection result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> retrievedResponse = await warehouseClient.PollOnceCreateCollectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Collection retrievedResult = retrievedResponse.Result;
    }
    

### CreateCollectionAsync(CreateCollectionRequest, CancellationToken)
    
    
    public virtual Task<Operation<Collection, CreateCollectionMetadata>> CreateCollectionAsync(CreateCollectionRequest request, CancellationToken cancellationToken)

Creates a collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCollectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCollectionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)[CreateCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCollectionMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CreateCollectionRequest request = new gcvv::CreateCollectionRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        Collection = new gcvv::Collection(),
        CollectionId = "",
    };
    // Make the request
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> response = await warehouseClient.CreateCollectionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::Collection result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> retrievedResponse = await warehouseClient.PollOnceCreateCollectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Collection retrievedResult = retrievedResponse.Result;
    }
    

### CreateCollectionAsync(string, Collection, string, CallSettings)
    
    
    public virtual Task<Operation<Collection, CreateCollectionMetadata>> CreateCollectionAsync(string parent, Collection collection, string collectionId, CallSettings callSettings = null)

Creates a collection.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this collection will be created. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`collection` | `[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)`  
Required. The collection resource to be created.  
`collectionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the collection, which will become the final component of the resource name if user choose to specify. Otherwise, collection id will be generated by system. This value should be up to 55 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)[CreateCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCollectionMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    gcvv::Collection collection = new gcvv::Collection();
    string collectionId = "";
    // Make the request
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> response = await warehouseClient.CreateCollectionAsync(parent, collection, collectionId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::Collection result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> retrievedResponse = await warehouseClient.PollOnceCreateCollectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Collection retrievedResult = retrievedResponse.Result;
    }
    

### CreateCollectionAsync(string, Collection, string, CancellationToken)
    
    
    public virtual Task<Operation<Collection, CreateCollectionMetadata>> CreateCollectionAsync(string parent, Collection collection, string collectionId, CancellationToken cancellationToken)

Creates a collection.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this collection will be created. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`collection` | `[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)`  
Required. The collection resource to be created.  
`collectionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the collection, which will become the final component of the resource name if user choose to specify. Otherwise, collection id will be generated by system. This value should be up to 55 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)[CreateCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCollectionMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    gcvv::Collection collection = new gcvv::Collection();
    string collectionId = "";
    // Make the request
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> response = await warehouseClient.CreateCollectionAsync(parent, collection, collectionId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::Collection result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Collection, gcvv::CreateCollectionMetadata> retrievedResponse = await warehouseClient.PollOnceCreateCollectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Collection retrievedResult = retrievedResponse.Result;
    }
    

### CreateCorpus(CreateCorpusRequest, CallSettings)
    
    
    public virtual Operation<Corpus, CreateCorpusMetadata> CreateCorpus(CreateCorpusRequest request, CallSettings callSettings = null)

Creates a corpus inside a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCorpusRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)[CreateCorpusMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCorpusMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CreateCorpusRequest request = new gcvv::CreateCorpusRequest
    {
        Parent = "",
        Corpus = new gcvv::Corpus(),
    };
    // Make the request
    Operation<gcvv::Corpus, gcvv::CreateCorpusMetadata> response = warehouseClient.CreateCorpus(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Corpus, gcvv::CreateCorpusMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::Corpus result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Corpus, gcvv::CreateCorpusMetadata> retrievedResponse = warehouseClient.PollOnceCreateCorpus(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Corpus retrievedResult = retrievedResponse.Result;
    }
    

### CreateCorpus(string, Corpus, CallSettings)
    
    
    public virtual Operation<Corpus, CreateCorpusMetadata> CreateCorpus(string parent, Corpus corpus, CallSettings callSettings = null)

Creates a corpus inside a project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Form: `projects/{project_number}/locations/{location_id}`  
`corpus` | `[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)`  
Required. The corpus to be created.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)[CreateCorpusMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCorpusMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string parent = "";
    gcvv::Corpus corpus = new gcvv::Corpus();
    // Make the request
    Operation<gcvv::Corpus, gcvv::CreateCorpusMetadata> response = warehouseClient.CreateCorpus(parent, corpus);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Corpus, gcvv::CreateCorpusMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::Corpus result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Corpus, gcvv::CreateCorpusMetadata> retrievedResponse = warehouseClient.PollOnceCreateCorpus(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Corpus retrievedResult = retrievedResponse.Result;
    }
    

### CreateCorpusAsync(CreateCorpusRequest, CallSettings)
    
    
    public virtual Task<Operation<Corpus, CreateCorpusMetadata>> CreateCorpusAsync(CreateCorpusRequest request, CallSettings callSettings = null)

Creates a corpus inside a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCorpusRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)[CreateCorpusMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCorpusMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CreateCorpusRequest request = new gcvv::CreateCorpusRequest
    {
        Parent = "",
        Corpus = new gcvv::Corpus(),
    };
    // Make the request
    Operation<gcvv::Corpus, gcvv::CreateCorpusMetadata> response = await warehouseClient.CreateCorpusAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Corpus, gcvv::CreateCorpusMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::Corpus result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Corpus, gcvv::CreateCorpusMetadata> retrievedResponse = await warehouseClient.PollOnceCreateCorpusAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Corpus retrievedResult = retrievedResponse.Result;
    }
    

### CreateCorpusAsync(CreateCorpusRequest, CancellationToken)
    
    
    public virtual Task<Operation<Corpus, CreateCorpusMetadata>> CreateCorpusAsync(CreateCorpusRequest request, CancellationToken cancellationToken)

Creates a corpus inside a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCorpusRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)[CreateCorpusMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCorpusMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CreateCorpusRequest request = new gcvv::CreateCorpusRequest
    {
        Parent = "",
        Corpus = new gcvv::Corpus(),
    };
    // Make the request
    Operation<gcvv::Corpus, gcvv::CreateCorpusMetadata> response = await warehouseClient.CreateCorpusAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Corpus, gcvv::CreateCorpusMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::Corpus result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Corpus, gcvv::CreateCorpusMetadata> retrievedResponse = await warehouseClient.PollOnceCreateCorpusAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Corpus retrievedResult = retrievedResponse.Result;
    }
    

### CreateCorpusAsync(string, Corpus, CallSettings)
    
    
    public virtual Task<Operation<Corpus, CreateCorpusMetadata>> CreateCorpusAsync(string parent, Corpus corpus, CallSettings callSettings = null)

Creates a corpus inside a project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Form: `projects/{project_number}/locations/{location_id}`  
`corpus` | `[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)`  
Required. The corpus to be created.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)[CreateCorpusMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCorpusMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "";
    gcvv::Corpus corpus = new gcvv::Corpus();
    // Make the request
    Operation<gcvv::Corpus, gcvv::CreateCorpusMetadata> response = await warehouseClient.CreateCorpusAsync(parent, corpus);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Corpus, gcvv::CreateCorpusMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::Corpus result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Corpus, gcvv::CreateCorpusMetadata> retrievedResponse = await warehouseClient.PollOnceCreateCorpusAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Corpus retrievedResult = retrievedResponse.Result;
    }
    

### CreateCorpusAsync(string, Corpus, CancellationToken)
    
    
    public virtual Task<Operation<Corpus, CreateCorpusMetadata>> CreateCorpusAsync(string parent, Corpus corpus, CancellationToken cancellationToken)

Creates a corpus inside a project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Form: `projects/{project_number}/locations/{location_id}`  
`corpus` | `[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)`  
Required. The corpus to be created.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)[CreateCorpusMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCorpusMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "";
    gcvv::Corpus corpus = new gcvv::Corpus();
    // Make the request
    Operation<gcvv::Corpus, gcvv::CreateCorpusMetadata> response = await warehouseClient.CreateCorpusAsync(parent, corpus);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Corpus, gcvv::CreateCorpusMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::Corpus result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Corpus, gcvv::CreateCorpusMetadata> retrievedResponse = await warehouseClient.PollOnceCreateCorpusAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Corpus retrievedResult = retrievedResponse.Result;
    }
    

### CreateDataSchema(CorpusName, DataSchema, CallSettings)
    
    
    public virtual DataSchema CreateDataSchema(CorpusName parent, DataSchema dataSchema, CallSettings callSettings = null)

Creates data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent resource where this data schema will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`dataSchema` | `[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)`  
Required. The data schema to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    gcvv::DataSchema dataSchema = new gcvv::DataSchema();
    // Make the request
    gcvv::DataSchema response = warehouseClient.CreateDataSchema(parent, dataSchema);
    

### CreateDataSchema(CreateDataSchemaRequest, CallSettings)
    
    
    public virtual DataSchema CreateDataSchema(CreateDataSchemaRequest request, CallSettings callSettings = null)

Creates data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateDataSchemaRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CreateDataSchemaRequest request = new gcvv::CreateDataSchemaRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        DataSchema = new gcvv::DataSchema(),
    };
    // Make the request
    gcvv::DataSchema response = warehouseClient.CreateDataSchema(request);
    

### CreateDataSchema(string, DataSchema, CallSettings)
    
    
    public virtual DataSchema CreateDataSchema(string parent, DataSchema dataSchema, CallSettings callSettings = null)

Creates data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this data schema will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`dataSchema` | `[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)`  
Required. The data schema to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    gcvv::DataSchema dataSchema = new gcvv::DataSchema();
    // Make the request
    gcvv::DataSchema response = warehouseClient.CreateDataSchema(parent, dataSchema);
    

### CreateDataSchemaAsync(CorpusName, DataSchema, CallSettings)
    
    
    public virtual Task<DataSchema> CreateDataSchemaAsync(CorpusName parent, DataSchema dataSchema, CallSettings callSettings = null)

Creates data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent resource where this data schema will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`dataSchema` | `[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)`  
Required. The data schema to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    gcvv::DataSchema dataSchema = new gcvv::DataSchema();
    // Make the request
    gcvv::DataSchema response = await warehouseClient.CreateDataSchemaAsync(parent, dataSchema);
    

### CreateDataSchemaAsync(CorpusName, DataSchema, CancellationToken)
    
    
    public virtual Task<DataSchema> CreateDataSchemaAsync(CorpusName parent, DataSchema dataSchema, CancellationToken cancellationToken)

Creates data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent resource where this data schema will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`dataSchema` | `[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)`  
Required. The data schema to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    gcvv::DataSchema dataSchema = new gcvv::DataSchema();
    // Make the request
    gcvv::DataSchema response = await warehouseClient.CreateDataSchemaAsync(parent, dataSchema);
    

### CreateDataSchemaAsync(CreateDataSchemaRequest, CallSettings)
    
    
    public virtual Task<DataSchema> CreateDataSchemaAsync(CreateDataSchemaRequest request, CallSettings callSettings = null)

Creates data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateDataSchemaRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CreateDataSchemaRequest request = new gcvv::CreateDataSchemaRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        DataSchema = new gcvv::DataSchema(),
    };
    // Make the request
    gcvv::DataSchema response = await warehouseClient.CreateDataSchemaAsync(request);
    

### CreateDataSchemaAsync(CreateDataSchemaRequest, CancellationToken)
    
    
    public virtual Task<DataSchema> CreateDataSchemaAsync(CreateDataSchemaRequest request, CancellationToken cancellationToken)

Creates data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateDataSchemaRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CreateDataSchemaRequest request = new gcvv::CreateDataSchemaRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        DataSchema = new gcvv::DataSchema(),
    };
    // Make the request
    gcvv::DataSchema response = await warehouseClient.CreateDataSchemaAsync(request);
    

### CreateDataSchemaAsync(string, DataSchema, CallSettings)
    
    
    public virtual Task<DataSchema> CreateDataSchemaAsync(string parent, DataSchema dataSchema, CallSettings callSettings = null)

Creates data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this data schema will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`dataSchema` | `[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)`  
Required. The data schema to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    gcvv::DataSchema dataSchema = new gcvv::DataSchema();
    // Make the request
    gcvv::DataSchema response = await warehouseClient.CreateDataSchemaAsync(parent, dataSchema);
    

### CreateDataSchemaAsync(string, DataSchema, CancellationToken)
    
    
    public virtual Task<DataSchema> CreateDataSchemaAsync(string parent, DataSchema dataSchema, CancellationToken cancellationToken)

Creates data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this data schema will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`dataSchema` | `[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)`  
Required. The data schema to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    gcvv::DataSchema dataSchema = new gcvv::DataSchema();
    // Make the request
    gcvv::DataSchema response = await warehouseClient.CreateDataSchemaAsync(parent, dataSchema);
    

### CreateIndex(CorpusName, Index, string, CallSettings)
    
    
    public virtual Operation<Index, CreateIndexMetadata> CreateIndex(CorpusName parent, Index index, string indexId, CallSettings callSettings = null)

Creates an Index under the corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. Value for the parent. The resource name of the Corpus under which this index is created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`index` | `[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)`  
Required. The index being created.  
`indexId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID for the index. This will become the final resource name for the index. If the user does not specify this value, it will be generated by system. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)[CreateIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    gcvv::Index index = new gcvv::Index();
    string indexId = "";
    // Make the request
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> response = warehouseClient.CreateIndex(parent, index, indexId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::Index result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> retrievedResponse = warehouseClient.PollOnceCreateIndex(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Index retrievedResult = retrievedResponse.Result;
    }
    

### CreateIndex(CreateIndexRequest, CallSettings)
    
    
    public virtual Operation<Index, CreateIndexMetadata> CreateIndex(CreateIndexRequest request, CallSettings callSettings = null)

Creates an Index under the corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)[CreateIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CreateIndexRequest request = new gcvv::CreateIndexRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        IndexId = "",
        Index = new gcvv::Index(),
    };
    // Make the request
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> response = warehouseClient.CreateIndex(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::Index result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> retrievedResponse = warehouseClient.PollOnceCreateIndex(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Index retrievedResult = retrievedResponse.Result;
    }
    

### CreateIndex(string, Index, string, CallSettings)
    
    
    public virtual Operation<Index, CreateIndexMetadata> CreateIndex(string parent, Index index, string indexId, CallSettings callSettings = null)

Creates an Index under the corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for the parent. The resource name of the Corpus under which this index is created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`index` | `[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)`  
Required. The index being created.  
`indexId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID for the index. This will become the final resource name for the index. If the user does not specify this value, it will be generated by system. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)[CreateIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    gcvv::Index index = new gcvv::Index();
    string indexId = "";
    // Make the request
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> response = warehouseClient.CreateIndex(parent, index, indexId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::Index result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> retrievedResponse = warehouseClient.PollOnceCreateIndex(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Index retrievedResult = retrievedResponse.Result;
    }
    

### CreateIndexAsync(CorpusName, Index, string, CallSettings)
    
    
    public virtual Task<Operation<Index, CreateIndexMetadata>> CreateIndexAsync(CorpusName parent, Index index, string indexId, CallSettings callSettings = null)

Creates an Index under the corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. Value for the parent. The resource name of the Corpus under which this index is created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`index` | `[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)`  
Required. The index being created.  
`indexId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID for the index. This will become the final resource name for the index. If the user does not specify this value, it will be generated by system. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)[CreateIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    gcvv::Index index = new gcvv::Index();
    string indexId = "";
    // Make the request
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> response = await warehouseClient.CreateIndexAsync(parent, index, indexId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::Index result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> retrievedResponse = await warehouseClient.PollOnceCreateIndexAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Index retrievedResult = retrievedResponse.Result;
    }
    

### CreateIndexAsync(CorpusName, Index, string, CancellationToken)
    
    
    public virtual Task<Operation<Index, CreateIndexMetadata>> CreateIndexAsync(CorpusName parent, Index index, string indexId, CancellationToken cancellationToken)

Creates an Index under the corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. Value for the parent. The resource name of the Corpus under which this index is created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`index` | `[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)`  
Required. The index being created.  
`indexId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID for the index. This will become the final resource name for the index. If the user does not specify this value, it will be generated by system. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)[CreateIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    gcvv::Index index = new gcvv::Index();
    string indexId = "";
    // Make the request
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> response = await warehouseClient.CreateIndexAsync(parent, index, indexId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::Index result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> retrievedResponse = await warehouseClient.PollOnceCreateIndexAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Index retrievedResult = retrievedResponse.Result;
    }
    

### CreateIndexAsync(CreateIndexRequest, CallSettings)
    
    
    public virtual Task<Operation<Index, CreateIndexMetadata>> CreateIndexAsync(CreateIndexRequest request, CallSettings callSettings = null)

Creates an Index under the corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)[CreateIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CreateIndexRequest request = new gcvv::CreateIndexRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        IndexId = "",
        Index = new gcvv::Index(),
    };
    // Make the request
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> response = await warehouseClient.CreateIndexAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::Index result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> retrievedResponse = await warehouseClient.PollOnceCreateIndexAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Index retrievedResult = retrievedResponse.Result;
    }
    

### CreateIndexAsync(CreateIndexRequest, CancellationToken)
    
    
    public virtual Task<Operation<Index, CreateIndexMetadata>> CreateIndexAsync(CreateIndexRequest request, CancellationToken cancellationToken)

Creates an Index under the corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)[CreateIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CreateIndexRequest request = new gcvv::CreateIndexRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        IndexId = "",
        Index = new gcvv::Index(),
    };
    // Make the request
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> response = await warehouseClient.CreateIndexAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::Index result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> retrievedResponse = await warehouseClient.PollOnceCreateIndexAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Index retrievedResult = retrievedResponse.Result;
    }
    

### CreateIndexAsync(string, Index, string, CallSettings)
    
    
    public virtual Task<Operation<Index, CreateIndexMetadata>> CreateIndexAsync(string parent, Index index, string indexId, CallSettings callSettings = null)

Creates an Index under the corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for the parent. The resource name of the Corpus under which this index is created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`index` | `[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)`  
Required. The index being created.  
`indexId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID for the index. This will become the final resource name for the index. If the user does not specify this value, it will be generated by system. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)[CreateIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    gcvv::Index index = new gcvv::Index();
    string indexId = "";
    // Make the request
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> response = await warehouseClient.CreateIndexAsync(parent, index, indexId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::Index result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> retrievedResponse = await warehouseClient.PollOnceCreateIndexAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Index retrievedResult = retrievedResponse.Result;
    }
    

### CreateIndexAsync(string, Index, string, CancellationToken)
    
    
    public virtual Task<Operation<Index, CreateIndexMetadata>> CreateIndexAsync(string parent, Index index, string indexId, CancellationToken cancellationToken)

Creates an Index under the corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Value for the parent. The resource name of the Corpus under which this index is created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`index` | `[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)`  
Required. The index being created.  
`indexId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID for the index. This will become the final resource name for the index. If the user does not specify this value, it will be generated by system. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-/. The first character must be a letter, the last could be a letter or a number.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)[CreateIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    gcvv::Index index = new gcvv::Index();
    string indexId = "";
    // Make the request
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> response = await warehouseClient.CreateIndexAsync(parent, index, indexId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::Index result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Index, gcvv::CreateIndexMetadata> retrievedResponse = await warehouseClient.PollOnceCreateIndexAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Index retrievedResult = retrievedResponse.Result;
    }
    

### CreateIndexEndpoint(LocationName, IndexEndpoint, string, CallSettings)
    
    
    public virtual Operation<IndexEndpoint, CreateIndexEndpointMetadata> CreateIndexEndpoint(LocationName parent, IndexEndpoint indexEndpoint, string indexEndpointId, CallSettings callSettings = null)

Creates an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Format: `projects/{project}/locations/{location}`  
`indexEndpoint` | `[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)`  
Required. The resource being created.  
`indexEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the IndexEndpoint, which will become the final component of the IndexEndpoint's resource name if the user specifies it. Otherwise, IndexEndpoint id will be autogenerated. This value should be up to 63 characters, and valid characters are a-z, 0-9 and dash (-). The first character must be a letter, the last must be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)[CreateIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexEndpointMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    gcvv::IndexEndpoint indexEndpoint = new gcvv::IndexEndpoint();
    string indexEndpointId = "";
    // Make the request
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> response = warehouseClient.CreateIndexEndpoint(parent, indexEndpoint, indexEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::IndexEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> retrievedResponse = warehouseClient.PollOnceCreateIndexEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::IndexEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateIndexEndpoint(CreateIndexEndpointRequest, CallSettings)
    
    
    public virtual Operation<IndexEndpoint, CreateIndexEndpointMetadata> CreateIndexEndpoint(CreateIndexEndpointRequest request, CallSettings callSettings = null)

Creates an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateIndexEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)[CreateIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexEndpointMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CreateIndexEndpointRequest request = new gcvv::CreateIndexEndpointRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        IndexEndpointId = "",
        IndexEndpoint = new gcvv::IndexEndpoint(),
    };
    // Make the request
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> response = warehouseClient.CreateIndexEndpoint(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::IndexEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> retrievedResponse = warehouseClient.PollOnceCreateIndexEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::IndexEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateIndexEndpoint(string, IndexEndpoint, string, CallSettings)
    
    
    public virtual Operation<IndexEndpoint, CreateIndexEndpointMetadata> CreateIndexEndpoint(string parent, IndexEndpoint indexEndpoint, string indexEndpointId, CallSettings callSettings = null)

Creates an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `projects/{project}/locations/{location}`  
`indexEndpoint` | `[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)`  
Required. The resource being created.  
`indexEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the IndexEndpoint, which will become the final component of the IndexEndpoint's resource name if the user specifies it. Otherwise, IndexEndpoint id will be autogenerated. This value should be up to 63 characters, and valid characters are a-z, 0-9 and dash (-). The first character must be a letter, the last must be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)[CreateIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexEndpointMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    gcvv::IndexEndpoint indexEndpoint = new gcvv::IndexEndpoint();
    string indexEndpointId = "";
    // Make the request
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> response = warehouseClient.CreateIndexEndpoint(parent, indexEndpoint, indexEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::IndexEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> retrievedResponse = warehouseClient.PollOnceCreateIndexEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::IndexEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateIndexEndpointAsync(LocationName, IndexEndpoint, string, CallSettings)
    
    
    public virtual Task<Operation<IndexEndpoint, CreateIndexEndpointMetadata>> CreateIndexEndpointAsync(LocationName parent, IndexEndpoint indexEndpoint, string indexEndpointId, CallSettings callSettings = null)

Creates an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Format: `projects/{project}/locations/{location}`  
`indexEndpoint` | `[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)`  
Required. The resource being created.  
`indexEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the IndexEndpoint, which will become the final component of the IndexEndpoint's resource name if the user specifies it. Otherwise, IndexEndpoint id will be autogenerated. This value should be up to 63 characters, and valid characters are a-z, 0-9 and dash (-). The first character must be a letter, the last must be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)[CreateIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexEndpointMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    gcvv::IndexEndpoint indexEndpoint = new gcvv::IndexEndpoint();
    string indexEndpointId = "";
    // Make the request
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> response = await warehouseClient.CreateIndexEndpointAsync(parent, indexEndpoint, indexEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::IndexEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> retrievedResponse = await warehouseClient.PollOnceCreateIndexEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::IndexEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateIndexEndpointAsync(LocationName, IndexEndpoint, string, CancellationToken)
    
    
    public virtual Task<Operation<IndexEndpoint, CreateIndexEndpointMetadata>> CreateIndexEndpointAsync(LocationName parent, IndexEndpoint indexEndpoint, string indexEndpointId, CancellationToken cancellationToken)

Creates an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Format: `projects/{project}/locations/{location}`  
`indexEndpoint` | `[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)`  
Required. The resource being created.  
`indexEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the IndexEndpoint, which will become the final component of the IndexEndpoint's resource name if the user specifies it. Otherwise, IndexEndpoint id will be autogenerated. This value should be up to 63 characters, and valid characters are a-z, 0-9 and dash (-). The first character must be a letter, the last must be a letter or a number.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)[CreateIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexEndpointMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    gcvv::IndexEndpoint indexEndpoint = new gcvv::IndexEndpoint();
    string indexEndpointId = "";
    // Make the request
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> response = await warehouseClient.CreateIndexEndpointAsync(parent, indexEndpoint, indexEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::IndexEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> retrievedResponse = await warehouseClient.PollOnceCreateIndexEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::IndexEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateIndexEndpointAsync(CreateIndexEndpointRequest, CallSettings)
    
    
    public virtual Task<Operation<IndexEndpoint, CreateIndexEndpointMetadata>> CreateIndexEndpointAsync(CreateIndexEndpointRequest request, CallSettings callSettings = null)

Creates an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateIndexEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)[CreateIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexEndpointMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CreateIndexEndpointRequest request = new gcvv::CreateIndexEndpointRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        IndexEndpointId = "",
        IndexEndpoint = new gcvv::IndexEndpoint(),
    };
    // Make the request
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> response = await warehouseClient.CreateIndexEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::IndexEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> retrievedResponse = await warehouseClient.PollOnceCreateIndexEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::IndexEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateIndexEndpointAsync(CreateIndexEndpointRequest, CancellationToken)
    
    
    public virtual Task<Operation<IndexEndpoint, CreateIndexEndpointMetadata>> CreateIndexEndpointAsync(CreateIndexEndpointRequest request, CancellationToken cancellationToken)

Creates an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateIndexEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)[CreateIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexEndpointMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CreateIndexEndpointRequest request = new gcvv::CreateIndexEndpointRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        IndexEndpointId = "",
        IndexEndpoint = new gcvv::IndexEndpoint(),
    };
    // Make the request
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> response = await warehouseClient.CreateIndexEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::IndexEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> retrievedResponse = await warehouseClient.PollOnceCreateIndexEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::IndexEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateIndexEndpointAsync(string, IndexEndpoint, string, CallSettings)
    
    
    public virtual Task<Operation<IndexEndpoint, CreateIndexEndpointMetadata>> CreateIndexEndpointAsync(string parent, IndexEndpoint indexEndpoint, string indexEndpointId, CallSettings callSettings = null)

Creates an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `projects/{project}/locations/{location}`  
`indexEndpoint` | `[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)`  
Required. The resource being created.  
`indexEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the IndexEndpoint, which will become the final component of the IndexEndpoint's resource name if the user specifies it. Otherwise, IndexEndpoint id will be autogenerated. This value should be up to 63 characters, and valid characters are a-z, 0-9 and dash (-). The first character must be a letter, the last must be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)[CreateIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexEndpointMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    gcvv::IndexEndpoint indexEndpoint = new gcvv::IndexEndpoint();
    string indexEndpointId = "";
    // Make the request
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> response = await warehouseClient.CreateIndexEndpointAsync(parent, indexEndpoint, indexEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::IndexEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> retrievedResponse = await warehouseClient.PollOnceCreateIndexEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::IndexEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateIndexEndpointAsync(string, IndexEndpoint, string, CancellationToken)
    
    
    public virtual Task<Operation<IndexEndpoint, CreateIndexEndpointMetadata>> CreateIndexEndpointAsync(string parent, IndexEndpoint indexEndpoint, string indexEndpointId, CancellationToken cancellationToken)

Creates an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `projects/{project}/locations/{location}`  
`indexEndpoint` | `[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)`  
Required. The resource being created.  
`indexEndpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The ID to use for the IndexEndpoint, which will become the final component of the IndexEndpoint's resource name if the user specifies it. Otherwise, IndexEndpoint id will be autogenerated. This value should be up to 63 characters, and valid characters are a-z, 0-9 and dash (-). The first character must be a letter, the last must be a letter or a number.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)[CreateIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexEndpointMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    gcvv::IndexEndpoint indexEndpoint = new gcvv::IndexEndpoint();
    string indexEndpointId = "";
    // Make the request
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> response = await warehouseClient.CreateIndexEndpointAsync(parent, indexEndpoint, indexEndpointId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::IndexEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::IndexEndpoint, gcvv::CreateIndexEndpointMetadata> retrievedResponse = await warehouseClient.PollOnceCreateIndexEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::IndexEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### CreateSearchConfig(CorpusName, SearchConfig, string, CallSettings)
    
    
    public virtual SearchConfig CreateSearchConfig(CorpusName parent, SearchConfig searchConfig, string searchConfigId, CallSettings callSettings = null)

Creates a search configuration inside a corpus.

Please follow the rules below to create a valid CreateSearchConfigRequest. \--- General Rules ---

  1. Request.search_config_id must not be associated with an existing SearchConfig.
  2. Request must contain at least one non-empty search_criteria_property or facet_property.
  3. mapped_fields must not be empty, and must map to existing UGA keys.
  4. All mapped_fields must be of the same type.
  5. All mapped_fields must share the same granularity.
  6. All mapped_fields must share the same semantic SearchConfig match options. For property-specific rules, please reference the comments for FacetProperty and SearchCriteriaProperty.



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent resource where this search configuration will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`searchConfig` | `[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)`  
Required. The search config to create.  
`searchConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID to use for the new search config. Will become the final component of the SearchConfig's resource name. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-_/. The first character must be a letter, the last could be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    gcvv::SearchConfig searchConfig = new gcvv::SearchConfig();
    string searchConfigId = "";
    // Make the request
    gcvv::SearchConfig response = warehouseClient.CreateSearchConfig(parent, searchConfig, searchConfigId);
    

### CreateSearchConfig(CreateSearchConfigRequest, CallSettings)
    
    
    public virtual SearchConfig CreateSearchConfig(CreateSearchConfigRequest request, CallSettings callSettings = null)

Creates a search configuration inside a corpus.

Please follow the rules below to create a valid CreateSearchConfigRequest. \--- General Rules ---

  1. Request.search_config_id must not be associated with an existing SearchConfig.
  2. Request must contain at least one non-empty search_criteria_property or facet_property.
  3. mapped_fields must not be empty, and must map to existing UGA keys.
  4. All mapped_fields must be of the same type.
  5. All mapped_fields must share the same granularity.
  6. All mapped_fields must share the same semantic SearchConfig match options. For property-specific rules, please reference the comments for FacetProperty and SearchCriteriaProperty.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSearchConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateSearchConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CreateSearchConfigRequest request = new gcvv::CreateSearchConfigRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        SearchConfig = new gcvv::SearchConfig(),
        SearchConfigId = "",
    };
    // Make the request
    gcvv::SearchConfig response = warehouseClient.CreateSearchConfig(request);
    

### CreateSearchConfig(string, SearchConfig, string, CallSettings)
    
    
    public virtual SearchConfig CreateSearchConfig(string parent, SearchConfig searchConfig, string searchConfigId, CallSettings callSettings = null)

Creates a search configuration inside a corpus.

Please follow the rules below to create a valid CreateSearchConfigRequest. \--- General Rules ---

  1. Request.search_config_id must not be associated with an existing SearchConfig.
  2. Request must contain at least one non-empty search_criteria_property or facet_property.
  3. mapped_fields must not be empty, and must map to existing UGA keys.
  4. All mapped_fields must be of the same type.
  5. All mapped_fields must share the same granularity.
  6. All mapped_fields must share the same semantic SearchConfig match options. For property-specific rules, please reference the comments for FacetProperty and SearchCriteriaProperty.



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this search configuration will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`searchConfig` | `[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)`  
Required. The search config to create.  
`searchConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID to use for the new search config. Will become the final component of the SearchConfig's resource name. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-_/. The first character must be a letter, the last could be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    gcvv::SearchConfig searchConfig = new gcvv::SearchConfig();
    string searchConfigId = "";
    // Make the request
    gcvv::SearchConfig response = warehouseClient.CreateSearchConfig(parent, searchConfig, searchConfigId);
    

### CreateSearchConfigAsync(CorpusName, SearchConfig, string, CallSettings)
    
    
    public virtual Task<SearchConfig> CreateSearchConfigAsync(CorpusName parent, SearchConfig searchConfig, string searchConfigId, CallSettings callSettings = null)

Creates a search configuration inside a corpus.

Please follow the rules below to create a valid CreateSearchConfigRequest. \--- General Rules ---

  1. Request.search_config_id must not be associated with an existing SearchConfig.
  2. Request must contain at least one non-empty search_criteria_property or facet_property.
  3. mapped_fields must not be empty, and must map to existing UGA keys.
  4. All mapped_fields must be of the same type.
  5. All mapped_fields must share the same granularity.
  6. All mapped_fields must share the same semantic SearchConfig match options. For property-specific rules, please reference the comments for FacetProperty and SearchCriteriaProperty.



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent resource where this search configuration will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`searchConfig` | `[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)`  
Required. The search config to create.  
`searchConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID to use for the new search config. Will become the final component of the SearchConfig's resource name. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-_/. The first character must be a letter, the last could be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    gcvv::SearchConfig searchConfig = new gcvv::SearchConfig();
    string searchConfigId = "";
    // Make the request
    gcvv::SearchConfig response = await warehouseClient.CreateSearchConfigAsync(parent, searchConfig, searchConfigId);
    

### CreateSearchConfigAsync(CorpusName, SearchConfig, string, CancellationToken)
    
    
    public virtual Task<SearchConfig> CreateSearchConfigAsync(CorpusName parent, SearchConfig searchConfig, string searchConfigId, CancellationToken cancellationToken)

Creates a search configuration inside a corpus.

Please follow the rules below to create a valid CreateSearchConfigRequest. \--- General Rules ---

  1. Request.search_config_id must not be associated with an existing SearchConfig.
  2. Request must contain at least one non-empty search_criteria_property or facet_property.
  3. mapped_fields must not be empty, and must map to existing UGA keys.
  4. All mapped_fields must be of the same type.
  5. All mapped_fields must share the same granularity.
  6. All mapped_fields must share the same semantic SearchConfig match options. For property-specific rules, please reference the comments for FacetProperty and SearchCriteriaProperty.



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent resource where this search configuration will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`searchConfig` | `[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)`  
Required. The search config to create.  
`searchConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID to use for the new search config. Will become the final component of the SearchConfig's resource name. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-_/. The first character must be a letter, the last could be a letter or a number.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    gcvv::SearchConfig searchConfig = new gcvv::SearchConfig();
    string searchConfigId = "";
    // Make the request
    gcvv::SearchConfig response = await warehouseClient.CreateSearchConfigAsync(parent, searchConfig, searchConfigId);
    

### CreateSearchConfigAsync(CreateSearchConfigRequest, CallSettings)
    
    
    public virtual Task<SearchConfig> CreateSearchConfigAsync(CreateSearchConfigRequest request, CallSettings callSettings = null)

Creates a search configuration inside a corpus.

Please follow the rules below to create a valid CreateSearchConfigRequest. \--- General Rules ---

  1. Request.search_config_id must not be associated with an existing SearchConfig.
  2. Request must contain at least one non-empty search_criteria_property or facet_property.
  3. mapped_fields must not be empty, and must map to existing UGA keys.
  4. All mapped_fields must be of the same type.
  5. All mapped_fields must share the same granularity.
  6. All mapped_fields must share the same semantic SearchConfig match options. For property-specific rules, please reference the comments for FacetProperty and SearchCriteriaProperty.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSearchConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateSearchConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CreateSearchConfigRequest request = new gcvv::CreateSearchConfigRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        SearchConfig = new gcvv::SearchConfig(),
        SearchConfigId = "",
    };
    // Make the request
    gcvv::SearchConfig response = await warehouseClient.CreateSearchConfigAsync(request);
    

### CreateSearchConfigAsync(CreateSearchConfigRequest, CancellationToken)
    
    
    public virtual Task<SearchConfig> CreateSearchConfigAsync(CreateSearchConfigRequest request, CancellationToken cancellationToken)

Creates a search configuration inside a corpus.

Please follow the rules below to create a valid CreateSearchConfigRequest. \--- General Rules ---

  1. Request.search_config_id must not be associated with an existing SearchConfig.
  2. Request must contain at least one non-empty search_criteria_property or facet_property.
  3. mapped_fields must not be empty, and must map to existing UGA keys.
  4. All mapped_fields must be of the same type.
  5. All mapped_fields must share the same granularity.
  6. All mapped_fields must share the same semantic SearchConfig match options. For property-specific rules, please reference the comments for FacetProperty and SearchCriteriaProperty.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSearchConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateSearchConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CreateSearchConfigRequest request = new gcvv::CreateSearchConfigRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        SearchConfig = new gcvv::SearchConfig(),
        SearchConfigId = "",
    };
    // Make the request
    gcvv::SearchConfig response = await warehouseClient.CreateSearchConfigAsync(request);
    

### CreateSearchConfigAsync(string, SearchConfig, string, CallSettings)
    
    
    public virtual Task<SearchConfig> CreateSearchConfigAsync(string parent, SearchConfig searchConfig, string searchConfigId, CallSettings callSettings = null)

Creates a search configuration inside a corpus.

Please follow the rules below to create a valid CreateSearchConfigRequest. \--- General Rules ---

  1. Request.search_config_id must not be associated with an existing SearchConfig.
  2. Request must contain at least one non-empty search_criteria_property or facet_property.
  3. mapped_fields must not be empty, and must map to existing UGA keys.
  4. All mapped_fields must be of the same type.
  5. All mapped_fields must share the same granularity.
  6. All mapped_fields must share the same semantic SearchConfig match options. For property-specific rules, please reference the comments for FacetProperty and SearchCriteriaProperty.



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this search configuration will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`searchConfig` | `[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)`  
Required. The search config to create.  
`searchConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID to use for the new search config. Will become the final component of the SearchConfig's resource name. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-_/. The first character must be a letter, the last could be a letter or a number.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    gcvv::SearchConfig searchConfig = new gcvv::SearchConfig();
    string searchConfigId = "";
    // Make the request
    gcvv::SearchConfig response = await warehouseClient.CreateSearchConfigAsync(parent, searchConfig, searchConfigId);
    

### CreateSearchConfigAsync(string, SearchConfig, string, CancellationToken)
    
    
    public virtual Task<SearchConfig> CreateSearchConfigAsync(string parent, SearchConfig searchConfig, string searchConfigId, CancellationToken cancellationToken)

Creates a search configuration inside a corpus.

Please follow the rules below to create a valid CreateSearchConfigRequest. \--- General Rules ---

  1. Request.search_config_id must not be associated with an existing SearchConfig.
  2. Request must contain at least one non-empty search_criteria_property or facet_property.
  3. mapped_fields must not be empty, and must map to existing UGA keys.
  4. All mapped_fields must be of the same type.
  5. All mapped_fields must share the same granularity.
  6. All mapped_fields must share the same semantic SearchConfig match options. For property-specific rules, please reference the comments for FacetProperty and SearchCriteriaProperty.



**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this search configuration will be created. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`searchConfig` | `[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)`  
Required. The search config to create.  
`searchConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. ID to use for the new search config. Will become the final component of the SearchConfig's resource name. This value should be up to 63 characters, and valid characters are /[a-z][0-9]-_/. The first character must be a letter, the last could be a letter or a number.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    gcvv::SearchConfig searchConfig = new gcvv::SearchConfig();
    string searchConfigId = "";
    // Make the request
    gcvv::SearchConfig response = await warehouseClient.CreateSearchConfigAsync(parent, searchConfig, searchConfigId);
    

### CreateSearchHypernym(CorpusName, SearchHypernym, string, CallSettings)
    
    
    public virtual SearchHypernym CreateSearchHypernym(CorpusName parent, SearchHypernym searchHypernym, string searchHypernymId, CallSettings callSettings = null)

Creates a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent resource where this SearchHypernym will be created. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`searchHypernym` | `[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)`  
Required. The SearchHypernym to create.  
`searchHypernymId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The search hypernym id. If omitted, a random UUID will be generated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    gcvv::SearchHypernym searchHypernym = new gcvv::SearchHypernym();
    string searchHypernymId = "";
    // Make the request
    gcvv::SearchHypernym response = warehouseClient.CreateSearchHypernym(parent, searchHypernym, searchHypernymId);
    

### CreateSearchHypernym(CreateSearchHypernymRequest, CallSettings)
    
    
    public virtual SearchHypernym CreateSearchHypernym(CreateSearchHypernymRequest request, CallSettings callSettings = null)

Creates a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSearchHypernymRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateSearchHypernymRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CreateSearchHypernymRequest request = new gcvv::CreateSearchHypernymRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        SearchHypernym = new gcvv::SearchHypernym(),
        SearchHypernymId = "",
    };
    // Make the request
    gcvv::SearchHypernym response = warehouseClient.CreateSearchHypernym(request);
    

### CreateSearchHypernym(string, SearchHypernym, string, CallSettings)
    
    
    public virtual SearchHypernym CreateSearchHypernym(string parent, SearchHypernym searchHypernym, string searchHypernymId, CallSettings callSettings = null)

Creates a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this SearchHypernym will be created. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`searchHypernym` | `[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)`  
Required. The SearchHypernym to create.  
`searchHypernymId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The search hypernym id. If omitted, a random UUID will be generated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    gcvv::SearchHypernym searchHypernym = new gcvv::SearchHypernym();
    string searchHypernymId = "";
    // Make the request
    gcvv::SearchHypernym response = warehouseClient.CreateSearchHypernym(parent, searchHypernym, searchHypernymId);
    

### CreateSearchHypernymAsync(CorpusName, SearchHypernym, string, CallSettings)
    
    
    public virtual Task<SearchHypernym> CreateSearchHypernymAsync(CorpusName parent, SearchHypernym searchHypernym, string searchHypernymId, CallSettings callSettings = null)

Creates a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent resource where this SearchHypernym will be created. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`searchHypernym` | `[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)`  
Required. The SearchHypernym to create.  
`searchHypernymId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The search hypernym id. If omitted, a random UUID will be generated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    gcvv::SearchHypernym searchHypernym = new gcvv::SearchHypernym();
    string searchHypernymId = "";
    // Make the request
    gcvv::SearchHypernym response = await warehouseClient.CreateSearchHypernymAsync(parent, searchHypernym, searchHypernymId);
    

### CreateSearchHypernymAsync(CorpusName, SearchHypernym, string, CancellationToken)
    
    
    public virtual Task<SearchHypernym> CreateSearchHypernymAsync(CorpusName parent, SearchHypernym searchHypernym, string searchHypernymId, CancellationToken cancellationToken)

Creates a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent resource where this SearchHypernym will be created. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`searchHypernym` | `[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)`  
Required. The SearchHypernym to create.  
`searchHypernymId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The search hypernym id. If omitted, a random UUID will be generated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    gcvv::SearchHypernym searchHypernym = new gcvv::SearchHypernym();
    string searchHypernymId = "";
    // Make the request
    gcvv::SearchHypernym response = await warehouseClient.CreateSearchHypernymAsync(parent, searchHypernym, searchHypernymId);
    

### CreateSearchHypernymAsync(CreateSearchHypernymRequest, CallSettings)
    
    
    public virtual Task<SearchHypernym> CreateSearchHypernymAsync(CreateSearchHypernymRequest request, CallSettings callSettings = null)

Creates a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSearchHypernymRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateSearchHypernymRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CreateSearchHypernymRequest request = new gcvv::CreateSearchHypernymRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        SearchHypernym = new gcvv::SearchHypernym(),
        SearchHypernymId = "",
    };
    // Make the request
    gcvv::SearchHypernym response = await warehouseClient.CreateSearchHypernymAsync(request);
    

### CreateSearchHypernymAsync(CreateSearchHypernymRequest, CancellationToken)
    
    
    public virtual Task<SearchHypernym> CreateSearchHypernymAsync(CreateSearchHypernymRequest request, CancellationToken cancellationToken)

Creates a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSearchHypernymRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateSearchHypernymRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CreateSearchHypernymRequest request = new gcvv::CreateSearchHypernymRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        SearchHypernym = new gcvv::SearchHypernym(),
        SearchHypernymId = "",
    };
    // Make the request
    gcvv::SearchHypernym response = await warehouseClient.CreateSearchHypernymAsync(request);
    

### CreateSearchHypernymAsync(string, SearchHypernym, string, CallSettings)
    
    
    public virtual Task<SearchHypernym> CreateSearchHypernymAsync(string parent, SearchHypernym searchHypernym, string searchHypernymId, CallSettings callSettings = null)

Creates a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this SearchHypernym will be created. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`searchHypernym` | `[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)`  
Required. The SearchHypernym to create.  
`searchHypernymId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The search hypernym id. If omitted, a random UUID will be generated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    gcvv::SearchHypernym searchHypernym = new gcvv::SearchHypernym();
    string searchHypernymId = "";
    // Make the request
    gcvv::SearchHypernym response = await warehouseClient.CreateSearchHypernymAsync(parent, searchHypernym, searchHypernymId);
    

### CreateSearchHypernymAsync(string, SearchHypernym, string, CancellationToken)
    
    
    public virtual Task<SearchHypernym> CreateSearchHypernymAsync(string parent, SearchHypernym searchHypernym, string searchHypernymId, CancellationToken cancellationToken)

Creates a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource where this SearchHypernym will be created. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`searchHypernym` | `[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)`  
Required. The SearchHypernym to create.  
`searchHypernymId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The search hypernym id. If omitted, a random UUID will be generated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    gcvv::SearchHypernym searchHypernym = new gcvv::SearchHypernym();
    string searchHypernymId = "";
    // Make the request
    gcvv::SearchHypernym response = await warehouseClient.CreateSearchHypernymAsync(parent, searchHypernym, searchHypernymId);
    

### DeleteAnnotation(AnnotationName, CallSettings)
    
    
    public virtual void DeleteAnnotation(AnnotationName name, CallSettings callSettings = null)

Deletes annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AnnotationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnnotationName)`  
Required. The name of the annotation to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}/annotations/{annotation}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::AnnotationName name = gcvv::AnnotationName.FromProjectNumberLocationCorpusAssetAnnotation("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]", "[ANNOTATION]");
    // Make the request
    warehouseClient.DeleteAnnotation(name);
    

### DeleteAnnotation(DeleteAnnotationRequest, CallSettings)
    
    
    public virtual void DeleteAnnotation(DeleteAnnotationRequest request, CallSettings callSettings = null)

Deletes annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAnnotationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAnnotationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::DeleteAnnotationRequest request = new gcvv::DeleteAnnotationRequest
    {
        AnnotationName = gcvv::AnnotationName.FromProjectNumberLocationCorpusAssetAnnotation("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]", "[ANNOTATION]"),
    };
    // Make the request
    warehouseClient.DeleteAnnotation(request);
    

### DeleteAnnotation(string, CallSettings)
    
    
    public virtual void DeleteAnnotation(string name, CallSettings callSettings = null)

Deletes annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the annotation to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}/annotations/{annotation}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/assets/[ASSET]/annotations/[ANNOTATION]";
    // Make the request
    warehouseClient.DeleteAnnotation(name);
    

### DeleteAnnotationAsync(AnnotationName, CallSettings)
    
    
    public virtual Task DeleteAnnotationAsync(AnnotationName name, CallSettings callSettings = null)

Deletes annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AnnotationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnnotationName)`  
Required. The name of the annotation to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}/annotations/{annotation}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::AnnotationName name = gcvv::AnnotationName.FromProjectNumberLocationCorpusAssetAnnotation("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]", "[ANNOTATION]");
    // Make the request
    await warehouseClient.DeleteAnnotationAsync(name);
    

### DeleteAnnotationAsync(AnnotationName, CancellationToken)
    
    
    public virtual Task DeleteAnnotationAsync(AnnotationName name, CancellationToken cancellationToken)

Deletes annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AnnotationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnnotationName)`  
Required. The name of the annotation to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}/annotations/{annotation}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::AnnotationName name = gcvv::AnnotationName.FromProjectNumberLocationCorpusAssetAnnotation("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]", "[ANNOTATION]");
    // Make the request
    await warehouseClient.DeleteAnnotationAsync(name);
    

### DeleteAnnotationAsync(DeleteAnnotationRequest, CallSettings)
    
    
    public virtual Task DeleteAnnotationAsync(DeleteAnnotationRequest request, CallSettings callSettings = null)

Deletes annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAnnotationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAnnotationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DeleteAnnotationRequest request = new gcvv::DeleteAnnotationRequest
    {
        AnnotationName = gcvv::AnnotationName.FromProjectNumberLocationCorpusAssetAnnotation("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]", "[ANNOTATION]"),
    };
    // Make the request
    await warehouseClient.DeleteAnnotationAsync(request);
    

### DeleteAnnotationAsync(DeleteAnnotationRequest, CancellationToken)
    
    
    public virtual Task DeleteAnnotationAsync(DeleteAnnotationRequest request, CancellationToken cancellationToken)

Deletes annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAnnotationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAnnotationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DeleteAnnotationRequest request = new gcvv::DeleteAnnotationRequest
    {
        AnnotationName = gcvv::AnnotationName.FromProjectNumberLocationCorpusAssetAnnotation("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]", "[ANNOTATION]"),
    };
    // Make the request
    await warehouseClient.DeleteAnnotationAsync(request);
    

### DeleteAnnotationAsync(string, CallSettings)
    
    
    public virtual Task DeleteAnnotationAsync(string name, CallSettings callSettings = null)

Deletes annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the annotation to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}/annotations/{annotation}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/assets/[ASSET]/annotations/[ANNOTATION]";
    // Make the request
    await warehouseClient.DeleteAnnotationAsync(name);
    

### DeleteAnnotationAsync(string, CancellationToken)
    
    
    public virtual Task DeleteAnnotationAsync(string name, CancellationToken cancellationToken)

Deletes annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the annotation to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}/annotations/{annotation}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/assets/[ASSET]/annotations/[ANNOTATION]";
    // Make the request
    await warehouseClient.DeleteAnnotationAsync(name);
    

### DeleteAsset(AssetName, CallSettings)
    
    
    public virtual Operation<Empty, DeleteAssetMetadata> DeleteAsset(AssetName name, CallSettings callSettings = null)

Deletes asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AssetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AssetName)`  
Required. The name of the asset to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAssetMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::AssetName name = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]");
    // Make the request
    Operation<Empty, gcvv::DeleteAssetMetadata> response = warehouseClient.DeleteAsset(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteAssetMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteAssetMetadata> retrievedResponse = warehouseClient.PollOnceDeleteAsset(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAsset(DeleteAssetRequest, CallSettings)
    
    
    public virtual Operation<Empty, DeleteAssetMetadata> DeleteAsset(DeleteAssetRequest request, CallSettings callSettings = null)

Deletes asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAssetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAssetMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::DeleteAssetRequest request = new gcvv::DeleteAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
    };
    // Make the request
    Operation<Empty, gcvv::DeleteAssetMetadata> response = warehouseClient.DeleteAsset(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteAssetMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteAssetMetadata> retrievedResponse = warehouseClient.PollOnceDeleteAsset(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAsset(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteAssetMetadata> DeleteAsset(string name, CallSettings callSettings = null)

Deletes asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the asset to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAssetMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/assets/[ASSET]";
    // Make the request
    Operation<Empty, gcvv::DeleteAssetMetadata> response = warehouseClient.DeleteAsset(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteAssetMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteAssetMetadata> retrievedResponse = warehouseClient.PollOnceDeleteAsset(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAssetAsync(AssetName, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteAssetMetadata>> DeleteAssetAsync(AssetName name, CallSettings callSettings = null)

Deletes asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AssetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AssetName)`  
Required. The name of the asset to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAssetMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::AssetName name = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]");
    // Make the request
    Operation<Empty, gcvv::DeleteAssetMetadata> response = await warehouseClient.DeleteAssetAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteAssetMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteAssetMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteAssetAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAssetAsync(AssetName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteAssetMetadata>> DeleteAssetAsync(AssetName name, CancellationToken cancellationToken)

Deletes asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AssetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AssetName)`  
Required. The name of the asset to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAssetMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::AssetName name = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]");
    // Make the request
    Operation<Empty, gcvv::DeleteAssetMetadata> response = await warehouseClient.DeleteAssetAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteAssetMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteAssetMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteAssetAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAssetAsync(DeleteAssetRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteAssetMetadata>> DeleteAssetAsync(DeleteAssetRequest request, CallSettings callSettings = null)

Deletes asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAssetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAssetMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DeleteAssetRequest request = new gcvv::DeleteAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
    };
    // Make the request
    Operation<Empty, gcvv::DeleteAssetMetadata> response = await warehouseClient.DeleteAssetAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteAssetMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteAssetMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteAssetAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAssetAsync(DeleteAssetRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteAssetMetadata>> DeleteAssetAsync(DeleteAssetRequest request, CancellationToken cancellationToken)

Deletes asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAssetRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAssetMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DeleteAssetRequest request = new gcvv::DeleteAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
    };
    // Make the request
    Operation<Empty, gcvv::DeleteAssetMetadata> response = await warehouseClient.DeleteAssetAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteAssetMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteAssetMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteAssetAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAssetAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteAssetMetadata>> DeleteAssetAsync(string name, CallSettings callSettings = null)

Deletes asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the asset to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAssetMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/assets/[ASSET]";
    // Make the request
    Operation<Empty, gcvv::DeleteAssetMetadata> response = await warehouseClient.DeleteAssetAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteAssetMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteAssetMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteAssetAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteAssetAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteAssetMetadata>> DeleteAssetAsync(string name, CancellationToken cancellationToken)

Deletes asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the asset to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAssetMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/assets/[ASSET]";
    // Make the request
    Operation<Empty, gcvv::DeleteAssetMetadata> response = await warehouseClient.DeleteAssetAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteAssetMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteAssetMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteAssetAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteCollection(CollectionName, CallSettings)
    
    
    public virtual Operation<Empty, DeleteCollectionMetadata> DeleteCollection(CollectionName name, CallSettings callSettings = null)

Deletes a collection.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CollectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionName)`  
Required. The name of the collection to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteCollectionMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CollectionName name = gcvv::CollectionName.FromProjectNumberLocationCorpusCollection("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[COLLECTION]");
    // Make the request
    Operation<Empty, gcvv::DeleteCollectionMetadata> response = warehouseClient.DeleteCollection(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteCollectionMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteCollectionMetadata> retrievedResponse = warehouseClient.PollOnceDeleteCollection(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteCollection(DeleteCollectionRequest, CallSettings)
    
    
    public virtual Operation<Empty, DeleteCollectionMetadata> DeleteCollection(DeleteCollectionRequest request, CallSettings callSettings = null)

Deletes a collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCollectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteCollectionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteCollectionMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::DeleteCollectionRequest request = new gcvv::DeleteCollectionRequest
    {
        CollectionName = gcvv::CollectionName.FromProjectNumberLocationCorpusCollection("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[COLLECTION]"),
    };
    // Make the request
    Operation<Empty, gcvv::DeleteCollectionMetadata> response = warehouseClient.DeleteCollection(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteCollectionMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteCollectionMetadata> retrievedResponse = warehouseClient.PollOnceDeleteCollection(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteCollection(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteCollectionMetadata> DeleteCollection(string name, CallSettings callSettings = null)

Deletes a collection.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the collection to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteCollectionMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/collections/[COLLECTION]";
    // Make the request
    Operation<Empty, gcvv::DeleteCollectionMetadata> response = warehouseClient.DeleteCollection(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteCollectionMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteCollectionMetadata> retrievedResponse = warehouseClient.PollOnceDeleteCollection(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteCollectionAsync(CollectionName, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteCollectionMetadata>> DeleteCollectionAsync(CollectionName name, CallSettings callSettings = null)

Deletes a collection.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CollectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionName)`  
Required. The name of the collection to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteCollectionMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CollectionName name = gcvv::CollectionName.FromProjectNumberLocationCorpusCollection("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[COLLECTION]");
    // Make the request
    Operation<Empty, gcvv::DeleteCollectionMetadata> response = await warehouseClient.DeleteCollectionAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteCollectionMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteCollectionMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteCollectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteCollectionAsync(CollectionName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteCollectionMetadata>> DeleteCollectionAsync(CollectionName name, CancellationToken cancellationToken)

Deletes a collection.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CollectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionName)`  
Required. The name of the collection to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteCollectionMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CollectionName name = gcvv::CollectionName.FromProjectNumberLocationCorpusCollection("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[COLLECTION]");
    // Make the request
    Operation<Empty, gcvv::DeleteCollectionMetadata> response = await warehouseClient.DeleteCollectionAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteCollectionMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteCollectionMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteCollectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteCollectionAsync(DeleteCollectionRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteCollectionMetadata>> DeleteCollectionAsync(DeleteCollectionRequest request, CallSettings callSettings = null)

Deletes a collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCollectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteCollectionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteCollectionMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DeleteCollectionRequest request = new gcvv::DeleteCollectionRequest
    {
        CollectionName = gcvv::CollectionName.FromProjectNumberLocationCorpusCollection("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[COLLECTION]"),
    };
    // Make the request
    Operation<Empty, gcvv::DeleteCollectionMetadata> response = await warehouseClient.DeleteCollectionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteCollectionMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteCollectionMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteCollectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteCollectionAsync(DeleteCollectionRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteCollectionMetadata>> DeleteCollectionAsync(DeleteCollectionRequest request, CancellationToken cancellationToken)

Deletes a collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCollectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteCollectionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteCollectionMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DeleteCollectionRequest request = new gcvv::DeleteCollectionRequest
    {
        CollectionName = gcvv::CollectionName.FromProjectNumberLocationCorpusCollection("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[COLLECTION]"),
    };
    // Make the request
    Operation<Empty, gcvv::DeleteCollectionMetadata> response = await warehouseClient.DeleteCollectionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteCollectionMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteCollectionMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteCollectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteCollectionAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteCollectionMetadata>> DeleteCollectionAsync(string name, CallSettings callSettings = null)

Deletes a collection.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the collection to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteCollectionMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/collections/[COLLECTION]";
    // Make the request
    Operation<Empty, gcvv::DeleteCollectionMetadata> response = await warehouseClient.DeleteCollectionAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteCollectionMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteCollectionMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteCollectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteCollectionAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteCollectionMetadata>> DeleteCollectionAsync(string name, CancellationToken cancellationToken)

Deletes a collection.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the collection to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteCollectionMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/collections/[COLLECTION]";
    // Make the request
    Operation<Empty, gcvv::DeleteCollectionMetadata> response = await warehouseClient.DeleteCollectionAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteCollectionMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteCollectionMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteCollectionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteCorpus(CorpusName, CallSettings)
    
    
    public virtual void DeleteCorpus(CorpusName name, CallSettings callSettings = null)

Deletes a corpus only if its empty. Returns empty response.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The resource name of the corpus to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CorpusName name = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    // Make the request
    warehouseClient.DeleteCorpus(name);
    

### DeleteCorpus(DeleteCorpusRequest, CallSettings)
    
    
    public virtual void DeleteCorpus(DeleteCorpusRequest request, CallSettings callSettings = null)

Deletes a corpus only if its empty. Returns empty response.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteCorpusRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::DeleteCorpusRequest request = new gcvv::DeleteCorpusRequest
    {
        CorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
    };
    // Make the request
    warehouseClient.DeleteCorpus(request);
    

### DeleteCorpus(string, CallSettings)
    
    
    public virtual void DeleteCorpus(string name, CallSettings callSettings = null)

Deletes a corpus only if its empty. Returns empty response.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the corpus to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    // Make the request
    warehouseClient.DeleteCorpus(name);
    

### DeleteCorpusAsync(CorpusName, CallSettings)
    
    
    public virtual Task DeleteCorpusAsync(CorpusName name, CallSettings callSettings = null)

Deletes a corpus only if its empty. Returns empty response.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The resource name of the corpus to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName name = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    // Make the request
    await warehouseClient.DeleteCorpusAsync(name);
    

### DeleteCorpusAsync(CorpusName, CancellationToken)
    
    
    public virtual Task DeleteCorpusAsync(CorpusName name, CancellationToken cancellationToken)

Deletes a corpus only if its empty. Returns empty response.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The resource name of the corpus to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName name = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    // Make the request
    await warehouseClient.DeleteCorpusAsync(name);
    

### DeleteCorpusAsync(DeleteCorpusRequest, CallSettings)
    
    
    public virtual Task DeleteCorpusAsync(DeleteCorpusRequest request, CallSettings callSettings = null)

Deletes a corpus only if its empty. Returns empty response.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteCorpusRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DeleteCorpusRequest request = new gcvv::DeleteCorpusRequest
    {
        CorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
    };
    // Make the request
    await warehouseClient.DeleteCorpusAsync(request);
    

### DeleteCorpusAsync(DeleteCorpusRequest, CancellationToken)
    
    
    public virtual Task DeleteCorpusAsync(DeleteCorpusRequest request, CancellationToken cancellationToken)

Deletes a corpus only if its empty. Returns empty response.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteCorpusRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DeleteCorpusRequest request = new gcvv::DeleteCorpusRequest
    {
        CorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
    };
    // Make the request
    await warehouseClient.DeleteCorpusAsync(request);
    

### DeleteCorpusAsync(string, CallSettings)
    
    
    public virtual Task DeleteCorpusAsync(string name, CallSettings callSettings = null)

Deletes a corpus only if its empty. Returns empty response.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the corpus to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    // Make the request
    await warehouseClient.DeleteCorpusAsync(name);
    

### DeleteCorpusAsync(string, CancellationToken)
    
    
    public virtual Task DeleteCorpusAsync(string name, CancellationToken cancellationToken)

Deletes a corpus only if its empty. Returns empty response.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the corpus to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    // Make the request
    await warehouseClient.DeleteCorpusAsync(name);
    

### DeleteDataSchema(DataSchemaName, CallSettings)
    
    
    public virtual void DeleteDataSchema(DataSchemaName name, CallSettings callSettings = null)

Deletes data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchemaName)`  
Required. The name of the data schema to delete. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/dataSchemas/{data_schema_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::DataSchemaName name = gcvv::DataSchemaName.FromProjectNumberLocationCorpusDataSchema("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[DATA_SCHEMA]");
    // Make the request
    warehouseClient.DeleteDataSchema(name);
    

### DeleteDataSchema(DeleteDataSchemaRequest, CallSettings)
    
    
    public virtual void DeleteDataSchema(DeleteDataSchemaRequest request, CallSettings callSettings = null)

Deletes data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteDataSchemaRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::DeleteDataSchemaRequest request = new gcvv::DeleteDataSchemaRequest
    {
        DataSchemaName = gcvv::DataSchemaName.FromProjectNumberLocationCorpusDataSchema("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[DATA_SCHEMA]"),
    };
    // Make the request
    warehouseClient.DeleteDataSchema(request);
    

### DeleteDataSchema(string, CallSettings)
    
    
    public virtual void DeleteDataSchema(string name, CallSettings callSettings = null)

Deletes data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the data schema to delete. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/dataSchemas/{data_schema_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/dataSchemas/[DATA_SCHEMA]";
    // Make the request
    warehouseClient.DeleteDataSchema(name);
    

### DeleteDataSchemaAsync(DataSchemaName, CallSettings)
    
    
    public virtual Task DeleteDataSchemaAsync(DataSchemaName name, CallSettings callSettings = null)

Deletes data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchemaName)`  
Required. The name of the data schema to delete. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/dataSchemas/{data_schema_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DataSchemaName name = gcvv::DataSchemaName.FromProjectNumberLocationCorpusDataSchema("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[DATA_SCHEMA]");
    // Make the request
    await warehouseClient.DeleteDataSchemaAsync(name);
    

### DeleteDataSchemaAsync(DataSchemaName, CancellationToken)
    
    
    public virtual Task DeleteDataSchemaAsync(DataSchemaName name, CancellationToken cancellationToken)

Deletes data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchemaName)`  
Required. The name of the data schema to delete. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/dataSchemas/{data_schema_id}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DataSchemaName name = gcvv::DataSchemaName.FromProjectNumberLocationCorpusDataSchema("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[DATA_SCHEMA]");
    // Make the request
    await warehouseClient.DeleteDataSchemaAsync(name);
    

### DeleteDataSchemaAsync(DeleteDataSchemaRequest, CallSettings)
    
    
    public virtual Task DeleteDataSchemaAsync(DeleteDataSchemaRequest request, CallSettings callSettings = null)

Deletes data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteDataSchemaRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DeleteDataSchemaRequest request = new gcvv::DeleteDataSchemaRequest
    {
        DataSchemaName = gcvv::DataSchemaName.FromProjectNumberLocationCorpusDataSchema("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[DATA_SCHEMA]"),
    };
    // Make the request
    await warehouseClient.DeleteDataSchemaAsync(request);
    

### DeleteDataSchemaAsync(DeleteDataSchemaRequest, CancellationToken)
    
    
    public virtual Task DeleteDataSchemaAsync(DeleteDataSchemaRequest request, CancellationToken cancellationToken)

Deletes data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteDataSchemaRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DeleteDataSchemaRequest request = new gcvv::DeleteDataSchemaRequest
    {
        DataSchemaName = gcvv::DataSchemaName.FromProjectNumberLocationCorpusDataSchema("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[DATA_SCHEMA]"),
    };
    // Make the request
    await warehouseClient.DeleteDataSchemaAsync(request);
    

### DeleteDataSchemaAsync(string, CallSettings)
    
    
    public virtual Task DeleteDataSchemaAsync(string name, CallSettings callSettings = null)

Deletes data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the data schema to delete. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/dataSchemas/{data_schema_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/dataSchemas/[DATA_SCHEMA]";
    // Make the request
    await warehouseClient.DeleteDataSchemaAsync(name);
    

### DeleteDataSchemaAsync(string, CancellationToken)
    
    
    public virtual Task DeleteDataSchemaAsync(string name, CancellationToken cancellationToken)

Deletes data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the data schema to delete. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/dataSchemas/{data_schema_id}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/dataSchemas/[DATA_SCHEMA]";
    // Make the request
    await warehouseClient.DeleteDataSchemaAsync(name);
    

### DeleteIndex(DeleteIndexRequest, CallSettings)
    
    
    public virtual Operation<Empty, DeleteIndexMetadata> DeleteIndex(DeleteIndexRequest request, CallSettings callSettings = null)

Delete a single Index. In order to delete an index, the caller must make sure that it is not deployed to any index endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::DeleteIndexRequest request = new gcvv::DeleteIndexRequest
    {
        IndexName = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]"),
    };
    // Make the request
    Operation<Empty, gcvv::DeleteIndexMetadata> response = warehouseClient.DeleteIndex(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteIndexMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteIndexMetadata> retrievedResponse = warehouseClient.PollOnceDeleteIndex(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIndex(IndexName, CallSettings)
    
    
    public virtual Operation<Empty, DeleteIndexMetadata> DeleteIndex(IndexName name, CallSettings callSettings = null)

Delete a single Index. In order to delete an index, the caller must make sure that it is not deployed to any index endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IndexName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexName)`  
Required. The name of the index to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::IndexName name = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]");
    // Make the request
    Operation<Empty, gcvv::DeleteIndexMetadata> response = warehouseClient.DeleteIndex(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteIndexMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteIndexMetadata> retrievedResponse = warehouseClient.PollOnceDeleteIndex(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIndex(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteIndexMetadata> DeleteIndex(string name, CallSettings callSettings = null)

Delete a single Index. In order to delete an index, the caller must make sure that it is not deployed to any index endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the index to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/indexes/[INDEX]";
    // Make the request
    Operation<Empty, gcvv::DeleteIndexMetadata> response = warehouseClient.DeleteIndex(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteIndexMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteIndexMetadata> retrievedResponse = warehouseClient.PollOnceDeleteIndex(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIndexAsync(DeleteIndexRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteIndexMetadata>> DeleteIndexAsync(DeleteIndexRequest request, CallSettings callSettings = null)

Delete a single Index. In order to delete an index, the caller must make sure that it is not deployed to any index endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DeleteIndexRequest request = new gcvv::DeleteIndexRequest
    {
        IndexName = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]"),
    };
    // Make the request
    Operation<Empty, gcvv::DeleteIndexMetadata> response = await warehouseClient.DeleteIndexAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteIndexMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteIndexMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteIndexAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIndexAsync(DeleteIndexRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteIndexMetadata>> DeleteIndexAsync(DeleteIndexRequest request, CancellationToken cancellationToken)

Delete a single Index. In order to delete an index, the caller must make sure that it is not deployed to any index endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DeleteIndexRequest request = new gcvv::DeleteIndexRequest
    {
        IndexName = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]"),
    };
    // Make the request
    Operation<Empty, gcvv::DeleteIndexMetadata> response = await warehouseClient.DeleteIndexAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteIndexMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteIndexMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteIndexAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIndexAsync(IndexName, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteIndexMetadata>> DeleteIndexAsync(IndexName name, CallSettings callSettings = null)

Delete a single Index. In order to delete an index, the caller must make sure that it is not deployed to any index endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IndexName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexName)`  
Required. The name of the index to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::IndexName name = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]");
    // Make the request
    Operation<Empty, gcvv::DeleteIndexMetadata> response = await warehouseClient.DeleteIndexAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteIndexMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteIndexMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteIndexAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIndexAsync(IndexName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteIndexMetadata>> DeleteIndexAsync(IndexName name, CancellationToken cancellationToken)

Delete a single Index. In order to delete an index, the caller must make sure that it is not deployed to any index endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IndexName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexName)`  
Required. The name of the index to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::IndexName name = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]");
    // Make the request
    Operation<Empty, gcvv::DeleteIndexMetadata> response = await warehouseClient.DeleteIndexAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteIndexMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteIndexMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteIndexAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIndexAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteIndexMetadata>> DeleteIndexAsync(string name, CallSettings callSettings = null)

Delete a single Index. In order to delete an index, the caller must make sure that it is not deployed to any index endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the index to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/indexes/[INDEX]";
    // Make the request
    Operation<Empty, gcvv::DeleteIndexMetadata> response = await warehouseClient.DeleteIndexAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteIndexMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteIndexMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteIndexAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIndexAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteIndexMetadata>> DeleteIndexAsync(string name, CancellationToken cancellationToken)

Delete a single Index. In order to delete an index, the caller must make sure that it is not deployed to any index endpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the index to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/indexes/[INDEX]";
    // Make the request
    Operation<Empty, gcvv::DeleteIndexMetadata> response = await warehouseClient.DeleteIndexAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteIndexMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteIndexMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteIndexAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIndexEndpoint(DeleteIndexEndpointRequest, CallSettings)
    
    
    public virtual Operation<Empty, DeleteIndexEndpointMetadata> DeleteIndexEndpoint(DeleteIndexEndpointRequest request, CallSettings callSettings = null)

Deletes an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteIndexEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexEndpointMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::DeleteIndexEndpointRequest request = new gcvv::DeleteIndexEndpointRequest
    {
        IndexEndpointName = gcvv::IndexEndpointName.FromProjectLocationIndexEndpoint("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]"),
    };
    // Make the request
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> response = warehouseClient.DeleteIndexEndpoint(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> retrievedResponse = warehouseClient.PollOnceDeleteIndexEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIndexEndpoint(IndexEndpointName, CallSettings)
    
    
    public virtual Operation<Empty, DeleteIndexEndpointMetadata> DeleteIndexEndpoint(IndexEndpointName name, CallSettings callSettings = null)

Deletes an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IndexEndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpointName)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexEndpointMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::IndexEndpointName name = gcvv::IndexEndpointName.FromProjectLocationIndexEndpoint("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]");
    // Make the request
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> response = warehouseClient.DeleteIndexEndpoint(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> retrievedResponse = warehouseClient.PollOnceDeleteIndexEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIndexEndpoint(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteIndexEndpointMetadata> DeleteIndexEndpoint(string name, CallSettings callSettings = null)

Deletes an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexEndpointMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/indexEndpoints/[INDEX_ENDPOINT]";
    // Make the request
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> response = warehouseClient.DeleteIndexEndpoint(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> retrievedResponse = warehouseClient.PollOnceDeleteIndexEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIndexEndpointAsync(DeleteIndexEndpointRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteIndexEndpointMetadata>> DeleteIndexEndpointAsync(DeleteIndexEndpointRequest request, CallSettings callSettings = null)

Deletes an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteIndexEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexEndpointMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DeleteIndexEndpointRequest request = new gcvv::DeleteIndexEndpointRequest
    {
        IndexEndpointName = gcvv::IndexEndpointName.FromProjectLocationIndexEndpoint("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]"),
    };
    // Make the request
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> response = await warehouseClient.DeleteIndexEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteIndexEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIndexEndpointAsync(DeleteIndexEndpointRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteIndexEndpointMetadata>> DeleteIndexEndpointAsync(DeleteIndexEndpointRequest request, CancellationToken cancellationToken)

Deletes an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteIndexEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexEndpointMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DeleteIndexEndpointRequest request = new gcvv::DeleteIndexEndpointRequest
    {
        IndexEndpointName = gcvv::IndexEndpointName.FromProjectLocationIndexEndpoint("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]"),
    };
    // Make the request
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> response = await warehouseClient.DeleteIndexEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteIndexEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIndexEndpointAsync(IndexEndpointName, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteIndexEndpointMetadata>> DeleteIndexEndpointAsync(IndexEndpointName name, CallSettings callSettings = null)

Deletes an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IndexEndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpointName)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexEndpointMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::IndexEndpointName name = gcvv::IndexEndpointName.FromProjectLocationIndexEndpoint("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]");
    // Make the request
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> response = await warehouseClient.DeleteIndexEndpointAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteIndexEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIndexEndpointAsync(IndexEndpointName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteIndexEndpointMetadata>> DeleteIndexEndpointAsync(IndexEndpointName name, CancellationToken cancellationToken)

Deletes an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IndexEndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpointName)`  
Required. Name of the resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexEndpointMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::IndexEndpointName name = gcvv::IndexEndpointName.FromProjectLocationIndexEndpoint("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]");
    // Make the request
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> response = await warehouseClient.DeleteIndexEndpointAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteIndexEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIndexEndpointAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteIndexEndpointMetadata>> DeleteIndexEndpointAsync(string name, CallSettings callSettings = null)

Deletes an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexEndpointMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/indexEndpoints/[INDEX_ENDPOINT]";
    // Make the request
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> response = await warehouseClient.DeleteIndexEndpointAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteIndexEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteIndexEndpointAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteIndexEndpointMetadata>> DeleteIndexEndpointAsync(string name, CancellationToken cancellationToken)

Deletes an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexEndpointMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/indexEndpoints/[INDEX_ENDPOINT]";
    // Make the request
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> response = await warehouseClient.DeleteIndexEndpointAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcvv::DeleteIndexEndpointMetadata> retrievedResponse = await warehouseClient.PollOnceDeleteIndexEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSearchConfig(DeleteSearchConfigRequest, CallSettings)
    
    
    public virtual void DeleteSearchConfig(DeleteSearchConfigRequest request, CallSettings callSettings = null)

Deletes a search configuration inside a corpus.

For a DeleteSearchConfigRequest to be valid, Request.search_configuration.name must already exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSearchConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteSearchConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::DeleteSearchConfigRequest request = new gcvv::DeleteSearchConfigRequest
    {
        SearchConfigName = gcvv::SearchConfigName.FromProjectNumberLocationCorpusSearchConfig("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_CONFIG]"),
    };
    // Make the request
    warehouseClient.DeleteSearchConfig(request);
    

### DeleteSearchConfig(SearchConfigName, CallSettings)
    
    
    public virtual void DeleteSearchConfig(SearchConfigName name, CallSettings callSettings = null)

Deletes a search configuration inside a corpus.

For a DeleteSearchConfigRequest to be valid, Request.search_configuration.name must already exist.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SearchConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfigName)`  
Required. The name of the search configuration to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchConfigs/{search_config}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::SearchConfigName name = gcvv::SearchConfigName.FromProjectNumberLocationCorpusSearchConfig("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_CONFIG]");
    // Make the request
    warehouseClient.DeleteSearchConfig(name);
    

### DeleteSearchConfig(string, CallSettings)
    
    
    public virtual void DeleteSearchConfig(string name, CallSettings callSettings = null)

Deletes a search configuration inside a corpus.

For a DeleteSearchConfigRequest to be valid, Request.search_configuration.name must already exist.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the search configuration to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchConfigs/{search_config}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/searchConfigs/[SEARCH_CONFIG]";
    // Make the request
    warehouseClient.DeleteSearchConfig(name);
    

### DeleteSearchConfigAsync(DeleteSearchConfigRequest, CallSettings)
    
    
    public virtual Task DeleteSearchConfigAsync(DeleteSearchConfigRequest request, CallSettings callSettings = null)

Deletes a search configuration inside a corpus.

For a DeleteSearchConfigRequest to be valid, Request.search_configuration.name must already exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSearchConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteSearchConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DeleteSearchConfigRequest request = new gcvv::DeleteSearchConfigRequest
    {
        SearchConfigName = gcvv::SearchConfigName.FromProjectNumberLocationCorpusSearchConfig("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_CONFIG]"),
    };
    // Make the request
    await warehouseClient.DeleteSearchConfigAsync(request);
    

### DeleteSearchConfigAsync(DeleteSearchConfigRequest, CancellationToken)
    
    
    public virtual Task DeleteSearchConfigAsync(DeleteSearchConfigRequest request, CancellationToken cancellationToken)

Deletes a search configuration inside a corpus.

For a DeleteSearchConfigRequest to be valid, Request.search_configuration.name must already exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSearchConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteSearchConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DeleteSearchConfigRequest request = new gcvv::DeleteSearchConfigRequest
    {
        SearchConfigName = gcvv::SearchConfigName.FromProjectNumberLocationCorpusSearchConfig("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_CONFIG]"),
    };
    // Make the request
    await warehouseClient.DeleteSearchConfigAsync(request);
    

### DeleteSearchConfigAsync(SearchConfigName, CallSettings)
    
    
    public virtual Task DeleteSearchConfigAsync(SearchConfigName name, CallSettings callSettings = null)

Deletes a search configuration inside a corpus.

For a DeleteSearchConfigRequest to be valid, Request.search_configuration.name must already exist.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SearchConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfigName)`  
Required. The name of the search configuration to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchConfigs/{search_config}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::SearchConfigName name = gcvv::SearchConfigName.FromProjectNumberLocationCorpusSearchConfig("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_CONFIG]");
    // Make the request
    await warehouseClient.DeleteSearchConfigAsync(name);
    

### DeleteSearchConfigAsync(SearchConfigName, CancellationToken)
    
    
    public virtual Task DeleteSearchConfigAsync(SearchConfigName name, CancellationToken cancellationToken)

Deletes a search configuration inside a corpus.

For a DeleteSearchConfigRequest to be valid, Request.search_configuration.name must already exist.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SearchConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfigName)`  
Required. The name of the search configuration to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchConfigs/{search_config}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::SearchConfigName name = gcvv::SearchConfigName.FromProjectNumberLocationCorpusSearchConfig("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_CONFIG]");
    // Make the request
    await warehouseClient.DeleteSearchConfigAsync(name);
    

### DeleteSearchConfigAsync(string, CallSettings)
    
    
    public virtual Task DeleteSearchConfigAsync(string name, CallSettings callSettings = null)

Deletes a search configuration inside a corpus.

For a DeleteSearchConfigRequest to be valid, Request.search_configuration.name must already exist.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the search configuration to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchConfigs/{search_config}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/searchConfigs/[SEARCH_CONFIG]";
    // Make the request
    await warehouseClient.DeleteSearchConfigAsync(name);
    

### DeleteSearchConfigAsync(string, CancellationToken)
    
    
    public virtual Task DeleteSearchConfigAsync(string name, CancellationToken cancellationToken)

Deletes a search configuration inside a corpus.

For a DeleteSearchConfigRequest to be valid, Request.search_configuration.name must already exist.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the search configuration to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchConfigs/{search_config}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/searchConfigs/[SEARCH_CONFIG]";
    // Make the request
    await warehouseClient.DeleteSearchConfigAsync(name);
    

### DeleteSearchHypernym(DeleteSearchHypernymRequest, CallSettings)
    
    
    public virtual void DeleteSearchHypernym(DeleteSearchHypernymRequest request, CallSettings callSettings = null)

Deletes a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSearchHypernymRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteSearchHypernymRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::DeleteSearchHypernymRequest request = new gcvv::DeleteSearchHypernymRequest
    {
        SearchHypernymName = gcvv::SearchHypernymName.FromProjectNumberLocationCorpusSearchHypernym("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_HYPERNYM]"),
    };
    // Make the request
    warehouseClient.DeleteSearchHypernym(request);
    

### DeleteSearchHypernym(SearchHypernymName, CallSettings)
    
    
    public virtual void DeleteSearchHypernym(SearchHypernymName name, CallSettings callSettings = null)

Deletes a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SearchHypernymName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernymName)`  
Required. The name of the SearchHypernym to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchHypernyms/{search_hypernym}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::SearchHypernymName name = gcvv::SearchHypernymName.FromProjectNumberLocationCorpusSearchHypernym("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_HYPERNYM]");
    // Make the request
    warehouseClient.DeleteSearchHypernym(name);
    

### DeleteSearchHypernym(string, CallSettings)
    
    
    public virtual void DeleteSearchHypernym(string name, CallSettings callSettings = null)

Deletes a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the SearchHypernym to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchHypernyms/{search_hypernym}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/searchHypernyms/[SEARCH_HYPERNYM]";
    // Make the request
    warehouseClient.DeleteSearchHypernym(name);
    

### DeleteSearchHypernymAsync(DeleteSearchHypernymRequest, CallSettings)
    
    
    public virtual Task DeleteSearchHypernymAsync(DeleteSearchHypernymRequest request, CallSettings callSettings = null)

Deletes a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSearchHypernymRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteSearchHypernymRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DeleteSearchHypernymRequest request = new gcvv::DeleteSearchHypernymRequest
    {
        SearchHypernymName = gcvv::SearchHypernymName.FromProjectNumberLocationCorpusSearchHypernym("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_HYPERNYM]"),
    };
    // Make the request
    await warehouseClient.DeleteSearchHypernymAsync(request);
    

### DeleteSearchHypernymAsync(DeleteSearchHypernymRequest, CancellationToken)
    
    
    public virtual Task DeleteSearchHypernymAsync(DeleteSearchHypernymRequest request, CancellationToken cancellationToken)

Deletes a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSearchHypernymRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteSearchHypernymRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DeleteSearchHypernymRequest request = new gcvv::DeleteSearchHypernymRequest
    {
        SearchHypernymName = gcvv::SearchHypernymName.FromProjectNumberLocationCorpusSearchHypernym("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_HYPERNYM]"),
    };
    // Make the request
    await warehouseClient.DeleteSearchHypernymAsync(request);
    

### DeleteSearchHypernymAsync(SearchHypernymName, CallSettings)
    
    
    public virtual Task DeleteSearchHypernymAsync(SearchHypernymName name, CallSettings callSettings = null)

Deletes a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SearchHypernymName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernymName)`  
Required. The name of the SearchHypernym to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchHypernyms/{search_hypernym}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::SearchHypernymName name = gcvv::SearchHypernymName.FromProjectNumberLocationCorpusSearchHypernym("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_HYPERNYM]");
    // Make the request
    await warehouseClient.DeleteSearchHypernymAsync(name);
    

### DeleteSearchHypernymAsync(SearchHypernymName, CancellationToken)
    
    
    public virtual Task DeleteSearchHypernymAsync(SearchHypernymName name, CancellationToken cancellationToken)

Deletes a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SearchHypernymName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernymName)`  
Required. The name of the SearchHypernym to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchHypernyms/{search_hypernym}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::SearchHypernymName name = gcvv::SearchHypernymName.FromProjectNumberLocationCorpusSearchHypernym("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_HYPERNYM]");
    // Make the request
    await warehouseClient.DeleteSearchHypernymAsync(name);
    

### DeleteSearchHypernymAsync(string, CallSettings)
    
    
    public virtual Task DeleteSearchHypernymAsync(string name, CallSettings callSettings = null)

Deletes a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the SearchHypernym to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchHypernyms/{search_hypernym}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/searchHypernyms/[SEARCH_HYPERNYM]";
    // Make the request
    await warehouseClient.DeleteSearchHypernymAsync(name);
    

### DeleteSearchHypernymAsync(string, CancellationToken)
    
    
    public virtual Task DeleteSearchHypernymAsync(string name, CancellationToken cancellationToken)

Deletes a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the SearchHypernym to delete. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchHypernyms/{search_hypernym}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/searchHypernyms/[SEARCH_HYPERNYM]";
    // Make the request
    await warehouseClient.DeleteSearchHypernymAsync(name);
    

### DeployIndex(DeployIndexRequest, CallSettings)
    
    
    public virtual Operation<DeployIndexResponse, DeployIndexMetadata> DeployIndex(DeployIndexRequest request, CallSettings callSettings = null)

Deploys an Index to IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeployIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployIndexRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployIndexResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployIndexResponse)[DeployIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployIndexMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::DeployIndexRequest request = new gcvv::DeployIndexRequest
    {
        IndexEndpointAsIndexEndpointName = gcvv::IndexEndpointName.FromProjectLocationIndexEndpoint("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]"),
        DeployedIndex = new gcvv::DeployedIndex(),
    };
    // Make the request
    Operation<gcvv::DeployIndexResponse, gcvv::DeployIndexMetadata> response = warehouseClient.DeployIndex(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::DeployIndexResponse, gcvv::DeployIndexMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::DeployIndexResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::DeployIndexResponse, gcvv::DeployIndexMetadata> retrievedResponse = warehouseClient.PollOnceDeployIndex(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::DeployIndexResponse retrievedResult = retrievedResponse.Result;
    }
    

### DeployIndexAsync(DeployIndexRequest, CallSettings)
    
    
    public virtual Task<Operation<DeployIndexResponse, DeployIndexMetadata>> DeployIndexAsync(DeployIndexRequest request, CallSettings callSettings = null)

Deploys an Index to IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeployIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployIndexRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployIndexResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployIndexResponse)[DeployIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployIndexMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DeployIndexRequest request = new gcvv::DeployIndexRequest
    {
        IndexEndpointAsIndexEndpointName = gcvv::IndexEndpointName.FromProjectLocationIndexEndpoint("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]"),
        DeployedIndex = new gcvv::DeployedIndex(),
    };
    // Make the request
    Operation<gcvv::DeployIndexResponse, gcvv::DeployIndexMetadata> response = await warehouseClient.DeployIndexAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::DeployIndexResponse, gcvv::DeployIndexMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::DeployIndexResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::DeployIndexResponse, gcvv::DeployIndexMetadata> retrievedResponse = await warehouseClient.PollOnceDeployIndexAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::DeployIndexResponse retrievedResult = retrievedResponse.Result;
    }
    

### DeployIndexAsync(DeployIndexRequest, CancellationToken)
    
    
    public virtual Task<Operation<DeployIndexResponse, DeployIndexMetadata>> DeployIndexAsync(DeployIndexRequest request, CancellationToken cancellationToken)

Deploys an Index to IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeployIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployIndexRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployIndexResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployIndexResponse)[DeployIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployIndexMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DeployIndexRequest request = new gcvv::DeployIndexRequest
    {
        IndexEndpointAsIndexEndpointName = gcvv::IndexEndpointName.FromProjectLocationIndexEndpoint("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]"),
        DeployedIndex = new gcvv::DeployedIndex(),
    };
    // Make the request
    Operation<gcvv::DeployIndexResponse, gcvv::DeployIndexMetadata> response = await warehouseClient.DeployIndexAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::DeployIndexResponse, gcvv::DeployIndexMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::DeployIndexResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::DeployIndexResponse, gcvv::DeployIndexMetadata> retrievedResponse = await warehouseClient.PollOnceDeployIndexAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::DeployIndexResponse retrievedResult = retrievedResponse.Result;
    }
    

### GenerateHlsUri(GenerateHlsUriRequest, CallSettings)
    
    
    public virtual GenerateHlsUriResponse GenerateHlsUri(GenerateHlsUriRequest request, CallSettings callSettings = null)

Generates a uri for an HLS manifest. The api takes in a collection of time ranges, and generates a URI for an HLS manifest that covers all the requested time ranges.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateHlsUriRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GenerateHlsUriRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateHlsUriResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GenerateHlsUriResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::GenerateHlsUriRequest request = new gcvv::GenerateHlsUriRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
        TemporalPartitions =
        {
            new gcvv::Partition.Types.TemporalPartition(),
        },
        LiveViewEnabled = false,
    };
    // Make the request
    gcvv::GenerateHlsUriResponse response = warehouseClient.GenerateHlsUri(request);
    

### GenerateHlsUriAsync(GenerateHlsUriRequest, CallSettings)
    
    
    public virtual Task<GenerateHlsUriResponse> GenerateHlsUriAsync(GenerateHlsUriRequest request, CallSettings callSettings = null)

Generates a uri for an HLS manifest. The api takes in a collection of time ranges, and generates a URI for an HLS manifest that covers all the requested time ranges.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateHlsUriRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GenerateHlsUriRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateHlsUriResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GenerateHlsUriResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GenerateHlsUriRequest request = new gcvv::GenerateHlsUriRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
        TemporalPartitions =
        {
            new gcvv::Partition.Types.TemporalPartition(),
        },
        LiveViewEnabled = false,
    };
    // Make the request
    gcvv::GenerateHlsUriResponse response = await warehouseClient.GenerateHlsUriAsync(request);
    

### GenerateHlsUriAsync(GenerateHlsUriRequest, CancellationToken)
    
    
    public virtual Task<GenerateHlsUriResponse> GenerateHlsUriAsync(GenerateHlsUriRequest request, CancellationToken cancellationToken)

Generates a uri for an HLS manifest. The api takes in a collection of time ranges, and generates a URI for an HLS manifest that covers all the requested time ranges.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateHlsUriRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GenerateHlsUriRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateHlsUriResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GenerateHlsUriResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GenerateHlsUriRequest request = new gcvv::GenerateHlsUriRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
        TemporalPartitions =
        {
            new gcvv::Partition.Types.TemporalPartition(),
        },
        LiveViewEnabled = false,
    };
    // Make the request
    gcvv::GenerateHlsUriResponse response = await warehouseClient.GenerateHlsUriAsync(request);
    

### GenerateRetrievalUrl(GenerateRetrievalUrlRequest, CallSettings)
    
    
    public virtual GenerateRetrievalUrlResponse GenerateRetrievalUrl(GenerateRetrievalUrlRequest request, CallSettings callSettings = null)

Generates a signed url for downloading the asset. For video warehouse, please see comment of UploadAsset about how to allow retrieval of cloud storage files in a different project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateRetrievalUrlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GenerateRetrievalUrlRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateRetrievalUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GenerateRetrievalUrlResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::GenerateRetrievalUrlRequest request = new gcvv::GenerateRetrievalUrlRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
    };
    // Make the request
    gcvv::GenerateRetrievalUrlResponse response = warehouseClient.GenerateRetrievalUrl(request);
    

### GenerateRetrievalUrlAsync(GenerateRetrievalUrlRequest, CallSettings)
    
    
    public virtual Task<GenerateRetrievalUrlResponse> GenerateRetrievalUrlAsync(GenerateRetrievalUrlRequest request, CallSettings callSettings = null)

Generates a signed url for downloading the asset. For video warehouse, please see comment of UploadAsset about how to allow retrieval of cloud storage files in a different project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateRetrievalUrlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GenerateRetrievalUrlRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateRetrievalUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GenerateRetrievalUrlResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GenerateRetrievalUrlRequest request = new gcvv::GenerateRetrievalUrlRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
    };
    // Make the request
    gcvv::GenerateRetrievalUrlResponse response = await warehouseClient.GenerateRetrievalUrlAsync(request);
    

### GenerateRetrievalUrlAsync(GenerateRetrievalUrlRequest, CancellationToken)
    
    
    public virtual Task<GenerateRetrievalUrlResponse> GenerateRetrievalUrlAsync(GenerateRetrievalUrlRequest request, CancellationToken cancellationToken)

Generates a signed url for downloading the asset. For video warehouse, please see comment of UploadAsset about how to allow retrieval of cloud storage files in a different project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateRetrievalUrlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GenerateRetrievalUrlRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateRetrievalUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GenerateRetrievalUrlResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GenerateRetrievalUrlRequest request = new gcvv::GenerateRetrievalUrlRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
    };
    // Make the request
    gcvv::GenerateRetrievalUrlResponse response = await warehouseClient.GenerateRetrievalUrlAsync(request);
    

### GetAnnotation(AnnotationName, CallSettings)
    
    
    public virtual Annotation GetAnnotation(AnnotationName name, CallSettings callSettings = null)

Reads annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AnnotationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnnotationName)`  
Required. The name of the annotation to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}/annotations/{annotation}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::AnnotationName name = gcvv::AnnotationName.FromProjectNumberLocationCorpusAssetAnnotation("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]", "[ANNOTATION]");
    // Make the request
    gcvv::Annotation response = warehouseClient.GetAnnotation(name);
    

### GetAnnotation(GetAnnotationRequest, CallSettings)
    
    
    public virtual Annotation GetAnnotation(GetAnnotationRequest request, CallSettings callSettings = null)

Reads annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAnnotationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetAnnotationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::GetAnnotationRequest request = new gcvv::GetAnnotationRequest
    {
        AnnotationName = gcvv::AnnotationName.FromProjectNumberLocationCorpusAssetAnnotation("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]", "[ANNOTATION]"),
    };
    // Make the request
    gcvv::Annotation response = warehouseClient.GetAnnotation(request);
    

### GetAnnotation(string, CallSettings)
    
    
    public virtual Annotation GetAnnotation(string name, CallSettings callSettings = null)

Reads annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the annotation to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}/annotations/{annotation}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/assets/[ASSET]/annotations/[ANNOTATION]";
    // Make the request
    gcvv::Annotation response = warehouseClient.GetAnnotation(name);
    

### GetAnnotationAsync(AnnotationName, CallSettings)
    
    
    public virtual Task<Annotation> GetAnnotationAsync(AnnotationName name, CallSettings callSettings = null)

Reads annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AnnotationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnnotationName)`  
Required. The name of the annotation to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}/annotations/{annotation}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::AnnotationName name = gcvv::AnnotationName.FromProjectNumberLocationCorpusAssetAnnotation("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]", "[ANNOTATION]");
    // Make the request
    gcvv::Annotation response = await warehouseClient.GetAnnotationAsync(name);
    

### GetAnnotationAsync(AnnotationName, CancellationToken)
    
    
    public virtual Task<Annotation> GetAnnotationAsync(AnnotationName name, CancellationToken cancellationToken)

Reads annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AnnotationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnnotationName)`  
Required. The name of the annotation to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}/annotations/{annotation}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::AnnotationName name = gcvv::AnnotationName.FromProjectNumberLocationCorpusAssetAnnotation("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]", "[ANNOTATION]");
    // Make the request
    gcvv::Annotation response = await warehouseClient.GetAnnotationAsync(name);
    

### GetAnnotationAsync(GetAnnotationRequest, CallSettings)
    
    
    public virtual Task<Annotation> GetAnnotationAsync(GetAnnotationRequest request, CallSettings callSettings = null)

Reads annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAnnotationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetAnnotationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GetAnnotationRequest request = new gcvv::GetAnnotationRequest
    {
        AnnotationName = gcvv::AnnotationName.FromProjectNumberLocationCorpusAssetAnnotation("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]", "[ANNOTATION]"),
    };
    // Make the request
    gcvv::Annotation response = await warehouseClient.GetAnnotationAsync(request);
    

### GetAnnotationAsync(GetAnnotationRequest, CancellationToken)
    
    
    public virtual Task<Annotation> GetAnnotationAsync(GetAnnotationRequest request, CancellationToken cancellationToken)

Reads annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAnnotationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetAnnotationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GetAnnotationRequest request = new gcvv::GetAnnotationRequest
    {
        AnnotationName = gcvv::AnnotationName.FromProjectNumberLocationCorpusAssetAnnotation("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]", "[ANNOTATION]"),
    };
    // Make the request
    gcvv::Annotation response = await warehouseClient.GetAnnotationAsync(request);
    

### GetAnnotationAsync(string, CallSettings)
    
    
    public virtual Task<Annotation> GetAnnotationAsync(string name, CallSettings callSettings = null)

Reads annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the annotation to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}/annotations/{annotation}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/assets/[ASSET]/annotations/[ANNOTATION]";
    // Make the request
    gcvv::Annotation response = await warehouseClient.GetAnnotationAsync(name);
    

### GetAnnotationAsync(string, CancellationToken)
    
    
    public virtual Task<Annotation> GetAnnotationAsync(string name, CancellationToken cancellationToken)

Reads annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the annotation to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}/annotations/{annotation}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/assets/[ASSET]/annotations/[ANNOTATION]";
    // Make the request
    gcvv::Annotation response = await warehouseClient.GetAnnotationAsync(name);
    

### GetAsset(AssetName, CallSettings)
    
    
    public virtual Asset GetAsset(AssetName name, CallSettings callSettings = null)

Reads an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AssetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AssetName)`  
Required. The name of the asset to retrieve. Format: projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::AssetName name = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]");
    // Make the request
    gcvv::Asset response = warehouseClient.GetAsset(name);
    

### GetAsset(GetAssetRequest, CallSettings)
    
    
    public virtual Asset GetAsset(GetAssetRequest request, CallSettings callSettings = null)

Reads an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetAssetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::GetAssetRequest request = new gcvv::GetAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
    };
    // Make the request
    gcvv::Asset response = warehouseClient.GetAsset(request);
    

### GetAsset(string, CallSettings)
    
    
    public virtual Asset GetAsset(string name, CallSettings callSettings = null)

Reads an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the asset to retrieve. Format: projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/assets/[ASSET]";
    // Make the request
    gcvv::Asset response = warehouseClient.GetAsset(name);
    

### GetAssetAsync(AssetName, CallSettings)
    
    
    public virtual Task<Asset> GetAssetAsync(AssetName name, CallSettings callSettings = null)

Reads an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AssetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AssetName)`  
Required. The name of the asset to retrieve. Format: projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::AssetName name = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]");
    // Make the request
    gcvv::Asset response = await warehouseClient.GetAssetAsync(name);
    

### GetAssetAsync(AssetName, CancellationToken)
    
    
    public virtual Task<Asset> GetAssetAsync(AssetName name, CancellationToken cancellationToken)

Reads an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AssetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AssetName)`  
Required. The name of the asset to retrieve. Format: projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::AssetName name = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]");
    // Make the request
    gcvv::Asset response = await warehouseClient.GetAssetAsync(name);
    

### GetAssetAsync(GetAssetRequest, CallSettings)
    
    
    public virtual Task<Asset> GetAssetAsync(GetAssetRequest request, CallSettings callSettings = null)

Reads an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetAssetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GetAssetRequest request = new gcvv::GetAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
    };
    // Make the request
    gcvv::Asset response = await warehouseClient.GetAssetAsync(request);
    

### GetAssetAsync(GetAssetRequest, CancellationToken)
    
    
    public virtual Task<Asset> GetAssetAsync(GetAssetRequest request, CancellationToken cancellationToken)

Reads an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetAssetRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GetAssetRequest request = new gcvv::GetAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
    };
    // Make the request
    gcvv::Asset response = await warehouseClient.GetAssetAsync(request);
    

### GetAssetAsync(string, CallSettings)
    
    
    public virtual Task<Asset> GetAssetAsync(string name, CallSettings callSettings = null)

Reads an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the asset to retrieve. Format: projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/assets/[ASSET]";
    // Make the request
    gcvv::Asset response = await warehouseClient.GetAssetAsync(name);
    

### GetAssetAsync(string, CancellationToken)
    
    
    public virtual Task<Asset> GetAssetAsync(string name, CancellationToken cancellationToken)

Reads an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the asset to retrieve. Format: projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/assets/[ASSET]";
    // Make the request
    gcvv::Asset response = await warehouseClient.GetAssetAsync(name);
    

### GetCollection(CollectionName, CallSettings)
    
    
    public virtual Collection GetCollection(CollectionName name, CallSettings callSettings = null)

Gets a collection.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CollectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionName)`  
Required. The name of the collection to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CollectionName name = gcvv::CollectionName.FromProjectNumberLocationCorpusCollection("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[COLLECTION]");
    // Make the request
    gcvv::Collection response = warehouseClient.GetCollection(name);
    

### GetCollection(GetCollectionRequest, CallSettings)
    
    
    public virtual Collection GetCollection(GetCollectionRequest request, CallSettings callSettings = null)

Gets a collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCollectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetCollectionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::GetCollectionRequest request = new gcvv::GetCollectionRequest
    {
        CollectionName = gcvv::CollectionName.FromProjectNumberLocationCorpusCollection("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[COLLECTION]"),
    };
    // Make the request
    gcvv::Collection response = warehouseClient.GetCollection(request);
    

### GetCollection(string, CallSettings)
    
    
    public virtual Collection GetCollection(string name, CallSettings callSettings = null)

Gets a collection.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the collection to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/collections/[COLLECTION]";
    // Make the request
    gcvv::Collection response = warehouseClient.GetCollection(name);
    

### GetCollectionAsync(CollectionName, CallSettings)
    
    
    public virtual Task<Collection> GetCollectionAsync(CollectionName name, CallSettings callSettings = null)

Gets a collection.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CollectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionName)`  
Required. The name of the collection to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CollectionName name = gcvv::CollectionName.FromProjectNumberLocationCorpusCollection("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[COLLECTION]");
    // Make the request
    gcvv::Collection response = await warehouseClient.GetCollectionAsync(name);
    

### GetCollectionAsync(CollectionName, CancellationToken)
    
    
    public virtual Task<Collection> GetCollectionAsync(CollectionName name, CancellationToken cancellationToken)

Gets a collection.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CollectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionName)`  
Required. The name of the collection to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CollectionName name = gcvv::CollectionName.FromProjectNumberLocationCorpusCollection("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[COLLECTION]");
    // Make the request
    gcvv::Collection response = await warehouseClient.GetCollectionAsync(name);
    

### GetCollectionAsync(GetCollectionRequest, CallSettings)
    
    
    public virtual Task<Collection> GetCollectionAsync(GetCollectionRequest request, CallSettings callSettings = null)

Gets a collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCollectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetCollectionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GetCollectionRequest request = new gcvv::GetCollectionRequest
    {
        CollectionName = gcvv::CollectionName.FromProjectNumberLocationCorpusCollection("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[COLLECTION]"),
    };
    // Make the request
    gcvv::Collection response = await warehouseClient.GetCollectionAsync(request);
    

### GetCollectionAsync(GetCollectionRequest, CancellationToken)
    
    
    public virtual Task<Collection> GetCollectionAsync(GetCollectionRequest request, CancellationToken cancellationToken)

Gets a collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCollectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetCollectionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GetCollectionRequest request = new gcvv::GetCollectionRequest
    {
        CollectionName = gcvv::CollectionName.FromProjectNumberLocationCorpusCollection("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[COLLECTION]"),
    };
    // Make the request
    gcvv::Collection response = await warehouseClient.GetCollectionAsync(request);
    

### GetCollectionAsync(string, CallSettings)
    
    
    public virtual Task<Collection> GetCollectionAsync(string name, CallSettings callSettings = null)

Gets a collection.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the collection to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/collections/[COLLECTION]";
    // Make the request
    gcvv::Collection response = await warehouseClient.GetCollectionAsync(name);
    

### GetCollectionAsync(string, CancellationToken)
    
    
    public virtual Task<Collection> GetCollectionAsync(string name, CancellationToken cancellationToken)

Gets a collection.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the collection to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/collections/[COLLECTION]";
    // Make the request
    gcvv::Collection response = await warehouseClient.GetCollectionAsync(name);
    

### GetCorpus(CorpusName, CallSettings)
    
    
    public virtual Corpus GetCorpus(CorpusName name, CallSettings callSettings = null)

Gets corpus details inside a project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The resource name of the corpus to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CorpusName name = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    // Make the request
    gcvv::Corpus response = warehouseClient.GetCorpus(name);
    

### GetCorpus(GetCorpusRequest, CallSettings)
    
    
    public virtual Corpus GetCorpus(GetCorpusRequest request, CallSettings callSettings = null)

Gets corpus details inside a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetCorpusRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::GetCorpusRequest request = new gcvv::GetCorpusRequest
    {
        CorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
    };
    // Make the request
    gcvv::Corpus response = warehouseClient.GetCorpus(request);
    

### GetCorpus(string, CallSettings)
    
    
    public virtual Corpus GetCorpus(string name, CallSettings callSettings = null)

Gets corpus details inside a project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the corpus to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    // Make the request
    gcvv::Corpus response = warehouseClient.GetCorpus(name);
    

### GetCorpusAsync(CorpusName, CallSettings)
    
    
    public virtual Task<Corpus> GetCorpusAsync(CorpusName name, CallSettings callSettings = null)

Gets corpus details inside a project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The resource name of the corpus to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName name = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    // Make the request
    gcvv::Corpus response = await warehouseClient.GetCorpusAsync(name);
    

### GetCorpusAsync(CorpusName, CancellationToken)
    
    
    public virtual Task<Corpus> GetCorpusAsync(CorpusName name, CancellationToken cancellationToken)

Gets corpus details inside a project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The resource name of the corpus to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName name = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    // Make the request
    gcvv::Corpus response = await warehouseClient.GetCorpusAsync(name);
    

### GetCorpusAsync(GetCorpusRequest, CallSettings)
    
    
    public virtual Task<Corpus> GetCorpusAsync(GetCorpusRequest request, CallSettings callSettings = null)

Gets corpus details inside a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetCorpusRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GetCorpusRequest request = new gcvv::GetCorpusRequest
    {
        CorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
    };
    // Make the request
    gcvv::Corpus response = await warehouseClient.GetCorpusAsync(request);
    

### GetCorpusAsync(GetCorpusRequest, CancellationToken)
    
    
    public virtual Task<Corpus> GetCorpusAsync(GetCorpusRequest request, CancellationToken cancellationToken)

Gets corpus details inside a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetCorpusRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GetCorpusRequest request = new gcvv::GetCorpusRequest
    {
        CorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
    };
    // Make the request
    gcvv::Corpus response = await warehouseClient.GetCorpusAsync(request);
    

### GetCorpusAsync(string, CallSettings)
    
    
    public virtual Task<Corpus> GetCorpusAsync(string name, CallSettings callSettings = null)

Gets corpus details inside a project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the corpus to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    // Make the request
    gcvv::Corpus response = await warehouseClient.GetCorpusAsync(name);
    

### GetCorpusAsync(string, CancellationToken)
    
    
    public virtual Task<Corpus> GetCorpusAsync(string name, CancellationToken cancellationToken)

Gets corpus details inside a project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the corpus to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    // Make the request
    gcvv::Corpus response = await warehouseClient.GetCorpusAsync(name);
    

### GetDataSchema(DataSchemaName, CallSettings)
    
    
    public virtual DataSchema GetDataSchema(DataSchemaName name, CallSettings callSettings = null)

Gets data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchemaName)`  
Required. The name of the data schema to retrieve. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/dataSchemas/{data_schema_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::DataSchemaName name = gcvv::DataSchemaName.FromProjectNumberLocationCorpusDataSchema("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[DATA_SCHEMA]");
    // Make the request
    gcvv::DataSchema response = warehouseClient.GetDataSchema(name);
    

### GetDataSchema(GetDataSchemaRequest, CallSettings)
    
    
    public virtual DataSchema GetDataSchema(GetDataSchemaRequest request, CallSettings callSettings = null)

Gets data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetDataSchemaRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::GetDataSchemaRequest request = new gcvv::GetDataSchemaRequest
    {
        DataSchemaName = gcvv::DataSchemaName.FromProjectNumberLocationCorpusDataSchema("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[DATA_SCHEMA]"),
    };
    // Make the request
    gcvv::DataSchema response = warehouseClient.GetDataSchema(request);
    

### GetDataSchema(string, CallSettings)
    
    
    public virtual DataSchema GetDataSchema(string name, CallSettings callSettings = null)

Gets data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the data schema to retrieve. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/dataSchemas/{data_schema_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/dataSchemas/[DATA_SCHEMA]";
    // Make the request
    gcvv::DataSchema response = warehouseClient.GetDataSchema(name);
    

### GetDataSchemaAsync(DataSchemaName, CallSettings)
    
    
    public virtual Task<DataSchema> GetDataSchemaAsync(DataSchemaName name, CallSettings callSettings = null)

Gets data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchemaName)`  
Required. The name of the data schema to retrieve. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/dataSchemas/{data_schema_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DataSchemaName name = gcvv::DataSchemaName.FromProjectNumberLocationCorpusDataSchema("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[DATA_SCHEMA]");
    // Make the request
    gcvv::DataSchema response = await warehouseClient.GetDataSchemaAsync(name);
    

### GetDataSchemaAsync(DataSchemaName, CancellationToken)
    
    
    public virtual Task<DataSchema> GetDataSchemaAsync(DataSchemaName name, CancellationToken cancellationToken)

Gets data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchemaName)`  
Required. The name of the data schema to retrieve. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/dataSchemas/{data_schema_id}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DataSchemaName name = gcvv::DataSchemaName.FromProjectNumberLocationCorpusDataSchema("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[DATA_SCHEMA]");
    // Make the request
    gcvv::DataSchema response = await warehouseClient.GetDataSchemaAsync(name);
    

### GetDataSchemaAsync(GetDataSchemaRequest, CallSettings)
    
    
    public virtual Task<DataSchema> GetDataSchemaAsync(GetDataSchemaRequest request, CallSettings callSettings = null)

Gets data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetDataSchemaRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GetDataSchemaRequest request = new gcvv::GetDataSchemaRequest
    {
        DataSchemaName = gcvv::DataSchemaName.FromProjectNumberLocationCorpusDataSchema("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[DATA_SCHEMA]"),
    };
    // Make the request
    gcvv::DataSchema response = await warehouseClient.GetDataSchemaAsync(request);
    

### GetDataSchemaAsync(GetDataSchemaRequest, CancellationToken)
    
    
    public virtual Task<DataSchema> GetDataSchemaAsync(GetDataSchemaRequest request, CancellationToken cancellationToken)

Gets data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetDataSchemaRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GetDataSchemaRequest request = new gcvv::GetDataSchemaRequest
    {
        DataSchemaName = gcvv::DataSchemaName.FromProjectNumberLocationCorpusDataSchema("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[DATA_SCHEMA]"),
    };
    // Make the request
    gcvv::DataSchema response = await warehouseClient.GetDataSchemaAsync(request);
    

### GetDataSchemaAsync(string, CallSettings)
    
    
    public virtual Task<DataSchema> GetDataSchemaAsync(string name, CallSettings callSettings = null)

Gets data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the data schema to retrieve. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/dataSchemas/{data_schema_id}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/dataSchemas/[DATA_SCHEMA]";
    // Make the request
    gcvv::DataSchema response = await warehouseClient.GetDataSchemaAsync(name);
    

### GetDataSchemaAsync(string, CancellationToken)
    
    
    public virtual Task<DataSchema> GetDataSchemaAsync(string name, CancellationToken cancellationToken)

Gets data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the data schema to retrieve. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/dataSchemas/{data_schema_id}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/dataSchemas/[DATA_SCHEMA]";
    // Make the request
    gcvv::DataSchema response = await warehouseClient.GetDataSchemaAsync(name);
    

### GetIndex(GetIndexRequest, CallSettings)
    
    
    public virtual Index GetIndex(GetIndexRequest request, CallSettings callSettings = null)

Gets the details of a single Index under a Corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetIndexRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::GetIndexRequest request = new gcvv::GetIndexRequest
    {
        IndexName = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]"),
    };
    // Make the request
    gcvv::Index response = warehouseClient.GetIndex(request);
    

### GetIndex(IndexName, CallSettings)
    
    
    public virtual Index GetIndex(IndexName name, CallSettings callSettings = null)

Gets the details of a single Index under a Corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IndexName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexName)`  
Required. Name of the Index resource. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::IndexName name = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]");
    // Make the request
    gcvv::Index response = warehouseClient.GetIndex(name);
    

### GetIndex(string, CallSettings)
    
    
    public virtual Index GetIndex(string name, CallSettings callSettings = null)

Gets the details of a single Index under a Corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the Index resource. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/indexes/[INDEX]";
    // Make the request
    gcvv::Index response = warehouseClient.GetIndex(name);
    

### GetIndexAsync(GetIndexRequest, CallSettings)
    
    
    public virtual Task<Index> GetIndexAsync(GetIndexRequest request, CallSettings callSettings = null)

Gets the details of a single Index under a Corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetIndexRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GetIndexRequest request = new gcvv::GetIndexRequest
    {
        IndexName = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]"),
    };
    // Make the request
    gcvv::Index response = await warehouseClient.GetIndexAsync(request);
    

### GetIndexAsync(GetIndexRequest, CancellationToken)
    
    
    public virtual Task<Index> GetIndexAsync(GetIndexRequest request, CancellationToken cancellationToken)

Gets the details of a single Index under a Corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetIndexRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GetIndexRequest request = new gcvv::GetIndexRequest
    {
        IndexName = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]"),
    };
    // Make the request
    gcvv::Index response = await warehouseClient.GetIndexAsync(request);
    

### GetIndexAsync(IndexName, CallSettings)
    
    
    public virtual Task<Index> GetIndexAsync(IndexName name, CallSettings callSettings = null)

Gets the details of a single Index under a Corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IndexName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexName)`  
Required. Name of the Index resource. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::IndexName name = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]");
    // Make the request
    gcvv::Index response = await warehouseClient.GetIndexAsync(name);
    

### GetIndexAsync(IndexName, CancellationToken)
    
    
    public virtual Task<Index> GetIndexAsync(IndexName name, CancellationToken cancellationToken)

Gets the details of a single Index under a Corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IndexName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexName)`  
Required. Name of the Index resource. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::IndexName name = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]");
    // Make the request
    gcvv::Index response = await warehouseClient.GetIndexAsync(name);
    

### GetIndexAsync(string, CallSettings)
    
    
    public virtual Task<Index> GetIndexAsync(string name, CallSettings callSettings = null)

Gets the details of a single Index under a Corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the Index resource. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/indexes/[INDEX]";
    // Make the request
    gcvv::Index response = await warehouseClient.GetIndexAsync(name);
    

### GetIndexAsync(string, CancellationToken)
    
    
    public virtual Task<Index> GetIndexAsync(string name, CancellationToken cancellationToken)

Gets the details of a single Index under a Corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the Index resource. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/indexes/[INDEX]";
    // Make the request
    gcvv::Index response = await warehouseClient.GetIndexAsync(name);
    

### GetIndexEndpoint(GetIndexEndpointRequest, CallSettings)
    
    
    public virtual IndexEndpoint GetIndexEndpoint(GetIndexEndpointRequest request, CallSettings callSettings = null)

Gets an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIndexEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetIndexEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::GetIndexEndpointRequest request = new gcvv::GetIndexEndpointRequest
    {
        IndexEndpointName = gcvv::IndexEndpointName.FromProjectLocationIndexEndpoint("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]"),
    };
    // Make the request
    gcvv::IndexEndpoint response = warehouseClient.GetIndexEndpoint(request);
    

### GetIndexEndpoint(IndexEndpointName, CallSettings)
    
    
    public virtual IndexEndpoint GetIndexEndpoint(IndexEndpointName name, CallSettings callSettings = null)

Gets an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IndexEndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpointName)`  
Required. Name of the IndexEndpoint resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::IndexEndpointName name = gcvv::IndexEndpointName.FromProjectLocationIndexEndpoint("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]");
    // Make the request
    gcvv::IndexEndpoint response = warehouseClient.GetIndexEndpoint(name);
    

### GetIndexEndpoint(string, CallSettings)
    
    
    public virtual IndexEndpoint GetIndexEndpoint(string name, CallSettings callSettings = null)

Gets an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the IndexEndpoint resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/indexEndpoints/[INDEX_ENDPOINT]";
    // Make the request
    gcvv::IndexEndpoint response = warehouseClient.GetIndexEndpoint(name);
    

### GetIndexEndpointAsync(GetIndexEndpointRequest, CallSettings)
    
    
    public virtual Task<IndexEndpoint> GetIndexEndpointAsync(GetIndexEndpointRequest request, CallSettings callSettings = null)

Gets an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIndexEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetIndexEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GetIndexEndpointRequest request = new gcvv::GetIndexEndpointRequest
    {
        IndexEndpointName = gcvv::IndexEndpointName.FromProjectLocationIndexEndpoint("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]"),
    };
    // Make the request
    gcvv::IndexEndpoint response = await warehouseClient.GetIndexEndpointAsync(request);
    

### GetIndexEndpointAsync(GetIndexEndpointRequest, CancellationToken)
    
    
    public virtual Task<IndexEndpoint> GetIndexEndpointAsync(GetIndexEndpointRequest request, CancellationToken cancellationToken)

Gets an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIndexEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetIndexEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GetIndexEndpointRequest request = new gcvv::GetIndexEndpointRequest
    {
        IndexEndpointName = gcvv::IndexEndpointName.FromProjectLocationIndexEndpoint("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]"),
    };
    // Make the request
    gcvv::IndexEndpoint response = await warehouseClient.GetIndexEndpointAsync(request);
    

### GetIndexEndpointAsync(IndexEndpointName, CallSettings)
    
    
    public virtual Task<IndexEndpoint> GetIndexEndpointAsync(IndexEndpointName name, CallSettings callSettings = null)

Gets an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IndexEndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpointName)`  
Required. Name of the IndexEndpoint resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::IndexEndpointName name = gcvv::IndexEndpointName.FromProjectLocationIndexEndpoint("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]");
    // Make the request
    gcvv::IndexEndpoint response = await warehouseClient.GetIndexEndpointAsync(name);
    

### GetIndexEndpointAsync(IndexEndpointName, CancellationToken)
    
    
    public virtual Task<IndexEndpoint> GetIndexEndpointAsync(IndexEndpointName name, CancellationToken cancellationToken)

Gets an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[IndexEndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpointName)`  
Required. Name of the IndexEndpoint resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::IndexEndpointName name = gcvv::IndexEndpointName.FromProjectLocationIndexEndpoint("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]");
    // Make the request
    gcvv::IndexEndpoint response = await warehouseClient.GetIndexEndpointAsync(name);
    

### GetIndexEndpointAsync(string, CallSettings)
    
    
    public virtual Task<IndexEndpoint> GetIndexEndpointAsync(string name, CallSettings callSettings = null)

Gets an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the IndexEndpoint resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/indexEndpoints/[INDEX_ENDPOINT]";
    // Make the request
    gcvv::IndexEndpoint response = await warehouseClient.GetIndexEndpointAsync(name);
    

### GetIndexEndpointAsync(string, CancellationToken)
    
    
    public virtual Task<IndexEndpoint> GetIndexEndpointAsync(string name, CancellationToken cancellationToken)

Gets an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Name of the IndexEndpoint resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/indexEndpoints/[INDEX_ENDPOINT]";
    // Make the request
    gcvv::IndexEndpoint response = await warehouseClient.GetIndexEndpointAsync(name);
    

### GetSearchConfig(GetSearchConfigRequest, CallSettings)
    
    
    public virtual SearchConfig GetSearchConfig(GetSearchConfigRequest request, CallSettings callSettings = null)

Gets a search configuration inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSearchConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetSearchConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::GetSearchConfigRequest request = new gcvv::GetSearchConfigRequest
    {
        SearchConfigName = gcvv::SearchConfigName.FromProjectNumberLocationCorpusSearchConfig("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_CONFIG]"),
    };
    // Make the request
    gcvv::SearchConfig response = warehouseClient.GetSearchConfig(request);
    

### GetSearchConfig(SearchConfigName, CallSettings)
    
    
    public virtual SearchConfig GetSearchConfig(SearchConfigName name, CallSettings callSettings = null)

Gets a search configuration inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SearchConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfigName)`  
Required. The name of the search configuration to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchConfigs/{search_config}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::SearchConfigName name = gcvv::SearchConfigName.FromProjectNumberLocationCorpusSearchConfig("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_CONFIG]");
    // Make the request
    gcvv::SearchConfig response = warehouseClient.GetSearchConfig(name);
    

### GetSearchConfig(string, CallSettings)
    
    
    public virtual SearchConfig GetSearchConfig(string name, CallSettings callSettings = null)

Gets a search configuration inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the search configuration to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchConfigs/{search_config}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/searchConfigs/[SEARCH_CONFIG]";
    // Make the request
    gcvv::SearchConfig response = warehouseClient.GetSearchConfig(name);
    

### GetSearchConfigAsync(GetSearchConfigRequest, CallSettings)
    
    
    public virtual Task<SearchConfig> GetSearchConfigAsync(GetSearchConfigRequest request, CallSettings callSettings = null)

Gets a search configuration inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSearchConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetSearchConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GetSearchConfigRequest request = new gcvv::GetSearchConfigRequest
    {
        SearchConfigName = gcvv::SearchConfigName.FromProjectNumberLocationCorpusSearchConfig("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_CONFIG]"),
    };
    // Make the request
    gcvv::SearchConfig response = await warehouseClient.GetSearchConfigAsync(request);
    

### GetSearchConfigAsync(GetSearchConfigRequest, CancellationToken)
    
    
    public virtual Task<SearchConfig> GetSearchConfigAsync(GetSearchConfigRequest request, CancellationToken cancellationToken)

Gets a search configuration inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSearchConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetSearchConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GetSearchConfigRequest request = new gcvv::GetSearchConfigRequest
    {
        SearchConfigName = gcvv::SearchConfigName.FromProjectNumberLocationCorpusSearchConfig("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_CONFIG]"),
    };
    // Make the request
    gcvv::SearchConfig response = await warehouseClient.GetSearchConfigAsync(request);
    

### GetSearchConfigAsync(SearchConfigName, CallSettings)
    
    
    public virtual Task<SearchConfig> GetSearchConfigAsync(SearchConfigName name, CallSettings callSettings = null)

Gets a search configuration inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SearchConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfigName)`  
Required. The name of the search configuration to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchConfigs/{search_config}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::SearchConfigName name = gcvv::SearchConfigName.FromProjectNumberLocationCorpusSearchConfig("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_CONFIG]");
    // Make the request
    gcvv::SearchConfig response = await warehouseClient.GetSearchConfigAsync(name);
    

### GetSearchConfigAsync(SearchConfigName, CancellationToken)
    
    
    public virtual Task<SearchConfig> GetSearchConfigAsync(SearchConfigName name, CancellationToken cancellationToken)

Gets a search configuration inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SearchConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfigName)`  
Required. The name of the search configuration to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchConfigs/{search_config}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::SearchConfigName name = gcvv::SearchConfigName.FromProjectNumberLocationCorpusSearchConfig("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_CONFIG]");
    // Make the request
    gcvv::SearchConfig response = await warehouseClient.GetSearchConfigAsync(name);
    

### GetSearchConfigAsync(string, CallSettings)
    
    
    public virtual Task<SearchConfig> GetSearchConfigAsync(string name, CallSettings callSettings = null)

Gets a search configuration inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the search configuration to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchConfigs/{search_config}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/searchConfigs/[SEARCH_CONFIG]";
    // Make the request
    gcvv::SearchConfig response = await warehouseClient.GetSearchConfigAsync(name);
    

### GetSearchConfigAsync(string, CancellationToken)
    
    
    public virtual Task<SearchConfig> GetSearchConfigAsync(string name, CancellationToken cancellationToken)

Gets a search configuration inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the search configuration to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchConfigs/{search_config}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/searchConfigs/[SEARCH_CONFIG]";
    // Make the request
    gcvv::SearchConfig response = await warehouseClient.GetSearchConfigAsync(name);
    

### GetSearchHypernym(GetSearchHypernymRequest, CallSettings)
    
    
    public virtual SearchHypernym GetSearchHypernym(GetSearchHypernymRequest request, CallSettings callSettings = null)

Gets a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSearchHypernymRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetSearchHypernymRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::GetSearchHypernymRequest request = new gcvv::GetSearchHypernymRequest
    {
        SearchHypernymName = gcvv::SearchHypernymName.FromProjectNumberLocationCorpusSearchHypernym("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_HYPERNYM]"),
    };
    // Make the request
    gcvv::SearchHypernym response = warehouseClient.GetSearchHypernym(request);
    

### GetSearchHypernym(SearchHypernymName, CallSettings)
    
    
    public virtual SearchHypernym GetSearchHypernym(SearchHypernymName name, CallSettings callSettings = null)

Gets a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SearchHypernymName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernymName)`  
Required. The name of the SearchHypernym to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchHypernyms/{search_hypernym}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::SearchHypernymName name = gcvv::SearchHypernymName.FromProjectNumberLocationCorpusSearchHypernym("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_HYPERNYM]");
    // Make the request
    gcvv::SearchHypernym response = warehouseClient.GetSearchHypernym(name);
    

### GetSearchHypernym(string, CallSettings)
    
    
    public virtual SearchHypernym GetSearchHypernym(string name, CallSettings callSettings = null)

Gets a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the SearchHypernym to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchHypernyms/{search_hypernym}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/searchHypernyms/[SEARCH_HYPERNYM]";
    // Make the request
    gcvv::SearchHypernym response = warehouseClient.GetSearchHypernym(name);
    

### GetSearchHypernymAsync(GetSearchHypernymRequest, CallSettings)
    
    
    public virtual Task<SearchHypernym> GetSearchHypernymAsync(GetSearchHypernymRequest request, CallSettings callSettings = null)

Gets a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSearchHypernymRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetSearchHypernymRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GetSearchHypernymRequest request = new gcvv::GetSearchHypernymRequest
    {
        SearchHypernymName = gcvv::SearchHypernymName.FromProjectNumberLocationCorpusSearchHypernym("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_HYPERNYM]"),
    };
    // Make the request
    gcvv::SearchHypernym response = await warehouseClient.GetSearchHypernymAsync(request);
    

### GetSearchHypernymAsync(GetSearchHypernymRequest, CancellationToken)
    
    
    public virtual Task<SearchHypernym> GetSearchHypernymAsync(GetSearchHypernymRequest request, CancellationToken cancellationToken)

Gets a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSearchHypernymRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.GetSearchHypernymRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::GetSearchHypernymRequest request = new gcvv::GetSearchHypernymRequest
    {
        SearchHypernymName = gcvv::SearchHypernymName.FromProjectNumberLocationCorpusSearchHypernym("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_HYPERNYM]"),
    };
    // Make the request
    gcvv::SearchHypernym response = await warehouseClient.GetSearchHypernymAsync(request);
    

### GetSearchHypernymAsync(SearchHypernymName, CallSettings)
    
    
    public virtual Task<SearchHypernym> GetSearchHypernymAsync(SearchHypernymName name, CallSettings callSettings = null)

Gets a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SearchHypernymName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernymName)`  
Required. The name of the SearchHypernym to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchHypernyms/{search_hypernym}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::SearchHypernymName name = gcvv::SearchHypernymName.FromProjectNumberLocationCorpusSearchHypernym("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_HYPERNYM]");
    // Make the request
    gcvv::SearchHypernym response = await warehouseClient.GetSearchHypernymAsync(name);
    

### GetSearchHypernymAsync(SearchHypernymName, CancellationToken)
    
    
    public virtual Task<SearchHypernym> GetSearchHypernymAsync(SearchHypernymName name, CancellationToken cancellationToken)

Gets a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SearchHypernymName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernymName)`  
Required. The name of the SearchHypernym to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchHypernyms/{search_hypernym}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::SearchHypernymName name = gcvv::SearchHypernymName.FromProjectNumberLocationCorpusSearchHypernym("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[SEARCH_HYPERNYM]");
    // Make the request
    gcvv::SearchHypernym response = await warehouseClient.GetSearchHypernymAsync(name);
    

### GetSearchHypernymAsync(string, CallSettings)
    
    
    public virtual Task<SearchHypernym> GetSearchHypernymAsync(string name, CallSettings callSettings = null)

Gets a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the SearchHypernym to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchHypernyms/{search_hypernym}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/searchHypernyms/[SEARCH_HYPERNYM]";
    // Make the request
    gcvv::SearchHypernym response = await warehouseClient.GetSearchHypernymAsync(name);
    

### GetSearchHypernymAsync(string, CancellationToken)
    
    
    public virtual Task<SearchHypernym> GetSearchHypernymAsync(string name, CancellationToken cancellationToken)

Gets a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the SearchHypernym to retrieve. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchHypernyms/{search_hypernym}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/searchHypernyms/[SEARCH_HYPERNYM]";
    // Make the request
    gcvv::SearchHypernym response = await warehouseClient.GetSearchHypernymAsync(name);
    

### ImportAssets(ImportAssetsRequest, CallSettings)
    
    
    public virtual Operation<ImportAssetsResponse, ImportAssetsMetadata> ImportAssets(ImportAssetsRequest request, CallSettings callSettings = null)

Imports assets (images plus annotations) from a meta file on cloud storage. Each row in the meta file is corresponding to an image (specified by a cloud storage uri) and its annotations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportAssetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ImportAssetsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ImportAssetsResponse)[ImportAssetsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ImportAssetsMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::ImportAssetsRequest request = new gcvv::ImportAssetsRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        AssetsGcsUri = "",
    };
    // Make the request
    Operation<gcvv::ImportAssetsResponse, gcvv::ImportAssetsMetadata> response = warehouseClient.ImportAssets(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::ImportAssetsResponse, gcvv::ImportAssetsMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::ImportAssetsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::ImportAssetsResponse, gcvv::ImportAssetsMetadata> retrievedResponse = warehouseClient.PollOnceImportAssets(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::ImportAssetsResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportAssetsAsync(ImportAssetsRequest, CallSettings)
    
    
    public virtual Task<Operation<ImportAssetsResponse, ImportAssetsMetadata>> ImportAssetsAsync(ImportAssetsRequest request, CallSettings callSettings = null)

Imports assets (images plus annotations) from a meta file on cloud storage. Each row in the meta file is corresponding to an image (specified by a cloud storage uri) and its annotations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportAssetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ImportAssetsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ImportAssetsResponse)[ImportAssetsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ImportAssetsMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::ImportAssetsRequest request = new gcvv::ImportAssetsRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        AssetsGcsUri = "",
    };
    // Make the request
    Operation<gcvv::ImportAssetsResponse, gcvv::ImportAssetsMetadata> response = await warehouseClient.ImportAssetsAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::ImportAssetsResponse, gcvv::ImportAssetsMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::ImportAssetsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::ImportAssetsResponse, gcvv::ImportAssetsMetadata> retrievedResponse = await warehouseClient.PollOnceImportAssetsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::ImportAssetsResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportAssetsAsync(ImportAssetsRequest, CancellationToken)
    
    
    public virtual Task<Operation<ImportAssetsResponse, ImportAssetsMetadata>> ImportAssetsAsync(ImportAssetsRequest request, CancellationToken cancellationToken)

Imports assets (images plus annotations) from a meta file on cloud storage. Each row in the meta file is corresponding to an image (specified by a cloud storage uri) and its annotations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportAssetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ImportAssetsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ImportAssetsResponse)[ImportAssetsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ImportAssetsMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::ImportAssetsRequest request = new gcvv::ImportAssetsRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        AssetsGcsUri = "",
    };
    // Make the request
    Operation<gcvv::ImportAssetsResponse, gcvv::ImportAssetsMetadata> response = await warehouseClient.ImportAssetsAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::ImportAssetsResponse, gcvv::ImportAssetsMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::ImportAssetsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::ImportAssetsResponse, gcvv::ImportAssetsMetadata> retrievedResponse = await warehouseClient.PollOnceImportAssetsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::ImportAssetsResponse retrievedResult = retrievedResponse.Result;
    }
    

### IndexAsset(IndexAssetRequest, CallSettings)
    
    
    public virtual Operation<IndexAssetResponse, IndexAssetMetadata> IndexAsset(IndexAssetRequest request, CallSettings callSettings = null)

Index one asset for search. Supported corpus type: Corpus.Type.VIDEO_ON_DEMAND

**Parameters**  
---  
**Name** | **Description**  
`request` | `[IndexAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexAssetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexAssetResponse)[IndexAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexAssetMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::IndexAssetRequest request = new gcvv::IndexAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
        IndexAsIndexName = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]"),
    };
    // Make the request
    Operation<gcvv::IndexAssetResponse, gcvv::IndexAssetMetadata> response = warehouseClient.IndexAsset(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::IndexAssetResponse, gcvv::IndexAssetMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::IndexAssetResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::IndexAssetResponse, gcvv::IndexAssetMetadata> retrievedResponse = warehouseClient.PollOnceIndexAsset(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::IndexAssetResponse retrievedResult = retrievedResponse.Result;
    }
    

### IndexAssetAsync(IndexAssetRequest, CallSettings)
    
    
    public virtual Task<Operation<IndexAssetResponse, IndexAssetMetadata>> IndexAssetAsync(IndexAssetRequest request, CallSettings callSettings = null)

Index one asset for search. Supported corpus type: Corpus.Type.VIDEO_ON_DEMAND

**Parameters**  
---  
**Name** | **Description**  
`request` | `[IndexAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexAssetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexAssetResponse)[IndexAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexAssetMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::IndexAssetRequest request = new gcvv::IndexAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
        IndexAsIndexName = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]"),
    };
    // Make the request
    Operation<gcvv::IndexAssetResponse, gcvv::IndexAssetMetadata> response = await warehouseClient.IndexAssetAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::IndexAssetResponse, gcvv::IndexAssetMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::IndexAssetResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::IndexAssetResponse, gcvv::IndexAssetMetadata> retrievedResponse = await warehouseClient.PollOnceIndexAssetAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::IndexAssetResponse retrievedResult = retrievedResponse.Result;
    }
    

### IndexAssetAsync(IndexAssetRequest, CancellationToken)
    
    
    public virtual Task<Operation<IndexAssetResponse, IndexAssetMetadata>> IndexAssetAsync(IndexAssetRequest request, CancellationToken cancellationToken)

Index one asset for search. Supported corpus type: Corpus.Type.VIDEO_ON_DEMAND

**Parameters**  
---  
**Name** | **Description**  
`request` | `[IndexAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexAssetRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexAssetResponse)[IndexAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexAssetMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::IndexAssetRequest request = new gcvv::IndexAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
        IndexAsIndexName = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]"),
    };
    // Make the request
    Operation<gcvv::IndexAssetResponse, gcvv::IndexAssetMetadata> response = await warehouseClient.IndexAssetAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::IndexAssetResponse, gcvv::IndexAssetMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::IndexAssetResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::IndexAssetResponse, gcvv::IndexAssetMetadata> retrievedResponse = await warehouseClient.PollOnceIndexAssetAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::IndexAssetResponse retrievedResult = retrievedResponse.Result;
    }
    

### IngestAsset(CallSettings, BidirectionalStreamingSettings)
    
    
    public virtual WarehouseClient.IngestAssetStream IngestAsset(CallSettings callSettings = null, BidirectionalStreamingSettings streamingSettings = null)

Ingests data for the asset. It is not allowed to ingest a data chunk which is already expired according to TTL. This method is only available via the gRPC API (not HTTP since bi-directional streaming is not supported via HTTP).

**Parameters**  
---  
**Name** | **Description**  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
`streamingSettings` | `[BidirectionalStreamingSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingSettings.html)`  
If not null, applies streaming overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[WarehouseClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.WarehouseClient)[IngestAssetStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.WarehouseClient.IngestAssetStream)` | The client-server stream.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize streaming call, retrieving the stream object
    using gcvv::WarehouseClient.IngestAssetStream response = warehouseClient.IngestAsset();
    
    // Sending requests and retrieving responses can be arbitrarily interleaved
    // Exact sequence will depend on client/server behavior
    
    // Create task to do something with responses from server
    Task responseHandlerTask = Task.Run(async () =>
    {
        // Note that C# 8 code can use await foreach
        AsyncResponseStream<gcvv::IngestAssetResponse> responseStream = response.GetResponseStream();
        while (await responseStream.MoveNextAsync())
        {
            gcvv::IngestAssetResponse responseItem = responseStream.Current;
            // Do something with streamed response
        }
        // The response stream has completed
    });
    
    // Send requests to the server
    bool done = false;
    while (!done)
    {
        // Initialize a request
        gcvv::IngestAssetRequest request = new gcvv::IngestAssetRequest
        {
            Config = new gcvv::IngestAssetRequest.Types.Config(),
        };
        // Stream a request to the server
        await response.WriteAsync(request);
        // Set "done" to true when sending requests is complete
    }
    
    // Complete writing requests to the stream
    await response.WriteCompleteAsync();
    // Await the response handler
    // This will complete once all server responses have been processed
    await responseHandlerTask;
    

### ListAnnotations(AssetName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAnnotationsResponse, Annotation> ListAnnotations(AssetName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists a list of annotations inside asset.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AssetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AssetName)`  
The parent, which owns this collection of annotations. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAnnotationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAnnotationsResponse)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A pageable sequence of [Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::AssetName parent = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]");
    // Make the request
    PagedEnumerable<gcvv::ListAnnotationsResponse, gcvv::Annotation> response = warehouseClient.ListAnnotations(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::Annotation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListAnnotationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Annotation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Annotation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Annotation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAnnotations(ListAnnotationsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListAnnotationsResponse, Annotation> ListAnnotations(ListAnnotationsRequest request, CallSettings callSettings = null)

Lists a list of annotations inside asset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAnnotationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAnnotationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAnnotationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAnnotationsResponse)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A pageable sequence of [Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::ListAnnotationsRequest request = new gcvv::ListAnnotationsRequest
    {
        ParentAsAssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<gcvv::ListAnnotationsResponse, gcvv::Annotation> response = warehouseClient.ListAnnotations(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::Annotation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListAnnotationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Annotation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Annotation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Annotation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAnnotations(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAnnotationsResponse, Annotation> ListAnnotations(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists a list of annotations inside asset.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The parent, which owns this collection of annotations. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAnnotationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAnnotationsResponse)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A pageable sequence of [Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/assets/[ASSET]";
    // Make the request
    PagedEnumerable<gcvv::ListAnnotationsResponse, gcvv::Annotation> response = warehouseClient.ListAnnotations(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::Annotation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListAnnotationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Annotation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Annotation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Annotation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAnnotationsAsync(AssetName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAnnotationsResponse, Annotation> ListAnnotationsAsync(AssetName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists a list of annotations inside asset.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AssetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AssetName)`  
The parent, which owns this collection of annotations. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAnnotationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAnnotationsResponse)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A pageable asynchronous sequence of [Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::AssetName parent = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]");
    // Make the request
    PagedAsyncEnumerable<gcvv::ListAnnotationsResponse, gcvv::Annotation> response = warehouseClient.ListAnnotationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::Annotation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListAnnotationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Annotation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Annotation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Annotation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAnnotationsAsync(ListAnnotationsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAnnotationsResponse, Annotation> ListAnnotationsAsync(ListAnnotationsRequest request, CallSettings callSettings = null)

Lists a list of annotations inside asset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAnnotationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAnnotationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAnnotationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAnnotationsResponse)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A pageable asynchronous sequence of [Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::ListAnnotationsRequest request = new gcvv::ListAnnotationsRequest
    {
        ParentAsAssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<gcvv::ListAnnotationsResponse, gcvv::Annotation> response = warehouseClient.ListAnnotationsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::Annotation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListAnnotationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Annotation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Annotation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Annotation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAnnotationsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAnnotationsResponse, Annotation> ListAnnotationsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists a list of annotations inside asset.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The parent, which owns this collection of annotations. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAnnotationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAnnotationsResponse)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A pageable asynchronous sequence of [Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/assets/[ASSET]";
    // Make the request
    PagedAsyncEnumerable<gcvv::ListAnnotationsResponse, gcvv::Annotation> response = warehouseClient.ListAnnotationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::Annotation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListAnnotationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Annotation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Annotation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Annotation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAssets(CorpusName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAssetsResponse, Asset> ListAssets(CorpusName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists an list of assets inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent, which owns this collection of assets. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAssetsResponse)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A pageable sequence of [Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    // Make the request
    PagedEnumerable<gcvv::ListAssetsResponse, gcvv::Asset> response = warehouseClient.ListAssets(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::Asset item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListAssetsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Asset item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Asset> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Asset item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAssets(ListAssetsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListAssetsResponse, Asset> ListAssets(ListAssetsRequest request, CallSettings callSettings = null)

Lists an list of assets inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAssetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAssetsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAssetsResponse)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A pageable sequence of [Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::ListAssetsRequest request = new gcvv::ListAssetsRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<gcvv::ListAssetsResponse, gcvv::Asset> response = warehouseClient.ListAssets(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::Asset item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListAssetsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Asset item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Asset> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Asset item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAssets(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAssetsResponse, Asset> ListAssets(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists an list of assets inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of assets. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAssetsResponse)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A pageable sequence of [Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    // Make the request
    PagedEnumerable<gcvv::ListAssetsResponse, gcvv::Asset> response = warehouseClient.ListAssets(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::Asset item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListAssetsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Asset item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Asset> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Asset item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAssetsAsync(CorpusName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAssetsResponse, Asset> ListAssetsAsync(CorpusName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists an list of assets inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent, which owns this collection of assets. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAssetsResponse)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A pageable asynchronous sequence of [Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    // Make the request
    PagedAsyncEnumerable<gcvv::ListAssetsResponse, gcvv::Asset> response = warehouseClient.ListAssetsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::Asset item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListAssetsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Asset item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Asset> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Asset item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAssetsAsync(ListAssetsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAssetsResponse, Asset> ListAssetsAsync(ListAssetsRequest request, CallSettings callSettings = null)

Lists an list of assets inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAssetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAssetsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAssetsResponse)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A pageable asynchronous sequence of [Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::ListAssetsRequest request = new gcvv::ListAssetsRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<gcvv::ListAssetsResponse, gcvv::Asset> response = warehouseClient.ListAssetsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::Asset item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListAssetsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Asset item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Asset> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Asset item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAssetsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAssetsResponse, Asset> ListAssetsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists an list of assets inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of assets. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListAssetsResponse)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A pageable asynchronous sequence of [Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    // Make the request
    PagedAsyncEnumerable<gcvv::ListAssetsResponse, gcvv::Asset> response = warehouseClient.ListAssetsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::Asset item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListAssetsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Asset item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Asset> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Asset item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCollections(CorpusName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListCollectionsResponse, Collection> ListCollections(CorpusName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists collections inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent corpus. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCollectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListCollectionsResponse)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | A pageable sequence of [Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    // Make the request
    PagedEnumerable<gcvv::ListCollectionsResponse, gcvv::Collection> response = warehouseClient.ListCollections(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::Collection item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListCollectionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Collection item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Collection> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Collection item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCollections(ListCollectionsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListCollectionsResponse, Collection> ListCollections(ListCollectionsRequest request, CallSettings callSettings = null)

Lists collections inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCollectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListCollectionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCollectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListCollectionsResponse)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | A pageable sequence of [Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::ListCollectionsRequest request = new gcvv::ListCollectionsRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
    };
    // Make the request
    PagedEnumerable<gcvv::ListCollectionsResponse, gcvv::Collection> response = warehouseClient.ListCollections(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::Collection item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListCollectionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Collection item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Collection> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Collection item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCollections(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListCollectionsResponse, Collection> ListCollections(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists collections inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent corpus. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCollectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListCollectionsResponse)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | A pageable sequence of [Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    // Make the request
    PagedEnumerable<gcvv::ListCollectionsResponse, gcvv::Collection> response = warehouseClient.ListCollections(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::Collection item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListCollectionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Collection item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Collection> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Collection item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCollectionsAsync(CorpusName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCollectionsResponse, Collection> ListCollectionsAsync(CorpusName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists collections inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent corpus. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCollectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListCollectionsResponse)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | A pageable asynchronous sequence of [Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    // Make the request
    PagedAsyncEnumerable<gcvv::ListCollectionsResponse, gcvv::Collection> response = warehouseClient.ListCollectionsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::Collection item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListCollectionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Collection item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Collection> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Collection item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCollectionsAsync(ListCollectionsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCollectionsResponse, Collection> ListCollectionsAsync(ListCollectionsRequest request, CallSettings callSettings = null)

Lists collections inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCollectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListCollectionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCollectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListCollectionsResponse)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | A pageable asynchronous sequence of [Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::ListCollectionsRequest request = new gcvv::ListCollectionsRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
    };
    // Make the request
    PagedAsyncEnumerable<gcvv::ListCollectionsResponse, gcvv::Collection> response = warehouseClient.ListCollectionsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::Collection item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListCollectionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Collection item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Collection> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Collection item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCollectionsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCollectionsResponse, Collection> ListCollectionsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists collections inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent corpus. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCollectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListCollectionsResponse)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | A pageable asynchronous sequence of [Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    // Make the request
    PagedAsyncEnumerable<gcvv::ListCollectionsResponse, gcvv::Collection> response = warehouseClient.ListCollectionsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::Collection item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListCollectionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Collection item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Collection> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Collection item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCorpora(ListCorporaRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListCorporaResponse, Corpus> ListCorpora(ListCorporaRequest request, CallSettings callSettings = null)

Lists all corpora in a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCorporaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListCorporaRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCorporaResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListCorporaResponse)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)` | A pageable sequence of [Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::ListCorporaRequest request = new gcvv::ListCorporaRequest
    {
        Parent = "",
        Filter = "",
    };
    // Make the request
    PagedEnumerable<gcvv::ListCorporaResponse, gcvv::Corpus> response = warehouseClient.ListCorpora(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::Corpus item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListCorporaResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Corpus item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Corpus> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Corpus item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCorpora(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListCorporaResponse, Corpus> ListCorpora(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all corpora in a project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the project from which to list corpora.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListCorporaResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListCorporaResponse)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)` | A pageable sequence of [Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string parent = "";
    // Make the request
    PagedEnumerable<gcvv::ListCorporaResponse, gcvv::Corpus> response = warehouseClient.ListCorpora(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::Corpus item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListCorporaResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Corpus item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Corpus> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Corpus item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCorporaAsync(ListCorporaRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCorporaResponse, Corpus> ListCorporaAsync(ListCorporaRequest request, CallSettings callSettings = null)

Lists all corpora in a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCorporaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListCorporaRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCorporaResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListCorporaResponse)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)` | A pageable asynchronous sequence of [Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::ListCorporaRequest request = new gcvv::ListCorporaRequest
    {
        Parent = "",
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<gcvv::ListCorporaResponse, gcvv::Corpus> response = warehouseClient.ListCorporaAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::Corpus item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListCorporaResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Corpus item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Corpus> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Corpus item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListCorporaAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListCorporaResponse, Corpus> ListCorporaAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all corpora in a project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the project from which to list corpora.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListCorporaResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListCorporaResponse)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)` | A pageable asynchronous sequence of [Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "";
    // Make the request
    PagedAsyncEnumerable<gcvv::ListCorporaResponse, gcvv::Corpus> response = warehouseClient.ListCorporaAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::Corpus item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListCorporaResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Corpus item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Corpus> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Corpus item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDataSchemas(CorpusName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDataSchemasResponse, DataSchema> ListDataSchemas(CorpusName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists a list of data schemas inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent, which owns this collection of data schemas. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDataSchemasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListDataSchemasResponse)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A pageable sequence of [DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    // Make the request
    PagedEnumerable<gcvv::ListDataSchemasResponse, gcvv::DataSchema> response = warehouseClient.ListDataSchemas(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::DataSchema item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListDataSchemasResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::DataSchema item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::DataSchema> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::DataSchema item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDataSchemas(ListDataSchemasRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListDataSchemasResponse, DataSchema> ListDataSchemas(ListDataSchemasRequest request, CallSettings callSettings = null)

Lists a list of data schemas inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataSchemasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListDataSchemasRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDataSchemasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListDataSchemasResponse)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A pageable sequence of [DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::ListDataSchemasRequest request = new gcvv::ListDataSchemasRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
    };
    // Make the request
    PagedEnumerable<gcvv::ListDataSchemasResponse, gcvv::DataSchema> response = warehouseClient.ListDataSchemas(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::DataSchema item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListDataSchemasResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::DataSchema item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::DataSchema> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::DataSchema item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDataSchemas(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDataSchemasResponse, DataSchema> ListDataSchemas(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists a list of data schemas inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of data schemas. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDataSchemasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListDataSchemasResponse)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A pageable sequence of [DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    // Make the request
    PagedEnumerable<gcvv::ListDataSchemasResponse, gcvv::DataSchema> response = warehouseClient.ListDataSchemas(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::DataSchema item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListDataSchemasResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::DataSchema item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::DataSchema> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::DataSchema item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDataSchemasAsync(CorpusName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDataSchemasResponse, DataSchema> ListDataSchemasAsync(CorpusName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists a list of data schemas inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent, which owns this collection of data schemas. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDataSchemasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListDataSchemasResponse)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A pageable asynchronous sequence of [DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    // Make the request
    PagedAsyncEnumerable<gcvv::ListDataSchemasResponse, gcvv::DataSchema> response = warehouseClient.ListDataSchemasAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::DataSchema item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListDataSchemasResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::DataSchema item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::DataSchema> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::DataSchema item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDataSchemasAsync(ListDataSchemasRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDataSchemasResponse, DataSchema> ListDataSchemasAsync(ListDataSchemasRequest request, CallSettings callSettings = null)

Lists a list of data schemas inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataSchemasRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListDataSchemasRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDataSchemasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListDataSchemasResponse)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A pageable asynchronous sequence of [DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::ListDataSchemasRequest request = new gcvv::ListDataSchemasRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
    };
    // Make the request
    PagedAsyncEnumerable<gcvv::ListDataSchemasResponse, gcvv::DataSchema> response = warehouseClient.ListDataSchemasAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::DataSchema item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListDataSchemasResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::DataSchema item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::DataSchema> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::DataSchema item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDataSchemasAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDataSchemasResponse, DataSchema> ListDataSchemasAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists a list of data schemas inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of data schemas. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDataSchemasResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListDataSchemasResponse)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A pageable asynchronous sequence of [DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    // Make the request
    PagedAsyncEnumerable<gcvv::ListDataSchemasResponse, gcvv::DataSchema> response = warehouseClient.ListDataSchemasAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::DataSchema item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListDataSchemasResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::DataSchema item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::DataSchema> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::DataSchema item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIndexEndpoints(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListIndexEndpointsResponse, IndexEndpoint> ListIndexEndpoints(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all IndexEndpoints in a project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListIndexEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListIndexEndpointsResponse)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)` | A pageable sequence of [IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<gcvv::ListIndexEndpointsResponse, gcvv::IndexEndpoint> response = warehouseClient.ListIndexEndpoints(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::IndexEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListIndexEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::IndexEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::IndexEndpoint> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::IndexEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIndexEndpoints(ListIndexEndpointsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListIndexEndpointsResponse, IndexEndpoint> ListIndexEndpoints(ListIndexEndpointsRequest request, CallSettings callSettings = null)

Lists all IndexEndpoints in a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListIndexEndpointsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListIndexEndpointsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListIndexEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListIndexEndpointsResponse)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)` | A pageable sequence of [IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::ListIndexEndpointsRequest request = new gcvv::ListIndexEndpointsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<gcvv::ListIndexEndpointsResponse, gcvv::IndexEndpoint> response = warehouseClient.ListIndexEndpoints(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::IndexEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListIndexEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::IndexEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::IndexEndpoint> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::IndexEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIndexEndpoints(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListIndexEndpointsResponse, IndexEndpoint> ListIndexEndpoints(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all IndexEndpoints in a project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListIndexEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListIndexEndpointsResponse)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)` | A pageable sequence of [IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<gcvv::ListIndexEndpointsResponse, gcvv::IndexEndpoint> response = warehouseClient.ListIndexEndpoints(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::IndexEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListIndexEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::IndexEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::IndexEndpoint> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::IndexEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIndexEndpointsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListIndexEndpointsResponse, IndexEndpoint> ListIndexEndpointsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all IndexEndpoints in a project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListIndexEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListIndexEndpointsResponse)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)` | A pageable asynchronous sequence of [IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<gcvv::ListIndexEndpointsResponse, gcvv::IndexEndpoint> response = warehouseClient.ListIndexEndpointsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::IndexEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListIndexEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::IndexEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::IndexEndpoint> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::IndexEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIndexEndpointsAsync(ListIndexEndpointsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListIndexEndpointsResponse, IndexEndpoint> ListIndexEndpointsAsync(ListIndexEndpointsRequest request, CallSettings callSettings = null)

Lists all IndexEndpoints in a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListIndexEndpointsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListIndexEndpointsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListIndexEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListIndexEndpointsResponse)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)` | A pageable asynchronous sequence of [IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::ListIndexEndpointsRequest request = new gcvv::ListIndexEndpointsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<gcvv::ListIndexEndpointsResponse, gcvv::IndexEndpoint> response = warehouseClient.ListIndexEndpointsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::IndexEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListIndexEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::IndexEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::IndexEndpoint> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::IndexEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIndexEndpointsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListIndexEndpointsResponse, IndexEndpoint> ListIndexEndpointsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all IndexEndpoints in a project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListIndexEndpointsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListIndexEndpointsResponse)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)` | A pageable asynchronous sequence of [IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<gcvv::ListIndexEndpointsResponse, gcvv::IndexEndpoint> response = warehouseClient.ListIndexEndpointsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::IndexEndpoint item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListIndexEndpointsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::IndexEndpoint item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::IndexEndpoint> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::IndexEndpoint item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIndexes(CorpusName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListIndexesResponse, Index> ListIndexes(CorpusName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List all Indexes in a given Corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent corpus that owns this collection of indexes. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListIndexesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListIndexesResponse)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)` | A pageable sequence of [Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    // Make the request
    PagedEnumerable<gcvv::ListIndexesResponse, gcvv::Index> response = warehouseClient.ListIndexes(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::Index item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListIndexesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Index item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Index> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Index item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIndexes(ListIndexesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListIndexesResponse, Index> ListIndexes(ListIndexesRequest request, CallSettings callSettings = null)

List all Indexes in a given Corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListIndexesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListIndexesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListIndexesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListIndexesResponse)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)` | A pageable sequence of [Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::ListIndexesRequest request = new gcvv::ListIndexesRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
    };
    // Make the request
    PagedEnumerable<gcvv::ListIndexesResponse, gcvv::Index> response = warehouseClient.ListIndexes(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::Index item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListIndexesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Index item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Index> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Index item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIndexes(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListIndexesResponse, Index> ListIndexes(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List all Indexes in a given Corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent corpus that owns this collection of indexes. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListIndexesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListIndexesResponse)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)` | A pageable sequence of [Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    // Make the request
    PagedEnumerable<gcvv::ListIndexesResponse, gcvv::Index> response = warehouseClient.ListIndexes(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::Index item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListIndexesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Index item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Index> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Index item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIndexesAsync(CorpusName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListIndexesResponse, Index> ListIndexesAsync(CorpusName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List all Indexes in a given Corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent corpus that owns this collection of indexes. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListIndexesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListIndexesResponse)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)` | A pageable asynchronous sequence of [Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    // Make the request
    PagedAsyncEnumerable<gcvv::ListIndexesResponse, gcvv::Index> response = warehouseClient.ListIndexesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::Index item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListIndexesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Index item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Index> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Index item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIndexesAsync(ListIndexesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListIndexesResponse, Index> ListIndexesAsync(ListIndexesRequest request, CallSettings callSettings = null)

List all Indexes in a given Corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListIndexesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListIndexesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListIndexesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListIndexesResponse)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)` | A pageable asynchronous sequence of [Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::ListIndexesRequest request = new gcvv::ListIndexesRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
    };
    // Make the request
    PagedAsyncEnumerable<gcvv::ListIndexesResponse, gcvv::Index> response = warehouseClient.ListIndexesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::Index item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListIndexesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Index item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Index> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Index item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListIndexesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListIndexesResponse, Index> ListIndexesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List all Indexes in a given Corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent corpus that owns this collection of indexes. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListIndexesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListIndexesResponse)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)` | A pageable asynchronous sequence of [Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    // Make the request
    PagedAsyncEnumerable<gcvv::ListIndexesResponse, gcvv::Index> response = warehouseClient.ListIndexesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::Index item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListIndexesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::Index item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::Index> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::Index item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSearchConfigs(CorpusName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListSearchConfigsResponse, SearchConfig> ListSearchConfigs(CorpusName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all search configurations inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent, which owns this collection of search configurations. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSearchConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListSearchConfigsResponse)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A pageable sequence of [SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    // Make the request
    PagedEnumerable<gcvv::ListSearchConfigsResponse, gcvv::SearchConfig> response = warehouseClient.ListSearchConfigs(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::SearchConfig item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListSearchConfigsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::SearchConfig item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::SearchConfig> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::SearchConfig item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSearchConfigs(ListSearchConfigsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListSearchConfigsResponse, SearchConfig> ListSearchConfigs(ListSearchConfigsRequest request, CallSettings callSettings = null)

Lists all search configurations inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSearchConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListSearchConfigsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSearchConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListSearchConfigsResponse)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A pageable sequence of [SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::ListSearchConfigsRequest request = new gcvv::ListSearchConfigsRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
    };
    // Make the request
    PagedEnumerable<gcvv::ListSearchConfigsResponse, gcvv::SearchConfig> response = warehouseClient.ListSearchConfigs(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::SearchConfig item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListSearchConfigsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::SearchConfig item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::SearchConfig> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::SearchConfig item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSearchConfigs(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListSearchConfigsResponse, SearchConfig> ListSearchConfigs(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all search configurations inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of search configurations. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSearchConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListSearchConfigsResponse)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A pageable sequence of [SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    // Make the request
    PagedEnumerable<gcvv::ListSearchConfigsResponse, gcvv::SearchConfig> response = warehouseClient.ListSearchConfigs(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::SearchConfig item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListSearchConfigsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::SearchConfig item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::SearchConfig> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::SearchConfig item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSearchConfigsAsync(CorpusName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSearchConfigsResponse, SearchConfig> ListSearchConfigsAsync(CorpusName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all search configurations inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent, which owns this collection of search configurations. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSearchConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListSearchConfigsResponse)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A pageable asynchronous sequence of [SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    // Make the request
    PagedAsyncEnumerable<gcvv::ListSearchConfigsResponse, gcvv::SearchConfig> response = warehouseClient.ListSearchConfigsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::SearchConfig item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListSearchConfigsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::SearchConfig item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::SearchConfig> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::SearchConfig item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSearchConfigsAsync(ListSearchConfigsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSearchConfigsResponse, SearchConfig> ListSearchConfigsAsync(ListSearchConfigsRequest request, CallSettings callSettings = null)

Lists all search configurations inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSearchConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListSearchConfigsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSearchConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListSearchConfigsResponse)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A pageable asynchronous sequence of [SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::ListSearchConfigsRequest request = new gcvv::ListSearchConfigsRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
    };
    // Make the request
    PagedAsyncEnumerable<gcvv::ListSearchConfigsResponse, gcvv::SearchConfig> response = warehouseClient.ListSearchConfigsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::SearchConfig item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListSearchConfigsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::SearchConfig item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::SearchConfig> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::SearchConfig item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSearchConfigsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSearchConfigsResponse, SearchConfig> ListSearchConfigsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists all search configurations inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of search configurations. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSearchConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListSearchConfigsResponse)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A pageable asynchronous sequence of [SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    // Make the request
    PagedAsyncEnumerable<gcvv::ListSearchConfigsResponse, gcvv::SearchConfig> response = warehouseClient.ListSearchConfigsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::SearchConfig item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListSearchConfigsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::SearchConfig item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::SearchConfig> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::SearchConfig item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSearchHypernyms(CorpusName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListSearchHypernymsResponse, SearchHypernym> ListSearchHypernyms(CorpusName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists SearchHypernyms inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent, which owns this collection of SearchHypernyms. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSearchHypernymsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListSearchHypernymsResponse)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A pageable sequence of [SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    // Make the request
    PagedEnumerable<gcvv::ListSearchHypernymsResponse, gcvv::SearchHypernym> response = warehouseClient.ListSearchHypernyms(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::SearchHypernym item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListSearchHypernymsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::SearchHypernym item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::SearchHypernym> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::SearchHypernym item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSearchHypernyms(ListSearchHypernymsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListSearchHypernymsResponse, SearchHypernym> ListSearchHypernyms(ListSearchHypernymsRequest request, CallSettings callSettings = null)

Lists SearchHypernyms inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSearchHypernymsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListSearchHypernymsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSearchHypernymsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListSearchHypernymsResponse)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A pageable sequence of [SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::ListSearchHypernymsRequest request = new gcvv::ListSearchHypernymsRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
    };
    // Make the request
    PagedEnumerable<gcvv::ListSearchHypernymsResponse, gcvv::SearchHypernym> response = warehouseClient.ListSearchHypernyms(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::SearchHypernym item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListSearchHypernymsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::SearchHypernym item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::SearchHypernym> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::SearchHypernym item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSearchHypernyms(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListSearchHypernymsResponse, SearchHypernym> ListSearchHypernyms(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists SearchHypernyms inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of SearchHypernyms. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSearchHypernymsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListSearchHypernymsResponse)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A pageable sequence of [SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    // Make the request
    PagedEnumerable<gcvv::ListSearchHypernymsResponse, gcvv::SearchHypernym> response = warehouseClient.ListSearchHypernyms(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::SearchHypernym item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ListSearchHypernymsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::SearchHypernym item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::SearchHypernym> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::SearchHypernym item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSearchHypernymsAsync(CorpusName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSearchHypernymsResponse, SearchHypernym> ListSearchHypernymsAsync(CorpusName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists SearchHypernyms inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)`  
Required. The parent, which owns this collection of SearchHypernyms. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSearchHypernymsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListSearchHypernymsResponse)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A pageable asynchronous sequence of [SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CorpusName parent = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]");
    // Make the request
    PagedAsyncEnumerable<gcvv::ListSearchHypernymsResponse, gcvv::SearchHypernym> response = warehouseClient.ListSearchHypernymsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::SearchHypernym item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListSearchHypernymsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::SearchHypernym item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::SearchHypernym> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::SearchHypernym item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSearchHypernymsAsync(ListSearchHypernymsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSearchHypernymsResponse, SearchHypernym> ListSearchHypernymsAsync(ListSearchHypernymsRequest request, CallSettings callSettings = null)

Lists SearchHypernyms inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSearchHypernymsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListSearchHypernymsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSearchHypernymsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListSearchHypernymsResponse)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A pageable asynchronous sequence of [SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::ListSearchHypernymsRequest request = new gcvv::ListSearchHypernymsRequest
    {
        ParentAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
    };
    // Make the request
    PagedAsyncEnumerable<gcvv::ListSearchHypernymsResponse, gcvv::SearchHypernym> response = warehouseClient.ListSearchHypernymsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::SearchHypernym item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListSearchHypernymsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::SearchHypernym item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::SearchHypernym> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::SearchHypernym item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSearchHypernymsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSearchHypernymsResponse, SearchHypernym> ListSearchHypernymsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists SearchHypernyms inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent, which owns this collection of SearchHypernyms. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSearchHypernymsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ListSearchHypernymsResponse)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A pageable asynchronous sequence of [SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]";
    // Make the request
    PagedAsyncEnumerable<gcvv::ListSearchHypernymsResponse, gcvv::SearchHypernym> response = warehouseClient.ListSearchHypernymsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::SearchHypernym item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ListSearchHypernymsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::SearchHypernym item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::SearchHypernym> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::SearchHypernym item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceAnalyzeAsset(string, CallSettings)
    
    
    public virtual Operation<AnalyzeAssetResponse, AnalyzeAssetMetadata> PollOnceAnalyzeAsset(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `AnalyzeAsset`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnalyzeAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeAssetResponse)[AnalyzeAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeAssetMetadata)` | The result of polling the operation.  
  
### PollOnceAnalyzeAssetAsync(string, CallSettings)
    
    
    public virtual Task<Operation<AnalyzeAssetResponse, AnalyzeAssetMetadata>> PollOnceAnalyzeAssetAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `AnalyzeAsset`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnalyzeAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeAssetResponse)[AnalyzeAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeAssetMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceAnalyzeCorpus(string, CallSettings)
    
    
    public virtual Operation<AnalyzeCorpusResponse, AnalyzeCorpusMetadata> PollOnceAnalyzeCorpus(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `AnalyzeCorpus`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnalyzeCorpusResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeCorpusResponse)[AnalyzeCorpusMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeCorpusMetadata)` | The result of polling the operation.  
  
### PollOnceAnalyzeCorpusAsync(string, CallSettings)
    
    
    public virtual Task<Operation<AnalyzeCorpusResponse, AnalyzeCorpusMetadata>> PollOnceAnalyzeCorpusAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `AnalyzeCorpus`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[AnalyzeCorpusResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeCorpusResponse)[AnalyzeCorpusMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.AnalyzeCorpusMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateCollection(string, CallSettings)
    
    
    public virtual Operation<Collection, CreateCollectionMetadata> PollOnceCreateCollection(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateCollection`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)[CreateCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCollectionMetadata)` | The result of polling the operation.  
  
### PollOnceCreateCollectionAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Collection, CreateCollectionMetadata>> PollOnceCreateCollectionAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateCollection`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)[CreateCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCollectionMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateCorpus(string, CallSettings)
    
    
    public virtual Operation<Corpus, CreateCorpusMetadata> PollOnceCreateCorpus(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateCorpus`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)[CreateCorpusMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCorpusMetadata)` | The result of polling the operation.  
  
### PollOnceCreateCorpusAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Corpus, CreateCorpusMetadata>> PollOnceCreateCorpusAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateCorpus`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)[CreateCorpusMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateCorpusMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateIndex(string, CallSettings)
    
    
    public virtual Operation<Index, CreateIndexMetadata> PollOnceCreateIndex(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateIndex`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)[CreateIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexMetadata)` | The result of polling the operation.  
  
### PollOnceCreateIndexAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Index, CreateIndexMetadata>> PollOnceCreateIndexAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateIndex`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)[CreateIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateIndexEndpoint(string, CallSettings)
    
    
    public virtual Operation<IndexEndpoint, CreateIndexEndpointMetadata> PollOnceCreateIndexEndpoint(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateIndexEndpoint` .

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)[CreateIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexEndpointMetadata)` | The result of polling the operation.  
  
### PollOnceCreateIndexEndpointAsync(string, CallSettings)
    
    
    public virtual Task<Operation<IndexEndpoint, CreateIndexEndpointMetadata>> PollOnceCreateIndexEndpointAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateIndexEndpoint`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)[CreateIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CreateIndexEndpointMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteAsset(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteAssetMetadata> PollOnceDeleteAsset(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteAsset`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAssetMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteAssetAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteAssetMetadata>> PollOnceDeleteAssetAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteAsset`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteAssetMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteCollection(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteCollectionMetadata> PollOnceDeleteCollection(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteCollection`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteCollectionMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteCollectionAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteCollectionMetadata>> PollOnceDeleteCollectionAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteCollection`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteCollectionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteCollectionMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteIndex(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteIndexMetadata> PollOnceDeleteIndex(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteIndex`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteIndexAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteIndexMetadata>> PollOnceDeleteIndexAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteIndex`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteIndexEndpoint(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteIndexEndpointMetadata> PollOnceDeleteIndexEndpoint(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteIndexEndpoint` .

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexEndpointMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteIndexEndpointAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteIndexEndpointMetadata>> PollOnceDeleteIndexEndpointAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteIndexEndpoint`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeleteIndexEndpointMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeployIndex(string, CallSettings)
    
    
    public virtual Operation<DeployIndexResponse, DeployIndexMetadata> PollOnceDeployIndex(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeployIndex`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployIndexResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployIndexResponse)[DeployIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployIndexMetadata)` | The result of polling the operation.  
  
### PollOnceDeployIndexAsync(string, CallSettings)
    
    
    public virtual Task<Operation<DeployIndexResponse, DeployIndexMetadata>> PollOnceDeployIndexAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeployIndex`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[DeployIndexResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployIndexResponse)[DeployIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DeployIndexMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceImportAssets(string, CallSettings)
    
    
    public virtual Operation<ImportAssetsResponse, ImportAssetsMetadata> PollOnceImportAssets(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `ImportAssets`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ImportAssetsResponse)[ImportAssetsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ImportAssetsMetadata)` | The result of polling the operation.  
  
### PollOnceImportAssetsAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ImportAssetsResponse, ImportAssetsMetadata>> PollOnceImportAssetsAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `ImportAssets`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ImportAssetsResponse)[ImportAssetsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ImportAssetsMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceIndexAsset(string, CallSettings)
    
    
    public virtual Operation<IndexAssetResponse, IndexAssetMetadata> PollOnceIndexAsset(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `IndexAsset`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexAssetResponse)[IndexAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexAssetMetadata)` | The result of polling the operation.  
  
### PollOnceIndexAssetAsync(string, CallSettings)
    
    
    public virtual Task<Operation<IndexAssetResponse, IndexAssetMetadata>> PollOnceIndexAssetAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `IndexAsset`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexAssetResponse)[IndexAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexAssetMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceRemoveIndexAsset(string, CallSettings)
    
    
    public virtual Operation<RemoveIndexAssetResponse, RemoveIndexAssetMetadata> PollOnceRemoveIndexAsset(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `RemoveIndexAsset`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RemoveIndexAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveIndexAssetResponse)[RemoveIndexAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveIndexAssetMetadata)` | The result of polling the operation.  
  
### PollOnceRemoveIndexAssetAsync(string, CallSettings)
    
    
    public virtual Task<Operation<RemoveIndexAssetResponse, RemoveIndexAssetMetadata>> PollOnceRemoveIndexAssetAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `RemoveIndexAsset`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RemoveIndexAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveIndexAssetResponse)[RemoveIndexAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveIndexAssetMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUndeployIndex(string, CallSettings)
    
    
    public virtual Operation<UndeployIndexResponse, UndeployIndexMetadata> PollOnceUndeployIndex(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UndeployIndex`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UndeployIndexResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployIndexResponse)[UndeployIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployIndexMetadata)` | The result of polling the operation.  
  
### PollOnceUndeployIndexAsync(string, CallSettings)
    
    
    public virtual Task<Operation<UndeployIndexResponse, UndeployIndexMetadata>> PollOnceUndeployIndexAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UndeployIndex`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UndeployIndexResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployIndexResponse)[UndeployIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployIndexMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateIndex(string, CallSettings)
    
    
    public virtual Operation<Index, UpdateIndexMetadata> PollOnceUpdateIndex(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateIndex`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)[UpdateIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateIndexAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Index, UpdateIndexMetadata>> PollOnceUpdateIndexAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateIndex`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)[UpdateIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateIndexEndpoint(string, CallSettings)
    
    
    public virtual Operation<IndexEndpoint, UpdateIndexEndpointMetadata> PollOnceUpdateIndexEndpoint(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateIndexEndpoint` .

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)[UpdateIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexEndpointMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateIndexEndpointAsync(string, CallSettings)
    
    
    public virtual Task<Operation<IndexEndpoint, UpdateIndexEndpointMetadata>> PollOnceUpdateIndexEndpointAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateIndexEndpoint`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)[UpdateIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexEndpointMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUploadAsset(string, CallSettings)
    
    
    public virtual Operation<UploadAssetResponse, UploadAssetMetadata> PollOnceUploadAsset(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UploadAsset`.

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
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UploadAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UploadAssetResponse)[UploadAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UploadAssetMetadata)` | The result of polling the operation.  
  
### PollOnceUploadAssetAsync(string, CallSettings)
    
    
    public virtual Task<Operation<UploadAssetResponse, UploadAssetMetadata>> PollOnceUploadAssetAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UploadAsset`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UploadAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UploadAssetResponse)[UploadAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UploadAssetMetadata)` | A task representing the result of polling the operation.  
  
### RemoveCollectionItem(CollectionItem, CallSettings)
    
    
    public virtual RemoveCollectionItemResponse RemoveCollectionItem(CollectionItem item, CallSettings callSettings = null)

Removes an item from a collection.

**Parameters**  
---  
**Name** | **Description**  
`item` | `[CollectionItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionItem)`  
Required. The item to be removed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[RemoveCollectionItemResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveCollectionItemResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CollectionItem item = new gcvv::CollectionItem();
    // Make the request
    gcvv::RemoveCollectionItemResponse response = warehouseClient.RemoveCollectionItem(item);
    

### RemoveCollectionItem(RemoveCollectionItemRequest, CallSettings)
    
    
    public virtual RemoveCollectionItemResponse RemoveCollectionItem(RemoveCollectionItemRequest request, CallSettings callSettings = null)

Removes an item from a collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveCollectionItemRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveCollectionItemRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[RemoveCollectionItemResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveCollectionItemResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::RemoveCollectionItemRequest request = new gcvv::RemoveCollectionItemRequest
    {
        Item = new gcvv::CollectionItem(),
    };
    // Make the request
    gcvv::RemoveCollectionItemResponse response = warehouseClient.RemoveCollectionItem(request);
    

### RemoveCollectionItemAsync(CollectionItem, CallSettings)
    
    
    public virtual Task<RemoveCollectionItemResponse> RemoveCollectionItemAsync(CollectionItem item, CallSettings callSettings = null)

Removes an item from a collection.

**Parameters**  
---  
**Name** | **Description**  
`item` | `[CollectionItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionItem)`  
Required. The item to be removed.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RemoveCollectionItemResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveCollectionItemResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CollectionItem item = new gcvv::CollectionItem();
    // Make the request
    gcvv::RemoveCollectionItemResponse response = await warehouseClient.RemoveCollectionItemAsync(item);
    

### RemoveCollectionItemAsync(CollectionItem, CancellationToken)
    
    
    public virtual Task<RemoveCollectionItemResponse> RemoveCollectionItemAsync(CollectionItem item, CancellationToken cancellationToken)

Removes an item from a collection.

**Parameters**  
---  
**Name** | **Description**  
`item` | `[CollectionItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionItem)`  
Required. The item to be removed.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RemoveCollectionItemResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveCollectionItemResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CollectionItem item = new gcvv::CollectionItem();
    // Make the request
    gcvv::RemoveCollectionItemResponse response = await warehouseClient.RemoveCollectionItemAsync(item);
    

### RemoveCollectionItemAsync(RemoveCollectionItemRequest, CallSettings)
    
    
    public virtual Task<RemoveCollectionItemResponse> RemoveCollectionItemAsync(RemoveCollectionItemRequest request, CallSettings callSettings = null)

Removes an item from a collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveCollectionItemRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveCollectionItemRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RemoveCollectionItemResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveCollectionItemResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::RemoveCollectionItemRequest request = new gcvv::RemoveCollectionItemRequest
    {
        Item = new gcvv::CollectionItem(),
    };
    // Make the request
    gcvv::RemoveCollectionItemResponse response = await warehouseClient.RemoveCollectionItemAsync(request);
    

### RemoveCollectionItemAsync(RemoveCollectionItemRequest, CancellationToken)
    
    
    public virtual Task<RemoveCollectionItemResponse> RemoveCollectionItemAsync(RemoveCollectionItemRequest request, CancellationToken cancellationToken)

Removes an item from a collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveCollectionItemRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveCollectionItemRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RemoveCollectionItemResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveCollectionItemResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::RemoveCollectionItemRequest request = new gcvv::RemoveCollectionItemRequest
    {
        Item = new gcvv::CollectionItem(),
    };
    // Make the request
    gcvv::RemoveCollectionItemResponse response = await warehouseClient.RemoveCollectionItemAsync(request);
    

### RemoveIndexAsset(RemoveIndexAssetRequest, CallSettings)
    
    
    public virtual Operation<RemoveIndexAssetResponse, RemoveIndexAssetMetadata> RemoveIndexAsset(RemoveIndexAssetRequest request, CallSettings callSettings = null)

Remove one asset's index data for search. Supported corpus type: Corpus.Type.VIDEO_ON_DEMAND

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveIndexAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveIndexAssetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RemoveIndexAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveIndexAssetResponse)[RemoveIndexAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveIndexAssetMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::RemoveIndexAssetRequest request = new gcvv::RemoveIndexAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
        IndexAsIndexName = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]"),
    };
    // Make the request
    Operation<gcvv::RemoveIndexAssetResponse, gcvv::RemoveIndexAssetMetadata> response = warehouseClient.RemoveIndexAsset(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::RemoveIndexAssetResponse, gcvv::RemoveIndexAssetMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::RemoveIndexAssetResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::RemoveIndexAssetResponse, gcvv::RemoveIndexAssetMetadata> retrievedResponse = warehouseClient.PollOnceRemoveIndexAsset(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::RemoveIndexAssetResponse retrievedResult = retrievedResponse.Result;
    }
    

### RemoveIndexAssetAsync(RemoveIndexAssetRequest, CallSettings)
    
    
    public virtual Task<Operation<RemoveIndexAssetResponse, RemoveIndexAssetMetadata>> RemoveIndexAssetAsync(RemoveIndexAssetRequest request, CallSettings callSettings = null)

Remove one asset's index data for search. Supported corpus type: Corpus.Type.VIDEO_ON_DEMAND

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveIndexAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveIndexAssetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RemoveIndexAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveIndexAssetResponse)[RemoveIndexAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveIndexAssetMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::RemoveIndexAssetRequest request = new gcvv::RemoveIndexAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
        IndexAsIndexName = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]"),
    };
    // Make the request
    Operation<gcvv::RemoveIndexAssetResponse, gcvv::RemoveIndexAssetMetadata> response = await warehouseClient.RemoveIndexAssetAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::RemoveIndexAssetResponse, gcvv::RemoveIndexAssetMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::RemoveIndexAssetResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::RemoveIndexAssetResponse, gcvv::RemoveIndexAssetMetadata> retrievedResponse = await warehouseClient.PollOnceRemoveIndexAssetAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::RemoveIndexAssetResponse retrievedResult = retrievedResponse.Result;
    }
    

### RemoveIndexAssetAsync(RemoveIndexAssetRequest, CancellationToken)
    
    
    public virtual Task<Operation<RemoveIndexAssetResponse, RemoveIndexAssetMetadata>> RemoveIndexAssetAsync(RemoveIndexAssetRequest request, CancellationToken cancellationToken)

Remove one asset's index data for search. Supported corpus type: Corpus.Type.VIDEO_ON_DEMAND

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveIndexAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveIndexAssetRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[RemoveIndexAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveIndexAssetResponse)[RemoveIndexAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.RemoveIndexAssetMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::RemoveIndexAssetRequest request = new gcvv::RemoveIndexAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
        IndexAsIndexName = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]"),
    };
    // Make the request
    Operation<gcvv::RemoveIndexAssetResponse, gcvv::RemoveIndexAssetMetadata> response = await warehouseClient.RemoveIndexAssetAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::RemoveIndexAssetResponse, gcvv::RemoveIndexAssetMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::RemoveIndexAssetResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::RemoveIndexAssetResponse, gcvv::RemoveIndexAssetMetadata> retrievedResponse = await warehouseClient.PollOnceRemoveIndexAssetAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::RemoveIndexAssetResponse retrievedResult = retrievedResponse.Result;
    }
    

### SearchAssets(SearchAssetsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<SearchAssetsResponse, SearchResultItem> SearchAssets(SearchAssetsRequest request, CallSettings callSettings = null)

Search media asset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchAssetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchAssetsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SearchAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchAssetsResponse)[SearchResultItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchResultItem)` | A pageable sequence of [SearchResultItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchResultItem) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::SearchAssetsRequest request = new gcvv::SearchAssetsRequest
    {
        CorpusAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        Criteria =
        {
            new gcvv::Criteria(),
        },
        ContentTimeRanges = new gcvv::DateTimeRangeArray(),
        FacetSelections =
        {
            new gcvv::FacetGroup(),
        },
        ResultAnnotationKeys = { "", },
        SchemaKeySortingStrategy = new gcvv::SchemaKeySortingStrategy(),
        SearchQuery = "",
    };
    // Make the request
    PagedEnumerable<gcvv::SearchAssetsResponse, gcvv::SearchResultItem> response = warehouseClient.SearchAssets(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::SearchResultItem item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::SearchAssetsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::SearchResultItem item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::SearchResultItem> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::SearchResultItem item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchAssetsAsync(SearchAssetsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SearchAssetsResponse, SearchResultItem> SearchAssetsAsync(SearchAssetsRequest request, CallSettings callSettings = null)

Search media asset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchAssetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchAssetsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SearchAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchAssetsResponse)[SearchResultItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchResultItem)` | A pageable asynchronous sequence of [SearchResultItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchResultItem) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::SearchAssetsRequest request = new gcvv::SearchAssetsRequest
    {
        CorpusAsCorpusName = gcvv::CorpusName.FromProjectNumberLocationCorpus("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]"),
        Criteria =
        {
            new gcvv::Criteria(),
        },
        ContentTimeRanges = new gcvv::DateTimeRangeArray(),
        FacetSelections =
        {
            new gcvv::FacetGroup(),
        },
        ResultAnnotationKeys = { "", },
        SchemaKeySortingStrategy = new gcvv::SchemaKeySortingStrategy(),
        SearchQuery = "",
    };
    // Make the request
    PagedAsyncEnumerable<gcvv::SearchAssetsResponse, gcvv::SearchResultItem> response = warehouseClient.SearchAssetsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::SearchResultItem item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::SearchAssetsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::SearchResultItem item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::SearchResultItem> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::SearchResultItem item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchIndexEndpoint(SearchIndexEndpointRequest, CallSettings)
    
    
    public virtual PagedEnumerable<SearchIndexEndpointResponse, SearchResultItem> SearchIndexEndpoint(SearchIndexEndpointRequest request, CallSettings callSettings = null)

Search a deployed index endpoint (IMAGE corpus type only).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchIndexEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchIndexEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SearchIndexEndpointResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchIndexEndpointResponse)[SearchResultItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchResultItem)` | A pageable sequence of [SearchResultItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchResultItem) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::SearchIndexEndpointRequest request = new gcvv::SearchIndexEndpointRequest
    {
        IndexEndpointAsIndexEndpointName = gcvv::IndexEndpointName.FromProjectLocationIndexEndpoint("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]"),
        ImageQuery = new gcvv::ImageQuery(),
        Criteria =
        {
            new gcvv::Criteria(),
        },
        ExclusionCriteria =
        {
            new gcvv::Criteria(),
        },
    };
    // Make the request
    PagedEnumerable<gcvv::SearchIndexEndpointResponse, gcvv::SearchResultItem> response = warehouseClient.SearchIndexEndpoint(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::SearchResultItem item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::SearchIndexEndpointResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::SearchResultItem item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::SearchResultItem> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::SearchResultItem item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchIndexEndpointAsync(SearchIndexEndpointRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SearchIndexEndpointResponse, SearchResultItem> SearchIndexEndpointAsync(SearchIndexEndpointRequest request, CallSettings callSettings = null)

Search a deployed index endpoint (IMAGE corpus type only).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchIndexEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchIndexEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SearchIndexEndpointResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchIndexEndpointResponse)[SearchResultItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchResultItem)` | A pageable asynchronous sequence of [SearchResultItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchResultItem) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::SearchIndexEndpointRequest request = new gcvv::SearchIndexEndpointRequest
    {
        IndexEndpointAsIndexEndpointName = gcvv::IndexEndpointName.FromProjectLocationIndexEndpoint("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]"),
        ImageQuery = new gcvv::ImageQuery(),
        Criteria =
        {
            new gcvv::Criteria(),
        },
        ExclusionCriteria =
        {
            new gcvv::Criteria(),
        },
    };
    // Make the request
    PagedAsyncEnumerable<gcvv::SearchIndexEndpointResponse, gcvv::SearchResultItem> response = warehouseClient.SearchIndexEndpointAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::SearchResultItem item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::SearchIndexEndpointResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::SearchResultItem item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::SearchResultItem> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::SearchResultItem item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.WarehouseClient#Google_Cloud_VisionAI_V1_WarehouseClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.WarehouseClient#Google_Cloud_VisionAI_V1_WarehouseClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.WarehouseClient#Google_Cloud_VisionAI_V1_WarehouseClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.WarehouseClient#Google_Cloud_VisionAI_V1_WarehouseClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UndeployIndex(UndeployIndexRequest, CallSettings)
    
    
    public virtual Operation<UndeployIndexResponse, UndeployIndexMetadata> UndeployIndex(UndeployIndexRequest request, CallSettings callSettings = null)

Undeploys an Index from IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UndeployIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployIndexRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UndeployIndexResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployIndexResponse)[UndeployIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployIndexMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::UndeployIndexRequest request = new gcvv::UndeployIndexRequest
    {
        IndexEndpointAsIndexEndpointName = gcvv::IndexEndpointName.FromProjectLocationIndexEndpoint("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]"),
    };
    // Make the request
    Operation<gcvv::UndeployIndexResponse, gcvv::UndeployIndexMetadata> response = warehouseClient.UndeployIndex(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::UndeployIndexResponse, gcvv::UndeployIndexMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::UndeployIndexResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::UndeployIndexResponse, gcvv::UndeployIndexMetadata> retrievedResponse = warehouseClient.PollOnceUndeployIndex(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::UndeployIndexResponse retrievedResult = retrievedResponse.Result;
    }
    

### UndeployIndexAsync(UndeployIndexRequest, CallSettings)
    
    
    public virtual Task<Operation<UndeployIndexResponse, UndeployIndexMetadata>> UndeployIndexAsync(UndeployIndexRequest request, CallSettings callSettings = null)

Undeploys an Index from IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UndeployIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployIndexRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UndeployIndexResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployIndexResponse)[UndeployIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployIndexMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UndeployIndexRequest request = new gcvv::UndeployIndexRequest
    {
        IndexEndpointAsIndexEndpointName = gcvv::IndexEndpointName.FromProjectLocationIndexEndpoint("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]"),
    };
    // Make the request
    Operation<gcvv::UndeployIndexResponse, gcvv::UndeployIndexMetadata> response = await warehouseClient.UndeployIndexAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::UndeployIndexResponse, gcvv::UndeployIndexMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::UndeployIndexResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::UndeployIndexResponse, gcvv::UndeployIndexMetadata> retrievedResponse = await warehouseClient.PollOnceUndeployIndexAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::UndeployIndexResponse retrievedResult = retrievedResponse.Result;
    }
    

### UndeployIndexAsync(UndeployIndexRequest, CancellationToken)
    
    
    public virtual Task<Operation<UndeployIndexResponse, UndeployIndexMetadata>> UndeployIndexAsync(UndeployIndexRequest request, CancellationToken cancellationToken)

Undeploys an Index from IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UndeployIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployIndexRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UndeployIndexResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployIndexResponse)[UndeployIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UndeployIndexMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UndeployIndexRequest request = new gcvv::UndeployIndexRequest
    {
        IndexEndpointAsIndexEndpointName = gcvv::IndexEndpointName.FromProjectLocationIndexEndpoint("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]"),
    };
    // Make the request
    Operation<gcvv::UndeployIndexResponse, gcvv::UndeployIndexMetadata> response = await warehouseClient.UndeployIndexAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::UndeployIndexResponse, gcvv::UndeployIndexMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::UndeployIndexResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::UndeployIndexResponse, gcvv::UndeployIndexMetadata> retrievedResponse = await warehouseClient.PollOnceUndeployIndexAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::UndeployIndexResponse retrievedResult = retrievedResponse.Result;
    }
    

### UpdateAnnotation(Annotation, FieldMask, CallSettings)
    
    
    public virtual Annotation UpdateAnnotation(Annotation annotation, FieldMask updateMask, CallSettings callSettings = null)

Updates annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`annotation` | `[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)`  
Required. The annotation to update. The annotation's `name` field is used to identify the annotation to be updated. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}/annotations/{annotation}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::Annotation annotation = new gcvv::Annotation();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::Annotation response = warehouseClient.UpdateAnnotation(annotation, updateMask);
    

### UpdateAnnotation(UpdateAnnotationRequest, CallSettings)
    
    
    public virtual Annotation UpdateAnnotation(UpdateAnnotationRequest request, CallSettings callSettings = null)

Updates annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAnnotationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateAnnotationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::UpdateAnnotationRequest request = new gcvv::UpdateAnnotationRequest
    {
        Annotation = new gcvv::Annotation(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::Annotation response = warehouseClient.UpdateAnnotation(request);
    

### UpdateAnnotationAsync(Annotation, FieldMask, CallSettings)
    
    
    public virtual Task<Annotation> UpdateAnnotationAsync(Annotation annotation, FieldMask updateMask, CallSettings callSettings = null)

Updates annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`annotation` | `[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)`  
Required. The annotation to update. The annotation's `name` field is used to identify the annotation to be updated. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}/annotations/{annotation}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::Annotation annotation = new gcvv::Annotation();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::Annotation response = await warehouseClient.UpdateAnnotationAsync(annotation, updateMask);
    

### UpdateAnnotationAsync(Annotation, FieldMask, CancellationToken)
    
    
    public virtual Task<Annotation> UpdateAnnotationAsync(Annotation annotation, FieldMask updateMask, CancellationToken cancellationToken)

Updates annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`annotation` | `[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)`  
Required. The annotation to update. The annotation's `name` field is used to identify the annotation to be updated. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}/annotations/{annotation}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::Annotation annotation = new gcvv::Annotation();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::Annotation response = await warehouseClient.UpdateAnnotationAsync(annotation, updateMask);
    

### UpdateAnnotationAsync(UpdateAnnotationRequest, CallSettings)
    
    
    public virtual Task<Annotation> UpdateAnnotationAsync(UpdateAnnotationRequest request, CallSettings callSettings = null)

Updates annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAnnotationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateAnnotationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UpdateAnnotationRequest request = new gcvv::UpdateAnnotationRequest
    {
        Annotation = new gcvv::Annotation(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::Annotation response = await warehouseClient.UpdateAnnotationAsync(request);
    

### UpdateAnnotationAsync(UpdateAnnotationRequest, CancellationToken)
    
    
    public virtual Task<Annotation> UpdateAnnotationAsync(UpdateAnnotationRequest request, CancellationToken cancellationToken)

Updates annotation inside asset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAnnotationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateAnnotationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Annotation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UpdateAnnotationRequest request = new gcvv::UpdateAnnotationRequest
    {
        Annotation = new gcvv::Annotation(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::Annotation response = await warehouseClient.UpdateAnnotationAsync(request);
    

### UpdateAsset(Asset, FieldMask, CallSettings)
    
    
    public virtual Asset UpdateAsset(Asset asset, FieldMask updateMask, CallSettings callSettings = null)

Updates an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`asset` | `[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)`  
Required. The asset to update. The asset's `name` field is used to identify the asset to be updated. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::Asset asset = new gcvv::Asset();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::Asset response = warehouseClient.UpdateAsset(asset, updateMask);
    

### UpdateAsset(UpdateAssetRequest, CallSettings)
    
    
    public virtual Asset UpdateAsset(UpdateAssetRequest request, CallSettings callSettings = null)

Updates an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateAssetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::UpdateAssetRequest request = new gcvv::UpdateAssetRequest
    {
        Asset = new gcvv::Asset(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::Asset response = warehouseClient.UpdateAsset(request);
    

### UpdateAssetAsync(Asset, FieldMask, CallSettings)
    
    
    public virtual Task<Asset> UpdateAssetAsync(Asset asset, FieldMask updateMask, CallSettings callSettings = null)

Updates an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`asset` | `[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)`  
Required. The asset to update. The asset's `name` field is used to identify the asset to be updated. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::Asset asset = new gcvv::Asset();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::Asset response = await warehouseClient.UpdateAssetAsync(asset, updateMask);
    

### UpdateAssetAsync(Asset, FieldMask, CancellationToken)
    
    
    public virtual Task<Asset> UpdateAssetAsync(Asset asset, FieldMask updateMask, CancellationToken cancellationToken)

Updates an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`asset` | `[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)`  
Required. The asset to update. The asset's `name` field is used to identify the asset to be updated. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/assets/{asset}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::Asset asset = new gcvv::Asset();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::Asset response = await warehouseClient.UpdateAssetAsync(asset, updateMask);
    

### UpdateAssetAsync(UpdateAssetRequest, CallSettings)
    
    
    public virtual Task<Asset> UpdateAssetAsync(UpdateAssetRequest request, CallSettings callSettings = null)

Updates an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateAssetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UpdateAssetRequest request = new gcvv::UpdateAssetRequest
    {
        Asset = new gcvv::Asset(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::Asset response = await warehouseClient.UpdateAssetAsync(request);
    

### UpdateAssetAsync(UpdateAssetRequest, CancellationToken)
    
    
    public virtual Task<Asset> UpdateAssetAsync(UpdateAssetRequest request, CancellationToken cancellationToken)

Updates an asset inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateAssetRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Asset)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UpdateAssetRequest request = new gcvv::UpdateAssetRequest
    {
        Asset = new gcvv::Asset(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::Asset response = await warehouseClient.UpdateAssetAsync(request);
    

### UpdateCollection(Collection, FieldMask, CallSettings)
    
    
    public virtual Collection UpdateCollection(Collection collection, FieldMask updateMask, CallSettings callSettings = null)

Updates a collection.

**Parameters**  
---  
**Name** | **Description**  
`collection` | `[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)`  
Required. The collection to update. The collection's `name` field is used to identify the collection to be updated. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated.

  * Unset `update_mask` or set `update_mask` to be a single "*" only will update all updatable fields with the value provided in `collection`.
  * To update `display_name` value to empty string, set it in the `collection` to empty string, and set `update_mask` with "display_name". Same applies to other updatable string fields in the `collection`.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::Collection collection = new gcvv::Collection();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::Collection response = warehouseClient.UpdateCollection(collection, updateMask);
    

### UpdateCollection(UpdateCollectionRequest, CallSettings)
    
    
    public virtual Collection UpdateCollection(UpdateCollectionRequest request, CallSettings callSettings = null)

Updates a collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCollectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateCollectionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::UpdateCollectionRequest request = new gcvv::UpdateCollectionRequest
    {
        Collection = new gcvv::Collection(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::Collection response = warehouseClient.UpdateCollection(request);
    

### UpdateCollectionAsync(Collection, FieldMask, CallSettings)
    
    
    public virtual Task<Collection> UpdateCollectionAsync(Collection collection, FieldMask updateMask, CallSettings callSettings = null)

Updates a collection.

**Parameters**  
---  
**Name** | **Description**  
`collection` | `[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)`  
Required. The collection to update. The collection's `name` field is used to identify the collection to be updated. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated.

  * Unset `update_mask` or set `update_mask` to be a single "*" only will update all updatable fields with the value provided in `collection`.
  * To update `display_name` value to empty string, set it in the `collection` to empty string, and set `update_mask` with "display_name". Same applies to other updatable string fields in the `collection`.

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::Collection collection = new gcvv::Collection();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::Collection response = await warehouseClient.UpdateCollectionAsync(collection, updateMask);
    

### UpdateCollectionAsync(Collection, FieldMask, CancellationToken)
    
    
    public virtual Task<Collection> UpdateCollectionAsync(Collection collection, FieldMask updateMask, CancellationToken cancellationToken)

Updates a collection.

**Parameters**  
---  
**Name** | **Description**  
`collection` | `[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)`  
Required. The collection to update. The collection's `name` field is used to identify the collection to be updated. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated.

  * Unset `update_mask` or set `update_mask` to be a single "*" only will update all updatable fields with the value provided in `collection`.
  * To update `display_name` value to empty string, set it in the `collection` to empty string, and set `update_mask` with "display_name". Same applies to other updatable string fields in the `collection`.

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::Collection collection = new gcvv::Collection();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::Collection response = await warehouseClient.UpdateCollectionAsync(collection, updateMask);
    

### UpdateCollectionAsync(UpdateCollectionRequest, CallSettings)
    
    
    public virtual Task<Collection> UpdateCollectionAsync(UpdateCollectionRequest request, CallSettings callSettings = null)

Updates a collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCollectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateCollectionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UpdateCollectionRequest request = new gcvv::UpdateCollectionRequest
    {
        Collection = new gcvv::Collection(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::Collection response = await warehouseClient.UpdateCollectionAsync(request);
    

### UpdateCollectionAsync(UpdateCollectionRequest, CancellationToken)
    
    
    public virtual Task<Collection> UpdateCollectionAsync(UpdateCollectionRequest request, CancellationToken cancellationToken)

Updates a collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCollectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateCollectionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Collection)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UpdateCollectionRequest request = new gcvv::UpdateCollectionRequest
    {
        Collection = new gcvv::Collection(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::Collection response = await warehouseClient.UpdateCollectionAsync(request);
    

### UpdateCorpus(Corpus, FieldMask, CallSettings)
    
    
    public virtual Corpus UpdateCorpus(Corpus corpus, FieldMask updateMask, CallSettings callSettings = null)

Updates a corpus in a project.

**Parameters**  
---  
**Name** | **Description**  
`corpus` | `[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)`  
Required. The corpus which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::Corpus corpus = new gcvv::Corpus();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::Corpus response = warehouseClient.UpdateCorpus(corpus, updateMask);
    

### UpdateCorpus(UpdateCorpusRequest, CallSettings)
    
    
    public virtual Corpus UpdateCorpus(UpdateCorpusRequest request, CallSettings callSettings = null)

Updates a corpus in a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateCorpusRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::UpdateCorpusRequest request = new gcvv::UpdateCorpusRequest
    {
        Corpus = new gcvv::Corpus(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::Corpus response = warehouseClient.UpdateCorpus(request);
    

### UpdateCorpusAsync(Corpus, FieldMask, CallSettings)
    
    
    public virtual Task<Corpus> UpdateCorpusAsync(Corpus corpus, FieldMask updateMask, CallSettings callSettings = null)

Updates a corpus in a project.

**Parameters**  
---  
**Name** | **Description**  
`corpus` | `[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)`  
Required. The corpus which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::Corpus corpus = new gcvv::Corpus();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::Corpus response = await warehouseClient.UpdateCorpusAsync(corpus, updateMask);
    

### UpdateCorpusAsync(Corpus, FieldMask, CancellationToken)
    
    
    public virtual Task<Corpus> UpdateCorpusAsync(Corpus corpus, FieldMask updateMask, CancellationToken cancellationToken)

Updates a corpus in a project.

**Parameters**  
---  
**Name** | **Description**  
`corpus` | `[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)`  
Required. The corpus which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::Corpus corpus = new gcvv::Corpus();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::Corpus response = await warehouseClient.UpdateCorpusAsync(corpus, updateMask);
    

### UpdateCorpusAsync(UpdateCorpusRequest, CallSettings)
    
    
    public virtual Task<Corpus> UpdateCorpusAsync(UpdateCorpusRequest request, CallSettings callSettings = null)

Updates a corpus in a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateCorpusRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UpdateCorpusRequest request = new gcvv::UpdateCorpusRequest
    {
        Corpus = new gcvv::Corpus(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::Corpus response = await warehouseClient.UpdateCorpusAsync(request);
    

### UpdateCorpusAsync(UpdateCorpusRequest, CancellationToken)
    
    
    public virtual Task<Corpus> UpdateCorpusAsync(UpdateCorpusRequest request, CancellationToken cancellationToken)

Updates a corpus in a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCorpusRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateCorpusRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Corpus)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UpdateCorpusRequest request = new gcvv::UpdateCorpusRequest
    {
        Corpus = new gcvv::Corpus(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::Corpus response = await warehouseClient.UpdateCorpusAsync(request);
    

### UpdateDataSchema(DataSchema, FieldMask, CallSettings)
    
    
    public virtual DataSchema UpdateDataSchema(DataSchema dataSchema, FieldMask updateMask, CallSettings callSettings = null)

Updates data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`dataSchema` | `[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)`  
Required. The data schema's `name` field is used to identify the data schema to be updated. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/dataSchemas/{data_schema}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::DataSchema dataSchema = new gcvv::DataSchema();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::DataSchema response = warehouseClient.UpdateDataSchema(dataSchema, updateMask);
    

### UpdateDataSchema(UpdateDataSchemaRequest, CallSettings)
    
    
    public virtual DataSchema UpdateDataSchema(UpdateDataSchemaRequest request, CallSettings callSettings = null)

Updates data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateDataSchemaRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::UpdateDataSchemaRequest request = new gcvv::UpdateDataSchemaRequest
    {
        DataSchema = new gcvv::DataSchema(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::DataSchema response = warehouseClient.UpdateDataSchema(request);
    

### UpdateDataSchemaAsync(DataSchema, FieldMask, CallSettings)
    
    
    public virtual Task<DataSchema> UpdateDataSchemaAsync(DataSchema dataSchema, FieldMask updateMask, CallSettings callSettings = null)

Updates data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`dataSchema` | `[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)`  
Required. The data schema's `name` field is used to identify the data schema to be updated. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/dataSchemas/{data_schema}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DataSchema dataSchema = new gcvv::DataSchema();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::DataSchema response = await warehouseClient.UpdateDataSchemaAsync(dataSchema, updateMask);
    

### UpdateDataSchemaAsync(DataSchema, FieldMask, CancellationToken)
    
    
    public virtual Task<DataSchema> UpdateDataSchemaAsync(DataSchema dataSchema, FieldMask updateMask, CancellationToken cancellationToken)

Updates data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`dataSchema` | `[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)`  
Required. The data schema's `name` field is used to identify the data schema to be updated. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/dataSchemas/{data_schema}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::DataSchema dataSchema = new gcvv::DataSchema();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::DataSchema response = await warehouseClient.UpdateDataSchemaAsync(dataSchema, updateMask);
    

### UpdateDataSchemaAsync(UpdateDataSchemaRequest, CallSettings)
    
    
    public virtual Task<DataSchema> UpdateDataSchemaAsync(UpdateDataSchemaRequest request, CallSettings callSettings = null)

Updates data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateDataSchemaRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UpdateDataSchemaRequest request = new gcvv::UpdateDataSchemaRequest
    {
        DataSchema = new gcvv::DataSchema(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::DataSchema response = await warehouseClient.UpdateDataSchemaAsync(request);
    

### UpdateDataSchemaAsync(UpdateDataSchemaRequest, CancellationToken)
    
    
    public virtual Task<DataSchema> UpdateDataSchemaAsync(UpdateDataSchemaRequest request, CancellationToken cancellationToken)

Updates data schema inside corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateDataSchemaRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DataSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DataSchema)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UpdateDataSchemaRequest request = new gcvv::UpdateDataSchemaRequest
    {
        DataSchema = new gcvv::DataSchema(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::DataSchema response = await warehouseClient.UpdateDataSchemaAsync(request);
    

### UpdateIndex(Index, FieldMask, CallSettings)
    
    
    public virtual Operation<Index, UpdateIndexMetadata> UpdateIndex(Index index, FieldMask updateMask, CallSettings callSettings = null)

Updates an Index under the corpus. Users can perform a metadata-only update or trigger a full index rebuild with different update_mask values.

**Parameters**  
---  
**Name** | **Description**  
`index` | `[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Index resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field of the resource will be overwritten if it is in the mask. Empty field mask is not allowed. If the mask is "*", it triggers a full update of the index, and also a whole rebuild of index data.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)[UpdateIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::Index index = new gcvv::Index();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcvv::Index, gcvv::UpdateIndexMetadata> response = warehouseClient.UpdateIndex(index, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Index, gcvv::UpdateIndexMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::Index result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Index, gcvv::UpdateIndexMetadata> retrievedResponse = warehouseClient.PollOnceUpdateIndex(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Index retrievedResult = retrievedResponse.Result;
    }
    

### UpdateIndex(UpdateIndexRequest, CallSettings)
    
    
    public virtual Operation<Index, UpdateIndexMetadata> UpdateIndex(UpdateIndexRequest request, CallSettings callSettings = null)

Updates an Index under the corpus. Users can perform a metadata-only update or trigger a full index rebuild with different update_mask values.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)[UpdateIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::UpdateIndexRequest request = new gcvv::UpdateIndexRequest
    {
        Index = new gcvv::Index(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<gcvv::Index, gcvv::UpdateIndexMetadata> response = warehouseClient.UpdateIndex(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Index, gcvv::UpdateIndexMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::Index result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Index, gcvv::UpdateIndexMetadata> retrievedResponse = warehouseClient.PollOnceUpdateIndex(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Index retrievedResult = retrievedResponse.Result;
    }
    

### UpdateIndexAsync(Index, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Index, UpdateIndexMetadata>> UpdateIndexAsync(Index index, FieldMask updateMask, CallSettings callSettings = null)

Updates an Index under the corpus. Users can perform a metadata-only update or trigger a full index rebuild with different update_mask values.

**Parameters**  
---  
**Name** | **Description**  
`index` | `[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Index resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field of the resource will be overwritten if it is in the mask. Empty field mask is not allowed. If the mask is "*", it triggers a full update of the index, and also a whole rebuild of index data.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)[UpdateIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::Index index = new gcvv::Index();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcvv::Index, gcvv::UpdateIndexMetadata> response = await warehouseClient.UpdateIndexAsync(index, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Index, gcvv::UpdateIndexMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::Index result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Index, gcvv::UpdateIndexMetadata> retrievedResponse = await warehouseClient.PollOnceUpdateIndexAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Index retrievedResult = retrievedResponse.Result;
    }
    

### UpdateIndexAsync(Index, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Index, UpdateIndexMetadata>> UpdateIndexAsync(Index index, FieldMask updateMask, CancellationToken cancellationToken)

Updates an Index under the corpus. Users can perform a metadata-only update or trigger a full index rebuild with different update_mask values.

**Parameters**  
---  
**Name** | **Description**  
`index` | `[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Index resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field of the resource will be overwritten if it is in the mask. Empty field mask is not allowed. If the mask is "*", it triggers a full update of the index, and also a whole rebuild of index data.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)[UpdateIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::Index index = new gcvv::Index();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcvv::Index, gcvv::UpdateIndexMetadata> response = await warehouseClient.UpdateIndexAsync(index, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Index, gcvv::UpdateIndexMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::Index result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Index, gcvv::UpdateIndexMetadata> retrievedResponse = await warehouseClient.PollOnceUpdateIndexAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Index retrievedResult = retrievedResponse.Result;
    }
    

### UpdateIndexAsync(UpdateIndexRequest, CallSettings)
    
    
    public virtual Task<Operation<Index, UpdateIndexMetadata>> UpdateIndexAsync(UpdateIndexRequest request, CallSettings callSettings = null)

Updates an Index under the corpus. Users can perform a metadata-only update or trigger a full index rebuild with different update_mask values.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)[UpdateIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UpdateIndexRequest request = new gcvv::UpdateIndexRequest
    {
        Index = new gcvv::Index(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<gcvv::Index, gcvv::UpdateIndexMetadata> response = await warehouseClient.UpdateIndexAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Index, gcvv::UpdateIndexMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::Index result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Index, gcvv::UpdateIndexMetadata> retrievedResponse = await warehouseClient.PollOnceUpdateIndexAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Index retrievedResult = retrievedResponse.Result;
    }
    

### UpdateIndexAsync(UpdateIndexRequest, CancellationToken)
    
    
    public virtual Task<Operation<Index, UpdateIndexMetadata>> UpdateIndexAsync(UpdateIndexRequest request, CancellationToken cancellationToken)

Updates an Index under the corpus. Users can perform a metadata-only update or trigger a full index rebuild with different update_mask values.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Index](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Index)[UpdateIndexMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UpdateIndexRequest request = new gcvv::UpdateIndexRequest
    {
        Index = new gcvv::Index(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<gcvv::Index, gcvv::UpdateIndexMetadata> response = await warehouseClient.UpdateIndexAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::Index, gcvv::UpdateIndexMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::Index result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::Index, gcvv::UpdateIndexMetadata> retrievedResponse = await warehouseClient.PollOnceUpdateIndexAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::Index retrievedResult = retrievedResponse.Result;
    }
    

### UpdateIndexEndpoint(IndexEndpoint, FieldMask, CallSettings)
    
    
    public virtual Operation<IndexEndpoint, UpdateIndexEndpointMetadata> UpdateIndexEndpoint(IndexEndpoint indexEndpoint, FieldMask updateMask, CallSettings callSettings = null)

Updates an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`indexEndpoint` | `[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the IndexEndpoint resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field of the resource will be overwritten if it is in the mask. Empty field mask is not allowed. If the mask is "*", then this is a full replacement of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)[UpdateIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexEndpointMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::IndexEndpoint indexEndpoint = new gcvv::IndexEndpoint();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcvv::IndexEndpoint, gcvv::UpdateIndexEndpointMetadata> response = warehouseClient.UpdateIndexEndpoint(indexEndpoint, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::IndexEndpoint, gcvv::UpdateIndexEndpointMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::IndexEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::IndexEndpoint, gcvv::UpdateIndexEndpointMetadata> retrievedResponse = warehouseClient.PollOnceUpdateIndexEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::IndexEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### UpdateIndexEndpoint(UpdateIndexEndpointRequest, CallSettings)
    
    
    public virtual Operation<IndexEndpoint, UpdateIndexEndpointMetadata> UpdateIndexEndpoint(UpdateIndexEndpointRequest request, CallSettings callSettings = null)

Updates an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateIndexEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)[UpdateIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexEndpointMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::UpdateIndexEndpointRequest request = new gcvv::UpdateIndexEndpointRequest
    {
        IndexEndpoint = new gcvv::IndexEndpoint(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<gcvv::IndexEndpoint, gcvv::UpdateIndexEndpointMetadata> response = warehouseClient.UpdateIndexEndpoint(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::IndexEndpoint, gcvv::UpdateIndexEndpointMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::IndexEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::IndexEndpoint, gcvv::UpdateIndexEndpointMetadata> retrievedResponse = warehouseClient.PollOnceUpdateIndexEndpoint(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::IndexEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### UpdateIndexEndpointAsync(IndexEndpoint, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<IndexEndpoint, UpdateIndexEndpointMetadata>> UpdateIndexEndpointAsync(IndexEndpoint indexEndpoint, FieldMask updateMask, CallSettings callSettings = null)

Updates an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`indexEndpoint` | `[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the IndexEndpoint resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field of the resource will be overwritten if it is in the mask. Empty field mask is not allowed. If the mask is "*", then this is a full replacement of the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)[UpdateIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexEndpointMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::IndexEndpoint indexEndpoint = new gcvv::IndexEndpoint();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcvv::IndexEndpoint, gcvv::UpdateIndexEndpointMetadata> response = await warehouseClient.UpdateIndexEndpointAsync(indexEndpoint, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::IndexEndpoint, gcvv::UpdateIndexEndpointMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::IndexEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::IndexEndpoint, gcvv::UpdateIndexEndpointMetadata> retrievedResponse = await warehouseClient.PollOnceUpdateIndexEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::IndexEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### UpdateIndexEndpointAsync(IndexEndpoint, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<IndexEndpoint, UpdateIndexEndpointMetadata>> UpdateIndexEndpointAsync(IndexEndpoint indexEndpoint, FieldMask updateMask, CancellationToken cancellationToken)

Updates an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`indexEndpoint` | `[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the IndexEndpoint resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field of the resource will be overwritten if it is in the mask. Empty field mask is not allowed. If the mask is "*", then this is a full replacement of the resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)[UpdateIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexEndpointMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::IndexEndpoint indexEndpoint = new gcvv::IndexEndpoint();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<gcvv::IndexEndpoint, gcvv::UpdateIndexEndpointMetadata> response = await warehouseClient.UpdateIndexEndpointAsync(indexEndpoint, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::IndexEndpoint, gcvv::UpdateIndexEndpointMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::IndexEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::IndexEndpoint, gcvv::UpdateIndexEndpointMetadata> retrievedResponse = await warehouseClient.PollOnceUpdateIndexEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::IndexEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### UpdateIndexEndpointAsync(UpdateIndexEndpointRequest, CallSettings)
    
    
    public virtual Task<Operation<IndexEndpoint, UpdateIndexEndpointMetadata>> UpdateIndexEndpointAsync(UpdateIndexEndpointRequest request, CallSettings callSettings = null)

Updates an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateIndexEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)[UpdateIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexEndpointMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UpdateIndexEndpointRequest request = new gcvv::UpdateIndexEndpointRequest
    {
        IndexEndpoint = new gcvv::IndexEndpoint(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<gcvv::IndexEndpoint, gcvv::UpdateIndexEndpointMetadata> response = await warehouseClient.UpdateIndexEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::IndexEndpoint, gcvv::UpdateIndexEndpointMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::IndexEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::IndexEndpoint, gcvv::UpdateIndexEndpointMetadata> retrievedResponse = await warehouseClient.PollOnceUpdateIndexEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::IndexEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### UpdateIndexEndpointAsync(UpdateIndexEndpointRequest, CancellationToken)
    
    
    public virtual Task<Operation<IndexEndpoint, UpdateIndexEndpointMetadata>> UpdateIndexEndpointAsync(UpdateIndexEndpointRequest request, CancellationToken cancellationToken)

Updates an IndexEndpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateIndexEndpointRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexEndpointRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[IndexEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexEndpoint)[UpdateIndexEndpointMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateIndexEndpointMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UpdateIndexEndpointRequest request = new gcvv::UpdateIndexEndpointRequest
    {
        IndexEndpoint = new gcvv::IndexEndpoint(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<gcvv::IndexEndpoint, gcvv::UpdateIndexEndpointMetadata> response = await warehouseClient.UpdateIndexEndpointAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::IndexEndpoint, gcvv::UpdateIndexEndpointMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::IndexEndpoint result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::IndexEndpoint, gcvv::UpdateIndexEndpointMetadata> retrievedResponse = await warehouseClient.PollOnceUpdateIndexEndpointAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::IndexEndpoint retrievedResult = retrievedResponse.Result;
    }
    

### UpdateSearchConfig(SearchConfig, FieldMask, CallSettings)
    
    
    public virtual SearchConfig UpdateSearchConfig(SearchConfig searchConfig, FieldMask updateMask, CallSettings callSettings = null)

Updates a search configuration inside a corpus.

Please follow the rules below to create a valid UpdateSearchConfigRequest. \--- General Rules ---

  1. Request.search_configuration.name must already exist.
  2. Request must contain at least one non-empty search_criteria_property or facet_property.
  3. mapped_fields must not be empty, and must map to existing UGA keys.
  4. All mapped_fields must be of the same type.
  5. All mapped_fields must share the same granularity.
  6. All mapped_fields must share the same semantic SearchConfig match options. For property-specific rules, please reference the comments for FacetProperty and SearchCriteriaProperty.



**Parameters**  
---  
**Name** | **Description**  
`searchConfig` | `[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)`  
Required. The search configuration to update. The search configuration's `name` field is used to identify the resource to be updated. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchConfigs/{search_config}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated. If left unset, all field paths will be updated/overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::SearchConfig searchConfig = new gcvv::SearchConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::SearchConfig response = warehouseClient.UpdateSearchConfig(searchConfig, updateMask);
    

### UpdateSearchConfig(UpdateSearchConfigRequest, CallSettings)
    
    
    public virtual SearchConfig UpdateSearchConfig(UpdateSearchConfigRequest request, CallSettings callSettings = null)

Updates a search configuration inside a corpus.

Please follow the rules below to create a valid UpdateSearchConfigRequest. \--- General Rules ---

  1. Request.search_configuration.name must already exist.
  2. Request must contain at least one non-empty search_criteria_property or facet_property.
  3. mapped_fields must not be empty, and must map to existing UGA keys.
  4. All mapped_fields must be of the same type.
  5. All mapped_fields must share the same granularity.
  6. All mapped_fields must share the same semantic SearchConfig match options. For property-specific rules, please reference the comments for FacetProperty and SearchCriteriaProperty.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSearchConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateSearchConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::UpdateSearchConfigRequest request = new gcvv::UpdateSearchConfigRequest
    {
        SearchConfig = new gcvv::SearchConfig(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::SearchConfig response = warehouseClient.UpdateSearchConfig(request);
    

### UpdateSearchConfigAsync(SearchConfig, FieldMask, CallSettings)
    
    
    public virtual Task<SearchConfig> UpdateSearchConfigAsync(SearchConfig searchConfig, FieldMask updateMask, CallSettings callSettings = null)

Updates a search configuration inside a corpus.

Please follow the rules below to create a valid UpdateSearchConfigRequest. \--- General Rules ---

  1. Request.search_configuration.name must already exist.
  2. Request must contain at least one non-empty search_criteria_property or facet_property.
  3. mapped_fields must not be empty, and must map to existing UGA keys.
  4. All mapped_fields must be of the same type.
  5. All mapped_fields must share the same granularity.
  6. All mapped_fields must share the same semantic SearchConfig match options. For property-specific rules, please reference the comments for FacetProperty and SearchCriteriaProperty.



**Parameters**  
---  
**Name** | **Description**  
`searchConfig` | `[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)`  
Required. The search configuration to update. The search configuration's `name` field is used to identify the resource to be updated. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchConfigs/{search_config}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated. If left unset, all field paths will be updated/overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::SearchConfig searchConfig = new gcvv::SearchConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::SearchConfig response = await warehouseClient.UpdateSearchConfigAsync(searchConfig, updateMask);
    

### UpdateSearchConfigAsync(SearchConfig, FieldMask, CancellationToken)
    
    
    public virtual Task<SearchConfig> UpdateSearchConfigAsync(SearchConfig searchConfig, FieldMask updateMask, CancellationToken cancellationToken)

Updates a search configuration inside a corpus.

Please follow the rules below to create a valid UpdateSearchConfigRequest. \--- General Rules ---

  1. Request.search_configuration.name must already exist.
  2. Request must contain at least one non-empty search_criteria_property or facet_property.
  3. mapped_fields must not be empty, and must map to existing UGA keys.
  4. All mapped_fields must be of the same type.
  5. All mapped_fields must share the same granularity.
  6. All mapped_fields must share the same semantic SearchConfig match options. For property-specific rules, please reference the comments for FacetProperty and SearchCriteriaProperty.



**Parameters**  
---  
**Name** | **Description**  
`searchConfig` | `[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)`  
Required. The search configuration to update. The search configuration's `name` field is used to identify the resource to be updated. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchConfigs/{search_config}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated. If left unset, all field paths will be updated/overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::SearchConfig searchConfig = new gcvv::SearchConfig();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::SearchConfig response = await warehouseClient.UpdateSearchConfigAsync(searchConfig, updateMask);
    

### UpdateSearchConfigAsync(UpdateSearchConfigRequest, CallSettings)
    
    
    public virtual Task<SearchConfig> UpdateSearchConfigAsync(UpdateSearchConfigRequest request, CallSettings callSettings = null)

Updates a search configuration inside a corpus.

Please follow the rules below to create a valid UpdateSearchConfigRequest. \--- General Rules ---

  1. Request.search_configuration.name must already exist.
  2. Request must contain at least one non-empty search_criteria_property or facet_property.
  3. mapped_fields must not be empty, and must map to existing UGA keys.
  4. All mapped_fields must be of the same type.
  5. All mapped_fields must share the same granularity.
  6. All mapped_fields must share the same semantic SearchConfig match options. For property-specific rules, please reference the comments for FacetProperty and SearchCriteriaProperty.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSearchConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateSearchConfigRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UpdateSearchConfigRequest request = new gcvv::UpdateSearchConfigRequest
    {
        SearchConfig = new gcvv::SearchConfig(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::SearchConfig response = await warehouseClient.UpdateSearchConfigAsync(request);
    

### UpdateSearchConfigAsync(UpdateSearchConfigRequest, CancellationToken)
    
    
    public virtual Task<SearchConfig> UpdateSearchConfigAsync(UpdateSearchConfigRequest request, CancellationToken cancellationToken)

Updates a search configuration inside a corpus.

Please follow the rules below to create a valid UpdateSearchConfigRequest. \--- General Rules ---

  1. Request.search_configuration.name must already exist.
  2. Request must contain at least one non-empty search_criteria_property or facet_property.
  3. mapped_fields must not be empty, and must map to existing UGA keys.
  4. All mapped_fields must be of the same type.
  5. All mapped_fields must share the same granularity.
  6. All mapped_fields must share the same semantic SearchConfig match options. For property-specific rules, please reference the comments for FacetProperty and SearchCriteriaProperty.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSearchConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateSearchConfigRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchConfig)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UpdateSearchConfigRequest request = new gcvv::UpdateSearchConfigRequest
    {
        SearchConfig = new gcvv::SearchConfig(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::SearchConfig response = await warehouseClient.UpdateSearchConfigAsync(request);
    

### UpdateSearchHypernym(SearchHypernym, FieldMask, CallSettings)
    
    
    public virtual SearchHypernym UpdateSearchHypernym(SearchHypernym searchHypernym, FieldMask updateMask, CallSettings callSettings = null)

Updates a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`searchHypernym` | `[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)`  
Required. The SearchHypernym to update. The search hypernym's `name` field is used to identify the search hypernym to be updated. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchHypernyms/{search_hypernym}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated. If left unset, all field paths will be updated/overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::SearchHypernym searchHypernym = new gcvv::SearchHypernym();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::SearchHypernym response = warehouseClient.UpdateSearchHypernym(searchHypernym, updateMask);
    

### UpdateSearchHypernym(UpdateSearchHypernymRequest, CallSettings)
    
    
    public virtual SearchHypernym UpdateSearchHypernym(UpdateSearchHypernymRequest request, CallSettings callSettings = null)

Updates a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSearchHypernymRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateSearchHypernymRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::UpdateSearchHypernymRequest request = new gcvv::UpdateSearchHypernymRequest
    {
        SearchHypernym = new gcvv::SearchHypernym(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::SearchHypernym response = warehouseClient.UpdateSearchHypernym(request);
    

### UpdateSearchHypernymAsync(SearchHypernym, FieldMask, CallSettings)
    
    
    public virtual Task<SearchHypernym> UpdateSearchHypernymAsync(SearchHypernym searchHypernym, FieldMask updateMask, CallSettings callSettings = null)

Updates a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`searchHypernym` | `[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)`  
Required. The SearchHypernym to update. The search hypernym's `name` field is used to identify the search hypernym to be updated. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchHypernyms/{search_hypernym}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated. If left unset, all field paths will be updated/overwritten.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::SearchHypernym searchHypernym = new gcvv::SearchHypernym();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::SearchHypernym response = await warehouseClient.UpdateSearchHypernymAsync(searchHypernym, updateMask);
    

### UpdateSearchHypernymAsync(SearchHypernym, FieldMask, CancellationToken)
    
    
    public virtual Task<SearchHypernym> UpdateSearchHypernymAsync(SearchHypernym searchHypernym, FieldMask updateMask, CancellationToken cancellationToken)

Updates a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`searchHypernym` | `[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)`  
Required. The SearchHypernym to update. The search hypernym's `name` field is used to identify the search hypernym to be updated. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchHypernyms/{search_hypernym}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The list of fields to be updated. If left unset, all field paths will be updated/overwritten.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::SearchHypernym searchHypernym = new gcvv::SearchHypernym();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcvv::SearchHypernym response = await warehouseClient.UpdateSearchHypernymAsync(searchHypernym, updateMask);
    

### UpdateSearchHypernymAsync(UpdateSearchHypernymRequest, CallSettings)
    
    
    public virtual Task<SearchHypernym> UpdateSearchHypernymAsync(UpdateSearchHypernymRequest request, CallSettings callSettings = null)

Updates a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSearchHypernymRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateSearchHypernymRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UpdateSearchHypernymRequest request = new gcvv::UpdateSearchHypernymRequest
    {
        SearchHypernym = new gcvv::SearchHypernym(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::SearchHypernym response = await warehouseClient.UpdateSearchHypernymAsync(request);
    

### UpdateSearchHypernymAsync(UpdateSearchHypernymRequest, CancellationToken)
    
    
    public virtual Task<SearchHypernym> UpdateSearchHypernymAsync(UpdateSearchHypernymRequest request, CancellationToken cancellationToken)

Updates a SearchHypernym inside a corpus.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSearchHypernymRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UpdateSearchHypernymRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchHypernym](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchHypernym)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UpdateSearchHypernymRequest request = new gcvv::UpdateSearchHypernymRequest
    {
        SearchHypernym = new gcvv::SearchHypernym(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcvv::SearchHypernym response = await warehouseClient.UpdateSearchHypernymAsync(request);
    

### UploadAsset(UploadAssetRequest, CallSettings)
    
    
    public virtual Operation<UploadAssetResponse, UploadAssetMetadata> UploadAsset(UploadAssetRequest request, CallSettings callSettings = null)

Upload asset by specifing the asset Cloud Storage uri. For video warehouse, it requires users who call this API have read access to the cloud storage file. Once it is uploaded, it can be retrieved by GenerateRetrievalUrl API which by default, only can retrieve cloud storage files from the same project of the warehouse. To allow retrieval cloud storage files that are in a separate project, it requires to find the vision ai service account (Go to IAM, check checkbox to show "Include Google-provided role grants", search for "Cloud Vision AI Service Agent") and grant the read access of the cloud storage files to that service account.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UploadAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UploadAssetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UploadAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UploadAssetResponse)[UploadAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UploadAssetMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::UploadAssetRequest request = new gcvv::UploadAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
        AssetSource = new gcvv::AssetSource(),
    };
    // Make the request
    Operation<gcvv::UploadAssetResponse, gcvv::UploadAssetMetadata> response = warehouseClient.UploadAsset(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::UploadAssetResponse, gcvv::UploadAssetMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcvv::UploadAssetResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::UploadAssetResponse, gcvv::UploadAssetMetadata> retrievedResponse = warehouseClient.PollOnceUploadAsset(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::UploadAssetResponse retrievedResult = retrievedResponse.Result;
    }
    

### UploadAssetAsync(UploadAssetRequest, CallSettings)
    
    
    public virtual Task<Operation<UploadAssetResponse, UploadAssetMetadata>> UploadAssetAsync(UploadAssetRequest request, CallSettings callSettings = null)

Upload asset by specifing the asset Cloud Storage uri. For video warehouse, it requires users who call this API have read access to the cloud storage file. Once it is uploaded, it can be retrieved by GenerateRetrievalUrl API which by default, only can retrieve cloud storage files from the same project of the warehouse. To allow retrieval cloud storage files that are in a separate project, it requires to find the vision ai service account (Go to IAM, check checkbox to show "Include Google-provided role grants", search for "Cloud Vision AI Service Agent") and grant the read access of the cloud storage files to that service account.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UploadAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UploadAssetRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UploadAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UploadAssetResponse)[UploadAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UploadAssetMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UploadAssetRequest request = new gcvv::UploadAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
        AssetSource = new gcvv::AssetSource(),
    };
    // Make the request
    Operation<gcvv::UploadAssetResponse, gcvv::UploadAssetMetadata> response = await warehouseClient.UploadAssetAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::UploadAssetResponse, gcvv::UploadAssetMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::UploadAssetResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::UploadAssetResponse, gcvv::UploadAssetMetadata> retrievedResponse = await warehouseClient.PollOnceUploadAssetAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::UploadAssetResponse retrievedResult = retrievedResponse.Result;
    }
    

### UploadAssetAsync(UploadAssetRequest, CancellationToken)
    
    
    public virtual Task<Operation<UploadAssetResponse, UploadAssetMetadata>> UploadAssetAsync(UploadAssetRequest request, CancellationToken cancellationToken)

Upload asset by specifing the asset Cloud Storage uri. For video warehouse, it requires users who call this API have read access to the cloud storage file. Once it is uploaded, it can be retrieved by GenerateRetrievalUrl API which by default, only can retrieve cloud storage files from the same project of the warehouse. To allow retrieval cloud storage files that are in a separate project, it requires to find the vision ai service account (Go to IAM, check checkbox to show "Include Google-provided role grants", search for "Cloud Vision AI Service Agent") and grant the read access of the cloud storage files to that service account.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UploadAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UploadAssetRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[UploadAssetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UploadAssetResponse)[UploadAssetMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.UploadAssetMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::UploadAssetRequest request = new gcvv::UploadAssetRequest
    {
        AssetName = gcvv::AssetName.FromProjectNumberLocationCorpusAsset("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[ASSET]"),
        AssetSource = new gcvv::AssetSource(),
    };
    // Make the request
    Operation<gcvv::UploadAssetResponse, gcvv::UploadAssetMetadata> response = await warehouseClient.UploadAssetAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcvv::UploadAssetResponse, gcvv::UploadAssetMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcvv::UploadAssetResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcvv::UploadAssetResponse, gcvv::UploadAssetMetadata> retrievedResponse = await warehouseClient.PollOnceUploadAssetAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcvv::UploadAssetResponse retrievedResult = retrievedResponse.Result;
    }
    

### ViewCollectionItems(CollectionName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ViewCollectionItemsResponse, CollectionItem> ViewCollectionItems(CollectionName collection, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

View items inside a collection.

**Parameters**  
---  
**Name** | **Description**  
`collection` | `[CollectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionName)`  
Required. The collection to view. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ViewCollectionItemsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ViewCollectionItemsResponse)[CollectionItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionItem)` | A pageable sequence of [CollectionItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionItem) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::CollectionName collection = gcvv::CollectionName.FromProjectNumberLocationCorpusCollection("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[COLLECTION]");
    // Make the request
    PagedEnumerable<gcvv::ViewCollectionItemsResponse, gcvv::CollectionItem> response = warehouseClient.ViewCollectionItems(collection);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::CollectionItem item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ViewCollectionItemsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::CollectionItem item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::CollectionItem> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::CollectionItem item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ViewCollectionItems(ViewCollectionItemsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ViewCollectionItemsResponse, CollectionItem> ViewCollectionItems(ViewCollectionItemsRequest request, CallSettings callSettings = null)

View items inside a collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ViewCollectionItemsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ViewCollectionItemsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ViewCollectionItemsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ViewCollectionItemsResponse)[CollectionItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionItem)` | A pageable sequence of [CollectionItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionItem) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::ViewCollectionItemsRequest request = new gcvv::ViewCollectionItemsRequest
    {
        CollectionAsCollectionName = gcvv::CollectionName.FromProjectNumberLocationCorpusCollection("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[COLLECTION]"),
    };
    // Make the request
    PagedEnumerable<gcvv::ViewCollectionItemsResponse, gcvv::CollectionItem> response = warehouseClient.ViewCollectionItems(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::CollectionItem item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ViewCollectionItemsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::CollectionItem item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::CollectionItem> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::CollectionItem item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ViewCollectionItems(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ViewCollectionItemsResponse, CollectionItem> ViewCollectionItems(string collection, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

View items inside a collection.

**Parameters**  
---  
**Name** | **Description**  
`collection` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The collection to view. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ViewCollectionItemsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ViewCollectionItemsResponse)[CollectionItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionItem)` | A pageable sequence of [CollectionItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionItem) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string collection = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/collections/[COLLECTION]";
    // Make the request
    PagedEnumerable<gcvv::ViewCollectionItemsResponse, gcvv::CollectionItem> response = warehouseClient.ViewCollectionItems(collection);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::CollectionItem item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ViewCollectionItemsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::CollectionItem item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::CollectionItem> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::CollectionItem item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ViewCollectionItemsAsync(CollectionName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ViewCollectionItemsResponse, CollectionItem> ViewCollectionItemsAsync(CollectionName collection, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

View items inside a collection.

**Parameters**  
---  
**Name** | **Description**  
`collection` | `[CollectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionName)`  
Required. The collection to view. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ViewCollectionItemsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ViewCollectionItemsResponse)[CollectionItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionItem)` | A pageable asynchronous sequence of [CollectionItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionItem) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::CollectionName collection = gcvv::CollectionName.FromProjectNumberLocationCorpusCollection("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[COLLECTION]");
    // Make the request
    PagedAsyncEnumerable<gcvv::ViewCollectionItemsResponse, gcvv::CollectionItem> response = warehouseClient.ViewCollectionItemsAsync(collection);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::CollectionItem item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ViewCollectionItemsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::CollectionItem item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::CollectionItem> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::CollectionItem item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ViewCollectionItemsAsync(ViewCollectionItemsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ViewCollectionItemsResponse, CollectionItem> ViewCollectionItemsAsync(ViewCollectionItemsRequest request, CallSettings callSettings = null)

View items inside a collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ViewCollectionItemsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ViewCollectionItemsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ViewCollectionItemsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ViewCollectionItemsResponse)[CollectionItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionItem)` | A pageable asynchronous sequence of [CollectionItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionItem) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::ViewCollectionItemsRequest request = new gcvv::ViewCollectionItemsRequest
    {
        CollectionAsCollectionName = gcvv::CollectionName.FromProjectNumberLocationCorpusCollection("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[COLLECTION]"),
    };
    // Make the request
    PagedAsyncEnumerable<gcvv::ViewCollectionItemsResponse, gcvv::CollectionItem> response = warehouseClient.ViewCollectionItemsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::CollectionItem item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ViewCollectionItemsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::CollectionItem item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::CollectionItem> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::CollectionItem item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ViewCollectionItemsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ViewCollectionItemsResponse, CollectionItem> ViewCollectionItemsAsync(string collection, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

View items inside a collection.

**Parameters**  
---  
**Name** | **Description**  
`collection` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The collection to view. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/collections/{collection}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ViewCollectionItemsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ViewCollectionItemsResponse)[CollectionItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionItem)` | A pageable asynchronous sequence of [CollectionItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CollectionItem) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string collection = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/collections/[COLLECTION]";
    // Make the request
    PagedAsyncEnumerable<gcvv::ViewCollectionItemsResponse, gcvv::CollectionItem> response = warehouseClient.ViewCollectionItemsAsync(collection);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::CollectionItem item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ViewCollectionItemsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::CollectionItem item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::CollectionItem> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::CollectionItem item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ViewIndexedAssets(IndexName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ViewIndexedAssetsResponse, IndexedAsset> ViewIndexedAssets(IndexName index, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists assets inside an index.

**Parameters**  
---  
**Name** | **Description**  
`index` | `[IndexName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexName)`  
Required. The index that owns this collection of assets. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ViewIndexedAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ViewIndexedAssetsResponse)[IndexedAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexedAsset)` | A pageable sequence of [IndexedAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexedAsset) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::IndexName index = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]");
    // Make the request
    PagedEnumerable<gcvv::ViewIndexedAssetsResponse, gcvv::IndexedAsset> response = warehouseClient.ViewIndexedAssets(index);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::IndexedAsset item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ViewIndexedAssetsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::IndexedAsset item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::IndexedAsset> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::IndexedAsset item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ViewIndexedAssets(ViewIndexedAssetsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ViewIndexedAssetsResponse, IndexedAsset> ViewIndexedAssets(ViewIndexedAssetsRequest request, CallSettings callSettings = null)

Lists assets inside an index.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ViewIndexedAssetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ViewIndexedAssetsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ViewIndexedAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ViewIndexedAssetsResponse)[IndexedAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexedAsset)` | A pageable sequence of [IndexedAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexedAsset) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    gcvv::ViewIndexedAssetsRequest request = new gcvv::ViewIndexedAssetsRequest
    {
        IndexAsIndexName = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<gcvv::ViewIndexedAssetsResponse, gcvv::IndexedAsset> response = warehouseClient.ViewIndexedAssets(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::IndexedAsset item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ViewIndexedAssetsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::IndexedAsset item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::IndexedAsset> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::IndexedAsset item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ViewIndexedAssets(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ViewIndexedAssetsResponse, IndexedAsset> ViewIndexedAssets(string index, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists assets inside an index.

**Parameters**  
---  
**Name** | **Description**  
`index` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The index that owns this collection of assets. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ViewIndexedAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ViewIndexedAssetsResponse)[IndexedAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexedAsset)` | A pageable sequence of [IndexedAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexedAsset) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = gcvv::WarehouseClient.Create();
    // Initialize request argument(s)
    string index = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/indexes/[INDEX]";
    // Make the request
    PagedEnumerable<gcvv::ViewIndexedAssetsResponse, gcvv::IndexedAsset> response = warehouseClient.ViewIndexedAssets(index);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcvv::IndexedAsset item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcvv::ViewIndexedAssetsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::IndexedAsset item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::IndexedAsset> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::IndexedAsset item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ViewIndexedAssetsAsync(IndexName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ViewIndexedAssetsResponse, IndexedAsset> ViewIndexedAssetsAsync(IndexName index, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists assets inside an index.

**Parameters**  
---  
**Name** | **Description**  
`index` | `[IndexName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexName)`  
Required. The index that owns this collection of assets. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ViewIndexedAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ViewIndexedAssetsResponse)[IndexedAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexedAsset)` | A pageable asynchronous sequence of [IndexedAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexedAsset) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::IndexName index = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]");
    // Make the request
    PagedAsyncEnumerable<gcvv::ViewIndexedAssetsResponse, gcvv::IndexedAsset> response = warehouseClient.ViewIndexedAssetsAsync(index);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::IndexedAsset item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ViewIndexedAssetsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::IndexedAsset item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::IndexedAsset> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::IndexedAsset item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ViewIndexedAssetsAsync(ViewIndexedAssetsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ViewIndexedAssetsResponse, IndexedAsset> ViewIndexedAssetsAsync(ViewIndexedAssetsRequest request, CallSettings callSettings = null)

Lists assets inside an index.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ViewIndexedAssetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ViewIndexedAssetsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ViewIndexedAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ViewIndexedAssetsResponse)[IndexedAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexedAsset)` | A pageable asynchronous sequence of [IndexedAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexedAsset) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    gcvv::ViewIndexedAssetsRequest request = new gcvv::ViewIndexedAssetsRequest
    {
        IndexAsIndexName = gcvv::IndexName.FromProjectNumberLocationCorpusIndex("[PROJECT_NUMBER]", "[LOCATION]", "[CORPUS]", "[INDEX]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<gcvv::ViewIndexedAssetsResponse, gcvv::IndexedAsset> response = warehouseClient.ViewIndexedAssetsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::IndexedAsset item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ViewIndexedAssetsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::IndexedAsset item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::IndexedAsset> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::IndexedAsset item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ViewIndexedAssetsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ViewIndexedAssetsResponse, IndexedAsset> ViewIndexedAssetsAsync(string index, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists assets inside an index.

**Parameters**  
---  
**Name** | **Description**  
`index` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The index that owns this collection of assets. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/indexes/{index}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ViewIndexedAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ViewIndexedAssetsResponse)[IndexedAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexedAsset)` | A pageable asynchronous sequence of [IndexedAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.IndexedAsset) resources.  
**Example**
    
    
    // Create client
    gcvv::WarehouseClient warehouseClient = await gcvv::WarehouseClient.CreateAsync();
    // Initialize request argument(s)
    string index = "projects/[PROJECT_NUMBER]/locations/[LOCATION]/corpora/[CORPUS]/indexes/[INDEX]";
    // Make the request
    PagedAsyncEnumerable<gcvv::ViewIndexedAssetsResponse, gcvv::IndexedAsset> response = warehouseClient.ViewIndexedAssetsAsync(index);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (gcvv::IndexedAsset item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (gcvv::ViewIndexedAssetsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcvv::IndexedAsset item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcvv::IndexedAsset> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcvv::IndexedAsset item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
