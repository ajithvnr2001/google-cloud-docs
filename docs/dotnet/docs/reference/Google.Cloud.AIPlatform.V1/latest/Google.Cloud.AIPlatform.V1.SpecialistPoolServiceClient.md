---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolServiceClient
title: Vertex AI v1 API - Class SpecialistPoolServiceClient (3.77.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:38.531053+00:00
---

# Vertex AI v1 API - Class SpecialistPoolServiceClient (3.77.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1 API - Class SpecialistPoolServiceClient (3.77.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.77.0 (latest)  3.76.0  3.75.0  3.74.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public abstract class SpecialistPoolServiceClient

Reference documentation and code samples for the Vertex AI v1 API class SpecialistPoolServiceClient.

SpecialistPoolService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SpecialistPoolServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[SpecialistPoolServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolServiceClientImpl)

## Namespace

[Google.Cloud.AIPlatform.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1)

## Assembly

Google.Cloud.AIPlatform.V1.dll

## Remarks

A service for creating and managing Customer SpecialistPools. When customers start Data Labeling jobs, they can reuse/create Specialist Pools to bring their own Specialists to label the data. Customers can add/remove Managers for the Specialist Pool on Cloud console, then Managers will get email notifications to manage Specialists and tasks on CrowdCompute console.

## Properties 

### CreateSpecialistPoolOperationsClient
    
    
    public virtual OperationsClient CreateSpecialistPoolOperationsClient { get; }

The long-running operations client for `CreateSpecialistPool`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the SpecialistPoolService service, which is a host of "aiplatform.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default SpecialistPoolService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default SpecialistPoolService scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteSpecialistPoolOperationsClient
    
    
    public virtual OperationsClient DeleteSpecialistPoolOperationsClient { get; }

The long-running operations client for `DeleteSpecialistPool`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual SpecialistPoolService.SpecialistPoolServiceClient GrpcClient { get; }

The underlying gRPC SpecialistPoolService client

**Property Value**  
---  
**Type** | **Description**  
`[SpecialistPoolService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolService)[SpecialistPoolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolService.SpecialistPoolServiceClient)` |   
  
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
  
### UpdateSpecialistPoolOperationsClient
    
    
    public virtual OperationsClient UpdateSpecialistPoolOperationsClient { get; }

The long-running operations client for `UpdateSpecialistPool`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### Create()
    
    
    public static SpecialistPoolServiceClient Create()

Synchronously creates a [SpecialistPoolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [SpecialistPoolServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[SpecialistPoolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolServiceClient)` | The created [SpecialistPoolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<SpecialistPoolServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [SpecialistPoolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [SpecialistPoolServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SpecialistPoolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolServiceClient)` | The task representing the created [SpecialistPoolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolServiceClient).  
  
### CreateSpecialistPool(LocationName, SpecialistPool, CallSettings)
    
    
    public virtual Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> CreateSpecialistPool(LocationName parent, SpecialistPool specialistPool, CallSettings callSettings = null)

Creates a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent Project name for the new SpecialistPool. The form is `projects/{project}/locations/{location}`.  
`specialistPool` | `[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)`  
Required. The SpecialistPool to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)[CreateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateSpecialistPoolOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = SpecialistPoolServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    SpecialistPool specialistPool = new SpecialistPool();
    // Make the request
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> response = specialistPoolServiceClient.CreateSpecialistPool(parent, specialistPool);
    
    // Poll until the returned long-running operation is complete
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    SpecialistPool result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> retrievedResponse = specialistPoolServiceClient.PollOnceCreateSpecialistPool(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        SpecialistPool retrievedResult = retrievedResponse.Result;
    }
    

### CreateSpecialistPool(CreateSpecialistPoolRequest, CallSettings)
    
    
    public virtual Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> CreateSpecialistPool(CreateSpecialistPoolRequest request, CallSettings callSettings = null)

Creates a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSpecialistPoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateSpecialistPoolRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)[CreateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateSpecialistPoolOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = SpecialistPoolServiceClient.Create();
    // Initialize request argument(s)
    CreateSpecialistPoolRequest request = new CreateSpecialistPoolRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        SpecialistPool = new SpecialistPool(),
    };
    // Make the request
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> response = specialistPoolServiceClient.CreateSpecialistPool(request);
    
    // Poll until the returned long-running operation is complete
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    SpecialistPool result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> retrievedResponse = specialistPoolServiceClient.PollOnceCreateSpecialistPool(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        SpecialistPool retrievedResult = retrievedResponse.Result;
    }
    

### CreateSpecialistPool(string, SpecialistPool, CallSettings)
    
    
    public virtual Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> CreateSpecialistPool(string parent, SpecialistPool specialistPool, CallSettings callSettings = null)

Creates a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent Project name for the new SpecialistPool. The form is `projects/{project}/locations/{location}`.  
`specialistPool` | `[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)`  
Required. The SpecialistPool to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)[CreateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateSpecialistPoolOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = SpecialistPoolServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    SpecialistPool specialistPool = new SpecialistPool();
    // Make the request
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> response = specialistPoolServiceClient.CreateSpecialistPool(parent, specialistPool);
    
    // Poll until the returned long-running operation is complete
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    SpecialistPool result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> retrievedResponse = specialistPoolServiceClient.PollOnceCreateSpecialistPool(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        SpecialistPool retrievedResult = retrievedResponse.Result;
    }
    

### CreateSpecialistPoolAsync(LocationName, SpecialistPool, CallSettings)
    
    
    public virtual Task<Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata>> CreateSpecialistPoolAsync(LocationName parent, SpecialistPool specialistPool, CallSettings callSettings = null)

Creates a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent Project name for the new SpecialistPool. The form is `projects/{project}/locations/{location}`.  
`specialistPool` | `[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)`  
Required. The SpecialistPool to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)[CreateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateSpecialistPoolOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    SpecialistPool specialistPool = new SpecialistPool();
    // Make the request
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> response = await specialistPoolServiceClient.CreateSpecialistPoolAsync(parent, specialistPool);
    
    // Poll until the returned long-running operation is complete
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    SpecialistPool result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> retrievedResponse = await specialistPoolServiceClient.PollOnceCreateSpecialistPoolAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        SpecialistPool retrievedResult = retrievedResponse.Result;
    }
    

### CreateSpecialistPoolAsync(LocationName, SpecialistPool, CancellationToken)
    
    
    public virtual Task<Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata>> CreateSpecialistPoolAsync(LocationName parent, SpecialistPool specialistPool, CancellationToken cancellationToken)

Creates a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent Project name for the new SpecialistPool. The form is `projects/{project}/locations/{location}`.  
`specialistPool` | `[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)`  
Required. The SpecialistPool to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)[CreateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateSpecialistPoolOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    SpecialistPool specialistPool = new SpecialistPool();
    // Make the request
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> response = await specialistPoolServiceClient.CreateSpecialistPoolAsync(parent, specialistPool);
    
    // Poll until the returned long-running operation is complete
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    SpecialistPool result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> retrievedResponse = await specialistPoolServiceClient.PollOnceCreateSpecialistPoolAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        SpecialistPool retrievedResult = retrievedResponse.Result;
    }
    

### CreateSpecialistPoolAsync(CreateSpecialistPoolRequest, CallSettings)
    
    
    public virtual Task<Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata>> CreateSpecialistPoolAsync(CreateSpecialistPoolRequest request, CallSettings callSettings = null)

Creates a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSpecialistPoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateSpecialistPoolRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)[CreateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateSpecialistPoolOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateSpecialistPoolRequest request = new CreateSpecialistPoolRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        SpecialistPool = new SpecialistPool(),
    };
    // Make the request
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> response = await specialistPoolServiceClient.CreateSpecialistPoolAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    SpecialistPool result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> retrievedResponse = await specialistPoolServiceClient.PollOnceCreateSpecialistPoolAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        SpecialistPool retrievedResult = retrievedResponse.Result;
    }
    

### CreateSpecialistPoolAsync(CreateSpecialistPoolRequest, CancellationToken)
    
    
    public virtual Task<Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata>> CreateSpecialistPoolAsync(CreateSpecialistPoolRequest request, CancellationToken cancellationToken)

Creates a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSpecialistPoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateSpecialistPoolRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)[CreateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateSpecialistPoolOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateSpecialistPoolRequest request = new CreateSpecialistPoolRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        SpecialistPool = new SpecialistPool(),
    };
    // Make the request
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> response = await specialistPoolServiceClient.CreateSpecialistPoolAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    SpecialistPool result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> retrievedResponse = await specialistPoolServiceClient.PollOnceCreateSpecialistPoolAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        SpecialistPool retrievedResult = retrievedResponse.Result;
    }
    

### CreateSpecialistPoolAsync(string, SpecialistPool, CallSettings)
    
    
    public virtual Task<Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata>> CreateSpecialistPoolAsync(string parent, SpecialistPool specialistPool, CallSettings callSettings = null)

Creates a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent Project name for the new SpecialistPool. The form is `projects/{project}/locations/{location}`.  
`specialistPool` | `[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)`  
Required. The SpecialistPool to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)[CreateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateSpecialistPoolOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    SpecialistPool specialistPool = new SpecialistPool();
    // Make the request
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> response = await specialistPoolServiceClient.CreateSpecialistPoolAsync(parent, specialistPool);
    
    // Poll until the returned long-running operation is complete
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    SpecialistPool result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> retrievedResponse = await specialistPoolServiceClient.PollOnceCreateSpecialistPoolAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        SpecialistPool retrievedResult = retrievedResponse.Result;
    }
    

### CreateSpecialistPoolAsync(string, SpecialistPool, CancellationToken)
    
    
    public virtual Task<Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata>> CreateSpecialistPoolAsync(string parent, SpecialistPool specialistPool, CancellationToken cancellationToken)

Creates a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent Project name for the new SpecialistPool. The form is `projects/{project}/locations/{location}`.  
`specialistPool` | `[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)`  
Required. The SpecialistPool to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)[CreateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateSpecialistPoolOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    SpecialistPool specialistPool = new SpecialistPool();
    // Make the request
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> response = await specialistPoolServiceClient.CreateSpecialistPoolAsync(parent, specialistPool);
    
    // Poll until the returned long-running operation is complete
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    SpecialistPool result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> retrievedResponse = await specialistPoolServiceClient.PollOnceCreateSpecialistPoolAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        SpecialistPool retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSpecialistPool(DeleteSpecialistPoolRequest, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteSpecialistPool(DeleteSpecialistPoolRequest request, CallSettings callSettings = null)

Deletes a SpecialistPool as well as all Specialists in the pool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSpecialistPoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteSpecialistPoolRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = SpecialistPoolServiceClient.Create();
    // Initialize request argument(s)
    DeleteSpecialistPoolRequest request = new DeleteSpecialistPoolRequest
    {
        SpecialistPoolName = SpecialistPoolName.FromProjectLocationSpecialistPool("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]"),
        Force = false,
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = specialistPoolServiceClient.DeleteSpecialistPool(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = specialistPoolServiceClient.PollOnceDeleteSpecialistPool(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSpecialistPool(SpecialistPoolName, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteSpecialistPool(SpecialistPoolName name, CallSettings callSettings = null)

Deletes a SpecialistPool as well as all Specialists in the pool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SpecialistPoolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolName)`  
Required. The resource name of the SpecialistPool to delete. Format: `projects/{project}/locations/{location}/specialistPools/{specialist_pool}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = SpecialistPoolServiceClient.Create();
    // Initialize request argument(s)
    SpecialistPoolName name = SpecialistPoolName.FromProjectLocationSpecialistPool("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]");
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = specialistPoolServiceClient.DeleteSpecialistPool(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = specialistPoolServiceClient.PollOnceDeleteSpecialistPool(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSpecialistPool(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteSpecialistPool(string name, CallSettings callSettings = null)

Deletes a SpecialistPool as well as all Specialists in the pool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the SpecialistPool to delete. Format: `projects/{project}/locations/{location}/specialistPools/{specialist_pool}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = SpecialistPoolServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/specialistPools/[SPECIALIST_POOL]";
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = specialistPoolServiceClient.DeleteSpecialistPool(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = specialistPoolServiceClient.PollOnceDeleteSpecialistPool(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSpecialistPoolAsync(DeleteSpecialistPoolRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteSpecialistPoolAsync(DeleteSpecialistPoolRequest request, CallSettings callSettings = null)

Deletes a SpecialistPool as well as all Specialists in the pool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSpecialistPoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteSpecialistPoolRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteSpecialistPoolRequest request = new DeleteSpecialistPoolRequest
    {
        SpecialistPoolName = SpecialistPoolName.FromProjectLocationSpecialistPool("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]"),
        Force = false,
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await specialistPoolServiceClient.DeleteSpecialistPoolAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await specialistPoolServiceClient.PollOnceDeleteSpecialistPoolAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSpecialistPoolAsync(DeleteSpecialistPoolRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteSpecialistPoolAsync(DeleteSpecialistPoolRequest request, CancellationToken cancellationToken)

Deletes a SpecialistPool as well as all Specialists in the pool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSpecialistPoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteSpecialistPoolRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteSpecialistPoolRequest request = new DeleteSpecialistPoolRequest
    {
        SpecialistPoolName = SpecialistPoolName.FromProjectLocationSpecialistPool("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]"),
        Force = false,
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await specialistPoolServiceClient.DeleteSpecialistPoolAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await specialistPoolServiceClient.PollOnceDeleteSpecialistPoolAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSpecialistPoolAsync(SpecialistPoolName, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteSpecialistPoolAsync(SpecialistPoolName name, CallSettings callSettings = null)

Deletes a SpecialistPool as well as all Specialists in the pool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SpecialistPoolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolName)`  
Required. The resource name of the SpecialistPool to delete. Format: `projects/{project}/locations/{location}/specialistPools/{specialist_pool}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    SpecialistPoolName name = SpecialistPoolName.FromProjectLocationSpecialistPool("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]");
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await specialistPoolServiceClient.DeleteSpecialistPoolAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await specialistPoolServiceClient.PollOnceDeleteSpecialistPoolAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSpecialistPoolAsync(SpecialistPoolName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteSpecialistPoolAsync(SpecialistPoolName name, CancellationToken cancellationToken)

Deletes a SpecialistPool as well as all Specialists in the pool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SpecialistPoolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolName)`  
Required. The resource name of the SpecialistPool to delete. Format: `projects/{project}/locations/{location}/specialistPools/{specialist_pool}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    SpecialistPoolName name = SpecialistPoolName.FromProjectLocationSpecialistPool("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]");
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await specialistPoolServiceClient.DeleteSpecialistPoolAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await specialistPoolServiceClient.PollOnceDeleteSpecialistPoolAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSpecialistPoolAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteSpecialistPoolAsync(string name, CallSettings callSettings = null)

Deletes a SpecialistPool as well as all Specialists in the pool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the SpecialistPool to delete. Format: `projects/{project}/locations/{location}/specialistPools/{specialist_pool}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/specialistPools/[SPECIALIST_POOL]";
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await specialistPoolServiceClient.DeleteSpecialistPoolAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await specialistPoolServiceClient.PollOnceDeleteSpecialistPoolAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSpecialistPoolAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteSpecialistPoolAsync(string name, CancellationToken cancellationToken)

Deletes a SpecialistPool as well as all Specialists in the pool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the SpecialistPool to delete. Format: `projects/{project}/locations/{location}/specialistPools/{specialist_pool}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/specialistPools/[SPECIALIST_POOL]";
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await specialistPoolServiceClient.DeleteSpecialistPoolAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await specialistPoolServiceClient.PollOnceDeleteSpecialistPoolAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GetSpecialistPool(GetSpecialistPoolRequest, CallSettings)
    
    
    public virtual SpecialistPool GetSpecialistPool(GetSpecialistPoolRequest request, CallSettings callSettings = null)

Gets a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSpecialistPoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GetSpecialistPoolRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)` | The RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = SpecialistPoolServiceClient.Create();
    // Initialize request argument(s)
    GetSpecialistPoolRequest request = new GetSpecialistPoolRequest
    {
        SpecialistPoolName = SpecialistPoolName.FromProjectLocationSpecialistPool("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]"),
    };
    // Make the request
    SpecialistPool response = specialistPoolServiceClient.GetSpecialistPool(request);
    

### GetSpecialistPool(SpecialistPoolName, CallSettings)
    
    
    public virtual SpecialistPool GetSpecialistPool(SpecialistPoolName name, CallSettings callSettings = null)

Gets a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SpecialistPoolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolName)`  
Required. The name of the SpecialistPool resource. The form is `projects/{project}/locations/{location}/specialistPools/{specialist_pool}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)` | The RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = SpecialistPoolServiceClient.Create();
    // Initialize request argument(s)
    SpecialistPoolName name = SpecialistPoolName.FromProjectLocationSpecialistPool("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]");
    // Make the request
    SpecialistPool response = specialistPoolServiceClient.GetSpecialistPool(name);
    

### GetSpecialistPool(string, CallSettings)
    
    
    public virtual SpecialistPool GetSpecialistPool(string name, CallSettings callSettings = null)

Gets a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the SpecialistPool resource. The form is `projects/{project}/locations/{location}/specialistPools/{specialist_pool}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)` | The RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = SpecialistPoolServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/specialistPools/[SPECIALIST_POOL]";
    // Make the request
    SpecialistPool response = specialistPoolServiceClient.GetSpecialistPool(name);
    

### GetSpecialistPoolAsync(GetSpecialistPoolRequest, CallSettings)
    
    
    public virtual Task<SpecialistPool> GetSpecialistPoolAsync(GetSpecialistPoolRequest request, CallSettings callSettings = null)

Gets a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSpecialistPoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GetSpecialistPoolRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetSpecialistPoolRequest request = new GetSpecialistPoolRequest
    {
        SpecialistPoolName = SpecialistPoolName.FromProjectLocationSpecialistPool("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]"),
    };
    // Make the request
    SpecialistPool response = await specialistPoolServiceClient.GetSpecialistPoolAsync(request);
    

### GetSpecialistPoolAsync(GetSpecialistPoolRequest, CancellationToken)
    
    
    public virtual Task<SpecialistPool> GetSpecialistPoolAsync(GetSpecialistPoolRequest request, CancellationToken cancellationToken)

Gets a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSpecialistPoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GetSpecialistPoolRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetSpecialistPoolRequest request = new GetSpecialistPoolRequest
    {
        SpecialistPoolName = SpecialistPoolName.FromProjectLocationSpecialistPool("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]"),
    };
    // Make the request
    SpecialistPool response = await specialistPoolServiceClient.GetSpecialistPoolAsync(request);
    

### GetSpecialistPoolAsync(SpecialistPoolName, CallSettings)
    
    
    public virtual Task<SpecialistPool> GetSpecialistPoolAsync(SpecialistPoolName name, CallSettings callSettings = null)

Gets a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SpecialistPoolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolName)`  
Required. The name of the SpecialistPool resource. The form is `projects/{project}/locations/{location}/specialistPools/{specialist_pool}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    SpecialistPoolName name = SpecialistPoolName.FromProjectLocationSpecialistPool("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]");
    // Make the request
    SpecialistPool response = await specialistPoolServiceClient.GetSpecialistPoolAsync(name);
    

### GetSpecialistPoolAsync(SpecialistPoolName, CancellationToken)
    
    
    public virtual Task<SpecialistPool> GetSpecialistPoolAsync(SpecialistPoolName name, CancellationToken cancellationToken)

Gets a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[SpecialistPoolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolName)`  
Required. The name of the SpecialistPool resource. The form is `projects/{project}/locations/{location}/specialistPools/{specialist_pool}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    SpecialistPoolName name = SpecialistPoolName.FromProjectLocationSpecialistPool("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]");
    // Make the request
    SpecialistPool response = await specialistPoolServiceClient.GetSpecialistPoolAsync(name);
    

### GetSpecialistPoolAsync(string, CallSettings)
    
    
    public virtual Task<SpecialistPool> GetSpecialistPoolAsync(string name, CallSettings callSettings = null)

Gets a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the SpecialistPool resource. The form is `projects/{project}/locations/{location}/specialistPools/{specialist_pool}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/specialistPools/[SPECIALIST_POOL]";
    // Make the request
    SpecialistPool response = await specialistPoolServiceClient.GetSpecialistPoolAsync(name);
    

### GetSpecialistPoolAsync(string, CancellationToken)
    
    
    public virtual Task<SpecialistPool> GetSpecialistPoolAsync(string name, CancellationToken cancellationToken)

Gets a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the SpecialistPool resource. The form is `projects/{project}/locations/{location}/specialistPools/{specialist_pool}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/specialistPools/[SPECIALIST_POOL]";
    // Make the request
    SpecialistPool response = await specialistPoolServiceClient.GetSpecialistPoolAsync(name);
    

### ListSpecialistPools(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListSpecialistPoolsResponse, SpecialistPool> ListSpecialistPools(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists SpecialistPools in a Location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the SpecialistPool's parent resource. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSpecialistPoolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListSpecialistPoolsResponse)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)` | A pageable sequence of [SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool) resources.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = SpecialistPoolServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListSpecialistPoolsResponse, SpecialistPool> response = specialistPoolServiceClient.ListSpecialistPools(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (SpecialistPool item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListSpecialistPoolsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (SpecialistPool item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<SpecialistPool> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (SpecialistPool item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSpecialistPools(ListSpecialistPoolsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListSpecialistPoolsResponse, SpecialistPool> ListSpecialistPools(ListSpecialistPoolsRequest request, CallSettings callSettings = null)

Lists SpecialistPools in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSpecialistPoolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListSpecialistPoolsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSpecialistPoolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListSpecialistPoolsResponse)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)` | A pageable sequence of [SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool) resources.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = SpecialistPoolServiceClient.Create();
    // Initialize request argument(s)
    ListSpecialistPoolsRequest request = new ListSpecialistPoolsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ReadMask = new FieldMask(),
    };
    // Make the request
    PagedEnumerable<ListSpecialistPoolsResponse, SpecialistPool> response = specialistPoolServiceClient.ListSpecialistPools(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (SpecialistPool item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListSpecialistPoolsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (SpecialistPool item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<SpecialistPool> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (SpecialistPool item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSpecialistPools(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListSpecialistPoolsResponse, SpecialistPool> ListSpecialistPools(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists SpecialistPools in a Location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the SpecialistPool's parent resource. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSpecialistPoolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListSpecialistPoolsResponse)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)` | A pageable sequence of [SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool) resources.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = SpecialistPoolServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListSpecialistPoolsResponse, SpecialistPool> response = specialistPoolServiceClient.ListSpecialistPools(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (SpecialistPool item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListSpecialistPoolsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (SpecialistPool item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<SpecialistPool> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (SpecialistPool item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSpecialistPoolsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSpecialistPoolsResponse, SpecialistPool> ListSpecialistPoolsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists SpecialistPools in a Location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the SpecialistPool's parent resource. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSpecialistPoolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListSpecialistPoolsResponse)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)` | A pageable asynchronous sequence of [SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool) resources.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListSpecialistPoolsResponse, SpecialistPool> response = specialistPoolServiceClient.ListSpecialistPoolsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (SpecialistPool item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListSpecialistPoolsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (SpecialistPool item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<SpecialistPool> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (SpecialistPool item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSpecialistPoolsAsync(ListSpecialistPoolsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSpecialistPoolsResponse, SpecialistPool> ListSpecialistPoolsAsync(ListSpecialistPoolsRequest request, CallSettings callSettings = null)

Lists SpecialistPools in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSpecialistPoolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListSpecialistPoolsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSpecialistPoolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListSpecialistPoolsResponse)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)` | A pageable asynchronous sequence of [SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool) resources.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListSpecialistPoolsRequest request = new ListSpecialistPoolsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ReadMask = new FieldMask(),
    };
    // Make the request
    PagedAsyncEnumerable<ListSpecialistPoolsResponse, SpecialistPool> response = specialistPoolServiceClient.ListSpecialistPoolsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (SpecialistPool item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListSpecialistPoolsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (SpecialistPool item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<SpecialistPool> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (SpecialistPool item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSpecialistPoolsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSpecialistPoolsResponse, SpecialistPool> ListSpecialistPoolsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists SpecialistPools in a Location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the SpecialistPool's parent resource. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSpecialistPoolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ListSpecialistPoolsResponse)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)` | A pageable asynchronous sequence of [SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool) resources.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListSpecialistPoolsResponse, SpecialistPool> response = specialistPoolServiceClient.ListSpecialistPoolsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (SpecialistPool item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListSpecialistPoolsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (SpecialistPool item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<SpecialistPool> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (SpecialistPool item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceCreateSpecialistPool(string, CallSettings)
    
    
    public virtual Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata> PollOnceCreateSpecialistPool(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateSpecialistPool` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)[CreateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateSpecialistPoolOperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateSpecialistPoolAsync(string, CallSettings)
    
    
    public virtual Task<Operation<SpecialistPool, CreateSpecialistPoolOperationMetadata>> PollOnceCreateSpecialistPoolAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateSpecialistPool`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)[CreateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.CreateSpecialistPoolOperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteSpecialistPool(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> PollOnceDeleteSpecialistPool(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteSpecialistPool` .

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
  
### PollOnceDeleteSpecialistPoolAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> PollOnceDeleteSpecialistPoolAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteSpecialistPool`.

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
  
### PollOnceUpdateSpecialistPool(string, CallSettings)
    
    
    public virtual Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> PollOnceUpdateSpecialistPool(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateSpecialistPool` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)[UpdateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateSpecialistPoolOperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateSpecialistPoolAsync(string, CallSettings)
    
    
    public virtual Task<Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata>> PollOnceUpdateSpecialistPoolAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateSpecialistPool`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)[UpdateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateSpecialistPoolOperationMetadata)` | A task representing the result of polling the operation.  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolServiceClient#Google_Cloud_AIPlatform_V1_SpecialistPoolServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolServiceClient#Google_Cloud_AIPlatform_V1_SpecialistPoolServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolServiceClient#Google_Cloud_AIPlatform_V1_SpecialistPoolServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolServiceClient#Google_Cloud_AIPlatform_V1_SpecialistPoolServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateSpecialistPool(SpecialistPool, FieldMask, CallSettings)
    
    
    public virtual Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> UpdateSpecialistPool(SpecialistPool specialistPool, FieldMask updateMask, CallSettings callSettings = null)

Updates a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`specialistPool` | `[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)`  
Required. The SpecialistPool which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The update mask applies to the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)[UpdateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateSpecialistPoolOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = SpecialistPoolServiceClient.Create();
    // Initialize request argument(s)
    SpecialistPool specialistPool = new SpecialistPool();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> response = specialistPoolServiceClient.UpdateSpecialistPool(specialistPool, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    SpecialistPool result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> retrievedResponse = specialistPoolServiceClient.PollOnceUpdateSpecialistPool(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        SpecialistPool retrievedResult = retrievedResponse.Result;
    }
    

### UpdateSpecialistPool(UpdateSpecialistPoolRequest, CallSettings)
    
    
    public virtual Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> UpdateSpecialistPool(UpdateSpecialistPoolRequest request, CallSettings callSettings = null)

Updates a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSpecialistPoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateSpecialistPoolRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)[UpdateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateSpecialistPoolOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = SpecialistPoolServiceClient.Create();
    // Initialize request argument(s)
    UpdateSpecialistPoolRequest request = new UpdateSpecialistPoolRequest
    {
        SpecialistPool = new SpecialistPool(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> response = specialistPoolServiceClient.UpdateSpecialistPool(request);
    
    // Poll until the returned long-running operation is complete
    Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    SpecialistPool result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> retrievedResponse = specialistPoolServiceClient.PollOnceUpdateSpecialistPool(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        SpecialistPool retrievedResult = retrievedResponse.Result;
    }
    

### UpdateSpecialistPoolAsync(SpecialistPool, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata>> UpdateSpecialistPoolAsync(SpecialistPool specialistPool, FieldMask updateMask, CallSettings callSettings = null)

Updates a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`specialistPool` | `[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)`  
Required. The SpecialistPool which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The update mask applies to the resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)[UpdateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateSpecialistPoolOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    SpecialistPool specialistPool = new SpecialistPool();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> response = await specialistPoolServiceClient.UpdateSpecialistPoolAsync(specialistPool, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    SpecialistPool result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> retrievedResponse = await specialistPoolServiceClient.PollOnceUpdateSpecialistPoolAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        SpecialistPool retrievedResult = retrievedResponse.Result;
    }
    

### UpdateSpecialistPoolAsync(SpecialistPool, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata>> UpdateSpecialistPoolAsync(SpecialistPool specialistPool, FieldMask updateMask, CancellationToken cancellationToken)

Updates a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`specialistPool` | `[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)`  
Required. The SpecialistPool which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The update mask applies to the resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)[UpdateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateSpecialistPoolOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    SpecialistPool specialistPool = new SpecialistPool();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> response = await specialistPoolServiceClient.UpdateSpecialistPoolAsync(specialistPool, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    SpecialistPool result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> retrievedResponse = await specialistPoolServiceClient.PollOnceUpdateSpecialistPoolAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        SpecialistPool retrievedResult = retrievedResponse.Result;
    }
    

### UpdateSpecialistPoolAsync(UpdateSpecialistPoolRequest, CallSettings)
    
    
    public virtual Task<Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata>> UpdateSpecialistPoolAsync(UpdateSpecialistPoolRequest request, CallSettings callSettings = null)

Updates a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSpecialistPoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateSpecialistPoolRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)[UpdateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateSpecialistPoolOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateSpecialistPoolRequest request = new UpdateSpecialistPoolRequest
    {
        SpecialistPool = new SpecialistPool(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> response = await specialistPoolServiceClient.UpdateSpecialistPoolAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    SpecialistPool result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> retrievedResponse = await specialistPoolServiceClient.PollOnceUpdateSpecialistPoolAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        SpecialistPool retrievedResult = retrievedResponse.Result;
    }
    

### UpdateSpecialistPoolAsync(UpdateSpecialistPoolRequest, CancellationToken)
    
    
    public virtual Task<Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata>> UpdateSpecialistPoolAsync(UpdateSpecialistPoolRequest request, CancellationToken cancellationToken)

Updates a SpecialistPool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSpecialistPoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateSpecialistPoolRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[SpecialistPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPool)[UpdateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.UpdateSpecialistPoolOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    SpecialistPoolServiceClient specialistPoolServiceClient = await SpecialistPoolServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateSpecialistPoolRequest request = new UpdateSpecialistPoolRequest
    {
        SpecialistPool = new SpecialistPool(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> response = await specialistPoolServiceClient.UpdateSpecialistPoolAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    SpecialistPool result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<SpecialistPool, UpdateSpecialistPoolOperationMetadata> retrievedResponse = await specialistPoolServiceClient.PollOnceUpdateSpecialistPoolAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        SpecialistPool retrievedResult = retrievedResponse.Result;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
