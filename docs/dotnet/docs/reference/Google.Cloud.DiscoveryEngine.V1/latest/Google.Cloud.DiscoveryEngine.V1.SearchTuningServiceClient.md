---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchTuningServiceClient
title: Discovery Engine v1 API - Class SearchTuningServiceClient (1.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:56.296240+00:00
---

# Discovery Engine v1 API - Class SearchTuningServiceClient (1.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchTuningServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1 API - Class SearchTuningServiceClient (1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0-beta06 
    
    
    public abstract class SearchTuningServiceClient

Reference documentation and code samples for the Discovery Engine v1 API class SearchTuningServiceClient.

SearchTuningService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SearchTuningServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[SearchTuningServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchTuningServiceClientImpl)

## Namespace

[Google.Cloud.DiscoveryEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1)

## Assembly

Google.Cloud.DiscoveryEngine.V1.dll

## Remarks

Service for search tuning.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the SearchTuningService service, which is a host of "discoveryengine.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default SearchTuningService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default SearchTuningService scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual SearchTuningService.SearchTuningServiceClient GrpcClient { get; }

The underlying gRPC SearchTuningService client

**Property Value**  
---  
**Type** | **Description**  
`[SearchTuningService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchTuningService)[SearchTuningServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchTuningService.SearchTuningServiceClient)` |   
  
### LocationsClient
    
    
    public virtual LocationsClient LocationsClient { get; }

The [LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
### TrainCustomModelOperationsClient
    
    
    public virtual OperationsClient TrainCustomModelOperationsClient { get; }

The long-running operations client for `TrainCustomModel`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### Create()
    
    
    public static SearchTuningServiceClient Create()

Synchronously creates a [SearchTuningServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchTuningServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [SearchTuningServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchTuningServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[SearchTuningServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchTuningServiceClient)` | The created [SearchTuningServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchTuningServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<SearchTuningServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [SearchTuningServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchTuningServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [SearchTuningServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchTuningServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchTuningServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchTuningServiceClient)` | The task representing the created [SearchTuningServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchTuningServiceClient).  
  
### ListCustomModels(ListCustomModelsRequest, CallSettings)
    
    
    public virtual ListCustomModelsResponse ListCustomModels(ListCustomModelsRequest request, CallSettings callSettings = null)

Gets a list of all the custom models.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCustomModelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ListCustomModelsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ListCustomModelsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ListCustomModelsResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    SearchTuningServiceClient searchTuningServiceClient = SearchTuningServiceClient.Create();
    // Initialize request argument(s)
    ListCustomModelsRequest request = new ListCustomModelsRequest
    {
        DataStoreAsDataStoreName = DataStoreName.FromProjectLocationDataStore("[PROJECT]", "[LOCATION]", "[DATA_STORE]"),
    };
    // Make the request
    ListCustomModelsResponse response = searchTuningServiceClient.ListCustomModels(request);
    

### ListCustomModelsAsync(ListCustomModelsRequest, CallSettings)
    
    
    public virtual Task<ListCustomModelsResponse> ListCustomModelsAsync(ListCustomModelsRequest request, CallSettings callSettings = null)

Gets a list of all the custom models.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCustomModelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ListCustomModelsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListCustomModelsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ListCustomModelsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SearchTuningServiceClient searchTuningServiceClient = await SearchTuningServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListCustomModelsRequest request = new ListCustomModelsRequest
    {
        DataStoreAsDataStoreName = DataStoreName.FromProjectLocationDataStore("[PROJECT]", "[LOCATION]", "[DATA_STORE]"),
    };
    // Make the request
    ListCustomModelsResponse response = await searchTuningServiceClient.ListCustomModelsAsync(request);
    

### ListCustomModelsAsync(ListCustomModelsRequest, CancellationToken)
    
    
    public virtual Task<ListCustomModelsResponse> ListCustomModelsAsync(ListCustomModelsRequest request, CancellationToken cancellationToken)

Gets a list of all the custom models.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCustomModelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ListCustomModelsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListCustomModelsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ListCustomModelsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SearchTuningServiceClient searchTuningServiceClient = await SearchTuningServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListCustomModelsRequest request = new ListCustomModelsRequest
    {
        DataStoreAsDataStoreName = DataStoreName.FromProjectLocationDataStore("[PROJECT]", "[LOCATION]", "[DATA_STORE]"),
    };
    // Make the request
    ListCustomModelsResponse response = await searchTuningServiceClient.ListCustomModelsAsync(request);
    

### PollOnceTrainCustomModel(string, CallSettings)
    
    
    public virtual Operation<TrainCustomModelResponse, TrainCustomModelMetadata> PollOnceTrainCustomModel(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `TrainCustomModel`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[TrainCustomModelResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.TrainCustomModelResponse)[TrainCustomModelMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.TrainCustomModelMetadata)` | The result of polling the operation.  
  
### PollOnceTrainCustomModelAsync(string, CallSettings)
    
    
    public virtual Task<Operation<TrainCustomModelResponse, TrainCustomModelMetadata>> PollOnceTrainCustomModelAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `TrainCustomModel`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[TrainCustomModelResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.TrainCustomModelResponse)[TrainCustomModelMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.TrainCustomModelMetadata)` | A task representing the result of polling the operation.  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchTuningServiceClient#Google_Cloud_DiscoveryEngine_V1_SearchTuningServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchTuningServiceClient#Google_Cloud_DiscoveryEngine_V1_SearchTuningServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchTuningServiceClient#Google_Cloud_DiscoveryEngine_V1_SearchTuningServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchTuningServiceClient#Google_Cloud_DiscoveryEngine_V1_SearchTuningServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### TrainCustomModel(TrainCustomModelRequest, CallSettings)
    
    
    public virtual Operation<TrainCustomModelResponse, TrainCustomModelMetadata> TrainCustomModel(TrainCustomModelRequest request, CallSettings callSettings = null)

Trains a custom model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TrainCustomModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.TrainCustomModelRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[TrainCustomModelResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.TrainCustomModelResponse)[TrainCustomModelMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.TrainCustomModelMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    SearchTuningServiceClient searchTuningServiceClient = SearchTuningServiceClient.Create();
    // Initialize request argument(s)
    TrainCustomModelRequest request = new TrainCustomModelRequest
    {
        DataStoreAsDataStoreName = DataStoreName.FromProjectLocationDataStore("[PROJECT]", "[LOCATION]", "[DATA_STORE]"),
        GcsTrainingInput = new TrainCustomModelRequest.Types.GcsTrainingInput(),
        ModelType = "",
        ErrorConfig = new ImportErrorConfig(),
        ModelId = "",
    };
    // Make the request
    Operation<TrainCustomModelResponse, TrainCustomModelMetadata> response = searchTuningServiceClient.TrainCustomModel(request);
    
    // Poll until the returned long-running operation is complete
    Operation<TrainCustomModelResponse, TrainCustomModelMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    TrainCustomModelResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<TrainCustomModelResponse, TrainCustomModelMetadata> retrievedResponse = searchTuningServiceClient.PollOnceTrainCustomModel(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        TrainCustomModelResponse retrievedResult = retrievedResponse.Result;
    }
    

### TrainCustomModelAsync(TrainCustomModelRequest, CallSettings)
    
    
    public virtual Task<Operation<TrainCustomModelResponse, TrainCustomModelMetadata>> TrainCustomModelAsync(TrainCustomModelRequest request, CallSettings callSettings = null)

Trains a custom model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TrainCustomModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.TrainCustomModelRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[TrainCustomModelResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.TrainCustomModelResponse)[TrainCustomModelMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.TrainCustomModelMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SearchTuningServiceClient searchTuningServiceClient = await SearchTuningServiceClient.CreateAsync();
    // Initialize request argument(s)
    TrainCustomModelRequest request = new TrainCustomModelRequest
    {
        DataStoreAsDataStoreName = DataStoreName.FromProjectLocationDataStore("[PROJECT]", "[LOCATION]", "[DATA_STORE]"),
        GcsTrainingInput = new TrainCustomModelRequest.Types.GcsTrainingInput(),
        ModelType = "",
        ErrorConfig = new ImportErrorConfig(),
        ModelId = "",
    };
    // Make the request
    Operation<TrainCustomModelResponse, TrainCustomModelMetadata> response = await searchTuningServiceClient.TrainCustomModelAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<TrainCustomModelResponse, TrainCustomModelMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    TrainCustomModelResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<TrainCustomModelResponse, TrainCustomModelMetadata> retrievedResponse = await searchTuningServiceClient.PollOnceTrainCustomModelAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        TrainCustomModelResponse retrievedResult = retrievedResponse.Result;
    }
    

### TrainCustomModelAsync(TrainCustomModelRequest, CancellationToken)
    
    
    public virtual Task<Operation<TrainCustomModelResponse, TrainCustomModelMetadata>> TrainCustomModelAsync(TrainCustomModelRequest request, CancellationToken cancellationToken)

Trains a custom model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TrainCustomModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.TrainCustomModelRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[TrainCustomModelResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.TrainCustomModelResponse)[TrainCustomModelMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.TrainCustomModelMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SearchTuningServiceClient searchTuningServiceClient = await SearchTuningServiceClient.CreateAsync();
    // Initialize request argument(s)
    TrainCustomModelRequest request = new TrainCustomModelRequest
    {
        DataStoreAsDataStoreName = DataStoreName.FromProjectLocationDataStore("[PROJECT]", "[LOCATION]", "[DATA_STORE]"),
        GcsTrainingInput = new TrainCustomModelRequest.Types.GcsTrainingInput(),
        ModelType = "",
        ErrorConfig = new ImportErrorConfig(),
        ModelId = "",
    };
    // Make the request
    Operation<TrainCustomModelResponse, TrainCustomModelMetadata> response = await searchTuningServiceClient.TrainCustomModelAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<TrainCustomModelResponse, TrainCustomModelMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    TrainCustomModelResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<TrainCustomModelResponse, TrainCustomModelMetadata> retrievedResponse = await searchTuningServiceClient.PollOnceTrainCustomModelAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        TrainCustomModelResponse retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
