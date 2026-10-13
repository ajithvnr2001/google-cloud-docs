---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryServiceClient
title: Vertex AI v1beta1 API - Class FeatureRegistryServiceClient (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:45.270319+00:00
---

# Vertex AI v1beta1 API - Class FeatureRegistryServiceClient (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class FeatureRegistryServiceClient (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public abstract class FeatureRegistryServiceClient

Reference documentation and code samples for the Vertex AI v1beta1 API class FeatureRegistryServiceClient.

FeatureRegistryService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > FeatureRegistryServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[FeatureRegistryServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryServiceClientImpl)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Remarks

The service that handles CRUD and List for resources for FeatureRegistry.

## Properties 

### BatchCreateFeaturesOperationsClient
    
    
    public virtual OperationsClient BatchCreateFeaturesOperationsClient { get; }

The long-running operations client for `BatchCreateFeatures`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateFeatureGroupOperationsClient
    
    
    public virtual OperationsClient CreateFeatureGroupOperationsClient { get; }

The long-running operations client for `CreateFeatureGroup`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateFeatureMonitorOperationsClient
    
    
    public virtual OperationsClient CreateFeatureMonitorOperationsClient { get; }

The long-running operations client for `CreateFeatureMonitor`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateFeatureOperationsClient
    
    
    public virtual OperationsClient CreateFeatureOperationsClient { get; }

The long-running operations client for `CreateFeature`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the FeatureRegistryService service, which is a host of "aiplatform.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default FeatureRegistryService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default FeatureRegistryService scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteFeatureGroupOperationsClient
    
    
    public virtual OperationsClient DeleteFeatureGroupOperationsClient { get; }

The long-running operations client for `DeleteFeatureGroup`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteFeatureMonitorOperationsClient
    
    
    public virtual OperationsClient DeleteFeatureMonitorOperationsClient { get; }

The long-running operations client for `DeleteFeatureMonitor`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteFeatureOperationsClient
    
    
    public virtual OperationsClient DeleteFeatureOperationsClient { get; }

The long-running operations client for `DeleteFeature`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual FeatureRegistryService.FeatureRegistryServiceClient GrpcClient { get; }

The underlying gRPC FeatureRegistryService client

**Property Value**  
---  
**Type** | **Description**  
`[FeatureRegistryService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryService)[FeatureRegistryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryService.FeatureRegistryServiceClient)` |   
  
### IAMPolicyClient
    
    
    public virtual IAMPolicyClient IAMPolicyClient { get; }

The [IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicyClient.html)` |   
  
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
  
### UpdateFeatureGroupOperationsClient
    
    
    public virtual OperationsClient UpdateFeatureGroupOperationsClient { get; }

The long-running operations client for `UpdateFeatureGroup`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateFeatureMonitorOperationsClient
    
    
    public virtual OperationsClient UpdateFeatureMonitorOperationsClient { get; }

The long-running operations client for `UpdateFeatureMonitor`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateFeatureOperationsClient
    
    
    public virtual OperationsClient UpdateFeatureOperationsClient { get; }

The long-running operations client for `UpdateFeature`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### BatchCreateFeatures(BatchCreateFeaturesRequest, CallSettings)
    
    
    public virtual Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> BatchCreateFeatures(BatchCreateFeaturesRequest request, CallSettings callSettings = null)

Creates a batch of Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateFeaturesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesResponse)[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    BatchCreateFeaturesRequest request = new BatchCreateFeaturesRequest
    {
        ParentAsEntityTypeName = EntityTypeName.FromProjectLocationFeaturestoreEntityType("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]"),
        Requests =
        {
            new CreateFeatureRequest(),
        },
    };
    // Make the request
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> response = featureRegistryServiceClient.BatchCreateFeatures(request);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    BatchCreateFeaturesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceBatchCreateFeatures(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchCreateFeaturesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateFeatures(EntityTypeName, IEnumerable<CreateFeatureRequest>, CallSettings)
    
    
    public virtual Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> BatchCreateFeatures(EntityTypeName parent, IEnumerable<CreateFeatureRequest> requests, CallSettings callSettings = null)

Creates a batch of Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.EntityTypeName)`  
Required. The resource name of the EntityType/FeatureGroup to create the batch of Features under. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureRequest)`  
Required. The request message specifying the Features to create. All Features must be created under the same parent EntityType / FeatureGroup. The `parent` field in each child request message can be omitted. If `parent` is set in a child request, then the value must match the `parent` value in this request message.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesResponse)[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    EntityTypeName parent = EntityTypeName.FromProjectLocationFeaturestoreEntityType("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
    IEnumerable<CreateFeatureRequest> requests = new CreateFeatureRequest[]
    {
        new CreateFeatureRequest(),
    };
    // Make the request
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> response = featureRegistryServiceClient.BatchCreateFeatures(parent, requests);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    BatchCreateFeaturesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceBatchCreateFeatures(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchCreateFeaturesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateFeatures(FeatureGroupName, IEnumerable<CreateFeatureRequest>, CallSettings)
    
    
    public virtual Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> BatchCreateFeatures(FeatureGroupName parent, IEnumerable<CreateFeatureRequest> requests, CallSettings callSettings = null)

Creates a batch of Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroupName)`  
Required. The resource name of the EntityType/FeatureGroup to create the batch of Features under. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureRequest)`  
Required. The request message specifying the Features to create. All Features must be created under the same parent EntityType / FeatureGroup. The `parent` field in each child request message can be omitted. If `parent` is set in a child request, then the value must match the `parent` value in this request message.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesResponse)[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    FeatureGroupName parent = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
    IEnumerable<CreateFeatureRequest> requests = new CreateFeatureRequest[]
    {
        new CreateFeatureRequest(),
    };
    // Make the request
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> response = featureRegistryServiceClient.BatchCreateFeatures(parent, requests);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    BatchCreateFeaturesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceBatchCreateFeatures(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchCreateFeaturesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateFeatures(string, IEnumerable<CreateFeatureRequest>, CallSettings)
    
    
    public virtual Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> BatchCreateFeatures(string parent, IEnumerable<CreateFeatureRequest> requests, CallSettings callSettings = null)

Creates a batch of Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the EntityType/FeatureGroup to create the batch of Features under. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureRequest)`  
Required. The request message specifying the Features to create. All Features must be created under the same parent EntityType / FeatureGroup. The `parent` field in each child request message can be omitted. If `parent` is set in a child request, then the value must match the `parent` value in this request message.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesResponse)[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featurestores/[FEATURESTORE]/entityTypes/[ENTITY_TYPE]";
    IEnumerable<CreateFeatureRequest> requests = new CreateFeatureRequest[]
    {
        new CreateFeatureRequest(),
    };
    // Make the request
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> response = featureRegistryServiceClient.BatchCreateFeatures(parent, requests);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    BatchCreateFeaturesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceBatchCreateFeatures(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchCreateFeaturesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateFeaturesAsync(BatchCreateFeaturesRequest, CallSettings)
    
    
    public virtual Task<Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata>> BatchCreateFeaturesAsync(BatchCreateFeaturesRequest request, CallSettings callSettings = null)

Creates a batch of Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateFeaturesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesResponse)[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    BatchCreateFeaturesRequest request = new BatchCreateFeaturesRequest
    {
        ParentAsEntityTypeName = EntityTypeName.FromProjectLocationFeaturestoreEntityType("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]"),
        Requests =
        {
            new CreateFeatureRequest(),
        },
    };
    // Make the request
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> response = await featureRegistryServiceClient.BatchCreateFeaturesAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchCreateFeaturesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceBatchCreateFeaturesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchCreateFeaturesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateFeaturesAsync(BatchCreateFeaturesRequest, CancellationToken)
    
    
    public virtual Task<Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata>> BatchCreateFeaturesAsync(BatchCreateFeaturesRequest request, CancellationToken cancellationToken)

Creates a batch of Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateFeaturesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesResponse)[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    BatchCreateFeaturesRequest request = new BatchCreateFeaturesRequest
    {
        ParentAsEntityTypeName = EntityTypeName.FromProjectLocationFeaturestoreEntityType("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]"),
        Requests =
        {
            new CreateFeatureRequest(),
        },
    };
    // Make the request
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> response = await featureRegistryServiceClient.BatchCreateFeaturesAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchCreateFeaturesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceBatchCreateFeaturesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchCreateFeaturesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateFeaturesAsync(EntityTypeName, IEnumerable<CreateFeatureRequest>, CallSettings)
    
    
    public virtual Task<Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata>> BatchCreateFeaturesAsync(EntityTypeName parent, IEnumerable<CreateFeatureRequest> requests, CallSettings callSettings = null)

Creates a batch of Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.EntityTypeName)`  
Required. The resource name of the EntityType/FeatureGroup to create the batch of Features under. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureRequest)`  
Required. The request message specifying the Features to create. All Features must be created under the same parent EntityType / FeatureGroup. The `parent` field in each child request message can be omitted. If `parent` is set in a child request, then the value must match the `parent` value in this request message.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesResponse)[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    EntityTypeName parent = EntityTypeName.FromProjectLocationFeaturestoreEntityType("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
    IEnumerable<CreateFeatureRequest> requests = new CreateFeatureRequest[]
    {
        new CreateFeatureRequest(),
    };
    // Make the request
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> response = await featureRegistryServiceClient.BatchCreateFeaturesAsync(parent, requests);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchCreateFeaturesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceBatchCreateFeaturesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchCreateFeaturesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateFeaturesAsync(EntityTypeName, IEnumerable<CreateFeatureRequest>, CancellationToken)
    
    
    public virtual Task<Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata>> BatchCreateFeaturesAsync(EntityTypeName parent, IEnumerable<CreateFeatureRequest> requests, CancellationToken cancellationToken)

Creates a batch of Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.EntityTypeName)`  
Required. The resource name of the EntityType/FeatureGroup to create the batch of Features under. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureRequest)`  
Required. The request message specifying the Features to create. All Features must be created under the same parent EntityType / FeatureGroup. The `parent` field in each child request message can be omitted. If `parent` is set in a child request, then the value must match the `parent` value in this request message.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesResponse)[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    EntityTypeName parent = EntityTypeName.FromProjectLocationFeaturestoreEntityType("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
    IEnumerable<CreateFeatureRequest> requests = new CreateFeatureRequest[]
    {
        new CreateFeatureRequest(),
    };
    // Make the request
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> response = await featureRegistryServiceClient.BatchCreateFeaturesAsync(parent, requests);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchCreateFeaturesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceBatchCreateFeaturesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchCreateFeaturesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateFeaturesAsync(FeatureGroupName, IEnumerable<CreateFeatureRequest>, CallSettings)
    
    
    public virtual Task<Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata>> BatchCreateFeaturesAsync(FeatureGroupName parent, IEnumerable<CreateFeatureRequest> requests, CallSettings callSettings = null)

Creates a batch of Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroupName)`  
Required. The resource name of the EntityType/FeatureGroup to create the batch of Features under. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureRequest)`  
Required. The request message specifying the Features to create. All Features must be created under the same parent EntityType / FeatureGroup. The `parent` field in each child request message can be omitted. If `parent` is set in a child request, then the value must match the `parent` value in this request message.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesResponse)[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureGroupName parent = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
    IEnumerable<CreateFeatureRequest> requests = new CreateFeatureRequest[]
    {
        new CreateFeatureRequest(),
    };
    // Make the request
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> response = await featureRegistryServiceClient.BatchCreateFeaturesAsync(parent, requests);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchCreateFeaturesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceBatchCreateFeaturesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchCreateFeaturesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateFeaturesAsync(FeatureGroupName, IEnumerable<CreateFeatureRequest>, CancellationToken)
    
    
    public virtual Task<Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata>> BatchCreateFeaturesAsync(FeatureGroupName parent, IEnumerable<CreateFeatureRequest> requests, CancellationToken cancellationToken)

Creates a batch of Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroupName)`  
Required. The resource name of the EntityType/FeatureGroup to create the batch of Features under. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureRequest)`  
Required. The request message specifying the Features to create. All Features must be created under the same parent EntityType / FeatureGroup. The `parent` field in each child request message can be omitted. If `parent` is set in a child request, then the value must match the `parent` value in this request message.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesResponse)[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureGroupName parent = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
    IEnumerable<CreateFeatureRequest> requests = new CreateFeatureRequest[]
    {
        new CreateFeatureRequest(),
    };
    // Make the request
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> response = await featureRegistryServiceClient.BatchCreateFeaturesAsync(parent, requests);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchCreateFeaturesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceBatchCreateFeaturesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchCreateFeaturesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateFeaturesAsync(string, IEnumerable<CreateFeatureRequest>, CallSettings)
    
    
    public virtual Task<Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata>> BatchCreateFeaturesAsync(string parent, IEnumerable<CreateFeatureRequest> requests, CallSettings callSettings = null)

Creates a batch of Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the EntityType/FeatureGroup to create the batch of Features under. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureRequest)`  
Required. The request message specifying the Features to create. All Features must be created under the same parent EntityType / FeatureGroup. The `parent` field in each child request message can be omitted. If `parent` is set in a child request, then the value must match the `parent` value in this request message.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesResponse)[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featurestores/[FEATURESTORE]/entityTypes/[ENTITY_TYPE]";
    IEnumerable<CreateFeatureRequest> requests = new CreateFeatureRequest[]
    {
        new CreateFeatureRequest(),
    };
    // Make the request
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> response = await featureRegistryServiceClient.BatchCreateFeaturesAsync(parent, requests);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchCreateFeaturesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceBatchCreateFeaturesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchCreateFeaturesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchCreateFeaturesAsync(string, IEnumerable<CreateFeatureRequest>, CancellationToken)
    
    
    public virtual Task<Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata>> BatchCreateFeaturesAsync(string parent, IEnumerable<CreateFeatureRequest> requests, CancellationToken cancellationToken)

Creates a batch of Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the EntityType/FeatureGroup to create the batch of Features under. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureRequest)`  
Required. The request message specifying the Features to create. All Features must be created under the same parent EntityType / FeatureGroup. The `parent` field in each child request message can be omitted. If `parent` is set in a child request, then the value must match the `parent` value in this request message.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesResponse)[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featurestores/[FEATURESTORE]/entityTypes/[ENTITY_TYPE]";
    IEnumerable<CreateFeatureRequest> requests = new CreateFeatureRequest[]
    {
        new CreateFeatureRequest(),
    };
    // Make the request
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> response = await featureRegistryServiceClient.BatchCreateFeaturesAsync(parent, requests);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchCreateFeaturesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceBatchCreateFeaturesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchCreateFeaturesResponse retrievedResult = retrievedResponse.Result;
    }
    

### Create()
    
    
    public static FeatureRegistryServiceClient Create()

Synchronously creates a [FeatureRegistryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [FeatureRegistryServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[FeatureRegistryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryServiceClient)` | The created [FeatureRegistryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<FeatureRegistryServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [FeatureRegistryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [FeatureRegistryServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureRegistryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryServiceClient)` | The task representing the created [FeatureRegistryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryServiceClient).  
  
### CreateFeature(CreateFeatureRequest, CallSettings)
    
    
    public virtual Operation<Feature, CreateFeatureOperationMetadata> CreateFeature(CreateFeatureRequest request, CallSettings callSettings = null)

Creates a new Feature in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[CreateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    CreateFeatureRequest request = new CreateFeatureRequest
    {
        ParentAsEntityTypeName = EntityTypeName.FromProjectLocationFeaturestoreEntityType("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]"),
        Feature = new Feature(),
        FeatureId = "",
    };
    // Make the request
    Operation<Feature, CreateFeatureOperationMetadata> response = featureRegistryServiceClient.CreateFeature(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Feature, CreateFeatureOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Feature result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Feature, CreateFeatureOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceCreateFeature(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Feature retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeature(EntityTypeName, Feature, string, CallSettings)
    
    
    public virtual Operation<Feature, CreateFeatureOperationMetadata> CreateFeature(EntityTypeName parent, Feature feature, string featureId, CallSettings callSettings = null)

Creates a new Feature in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.EntityTypeName)`  
Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`feature` | `[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)`  
Required. The Feature to create.  
`featureId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the Feature, which will become the final component of the Feature's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[CreateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    EntityTypeName parent = EntityTypeName.FromProjectLocationFeaturestoreEntityType("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
    Feature feature = new Feature();
    string featureId = "";
    // Make the request
    Operation<Feature, CreateFeatureOperationMetadata> response = featureRegistryServiceClient.CreateFeature(parent, feature, featureId);
    
    // Poll until the returned long-running operation is complete
    Operation<Feature, CreateFeatureOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Feature result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Feature, CreateFeatureOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceCreateFeature(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Feature retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeature(FeatureGroupName, Feature, string, CallSettings)
    
    
    public virtual Operation<Feature, CreateFeatureOperationMetadata> CreateFeature(FeatureGroupName parent, Feature feature, string featureId, CallSettings callSettings = null)

Creates a new Feature in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroupName)`  
Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`feature` | `[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)`  
Required. The Feature to create.  
`featureId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the Feature, which will become the final component of the Feature's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[CreateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    FeatureGroupName parent = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
    Feature feature = new Feature();
    string featureId = "";
    // Make the request
    Operation<Feature, CreateFeatureOperationMetadata> response = featureRegistryServiceClient.CreateFeature(parent, feature, featureId);
    
    // Poll until the returned long-running operation is complete
    Operation<Feature, CreateFeatureOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Feature result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Feature, CreateFeatureOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceCreateFeature(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Feature retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeature(string, Feature, string, CallSettings)
    
    
    public virtual Operation<Feature, CreateFeatureOperationMetadata> CreateFeature(string parent, Feature feature, string featureId, CallSettings callSettings = null)

Creates a new Feature in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`feature` | `[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)`  
Required. The Feature to create.  
`featureId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the Feature, which will become the final component of the Feature's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[CreateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featurestores/[FEATURESTORE]/entityTypes/[ENTITY_TYPE]";
    Feature feature = new Feature();
    string featureId = "";
    // Make the request
    Operation<Feature, CreateFeatureOperationMetadata> response = featureRegistryServiceClient.CreateFeature(parent, feature, featureId);
    
    // Poll until the returned long-running operation is complete
    Operation<Feature, CreateFeatureOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Feature result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Feature, CreateFeatureOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceCreateFeature(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Feature retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureAsync(CreateFeatureRequest, CallSettings)
    
    
    public virtual Task<Operation<Feature, CreateFeatureOperationMetadata>> CreateFeatureAsync(CreateFeatureRequest request, CallSettings callSettings = null)

Creates a new Feature in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[CreateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateFeatureRequest request = new CreateFeatureRequest
    {
        ParentAsEntityTypeName = EntityTypeName.FromProjectLocationFeaturestoreEntityType("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]"),
        Feature = new Feature(),
        FeatureId = "",
    };
    // Make the request
    Operation<Feature, CreateFeatureOperationMetadata> response = await featureRegistryServiceClient.CreateFeatureAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Feature, CreateFeatureOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Feature result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Feature, CreateFeatureOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceCreateFeatureAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Feature retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureAsync(CreateFeatureRequest, CancellationToken)
    
    
    public virtual Task<Operation<Feature, CreateFeatureOperationMetadata>> CreateFeatureAsync(CreateFeatureRequest request, CancellationToken cancellationToken)

Creates a new Feature in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[CreateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateFeatureRequest request = new CreateFeatureRequest
    {
        ParentAsEntityTypeName = EntityTypeName.FromProjectLocationFeaturestoreEntityType("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]"),
        Feature = new Feature(),
        FeatureId = "",
    };
    // Make the request
    Operation<Feature, CreateFeatureOperationMetadata> response = await featureRegistryServiceClient.CreateFeatureAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Feature, CreateFeatureOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Feature result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Feature, CreateFeatureOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceCreateFeatureAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Feature retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureAsync(EntityTypeName, Feature, string, CallSettings)
    
    
    public virtual Task<Operation<Feature, CreateFeatureOperationMetadata>> CreateFeatureAsync(EntityTypeName parent, Feature feature, string featureId, CallSettings callSettings = null)

Creates a new Feature in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.EntityTypeName)`  
Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`feature` | `[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)`  
Required. The Feature to create.  
`featureId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the Feature, which will become the final component of the Feature's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[CreateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    EntityTypeName parent = EntityTypeName.FromProjectLocationFeaturestoreEntityType("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
    Feature feature = new Feature();
    string featureId = "";
    // Make the request
    Operation<Feature, CreateFeatureOperationMetadata> response = await featureRegistryServiceClient.CreateFeatureAsync(parent, feature, featureId);
    
    // Poll until the returned long-running operation is complete
    Operation<Feature, CreateFeatureOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Feature result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Feature, CreateFeatureOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceCreateFeatureAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Feature retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureAsync(EntityTypeName, Feature, string, CancellationToken)
    
    
    public virtual Task<Operation<Feature, CreateFeatureOperationMetadata>> CreateFeatureAsync(EntityTypeName parent, Feature feature, string featureId, CancellationToken cancellationToken)

Creates a new Feature in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.EntityTypeName)`  
Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`feature` | `[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)`  
Required. The Feature to create.  
`featureId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the Feature, which will become the final component of the Feature's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[CreateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    EntityTypeName parent = EntityTypeName.FromProjectLocationFeaturestoreEntityType("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
    Feature feature = new Feature();
    string featureId = "";
    // Make the request
    Operation<Feature, CreateFeatureOperationMetadata> response = await featureRegistryServiceClient.CreateFeatureAsync(parent, feature, featureId);
    
    // Poll until the returned long-running operation is complete
    Operation<Feature, CreateFeatureOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Feature result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Feature, CreateFeatureOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceCreateFeatureAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Feature retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureAsync(FeatureGroupName, Feature, string, CallSettings)
    
    
    public virtual Task<Operation<Feature, CreateFeatureOperationMetadata>> CreateFeatureAsync(FeatureGroupName parent, Feature feature, string featureId, CallSettings callSettings = null)

Creates a new Feature in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroupName)`  
Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`feature` | `[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)`  
Required. The Feature to create.  
`featureId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the Feature, which will become the final component of the Feature's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[CreateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureGroupName parent = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
    Feature feature = new Feature();
    string featureId = "";
    // Make the request
    Operation<Feature, CreateFeatureOperationMetadata> response = await featureRegistryServiceClient.CreateFeatureAsync(parent, feature, featureId);
    
    // Poll until the returned long-running operation is complete
    Operation<Feature, CreateFeatureOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Feature result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Feature, CreateFeatureOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceCreateFeatureAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Feature retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureAsync(FeatureGroupName, Feature, string, CancellationToken)
    
    
    public virtual Task<Operation<Feature, CreateFeatureOperationMetadata>> CreateFeatureAsync(FeatureGroupName parent, Feature feature, string featureId, CancellationToken cancellationToken)

Creates a new Feature in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroupName)`  
Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`feature` | `[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)`  
Required. The Feature to create.  
`featureId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the Feature, which will become the final component of the Feature's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[CreateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureGroupName parent = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
    Feature feature = new Feature();
    string featureId = "";
    // Make the request
    Operation<Feature, CreateFeatureOperationMetadata> response = await featureRegistryServiceClient.CreateFeatureAsync(parent, feature, featureId);
    
    // Poll until the returned long-running operation is complete
    Operation<Feature, CreateFeatureOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Feature result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Feature, CreateFeatureOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceCreateFeatureAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Feature retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureAsync(string, Feature, string, CallSettings)
    
    
    public virtual Task<Operation<Feature, CreateFeatureOperationMetadata>> CreateFeatureAsync(string parent, Feature feature, string featureId, CallSettings callSettings = null)

Creates a new Feature in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`feature` | `[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)`  
Required. The Feature to create.  
`featureId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the Feature, which will become the final component of the Feature's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[CreateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featurestores/[FEATURESTORE]/entityTypes/[ENTITY_TYPE]";
    Feature feature = new Feature();
    string featureId = "";
    // Make the request
    Operation<Feature, CreateFeatureOperationMetadata> response = await featureRegistryServiceClient.CreateFeatureAsync(parent, feature, featureId);
    
    // Poll until the returned long-running operation is complete
    Operation<Feature, CreateFeatureOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Feature result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Feature, CreateFeatureOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceCreateFeatureAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Feature retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureAsync(string, Feature, string, CancellationToken)
    
    
    public virtual Task<Operation<Feature, CreateFeatureOperationMetadata>> CreateFeatureAsync(string parent, Feature feature, string featureId, CancellationToken cancellationToken)

Creates a new Feature in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`feature` | `[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)`  
Required. The Feature to create.  
`featureId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the Feature, which will become the final component of the Feature's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[CreateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featurestores/[FEATURESTORE]/entityTypes/[ENTITY_TYPE]";
    Feature feature = new Feature();
    string featureId = "";
    // Make the request
    Operation<Feature, CreateFeatureOperationMetadata> response = await featureRegistryServiceClient.CreateFeatureAsync(parent, feature, featureId);
    
    // Poll until the returned long-running operation is complete
    Operation<Feature, CreateFeatureOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Feature result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Feature, CreateFeatureOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceCreateFeatureAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Feature retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureGroup(LocationName, FeatureGroup, string, CallSettings)
    
    
    public virtual Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> CreateFeatureGroup(LocationName parent, FeatureGroup featureGroup, string featureGroupId, CallSettings callSettings = null)

Creates a new FeatureGroup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the Location to create FeatureGroups. Format: `projects/{project}/locations/{location}`  
`featureGroup` | `[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)`  
Required. The FeatureGroup to create.  
`featureGroupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this FeatureGroup, which will become the final component of the FeatureGroup's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)[CreateFeatureGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureGroupOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    FeatureGroup featureGroup = new FeatureGroup();
    string featureGroupId = "";
    // Make the request
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> response = featureRegistryServiceClient.CreateFeatureGroup(parent, featureGroup, featureGroupId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FeatureGroup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceCreateFeatureGroup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureGroup retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureGroup(CreateFeatureGroupRequest, CallSettings)
    
    
    public virtual Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> CreateFeatureGroup(CreateFeatureGroupRequest request, CallSettings callSettings = null)

Creates a new FeatureGroup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureGroupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)[CreateFeatureGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureGroupOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    CreateFeatureGroupRequest request = new CreateFeatureGroupRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        FeatureGroup = new FeatureGroup(),
        FeatureGroupId = "",
    };
    // Make the request
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> response = featureRegistryServiceClient.CreateFeatureGroup(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FeatureGroup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceCreateFeatureGroup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureGroup retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureGroup(string, FeatureGroup, string, CallSettings)
    
    
    public virtual Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> CreateFeatureGroup(string parent, FeatureGroup featureGroup, string featureGroupId, CallSettings callSettings = null)

Creates a new FeatureGroup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to create FeatureGroups. Format: `projects/{project}/locations/{location}`  
`featureGroup` | `[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)`  
Required. The FeatureGroup to create.  
`featureGroupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this FeatureGroup, which will become the final component of the FeatureGroup's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)[CreateFeatureGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureGroupOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    FeatureGroup featureGroup = new FeatureGroup();
    string featureGroupId = "";
    // Make the request
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> response = featureRegistryServiceClient.CreateFeatureGroup(parent, featureGroup, featureGroupId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FeatureGroup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceCreateFeatureGroup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureGroup retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureGroupAsync(LocationName, FeatureGroup, string, CallSettings)
    
    
    public virtual Task<Operation<FeatureGroup, CreateFeatureGroupOperationMetadata>> CreateFeatureGroupAsync(LocationName parent, FeatureGroup featureGroup, string featureGroupId, CallSettings callSettings = null)

Creates a new FeatureGroup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the Location to create FeatureGroups. Format: `projects/{project}/locations/{location}`  
`featureGroup` | `[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)`  
Required. The FeatureGroup to create.  
`featureGroupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this FeatureGroup, which will become the final component of the FeatureGroup's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)[CreateFeatureGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureGroupOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    FeatureGroup featureGroup = new FeatureGroup();
    string featureGroupId = "";
    // Make the request
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> response = await featureRegistryServiceClient.CreateFeatureGroupAsync(parent, featureGroup, featureGroupId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureGroup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceCreateFeatureGroupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureGroup retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureGroupAsync(LocationName, FeatureGroup, string, CancellationToken)
    
    
    public virtual Task<Operation<FeatureGroup, CreateFeatureGroupOperationMetadata>> CreateFeatureGroupAsync(LocationName parent, FeatureGroup featureGroup, string featureGroupId, CancellationToken cancellationToken)

Creates a new FeatureGroup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the Location to create FeatureGroups. Format: `projects/{project}/locations/{location}`  
`featureGroup` | `[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)`  
Required. The FeatureGroup to create.  
`featureGroupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this FeatureGroup, which will become the final component of the FeatureGroup's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)[CreateFeatureGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureGroupOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    FeatureGroup featureGroup = new FeatureGroup();
    string featureGroupId = "";
    // Make the request
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> response = await featureRegistryServiceClient.CreateFeatureGroupAsync(parent, featureGroup, featureGroupId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureGroup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceCreateFeatureGroupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureGroup retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureGroupAsync(CreateFeatureGroupRequest, CallSettings)
    
    
    public virtual Task<Operation<FeatureGroup, CreateFeatureGroupOperationMetadata>> CreateFeatureGroupAsync(CreateFeatureGroupRequest request, CallSettings callSettings = null)

Creates a new FeatureGroup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureGroupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)[CreateFeatureGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureGroupOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateFeatureGroupRequest request = new CreateFeatureGroupRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        FeatureGroup = new FeatureGroup(),
        FeatureGroupId = "",
    };
    // Make the request
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> response = await featureRegistryServiceClient.CreateFeatureGroupAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureGroup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceCreateFeatureGroupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureGroup retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureGroupAsync(CreateFeatureGroupRequest, CancellationToken)
    
    
    public virtual Task<Operation<FeatureGroup, CreateFeatureGroupOperationMetadata>> CreateFeatureGroupAsync(CreateFeatureGroupRequest request, CancellationToken cancellationToken)

Creates a new FeatureGroup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureGroupRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)[CreateFeatureGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureGroupOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateFeatureGroupRequest request = new CreateFeatureGroupRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        FeatureGroup = new FeatureGroup(),
        FeatureGroupId = "",
    };
    // Make the request
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> response = await featureRegistryServiceClient.CreateFeatureGroupAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureGroup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceCreateFeatureGroupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureGroup retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureGroupAsync(string, FeatureGroup, string, CallSettings)
    
    
    public virtual Task<Operation<FeatureGroup, CreateFeatureGroupOperationMetadata>> CreateFeatureGroupAsync(string parent, FeatureGroup featureGroup, string featureGroupId, CallSettings callSettings = null)

Creates a new FeatureGroup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to create FeatureGroups. Format: `projects/{project}/locations/{location}`  
`featureGroup` | `[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)`  
Required. The FeatureGroup to create.  
`featureGroupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this FeatureGroup, which will become the final component of the FeatureGroup's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)[CreateFeatureGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureGroupOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    FeatureGroup featureGroup = new FeatureGroup();
    string featureGroupId = "";
    // Make the request
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> response = await featureRegistryServiceClient.CreateFeatureGroupAsync(parent, featureGroup, featureGroupId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureGroup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceCreateFeatureGroupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureGroup retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureGroupAsync(string, FeatureGroup, string, CancellationToken)
    
    
    public virtual Task<Operation<FeatureGroup, CreateFeatureGroupOperationMetadata>> CreateFeatureGroupAsync(string parent, FeatureGroup featureGroup, string featureGroupId, CancellationToken cancellationToken)

Creates a new FeatureGroup in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to create FeatureGroups. Format: `projects/{project}/locations/{location}`  
`featureGroup` | `[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)`  
Required. The FeatureGroup to create.  
`featureGroupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this FeatureGroup, which will become the final component of the FeatureGroup's resource name. This value may be up to 128 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)[CreateFeatureGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureGroupOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    FeatureGroup featureGroup = new FeatureGroup();
    string featureGroupId = "";
    // Make the request
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> response = await featureRegistryServiceClient.CreateFeatureGroupAsync(parent, featureGroup, featureGroupId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureGroup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceCreateFeatureGroupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureGroup retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureMonitor(CreateFeatureMonitorRequest, CallSettings)
    
    
    public virtual Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> CreateFeatureMonitor(CreateFeatureMonitorRequest request, CallSettings callSettings = null)

Creates a new FeatureMonitor in a given project, location and FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)[CreateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    CreateFeatureMonitorRequest request = new CreateFeatureMonitorRequest
    {
        ParentAsFeatureGroupName = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]"),
        FeatureMonitor = new FeatureMonitor(),
        FeatureMonitorId = "",
    };
    // Make the request
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> response = featureRegistryServiceClient.CreateFeatureMonitor(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FeatureMonitor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceCreateFeatureMonitor(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureMonitor retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureMonitor(FeatureGroupName, FeatureMonitor, string, CallSettings)
    
    
    public virtual Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> CreateFeatureMonitor(FeatureGroupName parent, FeatureMonitor featureMonitor, string featureMonitorId, CallSettings callSettings = null)

Creates a new FeatureMonitor in a given project, location and FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroupName)`  
Required. The resource name of FeatureGroup to create FeatureMonitor. Format: `projects/{project}/locations/{location}/featureGroups/{featuregroup}`  
`featureMonitor` | `[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)`  
Required. The Monitor to create.  
`featureMonitorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this FeatureMonitor, which will become the final component of the FeatureGroup's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the FeatureGroup.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)[CreateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    FeatureGroupName parent = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
    FeatureMonitor featureMonitor = new FeatureMonitor();
    string featureMonitorId = "";
    // Make the request
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> response = featureRegistryServiceClient.CreateFeatureMonitor(parent, featureMonitor, featureMonitorId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FeatureMonitor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceCreateFeatureMonitor(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureMonitor retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureMonitor(string, FeatureMonitor, string, CallSettings)
    
    
    public virtual Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> CreateFeatureMonitor(string parent, FeatureMonitor featureMonitor, string featureMonitorId, CallSettings callSettings = null)

Creates a new FeatureMonitor in a given project, location and FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of FeatureGroup to create FeatureMonitor. Format: `projects/{project}/locations/{location}/featureGroups/{featuregroup}`  
`featureMonitor` | `[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)`  
Required. The Monitor to create.  
`featureMonitorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this FeatureMonitor, which will become the final component of the FeatureGroup's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the FeatureGroup.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)[CreateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]";
    FeatureMonitor featureMonitor = new FeatureMonitor();
    string featureMonitorId = "";
    // Make the request
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> response = featureRegistryServiceClient.CreateFeatureMonitor(parent, featureMonitor, featureMonitorId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FeatureMonitor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceCreateFeatureMonitor(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureMonitor retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureMonitorAsync(CreateFeatureMonitorRequest, CallSettings)
    
    
    public virtual Task<Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata>> CreateFeatureMonitorAsync(CreateFeatureMonitorRequest request, CallSettings callSettings = null)

Creates a new FeatureMonitor in a given project, location and FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)[CreateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateFeatureMonitorRequest request = new CreateFeatureMonitorRequest
    {
        ParentAsFeatureGroupName = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]"),
        FeatureMonitor = new FeatureMonitor(),
        FeatureMonitorId = "",
    };
    // Make the request
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> response = await featureRegistryServiceClient.CreateFeatureMonitorAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureMonitor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceCreateFeatureMonitorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureMonitor retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureMonitorAsync(CreateFeatureMonitorRequest, CancellationToken)
    
    
    public virtual Task<Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata>> CreateFeatureMonitorAsync(CreateFeatureMonitorRequest request, CancellationToken cancellationToken)

Creates a new FeatureMonitor in a given project, location and FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)[CreateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateFeatureMonitorRequest request = new CreateFeatureMonitorRequest
    {
        ParentAsFeatureGroupName = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]"),
        FeatureMonitor = new FeatureMonitor(),
        FeatureMonitorId = "",
    };
    // Make the request
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> response = await featureRegistryServiceClient.CreateFeatureMonitorAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureMonitor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceCreateFeatureMonitorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureMonitor retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureMonitorAsync(FeatureGroupName, FeatureMonitor, string, CallSettings)
    
    
    public virtual Task<Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata>> CreateFeatureMonitorAsync(FeatureGroupName parent, FeatureMonitor featureMonitor, string featureMonitorId, CallSettings callSettings = null)

Creates a new FeatureMonitor in a given project, location and FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroupName)`  
Required. The resource name of FeatureGroup to create FeatureMonitor. Format: `projects/{project}/locations/{location}/featureGroups/{featuregroup}`  
`featureMonitor` | `[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)`  
Required. The Monitor to create.  
`featureMonitorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this FeatureMonitor, which will become the final component of the FeatureGroup's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the FeatureGroup.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)[CreateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureGroupName parent = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
    FeatureMonitor featureMonitor = new FeatureMonitor();
    string featureMonitorId = "";
    // Make the request
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> response = await featureRegistryServiceClient.CreateFeatureMonitorAsync(parent, featureMonitor, featureMonitorId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureMonitor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceCreateFeatureMonitorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureMonitor retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureMonitorAsync(FeatureGroupName, FeatureMonitor, string, CancellationToken)
    
    
    public virtual Task<Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata>> CreateFeatureMonitorAsync(FeatureGroupName parent, FeatureMonitor featureMonitor, string featureMonitorId, CancellationToken cancellationToken)

Creates a new FeatureMonitor in a given project, location and FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroupName)`  
Required. The resource name of FeatureGroup to create FeatureMonitor. Format: `projects/{project}/locations/{location}/featureGroups/{featuregroup}`  
`featureMonitor` | `[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)`  
Required. The Monitor to create.  
`featureMonitorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this FeatureMonitor, which will become the final component of the FeatureGroup's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the FeatureGroup.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)[CreateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureGroupName parent = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
    FeatureMonitor featureMonitor = new FeatureMonitor();
    string featureMonitorId = "";
    // Make the request
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> response = await featureRegistryServiceClient.CreateFeatureMonitorAsync(parent, featureMonitor, featureMonitorId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureMonitor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceCreateFeatureMonitorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureMonitor retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureMonitorAsync(string, FeatureMonitor, string, CallSettings)
    
    
    public virtual Task<Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata>> CreateFeatureMonitorAsync(string parent, FeatureMonitor featureMonitor, string featureMonitorId, CallSettings callSettings = null)

Creates a new FeatureMonitor in a given project, location and FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of FeatureGroup to create FeatureMonitor. Format: `projects/{project}/locations/{location}/featureGroups/{featuregroup}`  
`featureMonitor` | `[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)`  
Required. The Monitor to create.  
`featureMonitorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this FeatureMonitor, which will become the final component of the FeatureGroup's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the FeatureGroup.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)[CreateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]";
    FeatureMonitor featureMonitor = new FeatureMonitor();
    string featureMonitorId = "";
    // Make the request
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> response = await featureRegistryServiceClient.CreateFeatureMonitorAsync(parent, featureMonitor, featureMonitorId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureMonitor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceCreateFeatureMonitorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureMonitor retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureMonitorAsync(string, FeatureMonitor, string, CancellationToken)
    
    
    public virtual Task<Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata>> CreateFeatureMonitorAsync(string parent, FeatureMonitor featureMonitor, string featureMonitorId, CancellationToken cancellationToken)

Creates a new FeatureMonitor in a given project, location and FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of FeatureGroup to create FeatureMonitor. Format: `projects/{project}/locations/{location}/featureGroups/{featuregroup}`  
`featureMonitor` | `[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)`  
Required. The Monitor to create.  
`featureMonitorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this FeatureMonitor, which will become the final component of the FeatureGroup's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the FeatureGroup.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)[CreateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]";
    FeatureMonitor featureMonitor = new FeatureMonitor();
    string featureMonitorId = "";
    // Make the request
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> response = await featureRegistryServiceClient.CreateFeatureMonitorAsync(parent, featureMonitor, featureMonitorId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureMonitor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceCreateFeatureMonitorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureMonitor retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureMonitorJob(CreateFeatureMonitorJobRequest, CallSettings)
    
    
    public virtual FeatureMonitorJob CreateFeatureMonitorJob(CreateFeatureMonitorJobRequest request, CallSettings callSettings = null)

Creates a new feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureMonitorJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorJobRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    CreateFeatureMonitorJobRequest request = new CreateFeatureMonitorJobRequest
    {
        ParentAsFeatureMonitorName = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]"),
        FeatureMonitorJob = new FeatureMonitorJob(),
        FeatureMonitorJobId = 0L,
    };
    // Make the request
    FeatureMonitorJob response = featureRegistryServiceClient.CreateFeatureMonitorJob(request);
    

### CreateFeatureMonitorJob(FeatureMonitorName, FeatureMonitorJob, long, CallSettings)
    
    
    public virtual FeatureMonitorJob CreateFeatureMonitorJob(FeatureMonitorName parent, FeatureMonitorJob featureMonitorJob, long featureMonitorJobId, CallSettings callSettings = null)

Creates a new feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureMonitorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorName)`  
Required. The resource name of FeatureMonitor to create FeatureMonitorJob. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`featureMonitorJob` | `[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)`  
Required. The Monitor to create.  
`featureMonitorJobId` | `[long](https://learn.microsoft.com/dotnet/api/system.int64)`  
Optional. Output only. System-generated ID for feature monitor job.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    FeatureMonitorName parent = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]");
    FeatureMonitorJob featureMonitorJob = new FeatureMonitorJob();
    long featureMonitorJobId = 0L;
    // Make the request
    FeatureMonitorJob response = featureRegistryServiceClient.CreateFeatureMonitorJob(parent, featureMonitorJob, featureMonitorJobId);
    

### CreateFeatureMonitorJob(string, FeatureMonitorJob, long, CallSettings)
    
    
    public virtual FeatureMonitorJob CreateFeatureMonitorJob(string parent, FeatureMonitorJob featureMonitorJob, long featureMonitorJobId, CallSettings callSettings = null)

Creates a new feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of FeatureMonitor to create FeatureMonitorJob. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`featureMonitorJob` | `[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)`  
Required. The Monitor to create.  
`featureMonitorJobId` | `[long](https://learn.microsoft.com/dotnet/api/system.int64)`  
Optional. Output only. System-generated ID for feature monitor job.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]/featureMonitors/[FEATURE_MONITOR]";
    FeatureMonitorJob featureMonitorJob = new FeatureMonitorJob();
    long featureMonitorJobId = 0L;
    // Make the request
    FeatureMonitorJob response = featureRegistryServiceClient.CreateFeatureMonitorJob(parent, featureMonitorJob, featureMonitorJobId);
    

### CreateFeatureMonitorJobAsync(CreateFeatureMonitorJobRequest, CallSettings)
    
    
    public virtual Task<FeatureMonitorJob> CreateFeatureMonitorJobAsync(CreateFeatureMonitorJobRequest request, CallSettings callSettings = null)

Creates a new feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureMonitorJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorJobRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateFeatureMonitorJobRequest request = new CreateFeatureMonitorJobRequest
    {
        ParentAsFeatureMonitorName = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]"),
        FeatureMonitorJob = new FeatureMonitorJob(),
        FeatureMonitorJobId = 0L,
    };
    // Make the request
    FeatureMonitorJob response = await featureRegistryServiceClient.CreateFeatureMonitorJobAsync(request);
    

### CreateFeatureMonitorJobAsync(CreateFeatureMonitorJobRequest, CancellationToken)
    
    
    public virtual Task<FeatureMonitorJob> CreateFeatureMonitorJobAsync(CreateFeatureMonitorJobRequest request, CancellationToken cancellationToken)

Creates a new feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureMonitorJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorJobRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateFeatureMonitorJobRequest request = new CreateFeatureMonitorJobRequest
    {
        ParentAsFeatureMonitorName = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]"),
        FeatureMonitorJob = new FeatureMonitorJob(),
        FeatureMonitorJobId = 0L,
    };
    // Make the request
    FeatureMonitorJob response = await featureRegistryServiceClient.CreateFeatureMonitorJobAsync(request);
    

### CreateFeatureMonitorJobAsync(FeatureMonitorName, FeatureMonitorJob, long, CallSettings)
    
    
    public virtual Task<FeatureMonitorJob> CreateFeatureMonitorJobAsync(FeatureMonitorName parent, FeatureMonitorJob featureMonitorJob, long featureMonitorJobId, CallSettings callSettings = null)

Creates a new feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureMonitorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorName)`  
Required. The resource name of FeatureMonitor to create FeatureMonitorJob. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`featureMonitorJob` | `[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)`  
Required. The Monitor to create.  
`featureMonitorJobId` | `[long](https://learn.microsoft.com/dotnet/api/system.int64)`  
Optional. Output only. System-generated ID for feature monitor job.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureMonitorName parent = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]");
    FeatureMonitorJob featureMonitorJob = new FeatureMonitorJob();
    long featureMonitorJobId = 0L;
    // Make the request
    FeatureMonitorJob response = await featureRegistryServiceClient.CreateFeatureMonitorJobAsync(parent, featureMonitorJob, featureMonitorJobId);
    

### CreateFeatureMonitorJobAsync(FeatureMonitorName, FeatureMonitorJob, long, CancellationToken)
    
    
    public virtual Task<FeatureMonitorJob> CreateFeatureMonitorJobAsync(FeatureMonitorName parent, FeatureMonitorJob featureMonitorJob, long featureMonitorJobId, CancellationToken cancellationToken)

Creates a new feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureMonitorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorName)`  
Required. The resource name of FeatureMonitor to create FeatureMonitorJob. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`featureMonitorJob` | `[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)`  
Required. The Monitor to create.  
`featureMonitorJobId` | `[long](https://learn.microsoft.com/dotnet/api/system.int64)`  
Optional. Output only. System-generated ID for feature monitor job.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureMonitorName parent = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]");
    FeatureMonitorJob featureMonitorJob = new FeatureMonitorJob();
    long featureMonitorJobId = 0L;
    // Make the request
    FeatureMonitorJob response = await featureRegistryServiceClient.CreateFeatureMonitorJobAsync(parent, featureMonitorJob, featureMonitorJobId);
    

### CreateFeatureMonitorJobAsync(string, FeatureMonitorJob, long, CallSettings)
    
    
    public virtual Task<FeatureMonitorJob> CreateFeatureMonitorJobAsync(string parent, FeatureMonitorJob featureMonitorJob, long featureMonitorJobId, CallSettings callSettings = null)

Creates a new feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of FeatureMonitor to create FeatureMonitorJob. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`featureMonitorJob` | `[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)`  
Required. The Monitor to create.  
`featureMonitorJobId` | `[long](https://learn.microsoft.com/dotnet/api/system.int64)`  
Optional. Output only. System-generated ID for feature monitor job.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]/featureMonitors/[FEATURE_MONITOR]";
    FeatureMonitorJob featureMonitorJob = new FeatureMonitorJob();
    long featureMonitorJobId = 0L;
    // Make the request
    FeatureMonitorJob response = await featureRegistryServiceClient.CreateFeatureMonitorJobAsync(parent, featureMonitorJob, featureMonitorJobId);
    

### CreateFeatureMonitorJobAsync(string, FeatureMonitorJob, long, CancellationToken)
    
    
    public virtual Task<FeatureMonitorJob> CreateFeatureMonitorJobAsync(string parent, FeatureMonitorJob featureMonitorJob, long featureMonitorJobId, CancellationToken cancellationToken)

Creates a new feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of FeatureMonitor to create FeatureMonitorJob. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`featureMonitorJob` | `[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)`  
Required. The Monitor to create.  
`featureMonitorJobId` | `[long](https://learn.microsoft.com/dotnet/api/system.int64)`  
Optional. Output only. System-generated ID for feature monitor job.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]/featureMonitors/[FEATURE_MONITOR]";
    FeatureMonitorJob featureMonitorJob = new FeatureMonitorJob();
    long featureMonitorJobId = 0L;
    // Make the request
    FeatureMonitorJob response = await featureRegistryServiceClient.CreateFeatureMonitorJobAsync(parent, featureMonitorJob, featureMonitorJobId);
    

### DeleteFeature(DeleteFeatureRequest, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteFeature(DeleteFeatureRequest request, CallSettings callSettings = null)

Deletes a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    DeleteFeatureRequest request = new DeleteFeatureRequest
    {
        FeatureName = FeatureName.FromProjectLocationFeaturestoreEntityTypeFeature("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]"),
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = featureRegistryServiceClient.DeleteFeature(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceDeleteFeature(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeature(FeatureName, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteFeature(FeatureName name, CallSettings callSettings = null)

Deletes a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureName)`  
Required. The name of the Features to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    FeatureName name = FeatureName.FromProjectLocationFeaturestoreEntityTypeFeature("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]");
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = featureRegistryServiceClient.DeleteFeature(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceDeleteFeature(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeature(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteFeature(string name, CallSettings callSettings = null)

Deletes a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Features to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featurestores/[FEATURESTORE]/entityTypes/[ENTITY_TYPE]/features/[FEATURE]";
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = featureRegistryServiceClient.DeleteFeature(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceDeleteFeature(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureAsync(DeleteFeatureRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureAsync(DeleteFeatureRequest request, CallSettings callSettings = null)

Deletes a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteFeatureRequest request = new DeleteFeatureRequest
    {
        FeatureName = FeatureName.FromProjectLocationFeaturestoreEntityTypeFeature("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]"),
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureRegistryServiceClient.DeleteFeatureAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceDeleteFeatureAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureAsync(DeleteFeatureRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureAsync(DeleteFeatureRequest request, CancellationToken cancellationToken)

Deletes a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteFeatureRequest request = new DeleteFeatureRequest
    {
        FeatureName = FeatureName.FromProjectLocationFeaturestoreEntityTypeFeature("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]"),
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureRegistryServiceClient.DeleteFeatureAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceDeleteFeatureAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureAsync(FeatureName, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureAsync(FeatureName name, CallSettings callSettings = null)

Deletes a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureName)`  
Required. The name of the Features to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureName name = FeatureName.FromProjectLocationFeaturestoreEntityTypeFeature("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]");
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureRegistryServiceClient.DeleteFeatureAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceDeleteFeatureAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureAsync(FeatureName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureAsync(FeatureName name, CancellationToken cancellationToken)

Deletes a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureName)`  
Required. The name of the Features to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureName name = FeatureName.FromProjectLocationFeaturestoreEntityTypeFeature("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]");
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureRegistryServiceClient.DeleteFeatureAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceDeleteFeatureAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureAsync(string name, CallSettings callSettings = null)

Deletes a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Features to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featurestores/[FEATURESTORE]/entityTypes/[ENTITY_TYPE]/features/[FEATURE]";
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureRegistryServiceClient.DeleteFeatureAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceDeleteFeatureAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureAsync(string name, CancellationToken cancellationToken)

Deletes a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Features to be deleted. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featurestores/[FEATURESTORE]/entityTypes/[ENTITY_TYPE]/features/[FEATURE]";
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureRegistryServiceClient.DeleteFeatureAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceDeleteFeatureAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureGroup(DeleteFeatureGroupRequest, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteFeatureGroup(DeleteFeatureGroupRequest request, CallSettings callSettings = null)

Deletes a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureGroupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    DeleteFeatureGroupRequest request = new DeleteFeatureGroupRequest
    {
        FeatureGroupName = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]"),
        Force = false,
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = featureRegistryServiceClient.DeleteFeatureGroup(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceDeleteFeatureGroup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureGroup(FeatureGroupName, bool, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteFeatureGroup(FeatureGroupName name, bool force, CallSettings callSettings = null)

Deletes a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroupName)`  
Required. The name of the FeatureGroup to be deleted. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`force` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If set to true, any Features under this FeatureGroup will also be deleted. (Otherwise, the request will only work if the FeatureGroup has no Features.)  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    FeatureGroupName name = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
    bool force = false;
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = featureRegistryServiceClient.DeleteFeatureGroup(name, force);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceDeleteFeatureGroup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureGroup(string, bool, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteFeatureGroup(string name, bool force, CallSettings callSettings = null)

Deletes a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureGroup to be deleted. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`force` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If set to true, any Features under this FeatureGroup will also be deleted. (Otherwise, the request will only work if the FeatureGroup has no Features.)  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]";
    bool force = false;
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = featureRegistryServiceClient.DeleteFeatureGroup(name, force);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceDeleteFeatureGroup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureGroupAsync(DeleteFeatureGroupRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureGroupAsync(DeleteFeatureGroupRequest request, CallSettings callSettings = null)

Deletes a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureGroupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteFeatureGroupRequest request = new DeleteFeatureGroupRequest
    {
        FeatureGroupName = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]"),
        Force = false,
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureRegistryServiceClient.DeleteFeatureGroupAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceDeleteFeatureGroupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureGroupAsync(DeleteFeatureGroupRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureGroupAsync(DeleteFeatureGroupRequest request, CancellationToken cancellationToken)

Deletes a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureGroupRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteFeatureGroupRequest request = new DeleteFeatureGroupRequest
    {
        FeatureGroupName = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]"),
        Force = false,
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureRegistryServiceClient.DeleteFeatureGroupAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceDeleteFeatureGroupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureGroupAsync(FeatureGroupName, bool, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureGroupAsync(FeatureGroupName name, bool force, CallSettings callSettings = null)

Deletes a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroupName)`  
Required. The name of the FeatureGroup to be deleted. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`force` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If set to true, any Features under this FeatureGroup will also be deleted. (Otherwise, the request will only work if the FeatureGroup has no Features.)  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureGroupName name = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
    bool force = false;
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureRegistryServiceClient.DeleteFeatureGroupAsync(name, force);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceDeleteFeatureGroupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureGroupAsync(FeatureGroupName, bool, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureGroupAsync(FeatureGroupName name, bool force, CancellationToken cancellationToken)

Deletes a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroupName)`  
Required. The name of the FeatureGroup to be deleted. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`force` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If set to true, any Features under this FeatureGroup will also be deleted. (Otherwise, the request will only work if the FeatureGroup has no Features.)  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureGroupName name = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
    bool force = false;
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureRegistryServiceClient.DeleteFeatureGroupAsync(name, force);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceDeleteFeatureGroupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureGroupAsync(string, bool, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureGroupAsync(string name, bool force, CallSettings callSettings = null)

Deletes a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureGroup to be deleted. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`force` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If set to true, any Features under this FeatureGroup will also be deleted. (Otherwise, the request will only work if the FeatureGroup has no Features.)  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]";
    bool force = false;
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureRegistryServiceClient.DeleteFeatureGroupAsync(name, force);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceDeleteFeatureGroupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureGroupAsync(string, bool, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureGroupAsync(string name, bool force, CancellationToken cancellationToken)

Deletes a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureGroup to be deleted. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`force` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If set to true, any Features under this FeatureGroup will also be deleted. (Otherwise, the request will only work if the FeatureGroup has no Features.)  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]";
    bool force = false;
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureRegistryServiceClient.DeleteFeatureGroupAsync(name, force);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceDeleteFeatureGroupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureMonitor(DeleteFeatureMonitorRequest, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteFeatureMonitor(DeleteFeatureMonitorRequest request, CallSettings callSettings = null)

Deletes a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureMonitorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    DeleteFeatureMonitorRequest request = new DeleteFeatureMonitorRequest
    {
        FeatureMonitorName = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]"),
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = featureRegistryServiceClient.DeleteFeatureMonitor(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceDeleteFeatureMonitor(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureMonitor(FeatureMonitorName, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteFeatureMonitor(FeatureMonitorName name, CallSettings callSettings = null)

Deletes a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureMonitorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorName)`  
Required. The name of the FeatureMonitor to be deleted. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    FeatureMonitorName name = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]");
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = featureRegistryServiceClient.DeleteFeatureMonitor(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceDeleteFeatureMonitor(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureMonitor(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteFeatureMonitor(string name, CallSettings callSettings = null)

Deletes a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureMonitor to be deleted. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]/featureMonitors/[FEATURE_MONITOR]";
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = featureRegistryServiceClient.DeleteFeatureMonitor(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceDeleteFeatureMonitor(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureMonitorAsync(DeleteFeatureMonitorRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureMonitorAsync(DeleteFeatureMonitorRequest request, CallSettings callSettings = null)

Deletes a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureMonitorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteFeatureMonitorRequest request = new DeleteFeatureMonitorRequest
    {
        FeatureMonitorName = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]"),
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureRegistryServiceClient.DeleteFeatureMonitorAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceDeleteFeatureMonitorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureMonitorAsync(DeleteFeatureMonitorRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureMonitorAsync(DeleteFeatureMonitorRequest request, CancellationToken cancellationToken)

Deletes a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteFeatureMonitorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteFeatureMonitorRequest request = new DeleteFeatureMonitorRequest
    {
        FeatureMonitorName = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]"),
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureRegistryServiceClient.DeleteFeatureMonitorAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceDeleteFeatureMonitorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureMonitorAsync(FeatureMonitorName, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureMonitorAsync(FeatureMonitorName name, CallSettings callSettings = null)

Deletes a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureMonitorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorName)`  
Required. The name of the FeatureMonitor to be deleted. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureMonitorName name = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]");
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureRegistryServiceClient.DeleteFeatureMonitorAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceDeleteFeatureMonitorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureMonitorAsync(FeatureMonitorName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureMonitorAsync(FeatureMonitorName name, CancellationToken cancellationToken)

Deletes a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureMonitorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorName)`  
Required. The name of the FeatureMonitor to be deleted. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureMonitorName name = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]");
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureRegistryServiceClient.DeleteFeatureMonitorAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceDeleteFeatureMonitorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureMonitorAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureMonitorAsync(string name, CallSettings callSettings = null)

Deletes a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureMonitor to be deleted. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]/featureMonitors/[FEATURE_MONITOR]";
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureRegistryServiceClient.DeleteFeatureMonitorAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceDeleteFeatureMonitorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureMonitorAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureMonitorAsync(string name, CancellationToken cancellationToken)

Deletes a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureMonitor to be deleted. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]/featureMonitors/[FEATURE_MONITOR]";
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureRegistryServiceClient.DeleteFeatureMonitorAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceDeleteFeatureMonitorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GetFeature(FeatureName, CallSettings)
    
    
    public virtual Feature GetFeature(FeatureName name, CallSettings callSettings = null)

Gets details of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureName)`  
Required. The name of the Feature resource. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    FeatureName name = FeatureName.FromProjectLocationFeaturestoreEntityTypeFeature("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]");
    // Make the request
    Feature response = featureRegistryServiceClient.GetFeature(name);
    

### GetFeature(GetFeatureRequest, CallSettings)
    
    
    public virtual Feature GetFeature(GetFeatureRequest request, CallSettings callSettings = null)

Gets details of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    GetFeatureRequest request = new GetFeatureRequest
    {
        FeatureName = FeatureName.FromProjectLocationFeaturestoreEntityTypeFeature("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]"),
        FeatureStatsAndAnomalySpec = new FeatureStatsAndAnomalySpec(),
    };
    // Make the request
    Feature response = featureRegistryServiceClient.GetFeature(request);
    

### GetFeature(string, CallSettings)
    
    
    public virtual Feature GetFeature(string name, CallSettings callSettings = null)

Gets details of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Feature resource. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featurestores/[FEATURESTORE]/entityTypes/[ENTITY_TYPE]/features/[FEATURE]";
    // Make the request
    Feature response = featureRegistryServiceClient.GetFeature(name);
    

### GetFeatureAsync(FeatureName, CallSettings)
    
    
    public virtual Task<Feature> GetFeatureAsync(FeatureName name, CallSettings callSettings = null)

Gets details of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureName)`  
Required. The name of the Feature resource. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureName name = FeatureName.FromProjectLocationFeaturestoreEntityTypeFeature("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]");
    // Make the request
    Feature response = await featureRegistryServiceClient.GetFeatureAsync(name);
    

### GetFeatureAsync(FeatureName, CancellationToken)
    
    
    public virtual Task<Feature> GetFeatureAsync(FeatureName name, CancellationToken cancellationToken)

Gets details of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureName)`  
Required. The name of the Feature resource. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureName name = FeatureName.FromProjectLocationFeaturestoreEntityTypeFeature("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]");
    // Make the request
    Feature response = await featureRegistryServiceClient.GetFeatureAsync(name);
    

### GetFeatureAsync(GetFeatureRequest, CallSettings)
    
    
    public virtual Task<Feature> GetFeatureAsync(GetFeatureRequest request, CallSettings callSettings = null)

Gets details of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetFeatureRequest request = new GetFeatureRequest
    {
        FeatureName = FeatureName.FromProjectLocationFeaturestoreEntityTypeFeature("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]"),
        FeatureStatsAndAnomalySpec = new FeatureStatsAndAnomalySpec(),
    };
    // Make the request
    Feature response = await featureRegistryServiceClient.GetFeatureAsync(request);
    

### GetFeatureAsync(GetFeatureRequest, CancellationToken)
    
    
    public virtual Task<Feature> GetFeatureAsync(GetFeatureRequest request, CancellationToken cancellationToken)

Gets details of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetFeatureRequest request = new GetFeatureRequest
    {
        FeatureName = FeatureName.FromProjectLocationFeaturestoreEntityTypeFeature("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]", "[FEATURE]"),
        FeatureStatsAndAnomalySpec = new FeatureStatsAndAnomalySpec(),
    };
    // Make the request
    Feature response = await featureRegistryServiceClient.GetFeatureAsync(request);
    

### GetFeatureAsync(string, CallSettings)
    
    
    public virtual Task<Feature> GetFeatureAsync(string name, CallSettings callSettings = null)

Gets details of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Feature resource. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featurestores/[FEATURESTORE]/entityTypes/[ENTITY_TYPE]/features/[FEATURE]";
    // Make the request
    Feature response = await featureRegistryServiceClient.GetFeatureAsync(name);
    

### GetFeatureAsync(string, CancellationToken)
    
    
    public virtual Task<Feature> GetFeatureAsync(string name, CancellationToken cancellationToken)

Gets details of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Feature resource. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featurestores/[FEATURESTORE]/entityTypes/[ENTITY_TYPE]/features/[FEATURE]";
    // Make the request
    Feature response = await featureRegistryServiceClient.GetFeatureAsync(name);
    

### GetFeatureGroup(FeatureGroupName, CallSettings)
    
    
    public virtual FeatureGroup GetFeatureGroup(FeatureGroupName name, CallSettings callSettings = null)

Gets details of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroupName)`  
Required. The name of the FeatureGroup resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    FeatureGroupName name = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
    // Make the request
    FeatureGroup response = featureRegistryServiceClient.GetFeatureGroup(name);
    

### GetFeatureGroup(GetFeatureGroupRequest, CallSettings)
    
    
    public virtual FeatureGroup GetFeatureGroup(GetFeatureGroupRequest request, CallSettings callSettings = null)

Gets details of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureGroupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    GetFeatureGroupRequest request = new GetFeatureGroupRequest
    {
        FeatureGroupName = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]"),
    };
    // Make the request
    FeatureGroup response = featureRegistryServiceClient.GetFeatureGroup(request);
    

### GetFeatureGroup(string, CallSettings)
    
    
    public virtual FeatureGroup GetFeatureGroup(string name, CallSettings callSettings = null)

Gets details of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureGroup resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]";
    // Make the request
    FeatureGroup response = featureRegistryServiceClient.GetFeatureGroup(name);
    

### GetFeatureGroupAsync(FeatureGroupName, CallSettings)
    
    
    public virtual Task<FeatureGroup> GetFeatureGroupAsync(FeatureGroupName name, CallSettings callSettings = null)

Gets details of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroupName)`  
Required. The name of the FeatureGroup resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureGroupName name = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
    // Make the request
    FeatureGroup response = await featureRegistryServiceClient.GetFeatureGroupAsync(name);
    

### GetFeatureGroupAsync(FeatureGroupName, CancellationToken)
    
    
    public virtual Task<FeatureGroup> GetFeatureGroupAsync(FeatureGroupName name, CancellationToken cancellationToken)

Gets details of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroupName)`  
Required. The name of the FeatureGroup resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureGroupName name = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
    // Make the request
    FeatureGroup response = await featureRegistryServiceClient.GetFeatureGroupAsync(name);
    

### GetFeatureGroupAsync(GetFeatureGroupRequest, CallSettings)
    
    
    public virtual Task<FeatureGroup> GetFeatureGroupAsync(GetFeatureGroupRequest request, CallSettings callSettings = null)

Gets details of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureGroupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetFeatureGroupRequest request = new GetFeatureGroupRequest
    {
        FeatureGroupName = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]"),
    };
    // Make the request
    FeatureGroup response = await featureRegistryServiceClient.GetFeatureGroupAsync(request);
    

### GetFeatureGroupAsync(GetFeatureGroupRequest, CancellationToken)
    
    
    public virtual Task<FeatureGroup> GetFeatureGroupAsync(GetFeatureGroupRequest request, CancellationToken cancellationToken)

Gets details of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureGroupRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetFeatureGroupRequest request = new GetFeatureGroupRequest
    {
        FeatureGroupName = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]"),
    };
    // Make the request
    FeatureGroup response = await featureRegistryServiceClient.GetFeatureGroupAsync(request);
    

### GetFeatureGroupAsync(string, CallSettings)
    
    
    public virtual Task<FeatureGroup> GetFeatureGroupAsync(string name, CallSettings callSettings = null)

Gets details of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureGroup resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]";
    // Make the request
    FeatureGroup response = await featureRegistryServiceClient.GetFeatureGroupAsync(name);
    

### GetFeatureGroupAsync(string, CancellationToken)
    
    
    public virtual Task<FeatureGroup> GetFeatureGroupAsync(string name, CancellationToken cancellationToken)

Gets details of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureGroup resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]";
    // Make the request
    FeatureGroup response = await featureRegistryServiceClient.GetFeatureGroupAsync(name);
    

### GetFeatureMonitor(FeatureMonitorName, CallSettings)
    
    
    public virtual FeatureMonitor GetFeatureMonitor(FeatureMonitorName name, CallSettings callSettings = null)

Gets details of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureMonitorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorName)`  
Required. The name of the FeatureMonitor resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    FeatureMonitorName name = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]");
    // Make the request
    FeatureMonitor response = featureRegistryServiceClient.GetFeatureMonitor(name);
    

### GetFeatureMonitor(GetFeatureMonitorRequest, CallSettings)
    
    
    public virtual FeatureMonitor GetFeatureMonitor(GetFeatureMonitorRequest request, CallSettings callSettings = null)

Gets details of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureMonitorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    GetFeatureMonitorRequest request = new GetFeatureMonitorRequest
    {
        FeatureMonitorName = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]"),
    };
    // Make the request
    FeatureMonitor response = featureRegistryServiceClient.GetFeatureMonitor(request);
    

### GetFeatureMonitor(string, CallSettings)
    
    
    public virtual FeatureMonitor GetFeatureMonitor(string name, CallSettings callSettings = null)

Gets details of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureMonitor resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]/featureMonitors/[FEATURE_MONITOR]";
    // Make the request
    FeatureMonitor response = featureRegistryServiceClient.GetFeatureMonitor(name);
    

### GetFeatureMonitorAsync(FeatureMonitorName, CallSettings)
    
    
    public virtual Task<FeatureMonitor> GetFeatureMonitorAsync(FeatureMonitorName name, CallSettings callSettings = null)

Gets details of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureMonitorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorName)`  
Required. The name of the FeatureMonitor resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureMonitorName name = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]");
    // Make the request
    FeatureMonitor response = await featureRegistryServiceClient.GetFeatureMonitorAsync(name);
    

### GetFeatureMonitorAsync(FeatureMonitorName, CancellationToken)
    
    
    public virtual Task<FeatureMonitor> GetFeatureMonitorAsync(FeatureMonitorName name, CancellationToken cancellationToken)

Gets details of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureMonitorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorName)`  
Required. The name of the FeatureMonitor resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureMonitorName name = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]");
    // Make the request
    FeatureMonitor response = await featureRegistryServiceClient.GetFeatureMonitorAsync(name);
    

### GetFeatureMonitorAsync(GetFeatureMonitorRequest, CallSettings)
    
    
    public virtual Task<FeatureMonitor> GetFeatureMonitorAsync(GetFeatureMonitorRequest request, CallSettings callSettings = null)

Gets details of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureMonitorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetFeatureMonitorRequest request = new GetFeatureMonitorRequest
    {
        FeatureMonitorName = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]"),
    };
    // Make the request
    FeatureMonitor response = await featureRegistryServiceClient.GetFeatureMonitorAsync(request);
    

### GetFeatureMonitorAsync(GetFeatureMonitorRequest, CancellationToken)
    
    
    public virtual Task<FeatureMonitor> GetFeatureMonitorAsync(GetFeatureMonitorRequest request, CancellationToken cancellationToken)

Gets details of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureMonitorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetFeatureMonitorRequest request = new GetFeatureMonitorRequest
    {
        FeatureMonitorName = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]"),
    };
    // Make the request
    FeatureMonitor response = await featureRegistryServiceClient.GetFeatureMonitorAsync(request);
    

### GetFeatureMonitorAsync(string, CallSettings)
    
    
    public virtual Task<FeatureMonitor> GetFeatureMonitorAsync(string name, CallSettings callSettings = null)

Gets details of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureMonitor resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]/featureMonitors/[FEATURE_MONITOR]";
    // Make the request
    FeatureMonitor response = await featureRegistryServiceClient.GetFeatureMonitorAsync(name);
    

### GetFeatureMonitorAsync(string, CancellationToken)
    
    
    public virtual Task<FeatureMonitor> GetFeatureMonitorAsync(string name, CancellationToken cancellationToken)

Gets details of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureMonitor resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]/featureMonitors/[FEATURE_MONITOR]";
    // Make the request
    FeatureMonitor response = await featureRegistryServiceClient.GetFeatureMonitorAsync(name);
    

### GetFeatureMonitorJob(FeatureMonitorJobName, CallSettings)
    
    
    public virtual FeatureMonitorJob GetFeatureMonitorJob(FeatureMonitorJobName name, CallSettings callSettings = null)

Get a feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureMonitorJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJobName)`  
Required. The name of the FeatureMonitorJob resource. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}/featureMonitorJobs/{feature_monitor_job}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    FeatureMonitorJobName name = FeatureMonitorJobName.FromProjectLocationFeatureGroupFeatureMonitorFeatureMonitorJob("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]", "[FEATURE_MONITOR_JOB]");
    // Make the request
    FeatureMonitorJob response = featureRegistryServiceClient.GetFeatureMonitorJob(name);
    

### GetFeatureMonitorJob(GetFeatureMonitorJobRequest, CallSettings)
    
    
    public virtual FeatureMonitorJob GetFeatureMonitorJob(GetFeatureMonitorJobRequest request, CallSettings callSettings = null)

Get a feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureMonitorJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureMonitorJobRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    GetFeatureMonitorJobRequest request = new GetFeatureMonitorJobRequest
    {
        FeatureMonitorJobName = FeatureMonitorJobName.FromProjectLocationFeatureGroupFeatureMonitorFeatureMonitorJob("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]", "[FEATURE_MONITOR_JOB]"),
    };
    // Make the request
    FeatureMonitorJob response = featureRegistryServiceClient.GetFeatureMonitorJob(request);
    

### GetFeatureMonitorJob(string, CallSettings)
    
    
    public virtual FeatureMonitorJob GetFeatureMonitorJob(string name, CallSettings callSettings = null)

Get a feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureMonitorJob resource. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}/featureMonitorJobs/{feature_monitor_job}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]/featureMonitors/[FEATURE_MONITOR]/featureMonitorJobs/[FEATURE_MONITOR_JOB]";
    // Make the request
    FeatureMonitorJob response = featureRegistryServiceClient.GetFeatureMonitorJob(name);
    

### GetFeatureMonitorJobAsync(FeatureMonitorJobName, CallSettings)
    
    
    public virtual Task<FeatureMonitorJob> GetFeatureMonitorJobAsync(FeatureMonitorJobName name, CallSettings callSettings = null)

Get a feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureMonitorJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJobName)`  
Required. The name of the FeatureMonitorJob resource. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}/featureMonitorJobs/{feature_monitor_job}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureMonitorJobName name = FeatureMonitorJobName.FromProjectLocationFeatureGroupFeatureMonitorFeatureMonitorJob("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]", "[FEATURE_MONITOR_JOB]");
    // Make the request
    FeatureMonitorJob response = await featureRegistryServiceClient.GetFeatureMonitorJobAsync(name);
    

### GetFeatureMonitorJobAsync(FeatureMonitorJobName, CancellationToken)
    
    
    public virtual Task<FeatureMonitorJob> GetFeatureMonitorJobAsync(FeatureMonitorJobName name, CancellationToken cancellationToken)

Get a feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureMonitorJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJobName)`  
Required. The name of the FeatureMonitorJob resource. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}/featureMonitorJobs/{feature_monitor_job}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureMonitorJobName name = FeatureMonitorJobName.FromProjectLocationFeatureGroupFeatureMonitorFeatureMonitorJob("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]", "[FEATURE_MONITOR_JOB]");
    // Make the request
    FeatureMonitorJob response = await featureRegistryServiceClient.GetFeatureMonitorJobAsync(name);
    

### GetFeatureMonitorJobAsync(GetFeatureMonitorJobRequest, CallSettings)
    
    
    public virtual Task<FeatureMonitorJob> GetFeatureMonitorJobAsync(GetFeatureMonitorJobRequest request, CallSettings callSettings = null)

Get a feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureMonitorJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureMonitorJobRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetFeatureMonitorJobRequest request = new GetFeatureMonitorJobRequest
    {
        FeatureMonitorJobName = FeatureMonitorJobName.FromProjectLocationFeatureGroupFeatureMonitorFeatureMonitorJob("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]", "[FEATURE_MONITOR_JOB]"),
    };
    // Make the request
    FeatureMonitorJob response = await featureRegistryServiceClient.GetFeatureMonitorJobAsync(request);
    

### GetFeatureMonitorJobAsync(GetFeatureMonitorJobRequest, CancellationToken)
    
    
    public virtual Task<FeatureMonitorJob> GetFeatureMonitorJobAsync(GetFeatureMonitorJobRequest request, CancellationToken cancellationToken)

Get a feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureMonitorJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetFeatureMonitorJobRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetFeatureMonitorJobRequest request = new GetFeatureMonitorJobRequest
    {
        FeatureMonitorJobName = FeatureMonitorJobName.FromProjectLocationFeatureGroupFeatureMonitorFeatureMonitorJob("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]", "[FEATURE_MONITOR_JOB]"),
    };
    // Make the request
    FeatureMonitorJob response = await featureRegistryServiceClient.GetFeatureMonitorJobAsync(request);
    

### GetFeatureMonitorJobAsync(string, CallSettings)
    
    
    public virtual Task<FeatureMonitorJob> GetFeatureMonitorJobAsync(string name, CallSettings callSettings = null)

Get a feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureMonitorJob resource. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}/featureMonitorJobs/{feature_monitor_job}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]/featureMonitors/[FEATURE_MONITOR]/featureMonitorJobs/[FEATURE_MONITOR_JOB]";
    // Make the request
    FeatureMonitorJob response = await featureRegistryServiceClient.GetFeatureMonitorJobAsync(name);
    

### GetFeatureMonitorJobAsync(string, CancellationToken)
    
    
    public virtual Task<FeatureMonitorJob> GetFeatureMonitorJobAsync(string name, CancellationToken cancellationToken)

Get a feature monitor job.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureMonitorJob resource. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}/featureMonitorJobs/{feature_monitor_job}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]/featureMonitors/[FEATURE_MONITOR]/featureMonitorJobs/[FEATURE_MONITOR_JOB]";
    // Make the request
    FeatureMonitorJob response = await featureRegistryServiceClient.GetFeatureMonitorJobAsync(name);
    

### ListFeatureGroups(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeatureGroupsResponse, FeatureGroup> ListFeatureGroups(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the Location to list FeatureGroups. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeatureGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureGroupsResponse)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)` | A pageable sequence of [FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListFeatureGroupsResponse, FeatureGroup> response = featureRegistryServiceClient.ListFeatureGroups(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FeatureGroup item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeatureGroupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureGroup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureGroup> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureGroup item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureGroups(ListFeatureGroupsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeatureGroupsResponse, FeatureGroup> ListFeatureGroups(ListFeatureGroupsRequest request, CallSettings callSettings = null)

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureGroupsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeatureGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureGroupsResponse)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)` | A pageable sequence of [FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    ListFeatureGroupsRequest request = new ListFeatureGroupsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListFeatureGroupsResponse, FeatureGroup> response = featureRegistryServiceClient.ListFeatureGroups(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FeatureGroup item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeatureGroupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureGroup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureGroup> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureGroup item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureGroups(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeatureGroupsResponse, FeatureGroup> ListFeatureGroups(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to list FeatureGroups. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeatureGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureGroupsResponse)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)` | A pageable sequence of [FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListFeatureGroupsResponse, FeatureGroup> response = featureRegistryServiceClient.ListFeatureGroups(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FeatureGroup item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeatureGroupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureGroup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureGroup> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureGroup item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureGroupsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeatureGroupsResponse, FeatureGroup> ListFeatureGroupsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the Location to list FeatureGroups. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeatureGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureGroupsResponse)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)` | A pageable asynchronous sequence of [FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListFeatureGroupsResponse, FeatureGroup> response = featureRegistryServiceClient.ListFeatureGroupsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FeatureGroup item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeatureGroupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureGroup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureGroup> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureGroup item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureGroupsAsync(ListFeatureGroupsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeatureGroupsResponse, FeatureGroup> ListFeatureGroupsAsync(ListFeatureGroupsRequest request, CallSettings callSettings = null)

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureGroupsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeatureGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureGroupsResponse)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)` | A pageable asynchronous sequence of [FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListFeatureGroupsRequest request = new ListFeatureGroupsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListFeatureGroupsResponse, FeatureGroup> response = featureRegistryServiceClient.ListFeatureGroupsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FeatureGroup item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeatureGroupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureGroup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureGroup> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureGroup item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureGroupsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeatureGroupsResponse, FeatureGroup> ListFeatureGroupsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to list FeatureGroups. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeatureGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureGroupsResponse)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)` | A pageable asynchronous sequence of [FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListFeatureGroupsResponse, FeatureGroup> response = featureRegistryServiceClient.ListFeatureGroupsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FeatureGroup item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeatureGroupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureGroup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureGroup> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureGroup item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureMonitorJobs(FeatureMonitorName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeatureMonitorJobsResponse, FeatureMonitorJob> ListFeatureMonitorJobs(FeatureMonitorName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List feature monitor jobs.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureMonitorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorName)`  
Required. The resource name of the FeatureMonitor to list FeatureMonitorJobs. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeatureMonitorJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorJobsResponse)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | A pageable sequence of [FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    FeatureMonitorName parent = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]");
    // Make the request
    PagedEnumerable<ListFeatureMonitorJobsResponse, FeatureMonitorJob> response = featureRegistryServiceClient.ListFeatureMonitorJobs(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FeatureMonitorJob item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeatureMonitorJobsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureMonitorJob item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureMonitorJob> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureMonitorJob item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureMonitorJobs(ListFeatureMonitorJobsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeatureMonitorJobsResponse, FeatureMonitorJob> ListFeatureMonitorJobs(ListFeatureMonitorJobsRequest request, CallSettings callSettings = null)

List feature monitor jobs.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureMonitorJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorJobsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeatureMonitorJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorJobsResponse)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | A pageable sequence of [FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    ListFeatureMonitorJobsRequest request = new ListFeatureMonitorJobsRequest
    {
        ParentAsFeatureMonitorName = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListFeatureMonitorJobsResponse, FeatureMonitorJob> response = featureRegistryServiceClient.ListFeatureMonitorJobs(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FeatureMonitorJob item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeatureMonitorJobsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureMonitorJob item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureMonitorJob> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureMonitorJob item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureMonitorJobs(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeatureMonitorJobsResponse, FeatureMonitorJob> ListFeatureMonitorJobs(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List feature monitor jobs.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the FeatureMonitor to list FeatureMonitorJobs. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeatureMonitorJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorJobsResponse)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | A pageable sequence of [FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]/featureMonitors/[FEATURE_MONITOR]";
    // Make the request
    PagedEnumerable<ListFeatureMonitorJobsResponse, FeatureMonitorJob> response = featureRegistryServiceClient.ListFeatureMonitorJobs(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FeatureMonitorJob item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeatureMonitorJobsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureMonitorJob item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureMonitorJob> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureMonitorJob item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureMonitorJobsAsync(FeatureMonitorName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeatureMonitorJobsResponse, FeatureMonitorJob> ListFeatureMonitorJobsAsync(FeatureMonitorName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List feature monitor jobs.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureMonitorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorName)`  
Required. The resource name of the FeatureMonitor to list FeatureMonitorJobs. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeatureMonitorJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorJobsResponse)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | A pageable asynchronous sequence of [FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureMonitorName parent = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]");
    // Make the request
    PagedAsyncEnumerable<ListFeatureMonitorJobsResponse, FeatureMonitorJob> response = featureRegistryServiceClient.ListFeatureMonitorJobsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FeatureMonitorJob item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeatureMonitorJobsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureMonitorJob item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureMonitorJob> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureMonitorJob item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureMonitorJobsAsync(ListFeatureMonitorJobsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeatureMonitorJobsResponse, FeatureMonitorJob> ListFeatureMonitorJobsAsync(ListFeatureMonitorJobsRequest request, CallSettings callSettings = null)

List feature monitor jobs.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureMonitorJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorJobsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeatureMonitorJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorJobsResponse)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | A pageable asynchronous sequence of [FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListFeatureMonitorJobsRequest request = new ListFeatureMonitorJobsRequest
    {
        ParentAsFeatureMonitorName = FeatureMonitorName.FromProjectLocationFeatureGroupFeatureMonitor("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]", "[FEATURE_MONITOR]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListFeatureMonitorJobsResponse, FeatureMonitorJob> response = featureRegistryServiceClient.ListFeatureMonitorJobsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FeatureMonitorJob item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeatureMonitorJobsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureMonitorJob item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureMonitorJob> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureMonitorJob item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureMonitorJobsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeatureMonitorJobsResponse, FeatureMonitorJob> ListFeatureMonitorJobsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

List feature monitor jobs.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the FeatureMonitor to list FeatureMonitorJobs. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeatureMonitorJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorJobsResponse)[FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob)` | A pageable asynchronous sequence of [FeatureMonitorJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitorJob) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]/featureMonitors/[FEATURE_MONITOR]";
    // Make the request
    PagedAsyncEnumerable<ListFeatureMonitorJobsResponse, FeatureMonitorJob> response = featureRegistryServiceClient.ListFeatureMonitorJobsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FeatureMonitorJob item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeatureMonitorJobsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureMonitorJob item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureMonitorJob> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureMonitorJob item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureMonitors(FeatureGroupName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeatureMonitorsResponse, FeatureMonitor> ListFeatureMonitors(FeatureGroupName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroupName)`  
Required. The resource name of the FeatureGroup to list FeatureMonitors. Format: `projects/{project}/locations/{location}/featureGroups/{featureGroup}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeatureMonitorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorsResponse)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)` | A pageable sequence of [FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    FeatureGroupName parent = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
    // Make the request
    PagedEnumerable<ListFeatureMonitorsResponse, FeatureMonitor> response = featureRegistryServiceClient.ListFeatureMonitors(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FeatureMonitor item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeatureMonitorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureMonitor item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureMonitor> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureMonitor item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureMonitors(ListFeatureMonitorsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeatureMonitorsResponse, FeatureMonitor> ListFeatureMonitors(ListFeatureMonitorsRequest request, CallSettings callSettings = null)

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureMonitorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeatureMonitorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorsResponse)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)` | A pageable sequence of [FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    ListFeatureMonitorsRequest request = new ListFeatureMonitorsRequest
    {
        ParentAsFeatureGroupName = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListFeatureMonitorsResponse, FeatureMonitor> response = featureRegistryServiceClient.ListFeatureMonitors(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FeatureMonitor item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeatureMonitorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureMonitor item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureMonitor> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureMonitor item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureMonitors(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeatureMonitorsResponse, FeatureMonitor> ListFeatureMonitors(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the FeatureGroup to list FeatureMonitors. Format: `projects/{project}/locations/{location}/featureGroups/{featureGroup}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeatureMonitorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorsResponse)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)` | A pageable sequence of [FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]";
    // Make the request
    PagedEnumerable<ListFeatureMonitorsResponse, FeatureMonitor> response = featureRegistryServiceClient.ListFeatureMonitors(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FeatureMonitor item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeatureMonitorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureMonitor item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureMonitor> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureMonitor item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureMonitorsAsync(FeatureGroupName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeatureMonitorsResponse, FeatureMonitor> ListFeatureMonitorsAsync(FeatureGroupName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroupName)`  
Required. The resource name of the FeatureGroup to list FeatureMonitors. Format: `projects/{project}/locations/{location}/featureGroups/{featureGroup}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeatureMonitorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorsResponse)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)` | A pageable asynchronous sequence of [FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureGroupName parent = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
    // Make the request
    PagedAsyncEnumerable<ListFeatureMonitorsResponse, FeatureMonitor> response = featureRegistryServiceClient.ListFeatureMonitorsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FeatureMonitor item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeatureMonitorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureMonitor item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureMonitor> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureMonitor item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureMonitorsAsync(ListFeatureMonitorsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeatureMonitorsResponse, FeatureMonitor> ListFeatureMonitorsAsync(ListFeatureMonitorsRequest request, CallSettings callSettings = null)

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureMonitorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeatureMonitorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorsResponse)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)` | A pageable asynchronous sequence of [FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListFeatureMonitorsRequest request = new ListFeatureMonitorsRequest
    {
        ParentAsFeatureGroupName = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListFeatureMonitorsResponse, FeatureMonitor> response = featureRegistryServiceClient.ListFeatureMonitorsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FeatureMonitor item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeatureMonitorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureMonitor item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureMonitor> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureMonitor item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureMonitorsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeatureMonitorsResponse, FeatureMonitor> ListFeatureMonitorsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FeatureGroups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the FeatureGroup to list FeatureMonitors. Format: `projects/{project}/locations/{location}/featureGroups/{featureGroup}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeatureMonitorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeatureMonitorsResponse)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)` | A pageable asynchronous sequence of [FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featureGroups/[FEATURE_GROUP]";
    // Make the request
    PagedAsyncEnumerable<ListFeatureMonitorsResponse, FeatureMonitor> response = featureRegistryServiceClient.ListFeatureMonitorsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FeatureMonitor item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeatureMonitorsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureMonitor item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureMonitor> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureMonitor item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatures(EntityTypeName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeaturesResponse, Feature> ListFeatures(EntityTypeName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.EntityTypeName)`  
Required. The resource name of the Location to list Features. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturesResponse)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | A pageable sequence of [Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    EntityTypeName parent = EntityTypeName.FromProjectLocationFeaturestoreEntityType("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
    // Make the request
    PagedEnumerable<ListFeaturesResponse, Feature> response = featureRegistryServiceClient.ListFeatures(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Feature item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeaturesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Feature item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Feature> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Feature item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatures(FeatureGroupName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeaturesResponse, Feature> ListFeatures(FeatureGroupName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroupName)`  
Required. The resource name of the Location to list Features. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturesResponse)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | A pageable sequence of [Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    FeatureGroupName parent = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
    // Make the request
    PagedEnumerable<ListFeaturesResponse, Feature> response = featureRegistryServiceClient.ListFeatures(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Feature item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeaturesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Feature item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Feature> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Feature item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatures(ListFeaturesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeaturesResponse, Feature> ListFeatures(ListFeaturesRequest request, CallSettings callSettings = null)

Lists Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeaturesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturesResponse)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | A pageable sequence of [Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    ListFeaturesRequest request = new ListFeaturesRequest
    {
        ParentAsEntityTypeName = EntityTypeName.FromProjectLocationFeaturestoreEntityType("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]"),
        Filter = "",
        OrderBy = "",
        ReadMask = new FieldMask(),
        LatestStatsCount = 0,
    };
    // Make the request
    PagedEnumerable<ListFeaturesResponse, Feature> response = featureRegistryServiceClient.ListFeatures(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Feature item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeaturesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Feature item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Feature> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Feature item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatures(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeaturesResponse, Feature> ListFeatures(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to list Features. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturesResponse)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | A pageable sequence of [Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featurestores/[FEATURESTORE]/entityTypes/[ENTITY_TYPE]";
    // Make the request
    PagedEnumerable<ListFeaturesResponse, Feature> response = featureRegistryServiceClient.ListFeatures(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Feature item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeaturesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Feature item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Feature> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Feature item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeaturesAsync(EntityTypeName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeaturesResponse, Feature> ListFeaturesAsync(EntityTypeName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[EntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.EntityTypeName)`  
Required. The resource name of the Location to list Features. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturesResponse)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | A pageable asynchronous sequence of [Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    EntityTypeName parent = EntityTypeName.FromProjectLocationFeaturestoreEntityType("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]");
    // Make the request
    PagedAsyncEnumerable<ListFeaturesResponse, Feature> response = featureRegistryServiceClient.ListFeaturesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Feature item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeaturesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Feature item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Feature> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Feature item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeaturesAsync(FeatureGroupName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeaturesResponse, Feature> ListFeaturesAsync(FeatureGroupName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroupName)`  
Required. The resource name of the Location to list Features. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturesResponse)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | A pageable asynchronous sequence of [Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureGroupName parent = FeatureGroupName.FromProjectLocationFeatureGroup("[PROJECT]", "[LOCATION]", "[FEATURE_GROUP]");
    // Make the request
    PagedAsyncEnumerable<ListFeaturesResponse, Feature> response = featureRegistryServiceClient.ListFeaturesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Feature item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeaturesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Feature item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Feature> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Feature item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeaturesAsync(ListFeaturesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeaturesResponse, Feature> ListFeaturesAsync(ListFeaturesRequest request, CallSettings callSettings = null)

Lists Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeaturesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturesResponse)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | A pageable asynchronous sequence of [Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListFeaturesRequest request = new ListFeaturesRequest
    {
        ParentAsEntityTypeName = EntityTypeName.FromProjectLocationFeaturestoreEntityType("[PROJECT]", "[LOCATION]", "[FEATURESTORE]", "[ENTITY_TYPE]"),
        Filter = "",
        OrderBy = "",
        ReadMask = new FieldMask(),
        LatestStatsCount = 0,
    };
    // Make the request
    PagedAsyncEnumerable<ListFeaturesResponse, Feature> response = featureRegistryServiceClient.ListFeaturesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Feature item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeaturesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Feature item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Feature> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Feature item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeaturesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeaturesResponse, Feature> ListFeaturesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Features in a given FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to list Features. Format for entity_type as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` Format for feature_group as parent: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListFeaturesResponse)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)` | A pageable asynchronous sequence of [Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature) resources.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featurestores/[FEATURESTORE]/entityTypes/[ENTITY_TYPE]";
    // Make the request
    PagedAsyncEnumerable<ListFeaturesResponse, Feature> response = featureRegistryServiceClient.ListFeaturesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Feature item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeaturesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Feature item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Feature> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Feature item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceBatchCreateFeatures(string, CallSettings)
    
    
    public virtual Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata> PollOnceBatchCreateFeatures(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `BatchCreateFeatures` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesResponse)[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesOperationMetadata)` | The result of polling the operation.  
  
### PollOnceBatchCreateFeaturesAsync(string, CallSettings)
    
    
    public virtual Task<Operation<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata>> PollOnceBatchCreateFeaturesAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `BatchCreateFeatures`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchCreateFeaturesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesResponse)[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchCreateFeaturesOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateFeature(string, CallSettings)
    
    
    public virtual Operation<Feature, CreateFeatureOperationMetadata> PollOnceCreateFeature(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateFeature`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[CreateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureOperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateFeatureAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Feature, CreateFeatureOperationMetadata>> PollOnceCreateFeatureAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateFeature`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[CreateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateFeatureGroup(string, CallSettings)
    
    
    public virtual Operation<FeatureGroup, CreateFeatureGroupOperationMetadata> PollOnceCreateFeatureGroup(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateFeatureGroup` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)[CreateFeatureGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureGroupOperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateFeatureGroupAsync(string, CallSettings)
    
    
    public virtual Task<Operation<FeatureGroup, CreateFeatureGroupOperationMetadata>> PollOnceCreateFeatureGroupAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateFeatureGroup`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)[CreateFeatureGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureGroupOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateFeatureMonitor(string, CallSettings)
    
    
    public virtual Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata> PollOnceCreateFeatureMonitor(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateFeatureMonitor` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)[CreateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorOperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateFeatureMonitorAsync(string, CallSettings)
    
    
    public virtual Task<Operation<FeatureMonitor, CreateFeatureMonitorOperationMetadata>> PollOnceCreateFeatureMonitorAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateFeatureMonitor`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)[CreateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateFeatureMonitorOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteFeature(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> PollOnceDeleteFeature(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteFeature`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteFeatureAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> PollOnceDeleteFeatureAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteFeature`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteFeatureGroup(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> PollOnceDeleteFeatureGroup(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteFeatureGroup` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteFeatureGroupAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> PollOnceDeleteFeatureGroupAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteFeatureGroup`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteFeatureMonitor(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> PollOnceDeleteFeatureMonitor(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteFeatureMonitor` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteFeatureMonitorAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> PollOnceDeleteFeatureMonitorAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteFeatureMonitor`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateFeature(string, CallSettings)
    
    
    public virtual Operation<Feature, UpdateFeatureOperationMetadata> PollOnceUpdateFeature(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateFeature`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[UpdateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureOperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateFeatureAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Feature, UpdateFeatureOperationMetadata>> PollOnceUpdateFeatureAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateFeature`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[UpdateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateFeatureGroup(string, CallSettings)
    
    
    public virtual Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> PollOnceUpdateFeatureGroup(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateFeatureGroup` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)[UpdateFeatureGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureGroupOperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateFeatureGroupAsync(string, CallSettings)
    
    
    public virtual Task<Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata>> PollOnceUpdateFeatureGroupAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateFeatureGroup`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)[UpdateFeatureGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureGroupOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateFeatureMonitor(string, CallSettings)
    
    
    public virtual Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> PollOnceUpdateFeatureMonitor(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateFeatureMonitor` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)[UpdateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureMonitorOperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateFeatureMonitorAsync(string, CallSettings)
    
    
    public virtual Task<Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata>> PollOnceUpdateFeatureMonitorAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateFeatureMonitor`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)[UpdateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureMonitorOperationMetadata)` | A task representing the result of polling the operation.  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryServiceClient#Google_Cloud_AIPlatform_V1Beta1_FeatureRegistryServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryServiceClient#Google_Cloud_AIPlatform_V1Beta1_FeatureRegistryServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryServiceClient#Google_Cloud_AIPlatform_V1Beta1_FeatureRegistryServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryServiceClient#Google_Cloud_AIPlatform_V1Beta1_FeatureRegistryServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateFeature(Feature, FieldMask, CallSettings)
    
    
    public virtual Operation<Feature, UpdateFeatureOperationMetadata> UpdateFeature(Feature feature, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`feature` | `[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)`  
Required. The Feature's `name` field is used to identify the Feature to be updated. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Features resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields:

  * `description`
  * `labels`
  * `disable_monitoring` (Not supported for FeatureRegistryService Feature)
  * `point_of_contact` (Not supported for FeaturestoreService FeatureStore)

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[UpdateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    Feature feature = new Feature();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Feature, UpdateFeatureOperationMetadata> response = featureRegistryServiceClient.UpdateFeature(feature, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Feature, UpdateFeatureOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Feature result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Feature, UpdateFeatureOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceUpdateFeature(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Feature retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeature(UpdateFeatureRequest, CallSettings)
    
    
    public virtual Operation<Feature, UpdateFeatureOperationMetadata> UpdateFeature(UpdateFeatureRequest request, CallSettings callSettings = null)

Updates the parameters of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[UpdateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    UpdateFeatureRequest request = new UpdateFeatureRequest
    {
        Feature = new Feature(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<Feature, UpdateFeatureOperationMetadata> response = featureRegistryServiceClient.UpdateFeature(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Feature, UpdateFeatureOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Feature result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Feature, UpdateFeatureOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceUpdateFeature(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Feature retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureAsync(Feature, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Feature, UpdateFeatureOperationMetadata>> UpdateFeatureAsync(Feature feature, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`feature` | `[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)`  
Required. The Feature's `name` field is used to identify the Feature to be updated. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Features resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields:

  * `description`
  * `labels`
  * `disable_monitoring` (Not supported for FeatureRegistryService Feature)
  * `point_of_contact` (Not supported for FeaturestoreService FeatureStore)

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[UpdateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    Feature feature = new Feature();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Feature, UpdateFeatureOperationMetadata> response = await featureRegistryServiceClient.UpdateFeatureAsync(feature, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Feature, UpdateFeatureOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Feature result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Feature, UpdateFeatureOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceUpdateFeatureAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Feature retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureAsync(Feature, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Feature, UpdateFeatureOperationMetadata>> UpdateFeatureAsync(Feature feature, FieldMask updateMask, CancellationToken cancellationToken)

Updates the parameters of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`feature` | `[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)`  
Required. The Feature's `name` field is used to identify the Feature to be updated. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the Features resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields:

  * `description`
  * `labels`
  * `disable_monitoring` (Not supported for FeatureRegistryService Feature)
  * `point_of_contact` (Not supported for FeaturestoreService FeatureStore)

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[UpdateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    Feature feature = new Feature();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Feature, UpdateFeatureOperationMetadata> response = await featureRegistryServiceClient.UpdateFeatureAsync(feature, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Feature, UpdateFeatureOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Feature result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Feature, UpdateFeatureOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceUpdateFeatureAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Feature retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureAsync(UpdateFeatureRequest, CallSettings)
    
    
    public virtual Task<Operation<Feature, UpdateFeatureOperationMetadata>> UpdateFeatureAsync(UpdateFeatureRequest request, CallSettings callSettings = null)

Updates the parameters of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[UpdateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateFeatureRequest request = new UpdateFeatureRequest
    {
        Feature = new Feature(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<Feature, UpdateFeatureOperationMetadata> response = await featureRegistryServiceClient.UpdateFeatureAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Feature, UpdateFeatureOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Feature result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Feature, UpdateFeatureOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceUpdateFeatureAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Feature retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureAsync(UpdateFeatureRequest, CancellationToken)
    
    
    public virtual Task<Operation<Feature, UpdateFeatureOperationMetadata>> UpdateFeatureAsync(UpdateFeatureRequest request, CancellationToken cancellationToken)

Updates the parameters of a single Feature.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Feature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Feature)[UpdateFeatureOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateFeatureRequest request = new UpdateFeatureRequest
    {
        Feature = new Feature(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<Feature, UpdateFeatureOperationMetadata> response = await featureRegistryServiceClient.UpdateFeatureAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Feature, UpdateFeatureOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Feature result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Feature, UpdateFeatureOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceUpdateFeatureAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Feature retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureGroup(FeatureGroup, FieldMask, CallSettings)
    
    
    public virtual Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> UpdateFeatureGroup(FeatureGroup featureGroup, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`featureGroup` | `[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)`  
Required. The FeatureGroup's `name` field is used to identify the FeatureGroup to be updated. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the FeatureGroup resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields:

  * `labels`
  * `description`
  * `big_query`
  * `big_query.entity_id_columns`

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)[UpdateFeatureGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureGroupOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    FeatureGroup featureGroup = new FeatureGroup();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> response = featureRegistryServiceClient.UpdateFeatureGroup(featureGroup, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FeatureGroup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceUpdateFeatureGroup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureGroup retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureGroup(UpdateFeatureGroupRequest, CallSettings)
    
    
    public virtual Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> UpdateFeatureGroup(UpdateFeatureGroupRequest request, CallSettings callSettings = null)

Updates the parameters of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureGroupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)[UpdateFeatureGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureGroupOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    UpdateFeatureGroupRequest request = new UpdateFeatureGroupRequest
    {
        FeatureGroup = new FeatureGroup(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> response = featureRegistryServiceClient.UpdateFeatureGroup(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FeatureGroup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceUpdateFeatureGroup(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureGroup retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureGroupAsync(FeatureGroup, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata>> UpdateFeatureGroupAsync(FeatureGroup featureGroup, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`featureGroup` | `[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)`  
Required. The FeatureGroup's `name` field is used to identify the FeatureGroup to be updated. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the FeatureGroup resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields:

  * `labels`
  * `description`
  * `big_query`
  * `big_query.entity_id_columns`

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)[UpdateFeatureGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureGroupOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureGroup featureGroup = new FeatureGroup();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> response = await featureRegistryServiceClient.UpdateFeatureGroupAsync(featureGroup, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureGroup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceUpdateFeatureGroupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureGroup retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureGroupAsync(FeatureGroup, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata>> UpdateFeatureGroupAsync(FeatureGroup featureGroup, FieldMask updateMask, CancellationToken cancellationToken)

Updates the parameters of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`featureGroup` | `[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)`  
Required. The FeatureGroup's `name` field is used to identify the FeatureGroup to be updated. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the FeatureGroup resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields:

  * `labels`
  * `description`
  * `big_query`
  * `big_query.entity_id_columns`

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)[UpdateFeatureGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureGroupOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureGroup featureGroup = new FeatureGroup();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> response = await featureRegistryServiceClient.UpdateFeatureGroupAsync(featureGroup, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureGroup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceUpdateFeatureGroupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureGroup retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureGroupAsync(UpdateFeatureGroupRequest, CallSettings)
    
    
    public virtual Task<Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata>> UpdateFeatureGroupAsync(UpdateFeatureGroupRequest request, CallSettings callSettings = null)

Updates the parameters of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureGroupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)[UpdateFeatureGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureGroupOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateFeatureGroupRequest request = new UpdateFeatureGroupRequest
    {
        FeatureGroup = new FeatureGroup(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> response = await featureRegistryServiceClient.UpdateFeatureGroupAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureGroup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceUpdateFeatureGroupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureGroup retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureGroupAsync(UpdateFeatureGroupRequest, CancellationToken)
    
    
    public virtual Task<Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata>> UpdateFeatureGroupAsync(UpdateFeatureGroupRequest request, CancellationToken cancellationToken)

Updates the parameters of a single FeatureGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureGroupRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureGroup)[UpdateFeatureGroupOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureGroupOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateFeatureGroupRequest request = new UpdateFeatureGroupRequest
    {
        FeatureGroup = new FeatureGroup(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> response = await featureRegistryServiceClient.UpdateFeatureGroupAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureGroup result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureGroup, UpdateFeatureGroupOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceUpdateFeatureGroupAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureGroup retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureMonitor(FeatureMonitor, FieldMask, CallSettings)
    
    
    public virtual Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> UpdateFeatureMonitor(FeatureMonitor featureMonitor, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`featureMonitor` | `[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)`  
Required. The FeatureMonitor's `name` field is used to identify the FeatureMonitor to be updated. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the FeatureMonitor resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields:

  * `labels`

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)[UpdateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureMonitorOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    FeatureMonitor featureMonitor = new FeatureMonitor();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> response = featureRegistryServiceClient.UpdateFeatureMonitor(featureMonitor, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FeatureMonitor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceUpdateFeatureMonitor(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureMonitor retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureMonitor(UpdateFeatureMonitorRequest, CallSettings)
    
    
    public virtual Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> UpdateFeatureMonitor(UpdateFeatureMonitorRequest request, CallSettings callSettings = null)

Updates the parameters of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureMonitorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)[UpdateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureMonitorOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = FeatureRegistryServiceClient.Create();
    // Initialize request argument(s)
    UpdateFeatureMonitorRequest request = new UpdateFeatureMonitorRequest
    {
        FeatureMonitor = new FeatureMonitor(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> response = featureRegistryServiceClient.UpdateFeatureMonitor(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FeatureMonitor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> retrievedResponse = featureRegistryServiceClient.PollOnceUpdateFeatureMonitor(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureMonitor retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureMonitorAsync(FeatureMonitor, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata>> UpdateFeatureMonitorAsync(FeatureMonitor featureMonitor, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`featureMonitor` | `[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)`  
Required. The FeatureMonitor's `name` field is used to identify the FeatureMonitor to be updated. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the FeatureMonitor resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields:

  * `labels`

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)[UpdateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureMonitorOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureMonitor featureMonitor = new FeatureMonitor();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> response = await featureRegistryServiceClient.UpdateFeatureMonitorAsync(featureMonitor, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureMonitor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceUpdateFeatureMonitorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureMonitor retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureMonitorAsync(FeatureMonitor, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata>> UpdateFeatureMonitorAsync(FeatureMonitor featureMonitor, FieldMask updateMask, CancellationToken cancellationToken)

Updates the parameters of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`featureMonitor` | `[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)`  
Required. The FeatureMonitor's `name` field is used to identify the FeatureMonitor to be updated. Format: `projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the FeatureMonitor resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields:

  * `labels`

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)[UpdateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureMonitorOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureMonitor featureMonitor = new FeatureMonitor();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> response = await featureRegistryServiceClient.UpdateFeatureMonitorAsync(featureMonitor, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureMonitor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceUpdateFeatureMonitorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureMonitor retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureMonitorAsync(UpdateFeatureMonitorRequest, CallSettings)
    
    
    public virtual Task<Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata>> UpdateFeatureMonitorAsync(UpdateFeatureMonitorRequest request, CallSettings callSettings = null)

Updates the parameters of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureMonitorRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)[UpdateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureMonitorOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateFeatureMonitorRequest request = new UpdateFeatureMonitorRequest
    {
        FeatureMonitor = new FeatureMonitor(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> response = await featureRegistryServiceClient.UpdateFeatureMonitorAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureMonitor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceUpdateFeatureMonitorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureMonitor retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureMonitorAsync(UpdateFeatureMonitorRequest, CancellationToken)
    
    
    public virtual Task<Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata>> UpdateFeatureMonitorAsync(UpdateFeatureMonitorRequest request, CancellationToken cancellationToken)

Updates the parameters of a single FeatureMonitor.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureMonitorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureMonitorRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureMonitor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureMonitor)[UpdateFeatureMonitorOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateFeatureMonitorOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureRegistryServiceClient featureRegistryServiceClient = await FeatureRegistryServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateFeatureMonitorRequest request = new UpdateFeatureMonitorRequest
    {
        FeatureMonitor = new FeatureMonitor(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> response = await featureRegistryServiceClient.UpdateFeatureMonitorAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureMonitor result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureMonitor, UpdateFeatureMonitorOperationMetadata> retrievedResponse = await featureRegistryServiceClient.PollOnceUpdateFeatureMonitorAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureMonitor retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
