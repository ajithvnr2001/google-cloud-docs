---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationServiceClient
title: Vertex AI v1beta1 API - Class MigrationServiceClient (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:31:42.576749+00:00
---

# Vertex AI v1beta1 API - Class MigrationServiceClient (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class MigrationServiceClient (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public abstract class MigrationServiceClient

Reference documentation and code samples for the Vertex AI v1beta1 API class MigrationServiceClient.

MigrationService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > MigrationServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[MigrationServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationServiceClientImpl)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Remarks

A service that migrates resources from automl.googleapis.com, datalabeling.googleapis.com and ml.googleapis.com to Vertex AI.

## Properties 

### BatchMigrateResourcesOperationsClient
    
    
    public virtual OperationsClient BatchMigrateResourcesOperationsClient { get; }

The long-running operations client for `BatchMigrateResources`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the MigrationService service, which is a host of "aiplatform.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default MigrationService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default MigrationService scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual MigrationService.MigrationServiceClient GrpcClient { get; }

The underlying gRPC MigrationService client

**Property Value**  
---  
**Type** | **Description**  
`[MigrationService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationService)[MigrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationService.MigrationServiceClient)` |   
  
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
  
## Methods 

### BatchMigrateResources(LocationName, IEnumerable<MigrateResourceRequest>, CallSettings)
    
    
    public virtual Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> BatchMigrateResources(LocationName parent, IEnumerable<MigrateResourceRequest> migrateResourceRequests, CallSettings callSettings = null)

Batch migrates resources from ml.googleapis.com, automl.googleapis.com, and datalabeling.googleapis.com to Vertex AI.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location of the migrated resource will live in. Format: `projects/{project}/locations/{location}`  
`migrateResourceRequests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[MigrateResourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrateResourceRequest)`  
Required. The request messages specifying the resources to migrate. They must be in the same location as the destination. Up to 50 resources can be migrated in one batch.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchMigrateResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesResponse)[BatchMigrateResourcesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    MigrationServiceClient migrationServiceClient = MigrationServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    IEnumerable<MigrateResourceRequest> migrateResourceRequests = new MigrateResourceRequest[]
    {
        new MigrateResourceRequest(),
    };
    // Make the request
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> response = migrationServiceClient.BatchMigrateResources(parent, migrateResourceRequests);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    BatchMigrateResourcesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> retrievedResponse = migrationServiceClient.PollOnceBatchMigrateResources(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchMigrateResourcesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchMigrateResources(BatchMigrateResourcesRequest, CallSettings)
    
    
    public virtual Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> BatchMigrateResources(BatchMigrateResourcesRequest request, CallSettings callSettings = null)

Batch migrates resources from ml.googleapis.com, automl.googleapis.com, and datalabeling.googleapis.com to Vertex AI.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchMigrateResourcesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchMigrateResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesResponse)[BatchMigrateResourcesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    MigrationServiceClient migrationServiceClient = MigrationServiceClient.Create();
    // Initialize request argument(s)
    BatchMigrateResourcesRequest request = new BatchMigrateResourcesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        MigrateResourceRequests =
        {
            new MigrateResourceRequest(),
        },
    };
    // Make the request
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> response = migrationServiceClient.BatchMigrateResources(request);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    BatchMigrateResourcesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> retrievedResponse = migrationServiceClient.PollOnceBatchMigrateResources(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchMigrateResourcesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchMigrateResources(string, IEnumerable<MigrateResourceRequest>, CallSettings)
    
    
    public virtual Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> BatchMigrateResources(string parent, IEnumerable<MigrateResourceRequest> migrateResourceRequests, CallSettings callSettings = null)

Batch migrates resources from ml.googleapis.com, automl.googleapis.com, and datalabeling.googleapis.com to Vertex AI.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location of the migrated resource will live in. Format: `projects/{project}/locations/{location}`  
`migrateResourceRequests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[MigrateResourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrateResourceRequest)`  
Required. The request messages specifying the resources to migrate. They must be in the same location as the destination. Up to 50 resources can be migrated in one batch.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchMigrateResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesResponse)[BatchMigrateResourcesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    MigrationServiceClient migrationServiceClient = MigrationServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    IEnumerable<MigrateResourceRequest> migrateResourceRequests = new MigrateResourceRequest[]
    {
        new MigrateResourceRequest(),
    };
    // Make the request
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> response = migrationServiceClient.BatchMigrateResources(parent, migrateResourceRequests);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    BatchMigrateResourcesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> retrievedResponse = migrationServiceClient.PollOnceBatchMigrateResources(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchMigrateResourcesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchMigrateResourcesAsync(LocationName, IEnumerable<MigrateResourceRequest>, CallSettings)
    
    
    public virtual Task<Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata>> BatchMigrateResourcesAsync(LocationName parent, IEnumerable<MigrateResourceRequest> migrateResourceRequests, CallSettings callSettings = null)

Batch migrates resources from ml.googleapis.com, automl.googleapis.com, and datalabeling.googleapis.com to Vertex AI.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location of the migrated resource will live in. Format: `projects/{project}/locations/{location}`  
`migrateResourceRequests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[MigrateResourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrateResourceRequest)`  
Required. The request messages specifying the resources to migrate. They must be in the same location as the destination. Up to 50 resources can be migrated in one batch.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchMigrateResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesResponse)[BatchMigrateResourcesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    MigrationServiceClient migrationServiceClient = await MigrationServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    IEnumerable<MigrateResourceRequest> migrateResourceRequests = new MigrateResourceRequest[]
    {
        new MigrateResourceRequest(),
    };
    // Make the request
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> response = await migrationServiceClient.BatchMigrateResourcesAsync(parent, migrateResourceRequests);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchMigrateResourcesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> retrievedResponse = await migrationServiceClient.PollOnceBatchMigrateResourcesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchMigrateResourcesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchMigrateResourcesAsync(LocationName, IEnumerable<MigrateResourceRequest>, CancellationToken)
    
    
    public virtual Task<Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata>> BatchMigrateResourcesAsync(LocationName parent, IEnumerable<MigrateResourceRequest> migrateResourceRequests, CancellationToken cancellationToken)

Batch migrates resources from ml.googleapis.com, automl.googleapis.com, and datalabeling.googleapis.com to Vertex AI.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location of the migrated resource will live in. Format: `projects/{project}/locations/{location}`  
`migrateResourceRequests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[MigrateResourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrateResourceRequest)`  
Required. The request messages specifying the resources to migrate. They must be in the same location as the destination. Up to 50 resources can be migrated in one batch.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchMigrateResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesResponse)[BatchMigrateResourcesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    MigrationServiceClient migrationServiceClient = await MigrationServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    IEnumerable<MigrateResourceRequest> migrateResourceRequests = new MigrateResourceRequest[]
    {
        new MigrateResourceRequest(),
    };
    // Make the request
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> response = await migrationServiceClient.BatchMigrateResourcesAsync(parent, migrateResourceRequests);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchMigrateResourcesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> retrievedResponse = await migrationServiceClient.PollOnceBatchMigrateResourcesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchMigrateResourcesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchMigrateResourcesAsync(BatchMigrateResourcesRequest, CallSettings)
    
    
    public virtual Task<Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata>> BatchMigrateResourcesAsync(BatchMigrateResourcesRequest request, CallSettings callSettings = null)

Batch migrates resources from ml.googleapis.com, automl.googleapis.com, and datalabeling.googleapis.com to Vertex AI.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchMigrateResourcesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchMigrateResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesResponse)[BatchMigrateResourcesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    MigrationServiceClient migrationServiceClient = await MigrationServiceClient.CreateAsync();
    // Initialize request argument(s)
    BatchMigrateResourcesRequest request = new BatchMigrateResourcesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        MigrateResourceRequests =
        {
            new MigrateResourceRequest(),
        },
    };
    // Make the request
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> response = await migrationServiceClient.BatchMigrateResourcesAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchMigrateResourcesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> retrievedResponse = await migrationServiceClient.PollOnceBatchMigrateResourcesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchMigrateResourcesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchMigrateResourcesAsync(BatchMigrateResourcesRequest, CancellationToken)
    
    
    public virtual Task<Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata>> BatchMigrateResourcesAsync(BatchMigrateResourcesRequest request, CancellationToken cancellationToken)

Batch migrates resources from ml.googleapis.com, automl.googleapis.com, and datalabeling.googleapis.com to Vertex AI.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchMigrateResourcesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchMigrateResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesResponse)[BatchMigrateResourcesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    MigrationServiceClient migrationServiceClient = await MigrationServiceClient.CreateAsync();
    // Initialize request argument(s)
    BatchMigrateResourcesRequest request = new BatchMigrateResourcesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        MigrateResourceRequests =
        {
            new MigrateResourceRequest(),
        },
    };
    // Make the request
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> response = await migrationServiceClient.BatchMigrateResourcesAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchMigrateResourcesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> retrievedResponse = await migrationServiceClient.PollOnceBatchMigrateResourcesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchMigrateResourcesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchMigrateResourcesAsync(string, IEnumerable<MigrateResourceRequest>, CallSettings)
    
    
    public virtual Task<Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata>> BatchMigrateResourcesAsync(string parent, IEnumerable<MigrateResourceRequest> migrateResourceRequests, CallSettings callSettings = null)

Batch migrates resources from ml.googleapis.com, automl.googleapis.com, and datalabeling.googleapis.com to Vertex AI.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location of the migrated resource will live in. Format: `projects/{project}/locations/{location}`  
`migrateResourceRequests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[MigrateResourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrateResourceRequest)`  
Required. The request messages specifying the resources to migrate. They must be in the same location as the destination. Up to 50 resources can be migrated in one batch.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchMigrateResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesResponse)[BatchMigrateResourcesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    MigrationServiceClient migrationServiceClient = await MigrationServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    IEnumerable<MigrateResourceRequest> migrateResourceRequests = new MigrateResourceRequest[]
    {
        new MigrateResourceRequest(),
    };
    // Make the request
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> response = await migrationServiceClient.BatchMigrateResourcesAsync(parent, migrateResourceRequests);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchMigrateResourcesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> retrievedResponse = await migrationServiceClient.PollOnceBatchMigrateResourcesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchMigrateResourcesResponse retrievedResult = retrievedResponse.Result;
    }
    

### BatchMigrateResourcesAsync(string, IEnumerable<MigrateResourceRequest>, CancellationToken)
    
    
    public virtual Task<Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata>> BatchMigrateResourcesAsync(string parent, IEnumerable<MigrateResourceRequest> migrateResourceRequests, CancellationToken cancellationToken)

Batch migrates resources from ml.googleapis.com, automl.googleapis.com, and datalabeling.googleapis.com to Vertex AI.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location of the migrated resource will live in. Format: `projects/{project}/locations/{location}`  
`migrateResourceRequests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[MigrateResourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrateResourceRequest)`  
Required. The request messages specifying the resources to migrate. They must be in the same location as the destination. Up to 50 resources can be migrated in one batch.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchMigrateResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesResponse)[BatchMigrateResourcesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    MigrationServiceClient migrationServiceClient = await MigrationServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    IEnumerable<MigrateResourceRequest> migrateResourceRequests = new MigrateResourceRequest[]
    {
        new MigrateResourceRequest(),
    };
    // Make the request
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> response = await migrationServiceClient.BatchMigrateResourcesAsync(parent, migrateResourceRequests);
    
    // Poll until the returned long-running operation is complete
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    BatchMigrateResourcesResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> retrievedResponse = await migrationServiceClient.PollOnceBatchMigrateResourcesAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        BatchMigrateResourcesResponse retrievedResult = retrievedResponse.Result;
    }
    

### Create()
    
    
    public static MigrationServiceClient Create()

Synchronously creates a [MigrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [MigrationServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[MigrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationServiceClient)` | The created [MigrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<MigrationServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [MigrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [MigrationServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MigrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationServiceClient)` | The task representing the created [MigrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationServiceClient).  
  
### PollOnceBatchMigrateResources(string, CallSettings)
    
    
    public virtual Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata> PollOnceBatchMigrateResources(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `BatchMigrateResources` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchMigrateResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesResponse)[BatchMigrateResourcesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesOperationMetadata)` | The result of polling the operation.  
  
### PollOnceBatchMigrateResourcesAsync(string, CallSettings)
    
    
    public virtual Task<Operation<BatchMigrateResourcesResponse, BatchMigrateResourcesOperationMetadata>> PollOnceBatchMigrateResourcesAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `BatchMigrateResources`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[BatchMigrateResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesResponse)[BatchMigrateResourcesOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.BatchMigrateResourcesOperationMetadata)` | A task representing the result of polling the operation.  
  
### SearchMigratableResources(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<SearchMigratableResourcesResponse, MigratableResource> SearchMigratableResources(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Searches all of the resources in automl.googleapis.com, datalabeling.googleapis.com and ml.googleapis.com that can be migrated to Vertex AI's given location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location that the migratable resources should be searched from. It's the Vertex AI location that the resources can be migrated to, not the resources' original location. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SearchMigratableResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SearchMigratableResourcesResponse)[MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource)` | A pageable sequence of [MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource) resources.  
**Example**
    
    
    // Create client
    MigrationServiceClient migrationServiceClient = MigrationServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<SearchMigratableResourcesResponse, MigratableResource> response = migrationServiceClient.SearchMigratableResources(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (MigratableResource item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SearchMigratableResourcesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MigratableResource item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MigratableResource> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MigratableResource item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchMigratableResources(SearchMigratableResourcesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<SearchMigratableResourcesResponse, MigratableResource> SearchMigratableResources(SearchMigratableResourcesRequest request, CallSettings callSettings = null)

Searches all of the resources in automl.googleapis.com, datalabeling.googleapis.com and ml.googleapis.com that can be migrated to Vertex AI's given location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchMigratableResourcesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SearchMigratableResourcesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SearchMigratableResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SearchMigratableResourcesResponse)[MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource)` | A pageable sequence of [MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource) resources.  
**Example**
    
    
    // Create client
    MigrationServiceClient migrationServiceClient = MigrationServiceClient.Create();
    // Initialize request argument(s)
    SearchMigratableResourcesRequest request = new SearchMigratableResourcesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<SearchMigratableResourcesResponse, MigratableResource> response = migrationServiceClient.SearchMigratableResources(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (MigratableResource item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SearchMigratableResourcesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MigratableResource item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MigratableResource> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MigratableResource item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchMigratableResources(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<SearchMigratableResourcesResponse, MigratableResource> SearchMigratableResources(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Searches all of the resources in automl.googleapis.com, datalabeling.googleapis.com and ml.googleapis.com that can be migrated to Vertex AI's given location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location that the migratable resources should be searched from. It's the Vertex AI location that the resources can be migrated to, not the resources' original location. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[SearchMigratableResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SearchMigratableResourcesResponse)[MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource)` | A pageable sequence of [MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource) resources.  
**Example**
    
    
    // Create client
    MigrationServiceClient migrationServiceClient = MigrationServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<SearchMigratableResourcesResponse, MigratableResource> response = migrationServiceClient.SearchMigratableResources(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (MigratableResource item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (SearchMigratableResourcesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MigratableResource item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MigratableResource> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MigratableResource item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchMigratableResourcesAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SearchMigratableResourcesResponse, MigratableResource> SearchMigratableResourcesAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Searches all of the resources in automl.googleapis.com, datalabeling.googleapis.com and ml.googleapis.com that can be migrated to Vertex AI's given location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The location that the migratable resources should be searched from. It's the Vertex AI location that the resources can be migrated to, not the resources' original location. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SearchMigratableResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SearchMigratableResourcesResponse)[MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource)` | A pageable asynchronous sequence of [MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource) resources.  
**Example**
    
    
    // Create client
    MigrationServiceClient migrationServiceClient = await MigrationServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<SearchMigratableResourcesResponse, MigratableResource> response = migrationServiceClient.SearchMigratableResourcesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (MigratableResource item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SearchMigratableResourcesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MigratableResource item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MigratableResource> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MigratableResource item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchMigratableResourcesAsync(SearchMigratableResourcesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SearchMigratableResourcesResponse, MigratableResource> SearchMigratableResourcesAsync(SearchMigratableResourcesRequest request, CallSettings callSettings = null)

Searches all of the resources in automl.googleapis.com, datalabeling.googleapis.com and ml.googleapis.com that can be migrated to Vertex AI's given location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchMigratableResourcesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SearchMigratableResourcesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SearchMigratableResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SearchMigratableResourcesResponse)[MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource)` | A pageable asynchronous sequence of [MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource) resources.  
**Example**
    
    
    // Create client
    MigrationServiceClient migrationServiceClient = await MigrationServiceClient.CreateAsync();
    // Initialize request argument(s)
    SearchMigratableResourcesRequest request = new SearchMigratableResourcesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<SearchMigratableResourcesResponse, MigratableResource> response = migrationServiceClient.SearchMigratableResourcesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (MigratableResource item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SearchMigratableResourcesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MigratableResource item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MigratableResource> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MigratableResource item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchMigratableResourcesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<SearchMigratableResourcesResponse, MigratableResource> SearchMigratableResourcesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Searches all of the resources in automl.googleapis.com, datalabeling.googleapis.com and ml.googleapis.com that can be migrated to Vertex AI's given location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The location that the migratable resources should be searched from. It's the Vertex AI location that the resources can be migrated to, not the resources' original location. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[SearchMigratableResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SearchMigratableResourcesResponse)[MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource)` | A pageable asynchronous sequence of [MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource) resources.  
**Example**
    
    
    // Create client
    MigrationServiceClient migrationServiceClient = await MigrationServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<SearchMigratableResourcesResponse, MigratableResource> response = migrationServiceClient.SearchMigratableResourcesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (MigratableResource item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (SearchMigratableResourcesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (MigratableResource item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<MigratableResource> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (MigratableResource item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationServiceClient#Google_Cloud_AIPlatform_V1Beta1_MigrationServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationServiceClient#Google_Cloud_AIPlatform_V1Beta1_MigrationServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationServiceClient#Google_Cloud_AIPlatform_V1Beta1_MigrationServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationServiceClient#Google_Cloud_AIPlatform_V1Beta1_MigrationServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
