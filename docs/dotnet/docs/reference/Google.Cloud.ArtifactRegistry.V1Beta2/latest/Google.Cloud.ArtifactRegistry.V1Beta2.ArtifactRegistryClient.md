---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClient
title: Artifact Registry v1beta2 API - Class ArtifactRegistryClient (2.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:34.790348+00:00
---

# Artifact Registry v1beta2 API - Class ArtifactRegistryClient (2.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Artifact Registry v1beta2 API - Class ArtifactRegistryClient (2.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClient)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/2.0.0-beta05/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClient)
  * [ 1.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/1.0.0-beta06/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClient)


    
    
    public abstract class ArtifactRegistryClient

Reference documentation and code samples for the Artifact Registry v1beta2 API class ArtifactRegistryClient.

ArtifactRegistry client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ArtifactRegistryClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[ArtifactRegistryClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClientImpl)

## Namespace

[Google.Cloud.ArtifactRegistry.V1Beta2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2)

## Assembly

Google.Cloud.ArtifactRegistry.V1Beta2.dll

## Remarks

The Artifact Registry API service.

Artifact Registry is an artifact management system for storing artifacts from different package management systems.

The resources managed by this API are:

  * Repositories, which group packages and their data.
  * Packages, which group versions and their tags.
  * Versions, which are specific forms of a package.
  * Tags, which represent alternative names for versions.
  * Files, which contain content and are optionally associated with a Package or Version.



## Properties 

### CreateRepositoryOperationsClient
    
    
    public virtual OperationsClient CreateRepositoryOperationsClient { get; }

The long-running operations client for `CreateRepository`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the ArtifactRegistry service, which is a host of "artifactregistry.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default ArtifactRegistry scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default ArtifactRegistry scopes are: 

  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/cloud-platform.read-only>



### DeletePackageOperationsClient
    
    
    public virtual OperationsClient DeletePackageOperationsClient { get; }

The long-running operations client for `DeletePackage`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteRepositoryOperationsClient
    
    
    public virtual OperationsClient DeleteRepositoryOperationsClient { get; }

The long-running operations client for `DeleteRepository`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DeleteVersionOperationsClient
    
    
    public virtual OperationsClient DeleteVersionOperationsClient { get; }

The long-running operations client for `DeleteVersion`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual ArtifactRegistry.ArtifactRegistryClient GrpcClient { get; }

The underlying gRPC ArtifactRegistry client

**Property Value**  
---  
**Type** | **Description**  
`[ArtifactRegistry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistry)[ArtifactRegistryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistry.ArtifactRegistryClient)` |   
  
### ImportAptArtifactsOperationsClient
    
    
    public virtual OperationsClient ImportAptArtifactsOperationsClient { get; }

The long-running operations client for `ImportAptArtifacts`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### ImportYumArtifactsOperationsClient
    
    
    public virtual OperationsClient ImportYumArtifactsOperationsClient { get; }

The long-running operations client for `ImportYumArtifacts`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
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

### Create()
    
    
    public static ArtifactRegistryClient Create()

Synchronously creates a [ArtifactRegistryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ArtifactRegistryClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[ArtifactRegistryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClient)` | The created [ArtifactRegistryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<ArtifactRegistryClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [ArtifactRegistryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ArtifactRegistryClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ArtifactRegistryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClient)` | The task representing the created [ArtifactRegistryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClient).  
  
### CreateRepository(LocationName, Repository, string, CallSettings)
    
    
    public virtual Operation<Repository, OperationMetadata> CreateRepository(LocationName parent, Repository repository, string repositoryId, CallSettings callSettings = null)

Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the parent resource where the repository will be created.  
`repository` | `[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)`  
The repository to be created.  
`repositoryId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The repository id to use for this repository.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    gcav::Repository repository = new gcav::Repository();
    string repositoryId = "";
    // Make the request
    Operation<gcav::Repository, gcav::OperationMetadata> response = artifactRegistryClient.CreateRepository(parent, repository, repositoryId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::Repository, gcav::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcav::Repository result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::Repository, gcav::OperationMetadata> retrievedResponse = artifactRegistryClient.PollOnceCreateRepository(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::Repository retrievedResult = retrievedResponse.Result;
    }
    

### CreateRepository(CreateRepositoryRequest, CallSettings)
    
    
    public virtual Operation<Repository, OperationMetadata> CreateRepository(CreateRepositoryRequest request, CallSettings callSettings = null)

Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.CreateRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::CreateRepositoryRequest request = new gcav::CreateRepositoryRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        RepositoryId = "",
        Repository = new gcav::Repository(),
    };
    // Make the request
    Operation<gcav::Repository, gcav::OperationMetadata> response = artifactRegistryClient.CreateRepository(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::Repository, gcav::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcav::Repository result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::Repository, gcav::OperationMetadata> retrievedResponse = artifactRegistryClient.PollOnceCreateRepository(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::Repository retrievedResult = retrievedResponse.Result;
    }
    

### CreateRepository(string, Repository, string, CallSettings)
    
    
    public virtual Operation<Repository, OperationMetadata> CreateRepository(string parent, Repository repository, string repositoryId, CallSettings callSettings = null)

Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource where the repository will be created.  
`repository` | `[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)`  
The repository to be created.  
`repositoryId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The repository id to use for this repository.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    gcav::Repository repository = new gcav::Repository();
    string repositoryId = "";
    // Make the request
    Operation<gcav::Repository, gcav::OperationMetadata> response = artifactRegistryClient.CreateRepository(parent, repository, repositoryId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::Repository, gcav::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcav::Repository result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::Repository, gcav::OperationMetadata> retrievedResponse = artifactRegistryClient.PollOnceCreateRepository(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::Repository retrievedResult = retrievedResponse.Result;
    }
    

### CreateRepositoryAsync(LocationName, Repository, string, CallSettings)
    
    
    public virtual Task<Operation<Repository, OperationMetadata>> CreateRepositoryAsync(LocationName parent, Repository repository, string repositoryId, CallSettings callSettings = null)

Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the parent resource where the repository will be created.  
`repository` | `[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)`  
The repository to be created.  
`repositoryId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The repository id to use for this repository.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    gcav::Repository repository = new gcav::Repository();
    string repositoryId = "";
    // Make the request
    Operation<gcav::Repository, gcav::OperationMetadata> response = await artifactRegistryClient.CreateRepositoryAsync(parent, repository, repositoryId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::Repository, gcav::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcav::Repository result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::Repository, gcav::OperationMetadata> retrievedResponse = await artifactRegistryClient.PollOnceCreateRepositoryAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::Repository retrievedResult = retrievedResponse.Result;
    }
    

### CreateRepositoryAsync(LocationName, Repository, string, CancellationToken)
    
    
    public virtual Task<Operation<Repository, OperationMetadata>> CreateRepositoryAsync(LocationName parent, Repository repository, string repositoryId, CancellationToken cancellationToken)

Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the parent resource where the repository will be created.  
`repository` | `[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)`  
The repository to be created.  
`repositoryId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The repository id to use for this repository.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    gcav::Repository repository = new gcav::Repository();
    string repositoryId = "";
    // Make the request
    Operation<gcav::Repository, gcav::OperationMetadata> response = await artifactRegistryClient.CreateRepositoryAsync(parent, repository, repositoryId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::Repository, gcav::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcav::Repository result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::Repository, gcav::OperationMetadata> retrievedResponse = await artifactRegistryClient.PollOnceCreateRepositoryAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::Repository retrievedResult = retrievedResponse.Result;
    }
    

### CreateRepositoryAsync(CreateRepositoryRequest, CallSettings)
    
    
    public virtual Task<Operation<Repository, OperationMetadata>> CreateRepositoryAsync(CreateRepositoryRequest request, CallSettings callSettings = null)

Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.CreateRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::CreateRepositoryRequest request = new gcav::CreateRepositoryRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        RepositoryId = "",
        Repository = new gcav::Repository(),
    };
    // Make the request
    Operation<gcav::Repository, gcav::OperationMetadata> response = await artifactRegistryClient.CreateRepositoryAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::Repository, gcav::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcav::Repository result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::Repository, gcav::OperationMetadata> retrievedResponse = await artifactRegistryClient.PollOnceCreateRepositoryAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::Repository retrievedResult = retrievedResponse.Result;
    }
    

### CreateRepositoryAsync(CreateRepositoryRequest, CancellationToken)
    
    
    public virtual Task<Operation<Repository, OperationMetadata>> CreateRepositoryAsync(CreateRepositoryRequest request, CancellationToken cancellationToken)

Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.CreateRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::CreateRepositoryRequest request = new gcav::CreateRepositoryRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        RepositoryId = "",
        Repository = new gcav::Repository(),
    };
    // Make the request
    Operation<gcav::Repository, gcav::OperationMetadata> response = await artifactRegistryClient.CreateRepositoryAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::Repository, gcav::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcav::Repository result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::Repository, gcav::OperationMetadata> retrievedResponse = await artifactRegistryClient.PollOnceCreateRepositoryAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::Repository retrievedResult = retrievedResponse.Result;
    }
    

### CreateRepositoryAsync(string, Repository, string, CallSettings)
    
    
    public virtual Task<Operation<Repository, OperationMetadata>> CreateRepositoryAsync(string parent, Repository repository, string repositoryId, CallSettings callSettings = null)

Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource where the repository will be created.  
`repository` | `[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)`  
The repository to be created.  
`repositoryId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The repository id to use for this repository.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    gcav::Repository repository = new gcav::Repository();
    string repositoryId = "";
    // Make the request
    Operation<gcav::Repository, gcav::OperationMetadata> response = await artifactRegistryClient.CreateRepositoryAsync(parent, repository, repositoryId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::Repository, gcav::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcav::Repository result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::Repository, gcav::OperationMetadata> retrievedResponse = await artifactRegistryClient.PollOnceCreateRepositoryAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::Repository retrievedResult = retrievedResponse.Result;
    }
    

### CreateRepositoryAsync(string, Repository, string, CancellationToken)
    
    
    public virtual Task<Operation<Repository, OperationMetadata>> CreateRepositoryAsync(string parent, Repository repository, string repositoryId, CancellationToken cancellationToken)

Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource where the repository will be created.  
`repository` | `[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)`  
The repository to be created.  
`repositoryId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The repository id to use for this repository.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    gcav::Repository repository = new gcav::Repository();
    string repositoryId = "";
    // Make the request
    Operation<gcav::Repository, gcav::OperationMetadata> response = await artifactRegistryClient.CreateRepositoryAsync(parent, repository, repositoryId);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::Repository, gcav::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcav::Repository result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::Repository, gcav::OperationMetadata> retrievedResponse = await artifactRegistryClient.PollOnceCreateRepositoryAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::Repository retrievedResult = retrievedResponse.Result;
    }
    

### CreateTag(CreateTagRequest, CallSettings)
    
    
    public virtual Tag CreateTag(CreateTagRequest request, CallSettings callSettings = null)

Creates a tag.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTagRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.CreateTagRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::CreateTagRequest request = new gcav::CreateTagRequest
    {
        Parent = "",
        TagId = "",
        Tag = new gcav::Tag(),
    };
    // Make the request
    gcav::Tag response = artifactRegistryClient.CreateTag(request);
    

### CreateTag(string, Tag, string, CallSettings)
    
    
    public virtual Tag CreateTag(string parent, Tag tag, string tagId, CallSettings callSettings = null)

Creates a tag.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the parent resource where the tag will be created.  
`tag` | `[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)`  
The tag to be created.  
`tagId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The tag id to use for this repository.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    string parent = "";
    gcav::Tag tag = new gcav::Tag();
    string tagId = "";
    // Make the request
    gcav::Tag response = artifactRegistryClient.CreateTag(parent, tag, tagId);
    

### CreateTagAsync(CreateTagRequest, CallSettings)
    
    
    public virtual Task<Tag> CreateTagAsync(CreateTagRequest request, CallSettings callSettings = null)

Creates a tag.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTagRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.CreateTagRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::CreateTagRequest request = new gcav::CreateTagRequest
    {
        Parent = "",
        TagId = "",
        Tag = new gcav::Tag(),
    };
    // Make the request
    gcav::Tag response = await artifactRegistryClient.CreateTagAsync(request);
    

### CreateTagAsync(CreateTagRequest, CancellationToken)
    
    
    public virtual Task<Tag> CreateTagAsync(CreateTagRequest request, CancellationToken cancellationToken)

Creates a tag.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTagRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.CreateTagRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::CreateTagRequest request = new gcav::CreateTagRequest
    {
        Parent = "",
        TagId = "",
        Tag = new gcav::Tag(),
    };
    // Make the request
    gcav::Tag response = await artifactRegistryClient.CreateTagAsync(request);
    

### CreateTagAsync(string, Tag, string, CallSettings)
    
    
    public virtual Task<Tag> CreateTagAsync(string parent, Tag tag, string tagId, CallSettings callSettings = null)

Creates a tag.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the parent resource where the tag will be created.  
`tag` | `[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)`  
The tag to be created.  
`tagId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The tag id to use for this repository.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "";
    gcav::Tag tag = new gcav::Tag();
    string tagId = "";
    // Make the request
    gcav::Tag response = await artifactRegistryClient.CreateTagAsync(parent, tag, tagId);
    

### CreateTagAsync(string, Tag, string, CancellationToken)
    
    
    public virtual Task<Tag> CreateTagAsync(string parent, Tag tag, string tagId, CancellationToken cancellationToken)

Creates a tag.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the parent resource where the tag will be created.  
`tag` | `[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)`  
The tag to be created.  
`tagId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The tag id to use for this repository.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "";
    gcav::Tag tag = new gcav::Tag();
    string tagId = "";
    // Make the request
    gcav::Tag response = await artifactRegistryClient.CreateTagAsync(parent, tag, tagId);
    

### DeletePackage(DeletePackageRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeletePackage(DeletePackageRequest request, CallSettings callSettings = null)

Deletes a package and all of its versions and tags. The returned operation will complete once the package has been deleted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.DeletePackageRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::DeletePackageRequest request = new gcav::DeletePackageRequest { Name = "", };
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = artifactRegistryClient.DeletePackage(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = artifactRegistryClient.PollOnceDeletePackage(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePackage(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeletePackage(string name, CallSettings callSettings = null)

Deletes a package and all of its versions and tags. The returned operation will complete once the package has been deleted.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the package to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = artifactRegistryClient.DeletePackage(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = artifactRegistryClient.PollOnceDeletePackage(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePackageAsync(DeletePackageRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeletePackageAsync(DeletePackageRequest request, CallSettings callSettings = null)

Deletes a package and all of its versions and tags. The returned operation will complete once the package has been deleted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.DeletePackageRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::DeletePackageRequest request = new gcav::DeletePackageRequest { Name = "", };
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = await artifactRegistryClient.DeletePackageAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = await artifactRegistryClient.PollOnceDeletePackageAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePackageAsync(DeletePackageRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeletePackageAsync(DeletePackageRequest request, CancellationToken cancellationToken)

Deletes a package and all of its versions and tags. The returned operation will complete once the package has been deleted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.DeletePackageRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::DeletePackageRequest request = new gcav::DeletePackageRequest { Name = "", };
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = await artifactRegistryClient.DeletePackageAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = await artifactRegistryClient.PollOnceDeletePackageAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePackageAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeletePackageAsync(string name, CallSettings callSettings = null)

Deletes a package and all of its versions and tags. The returned operation will complete once the package has been deleted.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the package to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = await artifactRegistryClient.DeletePackageAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = await artifactRegistryClient.PollOnceDeletePackageAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeletePackageAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeletePackageAsync(string name, CancellationToken cancellationToken)

Deletes a package and all of its versions and tags. The returned operation will complete once the package has been deleted.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the package to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = await artifactRegistryClient.DeletePackageAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = await artifactRegistryClient.PollOnceDeletePackageAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRepository(DeleteRepositoryRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteRepository(DeleteRepositoryRequest request, CallSettings callSettings = null)

Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.DeleteRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::DeleteRepositoryRequest request = new gcav::DeleteRepositoryRequest
    {
        RepositoryName = gcav::RepositoryName.FromProjectLocationRepository("[PROJECT]", "[LOCATION]", "[REPOSITORY]"),
    };
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = artifactRegistryClient.DeleteRepository(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = artifactRegistryClient.PollOnceDeleteRepository(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRepository(RepositoryName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteRepository(RepositoryName name, CallSettings callSettings = null)

Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RepositoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.RepositoryName)`  
Required. The name of the repository to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::RepositoryName name = gcav::RepositoryName.FromProjectLocationRepository("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = artifactRegistryClient.DeleteRepository(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = artifactRegistryClient.PollOnceDeleteRepository(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRepository(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteRepository(string name, CallSettings callSettings = null)

Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the repository to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/repositories/[REPOSITORY]";
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = artifactRegistryClient.DeleteRepository(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = artifactRegistryClient.PollOnceDeleteRepository(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRepositoryAsync(DeleteRepositoryRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteRepositoryAsync(DeleteRepositoryRequest request, CallSettings callSettings = null)

Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.DeleteRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::DeleteRepositoryRequest request = new gcav::DeleteRepositoryRequest
    {
        RepositoryName = gcav::RepositoryName.FromProjectLocationRepository("[PROJECT]", "[LOCATION]", "[REPOSITORY]"),
    };
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = await artifactRegistryClient.DeleteRepositoryAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = await artifactRegistryClient.PollOnceDeleteRepositoryAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRepositoryAsync(DeleteRepositoryRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteRepositoryAsync(DeleteRepositoryRequest request, CancellationToken cancellationToken)

Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.DeleteRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::DeleteRepositoryRequest request = new gcav::DeleteRepositoryRequest
    {
        RepositoryName = gcav::RepositoryName.FromProjectLocationRepository("[PROJECT]", "[LOCATION]", "[REPOSITORY]"),
    };
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = await artifactRegistryClient.DeleteRepositoryAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = await artifactRegistryClient.PollOnceDeleteRepositoryAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRepositoryAsync(RepositoryName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteRepositoryAsync(RepositoryName name, CallSettings callSettings = null)

Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RepositoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.RepositoryName)`  
Required. The name of the repository to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::RepositoryName name = gcav::RepositoryName.FromProjectLocationRepository("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = await artifactRegistryClient.DeleteRepositoryAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = await artifactRegistryClient.PollOnceDeleteRepositoryAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRepositoryAsync(RepositoryName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteRepositoryAsync(RepositoryName name, CancellationToken cancellationToken)

Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RepositoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.RepositoryName)`  
Required. The name of the repository to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::RepositoryName name = gcav::RepositoryName.FromProjectLocationRepository("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = await artifactRegistryClient.DeleteRepositoryAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = await artifactRegistryClient.PollOnceDeleteRepositoryAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRepositoryAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteRepositoryAsync(string name, CallSettings callSettings = null)

Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the repository to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/repositories/[REPOSITORY]";
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = await artifactRegistryClient.DeleteRepositoryAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = await artifactRegistryClient.PollOnceDeleteRepositoryAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteRepositoryAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteRepositoryAsync(string name, CancellationToken cancellationToken)

Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the repository to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/repositories/[REPOSITORY]";
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = await artifactRegistryClient.DeleteRepositoryAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = await artifactRegistryClient.PollOnceDeleteRepositoryAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteTag(DeleteTagRequest, CallSettings)
    
    
    public virtual void DeleteTag(DeleteTagRequest request, CallSettings callSettings = null)

Deletes a tag.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTagRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.DeleteTagRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::DeleteTagRequest request = new gcav::DeleteTagRequest { Name = "", };
    // Make the request
    artifactRegistryClient.DeleteTag(request);
    

### DeleteTag(string, CallSettings)
    
    
    public virtual void DeleteTag(string name, CallSettings callSettings = null)

Deletes a tag.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the tag to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    artifactRegistryClient.DeleteTag(name);
    

### DeleteTagAsync(DeleteTagRequest, CallSettings)
    
    
    public virtual Task DeleteTagAsync(DeleteTagRequest request, CallSettings callSettings = null)

Deletes a tag.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTagRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.DeleteTagRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::DeleteTagRequest request = new gcav::DeleteTagRequest { Name = "", };
    // Make the request
    await artifactRegistryClient.DeleteTagAsync(request);
    

### DeleteTagAsync(DeleteTagRequest, CancellationToken)
    
    
    public virtual Task DeleteTagAsync(DeleteTagRequest request, CancellationToken cancellationToken)

Deletes a tag.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTagRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.DeleteTagRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::DeleteTagRequest request = new gcav::DeleteTagRequest { Name = "", };
    // Make the request
    await artifactRegistryClient.DeleteTagAsync(request);
    

### DeleteTagAsync(string, CallSettings)
    
    
    public virtual Task DeleteTagAsync(string name, CallSettings callSettings = null)

Deletes a tag.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the tag to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    await artifactRegistryClient.DeleteTagAsync(name);
    

### DeleteTagAsync(string, CancellationToken)
    
    
    public virtual Task DeleteTagAsync(string name, CancellationToken cancellationToken)

Deletes a tag.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the tag to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    await artifactRegistryClient.DeleteTagAsync(name);
    

### DeleteVersion(DeleteVersionRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteVersion(DeleteVersionRequest request, CallSettings callSettings = null)

Deletes a version and all of its content. The returned operation will complete once the version has been deleted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.DeleteVersionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::DeleteVersionRequest request = new gcav::DeleteVersionRequest
    {
        Name = "",
        Force = false,
    };
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = artifactRegistryClient.DeleteVersion(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = artifactRegistryClient.PollOnceDeleteVersion(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteVersion(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteVersion(string name, CallSettings callSettings = null)

Deletes a version and all of its content. The returned operation will complete once the version has been deleted.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the version to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = artifactRegistryClient.DeleteVersion(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = artifactRegistryClient.PollOnceDeleteVersion(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteVersionAsync(DeleteVersionRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteVersionAsync(DeleteVersionRequest request, CallSettings callSettings = null)

Deletes a version and all of its content. The returned operation will complete once the version has been deleted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.DeleteVersionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::DeleteVersionRequest request = new gcav::DeleteVersionRequest
    {
        Name = "",
        Force = false,
    };
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = await artifactRegistryClient.DeleteVersionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = await artifactRegistryClient.PollOnceDeleteVersionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteVersionAsync(DeleteVersionRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteVersionAsync(DeleteVersionRequest request, CancellationToken cancellationToken)

Deletes a version and all of its content. The returned operation will complete once the version has been deleted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.DeleteVersionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::DeleteVersionRequest request = new gcav::DeleteVersionRequest
    {
        Name = "",
        Force = false,
    };
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = await artifactRegistryClient.DeleteVersionAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = await artifactRegistryClient.PollOnceDeleteVersionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteVersionAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteVersionAsync(string name, CallSettings callSettings = null)

Deletes a version and all of its content. The returned operation will complete once the version has been deleted.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the version to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = await artifactRegistryClient.DeleteVersionAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = await artifactRegistryClient.PollOnceDeleteVersionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteVersionAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteVersionAsync(string name, CancellationToken cancellationToken)

Deletes a version and all of its content. The returned operation will complete once the version has been deleted.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the version to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    Operation<Empty, gcav::OperationMetadata> response = await artifactRegistryClient.DeleteVersionAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, gcav::OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, gcav::OperationMetadata> retrievedResponse = await artifactRegistryClient.PollOnceDeleteVersionAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GetFile(GetFileRequest, CallSettings)
    
    
    public virtual File GetFile(GetFileRequest request, CallSettings callSettings = null)

Gets a file.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetFileRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.File)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::GetFileRequest request = new gcav::GetFileRequest { Name = "", };
    // Make the request
    gcav::File response = artifactRegistryClient.GetFile(request);
    

### GetFile(string, CallSettings)
    
    
    public virtual File GetFile(string name, CallSettings callSettings = null)

Gets a file.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the file to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.File)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    gcav::File response = artifactRegistryClient.GetFile(name);
    

### GetFileAsync(GetFileRequest, CallSettings)
    
    
    public virtual Task<File> GetFileAsync(GetFileRequest request, CallSettings callSettings = null)

Gets a file.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetFileRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.File)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::GetFileRequest request = new gcav::GetFileRequest { Name = "", };
    // Make the request
    gcav::File response = await artifactRegistryClient.GetFileAsync(request);
    

### GetFileAsync(GetFileRequest, CancellationToken)
    
    
    public virtual Task<File> GetFileAsync(GetFileRequest request, CancellationToken cancellationToken)

Gets a file.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetFileRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.File)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::GetFileRequest request = new gcav::GetFileRequest { Name = "", };
    // Make the request
    gcav::File response = await artifactRegistryClient.GetFileAsync(request);
    

### GetFileAsync(string, CallSettings)
    
    
    public virtual Task<File> GetFileAsync(string name, CallSettings callSettings = null)

Gets a file.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the file to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.File)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    gcav::File response = await artifactRegistryClient.GetFileAsync(name);
    

### GetFileAsync(string, CancellationToken)
    
    
    public virtual Task<File> GetFileAsync(string name, CancellationToken cancellationToken)

Gets a file.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the file to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.File)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    gcav::File response = await artifactRegistryClient.GetFileAsync(name);
    

### GetIamPolicy(GetIamPolicyRequest, CallSettings)
    
    
    public virtual Policy GetIamPolicy(GetIamPolicyRequest request, CallSettings callSettings = null)

Gets the IAM policy for a given resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    GetIamPolicyRequest request = new GetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Options = new GetPolicyOptions(),
    };
    // Make the request
    Policy response = artifactRegistryClient.GetIamPolicy(request);
    

### GetIamPolicyAsync(GetIamPolicyRequest, CallSettings)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(GetIamPolicyRequest request, CallSettings callSettings = null)

Gets the IAM policy for a given resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    GetIamPolicyRequest request = new GetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Options = new GetPolicyOptions(),
    };
    // Make the request
    Policy response = await artifactRegistryClient.GetIamPolicyAsync(request);
    

### GetIamPolicyAsync(GetIamPolicyRequest, CancellationToken)
    
    
    public virtual Task<Policy> GetIamPolicyAsync(GetIamPolicyRequest request, CancellationToken cancellationToken)

Gets the IAM policy for a given resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.GetIamPolicyRequest.html)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    GetIamPolicyRequest request = new GetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Options = new GetPolicyOptions(),
    };
    // Make the request
    Policy response = await artifactRegistryClient.GetIamPolicyAsync(request);
    

### GetPackage(GetPackageRequest, CallSettings)
    
    
    public virtual Package GetPackage(GetPackageRequest request, CallSettings callSettings = null)

Gets a package.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetPackageRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Package](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Package)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::GetPackageRequest request = new gcav::GetPackageRequest { Name = "", };
    // Make the request
    gcav::Package response = artifactRegistryClient.GetPackage(request);
    

### GetPackage(string, CallSettings)
    
    
    public virtual Package GetPackage(string name, CallSettings callSettings = null)

Gets a package.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the package to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Package](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Package)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    gcav::Package response = artifactRegistryClient.GetPackage(name);
    

### GetPackageAsync(GetPackageRequest, CallSettings)
    
    
    public virtual Task<Package> GetPackageAsync(GetPackageRequest request, CallSettings callSettings = null)

Gets a package.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetPackageRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Package](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Package)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::GetPackageRequest request = new gcav::GetPackageRequest { Name = "", };
    // Make the request
    gcav::Package response = await artifactRegistryClient.GetPackageAsync(request);
    

### GetPackageAsync(GetPackageRequest, CancellationToken)
    
    
    public virtual Task<Package> GetPackageAsync(GetPackageRequest request, CancellationToken cancellationToken)

Gets a package.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetPackageRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Package](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Package)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::GetPackageRequest request = new gcav::GetPackageRequest { Name = "", };
    // Make the request
    gcav::Package response = await artifactRegistryClient.GetPackageAsync(request);
    

### GetPackageAsync(string, CallSettings)
    
    
    public virtual Task<Package> GetPackageAsync(string name, CallSettings callSettings = null)

Gets a package.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the package to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Package](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Package)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    gcav::Package response = await artifactRegistryClient.GetPackageAsync(name);
    

### GetPackageAsync(string, CancellationToken)
    
    
    public virtual Task<Package> GetPackageAsync(string name, CancellationToken cancellationToken)

Gets a package.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the package to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Package](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Package)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    gcav::Package response = await artifactRegistryClient.GetPackageAsync(name);
    

### GetProjectSettings(GetProjectSettingsRequest, CallSettings)
    
    
    public virtual ProjectSettings GetProjectSettings(GetProjectSettingsRequest request, CallSettings callSettings = null)

Retrieves the Settings for the Project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProjectSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetProjectSettingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ProjectSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::GetProjectSettingsRequest request = new gcav::GetProjectSettingsRequest
    {
        ProjectSettingsName = gcav::ProjectSettingsName.FromProject("[PROJECT]"),
    };
    // Make the request
    gcav::ProjectSettings response = artifactRegistryClient.GetProjectSettings(request);
    

### GetProjectSettings(ProjectSettingsName, CallSettings)
    
    
    public virtual ProjectSettings GetProjectSettings(ProjectSettingsName name, CallSettings callSettings = null)

Retrieves the Settings for the Project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ProjectSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettingsName)`  
Required. The name of the projectSettings resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ProjectSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::ProjectSettingsName name = gcav::ProjectSettingsName.FromProject("[PROJECT]");
    // Make the request
    gcav::ProjectSettings response = artifactRegistryClient.GetProjectSettings(name);
    

### GetProjectSettings(string, CallSettings)
    
    
    public virtual ProjectSettings GetProjectSettings(string name, CallSettings callSettings = null)

Retrieves the Settings for the Project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the projectSettings resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ProjectSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/projectSettings";
    // Make the request
    gcav::ProjectSettings response = artifactRegistryClient.GetProjectSettings(name);
    

### GetProjectSettingsAsync(GetProjectSettingsRequest, CallSettings)
    
    
    public virtual Task<ProjectSettings> GetProjectSettingsAsync(GetProjectSettingsRequest request, CallSettings callSettings = null)

Retrieves the Settings for the Project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProjectSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetProjectSettingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ProjectSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::GetProjectSettingsRequest request = new gcav::GetProjectSettingsRequest
    {
        ProjectSettingsName = gcav::ProjectSettingsName.FromProject("[PROJECT]"),
    };
    // Make the request
    gcav::ProjectSettings response = await artifactRegistryClient.GetProjectSettingsAsync(request);
    

### GetProjectSettingsAsync(GetProjectSettingsRequest, CancellationToken)
    
    
    public virtual Task<ProjectSettings> GetProjectSettingsAsync(GetProjectSettingsRequest request, CancellationToken cancellationToken)

Retrieves the Settings for the Project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProjectSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetProjectSettingsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ProjectSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::GetProjectSettingsRequest request = new gcav::GetProjectSettingsRequest
    {
        ProjectSettingsName = gcav::ProjectSettingsName.FromProject("[PROJECT]"),
    };
    // Make the request
    gcav::ProjectSettings response = await artifactRegistryClient.GetProjectSettingsAsync(request);
    

### GetProjectSettingsAsync(ProjectSettingsName, CallSettings)
    
    
    public virtual Task<ProjectSettings> GetProjectSettingsAsync(ProjectSettingsName name, CallSettings callSettings = null)

Retrieves the Settings for the Project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ProjectSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettingsName)`  
Required. The name of the projectSettings resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ProjectSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::ProjectSettingsName name = gcav::ProjectSettingsName.FromProject("[PROJECT]");
    // Make the request
    gcav::ProjectSettings response = await artifactRegistryClient.GetProjectSettingsAsync(name);
    

### GetProjectSettingsAsync(ProjectSettingsName, CancellationToken)
    
    
    public virtual Task<ProjectSettings> GetProjectSettingsAsync(ProjectSettingsName name, CancellationToken cancellationToken)

Retrieves the Settings for the Project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ProjectSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettingsName)`  
Required. The name of the projectSettings resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ProjectSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::ProjectSettingsName name = gcav::ProjectSettingsName.FromProject("[PROJECT]");
    // Make the request
    gcav::ProjectSettings response = await artifactRegistryClient.GetProjectSettingsAsync(name);
    

### GetProjectSettingsAsync(string, CallSettings)
    
    
    public virtual Task<ProjectSettings> GetProjectSettingsAsync(string name, CallSettings callSettings = null)

Retrieves the Settings for the Project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the projectSettings resource.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ProjectSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/projectSettings";
    // Make the request
    gcav::ProjectSettings response = await artifactRegistryClient.GetProjectSettingsAsync(name);
    

### GetProjectSettingsAsync(string, CancellationToken)
    
    
    public virtual Task<ProjectSettings> GetProjectSettingsAsync(string name, CancellationToken cancellationToken)

Retrieves the Settings for the Project.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the projectSettings resource.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ProjectSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/projectSettings";
    // Make the request
    gcav::ProjectSettings response = await artifactRegistryClient.GetProjectSettingsAsync(name);
    

### GetRepository(GetRepositoryRequest, CallSettings)
    
    
    public virtual Repository GetRepository(GetRepositoryRequest request, CallSettings callSettings = null)

Gets a repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::GetRepositoryRequest request = new gcav::GetRepositoryRequest
    {
        RepositoryName = gcav::RepositoryName.FromProjectLocationRepository("[PROJECT]", "[LOCATION]", "[REPOSITORY]"),
    };
    // Make the request
    gcav::Repository response = artifactRegistryClient.GetRepository(request);
    

### GetRepository(RepositoryName, CallSettings)
    
    
    public virtual Repository GetRepository(RepositoryName name, CallSettings callSettings = null)

Gets a repository.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RepositoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.RepositoryName)`  
Required. The name of the repository to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::RepositoryName name = gcav::RepositoryName.FromProjectLocationRepository("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
    // Make the request
    gcav::Repository response = artifactRegistryClient.GetRepository(name);
    

### GetRepository(string, CallSettings)
    
    
    public virtual Repository GetRepository(string name, CallSettings callSettings = null)

Gets a repository.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the repository to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/repositories/[REPOSITORY]";
    // Make the request
    gcav::Repository response = artifactRegistryClient.GetRepository(name);
    

### GetRepositoryAsync(GetRepositoryRequest, CallSettings)
    
    
    public virtual Task<Repository> GetRepositoryAsync(GetRepositoryRequest request, CallSettings callSettings = null)

Gets a repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::GetRepositoryRequest request = new gcav::GetRepositoryRequest
    {
        RepositoryName = gcav::RepositoryName.FromProjectLocationRepository("[PROJECT]", "[LOCATION]", "[REPOSITORY]"),
    };
    // Make the request
    gcav::Repository response = await artifactRegistryClient.GetRepositoryAsync(request);
    

### GetRepositoryAsync(GetRepositoryRequest, CancellationToken)
    
    
    public virtual Task<Repository> GetRepositoryAsync(GetRepositoryRequest request, CancellationToken cancellationToken)

Gets a repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::GetRepositoryRequest request = new gcav::GetRepositoryRequest
    {
        RepositoryName = gcav::RepositoryName.FromProjectLocationRepository("[PROJECT]", "[LOCATION]", "[REPOSITORY]"),
    };
    // Make the request
    gcav::Repository response = await artifactRegistryClient.GetRepositoryAsync(request);
    

### GetRepositoryAsync(RepositoryName, CallSettings)
    
    
    public virtual Task<Repository> GetRepositoryAsync(RepositoryName name, CallSettings callSettings = null)

Gets a repository.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RepositoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.RepositoryName)`  
Required. The name of the repository to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::RepositoryName name = gcav::RepositoryName.FromProjectLocationRepository("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
    // Make the request
    gcav::Repository response = await artifactRegistryClient.GetRepositoryAsync(name);
    

### GetRepositoryAsync(RepositoryName, CancellationToken)
    
    
    public virtual Task<Repository> GetRepositoryAsync(RepositoryName name, CancellationToken cancellationToken)

Gets a repository.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[RepositoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.RepositoryName)`  
Required. The name of the repository to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::RepositoryName name = gcav::RepositoryName.FromProjectLocationRepository("[PROJECT]", "[LOCATION]", "[REPOSITORY]");
    // Make the request
    gcav::Repository response = await artifactRegistryClient.GetRepositoryAsync(name);
    

### GetRepositoryAsync(string, CallSettings)
    
    
    public virtual Task<Repository> GetRepositoryAsync(string name, CallSettings callSettings = null)

Gets a repository.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the repository to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/repositories/[REPOSITORY]";
    // Make the request
    gcav::Repository response = await artifactRegistryClient.GetRepositoryAsync(name);
    

### GetRepositoryAsync(string, CancellationToken)
    
    
    public virtual Task<Repository> GetRepositoryAsync(string name, CancellationToken cancellationToken)

Gets a repository.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the repository to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/repositories/[REPOSITORY]";
    // Make the request
    gcav::Repository response = await artifactRegistryClient.GetRepositoryAsync(name);
    

### GetTag(GetTagRequest, CallSettings)
    
    
    public virtual Tag GetTag(GetTagRequest request, CallSettings callSettings = null)

Gets a tag.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTagRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetTagRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::GetTagRequest request = new gcav::GetTagRequest { Name = "", };
    // Make the request
    gcav::Tag response = artifactRegistryClient.GetTag(request);
    

### GetTag(string, CallSettings)
    
    
    public virtual Tag GetTag(string name, CallSettings callSettings = null)

Gets a tag.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the tag to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    gcav::Tag response = artifactRegistryClient.GetTag(name);
    

### GetTagAsync(GetTagRequest, CallSettings)
    
    
    public virtual Task<Tag> GetTagAsync(GetTagRequest request, CallSettings callSettings = null)

Gets a tag.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTagRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetTagRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::GetTagRequest request = new gcav::GetTagRequest { Name = "", };
    // Make the request
    gcav::Tag response = await artifactRegistryClient.GetTagAsync(request);
    

### GetTagAsync(GetTagRequest, CancellationToken)
    
    
    public virtual Task<Tag> GetTagAsync(GetTagRequest request, CancellationToken cancellationToken)

Gets a tag.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTagRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetTagRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::GetTagRequest request = new gcav::GetTagRequest { Name = "", };
    // Make the request
    gcav::Tag response = await artifactRegistryClient.GetTagAsync(request);
    

### GetTagAsync(string, CallSettings)
    
    
    public virtual Task<Tag> GetTagAsync(string name, CallSettings callSettings = null)

Gets a tag.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the tag to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    gcav::Tag response = await artifactRegistryClient.GetTagAsync(name);
    

### GetTagAsync(string, CancellationToken)
    
    
    public virtual Task<Tag> GetTagAsync(string name, CancellationToken cancellationToken)

Gets a tag.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the tag to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    gcav::Tag response = await artifactRegistryClient.GetTagAsync(name);
    

### GetVersion(GetVersionRequest, CallSettings)
    
    
    public virtual Version GetVersion(GetVersionRequest request, CallSettings callSettings = null)

Gets a version

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetVersionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Version)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::GetVersionRequest request = new gcav::GetVersionRequest
    {
        Name = "",
        View = gcav::VersionView.Unspecified,
    };
    // Make the request
    gcav::Version response = artifactRegistryClient.GetVersion(request);
    

### GetVersion(string, CallSettings)
    
    
    public virtual Version GetVersion(string name, CallSettings callSettings = null)

Gets a version

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the version to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Version)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    gcav::Version response = artifactRegistryClient.GetVersion(name);
    

### GetVersionAsync(GetVersionRequest, CallSettings)
    
    
    public virtual Task<Version> GetVersionAsync(GetVersionRequest request, CallSettings callSettings = null)

Gets a version

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetVersionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Version)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::GetVersionRequest request = new gcav::GetVersionRequest
    {
        Name = "",
        View = gcav::VersionView.Unspecified,
    };
    // Make the request
    gcav::Version response = await artifactRegistryClient.GetVersionAsync(request);
    

### GetVersionAsync(GetVersionRequest, CancellationToken)
    
    
    public virtual Task<Version> GetVersionAsync(GetVersionRequest request, CancellationToken cancellationToken)

Gets a version

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.GetVersionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Version)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::GetVersionRequest request = new gcav::GetVersionRequest
    {
        Name = "",
        View = gcav::VersionView.Unspecified,
    };
    // Make the request
    gcav::Version response = await artifactRegistryClient.GetVersionAsync(request);
    

### GetVersionAsync(string, CallSettings)
    
    
    public virtual Task<Version> GetVersionAsync(string name, CallSettings callSettings = null)

Gets a version

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the version to retrieve.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Version)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    gcav::Version response = await artifactRegistryClient.GetVersionAsync(name);
    

### GetVersionAsync(string, CancellationToken)
    
    
    public virtual Task<Version> GetVersionAsync(string name, CancellationToken cancellationToken)

Gets a version

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the version to retrieve.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Version)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string name = "";
    // Make the request
    gcav::Version response = await artifactRegistryClient.GetVersionAsync(name);
    

### ImportAptArtifacts(ImportAptArtifactsRequest, CallSettings)
    
    
    public virtual Operation<ImportAptArtifactsResponse, ImportAptArtifactsMetadata> ImportAptArtifacts(ImportAptArtifactsRequest request, CallSettings callSettings = null)

Imports Apt artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportAptArtifactsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportAptArtifactsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAptArtifactsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportAptArtifactsResponse)[ImportAptArtifactsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportAptArtifactsMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::ImportAptArtifactsRequest request = new gcav::ImportAptArtifactsRequest
    {
        Parent = "",
        GcsSource = new gcav::ImportAptArtifactsGcsSource(),
    };
    // Make the request
    Operation<gcav::ImportAptArtifactsResponse, gcav::ImportAptArtifactsMetadata> response = artifactRegistryClient.ImportAptArtifacts(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::ImportAptArtifactsResponse, gcav::ImportAptArtifactsMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcav::ImportAptArtifactsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::ImportAptArtifactsResponse, gcav::ImportAptArtifactsMetadata> retrievedResponse = artifactRegistryClient.PollOnceImportAptArtifacts(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::ImportAptArtifactsResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportAptArtifactsAsync(ImportAptArtifactsRequest, CallSettings)
    
    
    public virtual Task<Operation<ImportAptArtifactsResponse, ImportAptArtifactsMetadata>> ImportAptArtifactsAsync(ImportAptArtifactsRequest request, CallSettings callSettings = null)

Imports Apt artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportAptArtifactsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportAptArtifactsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAptArtifactsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportAptArtifactsResponse)[ImportAptArtifactsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportAptArtifactsMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::ImportAptArtifactsRequest request = new gcav::ImportAptArtifactsRequest
    {
        Parent = "",
        GcsSource = new gcav::ImportAptArtifactsGcsSource(),
    };
    // Make the request
    Operation<gcav::ImportAptArtifactsResponse, gcav::ImportAptArtifactsMetadata> response = await artifactRegistryClient.ImportAptArtifactsAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::ImportAptArtifactsResponse, gcav::ImportAptArtifactsMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcav::ImportAptArtifactsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::ImportAptArtifactsResponse, gcav::ImportAptArtifactsMetadata> retrievedResponse = await artifactRegistryClient.PollOnceImportAptArtifactsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::ImportAptArtifactsResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportAptArtifactsAsync(ImportAptArtifactsRequest, CancellationToken)
    
    
    public virtual Task<Operation<ImportAptArtifactsResponse, ImportAptArtifactsMetadata>> ImportAptArtifactsAsync(ImportAptArtifactsRequest request, CancellationToken cancellationToken)

Imports Apt artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportAptArtifactsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportAptArtifactsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAptArtifactsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportAptArtifactsResponse)[ImportAptArtifactsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportAptArtifactsMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::ImportAptArtifactsRequest request = new gcav::ImportAptArtifactsRequest
    {
        Parent = "",
        GcsSource = new gcav::ImportAptArtifactsGcsSource(),
    };
    // Make the request
    Operation<gcav::ImportAptArtifactsResponse, gcav::ImportAptArtifactsMetadata> response = await artifactRegistryClient.ImportAptArtifactsAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::ImportAptArtifactsResponse, gcav::ImportAptArtifactsMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcav::ImportAptArtifactsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::ImportAptArtifactsResponse, gcav::ImportAptArtifactsMetadata> retrievedResponse = await artifactRegistryClient.PollOnceImportAptArtifactsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::ImportAptArtifactsResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportYumArtifacts(ImportYumArtifactsRequest, CallSettings)
    
    
    public virtual Operation<ImportYumArtifactsResponse, ImportYumArtifactsMetadata> ImportYumArtifacts(ImportYumArtifactsRequest request, CallSettings callSettings = null)

Imports Yum (RPM) artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportYumArtifactsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportYumArtifactsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsResponse)[ImportYumArtifactsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::ImportYumArtifactsRequest request = new gcav::ImportYumArtifactsRequest
    {
        Parent = "",
        GcsSource = new gcav::ImportYumArtifactsGcsSource(),
    };
    // Make the request
    Operation<gcav::ImportYumArtifactsResponse, gcav::ImportYumArtifactsMetadata> response = artifactRegistryClient.ImportYumArtifacts(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::ImportYumArtifactsResponse, gcav::ImportYumArtifactsMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    gcav::ImportYumArtifactsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::ImportYumArtifactsResponse, gcav::ImportYumArtifactsMetadata> retrievedResponse = artifactRegistryClient.PollOnceImportYumArtifacts(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::ImportYumArtifactsResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportYumArtifactsAsync(ImportYumArtifactsRequest, CallSettings)
    
    
    public virtual Task<Operation<ImportYumArtifactsResponse, ImportYumArtifactsMetadata>> ImportYumArtifactsAsync(ImportYumArtifactsRequest request, CallSettings callSettings = null)

Imports Yum (RPM) artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportYumArtifactsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportYumArtifactsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsResponse)[ImportYumArtifactsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::ImportYumArtifactsRequest request = new gcav::ImportYumArtifactsRequest
    {
        Parent = "",
        GcsSource = new gcav::ImportYumArtifactsGcsSource(),
    };
    // Make the request
    Operation<gcav::ImportYumArtifactsResponse, gcav::ImportYumArtifactsMetadata> response = await artifactRegistryClient.ImportYumArtifactsAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::ImportYumArtifactsResponse, gcav::ImportYumArtifactsMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcav::ImportYumArtifactsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::ImportYumArtifactsResponse, gcav::ImportYumArtifactsMetadata> retrievedResponse = await artifactRegistryClient.PollOnceImportYumArtifactsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::ImportYumArtifactsResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportYumArtifactsAsync(ImportYumArtifactsRequest, CancellationToken)
    
    
    public virtual Task<Operation<ImportYumArtifactsResponse, ImportYumArtifactsMetadata>> ImportYumArtifactsAsync(ImportYumArtifactsRequest request, CancellationToken cancellationToken)

Imports Yum (RPM) artifacts. The returned Operation will complete once the resources are imported. Package, Version, and File resources are created based on the imported artifacts. Imported artifacts that conflict with existing resources are ignored.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportYumArtifactsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportYumArtifactsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsResponse)[ImportYumArtifactsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::ImportYumArtifactsRequest request = new gcav::ImportYumArtifactsRequest
    {
        Parent = "",
        GcsSource = new gcav::ImportYumArtifactsGcsSource(),
    };
    // Make the request
    Operation<gcav::ImportYumArtifactsResponse, gcav::ImportYumArtifactsMetadata> response = await artifactRegistryClient.ImportYumArtifactsAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<gcav::ImportYumArtifactsResponse, gcav::ImportYumArtifactsMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    gcav::ImportYumArtifactsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<gcav::ImportYumArtifactsResponse, gcav::ImportYumArtifactsMetadata> retrievedResponse = await artifactRegistryClient.PollOnceImportYumArtifactsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        gcav::ImportYumArtifactsResponse retrievedResult = retrievedResponse.Result;
    }
    

### ListFiles(ListFilesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListFilesResponse, File> ListFiles(ListFilesRequest request, CallSettings callSettings = null)

Lists files.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListFilesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListFilesResponse)[File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.File)` | A pageable sequence of [File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.File) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::ListFilesRequest request = new gcav::ListFilesRequest
    {
        Parent = "",
        Filter = "",
    };
    // Make the request
    PagedEnumerable<gcav::ListFilesResponse, gcav::File> response = artifactRegistryClient.ListFiles(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcav::File item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcav::ListFilesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::File item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::File> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::File item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFiles(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListFilesResponse, File> ListFiles(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists files.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the repository whose files will be listed. For example: "projects/p1/locations/us-central1/repositories/repo1  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListFilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListFilesResponse)[File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.File)` | A pageable sequence of [File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.File) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    string parent = "";
    // Make the request
    PagedEnumerable<gcav::ListFilesResponse, gcav::File> response = artifactRegistryClient.ListFiles(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcav::File item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcav::ListFilesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::File item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::File> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::File item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFilesAsync(ListFilesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFilesResponse, File> ListFilesAsync(ListFilesRequest request, CallSettings callSettings = null)

Lists files.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFilesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListFilesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListFilesResponse)[File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.File)` | A pageable asynchronous sequence of [File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.File) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::ListFilesRequest request = new gcav::ListFilesRequest
    {
        Parent = "",
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<gcav::ListFilesResponse, gcav::File> response = artifactRegistryClient.ListFilesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcav::File item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcav::ListFilesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::File item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::File> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::File item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListFilesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListFilesResponse, File> ListFilesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists files.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the repository whose files will be listed. For example: "projects/p1/locations/us-central1/repositories/repo1  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListFilesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListFilesResponse)[File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.File)` | A pageable asynchronous sequence of [File](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.File) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "";
    // Make the request
    PagedAsyncEnumerable<gcav::ListFilesResponse, gcav::File> response = artifactRegistryClient.ListFilesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcav::File item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcav::ListFilesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::File item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::File> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::File item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListPackages(ListPackagesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListPackagesResponse, Package> ListPackages(ListPackagesRequest request, CallSettings callSettings = null)

Lists packages.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPackagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListPackagesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListPackagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListPackagesResponse)[Package](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Package)` | A pageable sequence of [Package](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Package) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::ListPackagesRequest request = new gcav::ListPackagesRequest { Parent = "", };
    // Make the request
    PagedEnumerable<gcav::ListPackagesResponse, gcav::Package> response = artifactRegistryClient.ListPackages(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcav::Package item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcav::ListPackagesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::Package item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::Package> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::Package item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListPackages(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListPackagesResponse, Package> ListPackages(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists packages.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the parent resource whose packages will be listed.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListPackagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListPackagesResponse)[Package](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Package)` | A pageable sequence of [Package](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Package) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    string parent = "";
    // Make the request
    PagedEnumerable<gcav::ListPackagesResponse, gcav::Package> response = artifactRegistryClient.ListPackages(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcav::Package item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcav::ListPackagesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::Package item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::Package> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::Package item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListPackagesAsync(ListPackagesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListPackagesResponse, Package> ListPackagesAsync(ListPackagesRequest request, CallSettings callSettings = null)

Lists packages.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPackagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListPackagesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListPackagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListPackagesResponse)[Package](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Package)` | A pageable asynchronous sequence of [Package](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Package) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::ListPackagesRequest request = new gcav::ListPackagesRequest { Parent = "", };
    // Make the request
    PagedAsyncEnumerable<gcav::ListPackagesResponse, gcav::Package> response = artifactRegistryClient.ListPackagesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcav::Package item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcav::ListPackagesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::Package item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::Package> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::Package item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListPackagesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListPackagesResponse, Package> ListPackagesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists packages.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the parent resource whose packages will be listed.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListPackagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListPackagesResponse)[Package](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Package)` | A pageable asynchronous sequence of [Package](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Package) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "";
    // Make the request
    PagedAsyncEnumerable<gcav::ListPackagesResponse, gcav::Package> response = artifactRegistryClient.ListPackagesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcav::Package item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcav::ListPackagesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::Package item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::Package> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::Package item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRepositories(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListRepositoriesResponse, Repository> ListRepositories(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists repositories.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the parent resource whose repositories will be listed.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListRepositoriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListRepositoriesResponse)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | A pageable sequence of [Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<gcav::ListRepositoriesResponse, gcav::Repository> response = artifactRegistryClient.ListRepositories(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcav::Repository item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcav::ListRepositoriesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::Repository item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::Repository> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::Repository item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRepositories(ListRepositoriesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListRepositoriesResponse, Repository> ListRepositories(ListRepositoriesRequest request, CallSettings callSettings = null)

Lists repositories.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRepositoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListRepositoriesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListRepositoriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListRepositoriesResponse)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | A pageable sequence of [Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::ListRepositoriesRequest request = new gcav::ListRepositoriesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedEnumerable<gcav::ListRepositoriesResponse, gcav::Repository> response = artifactRegistryClient.ListRepositories(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcav::Repository item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcav::ListRepositoriesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::Repository item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::Repository> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::Repository item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRepositories(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListRepositoriesResponse, Repository> ListRepositories(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists repositories.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource whose repositories will be listed.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListRepositoriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListRepositoriesResponse)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | A pageable sequence of [Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<gcav::ListRepositoriesResponse, gcav::Repository> response = artifactRegistryClient.ListRepositories(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcav::Repository item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcav::ListRepositoriesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::Repository item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::Repository> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::Repository item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRepositoriesAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListRepositoriesResponse, Repository> ListRepositoriesAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists repositories.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The name of the parent resource whose repositories will be listed.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListRepositoriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListRepositoriesResponse)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | A pageable asynchronous sequence of [Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<gcav::ListRepositoriesResponse, gcav::Repository> response = artifactRegistryClient.ListRepositoriesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcav::Repository item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcav::ListRepositoriesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::Repository item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::Repository> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::Repository item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRepositoriesAsync(ListRepositoriesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListRepositoriesResponse, Repository> ListRepositoriesAsync(ListRepositoriesRequest request, CallSettings callSettings = null)

Lists repositories.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRepositoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListRepositoriesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListRepositoriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListRepositoriesResponse)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | A pageable asynchronous sequence of [Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::ListRepositoriesRequest request = new gcav::ListRepositoriesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedAsyncEnumerable<gcav::ListRepositoriesResponse, gcav::Repository> response = artifactRegistryClient.ListRepositoriesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcav::Repository item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcav::ListRepositoriesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::Repository item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::Repository> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::Repository item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListRepositoriesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListRepositoriesResponse, Repository> ListRepositoriesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists repositories.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the parent resource whose repositories will be listed.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListRepositoriesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListRepositoriesResponse)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | A pageable asynchronous sequence of [Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<gcav::ListRepositoriesResponse, gcav::Repository> response = artifactRegistryClient.ListRepositoriesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcav::Repository item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcav::ListRepositoriesResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::Repository item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::Repository> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::Repository item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTags(ListTagsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListTagsResponse, Tag> ListTags(ListTagsRequest request, CallSettings callSettings = null)

Lists tags.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTagsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListTagsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListTagsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListTagsResponse)[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | A pageable sequence of [Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::ListTagsRequest request = new gcav::ListTagsRequest
    {
        Parent = "",
        Filter = "",
    };
    // Make the request
    PagedEnumerable<gcav::ListTagsResponse, gcav::Tag> response = artifactRegistryClient.ListTags(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcav::Tag item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcav::ListTagsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::Tag item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::Tag> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::Tag item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTags(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListTagsResponse, Tag> ListTags(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists tags.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the parent resource whose tags will be listed.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListTagsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListTagsResponse)[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | A pageable sequence of [Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    string parent = "";
    // Make the request
    PagedEnumerable<gcav::ListTagsResponse, gcav::Tag> response = artifactRegistryClient.ListTags(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcav::Tag item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcav::ListTagsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::Tag item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::Tag> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::Tag item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTagsAsync(ListTagsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListTagsResponse, Tag> ListTagsAsync(ListTagsRequest request, CallSettings callSettings = null)

Lists tags.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTagsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListTagsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListTagsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListTagsResponse)[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | A pageable asynchronous sequence of [Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::ListTagsRequest request = new gcav::ListTagsRequest
    {
        Parent = "",
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<gcav::ListTagsResponse, gcav::Tag> response = artifactRegistryClient.ListTagsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcav::Tag item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcav::ListTagsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::Tag item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::Tag> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::Tag item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTagsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListTagsResponse, Tag> ListTagsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists tags.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the parent resource whose tags will be listed.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListTagsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListTagsResponse)[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | A pageable asynchronous sequence of [Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "";
    // Make the request
    PagedAsyncEnumerable<gcav::ListTagsResponse, gcav::Tag> response = artifactRegistryClient.ListTagsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcav::Tag item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcav::ListTagsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::Tag item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::Tag> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::Tag item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListVersions(ListVersionsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListVersionsResponse, Version> ListVersions(ListVersionsRequest request, CallSettings callSettings = null)

Lists versions.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListVersionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListVersionsResponse)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Version)` | A pageable sequence of [Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Version) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::ListVersionsRequest request = new gcav::ListVersionsRequest
    {
        Parent = "",
        View = gcav::VersionView.Unspecified,
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<gcav::ListVersionsResponse, gcav::Version> response = artifactRegistryClient.ListVersions(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcav::Version item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcav::ListVersionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::Version item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::Version> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::Version item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListVersions(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListVersionsResponse, Version> ListVersions(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists versions.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the parent resource whose versions will be listed.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListVersionsResponse)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Version)` | A pageable sequence of [Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Version) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    string parent = "";
    // Make the request
    PagedEnumerable<gcav::ListVersionsResponse, gcav::Version> response = artifactRegistryClient.ListVersions(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (gcav::Version item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (gcav::ListVersionsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::Version item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::Version> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::Version item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListVersionsAsync(ListVersionsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListVersionsResponse, Version> ListVersionsAsync(ListVersionsRequest request, CallSettings callSettings = null)

Lists versions.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListVersionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListVersionsResponse)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Version)` | A pageable asynchronous sequence of [Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Version) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::ListVersionsRequest request = new gcav::ListVersionsRequest
    {
        Parent = "",
        View = gcav::VersionView.Unspecified,
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<gcav::ListVersionsResponse, gcav::Version> response = artifactRegistryClient.ListVersionsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcav::Version item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcav::ListVersionsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::Version item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::Version> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::Version item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListVersionsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListVersionsResponse, Version> ListVersionsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists versions.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the parent resource whose versions will be listed.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ListVersionsResponse)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Version)` | A pageable asynchronous sequence of [Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Version) resources.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "";
    // Make the request
    PagedAsyncEnumerable<gcav::ListVersionsResponse, gcav::Version> response = artifactRegistryClient.ListVersionsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((gcav::Version item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((gcav::ListVersionsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (gcav::Version item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<gcav::Version> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (gcav::Version item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceCreateRepository(string, CallSettings)
    
    
    public virtual Operation<Repository, OperationMetadata> PollOnceCreateRepository(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateRepository`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateRepositoryAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Repository, OperationMetadata>> PollOnceCreateRepositoryAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateRepository`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeletePackage(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeletePackage(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeletePackage`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeletePackageAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeletePackageAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeletePackage`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteRepository(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteRepository(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteRepository`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteRepositoryAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteRepositoryAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteRepository`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteVersion(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteVersion(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteVersion`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteVersionAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteVersionAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteVersion`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceImportAptArtifacts(string, CallSettings)
    
    
    public virtual Operation<ImportAptArtifactsResponse, ImportAptArtifactsMetadata> PollOnceImportAptArtifacts(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `ImportAptArtifacts` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAptArtifactsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportAptArtifactsResponse)[ImportAptArtifactsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportAptArtifactsMetadata)` | The result of polling the operation.  
  
### PollOnceImportAptArtifactsAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ImportAptArtifactsResponse, ImportAptArtifactsMetadata>> PollOnceImportAptArtifactsAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `ImportAptArtifacts`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportAptArtifactsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportAptArtifactsResponse)[ImportAptArtifactsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportAptArtifactsMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceImportYumArtifacts(string, CallSettings)
    
    
    public virtual Operation<ImportYumArtifactsResponse, ImportYumArtifactsMetadata> PollOnceImportYumArtifacts(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `ImportYumArtifacts` .

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportYumArtifactsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsResponse)[ImportYumArtifactsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsMetadata)` | The result of polling the operation.  
  
### PollOnceImportYumArtifactsAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ImportYumArtifactsResponse, ImportYumArtifactsMetadata>> PollOnceImportYumArtifactsAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `ImportYumArtifacts`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportYumArtifactsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsResponse)[ImportYumArtifactsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsMetadata)` | A task representing the result of polling the operation.  
  
### SetIamPolicy(SetIamPolicyRequest, CallSettings)
    
    
    public virtual Policy SetIamPolicy(SetIamPolicyRequest request, CallSettings callSettings = null)

Updates the IAM policy for a given resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    SetIamPolicyRequest request = new SetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Policy = new Policy(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Policy response = artifactRegistryClient.SetIamPolicy(request);
    

### SetIamPolicyAsync(SetIamPolicyRequest, CallSettings)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(SetIamPolicyRequest request, CallSettings callSettings = null)

Updates the IAM policy for a given resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    SetIamPolicyRequest request = new SetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Policy = new Policy(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Policy response = await artifactRegistryClient.SetIamPolicyAsync(request);
    

### SetIamPolicyAsync(SetIamPolicyRequest, CancellationToken)
    
    
    public virtual Task<Policy> SetIamPolicyAsync(SetIamPolicyRequest request, CancellationToken cancellationToken)

Updates the IAM policy for a given resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    SetIamPolicyRequest request = new SetIamPolicyRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Policy = new Policy(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Policy response = await artifactRegistryClient.SetIamPolicyAsync(request);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClient#Google_Cloud_ArtifactRegistry_V1Beta2_ArtifactRegistryClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClient#Google_Cloud_ArtifactRegistry_V1Beta2_ArtifactRegistryClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClient#Google_Cloud_ArtifactRegistry_V1Beta2_ArtifactRegistryClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ArtifactRegistryClient#Google_Cloud_ArtifactRegistry_V1Beta2_ArtifactRegistryClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### TestIamPermissions(TestIamPermissionsRequest, CallSettings)
    
    
    public virtual TestIamPermissionsResponse TestIamPermissions(TestIamPermissionsRequest request, CallSettings callSettings = null)

Tests if the caller has a list of permissions on a resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    TestIamPermissionsRequest request = new TestIamPermissionsRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Permissions = { "", },
    };
    // Make the request
    TestIamPermissionsResponse response = artifactRegistryClient.TestIamPermissions(request);
    

### TestIamPermissionsAsync(TestIamPermissionsRequest, CallSettings)
    
    
    public virtual Task<TestIamPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsRequest request, CallSettings callSettings = null)

Tests if the caller has a list of permissions on a resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    TestIamPermissionsRequest request = new TestIamPermissionsRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Permissions = { "", },
    };
    // Make the request
    TestIamPermissionsResponse response = await artifactRegistryClient.TestIamPermissionsAsync(request);
    

### TestIamPermissionsAsync(TestIamPermissionsRequest, CancellationToken)
    
    
    public virtual Task<TestIamPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsRequest request, CancellationToken cancellationToken)

Tests if the caller has a list of permissions on a resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    TestIamPermissionsRequest request = new TestIamPermissionsRequest
    {
        ResourceAsResourceName = new UnparsedResourceName("a/wildcard/resource"),
        Permissions = { "", },
    };
    // Make the request
    TestIamPermissionsResponse response = await artifactRegistryClient.TestIamPermissionsAsync(request);
    

### UpdateProjectSettings(ProjectSettings, FieldMask, CallSettings)
    
    
    public virtual ProjectSettings UpdateProjectSettings(ProjectSettings projectSettings, FieldMask updateMask, CallSettings callSettings = null)

Updates the Settings for the Project.

**Parameters**  
---  
**Name** | **Description**  
`projectSettings` | `[ProjectSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings)`  
The project settings.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask to support partial updates.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ProjectSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::ProjectSettings projectSettings = new gcav::ProjectSettings();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcav::ProjectSettings response = artifactRegistryClient.UpdateProjectSettings(projectSettings, updateMask);
    

### UpdateProjectSettings(UpdateProjectSettingsRequest, CallSettings)
    
    
    public virtual ProjectSettings UpdateProjectSettings(UpdateProjectSettingsRequest request, CallSettings callSettings = null)

Updates the Settings for the Project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProjectSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.UpdateProjectSettingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ProjectSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::UpdateProjectSettingsRequest request = new gcav::UpdateProjectSettingsRequest
    {
        ProjectSettings = new gcav::ProjectSettings(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcav::ProjectSettings response = artifactRegistryClient.UpdateProjectSettings(request);
    

### UpdateProjectSettingsAsync(ProjectSettings, FieldMask, CallSettings)
    
    
    public virtual Task<ProjectSettings> UpdateProjectSettingsAsync(ProjectSettings projectSettings, FieldMask updateMask, CallSettings callSettings = null)

Updates the Settings for the Project.

**Parameters**  
---  
**Name** | **Description**  
`projectSettings` | `[ProjectSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings)`  
The project settings.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask to support partial updates.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ProjectSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::ProjectSettings projectSettings = new gcav::ProjectSettings();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcav::ProjectSettings response = await artifactRegistryClient.UpdateProjectSettingsAsync(projectSettings, updateMask);
    

### UpdateProjectSettingsAsync(ProjectSettings, FieldMask, CancellationToken)
    
    
    public virtual Task<ProjectSettings> UpdateProjectSettingsAsync(ProjectSettings projectSettings, FieldMask updateMask, CancellationToken cancellationToken)

Updates the Settings for the Project.

**Parameters**  
---  
**Name** | **Description**  
`projectSettings` | `[ProjectSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings)`  
The project settings.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Field mask to support partial updates.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ProjectSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::ProjectSettings projectSettings = new gcav::ProjectSettings();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcav::ProjectSettings response = await artifactRegistryClient.UpdateProjectSettingsAsync(projectSettings, updateMask);
    

### UpdateProjectSettingsAsync(UpdateProjectSettingsRequest, CallSettings)
    
    
    public virtual Task<ProjectSettings> UpdateProjectSettingsAsync(UpdateProjectSettingsRequest request, CallSettings callSettings = null)

Updates the Settings for the Project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProjectSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.UpdateProjectSettingsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ProjectSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::UpdateProjectSettingsRequest request = new gcav::UpdateProjectSettingsRequest
    {
        ProjectSettings = new gcav::ProjectSettings(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcav::ProjectSettings response = await artifactRegistryClient.UpdateProjectSettingsAsync(request);
    

### UpdateProjectSettingsAsync(UpdateProjectSettingsRequest, CancellationToken)
    
    
    public virtual Task<ProjectSettings> UpdateProjectSettingsAsync(UpdateProjectSettingsRequest request, CancellationToken cancellationToken)

Updates the Settings for the Project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateProjectSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.UpdateProjectSettingsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ProjectSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ProjectSettings)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::UpdateProjectSettingsRequest request = new gcav::UpdateProjectSettingsRequest
    {
        ProjectSettings = new gcav::ProjectSettings(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcav::ProjectSettings response = await artifactRegistryClient.UpdateProjectSettingsAsync(request);
    

### UpdateRepository(Repository, FieldMask, CallSettings)
    
    
    public virtual Repository UpdateRepository(Repository repository, FieldMask updateMask, CallSettings callSettings = null)

Updates a repository.

**Parameters**  
---  
**Name** | **Description**  
`repository` | `[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)`  
The repository that replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::Repository repository = new gcav::Repository();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcav::Repository response = artifactRegistryClient.UpdateRepository(repository, updateMask);
    

### UpdateRepository(UpdateRepositoryRequest, CallSettings)
    
    
    public virtual Repository UpdateRepository(UpdateRepositoryRequest request, CallSettings callSettings = null)

Updates a repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.UpdateRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::UpdateRepositoryRequest request = new gcav::UpdateRepositoryRequest
    {
        Repository = new gcav::Repository(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcav::Repository response = artifactRegistryClient.UpdateRepository(request);
    

### UpdateRepositoryAsync(Repository, FieldMask, CallSettings)
    
    
    public virtual Task<Repository> UpdateRepositoryAsync(Repository repository, FieldMask updateMask, CallSettings callSettings = null)

Updates a repository.

**Parameters**  
---  
**Name** | **Description**  
`repository` | `[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)`  
The repository that replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::Repository repository = new gcav::Repository();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcav::Repository response = await artifactRegistryClient.UpdateRepositoryAsync(repository, updateMask);
    

### UpdateRepositoryAsync(Repository, FieldMask, CancellationToken)
    
    
    public virtual Task<Repository> UpdateRepositoryAsync(Repository repository, FieldMask updateMask, CancellationToken cancellationToken)

Updates a repository.

**Parameters**  
---  
**Name** | **Description**  
`repository` | `[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)`  
The repository that replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::Repository repository = new gcav::Repository();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcav::Repository response = await artifactRegistryClient.UpdateRepositoryAsync(repository, updateMask);
    

### UpdateRepositoryAsync(UpdateRepositoryRequest, CallSettings)
    
    
    public virtual Task<Repository> UpdateRepositoryAsync(UpdateRepositoryRequest request, CallSettings callSettings = null)

Updates a repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.UpdateRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::UpdateRepositoryRequest request = new gcav::UpdateRepositoryRequest
    {
        Repository = new gcav::Repository(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcav::Repository response = await artifactRegistryClient.UpdateRepositoryAsync(request);
    

### UpdateRepositoryAsync(UpdateRepositoryRequest, CancellationToken)
    
    
    public virtual Task<Repository> UpdateRepositoryAsync(UpdateRepositoryRequest request, CancellationToken cancellationToken)

Updates a repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.UpdateRepositoryRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Repository](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Repository)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::UpdateRepositoryRequest request = new gcav::UpdateRepositoryRequest
    {
        Repository = new gcav::Repository(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcav::Repository response = await artifactRegistryClient.UpdateRepositoryAsync(request);
    

### UpdateTag(Tag, FieldMask, CallSettings)
    
    
    public virtual Tag UpdateTag(Tag tag, FieldMask updateMask, CallSettings callSettings = null)

Updates a tag.

**Parameters**  
---  
**Name** | **Description**  
`tag` | `[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)`  
The tag that replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::Tag tag = new gcav::Tag();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcav::Tag response = artifactRegistryClient.UpdateTag(tag, updateMask);
    

### UpdateTag(UpdateTagRequest, CallSettings)
    
    
    public virtual Tag UpdateTag(UpdateTagRequest request, CallSettings callSettings = null)

Updates a tag.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTagRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.UpdateTagRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | The RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = gcav::ArtifactRegistryClient.Create();
    // Initialize request argument(s)
    gcav::UpdateTagRequest request = new gcav::UpdateTagRequest
    {
        Tag = new gcav::Tag(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcav::Tag response = artifactRegistryClient.UpdateTag(request);
    

### UpdateTagAsync(Tag, FieldMask, CallSettings)
    
    
    public virtual Task<Tag> UpdateTagAsync(Tag tag, FieldMask updateMask, CallSettings callSettings = null)

Updates a tag.

**Parameters**  
---  
**Name** | **Description**  
`tag` | `[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)`  
The tag that replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::Tag tag = new gcav::Tag();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcav::Tag response = await artifactRegistryClient.UpdateTagAsync(tag, updateMask);
    

### UpdateTagAsync(Tag, FieldMask, CancellationToken)
    
    
    public virtual Task<Tag> UpdateTagAsync(Tag tag, FieldMask updateMask, CancellationToken cancellationToken)

Updates a tag.

**Parameters**  
---  
**Name** | **Description**  
`tag` | `[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)`  
The tag that replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::Tag tag = new gcav::Tag();
    FieldMask updateMask = new FieldMask();
    // Make the request
    gcav::Tag response = await artifactRegistryClient.UpdateTagAsync(tag, updateMask);
    

### UpdateTagAsync(UpdateTagRequest, CallSettings)
    
    
    public virtual Task<Tag> UpdateTagAsync(UpdateTagRequest request, CallSettings callSettings = null)

Updates a tag.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTagRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.UpdateTagRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::UpdateTagRequest request = new gcav::UpdateTagRequest
    {
        Tag = new gcav::Tag(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcav::Tag response = await artifactRegistryClient.UpdateTagAsync(request);
    

### UpdateTagAsync(UpdateTagRequest, CancellationToken)
    
    
    public virtual Task<Tag> UpdateTagAsync(UpdateTagRequest request, CancellationToken cancellationToken)

Updates a tag.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTagRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.UpdateTagRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.Tag)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcav::ArtifactRegistryClient artifactRegistryClient = await gcav::ArtifactRegistryClient.CreateAsync();
    // Initialize request argument(s)
    gcav::UpdateTagRequest request = new gcav::UpdateTagRequest
    {
        Tag = new gcav::Tag(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    gcav::Tag response = await artifactRegistryClient.UpdateTagAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
