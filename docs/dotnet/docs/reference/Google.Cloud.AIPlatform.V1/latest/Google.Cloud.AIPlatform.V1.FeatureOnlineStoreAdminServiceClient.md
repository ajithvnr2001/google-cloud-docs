---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminServiceClient
title: Vertex AI v1 API - Class FeatureOnlineStoreAdminServiceClient (3.77.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:55.537982+00:00
---

# Vertex AI v1 API - Class FeatureOnlineStoreAdminServiceClient (3.77.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1 API - Class FeatureOnlineStoreAdminServiceClient (3.77.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.77.0 (latest)  3.76.0  3.75.0  3.74.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public abstract class FeatureOnlineStoreAdminServiceClient

Reference documentation and code samples for the Vertex AI v1 API class FeatureOnlineStoreAdminServiceClient.

FeatureOnlineStoreAdminService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > FeatureOnlineStoreAdminServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[FeatureOnlineStoreAdminServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminServiceClientImpl)

## Namespace

[Google.Cloud.AIPlatform.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1)

## Assembly

Google.Cloud.AIPlatform.V1.dll

## Remarks

The service that handles CRUD and List for resources for FeatureOnlineStore.

## Properties 

### CreateFeatureOnlineStoreOperationsClient
    
    
    public virtual OperationsClient CreateFeatureOnlineStoreOperationsClient { get; }

The long-running operations client for `CreateFeatureOnlineStore`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### CreateFeatureViewOperationsClient
    
    
    public virtual OperationsClient CreateFeatureViewOperationsClient { get; }

The long-running operations client for `CreateFeatureView`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the FeatureOnlineStoreAdminService service, which is a host of "aiplatform.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default FeatureOnlineStoreAdminService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default FeatureOnlineStoreAdminService scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteFeatureOnlineStoreOperationsClient
    
    
    public virtual OperationsClient DeleteFeatureOnlineStoreOperationsClient { get; }

The long-running operations client for `DeleteFeatureOnlineStore`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteFeatureViewOperationsClient
    
    
    public virtual OperationsClient DeleteFeatureViewOperationsClient { get; }

The long-running operations client for `DeleteFeatureView`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual FeatureOnlineStoreAdminService.FeatureOnlineStoreAdminServiceClient GrpcClient { get; }

The underlying gRPC FeatureOnlineStoreAdminService client

**Property Value**  
---  
**Type** | **Description**  
`[FeatureOnlineStoreAdminService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminService)[FeatureOnlineStoreAdminServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminService.FeatureOnlineStoreAdminServiceClient)` |   
  
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
  
### UpdateFeatureOnlineStoreOperationsClient
    
    
    public virtual OperationsClient UpdateFeatureOnlineStoreOperationsClient { get; }

The long-running operations client for `UpdateFeatureOnlineStore`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### UpdateFeatureViewOperationsClient
    
    
    public virtual OperationsClient UpdateFeatureViewOperationsClient { get; }

The long-running operations client for `UpdateFeatureView`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### Create()
    
    
    public static FeatureOnlineStoreAdminServiceClient Create()

Synchronously creates a [FeatureOnlineStoreAdminServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [FeatureOnlineStoreAdminServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStoreAdminServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminServiceClient)` | The created [FeatureOnlineStoreAdminServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<FeatureOnlineStoreAdminServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [FeatureOnlineStoreAdminServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [FeatureOnlineStoreAdminServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureOnlineStoreAdminServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminServiceClient)` | The task representing the created [FeatureOnlineStoreAdminServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminServiceClient).  
  
### CreateFeatureOnlineStore(LocationName, FeatureOnlineStore, string, CallSettings)
    
    
    public virtual Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> CreateFeatureOnlineStore(LocationName parent, FeatureOnlineStore featureOnlineStore, string featureOnlineStoreId, CallSettings callSettings = null)

Creates a new FeatureOnlineStore in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the Location to create FeatureOnlineStores. Format: `projects/{project}/locations/{location}`  
`featureOnlineStore` | `[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)`  
Required. The FeatureOnlineStore to create.  
`featureOnlineStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this FeatureOnlineStore, which will become the final component of the FeatureOnlineStore's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)[CreateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureOnlineStoreOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    FeatureOnlineStore featureOnlineStore = new FeatureOnlineStore();
    string featureOnlineStoreId = "";
    // Make the request
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> response = featureOnlineStoreAdminServiceClient.CreateFeatureOnlineStore(parent, featureOnlineStore, featureOnlineStoreId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FeatureOnlineStore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> retrievedResponse = featureOnlineStoreAdminServiceClient.PollOnceCreateFeatureOnlineStore(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureOnlineStore retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureOnlineStore(CreateFeatureOnlineStoreRequest, CallSettings)
    
    
    public virtual Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> CreateFeatureOnlineStore(CreateFeatureOnlineStoreRequest request, CallSettings callSettings = null)

Creates a new FeatureOnlineStore in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureOnlineStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureOnlineStoreRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)[CreateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureOnlineStoreOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    CreateFeatureOnlineStoreRequest request = new CreateFeatureOnlineStoreRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        FeatureOnlineStore = new FeatureOnlineStore(),
        FeatureOnlineStoreId = "",
    };
    // Make the request
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> response = featureOnlineStoreAdminServiceClient.CreateFeatureOnlineStore(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FeatureOnlineStore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> retrievedResponse = featureOnlineStoreAdminServiceClient.PollOnceCreateFeatureOnlineStore(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureOnlineStore retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureOnlineStore(string, FeatureOnlineStore, string, CallSettings)
    
    
    public virtual Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> CreateFeatureOnlineStore(string parent, FeatureOnlineStore featureOnlineStore, string featureOnlineStoreId, CallSettings callSettings = null)

Creates a new FeatureOnlineStore in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to create FeatureOnlineStores. Format: `projects/{project}/locations/{location}`  
`featureOnlineStore` | `[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)`  
Required. The FeatureOnlineStore to create.  
`featureOnlineStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this FeatureOnlineStore, which will become the final component of the FeatureOnlineStore's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)[CreateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureOnlineStoreOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    FeatureOnlineStore featureOnlineStore = new FeatureOnlineStore();
    string featureOnlineStoreId = "";
    // Make the request
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> response = featureOnlineStoreAdminServiceClient.CreateFeatureOnlineStore(parent, featureOnlineStore, featureOnlineStoreId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FeatureOnlineStore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> retrievedResponse = featureOnlineStoreAdminServiceClient.PollOnceCreateFeatureOnlineStore(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureOnlineStore retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureOnlineStoreAsync(LocationName, FeatureOnlineStore, string, CallSettings)
    
    
    public virtual Task<Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata>> CreateFeatureOnlineStoreAsync(LocationName parent, FeatureOnlineStore featureOnlineStore, string featureOnlineStoreId, CallSettings callSettings = null)

Creates a new FeatureOnlineStore in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the Location to create FeatureOnlineStores. Format: `projects/{project}/locations/{location}`  
`featureOnlineStore` | `[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)`  
Required. The FeatureOnlineStore to create.  
`featureOnlineStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this FeatureOnlineStore, which will become the final component of the FeatureOnlineStore's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)[CreateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureOnlineStoreOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    FeatureOnlineStore featureOnlineStore = new FeatureOnlineStore();
    string featureOnlineStoreId = "";
    // Make the request
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> response = await featureOnlineStoreAdminServiceClient.CreateFeatureOnlineStoreAsync(parent, featureOnlineStore, featureOnlineStoreId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureOnlineStore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceCreateFeatureOnlineStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureOnlineStore retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureOnlineStoreAsync(LocationName, FeatureOnlineStore, string, CancellationToken)
    
    
    public virtual Task<Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata>> CreateFeatureOnlineStoreAsync(LocationName parent, FeatureOnlineStore featureOnlineStore, string featureOnlineStoreId, CancellationToken cancellationToken)

Creates a new FeatureOnlineStore in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the Location to create FeatureOnlineStores. Format: `projects/{project}/locations/{location}`  
`featureOnlineStore` | `[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)`  
Required. The FeatureOnlineStore to create.  
`featureOnlineStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this FeatureOnlineStore, which will become the final component of the FeatureOnlineStore's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)[CreateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureOnlineStoreOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    FeatureOnlineStore featureOnlineStore = new FeatureOnlineStore();
    string featureOnlineStoreId = "";
    // Make the request
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> response = await featureOnlineStoreAdminServiceClient.CreateFeatureOnlineStoreAsync(parent, featureOnlineStore, featureOnlineStoreId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureOnlineStore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceCreateFeatureOnlineStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureOnlineStore retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureOnlineStoreAsync(CreateFeatureOnlineStoreRequest, CallSettings)
    
    
    public virtual Task<Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata>> CreateFeatureOnlineStoreAsync(CreateFeatureOnlineStoreRequest request, CallSettings callSettings = null)

Creates a new FeatureOnlineStore in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureOnlineStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureOnlineStoreRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)[CreateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureOnlineStoreOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateFeatureOnlineStoreRequest request = new CreateFeatureOnlineStoreRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        FeatureOnlineStore = new FeatureOnlineStore(),
        FeatureOnlineStoreId = "",
    };
    // Make the request
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> response = await featureOnlineStoreAdminServiceClient.CreateFeatureOnlineStoreAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureOnlineStore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceCreateFeatureOnlineStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureOnlineStore retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureOnlineStoreAsync(CreateFeatureOnlineStoreRequest, CancellationToken)
    
    
    public virtual Task<Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata>> CreateFeatureOnlineStoreAsync(CreateFeatureOnlineStoreRequest request, CancellationToken cancellationToken)

Creates a new FeatureOnlineStore in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureOnlineStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureOnlineStoreRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)[CreateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureOnlineStoreOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateFeatureOnlineStoreRequest request = new CreateFeatureOnlineStoreRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        FeatureOnlineStore = new FeatureOnlineStore(),
        FeatureOnlineStoreId = "",
    };
    // Make the request
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> response = await featureOnlineStoreAdminServiceClient.CreateFeatureOnlineStoreAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureOnlineStore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceCreateFeatureOnlineStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureOnlineStore retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureOnlineStoreAsync(string, FeatureOnlineStore, string, CallSettings)
    
    
    public virtual Task<Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata>> CreateFeatureOnlineStoreAsync(string parent, FeatureOnlineStore featureOnlineStore, string featureOnlineStoreId, CallSettings callSettings = null)

Creates a new FeatureOnlineStore in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to create FeatureOnlineStores. Format: `projects/{project}/locations/{location}`  
`featureOnlineStore` | `[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)`  
Required. The FeatureOnlineStore to create.  
`featureOnlineStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this FeatureOnlineStore, which will become the final component of the FeatureOnlineStore's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)[CreateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureOnlineStoreOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    FeatureOnlineStore featureOnlineStore = new FeatureOnlineStore();
    string featureOnlineStoreId = "";
    // Make the request
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> response = await featureOnlineStoreAdminServiceClient.CreateFeatureOnlineStoreAsync(parent, featureOnlineStore, featureOnlineStoreId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureOnlineStore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceCreateFeatureOnlineStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureOnlineStore retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureOnlineStoreAsync(string, FeatureOnlineStore, string, CancellationToken)
    
    
    public virtual Task<Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata>> CreateFeatureOnlineStoreAsync(string parent, FeatureOnlineStore featureOnlineStore, string featureOnlineStoreId, CancellationToken cancellationToken)

Creates a new FeatureOnlineStore in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to create FeatureOnlineStores. Format: `projects/{project}/locations/{location}`  
`featureOnlineStore` | `[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)`  
Required. The FeatureOnlineStore to create.  
`featureOnlineStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this FeatureOnlineStore, which will become the final component of the FeatureOnlineStore's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within the project and location.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)[CreateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureOnlineStoreOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    FeatureOnlineStore featureOnlineStore = new FeatureOnlineStore();
    string featureOnlineStoreId = "";
    // Make the request
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> response = await featureOnlineStoreAdminServiceClient.CreateFeatureOnlineStoreAsync(parent, featureOnlineStore, featureOnlineStoreId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureOnlineStore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceCreateFeatureOnlineStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureOnlineStore retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureView(CreateFeatureViewRequest, CallSettings)
    
    
    public virtual Operation<FeatureView, CreateFeatureViewOperationMetadata> CreateFeatureView(CreateFeatureViewRequest request, CallSettings callSettings = null)

Creates a new FeatureView in a given FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureViewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureViewRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)[CreateFeatureViewOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureViewOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    CreateFeatureViewRequest request = new CreateFeatureViewRequest
    {
        ParentAsFeatureOnlineStoreName = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]"),
        FeatureView = new FeatureView(),
        FeatureViewId = "",
        RunSyncImmediately = false,
    };
    // Make the request
    Operation<FeatureView, CreateFeatureViewOperationMetadata> response = featureOnlineStoreAdminServiceClient.CreateFeatureView(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureView, CreateFeatureViewOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FeatureView result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureView, CreateFeatureViewOperationMetadata> retrievedResponse = featureOnlineStoreAdminServiceClient.PollOnceCreateFeatureView(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureView retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureView(FeatureOnlineStoreName, FeatureView, string, CallSettings)
    
    
    public virtual Operation<FeatureView, CreateFeatureViewOperationMetadata> CreateFeatureView(FeatureOnlineStoreName parent, FeatureView featureView, string featureViewId, CallSettings callSettings = null)

Creates a new FeatureView in a given FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureOnlineStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreName)`  
Required. The resource name of the FeatureOnlineStore to create FeatureViews. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`featureView` | `[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)`  
Required. The FeatureView to create.  
`featureViewId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the FeatureView, which will become the final component of the FeatureView's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within a FeatureOnlineStore.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)[CreateFeatureViewOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureViewOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    FeatureOnlineStoreName parent = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]");
    FeatureView featureView = new FeatureView();
    string featureViewId = "";
    // Make the request
    Operation<FeatureView, CreateFeatureViewOperationMetadata> response = featureOnlineStoreAdminServiceClient.CreateFeatureView(parent, featureView, featureViewId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureView, CreateFeatureViewOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FeatureView result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureView, CreateFeatureViewOperationMetadata> retrievedResponse = featureOnlineStoreAdminServiceClient.PollOnceCreateFeatureView(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureView retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureView(string, FeatureView, string, CallSettings)
    
    
    public virtual Operation<FeatureView, CreateFeatureViewOperationMetadata> CreateFeatureView(string parent, FeatureView featureView, string featureViewId, CallSettings callSettings = null)

Creates a new FeatureView in a given FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the FeatureOnlineStore to create FeatureViews. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`featureView` | `[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)`  
Required. The FeatureView to create.  
`featureViewId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the FeatureView, which will become the final component of the FeatureView's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within a FeatureOnlineStore.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)[CreateFeatureViewOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureViewOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]";
    FeatureView featureView = new FeatureView();
    string featureViewId = "";
    // Make the request
    Operation<FeatureView, CreateFeatureViewOperationMetadata> response = featureOnlineStoreAdminServiceClient.CreateFeatureView(parent, featureView, featureViewId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureView, CreateFeatureViewOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FeatureView result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureView, CreateFeatureViewOperationMetadata> retrievedResponse = featureOnlineStoreAdminServiceClient.PollOnceCreateFeatureView(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureView retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureViewAsync(CreateFeatureViewRequest, CallSettings)
    
    
    public virtual Task<Operation<FeatureView, CreateFeatureViewOperationMetadata>> CreateFeatureViewAsync(CreateFeatureViewRequest request, CallSettings callSettings = null)

Creates a new FeatureView in a given FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureViewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureViewRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)[CreateFeatureViewOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureViewOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateFeatureViewRequest request = new CreateFeatureViewRequest
    {
        ParentAsFeatureOnlineStoreName = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]"),
        FeatureView = new FeatureView(),
        FeatureViewId = "",
        RunSyncImmediately = false,
    };
    // Make the request
    Operation<FeatureView, CreateFeatureViewOperationMetadata> response = await featureOnlineStoreAdminServiceClient.CreateFeatureViewAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureView, CreateFeatureViewOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureView result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureView, CreateFeatureViewOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceCreateFeatureViewAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureView retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureViewAsync(CreateFeatureViewRequest, CancellationToken)
    
    
    public virtual Task<Operation<FeatureView, CreateFeatureViewOperationMetadata>> CreateFeatureViewAsync(CreateFeatureViewRequest request, CancellationToken cancellationToken)

Creates a new FeatureView in a given FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureViewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureViewRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)[CreateFeatureViewOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureViewOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateFeatureViewRequest request = new CreateFeatureViewRequest
    {
        ParentAsFeatureOnlineStoreName = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]"),
        FeatureView = new FeatureView(),
        FeatureViewId = "",
        RunSyncImmediately = false,
    };
    // Make the request
    Operation<FeatureView, CreateFeatureViewOperationMetadata> response = await featureOnlineStoreAdminServiceClient.CreateFeatureViewAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureView, CreateFeatureViewOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureView result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureView, CreateFeatureViewOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceCreateFeatureViewAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureView retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureViewAsync(FeatureOnlineStoreName, FeatureView, string, CallSettings)
    
    
    public virtual Task<Operation<FeatureView, CreateFeatureViewOperationMetadata>> CreateFeatureViewAsync(FeatureOnlineStoreName parent, FeatureView featureView, string featureViewId, CallSettings callSettings = null)

Creates a new FeatureView in a given FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureOnlineStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreName)`  
Required. The resource name of the FeatureOnlineStore to create FeatureViews. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`featureView` | `[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)`  
Required. The FeatureView to create.  
`featureViewId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the FeatureView, which will become the final component of the FeatureView's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within a FeatureOnlineStore.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)[CreateFeatureViewOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureViewOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureOnlineStoreName parent = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]");
    FeatureView featureView = new FeatureView();
    string featureViewId = "";
    // Make the request
    Operation<FeatureView, CreateFeatureViewOperationMetadata> response = await featureOnlineStoreAdminServiceClient.CreateFeatureViewAsync(parent, featureView, featureViewId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureView, CreateFeatureViewOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureView result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureView, CreateFeatureViewOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceCreateFeatureViewAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureView retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureViewAsync(FeatureOnlineStoreName, FeatureView, string, CancellationToken)
    
    
    public virtual Task<Operation<FeatureView, CreateFeatureViewOperationMetadata>> CreateFeatureViewAsync(FeatureOnlineStoreName parent, FeatureView featureView, string featureViewId, CancellationToken cancellationToken)

Creates a new FeatureView in a given FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureOnlineStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreName)`  
Required. The resource name of the FeatureOnlineStore to create FeatureViews. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`featureView` | `[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)`  
Required. The FeatureView to create.  
`featureViewId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the FeatureView, which will become the final component of the FeatureView's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within a FeatureOnlineStore.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)[CreateFeatureViewOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureViewOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureOnlineStoreName parent = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]");
    FeatureView featureView = new FeatureView();
    string featureViewId = "";
    // Make the request
    Operation<FeatureView, CreateFeatureViewOperationMetadata> response = await featureOnlineStoreAdminServiceClient.CreateFeatureViewAsync(parent, featureView, featureViewId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureView, CreateFeatureViewOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureView result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureView, CreateFeatureViewOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceCreateFeatureViewAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureView retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureViewAsync(string, FeatureView, string, CallSettings)
    
    
    public virtual Task<Operation<FeatureView, CreateFeatureViewOperationMetadata>> CreateFeatureViewAsync(string parent, FeatureView featureView, string featureViewId, CallSettings callSettings = null)

Creates a new FeatureView in a given FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the FeatureOnlineStore to create FeatureViews. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`featureView` | `[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)`  
Required. The FeatureView to create.  
`featureViewId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the FeatureView, which will become the final component of the FeatureView's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within a FeatureOnlineStore.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)[CreateFeatureViewOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureViewOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]";
    FeatureView featureView = new FeatureView();
    string featureViewId = "";
    // Make the request
    Operation<FeatureView, CreateFeatureViewOperationMetadata> response = await featureOnlineStoreAdminServiceClient.CreateFeatureViewAsync(parent, featureView, featureViewId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureView, CreateFeatureViewOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureView result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureView, CreateFeatureViewOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceCreateFeatureViewAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureView retrievedResult = retrievedResponse.Result;
    }
    

### CreateFeatureViewAsync(string, FeatureView, string, CancellationToken)
    
    
    public virtual Task<Operation<FeatureView, CreateFeatureViewOperationMetadata>> CreateFeatureViewAsync(string parent, FeatureView featureView, string featureViewId, CancellationToken cancellationToken)

Creates a new FeatureView in a given FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the FeatureOnlineStore to create FeatureViews. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`featureView` | `[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)`  
Required. The FeatureView to create.  
`featureViewId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the FeatureView, which will become the final component of the FeatureView's resource name. This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number. The value must be unique within a FeatureOnlineStore.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)[CreateFeatureViewOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureViewOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]";
    FeatureView featureView = new FeatureView();
    string featureViewId = "";
    // Make the request
    Operation<FeatureView, CreateFeatureViewOperationMetadata> response = await featureOnlineStoreAdminServiceClient.CreateFeatureViewAsync(parent, featureView, featureViewId);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureView, CreateFeatureViewOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureView result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureView, CreateFeatureViewOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceCreateFeatureViewAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureView retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureOnlineStore(DeleteFeatureOnlineStoreRequest, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteFeatureOnlineStore(DeleteFeatureOnlineStoreRequest request, CallSettings callSettings = null)

Deletes a single FeatureOnlineStore. The FeatureOnlineStore must not contain any FeatureViews.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureOnlineStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteFeatureOnlineStoreRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    DeleteFeatureOnlineStoreRequest request = new DeleteFeatureOnlineStoreRequest
    {
        FeatureOnlineStoreName = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]"),
        Force = false,
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = featureOnlineStoreAdminServiceClient.DeleteFeatureOnlineStore(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = featureOnlineStoreAdminServiceClient.PollOnceDeleteFeatureOnlineStore(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureOnlineStore(FeatureOnlineStoreName, bool, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteFeatureOnlineStore(FeatureOnlineStoreName name, bool force, CallSettings callSettings = null)

Deletes a single FeatureOnlineStore. The FeatureOnlineStore must not contain any FeatureViews.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureOnlineStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreName)`  
Required. The name of the FeatureOnlineStore to be deleted. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`force` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If set to true, any FeatureViews and Features for this FeatureOnlineStore will also be deleted. (Otherwise, the request will only work if the FeatureOnlineStore has no FeatureViews.)  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    FeatureOnlineStoreName name = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]");
    bool force = false;
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = featureOnlineStoreAdminServiceClient.DeleteFeatureOnlineStore(name, force);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = featureOnlineStoreAdminServiceClient.PollOnceDeleteFeatureOnlineStore(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureOnlineStore(string, bool, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteFeatureOnlineStore(string name, bool force, CallSettings callSettings = null)

Deletes a single FeatureOnlineStore. The FeatureOnlineStore must not contain any FeatureViews.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureOnlineStore to be deleted. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`force` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If set to true, any FeatureViews and Features for this FeatureOnlineStore will also be deleted. (Otherwise, the request will only work if the FeatureOnlineStore has no FeatureViews.)  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]";
    bool force = false;
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = featureOnlineStoreAdminServiceClient.DeleteFeatureOnlineStore(name, force);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = featureOnlineStoreAdminServiceClient.PollOnceDeleteFeatureOnlineStore(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureOnlineStoreAsync(DeleteFeatureOnlineStoreRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureOnlineStoreAsync(DeleteFeatureOnlineStoreRequest request, CallSettings callSettings = null)

Deletes a single FeatureOnlineStore. The FeatureOnlineStore must not contain any FeatureViews.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureOnlineStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteFeatureOnlineStoreRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteFeatureOnlineStoreRequest request = new DeleteFeatureOnlineStoreRequest
    {
        FeatureOnlineStoreName = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]"),
        Force = false,
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureOnlineStoreAdminServiceClient.DeleteFeatureOnlineStoreAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceDeleteFeatureOnlineStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureOnlineStoreAsync(DeleteFeatureOnlineStoreRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureOnlineStoreAsync(DeleteFeatureOnlineStoreRequest request, CancellationToken cancellationToken)

Deletes a single FeatureOnlineStore. The FeatureOnlineStore must not contain any FeatureViews.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureOnlineStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteFeatureOnlineStoreRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteFeatureOnlineStoreRequest request = new DeleteFeatureOnlineStoreRequest
    {
        FeatureOnlineStoreName = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]"),
        Force = false,
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureOnlineStoreAdminServiceClient.DeleteFeatureOnlineStoreAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceDeleteFeatureOnlineStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureOnlineStoreAsync(FeatureOnlineStoreName, bool, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureOnlineStoreAsync(FeatureOnlineStoreName name, bool force, CallSettings callSettings = null)

Deletes a single FeatureOnlineStore. The FeatureOnlineStore must not contain any FeatureViews.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureOnlineStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreName)`  
Required. The name of the FeatureOnlineStore to be deleted. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`force` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If set to true, any FeatureViews and Features for this FeatureOnlineStore will also be deleted. (Otherwise, the request will only work if the FeatureOnlineStore has no FeatureViews.)  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureOnlineStoreName name = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]");
    bool force = false;
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureOnlineStoreAdminServiceClient.DeleteFeatureOnlineStoreAsync(name, force);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceDeleteFeatureOnlineStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureOnlineStoreAsync(FeatureOnlineStoreName, bool, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureOnlineStoreAsync(FeatureOnlineStoreName name, bool force, CancellationToken cancellationToken)

Deletes a single FeatureOnlineStore. The FeatureOnlineStore must not contain any FeatureViews.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureOnlineStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreName)`  
Required. The name of the FeatureOnlineStore to be deleted. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`force` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If set to true, any FeatureViews and Features for this FeatureOnlineStore will also be deleted. (Otherwise, the request will only work if the FeatureOnlineStore has no FeatureViews.)  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureOnlineStoreName name = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]");
    bool force = false;
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureOnlineStoreAdminServiceClient.DeleteFeatureOnlineStoreAsync(name, force);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceDeleteFeatureOnlineStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureOnlineStoreAsync(string, bool, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureOnlineStoreAsync(string name, bool force, CallSettings callSettings = null)

Deletes a single FeatureOnlineStore. The FeatureOnlineStore must not contain any FeatureViews.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureOnlineStore to be deleted. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`force` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If set to true, any FeatureViews and Features for this FeatureOnlineStore will also be deleted. (Otherwise, the request will only work if the FeatureOnlineStore has no FeatureViews.)  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]";
    bool force = false;
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureOnlineStoreAdminServiceClient.DeleteFeatureOnlineStoreAsync(name, force);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceDeleteFeatureOnlineStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureOnlineStoreAsync(string, bool, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureOnlineStoreAsync(string name, bool force, CancellationToken cancellationToken)

Deletes a single FeatureOnlineStore. The FeatureOnlineStore must not contain any FeatureViews.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureOnlineStore to be deleted. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`force` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If set to true, any FeatureViews and Features for this FeatureOnlineStore will also be deleted. (Otherwise, the request will only work if the FeatureOnlineStore has no FeatureViews.)  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]";
    bool force = false;
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureOnlineStoreAdminServiceClient.DeleteFeatureOnlineStoreAsync(name, force);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceDeleteFeatureOnlineStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureView(DeleteFeatureViewRequest, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteFeatureView(DeleteFeatureViewRequest request, CallSettings callSettings = null)

Deletes a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureViewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteFeatureViewRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    DeleteFeatureViewRequest request = new DeleteFeatureViewRequest
    {
        FeatureViewName = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]"),
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = featureOnlineStoreAdminServiceClient.DeleteFeatureView(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = featureOnlineStoreAdminServiceClient.PollOnceDeleteFeatureView(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureView(FeatureViewName, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteFeatureView(FeatureViewName name, CallSettings callSettings = null)

Deletes a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewName)`  
Required. The name of the FeatureView to be deleted. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    FeatureViewName name = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]");
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = featureOnlineStoreAdminServiceClient.DeleteFeatureView(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = featureOnlineStoreAdminServiceClient.PollOnceDeleteFeatureView(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureView(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteFeatureView(string name, CallSettings callSettings = null)

Deletes a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureView to be deleted. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]/featureViews/[FEATURE_VIEW]";
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = featureOnlineStoreAdminServiceClient.DeleteFeatureView(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = featureOnlineStoreAdminServiceClient.PollOnceDeleteFeatureView(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureViewAsync(DeleteFeatureViewRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureViewAsync(DeleteFeatureViewRequest request, CallSettings callSettings = null)

Deletes a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureViewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteFeatureViewRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteFeatureViewRequest request = new DeleteFeatureViewRequest
    {
        FeatureViewName = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]"),
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureOnlineStoreAdminServiceClient.DeleteFeatureViewAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceDeleteFeatureViewAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureViewAsync(DeleteFeatureViewRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureViewAsync(DeleteFeatureViewRequest request, CancellationToken cancellationToken)

Deletes a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureViewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteFeatureViewRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteFeatureViewRequest request = new DeleteFeatureViewRequest
    {
        FeatureViewName = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]"),
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureOnlineStoreAdminServiceClient.DeleteFeatureViewAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceDeleteFeatureViewAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureViewAsync(FeatureViewName, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureViewAsync(FeatureViewName name, CallSettings callSettings = null)

Deletes a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewName)`  
Required. The name of the FeatureView to be deleted. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureViewName name = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]");
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureOnlineStoreAdminServiceClient.DeleteFeatureViewAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceDeleteFeatureViewAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureViewAsync(FeatureViewName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureViewAsync(FeatureViewName name, CancellationToken cancellationToken)

Deletes a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewName)`  
Required. The name of the FeatureView to be deleted. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureViewName name = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]");
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureOnlineStoreAdminServiceClient.DeleteFeatureViewAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceDeleteFeatureViewAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureViewAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureViewAsync(string name, CallSettings callSettings = null)

Deletes a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureView to be deleted. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]/featureViews/[FEATURE_VIEW]";
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureOnlineStoreAdminServiceClient.DeleteFeatureViewAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceDeleteFeatureViewAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteFeatureViewAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteFeatureViewAsync(string name, CancellationToken cancellationToken)

Deletes a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureView to be deleted. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]/featureViews/[FEATURE_VIEW]";
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await featureOnlineStoreAdminServiceClient.DeleteFeatureViewAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceDeleteFeatureViewAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GetFeatureOnlineStore(FeatureOnlineStoreName, CallSettings)
    
    
    public virtual FeatureOnlineStore GetFeatureOnlineStore(FeatureOnlineStoreName name, CallSettings callSettings = null)

Gets details of a single FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureOnlineStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreName)`  
Required. The name of the FeatureOnlineStore resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    FeatureOnlineStoreName name = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]");
    // Make the request
    FeatureOnlineStore response = featureOnlineStoreAdminServiceClient.GetFeatureOnlineStore(name);
    

### GetFeatureOnlineStore(GetFeatureOnlineStoreRequest, CallSettings)
    
    
    public virtual FeatureOnlineStore GetFeatureOnlineStore(GetFeatureOnlineStoreRequest request, CallSettings callSettings = null)

Gets details of a single FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureOnlineStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GetFeatureOnlineStoreRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    GetFeatureOnlineStoreRequest request = new GetFeatureOnlineStoreRequest
    {
        FeatureOnlineStoreName = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]"),
    };
    // Make the request
    FeatureOnlineStore response = featureOnlineStoreAdminServiceClient.GetFeatureOnlineStore(request);
    

### GetFeatureOnlineStore(string, CallSettings)
    
    
    public virtual FeatureOnlineStore GetFeatureOnlineStore(string name, CallSettings callSettings = null)

Gets details of a single FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureOnlineStore resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]";
    // Make the request
    FeatureOnlineStore response = featureOnlineStoreAdminServiceClient.GetFeatureOnlineStore(name);
    

### GetFeatureOnlineStoreAsync(FeatureOnlineStoreName, CallSettings)
    
    
    public virtual Task<FeatureOnlineStore> GetFeatureOnlineStoreAsync(FeatureOnlineStoreName name, CallSettings callSettings = null)

Gets details of a single FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureOnlineStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreName)`  
Required. The name of the FeatureOnlineStore resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureOnlineStoreName name = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]");
    // Make the request
    FeatureOnlineStore response = await featureOnlineStoreAdminServiceClient.GetFeatureOnlineStoreAsync(name);
    

### GetFeatureOnlineStoreAsync(FeatureOnlineStoreName, CancellationToken)
    
    
    public virtual Task<FeatureOnlineStore> GetFeatureOnlineStoreAsync(FeatureOnlineStoreName name, CancellationToken cancellationToken)

Gets details of a single FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureOnlineStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreName)`  
Required. The name of the FeatureOnlineStore resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureOnlineStoreName name = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]");
    // Make the request
    FeatureOnlineStore response = await featureOnlineStoreAdminServiceClient.GetFeatureOnlineStoreAsync(name);
    

### GetFeatureOnlineStoreAsync(GetFeatureOnlineStoreRequest, CallSettings)
    
    
    public virtual Task<FeatureOnlineStore> GetFeatureOnlineStoreAsync(GetFeatureOnlineStoreRequest request, CallSettings callSettings = null)

Gets details of a single FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureOnlineStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GetFeatureOnlineStoreRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetFeatureOnlineStoreRequest request = new GetFeatureOnlineStoreRequest
    {
        FeatureOnlineStoreName = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]"),
    };
    // Make the request
    FeatureOnlineStore response = await featureOnlineStoreAdminServiceClient.GetFeatureOnlineStoreAsync(request);
    

### GetFeatureOnlineStoreAsync(GetFeatureOnlineStoreRequest, CancellationToken)
    
    
    public virtual Task<FeatureOnlineStore> GetFeatureOnlineStoreAsync(GetFeatureOnlineStoreRequest request, CancellationToken cancellationToken)

Gets details of a single FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureOnlineStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GetFeatureOnlineStoreRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetFeatureOnlineStoreRequest request = new GetFeatureOnlineStoreRequest
    {
        FeatureOnlineStoreName = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]"),
    };
    // Make the request
    FeatureOnlineStore response = await featureOnlineStoreAdminServiceClient.GetFeatureOnlineStoreAsync(request);
    

### GetFeatureOnlineStoreAsync(string, CallSettings)
    
    
    public virtual Task<FeatureOnlineStore> GetFeatureOnlineStoreAsync(string name, CallSettings callSettings = null)

Gets details of a single FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureOnlineStore resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]";
    // Make the request
    FeatureOnlineStore response = await featureOnlineStoreAdminServiceClient.GetFeatureOnlineStoreAsync(name);
    

### GetFeatureOnlineStoreAsync(string, CancellationToken)
    
    
    public virtual Task<FeatureOnlineStore> GetFeatureOnlineStoreAsync(string name, CancellationToken cancellationToken)

Gets details of a single FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureOnlineStore resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]";
    // Make the request
    FeatureOnlineStore response = await featureOnlineStoreAdminServiceClient.GetFeatureOnlineStoreAsync(name);
    

### GetFeatureView(FeatureViewName, CallSettings)
    
    
    public virtual FeatureView GetFeatureView(FeatureViewName name, CallSettings callSettings = null)

Gets details of a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewName)`  
Required. The name of the FeatureView resource. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    FeatureViewName name = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]");
    // Make the request
    FeatureView response = featureOnlineStoreAdminServiceClient.GetFeatureView(name);
    

### GetFeatureView(GetFeatureViewRequest, CallSettings)
    
    
    public virtual FeatureView GetFeatureView(GetFeatureViewRequest request, CallSettings callSettings = null)

Gets details of a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureViewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GetFeatureViewRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    GetFeatureViewRequest request = new GetFeatureViewRequest
    {
        FeatureViewName = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]"),
    };
    // Make the request
    FeatureView response = featureOnlineStoreAdminServiceClient.GetFeatureView(request);
    

### GetFeatureView(string, CallSettings)
    
    
    public virtual FeatureView GetFeatureView(string name, CallSettings callSettings = null)

Gets details of a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureView resource. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]/featureViews/[FEATURE_VIEW]";
    // Make the request
    FeatureView response = featureOnlineStoreAdminServiceClient.GetFeatureView(name);
    

### GetFeatureViewAsync(FeatureViewName, CallSettings)
    
    
    public virtual Task<FeatureView> GetFeatureViewAsync(FeatureViewName name, CallSettings callSettings = null)

Gets details of a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewName)`  
Required. The name of the FeatureView resource. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureViewName name = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]");
    // Make the request
    FeatureView response = await featureOnlineStoreAdminServiceClient.GetFeatureViewAsync(name);
    

### GetFeatureViewAsync(FeatureViewName, CancellationToken)
    
    
    public virtual Task<FeatureView> GetFeatureViewAsync(FeatureViewName name, CancellationToken cancellationToken)

Gets details of a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewName)`  
Required. The name of the FeatureView resource. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureViewName name = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]");
    // Make the request
    FeatureView response = await featureOnlineStoreAdminServiceClient.GetFeatureViewAsync(name);
    

### GetFeatureViewAsync(GetFeatureViewRequest, CallSettings)
    
    
    public virtual Task<FeatureView> GetFeatureViewAsync(GetFeatureViewRequest request, CallSettings callSettings = null)

Gets details of a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureViewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GetFeatureViewRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetFeatureViewRequest request = new GetFeatureViewRequest
    {
        FeatureViewName = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]"),
    };
    // Make the request
    FeatureView response = await featureOnlineStoreAdminServiceClient.GetFeatureViewAsync(request);
    

### GetFeatureViewAsync(GetFeatureViewRequest, CancellationToken)
    
    
    public virtual Task<FeatureView> GetFeatureViewAsync(GetFeatureViewRequest request, CancellationToken cancellationToken)

Gets details of a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureViewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GetFeatureViewRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetFeatureViewRequest request = new GetFeatureViewRequest
    {
        FeatureViewName = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]"),
    };
    // Make the request
    FeatureView response = await featureOnlineStoreAdminServiceClient.GetFeatureViewAsync(request);
    

### GetFeatureViewAsync(string, CallSettings)
    
    
    public virtual Task<FeatureView> GetFeatureViewAsync(string name, CallSettings callSettings = null)

Gets details of a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureView resource. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]/featureViews/[FEATURE_VIEW]";
    // Make the request
    FeatureView response = await featureOnlineStoreAdminServiceClient.GetFeatureViewAsync(name);
    

### GetFeatureViewAsync(string, CancellationToken)
    
    
    public virtual Task<FeatureView> GetFeatureViewAsync(string name, CancellationToken cancellationToken)

Gets details of a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureView resource. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]/featureViews/[FEATURE_VIEW]";
    // Make the request
    FeatureView response = await featureOnlineStoreAdminServiceClient.GetFeatureViewAsync(name);
    

### GetFeatureViewSync(FeatureViewSyncName, CallSettings)
    
    
    public virtual FeatureViewSync GetFeatureViewSync(FeatureViewSyncName name, CallSettings callSettings = null)

Gets details of a single FeatureViewSync.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureViewSyncName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSyncName)`  
Required. The name of the FeatureViewSync resource. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}/featureViewSyncs/{feature_view_sync}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    FeatureViewSyncName name = FeatureViewSyncName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]");
    // Make the request
    FeatureViewSync response = featureOnlineStoreAdminServiceClient.GetFeatureViewSync(name);
    

### GetFeatureViewSync(GetFeatureViewSyncRequest, CallSettings)
    
    
    public virtual FeatureViewSync GetFeatureViewSync(GetFeatureViewSyncRequest request, CallSettings callSettings = null)

Gets details of a single FeatureViewSync.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureViewSyncRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GetFeatureViewSyncRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    GetFeatureViewSyncRequest request = new GetFeatureViewSyncRequest
    {
        FeatureViewSyncName = FeatureViewSyncName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]"),
    };
    // Make the request
    FeatureViewSync response = featureOnlineStoreAdminServiceClient.GetFeatureViewSync(request);
    

### GetFeatureViewSync(string, CallSettings)
    
    
    public virtual FeatureViewSync GetFeatureViewSync(string name, CallSettings callSettings = null)

Gets details of a single FeatureViewSync.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureViewSync resource. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}/featureViewSyncs/{feature_view_sync}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]/featureViews/[FEATURE_VIEW]/featureViewSyncs/feature_view_sync";
    // Make the request
    FeatureViewSync response = featureOnlineStoreAdminServiceClient.GetFeatureViewSync(name);
    

### GetFeatureViewSyncAsync(FeatureViewSyncName, CallSettings)
    
    
    public virtual Task<FeatureViewSync> GetFeatureViewSyncAsync(FeatureViewSyncName name, CallSettings callSettings = null)

Gets details of a single FeatureViewSync.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureViewSyncName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSyncName)`  
Required. The name of the FeatureViewSync resource. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}/featureViewSyncs/{feature_view_sync}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureViewSyncName name = FeatureViewSyncName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]");
    // Make the request
    FeatureViewSync response = await featureOnlineStoreAdminServiceClient.GetFeatureViewSyncAsync(name);
    

### GetFeatureViewSyncAsync(FeatureViewSyncName, CancellationToken)
    
    
    public virtual Task<FeatureViewSync> GetFeatureViewSyncAsync(FeatureViewSyncName name, CancellationToken cancellationToken)

Gets details of a single FeatureViewSync.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[FeatureViewSyncName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSyncName)`  
Required. The name of the FeatureViewSync resource. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}/featureViewSyncs/{feature_view_sync}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureViewSyncName name = FeatureViewSyncName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]");
    // Make the request
    FeatureViewSync response = await featureOnlineStoreAdminServiceClient.GetFeatureViewSyncAsync(name);
    

### GetFeatureViewSyncAsync(GetFeatureViewSyncRequest, CallSettings)
    
    
    public virtual Task<FeatureViewSync> GetFeatureViewSyncAsync(GetFeatureViewSyncRequest request, CallSettings callSettings = null)

Gets details of a single FeatureViewSync.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureViewSyncRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GetFeatureViewSyncRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetFeatureViewSyncRequest request = new GetFeatureViewSyncRequest
    {
        FeatureViewSyncName = FeatureViewSyncName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]"),
    };
    // Make the request
    FeatureViewSync response = await featureOnlineStoreAdminServiceClient.GetFeatureViewSyncAsync(request);
    

### GetFeatureViewSyncAsync(GetFeatureViewSyncRequest, CancellationToken)
    
    
    public virtual Task<FeatureViewSync> GetFeatureViewSyncAsync(GetFeatureViewSyncRequest request, CancellationToken cancellationToken)

Gets details of a single FeatureViewSync.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureViewSyncRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GetFeatureViewSyncRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetFeatureViewSyncRequest request = new GetFeatureViewSyncRequest
    {
        FeatureViewSyncName = FeatureViewSyncName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]"),
    };
    // Make the request
    FeatureViewSync response = await featureOnlineStoreAdminServiceClient.GetFeatureViewSyncAsync(request);
    

### GetFeatureViewSyncAsync(string, CallSettings)
    
    
    public virtual Task<FeatureViewSync> GetFeatureViewSyncAsync(string name, CallSettings callSettings = null)

Gets details of a single FeatureViewSync.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureViewSync resource. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}/featureViewSyncs/{feature_view_sync}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]/featureViews/[FEATURE_VIEW]/featureViewSyncs/feature_view_sync";
    // Make the request
    FeatureViewSync response = await featureOnlineStoreAdminServiceClient.GetFeatureViewSyncAsync(name);
    

### GetFeatureViewSyncAsync(string, CancellationToken)
    
    
    public virtual Task<FeatureViewSync> GetFeatureViewSyncAsync(string name, CancellationToken cancellationToken)

Gets details of a single FeatureViewSync.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the FeatureViewSync resource. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}/featureViewSyncs/{feature_view_sync}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]/featureViews/[FEATURE_VIEW]/featureViewSyncs/feature_view_sync";
    // Make the request
    FeatureViewSync response = await featureOnlineStoreAdminServiceClient.GetFeatureViewSyncAsync(name);
    

### ListFeatureOnlineStores(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeatureOnlineStoresResponse, FeatureOnlineStore> ListFeatureOnlineStores(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FeatureOnlineStores in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the Location to list FeatureOnlineStores. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeatureOnlineStoresResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureOnlineStoresResponse)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)` | A pageable sequence of [FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore) resources.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListFeatureOnlineStoresResponse, FeatureOnlineStore> response = featureOnlineStoreAdminServiceClient.ListFeatureOnlineStores(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FeatureOnlineStore item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeatureOnlineStoresResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureOnlineStore item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureOnlineStore> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureOnlineStore item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureOnlineStores(ListFeatureOnlineStoresRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeatureOnlineStoresResponse, FeatureOnlineStore> ListFeatureOnlineStores(ListFeatureOnlineStoresRequest request, CallSettings callSettings = null)

Lists FeatureOnlineStores in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureOnlineStoresRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureOnlineStoresRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeatureOnlineStoresResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureOnlineStoresResponse)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)` | A pageable sequence of [FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore) resources.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    ListFeatureOnlineStoresRequest request = new ListFeatureOnlineStoresRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListFeatureOnlineStoresResponse, FeatureOnlineStore> response = featureOnlineStoreAdminServiceClient.ListFeatureOnlineStores(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FeatureOnlineStore item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeatureOnlineStoresResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureOnlineStore item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureOnlineStore> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureOnlineStore item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureOnlineStores(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeatureOnlineStoresResponse, FeatureOnlineStore> ListFeatureOnlineStores(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FeatureOnlineStores in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to list FeatureOnlineStores. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeatureOnlineStoresResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureOnlineStoresResponse)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)` | A pageable sequence of [FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore) resources.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListFeatureOnlineStoresResponse, FeatureOnlineStore> response = featureOnlineStoreAdminServiceClient.ListFeatureOnlineStores(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FeatureOnlineStore item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeatureOnlineStoresResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureOnlineStore item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureOnlineStore> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureOnlineStore item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureOnlineStoresAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeatureOnlineStoresResponse, FeatureOnlineStore> ListFeatureOnlineStoresAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FeatureOnlineStores in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the Location to list FeatureOnlineStores. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeatureOnlineStoresResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureOnlineStoresResponse)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)` | A pageable asynchronous sequence of [FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore) resources.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListFeatureOnlineStoresResponse, FeatureOnlineStore> response = featureOnlineStoreAdminServiceClient.ListFeatureOnlineStoresAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FeatureOnlineStore item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeatureOnlineStoresResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureOnlineStore item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureOnlineStore> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureOnlineStore item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureOnlineStoresAsync(ListFeatureOnlineStoresRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeatureOnlineStoresResponse, FeatureOnlineStore> ListFeatureOnlineStoresAsync(ListFeatureOnlineStoresRequest request, CallSettings callSettings = null)

Lists FeatureOnlineStores in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureOnlineStoresRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureOnlineStoresRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeatureOnlineStoresResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureOnlineStoresResponse)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)` | A pageable asynchronous sequence of [FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore) resources.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListFeatureOnlineStoresRequest request = new ListFeatureOnlineStoresRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListFeatureOnlineStoresResponse, FeatureOnlineStore> response = featureOnlineStoreAdminServiceClient.ListFeatureOnlineStoresAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FeatureOnlineStore item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeatureOnlineStoresResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureOnlineStore item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureOnlineStore> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureOnlineStore item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureOnlineStoresAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeatureOnlineStoresResponse, FeatureOnlineStore> ListFeatureOnlineStoresAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FeatureOnlineStores in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to list FeatureOnlineStores. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeatureOnlineStoresResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureOnlineStoresResponse)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)` | A pageable asynchronous sequence of [FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore) resources.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListFeatureOnlineStoresResponse, FeatureOnlineStore> response = featureOnlineStoreAdminServiceClient.ListFeatureOnlineStoresAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FeatureOnlineStore item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeatureOnlineStoresResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureOnlineStore item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureOnlineStore> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureOnlineStore item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureViewSyncs(FeatureViewName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeatureViewSyncsResponse, FeatureViewSync> ListFeatureViewSyncs(FeatureViewName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FeatureViewSyncs in a given FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewName)`  
Required. The resource name of the FeatureView to list FeatureViewSyncs. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeatureViewSyncsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureViewSyncsResponse)[FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync)` | A pageable sequence of [FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync) resources.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    FeatureViewName parent = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]");
    // Make the request
    PagedEnumerable<ListFeatureViewSyncsResponse, FeatureViewSync> response = featureOnlineStoreAdminServiceClient.ListFeatureViewSyncs(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FeatureViewSync item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeatureViewSyncsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureViewSync item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureViewSync> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureViewSync item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureViewSyncs(ListFeatureViewSyncsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeatureViewSyncsResponse, FeatureViewSync> ListFeatureViewSyncs(ListFeatureViewSyncsRequest request, CallSettings callSettings = null)

Lists FeatureViewSyncs in a given FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureViewSyncsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureViewSyncsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeatureViewSyncsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureViewSyncsResponse)[FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync)` | A pageable sequence of [FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync) resources.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    ListFeatureViewSyncsRequest request = new ListFeatureViewSyncsRequest
    {
        ParentAsFeatureViewName = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListFeatureViewSyncsResponse, FeatureViewSync> response = featureOnlineStoreAdminServiceClient.ListFeatureViewSyncs(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FeatureViewSync item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeatureViewSyncsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureViewSync item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureViewSync> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureViewSync item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureViewSyncs(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeatureViewSyncsResponse, FeatureViewSync> ListFeatureViewSyncs(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FeatureViewSyncs in a given FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the FeatureView to list FeatureViewSyncs. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeatureViewSyncsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureViewSyncsResponse)[FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync)` | A pageable sequence of [FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync) resources.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]/featureViews/[FEATURE_VIEW]";
    // Make the request
    PagedEnumerable<ListFeatureViewSyncsResponse, FeatureViewSync> response = featureOnlineStoreAdminServiceClient.ListFeatureViewSyncs(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FeatureViewSync item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeatureViewSyncsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureViewSync item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureViewSync> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureViewSync item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureViewSyncsAsync(FeatureViewName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeatureViewSyncsResponse, FeatureViewSync> ListFeatureViewSyncsAsync(FeatureViewName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FeatureViewSyncs in a given FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewName)`  
Required. The resource name of the FeatureView to list FeatureViewSyncs. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeatureViewSyncsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureViewSyncsResponse)[FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync)` | A pageable asynchronous sequence of [FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync) resources.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureViewName parent = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]");
    // Make the request
    PagedAsyncEnumerable<ListFeatureViewSyncsResponse, FeatureViewSync> response = featureOnlineStoreAdminServiceClient.ListFeatureViewSyncsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FeatureViewSync item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeatureViewSyncsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureViewSync item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureViewSync> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureViewSync item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureViewSyncsAsync(ListFeatureViewSyncsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeatureViewSyncsResponse, FeatureViewSync> ListFeatureViewSyncsAsync(ListFeatureViewSyncsRequest request, CallSettings callSettings = null)

Lists FeatureViewSyncs in a given FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureViewSyncsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureViewSyncsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeatureViewSyncsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureViewSyncsResponse)[FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync)` | A pageable asynchronous sequence of [FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync) resources.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListFeatureViewSyncsRequest request = new ListFeatureViewSyncsRequest
    {
        ParentAsFeatureViewName = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListFeatureViewSyncsResponse, FeatureViewSync> response = featureOnlineStoreAdminServiceClient.ListFeatureViewSyncsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FeatureViewSync item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeatureViewSyncsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureViewSync item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureViewSync> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureViewSync item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureViewSyncsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeatureViewSyncsResponse, FeatureViewSync> ListFeatureViewSyncsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FeatureViewSyncs in a given FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the FeatureView to list FeatureViewSyncs. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeatureViewSyncsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureViewSyncsResponse)[FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync)` | A pageable asynchronous sequence of [FeatureViewSync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewSync) resources.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]/featureViews/[FEATURE_VIEW]";
    // Make the request
    PagedAsyncEnumerable<ListFeatureViewSyncsResponse, FeatureViewSync> response = featureOnlineStoreAdminServiceClient.ListFeatureViewSyncsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FeatureViewSync item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeatureViewSyncsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureViewSync item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureViewSync> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureViewSync item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureViews(FeatureOnlineStoreName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeatureViewsResponse, FeatureView> ListFeatureViews(FeatureOnlineStoreName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FeatureViews in a given FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureOnlineStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreName)`  
Required. The resource name of the FeatureOnlineStore to list FeatureViews. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeatureViewsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureViewsResponse)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)` | A pageable sequence of [FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView) resources.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    FeatureOnlineStoreName parent = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]");
    // Make the request
    PagedEnumerable<ListFeatureViewsResponse, FeatureView> response = featureOnlineStoreAdminServiceClient.ListFeatureViews(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FeatureView item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeatureViewsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureView item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureView> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureView item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureViews(ListFeatureViewsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeatureViewsResponse, FeatureView> ListFeatureViews(ListFeatureViewsRequest request, CallSettings callSettings = null)

Lists FeatureViews in a given FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureViewsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureViewsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeatureViewsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureViewsResponse)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)` | A pageable sequence of [FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView) resources.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    ListFeatureViewsRequest request = new ListFeatureViewsRequest
    {
        ParentAsFeatureOnlineStoreName = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListFeatureViewsResponse, FeatureView> response = featureOnlineStoreAdminServiceClient.ListFeatureViews(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FeatureView item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeatureViewsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureView item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureView> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureView item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureViews(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFeatureViewsResponse, FeatureView> ListFeatureViews(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FeatureViews in a given FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the FeatureOnlineStore to list FeatureViews. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFeatureViewsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureViewsResponse)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)` | A pageable sequence of [FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView) resources.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]";
    // Make the request
    PagedEnumerable<ListFeatureViewsResponse, FeatureView> response = featureOnlineStoreAdminServiceClient.ListFeatureViews(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (FeatureView item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListFeatureViewsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureView item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureView> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureView item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureViewsAsync(FeatureOnlineStoreName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeatureViewsResponse, FeatureView> ListFeatureViewsAsync(FeatureOnlineStoreName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FeatureViews in a given FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[FeatureOnlineStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreName)`  
Required. The resource name of the FeatureOnlineStore to list FeatureViews. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeatureViewsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureViewsResponse)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)` | A pageable asynchronous sequence of [FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView) resources.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureOnlineStoreName parent = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]");
    // Make the request
    PagedAsyncEnumerable<ListFeatureViewsResponse, FeatureView> response = featureOnlineStoreAdminServiceClient.ListFeatureViewsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FeatureView item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeatureViewsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureView item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureView> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureView item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureViewsAsync(ListFeatureViewsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeatureViewsResponse, FeatureView> ListFeatureViewsAsync(ListFeatureViewsRequest request, CallSettings callSettings = null)

Lists FeatureViews in a given FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureViewsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureViewsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeatureViewsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureViewsResponse)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)` | A pageable asynchronous sequence of [FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView) resources.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListFeatureViewsRequest request = new ListFeatureViewsRequest
    {
        ParentAsFeatureOnlineStoreName = FeatureOnlineStoreName.FromProjectLocationFeatureOnlineStore("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListFeatureViewsResponse, FeatureView> response = featureOnlineStoreAdminServiceClient.ListFeatureViewsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FeatureView item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeatureViewsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureView item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureView> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureView item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFeatureViewsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFeatureViewsResponse, FeatureView> ListFeatureViewsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists FeatureViews in a given FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the FeatureOnlineStore to list FeatureViews. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFeatureViewsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListFeatureViewsResponse)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)` | A pageable asynchronous sequence of [FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView) resources.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]";
    // Make the request
    PagedAsyncEnumerable<ListFeatureViewsResponse, FeatureView> response = featureOnlineStoreAdminServiceClient.ListFeatureViewsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (FeatureView item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListFeatureViewsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (FeatureView item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<FeatureView> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (FeatureView item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceCreateFeatureOnlineStore(string, CallSettings)
    
    
    public virtual Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata> PollOnceCreateFeatureOnlineStore(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateFeatureOnlineStore`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)[CreateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureOnlineStoreOperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateFeatureOnlineStoreAsync(string, CallSettings)
    
    
    public virtual Task<Operation<FeatureOnlineStore, CreateFeatureOnlineStoreOperationMetadata>> PollOnceCreateFeatureOnlineStoreAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateFeatureOnlineStore`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)[CreateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureOnlineStoreOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceCreateFeatureView(string, CallSettings)
    
    
    public virtual Operation<FeatureView, CreateFeatureViewOperationMetadata> PollOnceCreateFeatureView(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateFeatureView` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)[CreateFeatureViewOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureViewOperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateFeatureViewAsync(string, CallSettings)
    
    
    public virtual Task<Operation<FeatureView, CreateFeatureViewOperationMetadata>> PollOnceCreateFeatureViewAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateFeatureView`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)[CreateFeatureViewOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateFeatureViewOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteFeatureOnlineStore(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> PollOnceDeleteFeatureOnlineStore(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteFeatureOnlineStore`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteFeatureOnlineStoreAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> PollOnceDeleteFeatureOnlineStoreAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteFeatureOnlineStore`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteFeatureView(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> PollOnceDeleteFeatureView(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteFeatureView` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteFeatureViewAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> PollOnceDeleteFeatureViewAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteFeatureView`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateFeatureOnlineStore(string, CallSettings)
    
    
    public virtual Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> PollOnceUpdateFeatureOnlineStore(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateFeatureOnlineStore`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)[UpdateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureOnlineStoreOperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateFeatureOnlineStoreAsync(string, CallSettings)
    
    
    public virtual Task<Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata>> PollOnceUpdateFeatureOnlineStoreAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateFeatureOnlineStore`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)[UpdateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureOnlineStoreOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateFeatureView(string, CallSettings)
    
    
    public virtual Operation<FeatureView, UpdateFeatureViewOperationMetadata> PollOnceUpdateFeatureView(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateFeatureView` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)[UpdateFeatureViewOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureViewOperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateFeatureViewAsync(string, CallSettings)
    
    
    public virtual Task<Operation<FeatureView, UpdateFeatureViewOperationMetadata>> PollOnceUpdateFeatureViewAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateFeatureView`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)[UpdateFeatureViewOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureViewOperationMetadata)` | A task representing the result of polling the operation.  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminServiceClient#Google_Cloud_AIPlatform_V1_FeatureOnlineStoreAdminServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminServiceClient#Google_Cloud_AIPlatform_V1_FeatureOnlineStoreAdminServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminServiceClient#Google_Cloud_AIPlatform_V1_FeatureOnlineStoreAdminServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminServiceClient#Google_Cloud_AIPlatform_V1_FeatureOnlineStoreAdminServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### SyncFeatureView(FeatureViewName, CallSettings)
    
    
    public virtual SyncFeatureViewResponse SyncFeatureView(FeatureViewName featureView, CallSettings callSettings = null)

Triggers on-demand sync for the FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`featureView` | `[FeatureViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewName)`  
Required. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SyncFeatureViewResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SyncFeatureViewResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    FeatureViewName featureView = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]");
    // Make the request
    SyncFeatureViewResponse response = featureOnlineStoreAdminServiceClient.SyncFeatureView(featureView);
    

### SyncFeatureView(SyncFeatureViewRequest, CallSettings)
    
    
    public virtual SyncFeatureViewResponse SyncFeatureView(SyncFeatureViewRequest request, CallSettings callSettings = null)

Triggers on-demand sync for the FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SyncFeatureViewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SyncFeatureViewRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SyncFeatureViewResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SyncFeatureViewResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    SyncFeatureViewRequest request = new SyncFeatureViewRequest
    {
        FeatureViewAsFeatureViewName = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]"),
    };
    // Make the request
    SyncFeatureViewResponse response = featureOnlineStoreAdminServiceClient.SyncFeatureView(request);
    

### SyncFeatureView(string, CallSettings)
    
    
    public virtual SyncFeatureViewResponse SyncFeatureView(string featureView, CallSettings callSettings = null)

Triggers on-demand sync for the FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`featureView` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SyncFeatureViewResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SyncFeatureViewResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    string featureView = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]/featureViews/[FEATURE_VIEW]";
    // Make the request
    SyncFeatureViewResponse response = featureOnlineStoreAdminServiceClient.SyncFeatureView(featureView);
    

### SyncFeatureViewAsync(FeatureViewName, CallSettings)
    
    
    public virtual Task<SyncFeatureViewResponse> SyncFeatureViewAsync(FeatureViewName featureView, CallSettings callSettings = null)

Triggers on-demand sync for the FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`featureView` | `[FeatureViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewName)`  
Required. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SyncFeatureViewResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SyncFeatureViewResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureViewName featureView = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]");
    // Make the request
    SyncFeatureViewResponse response = await featureOnlineStoreAdminServiceClient.SyncFeatureViewAsync(featureView);
    

### SyncFeatureViewAsync(FeatureViewName, CancellationToken)
    
    
    public virtual Task<SyncFeatureViewResponse> SyncFeatureViewAsync(FeatureViewName featureView, CancellationToken cancellationToken)

Triggers on-demand sync for the FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`featureView` | `[FeatureViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureViewName)`  
Required. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SyncFeatureViewResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SyncFeatureViewResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureViewName featureView = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]");
    // Make the request
    SyncFeatureViewResponse response = await featureOnlineStoreAdminServiceClient.SyncFeatureViewAsync(featureView);
    

### SyncFeatureViewAsync(SyncFeatureViewRequest, CallSettings)
    
    
    public virtual Task<SyncFeatureViewResponse> SyncFeatureViewAsync(SyncFeatureViewRequest request, CallSettings callSettings = null)

Triggers on-demand sync for the FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SyncFeatureViewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SyncFeatureViewRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SyncFeatureViewResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SyncFeatureViewResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    SyncFeatureViewRequest request = new SyncFeatureViewRequest
    {
        FeatureViewAsFeatureViewName = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]"),
    };
    // Make the request
    SyncFeatureViewResponse response = await featureOnlineStoreAdminServiceClient.SyncFeatureViewAsync(request);
    

### SyncFeatureViewAsync(SyncFeatureViewRequest, CancellationToken)
    
    
    public virtual Task<SyncFeatureViewResponse> SyncFeatureViewAsync(SyncFeatureViewRequest request, CancellationToken cancellationToken)

Triggers on-demand sync for the FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SyncFeatureViewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SyncFeatureViewRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SyncFeatureViewResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SyncFeatureViewResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    SyncFeatureViewRequest request = new SyncFeatureViewRequest
    {
        FeatureViewAsFeatureViewName = FeatureViewName.FromProjectLocationFeatureOnlineStoreFeatureView("[PROJECT]", "[LOCATION]", "[FEATURE_ONLINE_STORE]", "[FEATURE_VIEW]"),
    };
    // Make the request
    SyncFeatureViewResponse response = await featureOnlineStoreAdminServiceClient.SyncFeatureViewAsync(request);
    

### SyncFeatureViewAsync(string, CallSettings)
    
    
    public virtual Task<SyncFeatureViewResponse> SyncFeatureViewAsync(string featureView, CallSettings callSettings = null)

Triggers on-demand sync for the FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`featureView` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SyncFeatureViewResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SyncFeatureViewResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    string featureView = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]/featureViews/[FEATURE_VIEW]";
    // Make the request
    SyncFeatureViewResponse response = await featureOnlineStoreAdminServiceClient.SyncFeatureViewAsync(featureView);
    

### SyncFeatureViewAsync(string, CancellationToken)
    
    
    public virtual Task<SyncFeatureViewResponse> SyncFeatureViewAsync(string featureView, CancellationToken cancellationToken)

Triggers on-demand sync for the FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`featureView` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SyncFeatureViewResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SyncFeatureViewResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    string featureView = "projects/[PROJECT]/locations/[LOCATION]/featureOnlineStores/[FEATURE_ONLINE_STORE]/featureViews/[FEATURE_VIEW]";
    // Make the request
    SyncFeatureViewResponse response = await featureOnlineStoreAdminServiceClient.SyncFeatureViewAsync(featureView);
    

### UpdateFeatureOnlineStore(FeatureOnlineStore, FieldMask, CallSettings)
    
    
    public virtual Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> UpdateFeatureOnlineStore(FeatureOnlineStore featureOnlineStore, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`featureOnlineStore` | `[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)`  
Required. The FeatureOnlineStore's `name` field is used to identify the FeatureOnlineStore to be updated. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the FeatureOnlineStore resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields:

  * `labels`
  * `description`
  * `bigtable`
  * `bigtable.auto_scaling`
  * `bigtable.enable_multi_region_replica`

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)[UpdateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureOnlineStoreOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    FeatureOnlineStore featureOnlineStore = new FeatureOnlineStore();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> response = featureOnlineStoreAdminServiceClient.UpdateFeatureOnlineStore(featureOnlineStore, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FeatureOnlineStore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> retrievedResponse = featureOnlineStoreAdminServiceClient.PollOnceUpdateFeatureOnlineStore(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureOnlineStore retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureOnlineStore(UpdateFeatureOnlineStoreRequest, CallSettings)
    
    
    public virtual Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> UpdateFeatureOnlineStore(UpdateFeatureOnlineStoreRequest request, CallSettings callSettings = null)

Updates the parameters of a single FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureOnlineStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureOnlineStoreRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)[UpdateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureOnlineStoreOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    UpdateFeatureOnlineStoreRequest request = new UpdateFeatureOnlineStoreRequest
    {
        FeatureOnlineStore = new FeatureOnlineStore(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> response = featureOnlineStoreAdminServiceClient.UpdateFeatureOnlineStore(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FeatureOnlineStore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> retrievedResponse = featureOnlineStoreAdminServiceClient.PollOnceUpdateFeatureOnlineStore(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureOnlineStore retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureOnlineStoreAsync(FeatureOnlineStore, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata>> UpdateFeatureOnlineStoreAsync(FeatureOnlineStore featureOnlineStore, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`featureOnlineStore` | `[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)`  
Required. The FeatureOnlineStore's `name` field is used to identify the FeatureOnlineStore to be updated. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the FeatureOnlineStore resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields:

  * `labels`
  * `description`
  * `bigtable`
  * `bigtable.auto_scaling`
  * `bigtable.enable_multi_region_replica`

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)[UpdateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureOnlineStoreOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureOnlineStore featureOnlineStore = new FeatureOnlineStore();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> response = await featureOnlineStoreAdminServiceClient.UpdateFeatureOnlineStoreAsync(featureOnlineStore, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureOnlineStore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceUpdateFeatureOnlineStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureOnlineStore retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureOnlineStoreAsync(FeatureOnlineStore, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata>> UpdateFeatureOnlineStoreAsync(FeatureOnlineStore featureOnlineStore, FieldMask updateMask, CancellationToken cancellationToken)

Updates the parameters of a single FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`featureOnlineStore` | `[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)`  
Required. The FeatureOnlineStore's `name` field is used to identify the FeatureOnlineStore to be updated. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the FeatureOnlineStore resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields:

  * `labels`
  * `description`
  * `bigtable`
  * `bigtable.auto_scaling`
  * `bigtable.enable_multi_region_replica`

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)[UpdateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureOnlineStoreOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureOnlineStore featureOnlineStore = new FeatureOnlineStore();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> response = await featureOnlineStoreAdminServiceClient.UpdateFeatureOnlineStoreAsync(featureOnlineStore, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureOnlineStore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceUpdateFeatureOnlineStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureOnlineStore retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureOnlineStoreAsync(UpdateFeatureOnlineStoreRequest, CallSettings)
    
    
    public virtual Task<Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata>> UpdateFeatureOnlineStoreAsync(UpdateFeatureOnlineStoreRequest request, CallSettings callSettings = null)

Updates the parameters of a single FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureOnlineStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureOnlineStoreRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)[UpdateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureOnlineStoreOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateFeatureOnlineStoreRequest request = new UpdateFeatureOnlineStoreRequest
    {
        FeatureOnlineStore = new FeatureOnlineStore(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> response = await featureOnlineStoreAdminServiceClient.UpdateFeatureOnlineStoreAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureOnlineStore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceUpdateFeatureOnlineStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureOnlineStore retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureOnlineStoreAsync(UpdateFeatureOnlineStoreRequest, CancellationToken)
    
    
    public virtual Task<Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata>> UpdateFeatureOnlineStoreAsync(UpdateFeatureOnlineStoreRequest request, CancellationToken cancellationToken)

Updates the parameters of a single FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureOnlineStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureOnlineStoreRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStore)[UpdateFeatureOnlineStoreOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureOnlineStoreOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateFeatureOnlineStoreRequest request = new UpdateFeatureOnlineStoreRequest
    {
        FeatureOnlineStore = new FeatureOnlineStore(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> response = await featureOnlineStoreAdminServiceClient.UpdateFeatureOnlineStoreAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureOnlineStore result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureOnlineStore, UpdateFeatureOnlineStoreOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceUpdateFeatureOnlineStoreAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureOnlineStore retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureView(FeatureView, FieldMask, CallSettings)
    
    
    public virtual Operation<FeatureView, UpdateFeatureViewOperationMetadata> UpdateFeatureView(FeatureView featureView, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`featureView` | `[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)`  
Required. The FeatureView's `name` field is used to identify the FeatureView to be updated. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the FeatureView resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields:

  * `labels`
  * `service_agent_type`
  * `big_query_source`
  * `big_query_source.uri`
  * `big_query_source.entity_id_columns`
  * `feature_registry_source`
  * `feature_registry_source.feature_groups`
  * `sync_config`
  * `sync_config.cron`
  * `optimized_config.automatic_resources`

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)[UpdateFeatureViewOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureViewOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    FeatureView featureView = new FeatureView();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FeatureView, UpdateFeatureViewOperationMetadata> response = featureOnlineStoreAdminServiceClient.UpdateFeatureView(featureView, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureView, UpdateFeatureViewOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FeatureView result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureView, UpdateFeatureViewOperationMetadata> retrievedResponse = featureOnlineStoreAdminServiceClient.PollOnceUpdateFeatureView(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureView retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureView(UpdateFeatureViewRequest, CallSettings)
    
    
    public virtual Operation<FeatureView, UpdateFeatureViewOperationMetadata> UpdateFeatureView(UpdateFeatureViewRequest request, CallSettings callSettings = null)

Updates the parameters of a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureViewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureViewRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)[UpdateFeatureViewOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureViewOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = FeatureOnlineStoreAdminServiceClient.Create();
    // Initialize request argument(s)
    UpdateFeatureViewRequest request = new UpdateFeatureViewRequest
    {
        FeatureView = new FeatureView(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<FeatureView, UpdateFeatureViewOperationMetadata> response = featureOnlineStoreAdminServiceClient.UpdateFeatureView(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureView, UpdateFeatureViewOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    FeatureView result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureView, UpdateFeatureViewOperationMetadata> retrievedResponse = featureOnlineStoreAdminServiceClient.PollOnceUpdateFeatureView(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureView retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureViewAsync(FeatureView, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<FeatureView, UpdateFeatureViewOperationMetadata>> UpdateFeatureViewAsync(FeatureView featureView, FieldMask updateMask, CallSettings callSettings = null)

Updates the parameters of a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`featureView` | `[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)`  
Required. The FeatureView's `name` field is used to identify the FeatureView to be updated. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the FeatureView resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields:

  * `labels`
  * `service_agent_type`
  * `big_query_source`
  * `big_query_source.uri`
  * `big_query_source.entity_id_columns`
  * `feature_registry_source`
  * `feature_registry_source.feature_groups`
  * `sync_config`
  * `sync_config.cron`
  * `optimized_config.automatic_resources`

  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)[UpdateFeatureViewOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureViewOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureView featureView = new FeatureView();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FeatureView, UpdateFeatureViewOperationMetadata> response = await featureOnlineStoreAdminServiceClient.UpdateFeatureViewAsync(featureView, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureView, UpdateFeatureViewOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureView result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureView, UpdateFeatureViewOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceUpdateFeatureViewAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureView retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureViewAsync(FeatureView, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<FeatureView, UpdateFeatureViewOperationMetadata>> UpdateFeatureViewAsync(FeatureView featureView, FieldMask updateMask, CancellationToken cancellationToken)

Updates the parameters of a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`featureView` | `[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)`  
Required. The FeatureView's `name` field is used to identify the FeatureView to be updated. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask is used to specify the fields to be overwritten in the FeatureView resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields:

  * `labels`
  * `service_agent_type`
  * `big_query_source`
  * `big_query_source.uri`
  * `big_query_source.entity_id_columns`
  * `feature_registry_source`
  * `feature_registry_source.feature_groups`
  * `sync_config`
  * `sync_config.cron`
  * `optimized_config.automatic_resources`

  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)[UpdateFeatureViewOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureViewOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    FeatureView featureView = new FeatureView();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<FeatureView, UpdateFeatureViewOperationMetadata> response = await featureOnlineStoreAdminServiceClient.UpdateFeatureViewAsync(featureView, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureView, UpdateFeatureViewOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureView result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureView, UpdateFeatureViewOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceUpdateFeatureViewAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureView retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureViewAsync(UpdateFeatureViewRequest, CallSettings)
    
    
    public virtual Task<Operation<FeatureView, UpdateFeatureViewOperationMetadata>> UpdateFeatureViewAsync(UpdateFeatureViewRequest request, CallSettings callSettings = null)

Updates the parameters of a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureViewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureViewRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)[UpdateFeatureViewOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureViewOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateFeatureViewRequest request = new UpdateFeatureViewRequest
    {
        FeatureView = new FeatureView(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<FeatureView, UpdateFeatureViewOperationMetadata> response = await featureOnlineStoreAdminServiceClient.UpdateFeatureViewAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureView, UpdateFeatureViewOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureView result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureView, UpdateFeatureViewOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceUpdateFeatureViewAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureView retrievedResult = retrievedResponse.Result;
    }
    

### UpdateFeatureViewAsync(UpdateFeatureViewRequest, CancellationToken)
    
    
    public virtual Task<Operation<FeatureView, UpdateFeatureViewOperationMetadata>> UpdateFeatureViewAsync(UpdateFeatureViewRequest request, CancellationToken cancellationToken)

Updates the parameters of a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureViewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureViewRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[FeatureView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureView)[UpdateFeatureViewOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateFeatureViewOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    FeatureOnlineStoreAdminServiceClient featureOnlineStoreAdminServiceClient = await FeatureOnlineStoreAdminServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateFeatureViewRequest request = new UpdateFeatureViewRequest
    {
        FeatureView = new FeatureView(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<FeatureView, UpdateFeatureViewOperationMetadata> response = await featureOnlineStoreAdminServiceClient.UpdateFeatureViewAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<FeatureView, UpdateFeatureViewOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    FeatureView result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<FeatureView, UpdateFeatureViewOperationMetadata> retrievedResponse = await featureOnlineStoreAdminServiceClient.PollOnceUpdateFeatureViewAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        FeatureView retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
